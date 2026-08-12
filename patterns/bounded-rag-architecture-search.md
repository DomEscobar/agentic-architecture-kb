---
id: pattern-bounded-rag-architecture-search
type: pattern
title: Bounded RAG Architecture Search
status: reviewed
privacy: public
confidence: 0.84
created_at: 2026-08-12T18:42:00+02:00
updated_at: 2026-08-12T18:42:00+02:00
review_at: 2026-10-12
source_ids:
  - source-rag-architecture-search-2026
  - source-agent-evaluation-research-2026
relations:
  - predicate: derived_from
    target: source-rag-architecture-search-2026
  - predicate: evaluated_by
    target: pattern-eval-guided-improvement-loop
---

# Bounded RAG Architecture Search

## Search space

Represent the champion and candidates as typed manifests. Begin with reversible
query rewriting, filters, retrieval depth, fusion weights, reranking and context
packing. Parser, chunking and embedding changes form a later reindexing tier.
Every experiment changes one declared unit or uses a declared combinatorial
search budget.

## Architect loop

`baseline → sliced diagnosis → technique evidence → candidate manifest → isolated replay → paired comparison → promote/reject → archive`

The proposer sees aggregate development failures and allowed technique cards,
not hidden expected answers or promotion-gate details.

## Promotion rule

Optimizer rankings are task-dependent. Apply hard privacy/safety/citation gates,
then compare quality, latency and cost under the same data, seeds and budgets.
Repeat ambiguous comparisons. Promotion requires an untouched holdout,
immutable artifacts, canary, kill switch and rollback.

## Stopping

Stop on target attainment, exhausted budget, patience without improvement,
unstable judge agreement, repeated invalid patches or evaluator-integrity
failure. “Perfect on development” is not evidence of universal improvement.
