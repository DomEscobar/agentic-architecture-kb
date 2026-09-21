# Agentic Architecture KB review-gate proposal — 2026-09-21

Review state: **proposal only; human approval required**  
Promotion authority: **false**  
Inputs reviewed: `python3 tools/freshness.py due-reviews`, all four files in
`inbox/`, 21 due technique cards, and 20 due claim records.

## Approved bounded additions — 2026-09-21

Dom approved the three weekly-scout candidates for bounded canonical inclusion.
They were incorporated as provisional evidence, without advancing existing
technique-card freshness, changing evidence levels, or promoting a default:

- Designer-RSI: frozen-context paired skill replay and coupled
  acquisition/revision ablation in `patterns/verified-procedural-memory.md`.
- APort Vault: request/policy/tool/effect-separated authorization evidence in
  `patterns/agentic-runtime-security-boundary.md`.
- Memory Decision Controller: memory-free harm control and independently scored
  pre-injection abstention in `patterns/agent-memory-evaluation-blueprint.md`.

The shared provenance and limitations are recorded in
`sources/scout-evidence-designer-rsi-aport-mdl-2026-09.md`. The remaining review
gate below stays proposal-only and requires separate approval.

## Gate decision

No canonical content was rewritten. The required freshness command reports 21
due cards and 20 due claims. The September 13 inbox remains the only newly
material inbox batch since the prior gate; its runtime/security candidates still
lack independent replay. The August candidates remain bounded by the August 24
and 31 proposals, and the private latency candidate remains E1 with no traces or
controlled comparison. Review-date expiry is not evidence of invalidity and does
not authorize an administrative extension.

## Proposed changes

### 1. Runtime effect, resume and dispatch boundaries

After release-pinned independent replay, add Google ADK 2.9.0 at-least-once
resume evidence to `runtime.durable-checkpoint-ledger`,
`runtime.safety.transactional-effect-ledger`, and
`claim-runtime-side-effect-boundary`. Add caller-versus-agent event authorship,
tenant-bound identifier resolution, and discovery-versus-dispatch authorization
as explicit slices for `runtime.tool-policy-gateway`,
`runtime.security.strict-tool-contract`, and
`runtime.security.mcp-plugin-admission`. Keep lifecycle/status and E2 levels:
release notes, issues, proposed fixes and advisories from one project remain one
upstream provenance chain.

### 2. Runtime framework cards due September 17

- `runtime.microsoft-agent-framework`: preserve the release-scoped 1.16.0 fix
  for mutable checkpoint aliasing, but retain concurrent-lineage and restricted-
  deserialization gaps. Require fixed-version identification and effect-level
  replay before advancing freshness.
- `runtime.pydantic-ai-runtime`: retain the narrow affected UI-adapter/object-
  reference scope and require vulnerable/patched cross-principal negative
  controls. Do not infer that typed schemas provide authorization.
- `runtime.security.mcp-plugin-admission` and
  `runtime.security.strict-tool-contract`: incorporate September candidates only
  as version-pinned regression inputs after replay; do not generalize route-
  specific or deployment-dependent impact.

### 3. Memory cards due September 17

For `memory.episodic-event-log` and `memory.hybrid-read-router`, preserve raw-log
lexical/temporal/local-expansion as an equal-budget control; ReFind is a single
author preprint without public run artifacts and does not establish a default.
For `memory.temporal-entity-graph`, require exact-identifier, temporal,
multi-hop, owner-isolation, and cost slices against that control. For
`memory.security.influence-gated-write`, retain source/derived separation,
owner-scoped promotion, poisoning, conflict and deletion tests. No inbox
candidate justifies a lifecycle or evidence-level change.

### 4. Coding-agent cards and claims due September 16

Re-review `evaluation.coding-agent-project-replay`,
`runtime.coding-agent-instruction-stack`, and
`runtime.evaluated-project-skill-package` together with the nine associated
coding/project-memory claims. AutoSaddler is supportive but not independent: it
is one author provenance chain, not a general RSI result, and its published
benchmark surface is not fully turn-key in the inspected repository. Preserve
current E2/E3 levels and require fresh-context paired replays, hermetic manifests,
deterministic execution-aligned oracles, protected safety slices, repeated runs,
and equal-budget overhead reporting before advancing review dates.

### 5. Other due cards and claims

