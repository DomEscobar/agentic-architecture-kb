---
id: source-multi-domain-agent-latency-2026-09-04
type: source
title: Multi-Domain Agent Latency Owner Report 2026-09-04
status: inbox
privacy: internal
confidence: 0.65
created_at: 2026-09-04T07:22:00+02:00
updated_at: 2026-09-04T07:22:00+02:00
review_at: 2026-10-04
auditability: private
source_ids: []
relations:
  - predicate: applies_to
    target: pattern-selective-multi-domain-retrieval-orchestration
---

# Multi-Domain Agent Latency Owner Report — 2026-09-04

## Reported architecture

An orchestration agent routes requests to multiple domain agents. Each domain
agent performs reasoning and synthesis, then returns to the orchestrator for a
final response. A domain may need iterative discovery when its first retrieval
endpoint does not provide enough evidence. Cross-domain questions can require
fan-out to more than one domain.

## Reported failure

The current system is too slow. The report identifies repeated serial model
stages and per-domain synthesis before orchestration-level synthesis as likely
contributors, but it contains no trace timings, replay set or controlled
comparison. Causality and effect size therefore remain unverified.

## Candidate architecture discussed

```text
request
 -> selective domain routing
 -> parallel domain fan-out
      -> bounded evidence-gap retrieval loop per domain
      -> typed evidence packet
 -> fan-in with deduplication and conflict detection
 -> deterministic policy and security gates
 -> one final synthesis
```

Qwen3-32B in non-thinking mode was proposed as a possible domain controller,
with short structured outputs and thinking-mode escalation only for difficult
cases. This is a model-placement hypothesis, not a durable recommendation.

## Evidence needed

- stage-level p50 and p95 latency, time to first token and token counts;
- routing precision and selected-domain count;
- required-evidence coverage and unsupported-claim rate;
- loop depth, unique-evidence yield and unnecessary follow-up-query rate;
- timeout, incomplete, conflict and safety slices;
- paired replays of the current system, one-shot retrieval and the candidate;
- a smaller-controller comparison against Qwen3-32B.

This record is E1 practitioner evidence. It establishes the case and testable
hypotheses, not the superiority of the candidate design.
