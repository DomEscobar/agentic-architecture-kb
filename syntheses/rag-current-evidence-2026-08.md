---
id: synthesis-rag-current-evidence-2026-08
type: synthesis
title: Current RAG Evidence August 2026
status: reviewed
privacy: internal
confidence: 0.86
created_at: 2026-08-08T18:55:00+02:00
updated_at: 2026-08-08T18:55:00+02:00
review_at: 2026-10-08
source_ids:
  - source-rag-developments-2026-batch-1
  - source-rag-developments-2026-batch-2
  - source-rag-radar-2026-08
relations:
  - predicate: derived_from
    target: source-rag-radar-2026-08
---

# Current RAG Evidence — August 2026

## What is holding up

- Exact/lexical retrieval remains a first-class baseline, especially for names,
  identifiers, numeric and terminology-heavy questions.
- Dense retrieval remains useful for paraphrase and semantic mismatch.
- Fusion and reranking often help, but only after candidate-depth, truncation,
  domain and latency tuning; they can regress quality.
- Structure-aware and visual retrieval address real failure classes that text
  chunks cannot recover after destructive parsing.
- Agentic retrieval earns its cost for decomposable multi-source and multi-hop
  queries, not routine fact lookup.
- Long context is an evaluated branch, not an excuse to skip evidence selection.
- Stage-local metrics plus final grounded task success are necessary; neither
  retrieval nor answer scores alone diagnose the system.

## Recommended evaluation matrix

Every case should compare at least:

1. exact/SQL/metadata lookup where applicable;
2. BM25;
3. dense retrieval;
4. measured hybrid fusion;
5. the best candidate path with and without reranking;
6. long/full-context baseline when the corpus fits;
7. specialist branch only for its target slice.

Slice by exact identifiers, paraphrase, multi-hop, tables, visual layout,
negation/polarity, temporal freshness, conflicts, insufficient evidence,
cross-tenant attempts and corpus growth. Report Recall/nDCG, evidence coverage,
grounded task success, unsupported claims, latency and cost together.

## Architecture consequence

Use a query router only when the eval matrix identifies distinct winning paths.
Keep deterministic filters before probabilistic ranking. Preserve source-native
evidence and stable citation anchors. Put every expensive or learned branch
behind budgets, tracing, feature flags and a fallback to the simplest passing
baseline.

## Open questions

- How well do recent scaling results transfer to multilingual and multimodal
  corpora?
- When does generator-aware utility survive a generator/model upgrade?
- Can visual multi-vector compression retain answer quality on small-text and
  table-calculation slices?
- Which online signals detect retrieval drift without rewarding fluent but
  unsupported answers?
- What independent evidence exists for managed agentic-retrieval cost and
  reliability claims?

