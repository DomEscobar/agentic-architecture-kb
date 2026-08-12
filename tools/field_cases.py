#!/usr/bin/env python3
"""Validate independently reviewed field-case evidence without inventing outcomes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/field-case.schema.json").read_text())


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(record_path: Path) -> dict:
    payload = json.loads(record_path.read_text())
    errors = [issue.message for issue in jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).iter_errors(payload)]
    if payload.get("owner") == payload.get("independent_reviewer"):
        errors.append("independent reviewer must differ from owner")
    if payload.get("baseline_manifest_sha256") == payload.get("candidate_manifest_sha256"):
        errors.append("baseline and candidate manifests must differ")
    if payload.get("sample_size") and any(item.get("denominator") != payload["sample_size"] for item in payload.get("metrics", [])):
        errors.append("metric denominators must equal declared sample_size")
    for artifact in payload.get("evidence_artifacts", []):
        path = record_path.parent / artifact.get("path", "")
        if not path.is_file():
            errors.append(f"missing evidence artifact: {artifact.get('path')}")
        elif artifact.get("sha256") != digest(path):
            errors.append(f"evidence digest mismatch: {artifact.get('path')}")
    return {"ok": not errors, "case_id": payload.get("case_id"), "errors": sorted(errors)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    report = validate(args.record)
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
