import importlib.util
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


if __name__ == "__main__":
    unittest.main()
