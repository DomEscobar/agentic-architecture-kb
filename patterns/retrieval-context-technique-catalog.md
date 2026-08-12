---
id: pattern-retrieval-context-technique-catalog
type: pattern
title: Retrieval, Reranking, and Context Assembly Technique Catalog
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T22:06:00+02:00
updated_at: 2026-08-12T22:06:00+02:00
review_at: 2026-10-12
source_ids:
  - source-retrieval-context-landscape-2026-08
relations:
  - predicate: derived_from
    target: source-retrieval-context-landscape-2026-08
  - predicate: depends_on
    target: pattern-scaling-rag-baselines
---

# Retrieval, Reranking, and Context Assembly Technique Catalog

## Baseline ladder

1. Apply authorization and hard metadata predicates before ranking.
2. Measure BM25 and dense retrieval independently under the same candidate depth.
3. Add deterministic hybrid fusion only for complementary failure slices.
4. Tune retrieve-k, rerank-k and final-k from Recall@k and context-precision curves.
5. Rerank only when relevant evidence is found but ordered too low.
6. Select or compress evidence only when context noise or budget is the bottleneck.
7. Bind citations to stable source spans and abstain on calibrated missing evidence.
8. Route rewriting, decomposition, multi-query or iterative retrieval to queries
   that justify their extra calls and drift surface.

## Query routing

- Exact identifiers, versions, names and quoted text: BM25 first.
- Paraphrases and vocabulary mismatch: dense retrieval candidate.
- Mixed exact and conceptual workload: BM25 plus dense with RRF candidate.
- Conversational follow-up: intent-preserving standalone-query rewrite.
- Heterogeneous repeated workload: a logged sparse/dense/hybrid router only after oracle-route and confusion-matrix evaluation.
- Multi-facet request: bounded multi-query only if unique evidence yield improves.
- Multi-hop request: dependency-preserving decomposition or iterative retrieval.
- Direct lookup: no agent loop; keep one retrieval call as the control.

## Reranking and context routing

- Adequate Recall@k but poor rank: cross-encoder over a bounded candidate set.
- Redundant top results: MMR or coverage selection, sliced by query type.
- Long passages with local textual evidence: extractive sentence selection with
  adjacency and provenance.
- Context exceeds budget: evidence-preserving compression with an uncompressed
  fallback for high-risk or layout-dependent evidence.
- Missing evidence: bounded abstention or approved alternate source, never silent
  fallback to parametric memory where provenance is required.
- Every sourced answer: claim-to-span citation binding and post-generation checks.
- Long contexts: position-aware packing with deduplication and contradiction retention, not blind relevance concatenation.

## Diagnostic order

If required evidence is absent from the candidate pool, fix parsing, indexing,
filters, query transformation or first-stage retrieval. If it is present but ranks
low, inspect fusion and reranking. If it ranks high but is omitted from the prompt,
inspect diversity, compression and packing. If it is in the prompt but the answer
is unsupported, inspect generation, attribution and abstention. This ordering stops
downstream techniques from masking upstream defects.

## Promotion contract

Use paired replay with immutable corpus, relevance labels and permission sentinels.
Promote one bounded surface at a time. Require intended-slice gains without
regressions in exact identifiers, negative questions, citation attribution,
latency, cost or ACL leakage. Keep the previous manifest as rollback and log query
rewrites, fused ranks, reranker scores, selected spans, stop reasons and citations.
