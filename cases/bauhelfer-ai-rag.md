---
id: case-bauhelfer-ki-rag
type: case
title: Bauhelfer AI RAG
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T17:05:00+02:00
updated_at: 2026-08-08T17:05:00+02:00
review_at: 2026-10-08
source_ids:
  - source-domescobar-bauhelfer-ki
relations:
  - predicate: derived_from
    target: source-domescobar-bauhelfer-ki
  - predicate: evaluated_by
    target: pattern-document-centric-hybrid-rag
---

# Case: Bauhelfer AI RAG

## Context

A German-language estimating assistant processes heterogeneous construction and
trade documents such as bills of quantities, price lists, office files, scans,
and photos. Its output is not unconstrained chat text, but an auditable, editable
offer draft with line items, quantities, prices, assumptions, and sources.

## Relevant constraints

- Exact IDs, item numbers, units, amounts, and pages matter more than semantic
  similarity alone.
- Tables, layout, and reading order carry meaning.
- Retrieval must strictly isolate organizations and projects.
- Misattributing content across customers or projects is a severe failure.
- Unknown values must remain explicit rather than being plausibly completed.
- A user approves the result before PDF generation or any external effect.

## Implemented pattern

```text
upload
 -> project/tenant scope
 -> Docling parsing
 -> Markdown + JSON + layout/table metadata
 -> structure-aware chunks + contextual header
 -> embeddings + German FTS
 -> dense top-40 + lexical top-40
 -> RRF(k=60)
 -> poison/overview filtering
 -> optional LLM reranking of top-30
 -> top-8 context
 -> typed evidence bundle
 -> structured offer/document snapshot
 -> blocking review issues
 -> human approval
```

Postgres stores application data, metadata, the full-text index, and pgvector
together. The embedding column has 1,536 dimensions; OpenAI and Gemini are
provider options, with truncated Gemini vectors normalized. The ingestion worker
processes embeddings in batches of 64.

## Strengths of this pattern

- Tenant and project filters are enforced inside dense and FTS SQL queries,
  before result selection.
- Structured chunks preserve page, heading path, and type.
- Contextual headers improve the self-description of isolated chunks.
- RRF combines semantic and exact matches without adding incompatible raw scores.
- Evidence bundles are validated against file IDs that actually belong to the
  project.
- Document snapshots freeze source revision and evidence; stale revisions and
  cross-project evidence are rejected.
- Missing or external evidence creates a review requirement instead of false
  confidence.

## Weaknesses and open risks

### Evaluation

The committed retrieval test set contains only one question. The harness scores
a source hit and reports the same value as both context precision and context
recall. This measures neither ranking quality nor genuine precision/recall.
Missing cases include hard negatives, table cells, OCR errors, cross-project
leakage, conflicting document versions, and temporal updates.

### Reranking

The optional LLM reranker sees only the first 500 characters of each chunk. For
tables or evidence appearing later, this can produce incorrect rankings. It
needs an offline baseline against RRF alone, latency and cost measurements, and
a fault-tolerant fallback.

### Heuristic poison filters

Known parser fallback text and multi-project summaries are removed through
German substring rules. This is understandable as an incident fix but fragile.
The more robust solution is typed ingestion status, origin, and scope metadata
that is filtered deterministically before retrieval.

### Index and provider migration

The embedding dimension is coupled to the database schema. Changes to model,
dimension, normalization, or chunker require an index manifest, parallel
rebuild, recall comparison, and atomic cutover.

### Repository hygiene

Upload and parsed-output directories must not appear in public source-control
history. Deleting them in the current commit does not remove them from Git
history. Required controls are secret/PII scanning, reviewed history cleanup,
storage outside the repository, and CI guards against recommitting the data.

## Recommended next evaluations

1. Use 10–20 representative project folders, sliced by PDF, scan, XLSX, and
   photo.
2. Create at least 100 retrieval questions with complete relevance labels, not
   merely one expected source.
3. Measure each stage: parse-field accuracy, Recall@k, nDCG@k, MRR, context
   precision, citation correctness, unsupported-claim rate, and line-item field
   accuracy.
4. Run ablations for FTS, dense, hybrid/RRF, and hybrid plus reranker.
5. Add a negative suite for tenant/project leakage, deleted files, poisoned
   chunks, stale versions, and missing prices.
6. Replay with cost and p50/p95 latency; protect reranking with a canary and
   feature flag.

## Reusable conclusion

Document-centric domain applications need a pipeline-wide architecture. Parsing
quality, scope filters, structured chunks, hybrid retrieval, evidence contracts,
and deterministic postconditions jointly determine quality. Vector-database
choice alone does not.
