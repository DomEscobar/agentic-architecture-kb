---
id: source-harness-design-empirical-study-2026
type: source
title: Coding Harness Component Study Evidence 2026
status: reviewed
privacy: public
confidence: 0.78
created_at: 2026-09-26T07:35:00+02:00
updated_at: 2026-09-26T07:35:00+02:00
review_at: 2026-11-26
source_ids: []
relations: []
---

# Coding Harness Component Study Evidence 2026

Primary: An Empirical Study of Harness Design for Coding Agents,
[arXiv:2609.20804v1](https://arxiv.org/abs/2609.20804v1), submitted 2026-09-17,
43 pages, retrieved and inspected 2026-09-26. UMass Amherst, Emory University,
UNC Charlotte, with work completed partly during Zoom internships.
Author-reported preprint; no independent replication inspected.

## Reported design

- A lightweight harness keeps the ReAct execution loop and supporting mechanisms
  fixed (permission handling, post-edit diagnostics, stuck detection) while
  varying three components: planning, action space and context management.
- Models: Nemotron-3 at 30B, 120B and 550B as a within-family capability axis,
  plus Mistral-Medium-3.5-128B as a cross-family point.
- Benchmarks: SWE-Bench Verified and Terminal-Bench 2.1.
- 176 matched settings: five context strategies across four context budgets
  (32k, 64k, 96k, 128k), plus planning and action-space ablations at 128k.
- Context strategies: T0 no cross-turn compaction (terminate on overflow),
  T1 elide stale tool observations, T2 elision plus external store and a recall
  tool, T3 LLM summarization without elision, T4 staged elision before
  summarization under a soft and a hard token threshold, with the preamble and a
  recent window kept verbatim.
- Web search was excluded because SWE-Bench tasks derive from public GitHub
  issues and search could expose the corresponding pull request and gold patch.

## Reported findings

1. Context management matters most when the context budget is tight, and most of
   its benefit comes from preventing context-overflow failures; the accuracy
   benefit diminishes as the window grows.
2. Staged elision before summarization gives the strongest efficiency of the
   evaluated strategies. Making elided content recoverable was rarely invoked
   and produced no accuracy gain over elision alone.
3. Planning acts as an accuracy scaffold for weaker models and as a cost saver
   for stronger models, with little change in accuracy either way.
4. Predefined tools improve results for models with weak bash proficiency, while
   bash-capable models operate effectively with a bash-only interface at
   substantially lower cost, especially on command-line-centric tasks.

Trajectory-level analysis attributes the effects to mechanism rather than score:
context management extends trajectories without substantially altering
behaviour, planning changes where trajectories stop, and the action space
changes the granularity at which code is written.

## Limits

- Four models, three from one family, and two code-centric benchmarks: the
  findings are conditional diagnostics, and the authors present the models as
  probes rather than optimization targets.
- The context-strategy taxonomy and its thresholds are the authors' own
  implementation; another harness implementing a nominally identical strategy
  may behave differently.
- 176 settings are reported without confidence intervals in the inspected text,
  and Terminal-Bench 2.1 is a small benchmark.
- The recall result is weak evidence against recoverability: a rarely triggered
  mechanism may indicate an affordance or prompt problem rather than a true
  negative.
- The action-space comparison measures the complete interface, including
  read-before-write checks, file-state tracking and automatic diagnostics, so
  tool schemas are not separable from validation support by design.
- The planning conclusion is stated qualitatively; effect sizes would be needed
  to separate it from sampling noise.

## Use in this KB

Supplies the component-level protocol behind the harness improvement loop and
four conditional defaults for budget, compaction order, planning and action
space.
