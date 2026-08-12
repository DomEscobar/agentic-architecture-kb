---
id: pattern-multimodal-rag-technique-catalog
type: pattern
title: Multimodal RAG Technique Catalog and Routing Matrix
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-12T22:09:00+02:00
updated_at: 2026-08-12T22:09:00+02:00
review_at: 2026-10-12
source_ids:
  - source-multimodal-rag-landscape-2026-08
relations:
  - predicate: derived_from
    target: source-multimodal-rag-landscape-2026-08
  - predicate: depends_on
    target: pattern-multimodal-document-retrieval
---

# Multimodal RAG Technique Catalog and Routing Matrix

## Candidate lanes

- OCR and parsed text remain the cheap exact-text lane.
- Single-vector image embeddings are a compact visual baseline.
- Visual late interaction preserves patch-level evidence for layout-heavy pages at greater storage and scoring cost.
- OCR/text plus visual fusion hedges modality-specific failures but requires deduplication and calibrated fusion.

## Specialized structures

- Chart derendering maps plots to table-like data and should be fused with direct visual retrieval for complex charts.
- SQL-backed table retrieval preserves relational operations for multi-hop aggregation instead of flattening all rows into prose.
- Multimodal reranking spends a larger model only on a bounded candidate set.
- Region-anchored citation carries page, bounding box or cell coordinates into the answer contract.
- Layout-symbolic plus neural retrieval is a candidate for cross-page dependencies where graph construction can be inspected.
- Utility-oriented evidence selection reranks a bounded visual pool by downstream usefulness, not similarity alone.
- Hybrid single-/multi-vector retrieval uses a compact first stage and a fine-grained visual rescore.
- Interleaved representations are candidates for documents where text and visuals jointly define document-level relevance.

## Routing defaults

Use text-only retrieval for clean prose. Fan out to visual retrieval for layout, diagrams, slides and OCR uncertainty. Route chart questions to direct-image plus derendered-table lanes, and relational table questions to structured execution. All lanes share ACL/version filters and return stable page/region identities.

## Promotion gates

Compare text-only, OCR+text, visual-only and fused candidates by modality slice. Measure page and region recall, answer and citation correctness, exact-number accuracy, index bytes per page, ingestion throughput, p95 query latency and cost. A visual lane is not promoted from page-retrieval scores alone.
