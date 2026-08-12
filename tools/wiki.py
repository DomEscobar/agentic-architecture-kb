#!/usr/bin/env python3
"""Deterministic compiler and linter for the Agentic Architect wiki."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ("inbox", "sources", "concepts", "patterns", "cases", "entities", "syntheses")
SCHEMA_PATH = ROOT / "schemas" / "page.schema.json"
CLAIM_SCHEMA_PATH = ROOT / "schemas" / "claim.schema.json"
CLAIM_LEDGER_PATH = ROOT / "claims" / "ledger.jsonl"
TECHNIQUE_SCHEMA_PATH = ROOT / "schemas" / "technique-card.schema.json"
TECHNIQUE_DIR = ROOT / "techniques"
BUILD_DIR = ROOT / "build"
REPORTS_DIR = ROOT / "reports"
INDEX_DIR = ROOT / "indexes"
INDEX_PATH = INDEX_DIR / "wiki.sqlite"
TRACE_DIR = REPORTS_DIR / "retrieval-traces"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
REMOTE_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TOKEN = re.compile(r"[\w-]+", re.UNICODE)


@dataclass(frozen=True)
class Page:
    path: Path
    metadata: dict[str, Any]
    body: str
    sha256: str

    @property
    def relative_path(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


@dataclass(frozen=True)
class Section:
    section_id: str
    page_id: str
    path: str
    title: str
    heading: str
    heading_path: str
    ordinal: int
    privacy: str
    status: str
    page_type: str
    updated_at: str
    text: str


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


def load_techniques() -> tuple[list[dict[str, Any]], list[str]]:
    techniques: list[dict[str, Any]] = []
    errors: list[str] = []
    if not TECHNIQUE_DIR.exists():
        return techniques, ["techniques: missing technique directory"]
    for path in sorted(TECHNIQUE_DIR.rglob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        if not isinstance(payload, dict):
            errors.append(f"{path.relative_to(ROOT)}: technique card must be an object")
            continue
        payload["_path"] = path.relative_to(ROOT).as_posix()
        techniques.append(payload)
    return techniques, errors


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    return slug[:80] or "section"


def page_sections(page: Page) -> list[Section]:
    """Split Markdown at headings while ignoring headings inside fenced code."""
    chunks: list[tuple[str, str, str]] = []
    stack: list[str] = []
    current_heading = "Preamble"
    current_path = "Preamble"
    current_lines: list[str] = []
    in_fence = False

    def flush() -> None:
        text = "\n".join(current_lines).strip()
        if text:
            chunks.append((current_heading, current_path, text))

    for line in page.body.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        match = None if in_fence else HEADING.match(line)
        if match:
            flush()
            current_lines = []
            level = len(match.group(1))
            current_heading = match.group(2).strip().rstrip("#").strip()
            stack[level - 1:] = [current_heading]
            current_path = " > ".join(stack)
        else:
            current_lines.append(line)
    flush()

    seen: dict[str, int] = {}
    sections: list[Section] = []
    for ordinal, (heading, heading_path, text) in enumerate(chunks, start=1):
        base = slugify(heading_path)
        seen[base] = seen.get(base, 0) + 1
        anchor = base if seen[base] == 1 else f"{base}-{seen[base]}"
        sections.append(Section(
            section_id=f"{page.metadata['id']}#{anchor}",
            page_id=page.metadata["id"],
            path=page.relative_path,
            title=page.metadata["title"],
            heading=heading,
            heading_path=heading_path,
            ordinal=ordinal,
            privacy=page.metadata["privacy"],
            status=page.metadata["status"],
            page_type=page.metadata["type"],
            updated_at=page.metadata["updated_at"],
            text=text,
        ))
    return sections


def all_sections(pages: list[Page]) -> list[Section]:
    return [section for page in pages for section in page_sections(page)]


def build_fts(pages: list[Page], db_path: Path = INDEX_PATH) -> dict[str, Any]:
    sections = all_sections(pages)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    try:
        connection.executescript("""
            DROP TABLE IF EXISTS sections;
            DROP TABLE IF EXISTS sections_fts;
            CREATE TABLE sections (
                rowid INTEGER PRIMARY KEY,
                section_id TEXT NOT NULL UNIQUE,
                page_id TEXT NOT NULL,
                path TEXT NOT NULL,
                title TEXT NOT NULL,
                heading TEXT NOT NULL,
                heading_path TEXT NOT NULL,
                ordinal INTEGER NOT NULL,
                privacy TEXT NOT NULL,
                status TEXT NOT NULL,
                page_type TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                text TEXT NOT NULL
            );
            CREATE VIRTUAL TABLE sections_fts USING fts5(
                title, heading_path, text,
                content='sections', content_rowid='rowid',
                tokenize='unicode61 remove_diacritics 2'
            );
        """)
        for section in sections:
            cursor = connection.execute(
                """INSERT INTO sections
                (section_id,page_id,path,title,heading,heading_path,ordinal,privacy,status,page_type,updated_at,text)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                tuple(section.__dict__.values()),
            )
            connection.execute(
                "INSERT INTO sections_fts(rowid,title,heading_path,text) VALUES (?,?,?,?)",
                (cursor.lastrowid, section.title, section.heading_path, section.text),
            )
        connection.commit()
    finally:
        connection.close()
    return {"index": db_path.as_posix(), "page_count": len(pages), "section_count": len(sections)}


