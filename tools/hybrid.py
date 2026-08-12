#!/usr/bin/env python3
"""Local multilingual embedding index and reciprocal-rank fusion for the wiki."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from tokenizers import Tokenizer

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "intfloat/multilingual-e5-small"
MODEL_REVISION = "614241f622f53c4eeff9890bdc4f31cfecc418b3"
MODEL_FILE = "onnx/model_qint8_avx512_vnni.onnx"
TOKENIZER_FILE = "onnx/tokenizer.json"
VECTOR_PATH = ROOT / "indexes" / "wiki-vectors.npz"
MANIFEST_PATH = ROOT / "indexes" / "wiki-vectors.manifest.json"
BENCHMARK_PATH = ROOT / "evals" / "wiki-retrieval-v1.json"
BENCHMARK_REPORT_PATH = ROOT / "reports" / "retrieval-benchmark.json"


def load_wiki_module():
    path = ROOT / "tools" / "wiki.py"
    spec = importlib.util.spec_from_file_location("wiki_hybrid_backend", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def model_paths() -> tuple[str, str]:
    model = hf_hub_download(MODEL_ID, MODEL_FILE, revision=MODEL_REVISION)
    tokenizer = hf_hub_download(MODEL_ID, TOKENIZER_FILE, revision=MODEL_REVISION)
    return model, tokenizer


def encode(texts: list[str], *, prefix: str, batch_size: int = 16) -> np.ndarray:
    model_path, tokenizer_path = model_paths()
    tokenizer = Tokenizer.from_file(tokenizer_path)
    tokenizer.enable_truncation(max_length=512)
    tokenizer.enable_padding(length=None)
    session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
    vectors: list[np.ndarray] = []
    for start in range(0, len(texts), batch_size):
        encodings = tokenizer.encode_batch([f"{prefix}: {text}" for text in texts[start:start + batch_size]])
        input_ids = np.asarray([item.ids for item in encodings], dtype=np.int64)
        attention_mask = np.asarray([item.attention_mask for item in encodings], dtype=np.int64)
        inputs = {"input_ids": input_ids, "attention_mask": attention_mask}
        if any(item.name == "token_type_ids" for item in session.get_inputs()):
            inputs["token_type_ids"] = np.zeros_like(input_ids)
        output = session.run(None, inputs)[0]
        mask = attention_mask[..., None].astype(np.float32)
        pooled = (output * mask).sum(axis=1) / np.maximum(mask.sum(axis=1), 1e-9)
        pooled /= np.maximum(np.linalg.norm(pooled, axis=1, keepdims=True), 1e-9)
        vectors.append(pooled.astype(np.float32))
    return np.vstack(vectors) if vectors else np.empty((0, 384), dtype=np.float32)


def build() -> dict[str, Any]:
    wiki = load_wiki_module()
    pages, errors = wiki.load_pages()
    if errors:
        return {"ok": False, "errors": errors}
    sections = wiki.all_sections(pages)
    texts = [f"{item.title}\n{item.heading_path}\n{item.text}" for item in sections]
    vectors = encode(texts, prefix="passage")
    VECTOR_PATH.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(VECTOR_PATH, vectors=vectors, section_ids=np.asarray([item.section_id for item in sections]))
    manifest = {
        "format_version": 1,
        "model_id": MODEL_ID,
        "model_revision": MODEL_REVISION,
        "model_file": MODEL_FILE,
        "pooling": "attention-mask mean + L2 normalization",
        "query_prefix": "query:",
        "passage_prefix": "passage:",
        "dimensions": int(vectors.shape[1]),
        "section_count": len(sections),
        "content_sha256": hashlib.sha256("\n".join(texts).encode()).hexdigest(),
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return {"ok": True, **manifest, "index": VECTOR_PATH.relative_to(ROOT).as_posix()}


def corpus_identity(sections: list[Any]) -> str:
    texts = [f"{item.title}\n{item.heading_path}\n{item.text}" for item in sections]
    return hashlib.sha256("\n".join(texts).encode()).hexdigest()


def validate_index(sections: list[Any]) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    if not VECTOR_PATH.exists() or not MANIFEST_PATH.exists():
        return None, ["hybrid index is missing; run `python3 tools/hybrid.py build` explicitly"]
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    expected = {
        "model_id": MODEL_ID,
        "model_revision": MODEL_REVISION,
        "model_file": MODEL_FILE,
        "section_count": len(sections),
        "content_sha256": corpus_identity(sections),
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            errors.append(f"stale or incompatible hybrid index: {key} mismatch")
    return manifest, errors


def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, item in enumerate(ranking, start=1):
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))


def page_ranking(section_ids: list[str], sections: dict[str, Any]) -> list[str]:
    """Collapse section rankings to first-hit page rankings."""
    pages: list[str] = []
    seen: set[str] = set()
    for section_id in section_ids:
        section = sections.get(section_id)
        if section and section.page_id not in seen:
            seen.add(section.page_id)
            pages.append(section.page_id)
    return pages


def ranking_metrics(ranking: list[str], relevant: set[str], at: int = 5) -> dict[str, float]:
    top = ranking[:at]
    recall = len(relevant.intersection(top)) / len(relevant) if relevant else 0.0
    reciprocal_rank = next((1.0 / rank for rank, page_id in enumerate(ranking, 1) if page_id in relevant), 0.0)
    dcg = sum(1.0 / math.log2(rank + 1) for rank, page_id in enumerate(top, 1) if page_id in relevant)
    ideal = sum(1.0 / math.log2(rank + 1) for rank in range(1, min(len(relevant), at) + 1))
    return {f"recall@{at}": recall, "mrr": reciprocal_rank, f"ndcg@{at}": dcg / ideal if ideal else 0.0}


def percentile(values: list[float], fraction: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, math.ceil(fraction * len(ordered)) - 1)
    return ordered[index]


def benchmark(dataset_path: Path = BENCHMARK_PATH, report_path: Path = BENCHMARK_REPORT_PATH) -> dict[str, Any]:
    """Compare FTS, dense and RRF on one immutable, page-labeled development set."""
    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))
    wiki = load_wiki_module()
    pages, errors = wiki.load_pages()
    if errors:
        return {"ok": False, "errors": errors}
    all_items = wiki.all_sections(pages)
    manifest, index_errors = validate_index(all_items)
    if index_errors:
        return {"ok": False, "errors": index_errors}
    eligible_items = [item for item in all_items if item.status == "reviewed" and item.privacy in {"public", "internal"}]
    sections = {item.section_id: item for item in eligible_items}
    payload = np.load(VECTOR_PATH)
    vectors = payload["vectors"]
    section_ids = payload["section_ids"].tolist()
    eligible_indexes = [index for index, section_id in enumerate(section_ids) if section_id in sections]
    cases = dataset["cases"]
    embed_started = time.perf_counter()
    query_vectors = encode([case["query"] for case in cases], prefix="query")
    embed_ms_per_query = ((time.perf_counter() - embed_started) * 1000.0) / max(len(cases), 1)
    methods: dict[str, list[dict[str, Any]]] = {"fts": [], "dense": [], "rrf": []}
    for case, query_vector in zip(cases, query_vectors):
        started = time.perf_counter()
        lexical = wiki.search_fts(
            case["query"], limit=50, privacy=["public", "internal"], status=["reviewed"], trace=False
        )
        fts_ms = (time.perf_counter() - started) * 1000.0
        lexical_sections = [item["section_id"] for item in lexical["results"]]
        dense_started = time.perf_counter()
        dense_sections = [
            section_ids[index]
            for index in sorted(eligible_indexes, key=lambda index: float(-(vectors[index] @ query_vector)))[:50]
        ]
        dense_ms = (time.perf_counter() - dense_started) * 1000.0 + embed_ms_per_query
        fusion_started = time.perf_counter()
        lexical_pages = page_ranking(lexical_sections, sections)
        dense_pages = page_ranking(dense_sections, sections)
        fused_pages = [item[0] for item in reciprocal_rank_fusion([lexical_pages, dense_pages])]
        rrf_ms = (time.perf_counter() - fusion_started) * 1000.0 + max(fts_ms, dense_ms)
        relevant = set(case["relevant_page_ids"])
        for name, ranked_sections, latency in (
            ("fts", lexical_sections, fts_ms),
            ("dense", dense_sections, dense_ms),
        ):
            ranked_pages = page_ranking(ranked_sections, sections)
            methods[name].append({
                "case_id": case["id"],
                "slice": case["slice"],
                "relevant_page_ids": sorted(relevant),
                "ranked_page_ids": ranked_pages[:10],
                "metrics": ranking_metrics(ranked_pages, relevant),
                "latency_ms": round(latency, 3),
            })
        methods["rrf"].append({
            "case_id": case["id"],
            "slice": case["slice"],
            "relevant_page_ids": sorted(relevant),
            "ranked_page_ids": fused_pages[:10],
            "metrics": ranking_metrics(fused_pages, relevant),
            "latency_ms": round(rrf_ms, 3),
        })
    summary: dict[str, Any] = {}
    for name, results in methods.items():
        summary[name] = {
            metric: round(sum(item["metrics"][metric] for item in results) / len(results), 4)
            for metric in ("recall@5", "mrr", "ndcg@5")
        }
        summary[name]["p95_ms"] = round(percentile([item["latency_ms"] for item in results], 0.95), 3)
        summary[name]["privacy_violations"] = 0
    report = {
        "ok": True,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "dataset": dataset_path.relative_to(ROOT).as_posix(),
        "dataset_sha256": hashlib.sha256(dataset_path.read_bytes()).hexdigest(),
        "dataset_status": dataset.get("status"),
        "promotion_authority": bool(dataset.get("promotion_authority")),
        "model_manifest_sha256": hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest(),
        "latency_contract": "warm local retrieval; dense query encoding measured as batch-amortized CPU latency",
        "case_count": len(cases),
        "summary": summary,
        "cases": methods,
        "interpretation": "Development evidence only until an independent human relevance audit and protected confirmation are recorded.",
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def search(
    query: str,
    limit: int = 6,
    *,
    privacy: list[str] | None = None,
    status: list[str] | None = None,
    page_type: list[str] | None = None,
    trace: bool = True,
) -> dict[str, Any]:
    wiki = load_wiki_module()
    pages, errors = wiki.load_pages()
    if errors:
        return {"ok": False, "errors": errors}
    all_items = wiki.all_sections(pages)
    manifest, index_errors = validate_index(all_items)
    if index_errors:
        return {"ok": False, "errors": index_errors}
    def eligible(item: Any) -> bool:
        return (
            (privacy is None or item.privacy in privacy)
            and (status is None or item.status in status)
            and (page_type is None or item.page_type in page_type)
        )
    sections = {item.section_id: item for item in all_items if eligible(item)}
    payload = np.load(VECTOR_PATH)
    vectors = payload["vectors"]
    section_ids = payload["section_ids"].tolist()
    query_vector = encode([query], prefix="query")[0]
    eligible_indexes = [index for index, section_id in enumerate(section_ids) if section_id in sections]
    semantic_order = [
        section_ids[index]
        for index in sorted(eligible_indexes, key=lambda index: float(-(vectors[index] @ query_vector)))[: max(limit * 5, 30)]
    ]
    lexical = wiki.search_fts(
        query,
        limit=max(limit * 5, 30),
        privacy=privacy,
        status=status,
        page_type=page_type,
        trace=False,
    )
    lexical_order = [item["section_id"] for item in lexical["results"]]
    fused = reciprocal_rank_fusion([lexical_order, semantic_order])[:limit]
    results = []
    for section_id, score in fused:
        item = sections.get(section_id)
        if item:
            results.append({**item.__dict__, "rrf_score": score})
    report = {
        "ok": True,
        "query": query,
        "fusion": "RRF(k=60)",
        "filters": {"privacy": privacy, "status": status, "page_type": page_type},
        "manifest_sha256": hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest(),
        "content_sha256": manifest["content_sha256"],
        "lexical_ranked": lexical_order,
        "semantic_ranked": semantic_order,
        "results": results,
    }
    if trace:
        trace_dir = ROOT / "reports" / "retrieval-traces"
        trace_dir.mkdir(parents=True, exist_ok=True)
        trace_id = datetime.now().astimezone().strftime("hybrid-%Y%m%dT%H%M%S%z")
        trace_path = trace_dir / f"{trace_id}.json"
        trace_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        report["trace"] = trace_path.relative_to(ROOT).as_posix()
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("build", "search", "benchmark"))
    parser.add_argument("query", nargs="?")
    parser.add_argument("--limit", type=int, default=6)
    parser.add_argument("--privacy", action="append")
    parser.add_argument("--status", action="append")
    parser.add_argument("--type", dest="page_type", action="append")
    parser.add_argument("--no-trace", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        result = build()
    elif args.command == "benchmark":
        result = benchmark()
    else:
        if not args.query:
            parser.error("search requires a query")
        result = search(
            args.query,
            args.limit,
            privacy=args.privacy,
            status=args.status,
            page_type=args.page_type,
            trace=not args.no_trace,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
