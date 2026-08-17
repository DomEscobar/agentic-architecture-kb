---
id: source-memory-operational-baselines-and-tenancy-2026-08
type: source
title: Memory Operational Baselines and Tenancy Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.72
created_at: 2026-08-17T08:05:00+02:00
updated_at: 2026-08-17T08:05:00+02:00
review_at: 2026-09-17
source_ids: []
relations: []
---

# Memory Operational Baselines and Tenancy Evidence Audit — August 2026

Primary sources checked on 2026-08-17:

- [ReFind raw-log memory retrieval](https://arxiv.org/abs/2608.12888)
- [Memory serving-cost study](https://arxiv.org/abs/2608.11879)
- [neo4j-agent-memory issue 155](https://github.com/neo4j-labs/agent-memory/issues/155)
- [Owner-scoped agent-memory-dotnet implementation](https://github.com/joslat/agent-memory-dotnet)

## Evidence boundary

ReFind and the serving-cost study are recent author-reported preprints without
public run artifacts at review time. Their numerical rankings and break-even
observations are not admitted as generally transferable results. ReFind is
useful counterevidence to selecting graph or tree memory without an equal-budget
immutable raw-log lexical baseline. The cost study supports stage-level
measurement, not a universal cost ordering.

Issue 155 is an unconfirmed public report whose detailed proof of concept is
not public. The separate .NET implementation demonstrates the plausibility of
owner-scoped controls but is not an independent reproduction of the reported
Neo4j failure. Treat cross-user graph poisoning as a threat hypothesis, not an
accepted product vulnerability.

## Durable recommendation

Compare memory candidates with an immutable event log searched by BM25 plus
temporal narrowing and bounded local expansion under the same model, prompt,
context and reranking budgets. Meter ingest, extraction, retrieval,
consolidation and answer generation separately and report cost per correct
answer. Shared graph memory must stamp and enforce owner or tenant scope on
nodes, edges, facts and derived summaries across read, write, merge, refresh,
consolidation, deletion and rebuild paths.
