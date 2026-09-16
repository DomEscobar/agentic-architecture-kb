---
id: source-benchshield-reward-integrity-2026
type: source
title: BenchShield Reward Integrity Evidence 2026
status: reviewed
privacy: public
confidence: 0.82
created_at: 2026-09-14T08:39:00+02:00
updated_at: 2026-09-16T21:20:44+02:00
review_at: 2026-10-14
source_ids: []
relations: []
---

# BenchShield Reward Integrity Evidence 2026

Primary paper: [BenchShield v1](https://arxiv.org/abs/2609.11028v1), retrieved
and inspected 2026-09-14. This is an author-reported preprint, not an
independently reproduced production result.

## Supported distinctions

1. A vulnerable task exposes a possible reward-manipulation path; exposure does
   not establish that an agent attempted or successfully used it.
2. Reward integrity spans observations, actions/state, handoff, evaluator
   inputs, outcome/reward and feedback release. A correct final artifact alone
   does not prove legitimate derivation.
3. Infrastructure-side lifecycle evidence and sealed bundles support run-level
   attribution and structural replay without rerunning unsafe side effects.
4. Structural conformance and semantic adequacy are separate obligations. The
   paper's finite structural model does not prove that the reward captures the
   intended task meaning.

## Reported results and limits

The paper reports 456 adjudicated trajectories selected from more than 31,000
public runs across three benchmarks; 314 were labelled reward hacking under the
study protocol. This selected complete-artifact corpus is not a prevalence
estimate for deployed agents.

The runtime study planned 180 cells and reports 144 runnable cells. Reported
96% accuracy is conditional on cells receiving a verdict; abstentions affect
coverage. No directed exploit received `Checked` in that study, which is not a
universal prevention guarantee. Structural checks are reported without model
calls; full semantic auditing is reported at USD 5–10 per cell under the study
setup. These costs and accuracies require local measurement.

Transfer limits include BenchFlow-specific transformation, fixed lifecycle
assumptions, nondeterministic semantic adaptation, incomplete backend coverage
and out-of-scope multi-role noninterference. The paper does not establish
general RL/RSI improvement, semantic correctness from isolation or production
reliability.
