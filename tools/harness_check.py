#!/usr/bin/env python3
"""Fail-closed check of a repository harness binding.

Validates that a harness.json only cites artifacts that exist in the canonical
knowledge base, that cited claims are not superseded or contested, that every
declared invariant points at a real Makefile target, and that the review date is
still in the future. Absence of harness.json is allowed: adoption is opt-in.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ("inbox", "sources", "concepts", "patterns", "cases", "entities", "syntheses")
CLAIM_LEDGER = ROOT / "claims/ledger.jsonl"
MAKEFILE = ROOT / "Makefile"

ID_RE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)


def page_ids() -> set[str]:
    ids: set[str] = set()
    for directory in CONTENT_DIRS:
        for path in (ROOT / directory).rglob("*.md"):
            match = ID_RE.search(path.read_text(encoding="utf-8", errors="replace"))
            if match:
                ids.add(match.group(1))
    return ids


def claims() -> dict[str, str]:
    found: dict[str, str] = {}
    if not CLAIM_LEDGER.exists():
        return found
    for line in CLAIM_LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        found[record["id"]] = record.get("status", "unknown")
    return found


def make_targets() -> set[str]:
    targets: set[str] = set()
    for line in MAKEFILE.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^([A-Za-z0-9_.-]+):", line)
        if match:
            targets.add(match.group(1))
    return targets


def label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT.parent))
    except ValueError:
        return str(path)


def check(path: Path) -> dict:
    errors: list[str] = []
    if not path.exists():
        return {"ok": True, "binding": None, "errors": [], "note": "no harness binding present"}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return {"ok": False, "binding": label(path), "errors": [f"invalid JSON: {error}"]}

    required = {"schema_version", "kb_commit", "because_of", "invariants", "review_at"}
    missing = sorted(required - set(data))
    extra = sorted(set(data) - required)
    if missing:
        errors.append(f"missing fields: {', '.join(missing)}")
    if extra:
        errors.append(f"unexpected fields: {', '.join(extra)}")
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    commit = data.get("kb_commit", "")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
        errors.append("kb_commit must be a hex commit id")

    pages = page_ids()
    claim_status = claims()
    targets = make_targets()

    because = data.get("because_of")
    if not isinstance(because, list) or not because:
        errors.append("because_of must be a non-empty list")
    else:
        for entry in because:
            if entry in pages or entry in claim_status:
                if entry in claim_status and claim_status[entry] in {"superseded", "contested"}:
                    errors.append(f"bound claim is {claim_status[entry]}: {entry}")
            else:
                errors.append(f"unknown artifact: {entry}")

    invariants = data.get("invariants")
    if not isinstance(invariants, list) or not invariants:
        errors.append("invariants must be a non-empty list")
    else:
        for index, item in enumerate(invariants):
            if not isinstance(item, dict) or set(item) != {"rule", "check"}:
                errors.append(f"invariant {index}: expected exactly rule and check")
                continue
            if len(str(item["rule"])) < 10:
                errors.append(f"invariant {index}: rule is too short to be checkable")
            if item["check"] not in targets:
                errors.append(f"invariant {index}: unknown Makefile target: {item['check']}")

    review_at = data.get("review_at", "")
    try:
        if date.fromisoformat(review_at) < date.today():
            errors.append(f"review_at is overdue: {review_at}")
    except (TypeError, ValueError):
        errors.append("review_at must be an ISO date")

    return {"ok": not errors, "binding": label(path), "errors": errors}


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "harness.json"
    result = check(target)
    result["pages"] = len(page_ids())
    result["claims"] = len(claims())
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
