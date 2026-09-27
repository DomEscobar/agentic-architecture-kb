---
id: source-jaz-invoke-harness-as-language-2026
type: source
title: JAZ invoke Harness-as-Language Evidence 2026
status: reviewed
privacy: public
confidence: 0.76
created_at: 2026-09-27T07:30:00+02:00
updated_at: 2026-09-27T07:30:00+02:00
review_at: 2026-11-27
source_ids: []
relations: []
---

# JAZ invoke Harness-as-Language Evidence 2026

Primary: Harness as a Language: A Minimalist Agent Framework With Maximal
Expressivity (JAZ), MIT CSAIL with independent researchers,
[arXiv:2609.26891v1](https://arxiv.org/abs/2609.26891v1), submitted 2026-09-22,
25 pages. Framework code at github.com/jaz-lang/jaz and evaluation code at
github.com/jaz-lang/jaz-evals. Author-reported preprint; no independent
replication inspected.

## Reported primitive

- `invoke` is a function whose body the model writes at call time. Two defining
  properties: the model may write arbitrary executable code including recursive
  `invoke`, so subagents are the default; and everything visible to the model,
  including all inputs and the REPL history `__history__`, is a variable in the
  code environment.
- Property two is what distinguishes the design from smolagents and RLM, which
  expose the prompt and history only as messages.
- Tail-recursive delegation is the reported long-horizon mechanism: when the
  context fills, the agent delegates the remainder to a subagent while passing
  the entire history by reference, which is lossless rather than compacting.
- A built-in hook system carries observability, budget control and validation.
  The long-horizon experiment elicits delegation with a `ContextWindowWarning`
  hook that appends a user message containing a code template.

## Reported evaluation protocol

- Prompts split into environment-provided `instructions` (method-agnostic) and
  method-provided `guidance` (task-agnostic); self-improvement instructions
  contain no workflow guidance at all.
- Prompts kept byte-identical between methods except for necessary differences,
  and necessary differences are listed individually.
- Cost measurement controls cache effects: a distinct prompt cache key per run,
  at most three parallel runs, and cache-hit-rate drift calibrated on a toy
  environment at n=1,3,4,5 (drop above 5 percent from n=4 to n=5, within 2
  percent for n<=4), fixing n=3 with a stated systematic cost error below 2
  percent.
- Recursion depth capped at 2 for CodeAct+subagents and JAZ to remove the
  subagent confound.

## Reported results

StuLife long-horizon, 1,284 tasks with 939 scored and a 207-task far-recall
subset, GPT-5.4 nano (high) across all methods, mean and standard error over
three runs:

- CodeAct per task: 52.5 pass / 24.8 far-recall, 4.4 USD.
- CodeAct+subagents (smolagents): 30.2 / 20.6, 9.4 USD.
- CodeAct+subagents (RLM): 60.0 / 32.0, 13.1 USD.
- Letta Agent, not prompt-only: 70.9 / 61.8, 42.1 USD.
- JAZ invoke, prompt-only: 72.6 / 69.9, 18.3 USD.

AppWorld continual self-improvement, full test-challenge split, 417 tasks,
shuffled with seed 42, full test feedback per task, solver GPT-5.4 nano, meta
agent GPT-5.4, n=3 for non-self-improving and n=6 for self-improving methods:

- Official CodeAct, not prompt-only and carrying AppWorld-specific guidance:
  TGC 48.2, 16.6 USD.
- CodeAct per task: 67.5, 10.2 USD.
- CodeAct+subagents: 71.1, 21.6 USD.
- ACE on CodeAct, not prompt-only: 69.9, 30.6 USD.
- JAZ invoke: 74.2, 20.9 USD.

The headline comparison is the far-recall subset, where JAZ leads the
specialized memory harness by 8.1 points at roughly 57 percent lower cost.

## Limits

- No ablation isolates the primitive from the injected scaffolding: delegation
  was elicited by a hook that appends a message containing a code template.
- No comparison gives CodeAct+subagents equal access to its own history
  variable, so part of the measured gap reflects the baseline's missing
  capability rather than the primitive.
- Letta and ACE are not prompt-only while JAZ is, so the claim that specialized
  harnesses are unnecessary is not tested on equal footing.
- On the full StuLife set the margin over Letta shrinks to 1.7 points; the large
  gain sits in the 207-task recall subset.
- Both benchmarks are code, API and REPL centric; no memory-heavy or non-code
  domain is covered.
- Main results use one solver model; model-family dependence is untested.
- Self-improvement means editing prompts and skills inside the REPL, with no
  cross-family transfer and no weight updates.
- Standard errors are reported, but the samples remain small.

## Use in this KB

Supplies three transferable ideas: the interaction history as a first-class
variable, lossless delegation by reference instead of compaction, and the
instructions-versus-guidance split as evaluation methodology. The causal claim
is unverified without the missing ablation.
