import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ConsumerContractTests(unittest.TestCase):
    def test_promotion_graph_is_one_way_and_approval_gated(self):
        registry = json.loads((ROOT / "releases/registry.json").read_text())
        self.assertFalse(registry["reverse_sync_allowed"])
        self.assertTrue(all(item["approval_required"] for item in registry["consumers"].values()))

    def test_memory_projection_is_digest_locked_when_deployed(self):
        lock = json.loads((ROOT / "releases/memory-wiki.lock.json").read_text())
        self.assertEqual(lock["status"], "deployed")
        self.assertEqual(len(lock["canonical_sha256"]), 64)
        self.assertEqual(len(lock["artifact_sha256"]), 64)
        self.assertIn("rollback", lock)

    def test_public_artifact_records_approved_deployment(self):
        lock = json.loads((ROOT / "releases/public-ai-architect.lock.json").read_text())
        self.assertEqual(lock["status"], "deployed")
        self.assertEqual(len(lock["content_sha256"]), 64)
        self.assertEqual(len(lock["image_sha256"]), 64)
        self.assertIn("deployed_at", lock)
        self.assertIn("approved_by", lock)
        self.assertIn("rollback", lock)


if __name__ == "__main__":
    unittest.main()
