---
id: source-harnessdev-agent-harness-evolution-2026
type: source
title: HarnessDev Agent Harness Creation and Evolution Evidence 2026
status: reviewed
privacy: public
confidence: 0.76
created_at: 2026-09-04T13:52:00+02:00
updated_at: 2026-09-04T13:52:00+02:00
review_at: 2026-10-04
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-project-coding-agent-harness
  - predicate: supports
    target: pattern-rsi-evidence-boundary
  - predicate: evaluated_by
    target: pattern-evidence-first-agent-evaluation
---

# HarnessDev Agent Harness Creation and Evolution Evidence — 2026

Primary material checked on 2026-09-04:

- [HarnessDev, arXiv:2609.01437v1](https://arxiv.org/abs/2609.01437v1)
- [HarnessDev experimental HTML](https://arxiv.org/html/2609.01437v1)
- [Self-Developing Agents project page](https://self-developing-agents.github.io/)

## Evidence class

E2 for the author-reported creation and evolution results. This is a fresh v1
preprint without peer review or independent reproduction. The protocol exposes
task counts, frozen artifacts, model roles, feedback/held-out separation,
executor-token cost and important negative results. Evolution nevertheless has
one trajectory per creator-runtime cell, no population-level uncertainty, and
held-out evaluation only for one code benchmark.

## Benchmark mechanism

HarnessDev separates the creator model, development environment, persistent
harness, executor model and evaluator. The creator builds a runnable harness
from a weak compatibility seed, after which the harness is frozen and executed
on downstream tasks. The seed contains input/output plumbing and passive tools
but no agent loop, task decomposition, tool policy, context management,
persistent task state, verifier, retry, recovery or stopping policy.

Creation covers six creator models, four domains and five benchmarks with
2,207 unique downstream instances. Each creator-benchmark cell normally
contains three independent harness creations and reports avg@3. Self-Eval uses
the creator as executor; Unified-Eval runs generated harnesses with a fixed
executor to expose harness-executor compatibility.

Evolution begins from a frozen creation harness. Nine creator-runtime lineages
produce 73 official versions and 64 adjacent version switches using visible
SWE-Pro-100 and Terminal-Bench-89 feedback. Every frozen version is later run
on 630 SWE-Pro instances not shown to the creator. The evaluated unit is thus a
versioned executable artifact, not a prompt description or self-reported
success claim.

## Reported findings

Generated harnesses remain behind the selected mature human-engineered
references on code and search/research, while some writing and machine-learning
experimentation settings match or exceed their selected references. The human
reference rows are external system results rather than paired controls under a
common executor, so those distances are descriptive rather than causal.

Visible feedback and post-freeze held-out scores move in the same direction for
34 of 64 adjacent version switches. Only two of nine creator-declared final
versions are best on their lineage's held-out set. Under four fixed-Gemini
evolution runs, only the Opus-created harness improves over its own starting
harness on the 630-task held-out set; the Qwen, DeepSeek and GPT-created
harnesses regress. This supports an executor-conditioned promotion gate and is
negative evidence against treating visible feedback gain as retained harness
improvement.

The Qwen result concerns Qwen 3.7 Max as creator, not Qwen3-32B as a retrieval
controller. It does not update the Qwen3-32B controller hypothesis elsewhere in
this knowledge base.

## Limits and accounting gaps

- Evolution has one trajectory per creator-runtime cell and one unfinished
  main-runtime cell.
- The 630 held-out instances are disjoint from feedback but come from the same
  SWE-Pro public split; cross-benchmark transfer is not shown for Evolution.
- Execution-token cost excludes the creator tokens used to build or revise the
  harness, so it is not complete lifecycle cost.
- Higher execution-token use does not reliably predict better results.
- Some generated state or memory mechanisms exist in source code but do not
  appear in recorded formal execution; runnable code is not proof of an
  effective mechanism.
- Creation containers are provisioned for reproducibility, not containment;
  generated harnesses remain untrusted executable code.
- The paper explicitly studies model-external learning and does not show that
  harness evolution replaces parameter learning or yields domain-general RSI.

## Operational interpretation

Freeze every candidate harness by content digest. Evaluate it first with a
fixed executor on protected tasks, then across the executor models or releases
it must support. Keep visible feedback, selection and final confirmation splits
separate. Record creator and repair cost as well as downstream execution cost.
Require repeated trajectories, deterministic security checks, a canary, kill
switch and rollback before retaining an evolved harness.

Do not let the evolving harness change protected tasks, scorers, promotion
rules, budgets or rollback state. Execute generated code inside a hardened
untrusted-code boundary rather than relying on the benchmark's reproducibility
container.
