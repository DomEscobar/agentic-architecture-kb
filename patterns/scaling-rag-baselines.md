---
id: pattern-scaling-rag-baselines
type: pattern
title: Scaling RAG Baselines
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T18:35:00+02:00
updated_at: 2026-08-08T18:35:00+02:00
review_at: 2026-11-08
source_ids:
  - source-rag-developments-2026-batch-2
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-2
---

# Scaling RAG Baselines

## Pattern

Scale the candidate generator before scaling the agent. Keep an inverted index
as a cheap, inspectable control and expose retrieval to agents through bounded
search/read tools instead of unconstrained corpus browsing.

Baseline ladder:

1. ACL and metadata filters plus BM25;
2. BM25 plus dense retrieval and deterministic fusion;
3. reranking and evidence-budget optimization;
4. bounded query decomposition or an Agent+Search controller;
5. graph, visual or learned retrieval only for measured failure slices.

## Why it wins

Lexical retrieval scales without generative construction and is unusually
strong for identifiers, names and domain terminology. Agents are more useful as
query planners and evidence readers when a scalable search primitive narrows the
space. This keeps latency, cost and failure attribution observable.

## Failure modes and detection

- Vocabulary mismatch: compare against dense/hybrid Recall@k by query slice.
- Agent query drift: log query rewrites, read paths and stop reasons.
- Corpus growth regression: replay the same questions over nested corpus tiers.
- Graph construction wall: record indexed coverage, tokens per source token and
  freshness lag, not just quality on the completed subset.
- Answer gains that do not follow retrieval gains: evaluate evidence coverage
  and grounded answer accuracy separately.

## Rollout

Canary new retrieval paths behind a router. Preserve the lexical baseline,
per-query budgets and a kill switch. Promote only when paired replay shows gains
on the intended slice without unacceptable latency, cost or leakage regressions.

