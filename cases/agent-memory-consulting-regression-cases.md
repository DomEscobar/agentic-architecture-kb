---
id: case-agent-memory-consulting-regressions
type: case
title: Agent Memory Consulting Regression Cases
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-foundations-2026, source-agent-memory-systems-2026, source-agent-memory-evaluation-security-2026]
relations:
  - predicate: evaluated_by
    target: pattern-agent-memory-evaluation-blueprint
---

# Agent Memory Consulting Regression Cases

Each answer must state assumptions, minimum architecture, failure detection,
evaluation, rollout/rollback and alternatives.

1. Personal assistant: preferences change over years; private email is
   untrusted; user demands correction and deletion.
2. Tool agent: resume after crashes without replaying payments; remember local
   workflow constraints across sessions.
3. Enterprise multi-tenant support: shared product knowledge plus isolated
   customer histories and zero cross-tenant retrieval.
4. Coding agent: learn repository procedures while APIs, branches and tests
   change; reject stale or unsafe skills.
5. Healthcare-adjacent assistant: contested temporal facts, strict provenance,
   human approval and abstention.
6. Multi-agent research: agents share findings without allowing one poisoned
   source to become authoritative collective memory.
7. Existing vector-only memory: high recall but stale preferences, duplicates,
   no correction lineage and unverifiable deletes.
8. Graph proposal: determine whether temporal relationship queries justify
   extraction error, operational cost and deletion complexity.

Fail the consulting regression if the answer recommends a vendor before the
case, treats raw transcripts as canonical memory, omits write authority,
merges run state with durable facts, relies only on QA accuracy, or promises
deletion without lineage-aware verification.

