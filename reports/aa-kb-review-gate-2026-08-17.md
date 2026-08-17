# Agentic Architecture KB review-gate proposal — 2026-08-17

Review state: **proposal only; human approval required**  
Promotion authority: **false**  
Input reviewed: `inbox/research-radar-2026-08-16.md`  
Due-review result: no due technique cards and no due claims as of 2026-08-17.

## Gate decision

Six candidates are material enough to retain as review and regression-test
proposals. None meets the evidence bar for autonomous promotion or for changing
an accepted claim. The Cordis/DeepSeek Harness lead and all lane-level negative
results remain watch-only or rejected evidence.

The inbox report also contains two broken affected-card references that must be
fixed in the candidate before any promotion review:

- `runtime.transactional-effect-ledger` should be
  `runtime.safety.transactional-effect-ledger`.
- `retrieval.security.metadata-permission-filter` should be
  `retrieval.metadata.permission-filter`.

## Material proposals

### 1. Agent/MCP boundary advisories — retain as urgent regression evidence

**Provenance and independence.** GitHub Advisory Database records published
between 2026-08-12 and 2026-08-14 confirm the affected and patched ranges for
Pydantic AI, Token Optimizer MCP, Stata MCP, ContextForge and
`atomic-agents-stack`. Linked commits and releases are the same upstream
provenance as their GHSAs, not independent corroboration. No independent replay
was found.

**Scope and contradiction review.** These incidents support, rather than
contradict, the existing external-enforcement, strict-contract, sandbox and MCP
admission claims. They do not show that schema validation or a container alone
is sufficient. Applicability is conditional: the Pydantic AI issue requires an
affected UI adapter and attacker-known/guessed provider object reference;
ContextForge requires the non-default admin API plus `gateways.read`; dashboard
file exposure depends on reachability; the shell cases require affected tools
to be enabled and reachable.

**Proposed reviewed change after replay.** Register the five upstream projects
and six advisories in `freshness/projects.json`; create one admitted security
source audit; add version-pinned evidence links and narrow failure modes to the
affected high-risk cards. Do not raise claim evidence levels.

**Affected evaluation slices.** Provider-file confused deputy with application
credentials; cross-principal object references; newline and command-substitution
arguments; traversal with encoded/mixed separators and symlinks; DNS rebinding
between validation and connect; redirects and link-local metadata; dashboard
loopback/beyond-loopback exposure; fixed-version negative controls.

### 2. Microsoft Agent Framework checkpoints — add adoption-gate tests

**Provenance and independence.** Issues 7683, 7647 and 7618 are open maintainer-
repository reports created 2026-08-11 through 2026-08-16. They are separate
failure reports but not independent studies. Issue 7683 includes two minimal
reproductions and reports runs across Python 3.11–3.13 and Windows/Linux; those
runs remain one reporter's evidence. Issue 7647 explicitly reports correct final
results and no demonstrated duplicate effects. Issue 7618 is a narrower hosted-
resume report without a complete public reproduction.

**Scope and contradiction review.** The reports support the existing
release-specific adoption and side-effect-boundary claims. They do not prove
external effect loss, duplication or authorization bypass. The shallow-copy and
in-memory-store aliasing report targets `agent-framework-core==1.14.0`; the
lineage and pending-request reports target 1.13.0-era surfaces.

**Proposed reviewed change after replay.** Add release-pinned checkpoint tests
to the Microsoft runtime card and the durable-checkpoint/effect-ledger adoption
gate. Keep the runtime card at E2 and prerelease-quality language until a fixed
release is verified.

**Affected evaluation slices.** Immutable snapshot after restore; storage-read
isolation; nested mutable state; concurrent sibling checkpoint lineage; latest-
lineage reachability; pending request serialization round trip; upgrade/downgrade
resume; crash injection around external effects; duplicate, omitted and
unauthorized-effect counters.

### 3. ReFind raw-log search — require a lexical memory baseline

**Provenance and independence.** arXiv:2608.12888v1 was published 2026-08-13.
The paper reports matched GPT-4o-mini backbones over roughly 2,800
MemoryAgentBench precise-retrieval/fact-tracking questions, named baselines and
ablations, but publishes no implementation or run artifact. Reused baseline
results and the authors' runs are one study, not independent corroboration.

