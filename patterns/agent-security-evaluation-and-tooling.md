---
id: pattern-agent-security-evaluation-and-tooling
type: pattern
title: Agent Security Evaluation and Tooling
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-13T16:55:00+02:00
updated_at: 2026-08-13T16:55:00+02:00
review_at: 2026-10-13
source_ids: [source-agentic-security-verification-2026-08]
relations:
  - predicate: derived_from
    target: source-agentic-security-verification-2026-08
  - predicate: applies_to
    target: pattern-agentic-runtime-security-boundary
---

# Agent Security Evaluation and Tooling

## Evaluation contract

Run paired benign and adversarial cases against the complete deployed path.
Score authoritative external state: which resource was read, which tool and
arguments executed, which secret crossed a boundary, what memory was promoted
and what side effect committed. Model text and judge labels are diagnostic when
deterministic state exists.

The minimum suite combines:

- normal utility and recovery cases;
- direct, indirect, encoded, multimodal, multi-turn and cross-agent injection;
- data exfiltration, tool misuse, privilege, MCP, memory and RAG poisoning;
- adaptive attacks designed after inspecting the defense;
- over-defense cases containing benign security vocabulary and legitimate
  third-party instructions;
- fault injection into policy, identity, sandbox, verifier and telemetry;
- protected application-specific cases that were unavailable during tuning.

Report attack success, unauthorized-effect rate, sensitive-disclosure rate,
benign task success, refusal rate, latency, cost and detection false positives
by risk slice. A single aggregate score is insufficient.

## Tool selection

Use AgentDojo or InjecAgent as reproducible development environments for tool-
use injection. Use PyRIT, garak or promptfoo for orchestration and broader probe
coverage only after reviewing their execution model. Use skill scanners as
admission signals for extensions. No tool replaces workload-specific state
oracles, adaptive human review or protected cases.

Pin tool and dataset revisions. Run evaluators in a disposable environment with
scoped model keys, read-only target credentials, bounded egress and no access to
production secrets. Treat configuration files, templates, plugins, graders,
remote datasets and generated reports as untrusted code or active content.

## Promotion gate

Promotion fails on any deterministic authorization, tenant-isolation, sandbox
or irreversible-effect violation. Probabilistic detection thresholds require
confidence intervals, false-positive limits and repeated runs. A benchmark that
was used to design the defense cannot serve as the only release holdout.
