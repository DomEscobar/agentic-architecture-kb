---
id: concept-evaluation-metric-catalog
type: concept
title: Evaluation Metric Catalog and Selection Rules
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-11-09
source_ids:
  - source-evaluation-consulting-research-2026
relations:
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
---

# Evaluation Metric Catalog and Selection Rules

## Metric contract

Every metric declares: decision, unit, oracle, scale/direction, aggregation,
uncertainty, required sample, slices, threshold owner, cost, version and blind
spots. A number without this contract is telemetry, not a gate.

## Metric families

- **Task outcome:** exact state, acceptance tests, completion, human acceptance,
  abstention correctness.
- **Retrieval:** Recall@k, Precision@k, MRR, nDCG, evidence coverage, ACL leakage,
  stale retrieval and latency.
- **Grounded generation:** claim support precision, evidence completeness,
  citation correctness, contradiction and unsupported-claim rate.
- **Tool agents:** capability/argument correctness, side effects, forbidden and
  duplicate calls, recovery and terminal reason.
- **Coding agents:** tests, resolution, regression, forbidden files, diff scope,
  static analysis and reproducibility.
- **Memory:** write precision, recall, update, temporal validity, contradiction,
  privacy isolation and verified forgetting.
- **Conversation:** goal resolution, instruction retention, correction,
  escalation, consistency and turn efficiency.
- **Multimodal/voice:** correctness plus OCR/layout, transcription, temporal
  alignment, interruption and perceptual slices.
- **Operations:** p50/p95/p99 latency, cost per success, availability, retries,
  queue age and incidents.

## Selection rules

1. Choose one primary outcome tied to user value.
2. Add hard gates for safety, privacy, permissions and irreversible effects.
3. Add component metrics only for likely failure boundaries.
4. Keep latency and cost separate from correctness.
5. Report aggregate and decision-critical slices.
6. Pair every proxy with periodic outcome validation.
7. Report rates with denominators and confidence intervals.
8. Do not infer recall from source presence without a relevance set.
9. Do not infer correctness from citations or fluent prose alone.
10. Version semantics; threshold/rubric changes create a new lineage.
