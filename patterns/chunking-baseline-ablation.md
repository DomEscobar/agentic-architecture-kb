---
id: pattern-chunking-baseline-ablation
type: pattern
title: Chunking Baseline and Ablation
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T18:42:00+02:00
updated_at: 2026-08-12T18:42:00+02:00
review_at: 2026-11-12
source_ids:
  - source-chunking-evidence-2025-2026
relations:
  - predicate: derived_from
    target: source-chunking-evidence-2025-2026
---

# Chunking Baseline and Ablation

## Decision rule

Start with two controls: fixed token windows and structure-aware sections with a
hard maximum size. Semantic, LLM-based, late or mixture chunking is promoted
only after paired application replay. No strategy is a universal default.

## Manifest

Version parser identity, boundary policy, target/min/max tokens, overlap,
contextual prefix, parent/neighbor expansion, embedding model, index identity
and retrieval depth. Chunk IDs must be stable for unchanged source elements.

## Eval matrix

Cross query granularity (fact, section, synthesis) with document shape (short,
long, table-heavy, hierarchical). Measure Recall@k, evidence coverage, context
precision, answer completeness, citation correctness, index size, ingestion
cost and latency. Score relevance against an invariant evidence view when the
candidate changes contextual prefixes.

## Failure interpretation

Missing evidence before chunking indicates a parser defect. Evidence retrieved
but omitted from context indicates packing/reranking. Evidence present but the
answer is wrong indicates generation or grounding. Do not tune chunk boundaries
to mask another stage's failure.
