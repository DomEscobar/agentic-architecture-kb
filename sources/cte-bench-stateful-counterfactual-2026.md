---
id: source-cte-bench-stateful-counterfactual-2026
type: source
title: CTE-Bench Stateful Counterfactual Trace Evidence 2026
status: reviewed
privacy: public
confidence: 0.79
created_at: 2026-10-01T11:27:00+02:00
updated_at: 2026-10-01T11:27:00+02:00
review_at: 2026-11-30
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-evidence-first-agent-evaluation
---

# CTE-Bench Stateful Counterfactual Trace Evidence — 2026

Primary: [CTE-Bench, arXiv:2609.36647v1](https://arxiv.org/html/2609.36647v1) and [Core-v1 dataset/oracle](https://huggingface.co/datasets/zhangxr7/cte-bench-core-v1), inspected 2026-10-01. Author-reported preprint; dataset/oracle were identified, not independently rerun here.

## Protocol and result

A model sees a deterministic Python service, its observed calls, one source-token edit or state overwrite and 40 *fixed* future calls. It predicts each response; the executable edited and unedited services produce exact-value oracles. Core-v1 has 255 scenarios across six services (rate limiting over-represented), 10,200 predictions per model, and 2,476 intervention-affected calls. Effect-step value match excludes unaffected calls: replaying the unedited service scores 75.7% overall but 0% on affected steps. The 40 predictions within a scenario are correlated and must not be counted as independent trials.

Four hosted configurations obtain 54.3–61.5% exact match on affected steps when correct earlier responses are revealed, 23.2–28.9% without feedback and 24.8–33.2% when conditioned on their own earlier predictions; at most 1.2% of whole scenarios are predicted exactly in free rollout (paper §4). This isolates state-propagation and feedback dependence, **not** autonomous action choice or deployment safety.

## Limits and KB use

The six compact synthetic services, one prompt format, narrow state edits and selection for some intervention effect limit transfer. In 88/255 scenarios the first changed response occurs after the scored 40 calls; a matched no-effect slice is missing. Use a small replay with versioned state snapshots, intervention/no-intervention twin runs, delayed-effect versus unaffected-step metrics, and separate revealed/no-feedback/free-rollout protocols. Keep direct execution and safety invariants as the gate; good predictions cannot certify safe patches. This refines the stateful-oracle guidance in `pattern-evidence-first-agent-evaluation` and GroundEval coverage.
