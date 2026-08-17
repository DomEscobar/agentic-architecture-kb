---
id: pattern-agent-memory-evaluation-blueprint
type: pattern
title: Agent Memory Evaluation Blueprint
status: reviewed
privacy: internal
confidence: 0.91
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-17T08:05:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-evaluation-security-2026, source-memory-operational-baselines-and-tenancy-2026-08]
relations:
  - predicate: derived_from
    target: source-agent-memory-evaluation-security-2026
  - predicate: derived_from
    target: source-memory-operational-baselines-and-tenancy-2026-08
---

# Agent Memory Evaluation Blueprint

Evaluate `write -> maintain/update -> retrieve -> use/action -> delete` with
stage-level oracles and end-to-end outcomes.

## Minimum suite

- LoCoMo/LongMemEval for conversational recall and temporal updates.
- LongMemEval-V2 or Mem2ActBench for experienced workflows and actions.
- HaluMem-style cases to localize extraction and update errors.
- Private cases for project facts, preferences, conflicts and abstention.
- Adversarial poisoning, extraction, cross-tenant and internal-channel probes.
- Lineage-aware deletion and rebuild tests.
- An immutable raw-event-log BM25 control with temporal narrowing and bounded
  local expansion under the same model, prompt, context and reranking budgets.

## Metrics and gates

Write: extraction precision/recall, fabrication, unauthorized writes,
provenance completeness. Update: conflict recall, stale survival, current-value
accuracy. Retrieval: Recall/Precision@k, MRR/nDCG, distractors and abstention.
Use: task success, constraint grounding, exact tool arguments and side effects.
Operations: p50/p95 latency, storage, tokens and calls, with ingest, extraction,
retrieval, consolidation and answer cost metered separately. Report total cost
per correct answer and warm/cold behavior rather than query-serving cost alone.
Security: injection/activation, secret extraction and cross-tenant exposure.
Deletion: canonical/derived coverage, retrievability and rebuild consistency.

Use dev, selection, hidden holdout and red-team splits with corpus/config hashes.
Repeat stochastic runs and report confidence/flakiness. Zero cross-tenant leak,
zero forbidden side effect and complete required erasure are non-compensatory.
