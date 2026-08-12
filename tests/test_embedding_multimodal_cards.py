import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "wiki.py"
SPEC = importlib.util.spec_from_file_location("wiki_tool_embedding_multimodal", MODULE_PATH)
wiki = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = wiki
SPEC.loader.exec_module(wiki)


class EmbeddingMultimodalCardTests(unittest.TestCase):
    def test_catalogs_are_complete_and_machine_valid(self):
        report = wiki.lint()
        self.assertTrue(report["ok"], "\n".join(report["errors"]))
        cards, errors = wiki.load_techniques()
        self.assertEqual(errors, [])
        embeddings = [c for c in cards if c["technique_id"].startswith("embedding.")]
        multimodal = [c for c in cards if c["technique_id"].startswith("multimodal.")]
        self.assertGreaterEqual(len(embeddings), 8)
        self.assertGreaterEqual(len(multimodal), 8)
        self.assertTrue({"dense", "sparse", "hybrid", "multivector", "migration"}.issubset({c["family"] for c in embeddings}))
        self.assertTrue({"visual", "fusion", "routing", "reranking", "citation"}.issubset({c["family"] for c in multimodal}))
        for card in embeddings + multimodal:
            self.assertGreaterEqual(len(card["failure_modes"]), 3)
            self.assertGreaterEqual(len(card["required_evals"]), 4)
            self.assertIn(card["evidence"]["level"], {"E2", "E3"})

    def test_catalogs_are_retrievable_by_architecture_use_case(self):
        pages, errors = wiki.load_pages()
        self.assertEqual(errors, [])
        queries = {
            "multilingual cross language dense embedding": "embedding",
            "identifier exact match learned sparse hybrid": "embedding",
            "immutable challenger index dual read rollback": "embedding",
            "charts derender table direct visual retrieval": "multimodal",
            "page bounding box region citation": "multimodal",
            "SQL heterogeneous table reasoning": "multimodal",
        }
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "wiki.sqlite"
            wiki.build_fts(pages, index)
            for query, marker in queries.items():
                result = wiki.search_fts(query, privacy=["public"], status=["reviewed"], trace=False, db_path=index)
                self.assertGreater(result["candidate_count"], 0, query)
                self.assertTrue(any(marker in item["page_id"] for item in result["results"]), query)


if __name__ == "__main__":
    unittest.main()