- Administrative re-review only, with no material contradiction found:
  `evaluation.paired-perturbation-replay`, `memory.lineage-forgetting`,
  `rsi.archive-variant-search`, `rsi.canary-kill-rollback`,
  `rsi.fixed-evaluator-epoch`, `runtime.approval-interrupt`,
  `claim-rsi-evaluator-epoch`, `claim-runtime-not-single-loop`, and
  `claim-runtime-one-primary-loop`.
- Keep provisional pending better provenance or owner evidence:
  `claim-bauhelfer-structured-output`, `claim-document-hybrid-fit`,
  `claim-pageindex-hierarchical-navigation`, and
  `claim-memory-framework-workload-fit`.
- Keep `claim-public-architect-isolation` accepted, but do not extend freshness
  without rerunning deployment artifacts; owner-produced verification is not an
  independent penetration test.
- `claim-transition-statistics-require-measured-null` is due today. Its pinned
  reduced-record analysis is reproducible and supports the bounded claim, but it
  remains a single author-controlled study. Re-run the 45-test artifact suite and
  `analysis/nulls.py`; retain E3 and the model/workload-specific limits unless an
  independent replication is found.

## Rejected or watch-only evidence

- Reject issue/PR/release/advisory clusters from one project as independent
  corroboration, and reject unmerged fixes as protection for released versions.
- Reject exactly-once inference from checkpointing, authorization inference from
  schema validation or tool omission, and universal host-escape claims from
  deployment-dependent primitives.
- Reject promotion from the private multi-domain latency report: it still lacks
  stage traces, a replay set, controlled arms, and verified effect sizes.
- Reject universal graph-memory, PageIndex, project-memory, instruction-stack,
  skill, or harness conclusions from vendor/private/single-study evidence.
- Treat radar negative searches as bounded observations only; web-search failure
  and arXiv throttling make absence claims incomplete.

## Tests required before canonical changes

1. ADK 2.9.0 crash-after-effect/resume and caller-authored pending-call replays,
   with duplicate, omitted, unauthorized-effect and reconciliation counters.
2. Vulnerable/fixed Flowise, ADK artifact-service and MCPHub fixtures covering
   tenant ownership, encoded paths, direct calls, hidden/disabled tools, OAuth
   client authentication and PKCE.
3. Microsoft checkpoint immutability, nested read isolation, lineage reachability,
   pending-request round trip, upgrade/rollback and crash-around-effect tests.
4. Pydantic AI vulnerable/patched cross-principal object-reference tests plus
   durable replay and API-migration checks.
5. Memory raw-log versus hybrid/graph equal-budget replay across exact identifier,
   fact tracking, event order, temporal and multi-hop slices; include leakage,
   poisoning, owner-scope, deletion, latency and cost-per-correct-answer metrics.
6. Coding harness paired fresh-context replay with pinned manifests, execution-
   aligned deterministic oracles, safety sentinels, recovery, variance and total
   token/latency/tool/human cost.
7. RSI evaluator-hash, frozen-null, protected-holdout, canary, kill-switch and
   rollback drills; rerun the Phantom Gains pinned artifact checks.
8. Owner/corpus-specific Bauhelfer, public-isolation and PageIndex validation;
   then schema/ID/contradiction checks, compile/lint and protected retrieval,
   runtime, memory and security evals before human approval.

## Rollback impact

This run adds only this proposal and regenerates
`reports/freshness-due-reviews.json`. Rollback is deletion of this report and
regeneration of the dated freshness artifact. No canonical claim, technique,
index, threshold, release, runtime, merge, commit, push, deploy or promotion was
performed. Any later approved change must keep evidence/status edits separable
from review-date changes and preserve the prior pinned adapter/card plus tested
kill switch and rollback path.

## Unresolved questions

- Which released versions fix ADK caller-authored resume dispatch, artifact
  identifier traversal, and MCPHub disabled-tool direct execution?
- Can independent replays reproduce the Flowise, MCPHub, ADK, Pydantic AI and
  Microsoft failure/fix pairs against deployed wrappers?
- Are fresh owner-reviewed Bauhelfer and public-isolation artifacts available,
  and has PageIndex published independent equal-budget hierarchy evidence?
- Can ReFind, AutoSaddler and Phantom Gains be independently reproduced on other
  backbones, domains and execution stacks?
- Who owns the complete due-card eval run and approval to advance review dates?
