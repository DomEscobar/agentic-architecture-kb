---
id: synthesis-agentic-runtime-techniques
type: synthesis
title: Agentic Runtime Techniques
status: reviewed
privacy: internal
confidence: 0.82
created_at: 2026-08-08T16:45:00+02:00
updated_at: 2026-08-08T16:45:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-agentic-runtime-techniques
relations:
  - predicate: derived_from
    target: source-domescobar-agentic-runtime-techniques
---

# Agentic Runtime Techniques

## Core claim

A runtime is not a single agent loop. The smallest useful architecture combines
exactly **one primary control loop** with the cross-cutting layers required by
risk, duration, and operating environment. More loops and more agents are not an
automatic improvement.

## A. Control loops

### 1. Action loop

`observe -> reason/plan -> act -> observe -> stop/repeat`

For short, interactive tool tasks. Requires tool contracts, error handling, a
stop condition, and hard budgets. Insufficient by itself for long-running,
irreversible, or correctness-critical work.

### 2. Plan and execute

`plan -> execute step -> observe -> revise -> next step`

For multi-stage work with visible progress. Store the plan as a versioned
artifact and detect stale plans. Do not use when the task is solvable in one
step or is primarily exploratory.

### 3. Verifier loop

`attempt -> deterministic check -> fix/finish/escalate`

For tasks with verifiable acceptance criteria. Tests, schemas, and invariants
take precedence over an LLM judge. Verifier independence and retry limits are
necessary because a weak checker legitimizes false completion.

### 4. Bounded retry

`bounded attempt -> explicit result/failure -> retry/fresh context/escalate`

Time, cost, step, and context limits make failure an explicit state. Transfer
only typed state between attempts; otherwise a fresh context carries the same
errors forward.

### 5. Reflection and memory

`act -> evaluate -> candidate lesson -> validate/promote -> reuse`

Reflections must not be written directly to canonical memory. Promotion requires
repeated evidence, provenance, expiry, and rollback.

### 6. Research loop

`question -> query batch -> read -> claim/evidence ledger -> gap analysis -> repeat`

The decisive runtime component is the claim/evidence ledger, not web access.
Stop when core claims are covered, the budget is exhausted, or no new evidence
appears.

### 7. Experiment loop

`propose -> isolated run -> measure -> paired comparison -> keep/revert`

Use only with a fixed baseline, controlled variance, and immutable experiment
log. One successful run is insufficient for promotion.

### 8. Multi-agent orchestration

`decompose -> typed tasks -> isolated workers -> typed results -> review/merge`

Use only when separate contexts, tools, authorities, or genuine parallelism
outweigh coordination cost. Bound depth, turns, and fan-out; make ownership and
merge semantics explicit.

### 9. Durable runtime

`load -> work -> checkpoint -> wait -> resume`

Requires a persistent state machine, idempotent steps, lease or single-runner
semantics, retry/backoff, migrations, and recovery semantics. A long chat turn is
not a durable workflow.

### 10. Coding harness

`isolate -> edit -> test -> review -> merge/revert`

Git diffs, worktree or branch isolation, executable checks, review, and rollback
form the runtime boundary. Without strong tests, even multi-agent review remains
weak.

## B. Cross-cutting runtime layers

1. **Test-time compute:** generate multiple candidates only under a hard compute
   budget and with a reliable selector.
2. **HITL/governance:** model risky actions as resumable interrupts, not informal
   questions.
3. **Security/capabilities:** enforce trust zones, least privilege, and an action
   firewall before tool execution.
4. **Context/memory:** packing, paging, retrieval caps, promotion, and forgetting.
5. **Harness/composition:** separate the agent core from session, UI, queue, and
   persistence.
6. **Protocols:** use MCP/A2A only at boundaries that genuinely require
   portability or remote interoperability.
7. **Observability/provenance:** append-only events, run receipts, claim and
   artifact IDs, and replayable state transitions.
8. **Cost/serving:** budgets, model routing, caching, and latency SLOs as runtime
   policy rather than prompt suggestions.

## Composition rule

```text
request
  -> identity + trust classification
  -> capability + budget policy
  -> one primary control loop
  -> verifier / approval where required
  -> append-only events + checkpoints
  -> result with provenance
```

## Evidence status

The taxonomy is a useful synthesis but has not been experimentally validated as
a whole. Individual techniques have different evidence strength. In particular,
2026 patterns from isolated preprints remain hypotheses or candidates until
independent replication or local evaluations exist.
