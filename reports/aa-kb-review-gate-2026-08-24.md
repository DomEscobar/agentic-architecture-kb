# Agentic Architecture KB review-gate proposal — 2026-08-24

Review state: **proposal only; human approval required**  
Promotion authority: **false**  
Inputs reviewed: `python3 tools/freshness.py due-reviews` and every candidate in
`inbox/research-radar-2026-08-16.md`  
Due-review result: no due technique cards and no due claims as of 2026-08-24.

## Gate decision

Retain the same six material candidates as review and regression-test proposals.
Do not change an accepted claim, technique card, synthesis, index, evaluation
threshold or consumer. Freshness checks found no independent reproduction or
fixed-release replay that clears a promotion gate.

This review corrects one provenance detail and records one artifact change since
the 2026-08-17 proposal:

- ReFind is currently arXiv `2608.12888v2`, updated 2026-08-16, rather than v1.
  The reported results remain author evidence and no public implementation or
  run artifact was found.
- ToolHazard commit `544b73b12a25431cb0be3eb43df41b4aacce5335`
  expanded its README on 2026-08-18. The README now documents the pipeline more
  clearly but still says that scripts retain absolute experiment paths and that
  SFT/RL dependencies are absent from `requirements.txt`; a clean end-to-end
  reproduction is still missing.

Pre-existing changes elsewhere in the working tree were not reviewed, modified
or included in this proposal.

## Material proposals

### 1. Agent and MCP boundary advisories — urgent regression evidence only

**Provenance, independence and freshness.** The six GitHub Advisory Database
records, linked upstream commits and releases remain one upstream provenance per
defect, not independent corroboration. As checked on 2026-08-24, all GHSAs retain
their original published/updated timestamps and first-patched versions:
Pydantic AI 1.106.0/2.0.0b6; Token Optimizer MCP 5.1.0; Stata MCP 1.19.0;
ContextForge 1.0.3; and `atomic-agents-stack` 1.1.0. Later releases exist but no
independent vulnerable/fixed replay was found.

**Contradictions and scope.** The advisories reinforce external enforcement,
strict contracts, sandboxing and MCP admission; they do not establish that
schemas or containers alone are sufficient. Scope remains conditional on the
affected adapter/tool being reachable, attacker-controlled references or
arguments, application credentials, relevant ContextForge privileges, and
dashboard/network reachability.

**Proposed change after replay.** Keep the registered advisories and project
watch entries. Add version-pinned regression fixtures and narrow evidence links
to affected high-risk cards only after independent replay. Do not raise claim
evidence levels.

**Affected evaluation slices.** Cross-principal provider-file references;
newline and command-substitution arguments; traversal with encoded separators
and symlinks; DNS rebinding between validation and connection; redirects and
link-local metadata; loopback and externally bound dashboards; first-patched
negative controls.

### 2. Microsoft Agent Framework checkpoints — adoption-gate tests only

**Provenance, independence and freshness.** Issues 7683, 7647 and 7618 remain
open and carry the repository's `reproduced` label. Their reproduction notes are
explicitly agent-authored automated triage inside the same maintainer repository,
not independent studies. No suspected fix commit is recorded. The reports cover
1.14.0 snapshot/store aliasing and 1.13.0-era parallel lineage and pending-request
deserialization. Issue 7647 still does not demonstrate result loss or duplicate
external effects.

**Contradictions and scope.** These reports support release-specific adoption
and explicit side-effect-boundary claims. They do not prove authorization bypass,
duplicate effects or omitted effects.

**Proposed change after replay.** Add pinned checkpoint isolation, lineage and
round-trip cases to the runtime adoption gate. Keep prerelease-quality language
until the vulnerable and first fixed releases are independently replayed.

**Affected evaluation slices.** Nested mutable state; immutable snapshots;
storage-read isolation; concurrent sibling lineage and latest-lineage
reachability; pending request round trips; upgrade/downgrade resume; crash
injection around authoritative effects; duplicate, omitted and unauthorized
effect counters.

### 3. ReFind raw-log search — mandatory baseline candidate

**Provenance, independence and freshness.** arXiv `2608.12888v2` is a single
author-reported study. It reports matched backbones, named baselines, component
ablations and repeated LongMemEval runs, but no code, prompts, outputs or result
artifact was linked or found in an exact GitHub repository search. Reused
baseline results are not independent replication.

**Contradictions and scope.** The reported 58.2 versus 53.2 result is bounded to
the stated MemoryAgentBench subset and setup. The LongMemEval result does not
establish improvement over the paper's equal reported BM25 control. This is
counterevidence to adopting graph/tree memory without a lexical control, not to
governed writes, provenance, deletion, tenant filtering or type-aware routing.

**Proposed change after artifact release/replay.** Require raw immutable event-log
BM25 with temporal narrowing and local expansion as a memory-selection baseline.
Do not adopt the numeric ranking or weaken graph-memory use cases.

**Affected evaluation slices.** Exact lookup; fact tracking; temporal narrowing;
session fusion; local expansion; multi-hop and event order; irrelevant-memory
rate; tenant exclusion and deletion; equal backbone, prompt, context and
reranking budgets across lexical, dense, hybrid and graph baselines.

### 4. Memory serving cost — lifecycle instrumentation candidate

**Provenance, independence and freshness.** arXiv `2608.11879v1` remains a
single controlled preprint with no linked code or cached-run artifact. Its two
backbones, three memory systems, conversations through 400 turns and 665 LoCoMo
questions are useful but bounded; question-level intervals remain clustered
within only four dialogues.

**Contradictions and scope.** The reported 18–69% model miss, 21–54% accuracy
range and no-break-even-within-400-turn cells do not establish a universal cost
ranking. They support workload-specific selection and full-lifecycle evaluation.