def fts_expression(query: str) -> str:
    tokens = TOKEN.findall(query.lower())
    return " AND ".join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in tokens)


def search_fts(
    query: str,
    *,
    limit: int = 5,
    privacy: list[str] | None = None,
    status: list[str] | None = None,
    page_type: list[str] | None = None,
    trace: bool = True,
    db_path: Path = INDEX_PATH,
) -> dict[str, Any]:
    strict_expression = fts_expression(query)
    if not strict_expression:
        raise ValueError("query must contain searchable tokens")
    filters: list[str] = []
    filter_parameters: list[Any] = []
    for column, values in (("privacy", privacy), ("status", status), ("page_type", page_type)):
        if values:
            filters.append(f"s.{column} IN ({','.join('?' for _ in values)})")
            filter_parameters.extend(values)
    where = " AND " + " AND ".join(filters) if filters else ""
    candidate_limit = max(limit * 5, 20)
    sql = f"""SELECT s.section_id,s.page_id,s.path,s.title,s.heading_path,s.privacy,
                     s.status,s.page_type,s.updated_at,bm25(sections_fts,5.0,2.0,1.0) AS score,
                     snippet(sections_fts,2,'[',']',' … ',24) AS snippet
              FROM sections_fts JOIN sections s ON s.rowid=sections_fts.rowid
              WHERE sections_fts MATCH ?{where}
              ORDER BY score, s.section_id LIMIT ?"""
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    try:
        def execute(expression: str) -> list[dict[str, Any]]:
            parameters = [expression, *filter_parameters, candidate_limit]
            return [dict(row) for row in connection.execute(sql, parameters)]

        expression = strict_expression
        candidates = execute(expression)
        if not candidates and " AND " in strict_expression:
            expression = strict_expression.replace(" AND ", " OR ")
            candidates = execute(expression)
        loaded_ids = [item["section_id"] for item in candidates[:limit]]
        loaded: list[dict[str, Any]] = []
        if loaded_ids:
            placeholders = ",".join("?" for _ in loaded_ids)
            rows = connection.execute(
                f"SELECT section_id,text FROM sections WHERE section_id IN ({placeholders})",
                loaded_ids,
            )
            text_by_id = {row["section_id"]: row["text"] for row in rows}
            loaded = [{**item, "text": text_by_id[item["section_id"]]} for item in candidates[:limit]]
    finally:
        connection.close()
    result = {
        "query": query,
        "strict_fts_expression": strict_expression,
        "fts_expression": expression,
        "filters": {"privacy": privacy or [], "status": status or [], "type": page_type or []},
        "index": db_path.as_posix(),
        "candidate_count": len(candidates),
        "candidates": candidates,
        "loaded_section_ids": loaded_ids,
        "results": loaded,
    }
    if trace:
        TRACE_DIR.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S%z")
        digest = hashlib.sha256(json.dumps(result, sort_keys=True).encode()).hexdigest()[:10]
        trace_path = TRACE_DIR / f"{stamp}-{digest}.json"
        result["trace_id"] = trace_path.stem
        trace_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result["trace_path"] = trace_path.relative_to(ROOT).as_posix()
    return result


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

    claims: list[dict[str, Any]] = []
    if not CLAIM_LEDGER_PATH.exists():
        errors.append("claims/ledger.jsonl: missing claim ledger")
    else:
        claim_schema = json.loads(CLAIM_SCHEMA_PATH.read_text(encoding="utf-8"))
        claim_validator = jsonschema.Draft202012Validator(claim_schema, format_checker=jsonschema.FormatChecker())
        section_ids = {section.section_id for section in all_sections(pages)}
        seen_claim_ids: set[str] = set()
        for line_number, raw in enumerate(CLAIM_LEDGER_PATH.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw.strip():
                continue
            try:
                claim = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"claims/ledger.jsonl:{line_number}: invalid JSON: {exc.msg}")
                continue
            claims.append(claim)
            for issue in claim_validator.iter_errors(claim):
                errors.append(f"claims/ledger.jsonl:{line_number}: {issue.message}")
            claim_id = claim.get("id")
            if claim_id in seen_claim_ids:
                errors.append(f"claims/ledger.jsonl:{line_number}: duplicate claim id '{claim_id}'")
            seen_claim_ids.add(claim_id)
            if claim.get("section_id") not in section_ids:
                errors.append(f"claims/ledger.jsonl:{line_number}: unknown section_id '{claim.get('section_id')}'")
            for source_id in claim.get("source_ids", []):
                target = by_id.get(source_id)
                if target is None or target.metadata.get("type") != "source":
                    errors.append(f"claims/ledger.jsonl:{line_number}: unknown source page '{source_id}'")

    techniques, technique_errors = load_techniques()
    errors.extend(technique_errors)
    technique_schema = json.loads(TECHNIQUE_SCHEMA_PATH.read_text(encoding="utf-8"))
    technique_validator = jsonschema.Draft202012Validator(
        technique_schema, format_checker=jsonschema.FormatChecker()
    )
    seen_technique_ids: set[str] = set()
    for technique in techniques:
        path = technique.pop("_path")
        for issue in sorted(technique_validator.iter_errors(technique), key=lambda item: list(item.path)):
            location = ".".join(str(part) for part in issue.path) or "card"
            errors.append(f"{path}: {location}: {issue.message}")
        technique_id = technique.get("technique_id")
        if technique_id in seen_technique_ids:
            errors.append(f"{path}: duplicate technique_id '{technique_id}'")
        seen_technique_ids.add(technique_id)
        for source_id in technique.get("evidence", {}).get("source_ids", []):
            target = by_id.get(source_id)
            if target is None or target.metadata.get("type") != "source":
                errors.append(f"{path}: unknown source page '{source_id}'")

    eligible_claim_pages = {
        page.metadata["id"]
        for page in pages
        if page.metadata.get("status") == "reviewed"
        and page.metadata.get("type") in {"pattern", "synthesis", "concept", "case"}
    }
    section_to_page = {section.section_id: section.page_id for section in all_sections(pages)}
    covered_claim_pages = {
        section_to_page[claim["section_id"]]
        for claim in claims
        if claim.get("section_id") in section_to_page
    }
    claim_coverage = {
        "eligible_page_count": len(eligible_claim_pages),
        "covered_page_count": len(eligible_claim_pages & covered_claim_pages),
        "coverage_ratio": round(len(eligible_claim_pages & covered_claim_pages) / max(len(eligible_claim_pages), 1), 4),
        "uncovered_page_ids": sorted(eligible_claim_pages - covered_claim_pages),
        "interpretation": "Mechanical page coverage does not prove that every material claim was declared; human review remains required.",
    }
    errors.sort()
    return {
        "ok": not errors,
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "page_count": len(pages),
        "claim_count": len(claims),
        "technique_count": len(techniques),
        "claim_coverage": claim_coverage,
        "errors": errors,
    }


