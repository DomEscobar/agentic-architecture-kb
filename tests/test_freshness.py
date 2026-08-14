import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "freshness.py"
SPEC = importlib.util.spec_from_file_location("freshness_tool", MODULE_PATH)
freshness = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = freshness
SPEC.loader.exec_module(freshness)


class FreshnessTests(unittest.TestCase):
    def test_registry_is_complete_and_query_packs_forbid_direct_promotion(self):
        report = freshness.validate()
        self.assertTrue(report["ok"], "\n".join(report["errors"]))
        self.assertGreaterEqual(report["project_count"], 20)
        packs = json.loads(freshness.QUERY_PACKS.read_text())
        self.assertFalse(packs["policy"]["direct_promotion_allowed"])
        self.assertTrue(packs["policy"]["forums_are_e1_discovery_only"])

    def test_advisory_urls_are_not_misclassified_as_repositories(self):
        self.assertIsNone(freshness.normalize_github_repo("https://github.com/advisories/GHSA-test"))
        self.assertEqual(
            freshness.normalize_github_repo("https://github.com/langchain-ai/langgraph/blob/main/README.md"),
            "langchain-ai/langgraph",
        )

    def test_repo_pulse_creates_baseline_then_detects_release_change(self):
        snapshots = [
            {"default_branch":"main","head_sha":"a","latest_release":"v1","release_published_at":None,"archived":False,"disabled":False,"license":"MIT","pushed_at":None,"errors":[]},
            {"default_branch":"main","head_sha":"b","latest_release":"v2","release_published_at":None,"archived":False,"disabled":False,"license":"MIT","pushed_at":None,"errors":[]},
        ]
        single_registry = {"schema_version":1,"projects":[json.loads(freshness.REGISTRY.read_text())["projects"][0]],"advisories":[]}
        with tempfile.TemporaryDirectory() as directory:
            state = Path(directory) / "state.json"
            report = Path(directory) / "report.json"
            with patch.object(freshness, "validate", return_value={"ok":True}), patch.object(freshness, "read_json", side_effect=lambda path: single_registry if path == freshness.REGISTRY else json.loads(path.read_text())), patch.object(freshness, "snapshot_project", side_effect=[snapshots[0], snapshots[1]]), patch.object(freshness, "github_json", return_value=({"files":[{"filename":"README.md"}]}, None)):
                first = freshness.repo_pulse(state, report)
                second = freshness.repo_pulse(state, report)
        self.assertTrue(first["baseline_only"])
        self.assertEqual(second["changes"][0]["classifications"], ["activity-only", "documentation-change", "capability-change"])
        self.assertEqual(len(second["actionable"]), 1)

    def test_due_review_report_never_has_promotion_authority(self):
        with tempfile.TemporaryDirectory() as directory:
            result = freshness.due_reviews(Path(directory) / "due.json", today=date(2100, 1, 1))
        self.assertFalse(result["promotion_authority"])
        self.assertGreater(len(result["due_techniques"]), 0)
        self.assertGreater(len(result["due_claims"]), 0)


if __name__ == "__main__":
    unittest.main()
