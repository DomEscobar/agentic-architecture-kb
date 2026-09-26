---
id: source-coding-agent-skill-distillation-2026
type: source
title: Coding-Agent Skill Distillation Evidence 2026
status: reviewed
privacy: public
confidence: 0.74
created_at: 2026-09-26T07:10:00+02:00
updated_at: 2026-09-26T07:10:00+02:00
review_at: 2026-11-26
source_ids: []
relations: []
---

# Coding-Agent Skill Distillation Evidence 2026

Primary: Coding Agents are Strong Prompt Optimizers (CASD),
[arXiv:2609.26261v1](https://arxiv.org/abs/2609.26261v1), submitted 2026-08-13,
retrieved and inspected 2026-09-26. Author-reported preprint; no independent
replication inspected and no code link in the inspected abstract.

## Reported claim and method

- Claim: validation-gated iterative prompt search is unnecessary when a static
  corpus of agent rollouts is available.
- CASD gives an unmodified off-the-shelf coding agent the frozen rollout corpus
  and a single high-level instruction, then uses the skill markdown file it
  writes directly as the optimized system prompt. No environment interaction,
  no held-out validation gate, one offline pass.
- Mechanism is reflection scope: the agent writes and executes analysis code for
  corpus-wide statistics, then inspects only the episodes those statistics flag.

## Reported process evidence

- 24 logged distillation runs, 816 tool calls classified: 94 corpus-layout
  explorations, 184 statistics executions, 510 episode inspections, 28 skill
  writes. Runs used 16 to 51 tool calls (mean 34) and produced 5 to 8 KB skills.
- Every run measured pass rates and episode lengths; 96 percent quantified
  termination and failure modes; 92 percent analyzed tool usage; 79 percent
  broke performance down by task category; about one third searched for
  duplicated tool invocations.
- Generated skills carry 54 quantitative evidence citations (4.6 per 1k words)
  against none across four GEPA prompts and one across four SkillOpt prompts.

## Reported results

- Benchmarks: ALFWorld, tau2-bench retail, tau2-bench telecom and
  SpreadsheetBench-Verified.
- Under matched data access, CASD beats GEPA on three of four benchmarks and the
  validation-gated reflective baseline on four of four.
- Average improvement over the unoptimized baseline is 16.6 points against 10.9
  for GEPA and 5.3 for the gated baseline.
- Optimization cost is about 1.60 USD, reported as more than 22 times cheaper
  than validation-gated search.
- When baselines receive additional validation data and unrestricted
  environment access, CASD still leads on two of four benchmarks.

## Limits

- The headline claim exceeds the evidence: once baselines receive more data and
  environment access, the advantage holds on only two of four benchmarks.
- Corpus construction cost is excluded. The rollout corpus had to be generated
  by running the target agent, so the quoted figure covers only the analysis
  pass.
- No validation gate means no defence against corpus-specific overfitting. The
  inspected text asserts corpus representativeness rather than verifying it.
- Outcome variance is not reported: one optimized prompt per benchmark, while
  the 24 analyzed runs characterize process behaviour rather than result spread.
- Generated rules embed corpus-specific counts, for example a tool invoked 284
  times with 123 exact duplicates, with no length budget and no stated
  generalisation requirement.
- The gated baseline appears to be the authors' own; the better-established
  comparison is GEPA, where the win is three of four.
- Dependency on coding-agent analysis quality is untested across agent
  strengths.

## Use in this KB

Supports trace analysis performed as executable code and evidence-bound
generated artifacts. Treat single-pass distillation as a bounded alternative to
gated search that still requires independent corpus-representativeness evidence
before it can replace a held-out gate.
