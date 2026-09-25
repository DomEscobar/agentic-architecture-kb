---
id: pattern-rsi-evidence-boundary
type: pattern
title: Recursive Self-Improvement Evidence Boundary
status: reviewed
privacy: public
confidence: 0.81
created_at: 2026-08-12T18:42:00+02:00
updated_at: 2026-09-04T13:52:00+02:00
review_at: 2026-10-12
source_ids:
  - source-bounded-self-improvement-2025-2026
  - source-harnessdev-agent-harness-evolution-2026
relations:
  - predicate: derived_from
    target: source-bounded-self-improvement-2025-2026
  - predicate: derived_from
    target: source-harnessdev-agent-harness-evolution-2026
  - predicate: applies_to
    target: pattern-eval-guided-improvement-loop
---

# Recursive Self-Improvement Evidence Boundary

## What is demonstrated

DGM is evidence that an archived population of coding-agent variants can modify
its agent implementation and discover variants that score better on the tested
coding benchmarks. This is genuine self-referential agent improvement within a
bounded domain and evaluator.

## What is not demonstrated

It does not prove domain-general RSI, indefinite improvement, safe objective
evolution, autonomous production deployment, or that a better task agent is
also a better future optimizer. Prompt/config optimization alone is not RSI.

## Required RSI test

Generation N must produce a statistically supported improvement on untouched
tasks. Then, under equal search budget and information, generation N must also
produce better N+1 candidates than its predecessor. Evaluator and task-set
identity remain fixed during that comparison.

## Evaluator evolution

Changing the objective invalidates direct before/after claims. If utility must
evolve, use explicit epochs: freeze evaluation within each epoch, audit old/new
objective compatibility at the boundary, retain old sentinels and require human
approval. Treat recent co-evolving-evaluator research as experimental only.

## Harness evolution gate

Model-external harness editing can create useful reusable capability without
changing model weights, but a higher score on the feedback set is not retained
improvement. Freeze each harness version, hold the executor and evaluator fixed,
and test untouched tasks before attribution. Repeat across intended executors
because a harness can overfit to the model that created or first executed it.

HarnessDev's negative transfer and unstable version-selection results support
this gate but do not demonstrate recursive self-improvement. An RSI claim still
requires the improved generation to produce better future candidates under
equal search budget and information. Harness source that declares memory,
verification or recovery is evidence of implementation only; trace activation
and outcome ablations are needed to establish an effective mechanism.

SoL-Pi adds supporting evidence for the search process rather than for recursive
self-improvement. It fixed its acceptance gates outside the optimizing agent's
control, kept held-out results out of the search loop, and reported efficiency
gains at a measured capability cost, including fewer solved tasks than the base
harness on one benchmark (`source-sol-pi-harness-auto-research-2026`). A harness
that spends fewer tokens while solving fewer tasks is an operating-point choice,
not an improved generation.
