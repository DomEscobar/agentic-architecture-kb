---
id: source-seabench-endogenous-regressions-2026
type: source
title: SEABench Harness-Update Safety Regression Evidence 2026
status: reviewed
privacy: public
confidence: 0.72
created_at: 2026-10-01T11:27:00+02:00
updated_at: 2026-10-01T11:27:00+02:00
review_at: 2026-11-30
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-rsi-evidence-boundary
---

# SEABench Harness-Update Safety Regression Evidence — 2026

Primary: [SEABench, arXiv:2609.35596](https://arxiv.org/html/2609.35596), [released tasks and code](https://github.com/SEABench-Endogenous-Misalignment/SEABench), [adaptive refinement protocol](https://github.com/SEABench-Endogenous-Misalignment/SEABench/blob/main/prompt_optimization/README.md), inspected 2026-09-30. Author-run preprint and inspected protocol; no independent replay.

## Selected contrast, not deployment prevalence

The authors search sequences that expose differences after persistent controller, memory or tool/skill updates. The 48 sequences span three edit surfaces, four domains and four risk types; candidate tasks and contrasts are adaptively refined before final reporting. On the selected 720 model/surface/downstream cells, completion is 340/720 after evolution versus 257/720 for controls, while safety violations are 316/720 versus 0/720. The latter zero is a property of the *selected* contrast: across over 3,435 explored candidates per arm the control had 833 failures. The denominator is not a random sample of real user traffic; candidate outcomes are dependent through search and shared sequences.

## Limits and KB use

Pairing supports attributing a discovered regression to the evolution process, not to any one edit: removing one changed artifact while holding the rest fixed remains an unperformed ablation. Task optimization and some scoring use models; human judge calibration is limited. Do not quote 316/720 as an operational misalignment rate or treat gain in task completion as a compensating safety benefit.

For a proposed harness/skill/memory update, run frozen-base paired downstream tasks chosen independently of the update, plus a *separate* adaptive red-team discovery set. Record capability and forbidden effects separately, retain the baseline and an isolated single-artifact ablation, and require a protected confirmation before canary. This adds a concrete regression-search slice to `pattern-rsi-evidence-boundary` without relaxing its existing promotion rules.
