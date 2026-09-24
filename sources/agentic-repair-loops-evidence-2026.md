---
id: source-agentic-repair-loops-evidence-2026
type: source
title: Agentic Repair-Loop Evidence 2024-2026
status: reviewed
privacy: public
confidence: 0.78
created_at: 2026-09-24T08:05:00+02:00
updated_at: 2026-09-24T08:05:00+02:00
review_at: 2026-11-24
source_ids: []
relations: []
---

# Agentic Repair-Loop Evidence 2024-2026

Retrieved and inspected 2026-09-24. Search index was unavailable; every source
was fetched directly from the primary page.

## Sources

- [SWE-bench](https://arxiv.org/abs/2310.06770) (ICLR 2024): 2,294 real GitHub
  issue and pull-request tasks across 12 Python repositories. Requires
  cross-file coordination, long context and execution feedback. Best model in
  the paper resolved 1.96 percent.
- [SWE-agent](https://arxiv.org/abs/2405.15793): attributes performance to the
  agent-computer interface, reporting 12.5 percent pass@1 on SWE-bench.
- [Reflexion](https://arxiv.org/abs/2303.11366): verbal reinforcement via
  self-reflection in an episodic buffer; 91 percent pass@1 on HumanEval with
  feedback signals.
- [Agentless](https://arxiv.org/abs/2407.01489): fixed three-phase
  localize, repair, validate pipeline; reported highest open-source SWE-bench
  Lite performance at low cost, plus documented benchmark problems leading to
  SWE-bench Lite-S.
- [Agent-as-a-Judge](https://arxiv.org/abs/2410.10934): agentic step-level
  evaluation of agentic systems; reported as more reliable than plain
  LLM-as-a-judge judging on its DevAI tasks.
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
  and [/goal](https://code.claude.com/docs/en/goal): verification-first loop,
  plan-before-code, context as the binding constraint, adversarial review in
  fresh context, gating levels from prompt to deterministic stop check.
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents):
  distinguishes predefined workflows from model-directed agents and recommends
  the simplest sufficient structure.

## Supported claims

1. A fixed phase structure can outperform more autonomous agent loops on repair
   benchmarks.
2. Tool and interface design materially changes repair performance.
3. Self-critique requires an executable feedback signal to help.
4. Step-level verification adds signal beyond final-outcome judging.
5. Benchmark issue quality varies, so external success is not local acceptance.

## Limits

All percentages are benchmark-bound and were not independently reproduced here.
The Claude Code and Building Effective Agents material is vendor-authored
practitioner guidance. No local measurement of false-pass or false-fail rates
exists yet.
