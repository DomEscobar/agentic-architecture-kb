---
id: source-domescobar-agentic-eval-research
type: source
title: DomEscobar Agentic Eval Evolution Research
status: reviewed
privacy: public
confidence: 0.82
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

# Agentic Eval Evolution Runtime — Research Audit

- Repository: https://github.com/DomEscobar/agentic-eval-evolution-runtime
- Reviewed commit: `f890e15790f4a1a60adcd835f3c7993c38efaf09`
- Research permalink: https://github.com/DomEscobar/agentic-eval-evolution-runtime/tree/f890e15790f4a1a60adcd835f3c7993c38efaf09/research
- Retrieved: 2026-08-09

## Included research lanes

- Generic agent evaluation and evolution harness
- Evaluation-guided code patch loops
- Evaluation-dataset quality and leakage protection

Each lane contains a plan, source ledger, claims, evidence excerpts, pages, and
a report. This is more auditable than a prose-only research report.

## Defensible core findings

- Evaluation execution, mutation, and promotion are distinct roles.
- Deterministic oracles and hard gates take precedence over weighted soft scores.
- Training/development, candidate selection, and hidden holdout data require
  separate information boundaries.
- A patch loop needs immutable evaluator surfaces, diff/file boundaries, a
  budget, archive, canary, and rollback.
- A dataset architecture is not yet a valid dataset; case validity, oracles,
  representativeness, and leakage must be measured.
- Benchmark success demonstrates performance only on the bound dataset, commit,
  and configuration.

## Claims requiring lower confidence

- New 2026 preprints on autonomous evolution are mostly E2–E3 and not broadly
  replicated.
- Isolated improvement figures from small SWE-bench subsets do not generalize to
  other repositories or task distributions.
- GitHub stars measure attention, not evaluation validity or production
  readiness.
- A separate model does not automatically make an LLM judge independent;
  rubric, data, model family, and correlated errors require calibration.
- A composite dataset-quality score must not hide missing oracles or leakage
  behind an average.

## Assessment

The research structure is a useful hypothesis and source base. It is used as a
secondary synthesis source; strong architecture claims are also checked against
the relevant papers, official repositories, or standards.
