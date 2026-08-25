import importlib.util
import json
import unittest
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "consult_architecture", ROOT / "tools" / "consult_architecture.py"
)
CLIENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLIENT)

CACHE_SPEC = importlib.util.spec_from_file_location(
    "discovery_cache", ROOT / "tools" / "discovery_cache.py"
)
CACHE = importlib.util.module_from_spec(CACHE_SPEC)
CACHE_SPEC.loader.exec_module(CACHE)


class DiscoveryClientTests(unittest.TestCase):
    def test_payload_preserves_explicit_discovery_choice(self):
        payload = json.loads(CLIENT.build_payload("recovery semantics", False))
        self.assertEqual(payload, {"question": "recovery semantics", "include_discovery": False})

    def test_human_output_keeps_corpora_and_trust_labels_separate(self):
        rendered = CLIENT.format_response(
            {
                "canonical": [
                    {"id": "pattern-runtime", "title": "Runtime", "section": "Recovery", "text": "Use replay tests.", "canonical": True}
                ],
                "discovery": [
                    {"id": "ext:guide", "title": "Guide", "section": "Ideas", "text": "Try a planner split.", "canonical": False, "authority": "low-medium", "commit": "abc"}
                ],
                "corpus_sha256": "c" * 64,
                "discovery_corpus_sha256": "d" * 64,
            }
        )
        self.assertIn("[KB:pattern-runtime]", rendered)
        self.assertIn("[EXT:ext:guide]", rendered)
        self.assertIn("UNTRUSTED, NON-CANONICAL MATERIAL", rendered)
        self.assertNotIn("[KB:ext:guide]", rendered)

    def test_snapshot_rejects_canonical_external_content(self):
        payload = {"sources": [], "documents": [{"id": "x", "canonical": True, "corpus": "external-discovery"}]}
        payload["content_sha256"] = CACHE._content_digest(payload)
        with self.assertRaisesRegex(ValueError, "trust label"):
            CACHE.validate_snapshot(payload)

    def test_offline_search_caps_results_per_source(self):
        documents = [
            {"id": f"x-{index}", "source_id": "one", "title": "Recovery", "section": "Replay", "text": "tool recovery replay", "canonical": False, "corpus": "external-discovery"}
            for index in range(4)
        ]
        payload = {"sources": [], "documents": documents}
        payload["content_sha256"] = CACHE._content_digest(payload)
        results = CACHE.search_snapshot(payload, "tool recovery", limit=4)
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()
