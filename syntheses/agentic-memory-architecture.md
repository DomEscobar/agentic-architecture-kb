---
id: synthesis-agentic-memory-architecture
type: synthesis
title: Agentic Memory Architecture and Lifecycle
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids:
  - source-agent-memory-foundations-2026
  - source-agent-memory-systems-2026
  - source-agent-memory-evaluation-security-2026
relations:
  - predicate: derived_from
    target: source-agent-memory-foundations-2026
  - predicate: derived_from
    target: source-agent-memory-systems-2026
  - predicate: derived_from
    target: source-agent-memory-evaluation-security-2026
---

# Agentic Memory Architecture and Lifecycle

## Definition

Agentic memory is a governed lifecycle, not a vector database:

`observe -> qualify -> write -> consolidate -> retrieve -> use -> verify/correct -> supersede/forget`

Memory must improve future decisions under explicit correctness, privacy,
latency and deletion constraints. Raw transcript accumulation is not memory.

## Storage classes

1. Run state: current plan, variables, permissions and commit state; loaded
   deterministically and checkpointed.
2. Event/action ledger: append-only observations, actions, outcomes and side
   effects with actor, time and provenance.
3. Episodic memory: compact, source-linked summaries of relevant events.
4. Semantic memory: versioned claims, preferences and constraints.
5. Procedural memory: verified workflows or skills with preconditions,
   dependencies, evidence and kill switch.
6. Entity-temporal memory: relations with event time, ingestion time and
   validity intervals; add only when relational queries justify it.
7. Derived indexes: lexical, vector and graph projections rebuilt from the
   canonical stores.

## Minimal reference architecture

```text
durable run state
  -> append-only event/action ledger
  -> extraction into quarantined candidates
  -> policy and evidence admission
  -> versioned fact store / verified skill registry
  -> optional temporal graph
  -> rebuildable lexical, vector and graph indexes
  -> retrieval policy enforcement and evidence packet
  -> outcome logging, correction, supersession and verified erasure
```

No single audited framework supplies every layer. Start with records and FTS;
add embeddings, graph structure or autonomous consolidation only after a
workload eval shows material benefit.

## Non-negotiable invariants

- Run state is not long-term personal memory.
- An extracted claim never replaces its source event.
- Add, amend, supersede and delete are distinct operations.
- Tenant, privacy and validity filters run before semantic ranking.
- Conflicts remain inspectable; materialized current truth is reconstructable.
- Procedures are executable artifacts and require stronger admission than facts.
- Delete covers canonical and derived artifacts and produces a verified receipt.
- Quality scores cannot compensate for privacy, safety or forbidden-side-effect failures.

