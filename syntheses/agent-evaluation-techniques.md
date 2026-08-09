---
id: synthesis-agent-evaluation-techniques
type: synthesis
title: Agent Evaluation Techniques
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-10-09
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

# Agent Evaluation Techniques

## What must be evaluated

Agent evaluation is not a single answer score. It spans:

1. task and dataset validity;
2. external outcome/state correctness;
3. safety, permissions and side effects;
4. evidence provenance and causal trace integrity;
5. routing, planning, recovery and termination diagnostics;
6. robustness under repeats and perturbations;
7. latency, calls, tokens and cost;
8. evaluator/judge reliability;
9. regression and promotion evidence.

## Technique ladder

Start with the cheapest reliable oracle and add ambiguity handling only where
needed:

```text
schema/invariant checks
 -> environment state and executable tests
 -> trace causality and forbidden-action gates
 -> reference/rubric scoring
 -> calibrated LLM judge
 -> environment-aware Agent-as-a-Judge
 -> human adjudication for disagreement/high risk
```

## Outcome versus process

Outcome decides whether the task succeeded. Process evidence diagnoses why and
enforces critical constraints. Process should become a decisive gate only for
safety, compliance, causal validity or an explicitly required mechanism.
Otherwise, demanding one reference trajectory can reject legitimate solutions.

## Online and offline loop

- **Offline:** frozen cases, repeats, perturbations, judge calibration,
  baseline comparison and hidden promotion gates.
- **Replay:** production-derived traces executed against versioned simulators or
  fixtures without reusing unsafe side effects.
- **Online:** sampled telemetry, deterministic invariants, canary comparison,
  user correction and incident capture.
- **Dataset maintenance:** cluster production failures, review new cases,
  monitor slice coverage and rotate exposed holdouts.

## Recommended OIGL next steps

1. Add explicit `development`, `selection`, `holdout` and `redteam` split
   contracts with information-flow tests.
2. Create an evaluator-validation pack containing known-good, known-bad,
   trace-tampered and ambiguous attempts.
3. Calibrate every LLM-judge rubric against human labels; record criterion-wise
   confusion and disagreement.
4. Add repeat-aware confidence and flakiness reporting instead of assuming one
   confirmation is sufficient.
5. Add environment snapshot/reset identity and separate infrastructure errors.
6. Treat eval-pack changes as metric-semantic changes requiring review and a
   new baseline lineage.
7. Add private project-local cases before making capability or improvement
   claims.

## Current verdict on OIGL

OIGL already has a stronger acceptance and provenance model than many basic
eval runners: mechanical-first scoring, pack identity, causal traces, receipts,
confirmation and explicit acceptance are implemented. The main missing layer
is not another scorer collection. It is empirical validation of the evaluator
itself, protected dataset splits, repeat statistics and environment-grounded
oracles on real project cases.
