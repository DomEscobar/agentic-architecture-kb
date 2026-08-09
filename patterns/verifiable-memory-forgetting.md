---
id: pattern-verifiable-memory-forgetting
type: pattern
title: Verifiable Memory Forgetting and Erasure
status: reviewed
privacy: internal
confidence: 0.92
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-systems-2026, source-agent-memory-evaluation-security-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-systems-2026
  - predicate: evaluated_by
    target: source-agent-memory-evaluation-security-2026
---

# Verifiable Memory Forgetting and Erasure

Distinguish expiry, retrieval decay, supersession, archival and privacy/legal
erasure. Time decay alone is not forgetting: old facts can remain true and new
facts can be false.

## Erasure protocol

1. Tombstone and synchronously exclude the target from all reads.
2. Resolve lineage across raw events, claims, summaries, embeddings, graph
   nodes/edges, caches, traces and linked procedures.
3. Delete or redact canonical artifacts according to authority and retention.
4. Cascade deletion through derived stores or rebuild them from allowed data.
5. Probe exact text, paraphrases, semantic neighbors, graph neighborhoods and
   cross-session queries.
6. Issue a receipt with scope, artifacts, failures, completion time and backup
   expiry. Retry incomplete cascades.

Measure primary and derived deletion coverage, post-delete retrievability,
inference leakage, deletion latency and rebuild consistency. API success alone
is not evidence of forgetting.

