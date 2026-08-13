import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "wiki.py"
SPEC = importlib.util.spec_from_file_location("wiki_tool", MODULE_PATH)
wiki = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = wiki
SPEC.loader.exec_module(wiki)


class WikiToolTests(unittest.TestCase):
    def test_repository_lints(self):
        report = wiki.lint()
        self.assertTrue(report["ok"], "\n".join(report["errors"]))

    def test_every_page_has_unique_id(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        ids = [page.metadata["id"] for page in pages]
        self.assertEqual(len(ids), len(set(ids)))

    def test_consulting_cases_have_unique_ids_and_expectations(self):
        path = MODULE_PATH.parents[1] / "evals" / "consulting-cases.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        cases = payload["cases"]
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(cases), 8)
        for case in cases:
            self.assertGreaterEqual(len(case["expects"]), 5)

    def test_consulting_readiness_artifacts_exist_and_are_nonempty(self):
        root = MODULE_PATH.parents[1]
        contract = json.loads(
            (root / "evals" / "consulting-readiness.json").read_text(encoding="utf-8")
        )
        artifacts = contract["required_artifacts"]
        self.assertEqual(len(artifacts), len(set(artifacts)))
        for relative in artifacts:
            path = root / relative
            self.assertTrue(path.is_file(), relative)
            self.assertIn("# ", path.read_text(encoding="utf-8"), relative)

    def test_claim_ledger_is_compiled_and_source_backed(self):
        report = wiki.lint()
        self.assertTrue(report["ok"], "\n".join(report["errors"]))
        self.assertGreaterEqual(report["claim_count"], 55)
        self.assertEqual(report["claim_coverage"]["coverage_ratio"], 1.0)
        self.assertEqual(report["claim_coverage"]["uncovered_page_ids"], [])

    def test_parser_technique_catalog_is_complete_and_diverse(self):
        report = wiki.lint()
        self.assertTrue(report["ok"], "\n".join(report["errors"]))
        self.assertGreaterEqual(report["technique_count"], 15)
        techniques, errors = wiki.load_techniques()
        self.assertEqual(errors, [])
        parser_cards = [card for card in techniques if card["technique_id"].startswith("parser.")]
        self.assertGreaterEqual(len(parser_cards), 15)
        self.assertEqual({card["family"] for card in parser_cards}, {"native", "pipeline", "vlm", "managed"})
        for card in parser_cards:
            self.assertGreaterEqual(len(card["use_when"]), 2)
            self.assertGreaterEqual(len(card["avoid_when"]), 2)
            self.assertGreaterEqual(len(card["failure_modes"]), 3)
            self.assertGreaterEqual(len(card["required_evals"]), 4)
            self.assertEqual(card["reindex_required"], "full")

    def test_chunking_technique_catalog_is_complete_and_diverse(self):
        report = wiki.lint()
        self.assertTrue(report["ok"], "\n".join(report["errors"]))
        techniques, errors = wiki.load_techniques()
        self.assertEqual(errors, [])
        cards = [card for card in techniques if card["technique_id"].startswith("chunking.")]
        self.assertGreaterEqual(len(cards), 18)
        self.assertEqual(
            {card["family"] for card in cards},
            {"fixed", "structural", "semantic", "contextual", "hierarchical", "adaptive", "specialized"},
        )
        for card in cards:
            self.assertEqual(card["stage"], "segmentation")
            self.assertGreaterEqual(len(card["use_when"]), 2)
            self.assertGreaterEqual(len(card["avoid_when"]), 2)
            self.assertGreaterEqual(len(card["failure_modes"]), 3)
            self.assertGreaterEqual(len(card["required_evals"]), 4)
            self.assertEqual(card["reindex_required"], "full")

    def test_architecture_gap_eval_pack_is_bounded_and_unique(self):
        root = MODULE_PATH.parents[1]
        payload = json.loads((root / "evals" / "architecture-knowledge-gaps-v1.json").read_text(encoding="utf-8"))
        self.assertFalse(payload["holdout"])
        cases = payload["cases"]
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(cases), 12)
        for case in cases:
            self.assertGreaterEqual(len(case["expects"]), 6)

    def test_retrieval_eval_pack_has_query_style_slices(self):
        payload = json.loads((MODULE_PATH.parents[1] / "evals/wiki-retrieval-v1.json").read_text())
        self.assertFalse(payload["promotion_authority"])
        self.assertGreaterEqual(len(payload["cases"]), 12)
        slices = {case["slice"] for case in payload["cases"]}
        self.assertTrue(any(item.endswith("-exact") for item in slices))
        self.assertTrue(any(item.endswith("-paraphrase") for item in slices))

    def test_section_ids_are_stable_and_unique(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        first = [section.section_id for section in wiki.all_sections(pages)]
        second = [section.section_id for section in wiki.all_sections(pages)]
        self.assertEqual(first, second)
        self.assertEqual(len(first), len(set(first)))

    def test_compile_artifact_is_byte_reproducible(self):
        root = MODULE_PATH.parents[1]
        first = wiki.compile_wiki()
        self.assertTrue(first["ok"], first.get("errors"))
        before = (root / "build/wiki.json").read_bytes()
        second = wiki.compile_wiki()
        self.assertTrue(second["ok"], second.get("errors"))
        self.assertEqual(before, (root / "build/wiki.json").read_bytes())

    def test_fts_search_filters_and_returns_citable_sections(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "wiki.sqlite"
            wiki.build_fts(pages, index)
            result = wiki.search_fts(
                "LLM Judge Calibration",
                privacy=["internal"],
                status=["reviewed"],
                trace=False,
                db_path=index,
            )
        self.assertGreater(result["candidate_count"], 0)
        self.assertTrue(all("#" in item["section_id"] for item in result["results"]))
        self.assertTrue(all(item["privacy"] == "internal" for item in result["results"]))

    def test_memory_lane_is_retrievable_for_consulting_questions(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        queries = [
            "memory poisoning quarantine promotion",
            "verified forgetting derived indexes",
            "procedural memory preconditions rollback",
            "temporal validity conflicts supersession",
            "agent memory brownfield audit",
        ]
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "wiki.sqlite"
            wiki.build_fts(pages, index)
            for query in queries:
                result = wiki.search_fts(
                    query,
                    privacy=["internal"],
                    status=["reviewed"],
                    trace=False,
                    db_path=index,
                )
                self.assertGreater(result["candidate_count"], 0, query)
                self.assertTrue(
                    any("memory" in item["page_id"] for item in result["results"]),
                    query,
                )

    def test_parser_catalog_is_retrievable_by_use_case(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        queries = [
            "born digital bounding boxes PyMuPDF",
            "scientific formulas multilingual MinerU",
            "AWS forms signatures Textract",
            "historical multilingual PaddleOCR VL",
            "office local markdown AnyDoc",
            "PDF geometry tables pdfplumber",
        ]
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "wiki.sqlite"
            wiki.build_fts(pages, index)
            for query in queries:
                result = wiki.search_fts(
                    query,
                    privacy=["public"],
                    status=["reviewed"],
                    trace=False,
                    db_path=index,
                )
                self.assertGreater(result["candidate_count"], 0, query)
                self.assertTrue(
                    any("parser" in item["page_id"] for item in result["results"]),
                    query,
                )

    def test_chunking_catalog_is_retrievable_by_use_case(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        queries = [
            "atomic facts proposition chunking",
            "code AST chunking functions",
            "table headers rows chunking",
            "hierarchical synthesis summary tree",
            "conversation speaker turns episodes",
        ]
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "wiki.sqlite"
            wiki.build_fts(pages, index)
            for query in queries:
                result = wiki.search_fts(
                    query,
                    privacy=["public"],
                    status=["reviewed"],
                    trace=False,
                    db_path=index,
                )
                self.assertGreater(result["candidate_count"], 0, query)
                self.assertTrue(
                    any("chunking" in item["page_id"] for item in result["results"]),
                    query,
                )

    def test_runtime_adoption_catalog_covers_implementation_tiers(self):
        techniques, errors = wiki.load_techniques()
        self.assertEqual(errors, [])
        ids = {
            card["technique_id"]
            for card in techniques
            if card["technique_id"].startswith("runtime.")
        }
        self.assertTrue(
            {
                "runtime.custom-minimal-runtime",
                "runtime.langgraph-runtime",
                "runtime.deepagents-harness",
                "runtime.deerflow-harness",
                "runtime.openclaw-platform",
                "runtime.openai-agents-sdk",
                "runtime.pydantic-ai-runtime",
                "runtime.google-adk-runtime",
                "runtime.microsoft-agent-framework",
                "runtime.temporal-durable-substrate",
            }.issubset(ids)
        )

    def test_runtime_build_vs_adopt_is_retrievable(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        queries = [
            "Deep Agents long horizon harness sandbox",
            "DeerFlow gateway channels sandbox",
            "OpenClaw multi channel operational platform",
            "custom minimal loop versus framework",
            "Temporal durable workflow process restart",
        ]
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "wiki.sqlite"
            wiki.build_fts(pages, index)
            for query in queries:
                result = wiki.search_fts(
                    query,
                    privacy=["public"],
                    status=["reviewed"],
                    trace=False,
                    db_path=index,
                )
                self.assertGreater(result["candidate_count"], 0, query)
                self.assertTrue(
                    any(
                        item["page_id"]
                        in {
                            "pattern-runtime-build-vs-adopt",
                            "source-agent-runtime-framework-landscape-2026-08",
                        }
                        for item in result["results"]
                    ),
                    query,
                )


if __name__ == "__main__":
    unittest.main()
