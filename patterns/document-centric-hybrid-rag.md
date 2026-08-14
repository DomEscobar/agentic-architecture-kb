---
id: pattern-document-centric-hybrid-rag
type: pattern
title: Document-centric Hybrid RAG
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T17:05:00+02:00
updated_at: 2026-08-14T10:47:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-bauhelfer-ki
  - source-rag-radar-2026-08
relations:
  - predicate: derived_from
    target: source-domescobar-bauhelfer-ki
  - predicate: applies_to
    target: case-bauhelfer-ki-rag
---

# Document-centric Hybrid RAG

## Evidence boundary

The originating implementation is a private repository. Winning conditions and
pipeline shape below are a project-derived candidate. Lexical-plus-dense hybrid
retrieval is independently evidenced; the typed offer-output contract is not.
Do not treat this pattern as an accepted default until a public or otherwise
auditable paired evaluation exists.

## Winning conditions

This pattern fits when document structure and exact values are equally
important: offers, contracts, technical specifications, bills of quantities,
invoices, or regulatory documents.

## Architecture

### Ingestion

1. Store the original immutably and outside the code repository.
2. Set tenant, project, document type, and retention before parsing.
3. Extract layout, table, OCR, and page information.
4. Store parser output and parser/configuration versions.
5. Segment by heading, table, line item, or page; use fixed token windows only
   as a fallback.
6. Attach a stable ID, document version, page anchor, type, confidence, and
   compact context header to each chunk.
7. Build lexical and semantic indexes reproducibly.

### Retrieval

```text
intent/scope
 -> deterministic ACL + metadata filter
 -> dense retrieval || lexical retrieval
 -> RRF
 -> optional reranker
 -> diversity/coverage selection
 -> evidence pack with stable anchors
```

ACL and project filters must apply before ANN and ranking. RRF is a strong
default because it fuses ranks instead of uncalibrated scores. Top-k values are
dataset-specific parameters, not universal best practices.

### Generation

- Separate the evidence pack explicitly from the output schema.
- Link every domain claim and critical field to a source ID and page anchor.
- Model assumed, unknown, and contradictory as distinct states.
- Compute and validate calculable values deterministically.
- Require human approval before external or irreversible output.

## Do not use

- For small, fully structured datasets: direct SQL or API queries are simpler
  and more precise.
- For exact table aggregation: a parser plus structured database often
  outperforms text RAG.
- For one-off short documents: long context may be the cheaper baseline.

## Failure detection

- Parse goldens per document type
- Retrieval ablations and per-slice metrics
- Cross-scope canaries
- Citation and anchor validation
- Unsupported-claim and missing-field checks
- Index-manifest and deletion checks
- Latency, cost, and reranker fallback in the trace
