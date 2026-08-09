import importlib.util
import json
import sys
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


if __name__ == "__main__":
    unittest.main()
