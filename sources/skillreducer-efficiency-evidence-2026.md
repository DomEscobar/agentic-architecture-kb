---
id: source-skillreducer-efficiency-evidence-2026
type: source
title: SkillReducer Routing and Body Efficiency Evidence 2026
status: reviewed
privacy: public
confidence: 0.65
created_at: 2026-10-03T12:46:00+02:00
updated_at: 2026-10-03T12:46:00+02:00
review_at: 2026-12-02
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-project-coding-agent-harness
---

# SkillReducer Routing and Body Efficiency Evidence — 2026

Primary: [SkillReducer: Optimizing LLM Agent Skills for Token Efficiency, arXiv:2603.29919v2](https://arxiv.org/html/2603.29919v2), inspected 2026-10-03. Author-run preprint; user ZIP text used only to locate the primary source, no local experimental replay.

## Two surfaces, not one metric

SkillReducer separates short routing descriptions, which decide when a skill loads, from its procedure body and on-demand references, which affect execution after loading. The paper studies 55,315 public skills and evaluates its two-stage compression on 600 skills, reporting 48% shorter descriptions and 39% shorter bodies with an aggregate functional score improvement of 2.8% under its protocol. The authors also report that 86% of the 600 skills reach at least their original task score. These are author metrics in their test setting, not evidence that a particular project's compacted skill retains rare safety steps.

## Validity limit and decision

The functionality test is part of the optimization feedback and also the reported evaluation criterion. This optimization-to-criterion overlap is a material overfitting risk; the paper does not establish performance on a truly independent project holdout. In a project harness, ablate description-only versus body-only changes against the original skill and a no-skill arm, then measure trigger recall/precision, procedure completion, forbidden actions, missing prerequisites, token/cost and long-tail tasks on separately held-out cases. Keep executable/authority constraints outside compressible prose. Do not use token reduction or score retention from the optimization set as an automatic acceptance gate.
