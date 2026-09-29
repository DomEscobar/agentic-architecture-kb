---
id: source-rrsi-regularized-harness-evolution-2026
type: source
title: RRSI Regularized Harness Evolution Evidence 2026
status: reviewed
privacy: public
confidence: 0.73
created_at: 2026-09-29T07:45:00+02:00
updated_at: 2026-09-29T07:45:00+02:00
review_at: 2026-11-29
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-rsi-evidence-boundary
  - predicate: applies_to
    target: pattern-eval-guided-improvement-loop
---

# RRSI Regularized Harness Evolution Evidence — 2026

Primary material inspected 2026-09-29: [paper v2, arXiv:2609.24972](https://arxiv.org/html/2609.24972v2) and [released code](https://github.com/google-research/rrsi), especially `rrsi/domain.py`, `rrsi/selection.py`, `rrsi/evaluate.py`, `rrsi/history.py` and `rrsi/critic.py`. Author-reported preprint and code inspection, not an independent reproduction. Evidence class E2 for benchmark outcomes; implementation observations are code-backed but have not been exercised locally.

## Mechanism and tested scope

RRSI evolves an executable harness around a frozen policy, not model weights. In each round, candidates receive a bounded number of tagged edits, the proposer sees prior accepted and rejected hypotheses, stalled search reserves a proposal for an untried component, and a pre-evaluation critic screens task-specific logic. A noise-adjusted historical score floor, token-cost rule and domain guards govern selection. A git worktree isolates each candidate; the domain adapter supplies task ids, runtime, scoring, traces and guards. The critic combines deterministic patterns with an LLM review: it is a screen, not proof that leakage is absent.

The authors evolve on Terminal-Bench 2.1 (89 tasks, two trials each), Harvey LAB (120 evolve tasks; 40 in-distribution held out) and EngDesign (61 evolve tasks). The unchanged selected harness is then evaluated on SWE-bench Verified, JobBench, GDPval, APEX-Agents and Frontier-Eng. Coding evolution is also repeated with a second frozen policy; one evolved coding harness is tested on a smaller policy. These are selected benchmark transfers, not production deployment or proof of better future optimizers.

## Reported results and ablation

Against the unevolved harness, Terminal-Bench 2.1 changes 74.2 to 80.2 and unseen SWE-bench Verified 82.0 to 83.8 with Claude Opus 4.8. Harvey LAB evolve changes 89.4 to 90.5; its held-out split 86.9 to 89.2. The three workspace out-of-distribution scores change 36.0 to 40.7 (JobBench), 48.8 to 52.3 (GDPval) and 34.2 to 37.9 (APEX-Agents). EngDesign changes 50.0 to 54.9 and Frontier-Eng Medal points 17.7 to 22.0. These values are the authors' Table/Figure 3 measurements, not locally replicated effects.

The more distinctive evidence is the workspace ablation (paper §4.3, Table 2): removing acceptance constraints changes evolve 90.5 to 91.5 but lowers the three-benchmark OOD average 43.6 to 41.0; removing both proposal and acceptance regularizers changes evolve to 92.8 while OOD falls to 40.3, with 3.80 million policy tokens per trial versus RRSI's 2.42 million. This supports *testing* search-path regularization rather than selecting the highest repeatedly observed evolve score. It does not isolate every individual rule or establish a universal effect size.

## Limits and operational boundary

- One preprint and author-run comparisons; no independent replication or uncertainty interval sufficient here to promote a general default. Some workspace tasks use an LLM judge; engineering graders are deterministic but policy trajectories remain stochastic. A finite adaptively reused evolve set still risks overfit.
- Search and outcome budgets must count proposer, analyst, critic, repair, benchmark runs and policy execution separately. The headline policy-token comparison is not total lifecycle cost; the unevolved workspace harness is still cheaper than RRSI's evolved one (paper §4.3).
- Released `relative_cost_change` returns zero when either token count is unavailable. A cost gate using this value must fail closed or mark the result inconclusive in a production-oriented evaluator. The selection rule can admit within-noise-band changes for lower cost or structural novelty and can retain a small measured score decrease; it is not a safety/promotion gate.
- The per-edit history attributes a bundled candidate's one score change to each constituent edit. Treat this as a search trace, not causal attribution, unless single-edit ablations establish the mechanism.
- Keep candidate write authority away from tasks, hidden answers, evaluator, acceptance rules and receipts. Confirm finalists with repeated paired runs on protected tasks, explicit cost and noncompensatory safety gates; retain canary, kill switch and rollback. No evidence here supports relaxing those controls or a claim that generation N produces a better N+1 proposer under matched information and budget.
