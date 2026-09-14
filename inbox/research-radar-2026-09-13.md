---
id: source-research-radar-2026-09-13
type: source
title: Biweekly Agentic Architecture Research Radar 2026-09-13
status: inbox
privacy: internal
confidence: 0.86
created_at: 2026-09-13T07:00:00+02:00
updated_at: 2026-09-13T07:00:00+02:00
review_at: 2026-09-27
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

# Biweekly Agentic Architecture Research Radar — 2026-09-13

This is an automated research candidate, not reviewed knowledge. All 18 queries
in the six configured packs were executed for the interval beginning 2026-08-30.
The configured web-search provider failed authentication, so discovery used
OpenAlex, the arXiv API where rate limits permitted, GitHub releases, issues,
pull requests, commits and the GitHub Advisory Database. Primary provenance was
traced directly. An issue, proposed fix, release note and advisory from one
project are one evidence chain, not independent corroboration.

## 1. Google ADK 2.9.0 makes failed-node resume explicitly at-least-once

**Classification:** confirmed  
**Evidence:** E2 maintainer release note and linked implementation commits; no
independent effect-level replay was performed.

Google ADK Python 2.9.0 now reruns a failed workflow node on resume instead of
replaying it as complete. The release note explicitly warns that a node which
performs an external side effect and then fails will repeat that effect on every
resume, and requires node bodies to be idempotent. The same release also confines
GCS-tool local file access to a configured root, restricts transfers to declared
targets, and records tool-trajectory and telemetry changes. This directly
confirms that checkpoint/resume does not supply exactly-once external effects.

**Affected claims/cards:**

- `claim-runtime-side-effect-boundary`
- `claim-runtime-adoption-release-specific`
- `runtime.google-adk-runtime`
- `runtime.durable-checkpoint-ledger`
- `runtime.safety.transactional-effect-ledger`

Source:

- https://github.com/google/adk-python/releases/tag/v2.9.0

## 2. Google ADK resumable mode can dispatch a caller-authored tool call

**Classification:** security-critical  
**Evidence:** E2 public maintainer-repository issue with an executable,
no-credential reproduction against 2.7.1 and 2.8.0, plus an unmerged regression
fix; Google reportedly declined a tracked security advisory because the feature
is experimental. No independent reproduction was found.

In opt-in resumable mode, ADK accepts caller-seeded session events and selects a
trailing function call for replay without checking that the current agent
authored it. The published reproduction seeds a `user` event containing a
function call, resumes that invocation with no new message, and observes a file
side effect even when no model credential exists. This bypasses the model turn,
system prompt and model-mediated safety checks, but remains bounded by host-side
authentication, capabilities and before-tool policy. The proposed author check
and tests are not merged, and 2.9.0 does not list the fix.

**Affected claims/cards:**

- `claim-runtime-security-external-enforcement`
- `claim-runtime-side-effect-boundary`
- `claim-runtime-adoption-release-specific`
- `runtime.google-adk-runtime`
- `runtime.security.strict-tool-contract`
- `runtime.security.capability-policy-gateway`
- `runtime.durable-checkpoint-ledger`

**Candidate action:** add a resume-provenance regression that seeds caller-
authored function-call events and asserts that only agent-authored pending calls
can execute. Treat prompt or model approval as non-authoritative.

Sources:

- https://github.com/google/adk-python/issues/7076
- https://github.com/google/adk-python/pull/7077
- https://github.com/google/adk-python/releases/tag/v2.9.0

## 3. Cross-scope identifier resolution remains an active agent-platform failure

**Classification:** security-critical  
**Evidence:** E2 reviewed upstream advisories and project issue reproductions;
no independent reproduction was found.

Two current reports repeat the same confused-deputy mechanism at different
boundaries:

- Flowise through 3.1.3 lets an authenticated low-privilege caller select a raw
  credential ID from another workspace through
  `POST /api/v1/node-load-method/:name`. The service decrypts and uses the
  victim credential for provider calls without checking workspace ownership.
  The secret is not returned directly. Version 3.1.4 is named as fixed.
- Google ADK 2.8.0's `FileArtifactService` accepts path separators in a
  `user_id`; a crafted identifier can compose onto another user's session
  artifact tree and read, overwrite or delete artifacts. The stock HTTP route
  does not expose this exact path because Starlette does not decode an encoded
  slash inside that segment. The proposed fix is not merged and 2.9.0 does not
  list it.

These findings support binding every opaque resource ID to the active tenant or
workspace at resolution time and validating identifiers at service boundaries.
They do not establish cross-tenant exposure for deployments that never accept
the affected identifiers from callers.

**Affected claims/cards:**

- `claim-runtime-security-external-enforcement`
- `claim-sandbox-boundary-configured`
- `runtime.google-adk-runtime`
- `runtime.security.capability-policy-gateway`
- `runtime.security.strict-tool-contract`
- `retrieval.metadata.permission-filter`

Sources:

- https://github.com/advisories/GHSA-wfvf-r9gr-6qfq
- https://github.com/google/adk-python/issues/7067
- https://github.com/google/adk-python/pull/7068

## 4. MCPHub publishes an OAuth bypass and an unresolved disabled-tool bypass

**Classification:** security-critical  
**Evidence:** E2 reviewed advisory for the OAuth mechanism, and E1/E2
maintainer-repository pull request with regression tests for the tool-policy
mechanism; no independent reproduction was found.

MCPHub before 1.0.32 is reported to disable client authentication by default and
make PKCE optional in its embedded OAuth server. An intercepted authorization
code can therefore be redeemed without a client secret or verifier. Separately,
an open 2026-09-13 fix reports that disabling a tool removes it from discovery
but does not stop a direct `tools/call`, because the execution path checks
server activity rather than tool enablement. The latter has not reached a
release at check time.

**Affected claims/cards:**

- `claim-mcp-interoperability-not-trust`
- `claim-runtime-security-external-enforcement`
- `runtime.security.mcp-plugin-admission`
- `runtime.security.capability-policy-gateway`
- `runtime.security.strict-tool-contract`

**Candidate action:** add separate authorization tests for discovery and direct
execution; disabled or hidden tools must fail closed at the call boundary.

Sources:

- https://github.com/advisories/GHSA-c47m-m826-fc8g
- https://github.com/samanhappy/mcphub/pull/1178
- https://github.com/samanhappy/mcphub/releases/tag/v1.0.36

## 5. No qualifying quality or self-improvement evidence changed the KB

**Classification:** no-material-change  
**Evidence:** negative result from the configured interval search, not proof of
absence.

The RAG/retrieval, agentic-memory, evaluations/observability and bounded-
improvement packs produced recent papers, release notes and forum leads, but no
source found in this run combined a material claim change with sufficient
artifacts, matched baselines, scope reporting and upstream provenance. In
particular, no independent reproduction established a broadly transferable
retrieval winner, memory architecture default, calibrated LLM-judge default, or
self-modification improvement that passed paired holdout, canary and rollback
requirements.

The evidence gap is larger than usual because general web search was unavailable
and arXiv throttled most requests. This negative result must not be interpreted
as comprehensive absence of new work.
