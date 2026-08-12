import importlib.util
import sys
import json
import tempfile
from unittest import mock
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "hybrid.py"
SPEC = importlib.util.spec_from_file_location("wiki_hybrid", MODULE_PATH)
hybrid = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = hybrid
SPEC.loader.exec_module(hybrid)


class HybridTests(unittest.TestCase):
    def test_rrf_rewards_agreement_and_is_deterministic(self):
        result = hybrid.reciprocal_rank_fusion([["a", "b", "c"], ["b", "a", "d"]])
        self.assertEqual([item[0] for item in result[:2]], ["a", "b"])
        self.assertEqual(result, hybrid.reciprocal_rank_fusion([["a", "b", "c"], ["b", "a", "d"]]))

    def test_model_manifest_is_revision_pinned(self):
        self.assertEqual(len(hybrid.MODEL_REVISION), 40)
        self.assertNotIn("main", hybrid.MODEL_REVISION)

    def test_stale_manifest_fails_closed(self):
        wiki = hybrid.load_wiki_module()
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        sections = wiki.all_sections(pages)
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "manifest.json"
            manifest.write_text(json.dumps({"content_sha256": "stale"}))
            with mock.patch.object(hybrid, "MANIFEST_PATH", manifest), mock.patch.object(hybrid, "VECTOR_PATH", Path(directory) / "vectors.npz"):
                _, index_errors = hybrid.validate_index(sections)
        self.assertTrue(any("missing" in error or "mismatch" in error for error in index_errors))

    def test_eligibility_filters_apply_before_both_rankings(self):
        build = hybrid.build()
        self.assertTrue(build["ok"], build.get("errors"))
        result = hybrid.search(
            "parser architecture",
            limit=5,
            privacy=["public"],
            status=["reviewed"],
            trace=False,
        )
        self.assertTrue(result["ok"], result.get("errors"))
        self.assertTrue(result["results"])
        self.assertTrue(all(item["privacy"] == "public" and item["status"] == "reviewed" for item in result["results"]))
        eligible = {item["section_id"] for item in result["results"]}
        self.assertTrue(eligible.issubset(set(result["semantic_ranked"] + result["lexical_ranked"])))

    def test_page_ranking_deduplicates_sections(self):
        class Item:
            def __init__(self, page_id):
                self.page_id = page_id
        sections = {"a#1": Item("a"), "a#2": Item("a"), "b#1": Item("b")}
        self.assertEqual(hybrid.page_ranking(["a#1", "a#2", "b#1"], sections), ["a", "b"])

    def test_ranking_metrics_use_binary_page_relevance(self):
        metrics = hybrid.ranking_metrics(["x", "b", "a"], {"a", "b"})
        self.assertEqual(metrics["recall@5"], 1.0)
        self.assertEqual(metrics["mrr"], 0.5)
        self.assertGreater(metrics["ndcg@5"], 0.0)


if __name__ == "__main__":
    unittest.main()
