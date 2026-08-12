import json
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GovernanceTests(unittest.TestCase):
    def test_split_information_flow_keeps_optimizer_out_of_protected_answers(self):
        payload = json.loads((ROOT / "evals/split-contracts.json").read_text())
        flow = payload["information_flow"]
        self.assertTrue(flow["development"]["answers_visible_to_optimizer"])
        for split in ("selection", "holdout", "redteam"):
            self.assertFalse(flow[split]["answers_visible_to_optimizer"])
        self.assertEqual(flow["holdout"]["max_access_per_release"], 1)

    def test_redteam_ids_are_unique_and_have_hard_invariants(self):
        payload = json.loads((ROOT / "evals/redteam-sentinels-v1.json").read_text())
        ids = [case["id"] for case in payload["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 10)
        self.assertTrue(all(len(case["must"]) >= 3 for case in payload["cases"]))

    def test_judge_seed_does_not_pretend_ambiguous_labels_are_human_calibrated(self):
        payload = json.loads((ROOT / "evals/judge-validation-seed-v1.json").read_text())
        ambiguous = [case for case in payload["cases"] if case["class"] == "ambiguous"]
        self.assertTrue(ambiguous)
        self.assertTrue(all(case["expected"] is None and case["label_source"] == "human-required" for case in ambiguous))

    def test_field_case_register_exposes_missing_real_outcomes(self):
        payload = json.loads((ROOT / "evals/field-case-register.json").read_text())
        self.assertFalse(payload["complete"])
        self.assertEqual(payload["validated_case_count"], 0)
        self.assertTrue(any(record["status"].startswith("missing") for record in payload["records"]))

    def test_field_case_schema_requires_measured_denominated_outcomes(self):
        schema = json.loads((ROOT / "schemas/field-case.schema.json").read_text())
        self.assertIn("measured_outcomes", schema["required"])
        self.assertIn("independent_reviewer", schema["required"])
        self.assertIn("rollback_result", schema["required"])
        self.assertIn("evidence_artifacts", schema["required"])
        self.assertIn("denominator", schema["properties"]["measured_outcomes"]["items"]["required"])

    def test_promotion_evidence_requires_artifact_digests_not_booleans(self):
        schema = json.loads((ROOT / "schemas/promotion-evidence.schema.json").read_text())
        required = set(schema["required"])
        self.assertIn("redteam_report_sha256", required)
        self.assertIn("hard_gate_report_sha256", required)
        self.assertIn("case_set_file", required)
        self.assertNotIn("redteam_passed", schema["properties"])

    def test_eval_control_rejects_missing_private_evidence(self):
        module_path = ROOT / "tools/eval_control.py"
        spec = importlib.util.spec_from_file_location("eval_control_test", module_path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        payload = {
            "release_id": "release-test",
            "baseline_manifest_sha256": "a" * 64,
            "candidate_manifest_sha256": "b" * 64,
            "split_manifest_sha256": module.sha256(ROOT / "evals/split-contracts.json"),
            "split_id": "holdout-private-v1",
            "case_set_file": "missing.json",
            "case_set_sha256": "c" * 64,
            "scorer_sha256": "d" * 64,
            "judge_sha256": None,
            "repetition_ids": ["r1", "r2", "r3"],
            "redteam_report_sha256": "e" * 64,
            "hard_gate_report_sha256": "f" * 64,
            "judge_calibration_report_sha256": None,
            "human_approval": True
        }
        with tempfile.TemporaryDirectory() as directory:
            evidence = Path(directory) / "evidence.json"
            evidence.write_text(json.dumps(payload))
            report = module.verify(evidence)
        self.assertFalse(report["ok"])
        self.assertTrue(any("case set" in error or "case-set" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
