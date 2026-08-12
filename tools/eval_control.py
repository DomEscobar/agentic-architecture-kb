#!/usr/bin/env python3
"""Control-plane-only validation for promotion evidence; never imported by an optimizer."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/promotion-evidence.schema.json").read_text())
ACCESS_LOG = ROOT / "evals/private/access-log.jsonl"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_access_log() -> tuple[list[dict], list[str]]:
    events: list[dict] = []
    errors: list[str] = []
    if not ACCESS_LOG.is_file():
        return events, ["private access log unavailable"]
    for line_number, line in enumerate(ACCESS_LOG.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"access log line {line_number}: {exc}")
            continue
        required = {"event_id", "release_id", "split_id", "actor", "purpose", "accessed_at", "case_set_sha256"}
        missing = sorted(required - set(event))
        if missing:
            errors.append(f"access log line {line_number}: missing {', '.join(missing)}")
        events.append(event)
    ids = [event.get("event_id") for event in events]
    if len(ids) != len(set(ids)):
        errors.append("duplicate access-log event_id")
    return events, errors


def verify(path: Path) -> dict:
    payload = json.loads(path.read_text())
    errors = [issue.message for issue in jsonschema.Draft202012Validator(SCHEMA).iter_errors(payload)]
    split_contract = ROOT / "evals/split-contracts.json"
    if payload.get("split_manifest_sha256") != sha256(split_contract):
        errors.append("split manifest digest mismatch")
    if payload.get("baseline_manifest_sha256") == payload.get("candidate_manifest_sha256"):
        errors.append("baseline and candidate identities must differ")
    private_path = ROOT / "evals/private"
    if not private_path.is_dir():
        errors.append("private split mount unavailable")
    case_set = private_path / payload.get("case_set_file", "")
    if not case_set.is_file():
        errors.append("declared private case set is unavailable")
    elif payload.get("case_set_sha256") != sha256(case_set):
        errors.append("private case-set digest mismatch")
    events, access_errors = load_access_log()
    errors.extend(access_errors)
    matching_events = [
        event for event in events
        if event.get("release_id") == payload.get("release_id")
        and event.get("case_set_sha256") == payload.get("case_set_sha256")
        and event.get("split_id") == payload.get("split_id")
    ]
    if len(matching_events) != 1:
        errors.append("promotion requires exactly one matching protected-split access event")
    if matching_events and matching_events[0].get("purpose") != "promotion-confirmation":
        errors.append("protected split access purpose is not promotion-confirmation")
    return {"ok": not errors, "release_id": payload.get("release_id"), "errors": sorted(errors)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", type=Path)
    args = parser.parse_args()
    report = verify(args.evidence)
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
