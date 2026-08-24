---
id: pattern-evaluation-statistical-decision-rules
type: pattern
title: Statistical Decision Rules for Agent Evaluations
status: reviewed
privacy: internal
confidence: 0.89
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-21T21:04:57+02:00
review_at: 2026-09-21
source_ids:
  - source-evaluation-consulting-research-2026
  - source-phantom-gains-measured-null-2026
relations:
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
  - predicate: derived_from
    target: source-phantom-gains-measured-null-2026
---

# Statistical Decision Rules for Agent Evaluations

## Default comparison

- Pair candidate and baseline on the same cases, environment and evaluator.
- Predeclare primary metric, important effect, gates, slices, repetitions and
  stopping rule.
- For binary paired outcomes report wins/losses/ties and paired inference such
  as exact McNemar; bootstrap case-level deltas for complex metrics.
- Preserve hierarchy: repeated attempts within one case are not independent
  additional tasks.
- Report intervals, effect sizes and denominators; p-values are not effect size.

## Sample sizing and search

Size from baseline, smallest important delta, power/error tolerance and slice
needs; no universal minimum exists. Separate a primary decision from exploratory
metrics. Correct/control multiplicity when many variants or slices are searched.
Repeated holdout use turns it into selection data.

## Transition-level capability claims

Per-item claims that a model learned, forgot, corrupted or expanded a capability
compare noisy estimates and can report transitions when the model is unchanged.
For every such statistic, run a frozen model through the identical benchmark,
sampling, checkpoint, batching, decoding and grading design. Use the resulting
distribution as the design-matched null rather than assuming zero.

Report its interval and effect-size envelope, retain frozen replicates for a
negative-control check, and control multiplicity across tested problems and
arms. A null measured for one model, benchmark or checkpoint design does not
transfer automatically to another.

## Promotion rule

Promote only if hard gates pass, primary outcome meets its declared margin, no
critical slice exceeds regression tolerance, operational constraints hold, an
independent protected confirmation passes, and all identities match.

Sequential monitoring needs a declared confidence-sequence or alpha-spending
design. Repeatedly checking ordinary intervals until favorable inflates error.
