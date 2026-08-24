---
id: source-mistral-agentic-search-2026
type: source
title: Mistral Agentic Search — Navigable Retrieval Tool Contract
status: reviewed
privacy: public
confidence: 0.86
created_at: 2026-08-24T10:40:00+02:00
updated_at: 2026-08-24T10:40:00+02:00
review_at: 2026-10-24
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-agentic-corrective-retrieval
  - predicate: supports
    target: pattern-document-centric-hybrid-rag
  - predicate: applies_to
    target: pattern-project-coding-agent-harness
---

# Mistral Agentic Search — Navigable Retrieval Tool Contract

Primary material checked on 2026-08-24:

- [Product and benchmark announcement](https://mistral.ai/news/agentic-search/)
- [Agentic Search documentation](https://docs.mistral.ai/studio/search/agentic-search)
- [Search Toolkit documentation](https://docs.mistral.ai/studio/search/search-toolkit)
- [MIT starter application, commit
  `4c8c7ac611d6f818c6b3189edc97a45369ec65d2`](https://github.com/mistralai/search-starter-app/tree/4c8c7ac611d6f818c6b3189edc97a45369ec65d2)
- [`mistralai-search-toolkit` 0.0.11](https://pypi.org/project/mistralai-search-toolkit/0.0.11/),
  wheel SHA-256 `e7fcf78784a814570b240e821af768d40d3b7cfd5649a05e140489baa0e61707`

## Evidence class

E2 for the inspectable implementation and its interface contracts. Mistral's
FinanceBench, OfficeQA Pro, latency and token-use improvements are vendor-run
results without an independent reproduction or public end-to-end benchmark
replay in the starter repository. They are not promoted as effectiveness
claims.

## Implemented mechanism

The published package defines a runtime-checkable `NavigableIndex` contract.
Search results carry an opaque chunk ID, source ID and half-open
`[start_offset, end_offset)` positions. Separate operations resolve a hit,
read a source range, move to adjacent chunks in reading order and perform
source-local lexical grep. The starter exposes these operations over MCP.

This adds a concrete interface boundary to existing iterative-retrieval
patterns: global ranked discovery and source-local deterministic navigation
should not be collapsed into repeated semantic searches. Stable positional
identity lets a controller expand context around a hit, inspect exact ranges
and test whether an iteration produced genuinely new evidence.

## Artifact audit

A project generated from the pinned starter installed successfully. Its test
suite reported three passing tests and one skipped backend roundtrip because no
Vespa service was running; both ingestion and search CLI entry points loaded.
The tests exercise MCP schemas and `open` neighbour logic but do not reproduce
the announced quality, latency or cost results.

The documented MCP signature includes `exclude_ids`, but the pinned starter's
`search(query, top_k)` tool does not expose it. Toolkit 0.0.11 declares
`exclude_ids` in a query model, while its high-level query-engine method does
not pass the field through. Consequently, repeat-result prevention is an
advertised capability rather than an end-to-end property of this audited
starter. A consuming controller must maintain a seen-ID set, deduplicate
results and stop when no unique evidence remains.

The package specifies exclusive end offsets, while the starter's MCP `read`
docstring describes the end offset as inclusive. Contract tests must therefore
pin range semantics and boundary behaviour rather than infer them from tool
descriptions.

## Authority and privacy boundary

The same starter MCP server exposes read tools and the mutating `ingest` and
`delete` tools. Ingestion accepts local paths, directories, `file://` and HTTP
URLs. Non-text extraction defaults to Mistral OCR and embeddings use the
Mistral API, so a locally hosted Vespa index does not imply local-only document
processing.

Production and coding-agent deployments should expose a read-only retrieval
surface to ordinary agent runs and place ingestion and deletion behind a
separate administrative authority. Filesystem roots, network egress, source
ACLs and tenant filters must be enforced before search and navigation. Remote
OCR and embedding calls require an explicit data-egress decision.

## Practical regression contract

- A search hit opens to the same anchor and correct previous/next chunks in
  reading order.
- Range reads use one documented half-open convention and never cross a source
  or tenant boundary.
- Grep remains source-local and returns stable locators.
- Repeated retrieval cannot re-enter already-seen chunk IDs; if the backend
  lacks exclusion, the controller deduplicates and stops on zero new evidence.
- Read-only agent credentials cannot ingest or delete documents.
- Egress tests distinguish local indexing from remote OCR and embedding.

This is a portable tool and test contract for document-heavy agent research,
including coding agents consulting specifications and documentation. It is not
a coding harness, code indexer, RSI mechanism or general recommendation to use
Mistral's stack.
