---
id: pattern-runtime-safety-baseline
type: pattern
title: Runtime Safety Baseline
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

# Runtime Safety Baseline

This baseline applies regardless of the selected agent framework.

## Before the run

- Record the original intent immutably.
- Determine user, project, and privacy scope.
- Label context as trusted instruction, trusted data, or untrusted evidence.
- Issue minimal, time-limited capabilities.
- Set budgets for time, tokens, cost, calls, delegation depth, and fan-out.

## During the run

Separate conversational checkpoints from external side effects. Non-idempotent
effects need runtime-generated causal IDs, commit-time authority checks, and a
transactional or reconcilable effect ledger; replaying chat state is
insufficient.

- Record every state transition and tool attempt in an append-only log.
- Validate tool arguments against schema and policy.
- Recheck proposed actions against the original intent and trust zone.
- Protect side effects with idempotency keys or saga/compensation semantics.
- Enforce no-progress, repetition, and budget breakers.
- Use a resumable approval interrupt before risky or irreversible actions.

## After the run

- Let a verifier decide against explicit acceptance criteria.
- Include referenced inputs/outputs, tool results, cost, state transitions, and
  provenance in the run receipt.
- Redact secrets and private content according to policy.
- Write memory lessons only as inbox candidates.
- Test recovery, replay, and rollback paths regularly.

## Minimum evaluations

- Prompt injection through tool output, web pages, and memory
- Capability escalation and cross-project access
- Duplicate delivery and crash between side effect and checkpoint
- Infinite loops, no progress, and budget overruns
- Faulty verifier and false completion report
- Replay after schema or state migration
- Deletion of a memory entry across all projections
