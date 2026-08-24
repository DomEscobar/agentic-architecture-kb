---
id: pattern-agentic-corrective-retrieval
type: pattern
title: Agentic and Corrective Retrieval
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T18:20:00+02:00
updated_at: 2026-08-24T10:40:00+02:00
review_at: 2026-11-08
source_ids:
  - source-rag-developments-2026-batch-1
  - source-mistral-agentic-search-2026
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-1
  - predicate: derived_from
    target: source-mistral-agentic-search-2026
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

## Navigable source tool contract

For long documents, give the controller two distinct surfaces:

- global ranked discovery returning a stable opaque chunk ID, source ID and
  positional locator; and
- deterministic source-local operations to open the hit, move to adjacent
  chunks, read an exact half-open range and grep within that source.

The controller, not the model prompt, owns a set of seen result IDs. Each
iteration excludes or deduplicates those IDs and terminates when retrieval
produces no unique evidence. Backends that advertise exclusion still require
an end-to-end contract test; a query-model field that is not reachable from the
agent tool does not prevent loops.

Keep search and navigation read-only for ordinary agent runs. Ingestion and
deletion belong behind a separate administrative authority, with source and
tenant authorization applied before both ranked search and local navigation.
Treat local indexing, remote OCR and remote embedding as separate privacy and
egress decisions.

## Winning conditions

- queries vary substantially in complexity and source needs;
- multi-source or multi-hop evidence is common;
- failed first retrieval can be detected with useful precision;
- added latency and token cost are justified by task value.

## Controls

- hard limits for iterations, subqueries, sources, tokens, time and spend;
- typed evidence ledger and coverage by sub-question;
- no-progress and duplicate-query detection;
- stable source-local offsets and controller-owned seen-result deduplication;
- untrusted web/tool content remains data, never policy;
- external-source fallback respects privacy and authorization;
- abstention when the evaluator is uncertain;
- trace every rewrite, route, retrieval and stop decision.

## Evaluation

Compare against a fixed hybrid+rereanker baseline and slice simple versus
complex queries. Measure answer/evidence accuracy, correction precision,
unnecessary-retrieval rate, steps, latency, cost and failure recovery. A gain on
complex cases can still lose overall if the router overuses expensive paths.

For navigable retrieval, additionally test search-to-open identity, neighbour
ordering, range boundaries, source/tenant isolation, source-local grep,
zero-new-evidence termination and denial of mutation tools to read-only runs.
