---
id: pattern-evaluation-tool-selection
type: pattern
title: Evaluation Tool Selection
status: reviewed
privacy: internal
confidence: 0.85
created_at: 2026-08-09T13:30:00+02:00
updated_at: 2026-08-09T13:30:00+02:00
review_at: 2026-10-09
source_ids:
  - source-domescobar-eval-oigl
  - source-evaluation-consulting-research-2026
relations:
  - predicate: derived_from
    target: source-domescobar-eval-oigl
  - predicate: derived_from
    target: source-evaluation-consulting-research-2026
---

# Evaluation Tool Selection

Score candidates on deterministic oracles, trace model, split controls,
identity/reproducibility, CI, comparisons, online sampling, privacy/deployment,
extensibility, artifacts, cost and team fit.

## Winning conditions

- **OIGL:** Go-native standalone agent harness with causal traces, pack identity,
  confirmation and explicit acceptance; still needs external calibration and
  protected split lifecycle.
- **Inspect AI:** Python model/agent tasks needing datasets, solvers, scorers,
  sandboxed execution and inspectable logs.
- **promptfoo:** declarative prompt/model comparison, CI and red teaming;
  generated attacks and scorer meaning still need validation.
- **DeepEval:** Python/pytest teams wanting broad RAG/agent/LLM metrics; built-in
  judge metrics still require local calibration.
- **OpenAI Evals:** custom/private evals in an OpenAI-oriented workflow; verify
  portability and the current API surface.
- **Custom harness:** domain-state oracles, regulated data or specialized
  runtimes. Reuse tools for execution/reporting, not metric meaning.

Keep cases, oracles, identities and acceptance vendor-neutral. A migration must
reproduce the same decisions before replacing the previous runner.
