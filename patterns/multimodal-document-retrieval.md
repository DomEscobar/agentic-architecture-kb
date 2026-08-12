---
id: pattern-multimodal-document-retrieval
type: pattern
title: Routed Multimodal Document Retrieval
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-12T18:42:00+02:00
updated_at: 2026-08-12T18:42:00+02:00
review_at: 2026-11-12
source_ids:
  - source-multimodal-document-retrieval-2025
  - source-document-parsing-evidence-2026
relations:
  - predicate: derived_from
    target: source-multimodal-document-retrieval-2025
  - predicate: depends_on
    target: pattern-parser-selection-contract
---

# Routed Multimodal Document Retrieval

## Architecture boundary

Maintain text and visual candidate lanes behind the same ACL/version filter.
Route or fan out visual-heavy queries, fuse candidates, rerank, then assemble a
context package with exact page/region anchors. The visual lane supplements; it
does not silently replace text retrieval or provenance.

## Fit

Use for tables, diagrams, forms, slides, scanned pages and layout-dependent
questions. Prefer text-only retrieval for clean prose when it meets the evals at
lower cost.

## Evaluation

Slice by modality and compare text-only, OCR+text, visual-only and fused lanes.
Measure page and region recall, answer/citation correctness, index bytes per
page, ingestion/query latency and cost. Include visually similar negatives,
wrong-page citations and text-visible-but-layout-wrong cases.

## Failure controls

Preserve page images and parser output identities, cap visual candidate depth,
deduplicate text/visual hits, redact sensitive images, and fall back to exact
text extraction for quotations and numbers.