def compile_wiki() -> dict[str, Any]:
    report = lint()
    if not report["ok"]:
        return report
    pages, _ = load_pages()
    sections = all_sections(pages)
    techniques, _ = load_techniques()
    for technique in techniques:
        technique.pop("_path", None)
    # The canonical artifact must be byte-reproducible. Wall-clock generation
    # time belongs in reports, not in the content-addressed build projection.
    content_revision = max(page.metadata["updated_at"] for page in pages)
    compiled = {
        "format_version": 2,
        "content_revision": content_revision,
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
        "sections": [section.__dict__ for section in sections],
        "claims": [json.loads(line) for line in CLAIM_LEDGER_PATH.read_text(encoding="utf-8").splitlines() if line.strip()],
        "techniques": techniques,
    }
    BUILD_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)
    (BUILD_DIR / "wiki.json").write_text(json.dumps(compiled, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "quality.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REPORTS_DIR / "claim-coverage.json").write_text(
        json.dumps(report["claim_coverage"], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    index_report = build_fts(pages)
    report["section_count"] = len(sections)
    report["fts_index"] = index_report["index"]
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("lint", "compile", "index", "search"))
    parser.add_argument("query", nargs="?")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--privacy", action="append")
    parser.add_argument("--status", action="append")
    parser.add_argument("--type", dest="page_type", action="append")
    parser.add_argument("--no-trace", action="store_true")
    args = parser.parse_args()
    if args.command == "compile":
        report = compile_wiki()
    elif args.command == "index":
        pages, errors = load_pages()
        report = {"ok": not errors, "errors": errors}
        if not errors:
            report.update(build_fts(pages))
    elif args.command == "search":
        if not args.query:
            parser.error("search requires a query")
        if not INDEX_PATH.exists():
            pages, errors = load_pages()
            if errors:
                print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False, indent=2))
                return 1
            build_fts(pages)
        report = {"ok": True, **search_fts(
            args.query,
            limit=args.limit,
            privacy=args.privacy,
            status=args.status,
            page_type=args.page_type,
            trace=not args.no_trace,
        )}
    else:
        report = lint()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
