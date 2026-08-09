---
id: pattern-memory-conflict-temporal-validity
type: pattern
title: Memory Conflict and Temporal Validity
status: reviewed
privacy: internal
confidence: 0.89
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-foundations-2026, source-agent-memory-systems-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-foundations-2026
  - predicate: derived_from
    target: source-agent-memory-systems-2026
---

# Memory Conflict and Temporal Validity

Keep append-only evidence plus a reconstructable current view. Every mutable
claim carries event time, ingestion time, valid-from/to, source, status and a
supersession link. Never overwrite contradictory history silently.

Classify changes as duplicate, extension, correction, temporal transition or
unresolved contradiction. Source authority, freshness and corroboration inform
promotion but do not mechanically collapse contested claims. Measure conflict
detection precision/recall, stale-fact survival, latest-valid-value accuracy,
temporal interval accuracy and cascading invalidation completeness.

A temporal graph wins when relationship history and multi-hop temporal queries
are central. It is unnecessary overhead for simple stable preferences.

