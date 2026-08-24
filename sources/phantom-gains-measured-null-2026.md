---
id: source-phantom-gains-measured-null-2026
type: source
title: Phantom Gains — Measured Nulls for Self-Improvement Claims
status: reviewed
privacy: public
confidence: 0.86
created_at: 2026-08-21T21:04:57+02:00
updated_at: 2026-08-21T21:04:57+02:00
review_at: 2026-09-21
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-evaluation-statistical-decision-rules
---

# Phantom Gains — Measured Nulls for Self-Improvement Claims

Primary material checked on 2026-08-21:

- [Phantom Gains: Auditing Self-Improvement Against a Measured Null,
  arXiv:2608.20290v1](https://arxiv.org/abs/2608.20290)
- [Public analysis code and reduced per-problem records, commit
  `ccb887872e3c684fa2fb532bbd44064a7da07821`](https://github.com/chengxuphd/phantom-gains/tree/ccb887872e3c684fa2fb532bbd44064a7da07821)

## Evidence class

E3 for the bounded measurement claim. The preprint provides matched frozen-model
controls, multiple training seeds, explicit positive controls, sensitivity and
power analyses, and public code plus reduced records for all 48 reported runs.
This is strong primary evidence, not independent replication.

## Tested scope

The study evaluates transition-level learning, corruption and expansion metrics
for Qwen3-8B with rank-32 LoRA on mathematics workloads. It compares three-round
self-training and external-distillation arms against an unchanged model passed
through the same sampling and evaluation pipeline. The main evaluation sets are
MATH-500, AIME 2025–2026 and a deliberately selected 1,163-problem difficulty
band. Each problem is sampled 128 times per evaluated checkpoint.

## Supported finding

An unchanged model can produce non-zero per-problem capability transitions when
two noisy estimates are differenced. A conventional one-success expansion rule
reported 7 transitions among 25 base-unreached AIME problems, an apparent rate
of 0.280, despite unchanged weights. Across 11 independent frozen AIME
evaluations, the 110 ordered comparisons gave the repaired two-success rule a
pooled null of 146/2,530 = 0.058, with a task-cluster bootstrap 95% interval of
[0.038, 0.078].

The paper replaces the threshold rule with a per-problem exact test against
1,408 pooled baseline draws under false-discovery-rate control. That procedure
returned zero detections on each of 11 held-out frozen replicates in the tested
setting. The result supports measuring a separate, design-matched frozen-model
null for every transition statistic rather than assuming that its unchanged
value is zero.

## Artifact audit

The repository's offline suite passed 45/45 tests locally on 2026-08-21. Running
`analysis/nulls.py` reproduced the reported AIME two-success null of 146/2,530 =
0.058 with interval [0.038, 0.078], together with the published matched floors
for the difficulty band and MATH-500.

This verifies the released analysis over reduced per-problem records. It does
not reproduce hosted sampling, training or grading from first principles. The
repository contains 19 MB of reduced counts; approximately 15 GB of raw
generation text is available only on request.

## Operational interpretation

For transition-level improvement claims, the control must match the treatment's
benchmark, sampling count, checkpoint count, batching path, decoding and
grading. Report the null distribution, uncertainty and effect-size envelope;
reserve frozen replicates for negative-control validation and correct for
multiple testing across problems and arms.

Do not transfer the numerical null rates to another model or workload. Measure
them again under the target design. This source does not establish that
self-training generally fails, that external distillation generally wins, or
that the reported policy-gradient collapse transfers beyond the tested
configuration.

## What would change the claim

Independent reproduction across other backbones, domains and inference stacks
would raise confidence and may identify analytic nulls that replace some
empirical controls. Failure of the released analysis on the pinned records, or
a matched frozen control that does not reproduce the reported floors, would
contest this source record.
