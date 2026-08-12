---
id: source-bounded-self-improvement-2025-2026
type: source
title: Bounded Self-Improvement Evidence 2025–2026
status: reviewed
privacy: public
confidence: 0.8
created_at: 2026-08-12T18:41:00+02:00
updated_at: 2026-08-12T18:41:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Bounded Self-Improvement Evidence 2025–2026

Primary sources checked on 2026-08-12:

- [Darwin Gödel Machine, 2025](https://arxiv.org/abs/2505.22954)
- [Red Queen Gödel Machine, 2026](https://arxiv.org/abs/2606.26294)
- [GEPA repository and paper](https://github.com/gepa-ai/gepa)

## Evidence class

All three are E2 for durable recommendations here. DGM has unusually detailed
experiments, ablations and artifacts but remains narrow coding-agent evidence.
RQGM is a recent preprint. GEPA supports reflective evolution of prompts and
code-like text, but does not by itself prove recursive improvement of the
optimizer.

## What DGM demonstrates

DGM branches an archive of coding agents, lets selected agents modify their own
codebase, and evaluates descendants. After 80 iterations, the paper reports
SWE-bench improvement from 20.0% to 50.0% and full-Polyglot improvement from
14.2% to 30.7%, with ablations for self-improvement and open-ended exploration.
Experiments used sandboxing and human oversight.

## What remains unproven

The result does not demonstrate domain-general recursive self-improvement,
indefinite capability growth, safe evaluator self-modification or reliable
transfer to production RAG. The archive-selection mechanism remained fixed.
RQGM proposes changing utilities only at epoch boundaries while keeping each
within-epoch objective fixed; this is a useful control concept, not yet strong
production evidence.

## Safety interpretation

Production systems should begin with a fixed evaluator, bounded mutable surface,
paired replay, hidden gates, budgets, sandboxing, human promotion, canaries and
rollback. Evaluator evolution is a separate governed transaction with an old-
and-new objective compatibility audit.
