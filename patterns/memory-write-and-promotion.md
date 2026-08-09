---
id: pattern-memory-write-and-promotion
type: pattern
title: Controlled Memory Write and Promotion
status: reviewed
privacy: internal
confidence: 0.91
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-foundations-2026, source-agent-memory-evaluation-security-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-foundations-2026
  - predicate: derived_from
    target: source-agent-memory-evaluation-security-2026
---

# Controlled Memory Write and Promotion

## Pipeline

1. Record the immutable source event with actor, timestamp, scope and origin.
2. Qualify retention purpose, expected reuse, novelty, sensitivity and risk.
3. Extract a typed candidate: episode, claim, preference, relation or procedure.
4. Compare with active memory for duplicate, amendment, conflict, correction or
   temporal supersession.
5. Keep candidates quarantined until deterministic validation and required
   approval pass.
6. Promote with provenance, confidence, validity, privacy, retention and model/
   extractor identity.
7. Update rebuildable indexes; never make an index the only copy.

Untrusted documents, emails, tool output and other agents cannot directly
author authoritative preferences, permissions or procedures. High-risk writes
need human approval. Promotion metrics include extraction precision/recall,
fabrication rate, unauthorized-write rate and provenance completeness.