**Scope and contradiction review.** The 58.2 mean versus HippoRAG 2's 53.2 is
bounded to the reported task subset and setup. On LongMemEval-S/M, the paper's
five-run ReFind result (93.2 +/- 3.3 and 89.3 +/- 6.0) is exactly the reported
five-run BM25 control, so it does not establish a gain there. This is
counterevidence to adopting graph/tree memory without a lexical control, but it
does not contradict governed writes, provenance, deletion, tenant filtering, or
type-aware routing. ReFind itself uses session ranking, temporal narrowing and
local expansion, so it is not evidence that routing controls are useless.

**Proposed reviewed change after artifact release/replay.** Add raw immutable
event-log BM25 plus temporal/local expansion as a mandatory memory-selection
baseline. Do not adopt numeric rankings or weaken graph-memory use cases.

**Affected evaluation slices.** Exact entity/identifier lookup; fact tracking;
temporal narrowing; session fusion; local expansion; multi-hop and event-order
counter-slices; irrelevant-memory rate; cross-tenant exclusion; deletion; equal
backbone, prompts, context budget and reranking budget across BM25, dense,
hybrid and graph baselines.

### 4. Memory serving cost — add lifecycle cost instrumentation

**Provenance and independence.** arXiv:2608.11879v1 was published 2026-08-12.
It is one controlled author-reported study with no linked code or cached-run
artifact. It compares three memory systems, two backbones, synthetic cost
dialogues through 400 turns, and accuracy on 665 questions drawn from four
LoCoMo dialogues. The paper states that question-level confidence intervals
understate uncertainty because questions are clustered by dialogue.

**Scope and contradiction review.** The 18–69 percent cost-model miss, 21–54
percent accuracy range and no-break-even-within-400-turn observations are
bounded findings, not universal rankings. They support the current
workload-specific selection and full-lifecycle evaluation claims.

**Proposed reviewed change after artifact release/replay.** Extend the memory
evaluation blueprint with separately metered ingest, extraction, retrieval,
consolidation and answer stages plus cost-per-correct-answer. Do not encode a
universal break-even threshold.

**Affected evaluation slices.** Conversation depth, message size, backbone,
rolling-window and full-history controls; warm/cold ingest; consolidation
frequency; retrieved-context size; cached/uncached execution; token and billed
cost; latency; accuracy; clustered bootstrap uncertainty; break-even curves and
cost-per-correct-answer.

### 5. ToolHazard — admit only as a development evaluation candidate

**Provenance and independence.** arXiv:2608.11878v1 and the MIT-licensed
`MurrayTom/ToolHazard` repository were published in the same project and are one
upstream source. The repository contains executable environments, benchmark
data and state checkers. Its README warns that scripts retain absolute paths and
that SFT/RL dependencies are absent from `requirements.txt`; reported paper
results use prompt mode. A clean full reproduction was not established.

**Scope and contradiction review.** The reported 87 tasks, 28 environments,
512 tools, mean 15.56 steps and 18.75 candidate tools describe the generated
benchmark distribution. They support deterministic state oracles and adaptive
attack replay, but do not establish production transfer or universal security.

**Proposed reviewed change after clean replay.** Add ToolHazard as an optional
development suite with a pinned commit and environment manifest. Keep protected
workload cases and existing AgentDojo/InjecAgent controls; do not use it as a
promotion oracle by itself.

**Affected evaluation slices.** Clean-install reproducibility; benign utility;
authoritative pre/post state; attack-point reachability; multi-turn horizon;
changed tool schemas and models; generated-versus-real environment transfer;
prompt versus function-calling mode; adaptive holdout attacks; dependency and
absolute-path isolation.

### 6. Graph-memory cross-user poisoning — retain as a threat hypothesis

