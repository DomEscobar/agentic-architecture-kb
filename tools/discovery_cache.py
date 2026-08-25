#!/usr/bin/env python3
"""Digest-checked offline cache and lexical retrieval for external discovery."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import tempfile
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CACHE_DIR = ROOT / ".architecture-cache" / "discovery"
DEFAULT_SNAPSHOT_URL = "https://ai-architect.huecki.com/api/v1/discovery/snapshot"
MAX_SNAPSHOT_BYTES = 12 * 1024 * 1024
TOKEN = re.compile(r"[\w-]+", re.UNICODE)


def _content_digest(payload: dict) -> str:
    raw = json.dumps(
        {"sources": payload["sources"], "documents": payload["documents"]},
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def validate_snapshot(payload: dict) -> str:
    if not isinstance(payload, dict) or not isinstance(payload.get("sources"), list) or not isinstance(payload.get("documents"), list):
        raise ValueError("snapshot does not match the external discovery contract")
    if not payload["documents"]:
        raise ValueError("snapshot contains no discovery documents")
    for document in payload["documents"]:
        if document.get("canonical") is not False or document.get("corpus") != "external-discovery":
            raise ValueError("snapshot contains an invalid trust label")
    digest = _content_digest(payload)
    if payload.get("content_sha256") != digest:
        raise ValueError("snapshot content digest mismatch")
    return digest


def sync_snapshot(url: str = DEFAULT_SNAPSHOT_URL, cache_dir: Path = DEFAULT_CACHE_DIR, timeout: float = 30.0) -> Path:
    request = urllib.request.Request(url, headers={"user-agent": "agentic-architecture-kb-discovery-sync/1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read(MAX_SNAPSHOT_BYTES + 1)
    if len(raw) > MAX_SNAPSHOT_BYTES:
        raise ValueError("snapshot exceeds the 12 MiB safety limit")
    payload = json.loads(raw.decode("utf-8"))
    digest = validate_snapshot(payload)
    cache_dir.mkdir(parents=True, exist_ok=True)
    immutable = cache_dir / f"external-discovery.{digest}.json"
    normalized = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    with tempfile.NamedTemporaryFile(dir=cache_dir, prefix=".snapshot-", delete=False) as handle:
        handle.write(normalized)
        temporary = Path(handle.name)
    os.replace(temporary, immutable)
    pointer = cache_dir / "current.json"
    with tempfile.NamedTemporaryFile(dir=cache_dir, prefix=".current-", mode="w", encoding="utf-8", delete=False) as handle:
        json.dump({"artifact": immutable.name, "content_sha256": digest}, handle, indent=2)
        handle.write("\n")
        temporary_pointer = Path(handle.name)
    os.replace(temporary_pointer, pointer)
    return immutable


def load_snapshot(cache_dir: Path = DEFAULT_CACHE_DIR) -> dict:
    pointer = json.loads((cache_dir / "current.json").read_text(encoding="utf-8"))
    artifact = cache_dir / Path(pointer["artifact"]).name
    payload = json.loads(artifact.read_text(encoding="utf-8"))
    digest = validate_snapshot(payload)
    if pointer.get("content_sha256") != digest:
        raise ValueError("offline discovery pointer digest mismatch")
    return payload


def _tokens(value: str) -> list[str]:
    return [token.lower() for token in TOKEN.findall(value)]


def search_snapshot(payload: dict, question: str, limit: int = 4, max_per_source: int = 2) -> list[dict]:
    query = Counter(_tokens(question))
    documents = payload["documents"]
    document_frequencies = Counter()
    tokenized = []
    for document in documents:
        tokens = _tokens(f"{document.get('title', '')} {document.get('section', '')} {document.get('text', '')}")
        tokenized.append(tokens)
        document_frequencies.update(set(tokens))
    average_length = sum(map(len, tokenized)) / max(1, len(tokenized))
    scored = []
    for document, tokens in zip(documents, tokenized):
        frequencies = Counter(tokens)
        score = 0.0
        for term, query_frequency in query.items():
            frequency = frequencies[term]
            if not frequency:
                continue
            inverse = math.log(1 + (len(documents) - document_frequencies[term] + 0.5) / (document_frequencies[term] + 0.5))
            denominator = frequency + 1.2 * (0.25 + 0.75 * len(tokens) / max(1.0, average_length))
            score += query_frequency * inverse * frequency * 2.2 / denominator
        if score:
            scored.append((score, document))
    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    selected, counts = [], Counter()
    for score, document in scored:
        source = document.get("source_id") or document.get("url") or document["id"]
        if counts[source] >= max_per_source:
            continue
        selected.append({**document, "score": round(score, 6)})
        counts[source] += 1
        if len(selected) >= limit:
            break
    return selected
