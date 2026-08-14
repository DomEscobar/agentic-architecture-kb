#!/usr/bin/env python3
"""Deterministic freshness inventory, GitHub pulse, and due-review reporting."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "freshness" / "projects.json"
QUERY_PACKS = ROOT / "freshness" / "research-query-packs.json"
SCHEMA = ROOT / "schemas" / "project-registry.schema.json"
TECHNIQUES = ROOT / "techniques"
STATE = ROOT / "reports" / "repo-pulse-state.json"
REPORT = ROOT / "reports" / "repo-pulse-latest.json"
DUE_REPORT = ROOT / "reports" / "freshness-due-reviews.json"
USER_AGENT = "agentic-architecture-kb-freshness/1"


@lru_cache(maxsize=1)
def github_token() -> str | None:
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"], check=True, capture_output=True, text=True, timeout=10
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    return result.stdout.strip() or None


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_techniques() -> dict[str, dict[str, Any]]:
    cards: dict[str, dict[str, Any]] = {}
    for path in sorted(TECHNIQUES.rglob("*.json")):
        card = read_json(path)
        cards[card["technique_id"]] = card
    return cards


def normalize_github_repo(url: str) -> str | None:
    prefix = "https://github.com/"
    if not url.startswith(prefix):
        return None
    parts = [part for part in url[len(prefix):].split("/") if part]
    if len(parts) < 2 or parts[0] == "advisories":
        return None
    return f"{parts[0]}/{parts[1].removesuffix('.git')}"


def validate() -> dict[str, Any]:
    errors: list[str] = []
    registry = read_json(REGISTRY)
    schema = read_json(SCHEMA)
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    for issue in validator.iter_errors(registry):
        errors.append(f"project registry: {'.'.join(map(str, issue.path))}: {issue.message}")

    cards = load_techniques()
    ids = [project.get("id") for project in registry.get("projects", [])]
    if len(ids) != len(set(ids)):
        errors.append("project registry: duplicate project id")
    registered = set(ids)
    for project in registry.get("projects", []):
        expected = f"https://github.com/{project.get('id')}"
        if project.get("repository") != expected:
            errors.append(f"{project.get('id')}: repository must be {expected}")
        for technique_id in project.get("technique_ids", []):
            if technique_id not in cards:
                errors.append(f"{project.get('id')}: unknown technique id {technique_id}")

    advisory_set = set(registry.get("advisories", []))
    for technique_id, card in cards.items():
        for link in card.get("evidence", {}).get("links", []):
            repo = normalize_github_repo(link)
            if repo and repo not in registered:
                errors.append(f"{technique_id}: GitHub repository is not registered: {repo}")
            if link.startswith("https://github.com/advisories/") and link not in advisory_set:
                errors.append(f"{technique_id}: GitHub advisory is not registered: {link}")

    query_packs = read_json(QUERY_PACKS)
    lane_ids = [lane.get("id") for lane in query_packs.get("lanes", [])]
    if len(lane_ids) != len(set(lane_ids)) or len(lane_ids) < 6:
        errors.append("research query packs require at least six unique lanes")
    if query_packs.get("policy", {}).get("direct_promotion_allowed") is not False:
        errors.append("research query packs must forbid direct promotion")
    return {"ok": not errors, "project_count": len(ids), "advisory_count": len(advisory_set), "errors": sorted(errors)}


def github_json(path: str) -> tuple[dict[str, Any] | None, str | None]:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT}
    token = github_token()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com{path}", headers=headers)
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response), None
    except HTTPError as exc:
        if exc.code == 404:
            return None, None
        return None, f"HTTP {exc.code}"
    except (URLError, TimeoutError) as exc:
        return None, str(exc)


def remote_head(repository: str) -> tuple[str | None, str | None, str | None]:
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--symref", repository, "HEAD"],
            check=True,
            capture_output=True,
            text=True,
            timeout=45,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        return None, None, str(exc)
    branch = None
    sha = None
    for line in result.stdout.splitlines():
        if line.startswith("ref: refs/heads/") and line.endswith("\tHEAD"):
            branch = line.split("refs/heads/", 1)[1].split("\t", 1)[0]
        elif line.endswith("\tHEAD"):
            sha = line.split("\t", 1)[0]
    return branch, sha, None


def snapshot_project(project: dict[str, Any]) -> dict[str, Any]:
    branch, sha, head_error = remote_head(project["repository"])
    metadata, metadata_error = github_json(f"/repos/{project['id']}")
    release = None
    release_error = None
    if project["watch"]["releases"]:
        release, release_error = github_json(f"/repos/{project['id']}/releases/latest")
    errors = [error for error in (head_error, metadata_error, release_error) if error]
    return {
        "default_branch": branch or (metadata or {}).get("default_branch"),
        "head_sha": sha,
        "latest_release": (release or {}).get("tag_name"),
        "release_published_at": (release or {}).get("published_at"),
        "archived": (metadata or {}).get("archived"),
        "disabled": (metadata or {}).get("disabled"),
        "license": ((metadata or {}).get("license") or {}).get("spdx_id"),
        "pushed_at": (metadata or {}).get("pushed_at"),
        "errors": errors,
    }


def classify(project: dict[str, Any], previous: dict[str, Any] | None, current: dict[str, Any]) -> list[str]:
    if current["errors"]:
        return ["manual-verification-needed"]
    if current["archived"] or current["disabled"]:
        return ["archived-or-abandoned"]
    if previous is None:
        return ["baseline-created"]
    changes: list[str] = []
    if current["head_sha"] != previous.get("head_sha"):
        changes.append("activity-only")
        watched = tuple(project["watch"].get("paths", []))
        if watched and any(path == prefix or path.startswith(prefix.rstrip("/") + "/") for path in current.get("changed_paths", []) for prefix in watched):
            changes.append("documentation-change")
    if current["latest_release"] != previous.get("latest_release"):
        changes.append("capability-change")
    if current["license"] != previous.get("license"):
        changes.append("manual-verification-needed")
    return changes or ["unchanged"]


def repo_pulse(state_path: Path = STATE, report_path: Path = REPORT) -> dict[str, Any]:
    validation = validate()
    if not validation["ok"]:
        return validation
    registry = read_json(REGISTRY)
    previous = read_json(state_path) if state_path.exists() else {"projects": {}}
    snapshots: dict[str, Any] = {}
    changes: list[dict[str, Any]] = []
    projects = registry["projects"]
    with ThreadPoolExecutor(max_workers=min(6, len(projects))) as executor:
        current_snapshots = list(executor.map(snapshot_project, projects))
    for project, current in zip(projects, current_snapshots, strict=True):
        old = previous.get("projects", {}).get(project["id"])
        current["changed_paths"] = []
        if old and old.get("head_sha") and current.get("head_sha") and old["head_sha"] != current["head_sha"]:
            comparison, comparison_error = github_json(
                f"/repos/{project['id']}/compare/{old['head_sha']}...{current['head_sha']}"
            )
            if comparison_error:
                current["errors"].append(comparison_error)
            elif comparison:
                current["changed_paths"] = sorted(file["filename"] for file in comparison.get("files", []))
        snapshots[project["id"]] = current
        classes = classify(project, old, current)
        changes.append({
            "id": project["id"],
            "risk": project["risk"],
            "technique_ids": project["technique_ids"],
            "classifications": classes,
            "previous": old,
            "current": current,
        })
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    state = {"schema_version": 1, "checked_at": now, "projects": snapshots}
    report = {
        "ok": not any(item["current"]["errors"] for item in changes),
        "checked_at": now,
        "baseline_only": not state_path.exists(),
        "project_count": len(changes),
        "actionable": [item for item in changes if item["classifications"] not in (["unchanged"], ["baseline-created"], ["activity-only"])],
        "changes": changes,
        "promotion_authority": False,
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def due_reviews(output_path: Path = DUE_REPORT, today: date | None = None) -> dict[str, Any]:
    today = today or date.today()
    cards = load_techniques()
    due = []
    for technique_id, card in cards.items():
        review = date.fromisoformat(card["freshness"]["review"])
        if review <= today:
            due.append({"technique_id": technique_id, "review": review.isoformat(), "overdue_days": (today - review).days})
    claims = []
    for line in (ROOT / "claims" / "ledger.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        claim = json.loads(line)
        review = date.fromisoformat(claim["review_at"])
        if review <= today:
            claims.append({"claim_id": claim["id"], "review": review.isoformat(), "overdue_days": (today - review).days})
    result = {
        "ok": True,
        "as_of": today.isoformat(),
        "due_techniques": sorted(due, key=lambda item: (item["review"], item["technique_id"])),
        "due_claims": sorted(claims, key=lambda item: (item["review"], item["claim_id"])),
        "promotion_authority": False,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("validate", "repo-pulse", "due-reviews"))
    args = parser.parse_args()
    if args.command == "repo-pulse":
        result = repo_pulse()
    elif args.command == "due-reviews":
        result = due_reviews()
    else:
        result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
