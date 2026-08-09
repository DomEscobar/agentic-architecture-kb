---
id: pattern-agent-memory-framework-selection
type: pattern
title: Agent Memory Framework Selection
status: reviewed
privacy: internal
confidence: 0.86
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-systems-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-systems-2026
---

# Agent Memory Framework Selection

- LangGraph wins when recoverable tool execution, checkpoints, replay and HITL
  dominate. Build the memory lifecycle explicitly.
- Letta wins when the agent must actively manage a visible self/user memory and
  platform coupling is acceptable. Add admission controls for writes.
- Mem0 wins as an embeddable fact-extraction/retrieval service. Pin version and
  evaluate current ADD-only behavior and deletion lineage.
- Graphiti/Zep wins for temporal entity relationships and provenance. Test
  extraction quality, tenant namespaces and semantic erasure.
- Client-owned files win for minimal transparent memory. Add schema, ACL,
  search, versioning and backups.
- Provider conversation state wins only for conversation continuity; do not
  represent it as a complete memory architecture.

Score candidates against workload success, write correctness, update/conflict
semantics, recovery, deletion coverage, privacy, latency, cost, portability and
operational burden. Vendor benchmark deltas are hypotheses until reproduced
under identical models, budgets, corpus and evaluator.

