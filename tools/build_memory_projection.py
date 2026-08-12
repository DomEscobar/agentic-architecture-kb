#!/usr/bin/env python3
"""Build a deterministic, one-way Memory Wiki projection from canonical build/wiki.json."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build/wiki.json"
OUTPUT = ROOT / "releases/memory-wiki-projection.md"
MANIFEST = ROOT / "releases/memory-wiki-projection.manifest.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    payload = json.loads(BUILD.read_text())
    canonical_sha = digest(BUILD)
    pages = [
        page for page in payload["pages"]
        if page["metadata"].get("status") == "reviewed"
        and page["metadata"].get("privacy") in {"public", "internal"}
    ]
    lines = [
        "# Agentic Architect canonical projection",
        "",
        f"Canonical SHA-256: `{canonical_sha}`",
        "",
        "This is a generated, one-way projection. The canonical source is `llm-wiki`;",
        "edits here must never reverse-sync into the canonical repository.",
        "",
    ]
    for page in sorted(pages, key=lambda item: item["metadata"]["id"]):
        metadata = page["metadata"]
        lines.extend([
            f"## {metadata['title']}",
            "",
            f"Canonical ID: `{metadata['id']}`  ",
            f"Type: `{metadata['type']}` · Privacy: `{metadata['privacy']}` · Confidence: `{metadata.get('confidence', 'undeclared')}`  ",
            f"Sources: {', '.join(f'`{item}`' for item in metadata.get('source_ids', [])) or 'none'}",
            "",
            page["body"].strip(),
            "",
        ])
    lines.extend(["## Validated technique cards", ""])
    for card in sorted(payload["techniques"], key=lambda item: item["technique_id"]):
        evidence = card["evidence"]
        lines.extend([
            f"### {card['name']}",
            "",
            f"Technique ID: `{card['technique_id']}` · Stage: `{card['stage']}` · Risk: `{card['risk_class']}`",
            "",
            card["mechanism"],
            "",
            "Use when: " + "; ".join(card["use_when"]),
            "",
            "Avoid when: " + "; ".join(card["avoid_when"]),
            "",
            "Failure modes: " + "; ".join(card["failure_modes"]),
            "",
            "Required evals: " + "; ".join(card["required_evals"]),
            "",
            f"Evidence: `{evidence['level']}` from {', '.join(f'`{item}`' for item in evidence['source_ids'])}; reviewed `{card['freshness']['review']}`.",
            "",
        ])
    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "canonical_sha256": canonical_sha,
        "artifact_sha256": digest(OUTPUT),
        "page_count": len(pages),
        "technique_count": len(payload["techniques"]),
        "privacy_allowlist": ["public", "internal"],
        "status_allowlist": ["reviewed"],
        "reverse_sync_allowed": False,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
