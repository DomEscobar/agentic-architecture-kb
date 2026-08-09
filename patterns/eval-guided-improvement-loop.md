---
id: pattern-eval-guided-improvement-loop
type: pattern
title: Eval-guided Bounded Improvement Loop
status: reviewed
privacy: internal
confidence: 0.87
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-11-09
source_ids:
  - source-domescobar-eval-oigl
  - source-domescobar-agentic-eval-research
  - source-agent-evaluation-research-2026
relations:
  - predicate: derived_from
    target: source-domescobar-eval-oigl
  - predicate: derived_from
    target: source-domescobar-agentic-eval-research
  - predicate: derived_from
    target: source-agent-evaluation-research-2026
---

# Eval-guided Bounded Improvement Loop

## Control loop

```text
accepted baseline
 -> select failing development slices
 -> diagnose from bounded traces
 -> propose one typed mutation
 -> validate patch surface and policy
 -> development + regression evaluation
 -> candidate-selection comparison
 -> archive candidate and evidence
 -> independent full + confirmation on hidden promotion gates
 -> human acceptance
 -> canary
 -> promote or rollback
```

## Separate mutation modes

- **Prompt/config:** prompt text, routing thresholds, retrieval depth, model or
  tool policy within a typed schema.
- **Code patch:** application or agent scaffold files within an allowlist, with
  executable tests and forbidden evaluator/guardrail files.
- **Dataset:** never part of the same automatic optimization transaction;
  changes alter metric meaning and require review/versioning.

## Non-negotiable boundaries

- The optimizer cannot read hidden expected outputs or detailed holdout errors.
- Evaluator, policies, hidden tests and acceptance logic are read-only to the
  candidate patcher.
- Every candidate stores parent, diff, rationale, model/config identities,
  traces, scores, cost and terminal reason.
- Hard safety or privacy regressions reject regardless of aggregate gain.
- Compare against the same baseline, dataset and environment identity.
- Ambiguous deltas require repeated evidence; one successful replay is not an
  improvement.
- Promotion has a kill switch, bounded canary and automatic rollback trigger.

## Selection

Do not collapse all objectives into one score. First apply hard gates, then use
a declared ordering or Pareto frontier over quality, safety, latency and cost.
Report slice regressions even when the aggregate improves.

## Stopping conditions

- target quality reached without gate regression;
- budget exhausted;
- no improvement beyond epsilon for declared patience;
- variance or judge disagreement makes ranking unreliable;
- repeated invalid/reverted patches;
- policy violation or evaluator-integrity event.

## Fit

Use this loop only where the mutable surface is bounded and outcome evidence is
strong. It is unsuitable when correctness depends mainly on an uncalibrated
LLM judge, the environment cannot be reset, or hidden promotion data cannot be
protected.
