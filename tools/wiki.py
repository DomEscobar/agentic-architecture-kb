#!/usr/bin/env python3
"""Deterministic compiler and linter for the Agentic Architect wiki."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ("inbox", "sources", "concepts", "patterns", "cases", "entities", "syntheses")
SCHEMA_PATH = ROOT / "schemas" / "page.schema.json"
BUILD_DIR = ROOT / "build"
REPORTS_DIR = ROOT / "reports"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
REMOTE_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")


@dataclass(frozen=True)
class Page:
    path: Path
    metadata: dict[str, Any]
    body: str
    sha256: str

    @property
    def relative_path(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def json_value(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: json_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_value(item) for item in value]
    return value


def content_paths() -> list[Path]:
    return sorted(path for directory in CONTENT_DIRS for path in (ROOT / directory).rglob("*.md"))


def parse_page(path: Path) -> Page:
    raw = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(raw)
    if not match:
        raise ValueError("missing YAML frontmatter")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    body = raw[match.end():]
    return Page(path, json_value(metadata), body, hashlib.sha256(raw.encode()).hexdigest())


def load_pages() -> tuple[list[Page], list[str]]:
    pages: list[Page] = []
    errors: list[str] = []
    for path in content_paths():
        try:
            pages.append(parse_page(path))
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return pages, errors


def local_link_target(page: Page, target: str) -> Path | None:
    target = target.strip().strip("<>").split("#", 1)[0]
    if not target or target.startswith(REMOTE_SCHEMES):
        return None
    return (page.path.parent / target).resolve()


def lint() -> dict[str, Any]:
    pages, errors = load_pages()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    by_id: dict[str, Page] = {}

    for page in pages:
        rel = page.relative_path
        for issue in sorted(validator.iter_errors(page.metadata), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in issue.path) or "frontmatter"
            errors.append(f"{rel}: {location}: {issue.message}")

        page_id = page.metadata.get("id")
        if isinstance(page_id, str):
            if page_id in by_id:
                errors.append(f"{rel}: duplicate id '{page_id}' (also {by_id[page_id].relative_path})")
            else:
                by_id[page_id] = page

        expected_type = page.path.parent.name.rstrip("s")
        if page.path.parent.name == "syntheses":
            expected_type = "synthesis"
        if page.path.parent.name != "inbox" and page.metadata.get("type") != expected_type:
            errors.append(f"{rel}: type must be '{expected_type}' for this directory")

        created = page.metadata.get("created_at")
        updated = page.metadata.get("updated_at")
        if isinstance(created, str) and isinstance(updated, str):
            try:
                if datetime.fromisoformat(updated) < datetime.fromisoformat(created):
                    errors.append(f"{rel}: updated_at predates created_at")
            except ValueError:
                pass

        for link in MARKDOWN_LINK.findall(page.body):
            target = local_link_target(page, link)
            if target is not None and not target.exists():
                errors.append(f"{rel}: broken link '{link}'")

        for link in WIKILINK.findall(page.body):
            candidates = list(ROOT.rglob(f"{link}.md"))
            if not candidates:
                errors.append(f"{rel}: unresolved wikilink '[[{link}]]'")

    for page in pages:
        rel = page.relative_path
        page_type = page.metadata.get("type")
        source_ids = page.metadata.get("source_ids", [])
        status = page.metadata.get("status")
        if page_type not in ("source", "episode") and status not in ("inbox", "draft") and not source_ids:
            errors.append(f"{rel}: reviewed canonical page requires at least one source_id")
        for source_id in source_ids if isinstance(source_ids, list) else []:
            target = by_id.get(source_id)
            if target is None:
                errors.append(f"{rel}: unknown source_id '{source_id}'")
            elif target.metadata.get("type") != "source":
                errors.append(f"{rel}: source_id '{source_id}' does not target a source page")
        for relation in page.metadata.get("relations", []) if isinstance(page.metadata.get("relations", []), list) else []:
            if isinstance(relation, dict) and relation.get("target") not in by_id:
                errors.append(f"{rel}: relation targets unknown id '{relation.get('target')}'")

    errors.sort()
    return {
        "ok": not errors,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "page_count": len(pages),
        "errors": errors,
    }


def compile_wiki() -> dict[str, Any]:
    report = lint()
    if not report["ok"]:
        return report
    pages, _ = load_pages()
    compiled = {
        "format_version": 1,
        "generated_at": report["generated_at"],
        "source_root": ".",
        "pages": [
            {
                "path": page.relative_path,
                "sha256": page.sha256,
                "metadata": page.metadata,
                "body": page.body,
            }
            for page in sorted(pages, key=lambda item: item.metadata["id"])
        ],
    }
    BUILD_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)
    (BUILD_DIR / "wiki.json").write_text(json.dumps(compiled, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "quality.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("lint", "compile"))
    args = parser.parse_args()
    report = compile_wiki() if args.command == "compile" else lint()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
