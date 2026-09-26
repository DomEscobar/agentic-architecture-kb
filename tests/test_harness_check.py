import importlib.util
import json
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

KB = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("harness_check", KB / "tools/harness_check.py")
harness_check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(harness_check)


def binding(**overrides):
    data = {
        "schema_version": 1,
        "kb_commit": "4d99256",
        "because_of": ["pattern-project-coding-agent-harness"],
        "invariants": [{"rule": "The test suite passes before publication", "check": "test"}],
        "review_at": (date.today() + timedelta(days=30)).isoformat(),
    }
    data.update(overrides)
    return data


class HarnessCheckTests(unittest.TestCase):
    def write(self, tmp, data):
        path = Path(tmp) / "harness.json"
        path.write_text(json.dumps(data))
        return path

    def test_absent_binding_is_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = harness_check.check(Path(tmp) / "harness.json")
        self.assertTrue(result["ok"])
        self.assertIsNone(result["binding"])

    def test_valid_binding_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = harness_check.check(self.write(tmp, binding()))
        self.assertTrue(result["ok"], result["errors"])

    def test_unknown_artifact_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = harness_check.check(self.write(tmp, binding(because_of=["pattern-does-not-exist"])))
        self.assertFalse(result["ok"])
        self.assertTrue(any("unknown artifact" in error for error in result["errors"]))

    def test_superseded_claim_fails(self):
        original = harness_check.claims
        harness_check.claims = lambda: {"claim-retired": "superseded"}
        try:
            with tempfile.TemporaryDirectory() as tmp:
                result = harness_check.check(self.write(tmp, binding(because_of=["claim-retired"])))
        finally:
            harness_check.claims = original
        self.assertFalse(result["ok"])
        self.assertTrue(any("superseded" in error for error in result["errors"]))

    def test_unknown_make_target_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            data = binding(invariants=[{"rule": "Something must always hold", "check": "not-a-target"}])
            result = harness_check.check(self.write(tmp, data))
        self.assertFalse(result["ok"])
        self.assertTrue(any("unknown Makefile target" in error for error in result["errors"]))

    def test_missing_field_fails(self):
        data = binding()
        data.pop("review_at")
        with tempfile.TemporaryDirectory() as tmp:
            result = harness_check.check(self.write(tmp, data))
        self.assertFalse(result["ok"])
        self.assertTrue(any("missing fields" in error for error in result["errors"]))

    def test_stale_review_fails(self):
        data = binding(review_at=(date.today() - timedelta(days=1)).isoformat())
        with tempfile.TemporaryDirectory() as tmp:
            result = harness_check.check(self.write(tmp, data))
        self.assertFalse(result["ok"])
        self.assertTrue(any("overdue" in error for error in result["errors"]))

    def test_repository_binding_is_valid(self):
        result = harness_check.check(KB / "harness.json")
        self.assertTrue(result["ok"], result["errors"])


if __name__ == "__main__":
    unittest.main()
