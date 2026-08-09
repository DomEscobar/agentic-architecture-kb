---
id: pattern-evidence-first-agent-evaluation
type: pattern
title: Evidence-first Agent Evaluation
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-11-09
source_ids:
  - source-domescobar-eval-oigl
  - source-agent-evaluation-research-2026
relations:
  - predicate: derived_from
    target: source-domescobar-eval-oigl
  - predicate: derived_from
    target: source-agent-evaluation-research-2026
---

# Evidence-first Agent Evaluation

## Core pattern

```text
versioned task + environment + policy
 -> repeated agent attempts
 -> final outcome + causal trace + environment state
 -> deterministic invariants and safety gates
 -> calibrated semantic/process judges only for residual ambiguity
 -> slice metrics + uncertainty + artifacts
 -> independent confirmation
 -> explicit acceptance or rejection
```

The unit of evidence is an attempt bound to task version, environment snapshot,
agent/runtime identity, judge identity, policy and evaluator hash.

## Evaluation layers

1. **Task validity:** Is the task real, solvable and unambiguous enough?
2. **Outcome validity:** Did the required external state or answer result?
3. **Safety invariants:** Were forbidden actions, permissions and side effects
   respected? These are hard gates.
4. **Causal grounding:** Can claims and observations be traced to valid calls,
   accessible evidence and the correct time/state?
5. **Process diagnostics:** Routing, retries, recovery, escalation and budgets.
   These explain failure but should not demand one exact successful path.
6. **Efficiency:** Calls, tokens, wall time and cost, reported as a vector or
   Pareto frontier rather than hidden in correctness.
7. **Robustness:** Repeat variance, perturbations, alternate environments and
   failure slices.

## Judge policy

- Use schema checks, database state, executable tests and causal IDs first.
- Use an LLM judge only for criteria that cannot be represented reliably as an
  executable oracle.
- Freeze rubric, prompt, model, decoding configuration and input projection.
- Calibrate each criterion against human labels and adversarial examples.
- Measure agreement, false positives/negatives and instability per slice.
- Abstain or escalate uncertain/disagreeing cases instead of forcing a score.
- An Agent-as-a-Judge may inspect the environment, but its acquired evidence
  and actions must themselves be recorded and evaluated.

## Dataset contract

- visible development set for iteration;
- candidate-selection set not used for mutation feedback;
- hidden holdout used sparingly for promotion;
- separate safety/redteam suite;
- immutable split manifests and content hashes;
- duplicate and semantic-near-duplicate checks across splits;
- case ownership, review record, provenance and expiry;
- production failure promotion goes to development first, not directly into a
  repeatedly exposed holdout.

## Required reports

- pass rate with confidence intervals and repeat distribution;
- results by task/risk/failure slice;
- hard-gate violations separately from quality scores;
- delta against the same baseline identity;
- cost/latency vector;
- judge calibration and disagreement;
- missing/invalid traces and infrastructure failures separated from agent
  failures.

## Failure modes

- **Goodharting:** candidate optimizes visible proxy; detect with hidden gates
  and counterfactual/adversarial cases.
- **Trace theater:** plausible trace without causal correspondence; bind calls,
  observations and state transitions through runtime-generated IDs.
- **Over-specified trajectory:** correct alternative path fails; assert causal
  invariants, not one golden chain unless compliance requires it.
- **Judge drift:** scores change after model/prompt update; hash and re-calibrate.
- **Flaky environment:** agent variance confused with infrastructure variance;
  snapshot/reset state and classify infra failures separately.
- **Contamination:** benchmark memorized or repeatedly exposed; use private and
  rotating holdouts plus fresh executable tasks.
