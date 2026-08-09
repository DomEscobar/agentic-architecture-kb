---
id: pattern-llm-judge-calibration
type: pattern
title: LLM Judge Calibration and Governance
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-10-09
source_ids:
  - source-agent-evaluation-research-2026
  - source-evaluation-consulting-research-2026
relations:
  - predicate: derived_from
    target: source-agent-evaluation-research-2026
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
---

# LLM Judge Calibration and Governance

## Admission test

Use labeled controls covering clear pass/fail, boundaries, adversarial prose,
missing evidence, contradictions and each critical slice. Measure confusion,
sensitivity/specificity, repeat agreement, calibration, position/order,
verbosity/style/self-preference, slice performance and escalation quality.
Aggregate correlation alone cannot expose rare catastrophic false passes.

## Runtime contract

Freeze model, provider, prompt, rubric, examples, decoding, input projection and
parser. Keep judge identity separate from the evaluated runtime. Blind model
identity and randomize pair order; test reversals rather than assuming they fix
bias.

## Policy and kill conditions

- deterministic gates override judge plausibility;
- use atomic criteria instead of one holistic score;
- rationales are diagnostics, not proof;
- uncertain/high-risk cases abstain or go to human adjudication;
- re-calibrate after any identity/semantic change and on production controls;
- disable promotion use when false-pass tolerance, slice coverage,
  reproducibility or parsing fails.
