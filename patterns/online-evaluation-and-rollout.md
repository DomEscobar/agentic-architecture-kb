---
id: pattern-online-evaluation-and-rollout
type: pattern
title: Online Evaluation Canary and Rollback
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-11-09
source_ids:
  - source-evaluation-consulting-research-2026
relations:
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
---

# Online Evaluation, Canary and Rollback

## Rollout ladder

```text
offline replay -> no-effect shadow -> internal cohort
 -> bounded canary by risk/tenant -> staged expansion -> general availability
```

Each stage declares entry evidence, exposure/time budget, success metrics, hard
stops, owner and tested rollback.

## Telemetry and signals

Record release/run identity, workload slice, terminal reason, tool effects,
grounding, latency/cost, corrections and safety events. Apply purpose-bound
redaction/retention; do not log hidden reasoning or unrestricted content.

Use verified outcome/state, safety/privacy/permission violations, abstention,
escalation, retries, duplicate effects, corrections/undo/handover, SLOs and
distribution drift. Clicks, thumbs and conversation length are ambiguous
signals, not standalone correctness.

## Incident and rollback

Turn incidents into reviewed development/redteam cases, not an exposed hidden
holdout. Reproduce, patch, regress and canary again. Rollback restores model,
prompt, tools, retrieval and runtime as one compatible release identity, with
automatic hard-safety triggers and an accountable owner.
