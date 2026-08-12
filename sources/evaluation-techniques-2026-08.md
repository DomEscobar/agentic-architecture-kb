---
id: source-evaluation-techniques-2026-08
type: source
title: Agent Evaluation Technique Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.89
created_at: 2026-08-12T22:05:00+02:00
updated_at: 2026-08-12T22:05:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Agent Evaluation Technique Evidence Audit — August 2026

Primary sources checked on 2026-08-12:

- [Agentic Benchmark Checklist, 2025](https://arxiv.org/abs/2507.02825)
- [AgentRewardBench, 2025](https://arxiv.org/abs/2504.08942)
- [RAGChecker, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/27229a2bd5bd22095b17e4d6f1334241-Abstract-Datasets_and_Benchmarks_Track.html)
- [GroundEval, 2026](https://arxiv.org/abs/2606.22737)
- [Procedure-Aware Evaluation, 2026](https://arxiv.org/abs/2603.03116)
- [SWE-bench Live, 2025](https://arxiv.org/abs/2505.23419)
- [SWE-bench Illusion, 2025](https://arxiv.org/abs/2506.12286)
- [Sell Me This Stock: Unsafe Recommendation Drift in LLM Agents, 2026](https://arxiv.org/abs/2603.12564), narrow evidence for paired clean/manipulated tool-data replay in a financial workload.

## Evidence hierarchy

External state, executable tests, authorization logs and causal tool IDs are
stronger oracles than a plausible final answer. GroundEval and Procedure-Aware
Evaluation are recent E2 evidence for state- and process-aware scoring; their
specific results are not yet universal. AgentRewardBench supports calibrating
trajectory judges against expert labels, not trusting an unvalidated judge.

Public static benchmarks are useful development controls. SWE-bench Live and
SWE-bench Illusion reinforce the need for fresh executable tasks, duplicate
checks and private holdouts when making generalization claims. The Agentic
Benchmark Checklist shows that task and reward defects can distort rankings;
the evaluator itself therefore needs tests and adversarial negatives.

## Durable recommendation

Combine deterministic invariants with calibrated semantic judging only for
residual ambiguity. Report outcome, safety, causal grounding, process,
efficiency and robustness separately. Promotion requires paired comparison on
the same task/environment identities, repeated attempts, uncertainty, hard
regression gates and protected selection/holdout splits.
