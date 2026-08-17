---
id: pattern-memory-poisoning-defense
type: pattern
title: Memory Poisoning Defense
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-17T08:05:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-evaluation-security-2026, source-memory-operational-baselines-and-tenancy-2026-08]
relations:
  - predicate: derived_from
    target: source-agent-memory-evaluation-security-2026
  - predicate: derived_from
    target: source-memory-operational-baselines-and-tenancy-2026-08
---

# Memory Poisoning Defense

## Trust boundary

External content, tool output, messages, shared-agent memories and model
reflections are untrusted observations. They enter quarantine, not active
personal or procedural memory.

Use schema and allowlist checks, source authentication, tenant isolation,
write-rate limits, provenance, anomaly checks and human approval for sensitive
classes. At retrieval, screen both query and candidate, preserve trust labels
in context and prevent recalled text from acquiring system-level authority.

Red-team delayed triggers, indirect injection, conflicting updates, shared-
memory propagation and sleeper activation. Measure injection, retrieval and
activation success; persistence half-life; blast radius; defense false
positive/negative rates; and clean-utility loss. Kill promotion if forbidden
authority changes or cross-tenant exposure occur.

For shared graph memory, attach owner or tenant scope to nodes, edges, facts and
derived summaries. Exercise identical entity names across two owners and verify
every read, write, merge, refresh, consolidation, deletion and rebuild path.
Missing ownership metadata must fail closed; a query-time filter does not prove
that background graph maintenance preserves scope.
