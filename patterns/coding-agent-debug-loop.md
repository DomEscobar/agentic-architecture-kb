---
id: pattern-coding-agent-debug-loop
type: pattern
title: Coding-Agent Debug Loop
status: reviewed
privacy: internal
confidence: 0.82
created_at: 2026-09-24T08:05:00+02:00
updated_at: 2026-09-24T08:05:00+02:00
review_at: 2026-12-24
source_ids:
  - source-agentic-repair-loops-evidence-2026
relations:
  - predicate: applies_to
    target: pattern-project-coding-agent-harness
  - predicate: applies_to
    target: pattern-evidence-first-agent-evaluation
  - predicate: applies_to
    target: pattern-eval-guided-improvement-loop
---

# Coding-Agent Debug Loop

## Trigger

Apply when a failing test, build, runtime error or production incident must be
fixed by an agent and the result claimed as done.

Do not apply to exploratory refactoring without a failure signal.

## Invariants

1. No fix without a reproduction that failed before the change.
2. No completion claim without raw command output.
3. Never delete, skip, relax or xfail a test to pass.
4. One hypothesis at a time; disconfirm before patching.
5. After two failed attempts on the same cause: clear context, restate the task
   with what was learned, restart from reproduction.
6. The verifier runs in fresh context; the author never grades the own fix.
7. Fail closed: missing or failed check means not done.

## Phase contract

Every phase declares input, action, artifact and gate. Stop at the first
unsatisfied gate; do not advance on narrative.

### P0 Reproduce

- Action: run the smallest command that exhibits the failure; capture exit code,
  stderr and the environment (revision, dependency lock, data fixture).
- Artifact: `repro/` failing test plus raw output log.
- Gate: the repro fails on the unmodified revision and its message names the
  reported symptom.
- Reject: "it likely fails because …" without output.

### P1 Localize

- Action: state three candidate causes; for each give the falsifier and the
  cheapest command that would show it.
- Artifact: table of cause, evidence for, falsifier, command, observed result.
- Gate: every candidate carries an executed command and result; at least one is
  eliminated or narrowed.
- Reject: editing before elimination.

### P2 Disconfirm

- Action: run the cheapest discriminating check between the surviving
  candidates.
- Gate: the surviving cause names the exact code path and the mechanism that
  produces the symptom.
- Reject: attributing the cause to model intuition.

### P3 Minimal repair

- Action: smallest diff that makes P0 pass.
- Constraints: no new dependencies, no unrelated refactors, no widened
  try/catch, no error suppression, no behaviour change outside the failing path.
- Artifact: diff plus rationale of at most five lines.
- Gate: the P0 repro passes.

### P4 Regression

- Action: run the existing suite plus type, lint and build checks.
- Artifact: raw logs for the repro and the full suite.
- Gate: repro green, previously green suite green, and a test-file diff shows no
  removed, skipped or loosened assertion.
- Reject: passing by weakening shared correctness.

### P5 Adversarial verification

- Action: hand the diff, the repro and the claimed cause to a fresh-context
  verifier that must attempt refutation.
- Gate: the verifier answers PASS with evidence for all four checks:
  1. does the repro fail without the patch;
  2. does the repro exercise the reported symptom rather than a proxy;
  3. does the patch fix the cause rather than suppress the symptom;
  4. were previously passing tests weakened.
- Reject: self-review counted as verification.

### P6 Evidence handoff

- Artifact: diff or commit, commands with outputs, cause, fix summary, residual
  risk, explicitly unverified parts, next owner.
- Gate: every statement binds to a command output or a file.

## Gate escalation

Choose the hardest gate the environment supports:

1. in the same prompt;
2. completion condition with a separate evaluator after each turn;
3. deterministic stop check that blocks the turn from ending;
4. verifier in fresh context.

Unattended runs require 2 or 3; a passing prompt-level check is not evidence.

## Prompt blocks

Reproduction brief:

```text
Symptom: <one observable sentence>
Repro: <exact command> -> expected <X>, actual <Y>
Evidence: <log or stacktrace>
Boundary: change only the failing path.
Step 1: a failing test that reproduces it.
Show that output before touching production code.
```

Localization with refutation duty:

```text
List three candidate causes ranked by evidence.
For each: the observation that would falsify it and the cheapest check.
Run the checks. Report which survived, with command and output.
Change nothing yet.
```

Patch contract:

```text
Smallest change that makes the repro test pass.
Forbidden: new dependencies, unrelated refactors, suppressing errors,
widening try/catch, weakening or skipping tests.
Afterwards: repro green AND existing suite green - show both outputs.
```

Verifier:

```text
You are the verifier. Inputs: diff, repro, claimed cause.
Refute: (1) does the repro fail without the patch? (2) does it exercise the
reported symptom? (3) is the symptom suppressed instead of fixed? (4) was a
green test weakened?
Answer PASS or FAIL with evidence. Do not trust the author's summary.
```

## Anti-pattern detectors

- Declaring done from summary text -> require command output in the handoff.
- Acceptance criteria drifting to an easier target -> diff the criteria against
  the original request before accepting.
- Green counts used as quality proof -> require the check to bind to the claimed
  property; add a known-bad negative fixture that must fail the same gate.
- Symptom suppressed by catching, clamping or retrying -> inspect the diff for
  catch/except, tolerance and timeout changes.
- Proxy test instead of the reported symptom -> assert the repro reproduces the
  original failure mode.
- Repeated identical retries -> after the second failure, clear context and
  restate with new information.
- Child task ends at a raw artifact -> require integration, capture and review
  in the same handoff.

## Evidence

- Agentless: a fixed localize, repair and validate pipeline reached the best
  reported SWE-bench Lite result among open systems at low cost, outperforming
  more autonomous tool-using agents.
- SWE-agent: agent-computer interface design is a first-class performance lever,
  not transport.
- Reflexion: verbal self-reflection improves coding outcomes only when an
  executable feedback signal exists.
- SWE-bench: real multi-file issues; the authors of Agentless documented
  misleading issue text and exact ground-truth patches, so benchmark success is
  not acceptance.
- Agent-as-a-Judge: step-level judgement is more reliable than final-outcome-only
  judging.
- Claude Code guidance: an executable check closes the loop; context exhaustion
  is the binding constraint; adversarial review needs fresh context.

## Limits

Benchmark percentages are workload-bound and do not transfer to another
repository. Vendor documentation is vendor-authored. The invariants above are a
synthesis, not a reproduced measurement; local false-pass and false-fail rates
remain unmeasured.
