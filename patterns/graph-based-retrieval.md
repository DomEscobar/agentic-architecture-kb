---
id: pattern-graph-based-retrieval
type: pattern
title: Graph-based Retrieval
status: reviewed
privacy: internal
confidence: 0.87
created_at: 2026-08-08T18:20:00+02:00
updated_at: 2026-08-08T18:20:00+02:00
review_at: 2026-11-08
source_ids:
  - source-rag-developments-2026-batch-1
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-1
---

# Graph-based Retrieval

## Choose the graph for the query class

### Entity/relation graph

Extract entities, claims and relations; retrieve local neighborhoods. Useful for
explicit relationship and multi-hop questions. Main risk: extraction errors
become graph facts.

### Community-summary graph

Cluster the graph and summarize communities at multiple levels. Useful for
global questions such as themes, trends and corpus-wide comparison. Expensive to
index and refresh; summary loss can hide minority evidence.

### Co-occurrence/lazy graph

Build cheap noun-phrase/co-occurrence structure and defer interpretation to
query time. Reduces indexing cost but moves cost and latency into reads.

### Personalized PageRank memory graph

Seed a graph from query-linked entities/passages and diffuse relevance through
relationships. Useful for associative multi-hop retrieval; sensitive to graph
construction, edge weighting and seed quality.

## Default composition

```text
metadata/ACL filter
 -> sparse+dense candidate retrieval
 -> graph expansion only for relational/global query classes
 -> evidence-level rerank and coverage
 -> source passages, not graph summaries alone, feed generation
```

## Winning conditions

- questions repeatedly require relations across passages or corpus-wide themes;
- entities can be resolved with acceptable precision;
- update frequency allows graph maintenance;
- graph-specific evals beat strong hybrid and long-context baselines.

## Losing conditions

- exact lookup or single-passage QA dominates;
- corpus changes rapidly and graph invalidation is expensive;
- names/entities are ambiguous or extraction quality is weak;
- deletion, ACL propagation or provenance cannot be guaranteed.

## Required evaluation

Evaluate local factual, multi-hop, global thematic and negative-premise slices
separately. Measure extraction precision/recall, path validity, source coverage,
answer quality, indexing/update cost, query latency and deletion propagation.
LLM-judge comprehensiveness alone is insufficient.
