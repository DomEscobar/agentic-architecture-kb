---
id: pattern-agentic-corrective-retrieval
type: pattern
title: Agentic and Corrective Retrieval
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T18:20:00+02:00
updated_at: 2026-08-08T18:20:00+02:00
review_at: 2026-11-08
source_ids:
  - source-rag-developments-2026-batch-1
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-1
---

# Agentic and Corrective Retrieval

## Minimal adaptive controller

```text
classify query
 -> no retrieval | single retrieval | decomposed retrieval
 -> assess evidence sufficiency
 -> answer | rewrite/retry | alternate source | abstain/escalate
```

The controller owns budgets and state. Retrieval tools remain deterministic
services where possible.

## Distinct mechanisms

- **Adaptive/router RAG:** chooses pipeline complexity from query features.
- **CRAG:** evaluates retrieved evidence and triggers correction or web fallback.
- **Self-RAG:** a specially trained model emits reflection tokens to decide when
  to retrieve and critique evidence/output.
- **Agentic retrieval:** a runtime plans subqueries, calls sources iteratively,
  tracks coverage and stops under explicit criteria.

These names should not be collapsed into a generic “agent loop”.

## Winning conditions

- queries vary substantially in complexity and source needs;
- multi-source or multi-hop evidence is common;
- failed first retrieval can be detected with useful precision;
- added latency and token cost are justified by task value.

## Controls

- hard limits for iterations, subqueries, sources, tokens, time and spend;
- typed evidence ledger and coverage by sub-question;
- no-progress and duplicate-query detection;
- untrusted web/tool content remains data, never policy;
- external-source fallback respects privacy and authorization;
- abstention when the evaluator is uncertain;
- trace every rewrite, route, retrieval and stop decision.

## Evaluation

Compare against a fixed hybrid+rereanker baseline and slice simple versus
complex queries. Measure answer/evidence accuracy, correction precision,
unnecessary-retrieval rate, steps, latency, cost and failure recovery. A gain on
complex cases can still lose overall if the router overuses expensive paths.
