---
id: pattern-selective-multi-domain-retrieval-orchestration
type: pattern
title: Selective Multi-Domain Retrieval Orchestration
status: draft
privacy: internal
confidence: 0.75
created_at: 2026-09-04T07:22:00+02:00
updated_at: 2026-09-04T07:22:00+02:00
review_at: 2026-10-04
source_ids:
  - source-multi-domain-agent-latency-2026-09-04
  - source-adaptive-agentic-retrieval-control-2024-2026
  - source-qwen3-32b-controller-candidate-2026
  - source-retrieval-context-landscape-2026-08
  - source-domescobar-agentic-runtime-techniques
relations:
  - predicate: derived_from
    target: source-multi-domain-agent-latency-2026-09-04
  - predicate: derived_from
    target: source-adaptive-agentic-retrieval-control-2024-2026
  - predicate: derived_from
    target: source-qwen3-32b-controller-candidate-2026
  - predicate: derived_from
    target: source-retrieval-context-landscape-2026-08
  - predicate: depends_on
    target: pattern-agentic-corrective-retrieval
  - predicate: depends_on
    target: pattern-runtime-safety-baseline
  - predicate: evaluated_by
    target: pattern-evidence-first-agent-evaluation
---

# Selective Multi-Domain Retrieval Orchestration

## Fit

Use this pattern when a request may require more than one specialized corpus or
tool boundary, domain selection can be estimated before execution, and some
domains need iterative evidence discovery. Do not use multi-agent fan-out when
a single retriever and one synthesis can meet the evidence contract.

## Flow

```text
request
 -> route to the minimum sufficient domain set
 -> parallel fan-out
      -> retrieve and normalize
      -> assess required-evidence coverage
      -> stop | query a named gap | return incomplete
      -> typed evidence packet
 -> typed fan-in
      -> deduplicate claims and sources
      -> expose conflicts, missing domains and timeouts
 -> deterministic policy and security gates
 -> one final synthesis
```

Each domain branch owns its retrieval state but not the global budget. The
orchestrator owns the request deadline, maximum fan-out, shared token and tool
budgets, cancellation and final answer contract. A branch returns evidence and
status, not a polished response.

## Evidence packet

Require a stable schema containing domain, claims, source identifiers and
locators, publication or observation times where relevant, evidence coverage,
conflicts, unresolved gaps, branch status and resource use. Preserve source
identity through fan-in; never merge citations by text similarity alone.

## Control rules

- route simple requests to no-retrieval or one-shot paths;
- fan out only to domains that can contribute a named required fact;
- parallelize independent branches and cap concurrency;
- let the model propose sufficiency, gaps and next queries;
- let code enforce schemas, seen-result deduplication, no-progress breakers,
  deadlines, permissions, tool allowlists and budgets;
- stop a branch on sufficient evidence, repeated/no-new evidence, deadline or
  exhausted budget, and label partial results `incomplete`;
- invoke an additional semantic reviewer only for declared high-risk or
  conflict cases, and return a typed verdict rather than another full rewrite.

## Failure modes and detection

- **Router under-selection:** required evidence maps to an uncalled domain;
  measure domain recall against labelled requests.
- **Router over-selection:** irrelevant branches consume the tail budget;
  measure unnecessary fan-out and marginal evidence yield.
- **Straggler amplification:** fan-in waits for a low-value branch; trace branch
  deadlines, cancellations and answer-critical dependencies.
- **Independent branch duplication:** domains rediscover the same evidence;
  compare unique source and claim yield after fan-in.
- **Premature sufficiency:** a branch stops with missing required evidence;
  score sufficiency decisions against explicit evidence labels.
- **Synthesis distortion:** the final answer drops qualifiers or hides
  conflicts; compare evidence packets with answer claims and citations.

## Evaluation and rollout

Replay the same requests against the current serial pipeline, a single-domain
baseline and this pattern. Hold models, retrievers and corpus snapshot fixed
before attributing gains to orchestration. Report answer and evidence quality,
domain-routing error, steps, p50/p95 latency, time to first token, cost and
timeout rate by slice.

Start in shadow mode. Canary only the direct and clearly separable
cross-domain slices, retain the old pipeline as rollback, and provide a kill
switch for fan-out and iterative retrieval independently. Promote this draft
only after paired evidence shows that tail-latency savings do not trade away
required-evidence coverage or safety.

## Model placement

Use the smallest controller that passes the routing, gap, stop and structured
output evals. Qwen3-32B non-thinking is one case-specific candidate, not the
pattern default. Its official interface supports a hard thinking-mode switch
and tool use, but those properties do not prove controller quality or latency
fit. Escalate to thinking mode only when deterministic signals or labelled risk
rules require it, and compare against a smaller controller under identical
retrieval and serving conditions.
