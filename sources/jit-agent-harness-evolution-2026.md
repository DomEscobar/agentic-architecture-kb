---
id: source-jit-agent-harness-evolution-2026
type: source
title: JIT-Agent — Instance-Conditioned Harness Synthesis
status: reviewed
privacy: public
confidence: 0.72
created_at: 2026-08-28T18:53:00+02:00
updated_at: 2026-08-28T18:53:00+02:00
review_at: 2026-09-28
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-project-coding-agent-harness
  - predicate: supports
    target: pattern-eval-guided-improvement-loop
  - predicate: evaluated_by
    target: pattern-rsi-evidence-boundary
  - predicate: depends_on
    target: pattern-agent-sandbox-selection
---

# JIT-Agent — Instance-Conditioned Harness Synthesis

Primary material checked on 2026-08-28:

- [JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution,
  arXiv:2608.25593v1](https://arxiv.org/abs/2608.25593v1)
- [Public Apache-2.0 runtime and benchmark adapters, commit
  `ababa06c2f54d799fd9fbc356e5368f61a452260`](https://github.com/bingreeky/JIT/tree/ababa06c2f54d799fd9fbc356e5368f61a452260)
- [JIT-Agent-27B model checkpoint, revision
  `0705ca15b822942e6531b7301a79a16738175094`](https://huggingface.co/JIT-Agent/jit-27b/tree/0705ca15b822942e6531b7301a79a16738175094)

## Evidence class

E2 for the author-reported task-conditioned harness results and E2 for the
released static synthesis mechanism. This is a two-day-old v1 preprint without
peer review or independent replication. The paper reports within-backbone
comparisons, multiple model families, task and cost outcomes, and qualitative
generated-harness examples. It does not report confidence intervals,
hypothesis tests or a design-matched frozen-generator null, and the released
artifacts do not reproduce the full streaming-evolution claim.

## Mechanism

JIT-Agent treats an agent harness as four generated Python modules for memory,
planning, action and capability or tool-policy orchestration, plus a YAML prompt
configuration. A separate 27B meta-model receives the task, tool registry,
shared protocol and descriptions of reference harnesses. It emits a
task-conditioned harness, validates its fixed exports, repairs failures within
a bounded retry loop and wraps an unchanged executor model.

The paper's training design has three stages: teacher-supervised customization,
repair learning from compiler and runtime diagnostics, and Evo-GDPO selection
against an archive frontier over task reward, latency and monetary cost. Static
inference generates several candidates and selects one before execution.
Streaming inference additionally proposes retaining successful task-harness
records for retrieval by later tasks while keeping the generator weights fixed
at deployment.

The novel architectural hypothesis is narrow: when task structures vary enough
that one fixed scaffold is repeatedly mismatched, an instance-conditioned
harness generator may be a useful challenger to fixed-harness selection. It is
not evidence that every task needs generated code or that a generated harness
should receive production authority.

## Tested scope and reported results

The paper evaluates nine benchmarks covering deep research, daily work,
planning and office-style workspace execution. It does not evaluate SWE-bench,
repository-scale software evolution or live production systems.

Across the authors' 18 directly matched backbone-benchmark comparisons,
JIT-generated harnesses improve the corresponding default scaffold. Reported
nine-benchmark averages increase from 74.1 to 81.8 for GLM-5.2 and from 66.7 to
75.5 for DeepSeek-V4-Flash. In a narrower fixed-backbone comparison against
Claude Code, Codex, OpenCode, Hermes and NanoBot on three benchmarks and two
backbones, JIT-Agent leads four of six settings. It trails the best fixed
harness in the remaining two while using fewer tokens. The paper reports the
lowest API cost in all six controlled settings and an average reduction of
36.0 percent relative to the cheapest fixed alternative in each setting.

These are author-run benchmark results. Main-table sample counts, repeated
seeds and uncertainty are not reported sufficiently to treat the point
differences as portable effects. Several tasks use model-based scoring, and the
public benchmark data and harness references also require a contamination and
selection-bias audit before causal interpretation.

## Artifact audit

The pinned runtime contains adapters for seven of the paper's nine benchmarks,
eleven seed harnesses, generated-harness parsing, best-of-N selection, bounded
repair and a shared execution path. Its Python packages compile successfully,
but the repository contains no automated tests. Reproducing the benchmark
tables requires hosted model and judge calls, benchmark-specific credentials
and large datasets; those experiments were not rerun in this audit.

The released model card describes its checkpoint as an initial research
release built on the Stage-I customization model and further distilled from
the final research checkpoint. It therefore cannot be assumed to be the exact
full Evo-GDPO checkpoint behind every paper result.

More importantly, the released Python runtime does not implement the paper's
streaming harness-bank update or Evo-GDPO training loop. Archive, retention and
frontier-update logic appears in the paper and repository overview, not in the
executable Python path. The public artifact supports static generation,
selection, validation and repair; it does not independently substantiate
compounding self-evolution.

## Security audit

Generated harness modules are written into the repository workspace and loaded
through ordinary Python imports in the evaluator process. Import-time code can
therefore execute with the process's filesystem, network and environment
authority before any strategy interface is instantiated. Export-name checks
and runtime repair are compatibility controls, not a security boundary.

The separate `execute_code` tool is also not a hardened sandbox. It invokes a
Python interpreter from a Conda environment in a workspace directory, copies
the parent environment, uses a short command-string blocklist and falls back
to the current interpreter when the configured environment is absent. It does
not provide credential stripping, filesystem or network isolation, syscall
policy, user-namespace isolation or a default-deny capability boundary.

Treat every generated harness as untrusted code. Validate its schema and
imports statically, reject unexpected dependencies and execute it only inside a
disposable container or microVM with no ambient credentials, restricted mounts
and egress, resource limits and externally controlled termination. The trusted
evaluator, policy gateway, protected cases, budgets and promotion controller
must remain outside that boundary.

## Operational interpretation

Do not begin with a 27B harness generator. First compare a minimal fixed harness
and explicit routing among a small reviewed harness set. Add JIT synthesis only
when task-slice evidence shows repeatable structural mismatch that fixed
routing does not solve within the latency and cost budget.

Evaluate the complete model-harness-environment tuple on paired tasks. Include
generator cost, candidate-selection cost, compilation and import failures,
repair attempts, executor tokens, wall time, side effects and safety sentinels.
Keep generated artifacts immutable and content-addressed. Promotion requires a
protected confirmation split, repeated evidence, a bounded canary, kill switch
and rollback to the prior fixed harness or router.

Streaming retention needs a second gate. A successful task trajectory may be
stored as an experimental reference only after provenance, contamination,
privacy and task-family checks. Do not let a same-task reward update become
evidence of cross-task improvement, and do not call archive growth recursive
self-improvement without showing that one generation produces better future
candidates under equal search budget on untouched tasks.

## Limits and falsifiers

Independent reproduction with the released checkpoint, pinned datasets,
matched baselines, repeated seeds and paired uncertainty would raise
confidence. A faithful implementation of streaming retention must separately
measure performance over task order, forgetting, contamination, archive growth,
selection overhead and held-out transfer.

The hypothesis weakens if a small fixed router matches JIT-Agent under total
cost, gains disappear on protected project tasks, generated code violates the
capability contract, or archive updates improve same-distribution scores while
regressing later task families. Until these checks exist, JIT-Agent is a useful
experimental challenger and source of harness design hypotheses, not a
production default or evidence of autonomous RSI.