**Proposed change after artifact release/replay.** Meter ingest, extraction,
retrieval, consolidation and answer stages separately and report cost per correct
answer. Do not encode a universal break-even point.

**Affected evaluation slices.** Conversation depth and message size; backbone;
rolling-window and full-history controls; warm/cold ingest; consolidation
frequency; cached/uncached execution; token, billed cost and latency; accuracy;
task-cluster uncertainty; break-even curves.

### 5. ToolHazard — development evaluation candidate only

**Provenance, independence and freshness.** arXiv `2608.11878v1` remains marked
work in progress. The paper and MIT-licensed repository are one project. The
August 18 README improves pipeline documentation, but the repository still
requires manual path edits and omits SFT/RL dependencies from its lock surface.
No independent clean replay was found.

**Contradictions and scope.** Executable state checks support deterministic
oracles and adaptive attack replay. The 87 tasks, 28 environments and 512 tools
describe a generated distribution; they do not establish production transfer or
universal security.

**Proposed change after clean replay.** Admit a pinned commit and environment
manifest as an optional development suite. Preserve protected workload cases and
existing controls; never use ToolHazard alone as a promotion oracle.

**Affected evaluation slices.** Clean install; benign utility; authoritative
pre/post state; attack-point reachability; long horizons; tool-schema/model
changes; generated-to-real transfer; prompt versus function-calling mode;
adaptive holdouts; dependency, path and environment isolation.

### 6. Graph-memory cross-user poisoning — threat hypothesis only

**Provenance, independence and freshness.** Neo4j Labs issue 155 remains open
without a public PoC or maintainer confirmation. Its 2026-08-23 update is a new
comment linking a separate memory project and recommending provenance-aware
retrieval; it does not reproduce the reported vulnerability. The .NET port's
owner-scoping fixtures support control plausibility but are not a reproduction
of `neo4j-agent-memory==0.5.0`.

**Contradictions and scope.** The hypothesis applies to shared graph deployments
that ingest untrusted content without complete owner/trust scoping. It may be a
host configuration failure rather than an upstream vulnerability. It supports
untrusted-write, conflict/temporal and pre-ranking permission controls; it does
not justify rejecting graph memory generally.

**Proposed change after public fixture/replay.** Add a versioned two-tenant
failure fixture and owner-scoped regression case. Do not cite issue 155 as
accepted empirical evidence yet.

**Affected evaluation slices.** Identical entity names across two tenants;
shared versus isolated graphs; ownership on nodes, edges, facts and summaries;
merge/refresh/consolidation paths; pre-ranking filters; conflict representation;
cross-session retrieval; deletion/supersession; fail-closed missing metadata.

## Rejected or watch-only evidence

- **Cordis/DeepSeek Harness:** both repositories were active through 2026-08-21,
  but Harness still declares developer preview with compatibility-breaking
  changes and Cordis still declares its API unstable. Implementation activity
  is not evidence of comparative quality, durability or self-improvement.
- **Sinhala/Tamil retrieval study:** no canonical change; it remains a bounded
  confirmation that embedding choice is language- and workload-specific.
- **OpRAG:** no admission; arXiv remains v1 and no auditable implementation or
  run artifact is linked.
- **OpenTelemetry semantic conventions 1.44.0:** no material agent evaluation or
  state-oracle contract identified.
- **ATOBench:** reject paper claims for promotion; the linked GitHub repository
  remains an empty placeholder (`size: 0`, last push 2026-08-13).
- **AQuA:** arXiv advanced to v2 on 2026-08-17, but no public code or run artifact
  was found. Its bounded-loop claims do not replace equal-budget generational
  comparisons, protected holdouts or fixed evaluator epochs.
- **SBCO:** remain watch-only; no linked code/run artifact was found, and
  co-learning verifier and harness surfaces does not weaken protected evaluator,
  paired comparison or rollback requirements.

## Tests required before any canonical change

1. Independently replay every vulnerable and first-patched security release in
   credential-free isolation, with patched negative controls.
2. Replay Microsoft checkpoint cases on pinned affected and first-fixed releases,
   then inject crashes around authoritative effects.
3. Reproduce ReFind and the memory-cost study from public code, prompts, inputs
   and raw outputs against equal-budget local baselines.
4. Run ToolHazard from a clean environment with a locked dependency and artifact
   manifest; record data, environment, model, prompt and result digests.
5. Obtain or independently create an upstream-versioned graph-poisoning fixture
   and test every owner-scoped read, write, merge and refresh path.
6. Before promotion, validate IDs and schemas, run contradiction/claim-coverage
   checks, compile and lint, execute protected retrieval/security slices, obtain
   human approval, and release consumers separately.

## Rollback impact

This proposal adds one report only. It changes no canonical claim, technique
card, synthesis, evaluation or consumer. Rollback is deletion of this report.
Any later approved source, registry or fixture addition should be independently
revertible. A future claim/status/evidence change requires a new compiled
artifact, paired evaluations, a human-approved consumer release and retention of
the previous release lock.

## Unresolved questions

- Will independent parties replay the six advisories and verify all first-patched
  negative controls?
- Which Microsoft release fixes each checkpoint defect, and can any defect cause
  an external effect error?
- Will the ReFind and memory-cost authors publish code, prompts and raw outputs?
- Can ToolHazard run end to end without manual path edits, undeclared dependencies
  or experiment-specific infrastructure?
- Is Neo4j issue 155 reproducible under the documented deployment model, and how
  will upstream classify responsibility?
- Who owns the regression fixtures, and what protected-slice thresholds are
  required for promotion?
