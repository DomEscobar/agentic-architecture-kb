---
id: synthesis-reward-integrity-in-agent-evaluations
type: synthesis
title: Reward Integrity in Agent Evaluations
status: reviewed
privacy: internal
confidence: 0.84
created_at: 2026-09-14T08:39:00+02:00
updated_at: 2026-09-16T21:20:44+02:00
review_at: 2026-10-14
source_ids:
  - source-benchshield-reward-integrity-2026
  - source-agent-evaluation-research-2026
relations:
  - predicate: derived_from
    target: source-benchshield-reward-integrity-2026
  - predicate: applies_to
    target: pattern-evidence-first-agent-evaluation
  - predicate: applies_to
    target: pattern-rsi-evidence-boundary
---

# Reward Integrity in Agent Evaluations

## Decision rule

A passing task score is insufficient for promotion when the evaluated agent can
influence evaluator inputs, reward-relevant artifacts or scoring
infrastructure. Record outcome and integrity verdict separately; admit a score
to optimization or promotion only when the declared integrity boundary is
supported. Enforce forbidden channels and authority transitions, not one golden
trajectory.

## Minimum contract

1. Keep evaluator code/configuration, hidden references, reward collection and
   evidence recording outside the agent's writable authority. Treat executable
   handoffs as agent-controlled even when mounted into an isolated verifier.
2. Seal run/task/baseline identity, ordered lifecycle events, artifact and
   evaluator-input hashes, reward producer/value, errors and feedback release.
   Check sequence and artifact-to-input binding, not hash presence alone.
3. Distinguish checked-within-scope, exposed-without-observed-use,
   attempted/observed violation and inconclusive. Missing or conflicting
   evidence must not become a clean pass.
4. Check structural transitions and provenance deterministically. Keep semantic
   adequacy as a separately calibrated review; a judge cannot rewrite
   infrastructure facts.

## Evaluation and rollout

Use paired honest/exploit cases covering evaluator mutation, hidden-reference
access, handoff substitution, forged reward/logs, missing or reordered events,
fail-open errors and benign unconventional solutions. Measure unauthorized
accepted rewards, honest-run false violations, abstention/coverage and semantic
review disagreement by slice.

Replay sealed receipts against pinned checker versions without rerunning side
effects. Checker upgrades create a new verdict lineage. Start deployment in
shadow mode and canary; quarantine violated or inconclusive rewards from
training/promotion datasets. The kill switch suspends reward admission, not
merely the agent prompt.

## Boundary

This pattern applies to tool/coding agents and bounded self-improvement where
reward can be manipulated. It is not automatic RAG or memory coverage and does
not imply that BenchShield's reported accuracy, cost or lifecycle transfers to
the target system.
