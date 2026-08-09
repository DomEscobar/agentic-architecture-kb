---
id: pattern-evaluation-consulting-intake
type: pattern
title: Evaluation Consulting Intake and Decision Process
status: reviewed
privacy: internal
confidence: 0.91
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-11-09
source_ids:
  - source-evaluation-consulting-research-2026
relations:
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
---

# Evaluation Consulting Intake and Decision Process

## Intake

Establish user/decision/harm, workload and long tail, available deterministic
state, modalities and effects, provenance/freshness/privacy, current system and
traces, latency/cost/scale, obligations, incidents and team maturity before
recommending metrics or tools.

## Brownfield audit

1. Inventory prompts, models, tools, datasets, scorers, environments and gates.
2. Reproduce the last baseline from immutable identities.
3. Trace representative successes and failures end to end.
4. Validate cases, oracles and judges with known controls.
5. Check leakage, duplication, contamination and holdout access.
6. Separate system, evaluator, infrastructure and data failures.
7. Compare offline gates with production incidents and corrections.
8. Produce a risk-ranked gap register before proposing migration.

## Greenfield design

1. Define user outcome and unacceptable effects.
2. Build 20–50 reviewed seed cases across dominant/high-risk slices.
3. Implement deterministic outcome and safety gates first.
4. Add trace diagnostics only where actionable.
5. Add calibrated judges for residual semantic criteria.
6. Freeze identities, artifacts and split access.
7. Establish paired regression, confirmation and human acceptance.
8. Add shadow/canary telemetry and rollback before more autonomy.

## Deliverables

Evaluation Strategy, Dataset Card, metric/oracle registry, evaluator validation,
baseline scorecard, go-live gates, rollout/rollback, ownership and unresolved
evidence register.
