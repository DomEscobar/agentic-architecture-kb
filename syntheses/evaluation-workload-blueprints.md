---
id: synthesis-evaluation-workload-blueprints
type: synthesis
title: Evaluation Workload Blueprints
status: reviewed
privacy: internal
confidence: 0.89
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-10-09
source_ids:
  - source-agent-evaluation-research-2026
  - source-evaluation-consulting-research-2026
relations:
  - predicate: derived_from
    target: source-agent-evaluation-research-2026
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
---

# Evaluation Workload Blueprints

## RAG

Corpus/snapshot identity, ACL tests, lexical/dense baselines, Recall@k/nDCG with
relevance sets, evidence coverage, claim support/citations, abstention,
staleness/contradiction, latency and cost. Measure ingestion, retrieval, context
and generation separately plus end to end.

## Tool agents

Outcome/state oracle, capability/arguments, forbidden actions, idempotency,
causal trace, recovery, terminal reason, budgets and permission attacks. A
plausible answer cannot replace the required external effect.

## Coding agents

Immutable task/repository, visible and hidden executable tests, regression,
forbidden evaluator files, diff scope, static checks, fresh/private tasks, cost
and reproducibility.

## Agentic memory

Write precision, recall, update/supersession, temporal validity, contradiction,
selective forgetting, privacy isolation, provenance and long-run utility. Test
the decision not to remember; retaining everything is failure.

## Multi-agent

Outcome, routing/delegation, authority, handoff, duplicate work/effects,
fan-out/cost, containment and recovery. Compare with a single-agent baseline.

## Conversation, multimodal and voice

Conversation needs multi-turn goal resolution, retention, correction,
clarification, escalation and efficiency. Multimodal adds layout/table/OCR and
perceptual grounding; voice adds transcription, speaker/noise/accent,
interruption and timing slices.

## High stakes

Add deterministic policy, approval/dual control, misuse and counterfactual
tests, audit completeness, fail-closed behavior, incident drills and rollback.
LLM-only judging cannot authorize irreversible effects.
