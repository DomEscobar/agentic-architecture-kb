---
id: source-research-radar-2026-09-30
type: source
title: Biweekly Agentic Architecture Research Radar 2026-09-30
status: inbox
privacy: internal
confidence: 0.84
created_at: 2026-09-30T18:38:00+02:00
updated_at: 2026-09-30T18:38:00+02:00
review_at: 2026-10-14
auditability: public
source_ids: []
relations:
  - predicate: applies_to
    target: synthesis-agentic-runtime-techniques
  - predicate: applies_to
    target: synthesis-rag-current-evidence-2026-08
  - predicate: applies_to
    target: synthesis-agentic-memory-architecture
  - predicate: applies_to
    target: synthesis-agent-evaluation-techniques
  - predicate: applies_to
    target: pattern-agentic-runtime-security-boundary
  - predicate: applies_to
    target: pattern-rsi-evidence-boundary
---

# Biweekly Agentic Architecture Research Radar — 2026-09-30

This is an automated research candidate, not reviewed knowledge. All 18 queries
in the six configured packs were attempted for the interval beginning
2026-09-13. Date-filtered web search returned an unsupported-filter error and
the required minimal-query retry returned HTTP 401 for every query. Discovery
therefore switched to reachable primary GitHub release pages and arXiv category
pages. Primary provenance was traced directly; release notes and their linked
commits are one evidence chain, not independent corroboration.

## 1. Google ADK 2.10.0 closes the resume-authorship gap

**Classification:** confirmed
**Evidence:** E2 maintainer release and linked implementation commit; no
independent replay was performed.

Google ADK 2.10.0, released 2026-09-24, requires agent authorship before a
function call can be dispatched during resume. This is the released fix for the
caller-authored resumable-event execution path recorded in the 2026-09-13
radar. The same release adds confirmation-history filtering across agents,
keeps OAuth2 client secrets out of session state, limits artifact resolution
depth, validates reserved path segments, and confines agent-builder globs.

**Affected claims/cards:**

- `claim-runtime-security-external-enforcement`
- `claim-runtime-side-effect-boundary`
- `claim-runtime-adoption-release-specific`
- `runtime.google-adk-runtime`
- `runtime.durable-checkpoint-ledger`
- `runtime.security.strict-tool-contract`

Sources:

- https://github.com/google/adk-python/releases/tag/v2.10.0
- https://github.com/google/adk-python/commit/2c61b84

## 2. ADK makes skill lifetime and disclosure explicit, but remains experimental

**Classification:** new-candidate
**Evidence:** E2 maintainer release and implementation commits; no comparative
security or resource-control evaluation.

ADK 2.10.0 adds opt-in one-turn ephemeral skills, unload operations, active-
skill caps, catalog-disclosure modes, change detection, and removal of unloaded
skill instructions from later model requests. These mechanisms can bound tool
and instruction persistence, but the feature is experimental and disabled by
default. The release does not establish that lifecycle controls prevent skill
confusion, supply-chain compromise, or stale capability use.

**Affected claims/cards:**

- `claim-runtime-adoption-release-specific`
- `runtime.google-adk-runtime`
- `runtime.security.mcp-plugin-admission`
- `runtime.security.extension-supply-chain-scan`

**Candidate action:** evaluate whether unload removes instructions, tools and
cached state across retries, resumes and concurrent branches; pair this with a
negative direct-call test after capability removal.

Source:

- https://github.com/google/adk-python/releases/tag/v2.10.0

## 3. ADK's resume and state fixes reinforce replay-specific regression gates

**Classification:** confirmed
**Evidence:** E2 maintainer release with linked regressions; no independent
reproduction.

ADK 2.10.0 includes fixes for rewound-invocation filtering, replay sequence
ordering, resumed transfers, interrupt resume without node rerun, parallel
state-list writes, temporary rewind state, and peer task-mode isolation. This
confirms that recovery correctness is a collection of state-machine invariants,
not a single checkpoint feature, and that released-version replay suites remain
necessary.

**Affected claims/cards:**

- `claim-runtime-side-effect-boundary`
- `claim-runtime-adoption-release-specific`
- `runtime.google-adk-runtime`
- `runtime.durable-checkpoint-ledger`
- `evaluation.deterministic-state-oracle`

