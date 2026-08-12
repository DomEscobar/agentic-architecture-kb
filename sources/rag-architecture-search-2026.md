---
id: source-rag-architecture-search-2026
type: source
title: RAG Architecture Search Evidence 2026
status: reviewed
privacy: public
confidence: 0.82
created_at: 2026-08-12T18:41:00+02:00
updated_at: 2026-08-12T18:41:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# RAG Architecture Search Evidence 2026

Primary sources checked on 2026-08-12:

- [RAISE: RAG Design as an Architecture Search Problem](https://arxiv.org/abs/2605.30029)
- [AutoRAGTuner](https://arxiv.org/abs/2605.02967)
- [GEPA](https://github.com/gepa-ai/gepa)

## Evidence class

RAISE and AutoRAGTuner are recent preprints and therefore E2. They directly
support modular, configuration-driven and budgeted RAG optimization, but do not
establish a production standard. GEPA is supporting evidence for reflective
candidate proposal and selection.

## Strongest direct observation

RAISE standardizes search spaces and budgets, implements 13 search algorithms,
and evaluates seven text and multimodal datasets with three random seeds. Its
important result for architecture practice is negative: optimizer performance
is task-dependent, so aggregate rankings do not establish a universal winner.

AutoRAGTuner supports declarative component registration and Bayesian
optimization across pipeline configurations. Its reported reduction in code
churn is author-reported framework evidence, not a quality guarantee.

## Production implication

Treat architecture search as controlled experimentation over a typed manifest.
Freeze evaluator meaning during a promotion epoch, compare candidates under the
same dataset and budgets, repeat ambiguous comparisons, reject hard-gate
regressions, and keep an immutable champion plus rollback path.
