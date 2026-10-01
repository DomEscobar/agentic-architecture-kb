---
id: source-context-language-models-2026
type: source
title: Context Language Models Editable Live Context Evidence 2026
status: reviewed
privacy: public
confidence: 0.72
created_at: 2026-10-01T11:27:00+02:00
updated_at: 2026-10-01T11:27:00+02:00
review_at: 2026-11-30
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-generation-aware-context-efficiency
---

# Context Language Models Editable Live Context Evidence — 2026

Primary: [Context Language Models, arXiv:2609.37725v1](https://arxiv.org/html/2609.37725v1), [code](https://github.com/facebookresearch/context-language-models), including [harness](https://github.com/facebookresearch/context-language-models/blob/main/clm/clm_harness/README.md) and [Suffix Cache Reuse](https://github.com/facebookresearch/context-language-models/tree/main/suffix_cache_reuse), inspected 2026-09-30. Author-reported results, not a locally reproduced deployment benchmark.

## Mechanism and reported result

The model edits a file that mirrors its *live* context; edits change what the next model call sees. This is distinct from a retriever, append-only transcript or offloaded memory. On 830 BrowseComp-Plus questions with Qwen3.6-27B, the authors report 59.4% accuracy, an 11.4% **relative** improvement over a Codex-style summarization control, and 21.5% fewer *modeled prefix-reuse FLOPs* (paper §5). Suffix Cache Reuse (SCR) separately reduces modeled server compute by about 35% versus the authors' standard SGLang comparison at matched task performance.

## Limits and KB use

Prefix-reuse FLOPs do not establish wall-clock latency, GPU memory footprint or money saved. The released ContextBench fixture is not available in the inspected repository; the inspected BrowseComp-Plus configuration and paper report differ in some turn/token budgets. SCR is an approximate reuse method evaluated on a narrow serving/model setting. Freely editable context also gives untrusted text and self-generated instructions a persistent attack surface; the paper explicitly flags this issue without demonstrating a complete defense.

Treat editable live context as a challenger to fixed summary and bounded edit tools, not a default. Pin effective budgets and compare end-state quality, evidence loss, prompt-injection persistence, context provenance, cost, TTFT/p95 latency and memory usage separately; verify replay/rollback after edits and keep authority outside model-editable content. This adds a distinct control surface to `pattern-generation-aware-context-efficiency`.
