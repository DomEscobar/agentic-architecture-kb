---
id: source-evaluation-consulting-research-2026
type: source
title: Evaluation Consulting Research August 2026
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

# Evaluation Consulting Research — August 2026

Primary sources and official implementation artifacts, reviewed on 2026-08-09:

- Agentic Benchmark Checklist: https://arxiv.org/abs/2507.02825
- AgentRewardBench: https://arxiv.org/abs/2504.08942
- GroUSE evaluator unit tests: https://arxiv.org/abs/2409.06595
- RAGCHECKER: https://arxiv.org/abs/2408.08067
- RAGBench/TRACe: https://arxiv.org/abs/2407.11005
- MIRAGE component/adaptability evaluation: https://arxiv.org/abs/2504.17137
- Automated structural agent testing: https://arxiv.org/abs/2601.18827
- Holistic agent failure diagnosis: https://arxiv.org/abs/2605.14865
- SWE-bench Live: https://arxiv.org/abs/2505.23419
- MemoryAgentBench: https://arxiv.org/abs/2507.05257
- OpenAI Evals: https://github.com/openai/evals
- UK AISI Inspect AI: https://github.com/UKGovernmentBEIS/inspect_ai
- promptfoo: https://github.com/promptfoo/promptfoo
- DeepEval: https://github.com/confident-ai/deepeval

## Convergent findings

- Benchmark validity is an evaluated property, not a consequence of dataset
  size or popularity.
- End-to-end outcomes decide usefulness; component and span metrics diagnose.
- Grounded systems require separate retrieval/evidence and generation checks.
- Evaluator unit tests need known failure modes; correlation with another model
  judge is insufficient.
- Agent traces help localize errors, but exact golden trajectories can reject
  valid alternative behavior.
- Public static coding benchmarks need fresh/private counterparts because of
  contamination and tuning exposure.
- Framework feature lists show capability, not metric validity. Tool selection
  follows workload, data boundary, integration and evidence lifecycle.

## Evidence boundaries

The 2026 papers are recent and often domain-specific. They justify eval slices
and canaries, not universal numeric thresholds. Vendor and repository docs are
E2 for observed functionality and E0 for unsupported superiority claims.