Source:

- https://github.com/google/adk-python/releases/tag/v2.10.0

## 4. Microsoft Agent Framework 1.19.0 hardens invocation and resume boundaries

**Classification:** confirmed
**Evidence:** E2 maintainer release and linked pull requests; no independent
cross-version replay.

The 2026-09-18 Python 1.19.0 release scopes provider-backed MCP sessions per
invocation, authenticates MCP requests and sessions to invocation identity,
origin and ownership, verifies skill archive digests, and preserves approval,
checkpoint and replay context across mixed batches, nested workflows and
streaming merges. File checkpoint operations are also described as concurrency-
safe and lossless. These are release-specific confirmations of the KB's
external-enforcement and replay-integrity requirements, not independent proof
that all paths are covered.

**Affected claims/cards:**

- `claim-runtime-security-external-enforcement`
- `claim-runtime-side-effect-boundary`
- `claim-runtime-adoption-release-specific`
- `runtime.microsoft-agent-framework`
- `runtime.approval-interrupt`
- `runtime.durable-checkpoint-ledger`
- `runtime.security.mcp-plugin-admission`

Source:

- https://github.com/microsoft/agent-framework/releases/tag/python-1.19.0

## 5. Runtime update rollback now explicitly includes database snapshots

**Classification:** new-candidate
**Evidence:** E2 OpenClaw maintainer release note; no independent fault-
injection evidence was found.

OpenClaw 2026.9.7 reports pre-migration backups of state and agent databases,
consistent snapshots while the gateway continues writing, rollback restoration,
and fail-closed behavior when snapshot cleanup fails. This is a concrete
runtime-upgrade recovery mechanism relevant to stateful agent platforms. The
release note does not provide recovery-point measurements, crash matrices, or
independent restore verification.

**Affected claims/cards:**

- `claim-runtime-adoption-release-specific`
- `claim-runtime-side-effect-boundary`
- `runtime.openclaw-platform`
- `runtime.durable-checkpoint-ledger`

**Candidate action:** add upgrade fault injection at snapshot, migration and
handoff boundaries and verify pre-upgrade state plus post-rollback writability.

Source:

- https://github.com/openclaw/openclaw/releases/tag/v2026.9.7

## 6. Other lanes did not produce an admissible material change

**Classification:** no-material-change
**Evidence:** bounded negative result, not proof of absence.

- **RAG/retrieval:** reachable sources were registered parser/runtime GitHub
  release pages and the arXiv `cs.IR` recent listing. No inspected source
  combined a material claim change with matched baselines, stage-separated
  metrics, artifacts and transfer limits.
- **Agentic memory:** reachable sources were the ADK and Microsoft Agent
  Framework release pages plus arXiv `cs.AI`. The release mechanisms above are
  runtime state controls; no independently supported memory default, forgetting
  guarantee, or lifecycle benchmark was found.
- **Evaluations/observability:** ADK added duration, token and model-call metrics
  and now fails when zero cases are evaluated. These are useful instrumentation
  controls but do not change the KB's deterministic-before-judge or calibration
  claims. Promptfoo and framework release pages were reachable, but no
  qualifying comparative result was established.
- **Security:** GitHub releases and the GitHub advisory HTML surface were
  reachable, and ADK/Microsoft/OpenClaw hardening is recorded above. The
  advisory page did not provide a reliable bounded export for the interval, so
  comprehensive advisory absence is not claimed.
- **Bounded self-improvement:** reachable sources were arXiv `cs.AI` recent
  listings and framework releases. No source inspected supplied paired shared-
  baseline evaluation, protected holdout, canary, kill switch and rollback
  evidence sufficient to alter `claim-improvement-loop-bounded`.

## Coverage gaps

General discovery was unavailable after the mandated retry, so all lanes have
reduced recall. GitHub's direct HTML surfaces were reachable, but the local
repository pulse could not verify any of the 23 registered projects because
Git transport failed and Python HTTPS validation reported an expired
certificate. arXiv category listings were reachable, but listing extraction did
not expose enough title/abstract context for comprehensive query matching.
These gaps prevent any claim of comprehensive absence. No reviewed claim,
technique, pattern or synthesis was modified.
