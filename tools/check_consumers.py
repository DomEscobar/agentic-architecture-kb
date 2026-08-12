#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    canonical = ROOT / "build/wiki.json"
    registry = json.loads((ROOT / "releases/registry.json").read_text())
    canonical_sha = digest(canonical)
    consumers = {}
    for name, spec in registry["consumers"].items():
        lock_path = ROOT / spec["lock"]
        lock = json.loads(lock_path.read_text()) if lock_path.exists() else {"status": "missing-lock"}
        digest_matches = lock.get("canonical_sha256") == canonical_sha
        consumer_status = "current" if digest_matches and lock.get("status") == "deployed" else ("pending-approval" if digest_matches else "stale")
        consumers[name] = {
            "status": consumer_status,
            "locked_canonical_sha256": lock.get("canonical_sha256"),
            "lock": spec["lock"],
            "approval_required": spec["approval_required"],
        }
    report = {
        "canonical_sha256": canonical_sha,
        "reverse_sync_allowed": registry["reverse_sync_allowed"],
        "consumers": consumers,
    }
    report_path = ROOT / "reports/consumer-drift.json"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