**Provenance and independence.** Neo4j Labs issue 155 is an open public report
against `neo4j-agent-memory==0.5.0`; the detailed PoC and logs are private and
upstream maintainers have not confirmed the issue. The separate
`joslat/agent-memory-dotnet` repository contains owner-scope migrations,
fail-closed modes and integration fixtures, but it is an independent
implementation, not an independent reproduction of issue 155. It supports the
control's plausibility, not the upstream vulnerability claim.

**Scope and contradiction review.** The report applies to shared graph-memory
deployments that ingest untrusted user content without complete owner/trust
scoping. It may be an unsafe host configuration rather than an upstream product
vulnerability. It supports existing untrusted-write, temporal/conflict and
pre-ranking permission-filter claims; it does not justify rejecting graph
memory generally.

**Proposed reviewed change after public fixture/replay.** Add the failure mode
and owner-scoped regression fixture to graph-memory and influence-gated-write
evaluations. Do not cite issue 155 as accepted empirical evidence until the PoC
is public or independently replayed.

**Affected evaluation slices.** Two tenants reusing identical entity names;
shared versus isolated graph; owner stamping on nodes, edges, facts and derived
summaries; merge/refresh/consolidation paths; pre-ranking owner filters;
conflicting-claim representation; cross-session retrieval; deletion and
supersession; fail-closed behavior for missing ownership metadata.

## Rejected or watch-only evidence

- **Cordis/DeepSeek Harness:** keep watch-only. The Harness README calls the
  project a developer preview with compatibility-breaking changes; Cordis says
  its API is unstable. Official repositories establish implementation, not
  comparative quality, durability or self-improvement.
- **Sinhala/Tamil retrieval study:** no canonical change. The 500-question,
  1,699-context result is a bounded confirmation of language/workload-specific
  embedding selection.
- **OpRAG:** no admission beyond the inbox. The latency claims have no linked
  auditable implementation or run artifact.
- **OpenTelemetry semantic conventions 1.44.0:** release notes contain no
  material agent evaluation or state-oracle contract.
- **ATOBench:** paper claims are not admitted because the linked repository is
  only a two-line placeholder and supplies no reproducibility artifact.
- **AQuA and SBCO:** keep as bounded-optimization leads. No linked code/run
  artifacts were found; neither weakens fixed evaluator epochs, protected
  holdouts, paired comparison or rollback.

## Tests required before any canonical change

1. Replay every vulnerable and first-patched security release in an isolated,
   credential-free fixture, including fixed-version negative controls.
2. Replay all Microsoft checkpoint cases on pinned 1.13.0/1.14.0 and the first
   claimed fixed release, then inject crashes around authoritative effects.
3. Reproduce ReFind and the memory-cost study from public code, prompts, inputs
   and raw outputs; compare against equal-budget local baselines.
4. Run ToolHazard from a clean environment with a locked dependency manifest
   and record dataset, environment, model, prompt and result digests.
5. Obtain or independently build an upstream-versioned graph-poisoning fixture
   and verify every owner-scoped read, write, merge and refresh path.
6. Before promotion: validate IDs/schema, run contradiction and claim-coverage
   checks, compile/lint, execute protected retrieval/security slices, obtain
   human approval, and release consumers separately.

## Rollback impact

This proposal changes no canonical claim, technique card, synthesis, index or
consumer. Its rollback is deletion of this report only. If later approved,
registry/source/evaluation additions are independently revertible. Any future
claim wording, status or evidence-level change would alter retrieval and
downstream consumers and therefore requires a new compiled artifact, paired
evaluation, human-approved consumer release and the prior release lock for
rollback.

## Unresolved questions

- Will independent parties reproduce any of the six security advisories, and
  do the first patched releases close every documented path?
- Which Microsoft Agent Framework release fixes snapshot isolation, lineage and
  pending-request restore, and can any defect create an external effect error?
- Will ReFind and the memory-cost authors release code, prompts, cached inputs
  and raw outputs?
- Can ToolHazard be reproduced without editing experiment paths, and how well do
  generated environments transfer to protected real-tool workloads?
- Is neo4j-agent-memory issue 155 reproducible under the product's documented
  deployment model, and will upstream classify it as a vulnerability,
  hardening gap or host responsibility?
- Who owns the new regression fixtures and what protected-slice thresholds are
  required for promotion?
