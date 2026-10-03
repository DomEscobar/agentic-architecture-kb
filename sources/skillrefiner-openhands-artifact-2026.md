---
id: source-skillrefiner-openhands-artifact-2026
type: source
title: SkillRefiner OpenHands Artifact and Evidence Boundary 2026
status: reviewed
privacy: public
confidence: 0.63
created_at: 2026-10-03T12:00:00+02:00
updated_at: 2026-10-03T12:00:00+02:00
review_at: 2026-11-03
auditability: public
source_ids: []
relations:
  - predicate: applies_to
    target: pattern-project-coding-agent-harness
  - predicate: applies_to
    target: pattern-eval-guided-improvement-loop
---

# SkillRefiner OpenHands Artifact and Evidence Boundary — 2026

Primary artifact inspected 2026-10-03: [OpenHands/SkillRefiner at commit `d9dfdb8e7e73e2449a7af1e04bd78ecb366db1db`](https://github.com/OpenHands/SkillRefiner/tree/d9dfdb8e7e73e2449a7af1e04bd78ecb366db1db), including [dataset inventory](https://github.com/OpenHands/SkillRefiner/blob/d9dfdb8/datasets/README.md), [baseline protocol](https://github.com/OpenHands/SkillRefiner/blob/d9dfdb8/baselines/README.md), and [ablations](https://github.com/OpenHands/SkillRefiner/blob/d9dfdb8/scripts/ablations/README.md). The [alphaXiv item](https://www.alphaxiv.org/abs/2610.skillrefiner-offline-skill-refinement) is a discovery/summary surface only. Its slug is not a valid arXiv identifier; no matching primary arXiv publication or DOI was verified at inspection. This entry describes **inspectable code and its limitations**, not a verified paper result.

## Implemented candidate mechanism

The released pipeline refines a reusable agent skill *offline* from already collected historical task traces. It separates successful and failed trajectories, clusters the failure evidence, proposes skill changes and checks candidates against offline feedback. This differs from a single corpus-wide distillation pass, which does not explicitly organize failure clusters, and from a validation-gated online search that obtains new task rollouts for each candidate. The repository contains pipeline code, prompts, baseline definitions and ablation scripts; these establish an implementation surface, not its general effectiveness.

## Evaluation and reproduction gaps

The repository documents SpreadsheetBench, DAPO-Math and PR-review task splits and comparisons with a shared initial skill, Trace2Skill, and a multi-revision GEPA configuration. The reported SpreadsheetBench percentages and refinement-token figures appear in the alphaXiv summary, but the relevant historical rollout corpus and reported spreadsheet data are not released for independent reconstruction. The private PR data and matching judge are also unavailable. The repository notes a discrepancy between its stored and paper-used initial skill and differing counts in a PR gold copy. No independent benchmark replay was run for this audit. A paired bootstrap over test tasks would not replace repeated refinement trajectories, and refinement-only token counts exclude the cost of collecting historical traces.

## Fit in this KB

`source-coding-agent-skill-distillation-2026` already motivates testing an offline pass on a frozen rollout corpus; SkillRefiner supplies a *candidate mechanism for failure-aware refinement*, not new evidence that it wins. In a project-specific coding harness, consider it only when the project has reusable, consented traces with versioned task outcomes and enough repeated failures to form meaningful clusters. Compare against the current skill, no skill, a single corpus-wide distillation pass, and a budget-matched validation-gated search on untouched project tasks. Keep the candidate skill inside a bounded editable surface with authority checks; account for corpus construction and selection cost, cross-project transfer, safety regressions and rollback. Do not quote alphaXiv effect sizes as accepted KB claims.
