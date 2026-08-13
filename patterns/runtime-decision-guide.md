---
id: pattern-runtime-decision-guide
type: pattern
title: Runtime Decision Guide
status: reviewed
privacy: internal
confidence: 0.85
created_at: 2026-08-08T16:45:00+02:00
updated_at: 2026-08-08T16:45:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-agentic-runtime-techniques
relations:
  - predicate: derived_from
    target: source-domescobar-agentic-runtime-techniques
---

# Runtime Decision Guide

## Select by dominant requirement

- Short tool task: action loop, stopper, and error handling.
- Multi-stage task: plan-and-execute with typed task state.
- Objectively verifiable result: verifier loop; deterministic checks first.
- Open-ended research: research loop, claim/evidence ledger, and gap analysis.
- Code change: coding harness, isolation, tests, and rollback.
- Background work: durable workflow, queue, checkpoints, and idempotency.
- Risky external action: approval interrupt, audit, and edit/reject path.
- Multiple specialists: supervisor or planner/executor only when roles require
  separate context, tools, authority, or measurable parallelism.
- Recurring sessions: controlled memory promotion and forgetting.
- Difficult reasoning task: test-time compute only with a budget and verifier.

## Decision questions

1. What objective done condition exists?
2. Can a step have an external, financial, or irreversible effect?
3. Must the run survive process failure?
4. Which states must be exactly replayable?
5. Are steps idempotent; if not, what compensation exists?
6. Do roles need separate context, tools, or permissions?
7. What are the maximum time, cost, tool-call, depth, and fan-out budgets?
8. What is the kill switch, and how is the system rolled back?
9. Which offline replays and online signals demonstrate improvement?

## Default

Start with one agent, one primary loop, typed state, deterministic checks, hard
budgets, and a complete trace. Add orchestration only when a concrete evaluation
deficit justifies the additional complexity.
