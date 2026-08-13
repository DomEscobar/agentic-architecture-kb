---
id: source-agent-evaluation-research-2026
type: source
title: Agent Evaluation Research August 2026
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

# Agent Evaluation Research — August 2026

Current primary sources, reviewed on 2026-08-09:

- Agentic Benchmark Checklist:
  https://arxiv.org/abs/2507.02825
- AgentRewardBench:
  https://arxiv.org/abs/2504.08942
- AJ-Bench / Agent-as-a-Judge:
  https://arxiv.org/abs/2604.18240
- TRACE / cross-step trajectory monitoring:
  https://arxiv.org/abs/2606.07054
- GroundEval / deterministische stateful evaluation:
  https://arxiv.org/abs/2606.22737
- GEPA / reflective prompt evolution:
  https://arxiv.org/abs/2507.19457
- SWE-bench Live:
  https://arxiv.org/abs/2505.23419
- SWE-bench Illusion:
  https://arxiv.org/abs/2506.12286

## Evidence audit

### Benchmark validity — E4 direction, E3 measurements

The Agentic Benchmark Checklist identifies concrete errors in task setup and
reward design that can materially distort rankings. The generalizable conclusion
is not a particular percentage: evaluators and tasks themselves require tests,
adversarial negatives, and validity checks.

### Trajectory judges — E3, workload-bound

AgentRewardBench compares automated evaluators against expert-labeled web-agent
trajectories. AJ-Bench extends the judge with active environment interaction.
Both support calibration against human or deterministic references; neither
demonstrates a universal judge.

### Long-horizon evidence — E2–E3, new

TRACE accumulates evidence across distant steps instead of judging only local
windows or final output. This is relevant to sabotage and long causal chains,
but the evidence comes from ten SHADE-Arena domains and is not yet a general
production standard.

### Deterministic stateful evaluation — E2, strong pattern

GroundEval checks search, fetch, access, and temporal paths against state truth.
The pattern fits agentic systems with controlled environments. The publication
is very recent, and its case studies do not replace independent replication.

### Evaluation-guided optimization — E3 within tested tasks

GEPA uses trajectories and textual reflection to evolve prompt variants through
Pareto selection. Its reported sample efficiency applies to the tested tasks.
Safe self-improvement still requires holdouts, immutable gates, patch
boundaries, canaries, and rollback.

### Contamination resistance — converging E3 evidence

SWE-bench Illusion finds indications of memorization and artifact exploitation.
SWE-bench Live uses newer executable repository tasks. Public static benchmarks
are therefore development baselines, not sufficient final evidence of
generalizable coding-agent capability.
