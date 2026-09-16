---
id: pattern-evaluation-operations-and-economics
type: pattern
title: Evaluation Operations, Resilience, and Economics
status: reviewed
privacy: internal
confidence: 0.84
created_at: 2026-09-16T21:20:44+02:00
updated_at: 2026-09-16T21:20:44+02:00
review_at: 2026-12-16
source_ids:
  - source-evaluation-consulting-research-2026
  - source-agent-evaluation-research-2026
  - source-domescobar-agentic-runtime-techniques
relations:
  - predicate: applies_to
    target: pattern-evidence-first-agent-evaluation
  - predicate: applies_to
    target: pattern-online-evaluation-and-rollout
  - predicate: applies_to
    target: pattern-runtime-safety-baseline
---

# Evaluation Operations, Resilience, and Economics

## Scope

Use this pattern after metric meaning, datasets and hard gates are defined. It
connects evaluation to production traces, resilience tests, cost allocation and
incident response. It is not a Python/testing curriculum, an observability
vendor catalog or a substitute for workload-specific SLOs.

## Trace and sampling contract

Emit OpenTelemetry-compatible spans or an equivalent open schema for request,
model, retrieval, tool, checkpoint, judge and side-effect boundaries. Preserve
release/run/tenant pseudonym, case/slice, model and prompt identity, tool call
and causal IDs, terminal reason, latency, tokens, cost and evaluator result.
Do not log hidden reasoning or unrestricted content.

Keep deterministic safety and accounting events at full coverage. Sample rich
payloads by declared policy: retain errors, rare/high-risk slices and canaries;
use bounded representative sampling for routine successes. Products such as
Langfuse, LangSmith and Phoenix are storage/analysis choices. Select them by
schema fidelity, exportability, privacy, sampling controls, replay support and
operating model; product adoption does not validate a metric.

## Reliability and chaos evaluation

Test timeout, rate limit, malformed response, partial tool success, duplicate
delivery, dependency outage, checkpoint crash, lease loss, queue backlog and
recovery after schema migration. Validate bounded retry/backoff, circuit
open/half-open behavior, idempotency, compensation and explicit degraded-mode
semantics. Load tests preserve workload mix and model/provider quotas while
measuring p50/p95/p99 latency, saturation, error class, queue age, cost and
quality gates. Chaos tests run in isolated or shadow environments first and
carry stop conditions; they must not create uncontrolled external effects.

## FinOps decision contract

Attribute model, retrieval, tool, judge, retry and storage cost to request,
tenant, workload slice and release. Report cost per request and per successful
outcome separately; averages must retain denominators and tail slices. Enforce
per-run and aggregate budgets with warning and hard-stop owners. Measure cache
ROI as avoided cost and latency minus cache infrastructure, invalidation,
staleness and quality-regression cost. A cheaper fallback wins only if its
quality, safety and degraded-mode contract pass the same gates.

## Incident-to-evaluation loop

Detection starts from explicit SLO/error-budget burn or hard-gate events.
Runbooks identify containment, kill switch, rollback unit, evidence capture,
communications and authority. Postmortems separate agent, evaluator, data,
runtime and infrastructure causes. Convert reviewed incidents into development
and regression cases, preserve protected holdouts, and verify the fix through
offline replay, shadow traffic and bounded canary before closing the action.

## Minimum evidence

- trace-schema and retention test, including redaction and dropped-span rate;
- paired baseline/candidate results by quality, safety, latency and cost;
- retry/circuit/idempotency and checkpoint-recovery fault injection;
- tenant/request cost reconciliation and budget-kill test;
- alert precision, detection delay, rollback rehearsal and postmortem-derived
  regression replay.

## Exclusions

Do not add a vendor-specific page unless a concrete architecture decision needs
one. Do not turn general Python, Git, pandas or portfolio-writing education into
canonical architecture knowledge. Do not publish universal alert thresholds,
cost targets or chaos schedules without workload evidence.
