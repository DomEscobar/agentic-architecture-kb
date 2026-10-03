---
id: source-pair-counterfactual-compression-2026
type: source
title: PAIR Counterfactual Compression Replay Evidence 2026
status: reviewed
privacy: public
confidence: 0.73
created_at: 2026-10-03T12:46:00+02:00
updated_at: 2026-10-03T12:46:00+02:00
review_at: 2026-12-02
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-generation-aware-context-efficiency
---

# PAIR Counterfactual Compression Replay Evidence — 2026

Primary: [Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations, arXiv:2609.36526v1](https://arxiv.org/html/2609.36526v1), inspected 2026-10-03. The attached ZIP is a research cache, not authenticated evidence. Author-controlled preprint; no independent replay or production deployment inspected.

## Intervention and inference

PAIR studies context compression as an intervention at an exact trajectory boundary. From the same saved agent/environment state, continue with and without the compressed context, then compare downstream task outcome, reliability and token consumption. The paper reports 197 selected compression boundaries from 82 trajectories, with nine continuations per condition at each boundary. This paired design targets the effect of a *particular compression*, rather than attributing divergence between different full agent runs to compression alone. The reported strongest cross-run reliability among compressed methods does not show that compression is always preferable to **no compression**: on the retail task it was not simultaneously more reliable and cheaper in tokens than the uncompressed arm.

## Limits and decision

The method requires reproducible snapshots of model-visible context, external tool state and side effects. Its repeated continuations are correlated within boundaries; report intervals over boundaries/tasks rather than treating all continuations as independent examples. Pair with the same frozen agent, model, tools, task state and budget; compare no compression, current summary and the candidate compressor. Record lost facts, authorization scope, exact outcomes, p95 latency and tokens/cost. If a changed context cannot be replayed or a protected safety slice regresses, do not promote the compressor. This is an evaluation design for the project harness, not a mandate to adopt PAIR prompts.
