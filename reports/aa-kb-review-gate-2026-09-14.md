# Agentic Architecture KB review-gate proposal — 2026-09-14

Review state: **proposal only; human approval required**  
Promotion authority: **false**  
Inputs reviewed: `python3 tools/freshness.py due-reviews`, all four files in
`inbox/`, the ten due technique cards, and the nine due claim records.

## Gate decision

No canonical content was rewritten. Ten technique cards and nine claims became
due on 2026-09-12. The 2026-09-13 radar also contains four material runtime and
security candidates. The new evidence supports narrower, version-pinned failure
modes and regression slices, but it is upstream-only E1/E2 evidence and does not
justify promotion or a higher evidence level.

The older August 16 and August 30 radar candidates remain bounded by the August
24/31 proposals. The private multi-domain latency report remains E1 and is not
due until 2026-10-04; it supplies a replay plan, not a causal latency result.

Pre-existing working-tree changes were not reviewed, modified, or incorporated
except for the deterministic freshness report written by the required command.

## Proposed changes

### Runtime effect and resume boundary

Google ADK Python 2.9.0 explicitly documents at-least-once rerun of failed nodes.
This directly supports `claim-runtime-side-effect-boundary`,
`runtime.durable-checkpoint-ledger`, and
`runtime.safety.transactional-effect-ledger`, but the release note and linked
implementation are one maintainer provenance chain. Separately, issue 7076 and
unmerged PR 7077 report that resumable mode can execute a caller-seeded function
call without proving agent authorship. This is scoped to opt-in resumable mode
and remains unresolved in the cited 2.9.0 release.

**Proposal after independent replay:** add ADK 2.9.0 as version-pinned evidence;
make resume-event authorship and authoritative effect identity explicit failure
modes. Retain E2/situational status and the current scope limits.

### Cross-scope identifiers and tool-policy enforcement

Flowise through 3.1.3 is covered by a reviewed upstream advisory naming 3.1.4
as fixed. Google ADK's `FileArtifactService` path-separator report is a public
maintainer issue with an unmerged fix and does not apply to the stock Starlette
route as described. MCPHub's OAuth issue is a reviewed advisory fixed before
1.0.32; the disabled-tool direct-call bypass is an open project PR and has not
been tied to a fixed release. Each defect has only one upstream provenance
chain; none was independently reproduced.

**Proposal after replay:** add narrow regression evidence to the capability
gateway, strict tool contract, MCP admission, and permission-filter surfaces.
Require tenant/workspace binding when resolving opaque IDs; validate path-like
identifiers at service boundaries; and enforce tool enablement at dispatch, not
only discovery. Do not generalize the ADK artifact issue to deployments that do
not expose caller-controlled identifiers.

### Due cards and claims

- **Refresh with material evidence after tests:**
  `evaluation.deterministic-state-oracle`,
  `runtime.durable-checkpoint-ledger`,
  `runtime.safety.transactional-effect-ledger`,
  `runtime.tool-policy-gateway`, and
  `claim-runtime-side-effect-boundary`. The August advisories and September ADK,
  Flowise, and MCPHub candidates sharpen failure modes; they do not alter the
  cards' lifecycle or evidence level.
- **Administrative re-review only; no material contradiction found:**
  `evaluation.paired-perturbation-replay`, `memory.lineage-forgetting`,
  `rsi.archive-variant-search`, `rsi.canary-kill-rollback`,
  `rsi.fixed-evaluator-epoch`, `runtime.approval-interrupt`,
  `claim-rsi-evaluator-epoch`, `claim-memory-framework-workload-fit`,
  `claim-runtime-not-single-loop`, and `claim-runtime-one-primary-loop`.
  The September radar reports no qualifying quality, memory, evaluation, or RSI
  change; that negative search was incomplete because general web search failed
  and arXiv was throttled.
- **Keep provisional and request owner/corpus refresh:**
  `claim-bauhelfer-structured-output`, `claim-document-hybrid-fit`, and
  `claim-pageindex-hierarchical-navigation`. Their private/vendor-derived
  provenance is unchanged and insufficient for promotion.
- **Keep accepted, but require deployment re-verification before extending the
  review date:** `claim-public-architect-isolation`. Its evidence remains
  owner-produced rather than an independent penetration test.

## Rejected or watch-only evidence

- Treat ADK issue/PR pairs, release notes, Flowise/MCPHub advisories and their
  project fixes as single upstream chains, not independent corroboration.
- Reject any inference that checkpointing supplies exactly-once effects, that a
  proposed/unmerged fix protects a released version, or that hidden/disabled
  tools are blocked merely because discovery omits them.
- Reject promotion from the multi-domain latency report: it contains no traces,
  replay set, controlled comparison, or verified effect size.
- Retain the September radar's RAG, memory, evaluation, and RSI negative result
  only as a bounded search result, not proof that no relevant work exists.

## Tests required before canonical changes

1. Replay ADK 2.9.0 crash-after-effect/resume with runtime-generated operation
   IDs; measure duplicate effects and reconciliation across every crash boundary.
2. Run caller-authored versus agent-authored pending-function-call fixtures on
   ADK 2.7.1, 2.8.0, 2.9.0, and the eventual fixed release; assert policy and
   provenance checks occur before dispatch.
3. Replay Flowise 3.1.3 and 3.1.4 with two workspaces, opaque credential IDs, and
   authoritative provider-call observations; verify no cross-workspace use.
4. Test ADK artifact identifiers across direct service calls and stock HTTP
   routes for read, overwrite, delete, traversal encodings, symlinks, and tenant
   isolation; preserve route-specific scope.
5. Test MCPHub vulnerable/fixed OAuth flows for mandatory client authentication
   and PKCE; separately test discovered, hidden, disabled, and direct
   `tools/call` paths at the dispatch boundary.
6. Re-run due-card unit/mutation, paired replay, forgetting, evaluator-hash,
   canary/rollback, approval replay, and policy-gateway slices before changing
   dates. Re-run owner-specific Bauhelfer and public-isolation evidence rather
   than extending review dates administratively.
7. Validate schemas/IDs and contradictions, compile/lint, run protected
   retrieval/runtime/security evals, and obtain human approval before promotion.

## Rollback impact

This gate adds only this proposal and refreshes the reproducible
`reports/freshness-due-reviews.json`. Rollback is deletion of this report and
regeneration of the due-review output for the same date. No runtime, index,
threshold, canonical page, claim, technique card, or consumer release changed.

Any later approved runtime change must retain the previous pinned adapter and
ledger schema, support pending-run migration or abort, and preserve a tested
kill switch. Security fixture changes are additive and independently removable.
Any review-date update must be separately revertible from evidence-level or
status changes.

## Unresolved questions

- Which released ADK version, if any, fixes caller-authored resume dispatch and
  artifact identifier traversal?
- Does MCPHub's disabled-tool execution fix ship, and do all transports share
  the same dispatch-time authorization path?
- Can independent replays reproduce the Flowise and MCPHub advisories and the
  ADK resume failures against the actual deployed wrappers?
- Are fresh owner-reviewed Bauhelfer and public-isolation artifacts available?
- Has PageIndex published independent hierarchy-fidelity and equal-budget
  retrieval evidence since the last review?
- Who owns the full due-card eval run and the approval to advance review dates?

