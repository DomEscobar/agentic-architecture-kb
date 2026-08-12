import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EvalIsolationTests(unittest.TestCase):
    def test_private_splits_are_absent_and_ignored_until_real_cases_exist(self):
        ignore = (ROOT / "evals/private/.gitignore").read_text()
        self.assertIn("*", ignore)
        contract = json.loads((ROOT / "evals/split-contracts.json").read_text())
        private = [item for item in contract["splits"] if item["kind"] in {"selection", "holdout"}]
        self.assertTrue(all(item["status"] == "awaiting-private-cases" for item in private))

    def test_promotion_evidence_cannot_be_a_boolean(self):
        schema = json.loads((ROOT / "schemas/promotion-evidence.schema.json").read_text())
        self.assertEqual(schema["type"], "object")
        self.assertIn("candidate_manifest_sha256", schema["required"])
        self.assertEqual(schema["properties"]["human_approval"]["const"], True)


if __name__ == "__main__":
    unittest.main()
