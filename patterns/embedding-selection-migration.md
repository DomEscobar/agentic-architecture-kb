---
id: pattern-embedding-selection-migration
type: pattern
title: Embedding Selection and Migration
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-12T18:42:00+02:00
updated_at: 2026-08-12T18:42:00+02:00
review_at: 2026-11-12
source_ids:
  - source-embedding-evaluation-2025
relations:
  - predicate: derived_from
    target: source-embedding-evaluation-2025
---

# Embedding Selection and Migration

## Selection rule

Shortlist from public benchmarks, select on private retrieval slices. Always
include BM25 and the current embedder. Compare dense-only and hybrid retrieval
under fixed chunking, candidate depth and reranking.

## Required slices

Languages, domain terms, identifiers, paraphrases, long passages, hard
negatives, freshness and unanswerable queries. Report Recall@k/nDCG by slice,
not only an aggregate mean, plus encoding throughput, query latency, index size,
licence and data-residency constraints.

## Migration

Build a new immutable index with model revision, dimension, normalization,
instruction template, tokenizer/truncation and source-manifest hashes. Shadow or
dual-read it. Promote only after paired replay and rollback rehearsal; never
rewrite the champion index in place.

## Drift

Re-run sentinel queries after model/provider revisions and on a schedule tied to
corpus and query-distribution change. A stable API name does not guarantee a
stable embedding space.
