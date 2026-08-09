---
id: pattern-agent-memory-consulting-intake
type: pattern
title: Agent Memory Brownfield Audit and Greenfield Intake
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-foundations-2026, source-agent-memory-systems-2026, source-agent-memory-evaluation-security-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-foundations-2026
  - predicate: derived_from
    target: source-agent-memory-systems-2026
---

# Agent Memory Brownfield Audit and Greenfield Intake

## Intake variables

Establish users/tenants, workloads, memory purpose, data classes, horizon,
freshness, acceptable false recall, correction authority, deletion SLA,
latency/cost budget, deployment, compliance, action risk and operating maturity.

## Brownfield audit

Trace representative memories from observation through write, update,
retrieval, use and deletion. Inventory stores, indexes, caches, graphs, traces,
backups, models, prompts, schemas and access boundaries. Reproduce stale facts,
conflicts, leaks, poison writes, failed deletes and crash recovery. Baseline
quality by lifecycle stage rather than relying on end-QA.

## Greenfield decision

Start with checkpointed run state, append-only events, versioned records and
FTS. Add semantic retrieval for demonstrated paraphrase recall; add a temporal
graph for relationship/time queries; add autonomous consolidation only with
provenance and promotion gates; add procedures only with executable validation.
The smallest design that passes workload and risk gates wins.

