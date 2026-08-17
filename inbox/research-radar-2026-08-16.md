---
id: source-research-radar-2026-08-16
type: source
title: Biweekly Agentic Architecture Research Radar 2026-08-16
status: inbox
privacy: internal
confidence: 0.88
created_at: 2026-08-16T07:00:00+02:00
updated_at: 2026-08-16T09:44:00+02:00
review_at: 2026-08-30
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

# Biweekly Agentic Architecture Research Radar — 2026-08-16

This is an automated research candidate, not reviewed knowledge. The six query
packs were executed for the interval beginning 2026-08-02. Primary repositories,
release notes, specifications, reviewed advisories, recent papers and public
issue threads were inspected. The configured web-search provider was disabled,
so discovery used the GitHub API, GitHub Advisory Database, arXiv API and direct
primary-source retrieval. A GitHub advisory and its repository advisory are one
upstream source, not independent corroboration.

## 1. Agent and MCP boundary advisories require version-pinned review

**Classification:** security-critical  
**Evidence:** E2, reviewed upstream advisories with public vulnerable paths,
proofs of concept and fixed versions; no independent reproduction was found in
this run.

Five distinct advisories expose the same architectural failure class: an agent
or MCP adapter accepts an untrusted reference or argument, then resolves it with
server credentials or interpolates it into a privileged filesystem, network or
shell operation.

- Pydantic AI UI adapters accepted client-supplied `UploadedFile` references
  and let the model provider resolve them with the application's identity.
  Affected releases are `pydantic-ai` and `pydantic-ai-slim` 1.65.0 through
  1.105.x, and 2.0.0b1 through 2.0.0b5. Fixed releases are 1.106.0 and
  2.0.0b6. The scope requires an application to pass untrusted client message
  history through an affected UI adapter and an attacker to know or guess a
  valid provider or cloud object identifier.
- Token Optimizer MCP before 5.1.0 shell-interpolated the MCP-controlled
  `smart_user.get-user-info.username` value. The published proof of concept
  executes command substitution as the MCP server user. The same release also
  fixes unauthenticated traversal from dashboard `sessionId` values to readable
  `.jsonl` files outside the intended log directory.
- Stata MCP before 1.19.0 accepted newlines in the default-enabled
  `ado_package_install.package` argument, allowing a second Stata `shell`
  command to execute as the server account. The advisory includes a container
  reproduction that does not require a Stata license.
- ContextForge before 1.0.3 checked DNS-resolved addresses before an HTTP
  request but re-resolved the hostname at connect time, leaving a DNS-rebinding
  SSRF gap. Exploitation requires the non-default admin API and a database role
  with `gateways.read`; the affected endpoint can expose internal services or
  cloud metadata when those prerequisites hold.
- `atomic-agents-stack` through 1.0.0 served optional dashboard paths without
  containment. Version 1.1.0 fixes arbitrary file read; exposure is higher when
  the dashboard is bound beyond loopback, though loopback remains reachable
  through another SSRF or some DNS-rebinding paths.

**Affected claims/cards:**

- `claim-runtime-security-external-enforcement`
- `claim-mcp-interoperability-not-trust`
- `claim-sandbox-boundary-configured`
- `runtime.pydantic-ai-runtime`
- `runtime.security.strict-tool-contract`
- `runtime.security.mcp-plugin-admission`
- `runtime.security.isolated-tool-sandbox`
- `runtime.security.capability-policy-gateway`

**Candidate action:** register the affected upstream projects and advisories for
freshness monitoring; add regression cases for provider-file confused-deputy
access, newline and command-substitution arguments, path containment, and DNS
rebinding between validation and connection. Do not promote this finding until
the vulnerable and fixed releases are independently replayed or otherwise
corroborated.

Sources:

- https://github.com/advisories/GHSA-h7p7-w5gc-xj3w
- https://github.com/pydantic/pydantic-ai/releases/tag/v1.106.0
- https://github.com/pydantic/pydantic-ai/releases/tag/v2.0.0b6
- https://github.com/advisories/GHSA-49mq-fc6q-3h46
- https://github.com/advisories/GHSA-76pc-mqxp-3rq5
- https://github.com/ooples/token-optimizer-mcp/commit/b4ee96dac799cbfba0a9f9c17844ce9d613cbcc7
- https://github.com/ooples/token-optimizer-mcp/releases/tag/v5.1.0
- https://github.com/advisories/GHSA-49m4-vp58-wgc9
- https://github.com/SepineTam/mcp-for-stata/releases/tag/v1.19.0
- https://github.com/advisories/GHSA-9hgc-g3w5-67cm
- https://github.com/IBM/mcp-context-forge/releases/tag/v1.0.3
- https://github.com/advisories/GHSA-rm43-82j9-r4mj
- https://github.com/dep0we/atomic-agents-stack/commit/ec474f458122c5c0ca718d0df3078c8080338b2c

## 2. Microsoft Agent Framework checkpoint state is not a stable snapshot

**Classification:** new-candidate  
**Evidence:** E2 maintainer-repository issues with minimal reproductions and
automated repository triage; the triage comments are agent-authored and are not
independent corroboration.

Microsoft Agent Framework 1.14.0 shallow-copies workflow state across checkpoint
build and restore boundaries and returns objects from its in-memory checkpoint
store by reference. A reproduced issue shows that ordinary mutation of a list
in resumed state silently changes both the checkpoint object and the stored
snapshot. The reporter reproduced the behavior across Python 3.11, 3.12 and
3.13 on Windows and Linux, but those runs belong to one report.

Two adjacent open reports cover different 1.13.0 failure modes: parallel
functional steps can create sibling checkpoint roots and leave one checkpoint
unreachable from the latest lineage, while hosted workflow resume can reject
pending orchestration request types during restricted deserialization and fall
back to an older or incompatible checkpoint. The parallel-lineage report did
not demonstrate result loss or duplicate effects; that negative result must be
retained.

**Affected claims/cards:**

- `claim-runtime-side-effect-boundary`
- `claim-runtime-adoption-release-specific`
- `runtime.microsoft-agent-framework`
- `runtime.durable-checkpoint-ledger`
- `runtime.safety.transactional-effect-ledger`

**Candidate action:** add immutable-snapshot, storage-read isolation, concurrent
lineage and pending-request round-trip cases to the adoption gate. Treat current
checkpointing as prerelease-quality until fixed releases and independent
reproductions are available.

Sources:

- https://github.com/microsoft/agent-framework/releases/tag/python-1.14.0
- https://github.com/microsoft/agent-framework/issues/7683
- https://github.com/microsoft/agent-framework/issues/7647
- https://github.com/microsoft/agent-framework/issues/7618

## 3. Raw-log lexical search is candidate counterevidence to complex memory reads

**Classification:** new-candidate  
**Evidence:** E2 recent preprint with matched backbones, named baselines,
ablations and repeated LongMemEval runs; no public code or result artifact was
linked at check time.

ReFind leaves chat history unmodified, indexes raw turns lexically and gives an
agent bounded keyword search plus session rank fusion, local expansion, temporal
narrowing and seen-session filtering. The authors report mean accuracy 58.2
over roughly 2,800 MemoryAgentBench precise-retrieval and fact-tracking
questions using GPT-4o-mini, compared with 53.2 for the strongest reported
graph/tree baseline, HippoRAG 2, under a matched backbone. They report
LongMemEval-S/M accuracy of 93.2 plus or minus 3.3 and 89.3 plus or minus 6.0
over five runs with GPT-5-mini.

This does not contradict governed memory write, provenance, correction or
deletion requirements. It is counterevidence to promoting graph or tree memory
for precise conversational retrieval without first testing a raw immutable log
plus lexical, temporal and local-expansion controls.

**Affected claims/cards:**

- `claim-memory-framework-workload-fit`
- `claim-memory-type-aware-read`
- `claim-memory-retrieval-can-hurt`
- `memory.hybrid-read-router`
- `memory.episodic-event-log`
- `retrieval.bm25`

**Candidate action:** add ReFind-style raw-log search as a required memory
baseline, but do not adopt the reported ranking until code, prompts and outputs
are released and independently replayed.

Source: https://arxiv.org/abs/2608.12888

## 4. Memory serving cost has no universal break-even point

**Classification:** new-candidate  
**Evidence:** E2 recent controlled preprint with declared systems, baselines,
models, repeated grid cells and bootstrap confidence intervals; no public code
or cached-run artifact was linked at check time.

A cost study compares Mem0, Hindsight and Mastra Observational Memory with a
10-turn rolling window and full-history resubmission across two backbones,
conversations up to 400 turns and 665 LoCoMo questions. It reports that a model
based only on conversation length and message size misses memory-system serving
cost by 18–69 percent, that some systems never become cheaper than full history
within 400 turns, and that answer accuracy spans 21–54 percent in the evaluated
matrix. Backbone choice moves cost as much as the memory system.

The result fills a current operational evidence gap but remains limited to
three systems, two backbones, synthetic cost conversations and one answer
benchmark. It supports measuring ingest, retrieval, consolidation and answer
cost separately; it does not establish a universal cost ranking.

**Affected claims/cards:**

- `claim-memory-framework-workload-fit`
- `claim-memory-eval-full-lifecycle`
- `pattern-agent-memory-framework-selection`
- `pattern-agent-memory-evaluation-blueprint`

Source: https://arxiv.org/abs/2608.11879

## 5. ToolHazard adds executable long-horizon security environments

**Classification:** new-candidate  
**Evidence:** E2 recent preprint plus MIT-licensed code and benchmark data;
several scripts retain absolute experiment paths and the released requirements
do not include all SFT/RL dependencies, so full reproduction was not established.

ToolHazard synthesizes executable stateful environments, discovers reachable
injection points and verifies environment-side effects. The paper describes 87
long-horizon tasks across 28 environments and 512 tools, with mean 15.56 steps
and 18.75 candidate tools per task. Unlike stochastic tool simulation, the
released environments expose state-based checks. This is useful candidate
evidence for adaptive attacks and authoritative state oracles, but the generated
environment distribution and incomplete turn-key reproduction may bias both
attack success and benign utility.

**Affected claims/cards:**

- `claim-agent-security-paired-state-evals`
- `claim-eval-deterministic-before-judge`
- `evaluation.security.agent-benchmark-suite`
- `evaluation.security.adaptive-attack-replay`

Sources:

- https://arxiv.org/abs/2608.11878
- https://github.com/MurrayTom/ToolHazard

## 6. Graph-memory entity merge can carry attacker claims across users

**Classification:** new-candidate  
**Evidence:** E1/E2 public security report with a controlled but unpublished
proof of concept, plus a separate .NET port maintainer describing the same
unscoped-neighborhood failure and owner-scoped regression fixtures. The upstream
Neo4j Labs maintainers have not confirmed the issue publicly.

The report targets `neo4j-agent-memory` 0.5.0 in a shared graph deployment. An
ordinary user message reused trusted entity names; the resulting claims entered
the same entity neighborhood and were later retrieved for another user. A
separate implementation maintainer reports that per-query filters were
insufficient because some merge refresh paths operated outside caller scope;
central owner scoping across every read and write path closed the analogous
leak in that port.

This is direct support for source-bound provenance, pre-ranking tenant filters
and conflict representation. It is not yet independently reproducible from the
published upstream issue because the original proof-of-concept artifacts were
sent privately.

**Affected claims/cards:**

- `claim-memory-untrusted-write`
- `claim-memory-temporal-records`
- `claim-memory-type-aware-read`
- `memory.temporal-entity-graph`
- `memory.security.influence-gated-write`
- `retrieval.metadata.permission-filter`

Sources:

- https://github.com/neo4j-labs/agent-memory/issues/155
- https://github.com/joslat/agent-memory-dotnet

## 7. Cordis and DeepSeek Harness remain a watch-only runtime lead

**Classification:** research-lead, no promotion  
**Evidence:** E1 official repositories and an actively revised preprint; no
comparative evaluation or production case was reviewed.

DeepSeek Harness presents an agent runtime in which models, tools, sessions and
other runtime capabilities are plugins. It is built on Cordis, a meta-framework
for spatiotemporal composability. The Harness is explicitly a developer preview
with expected compatibility-breaking changes, the Cordis API is not stable, and
the paper is a preprint under active revision.

The mechanism may become relevant when a concrete case requires runtime
self-extension: creating, mounting, replacing or retiring capabilities while an
agent is running. It is not evidence of durable self-improvement. The reviewed
project material does not by itself establish persistent mutation, paired
evaluation, promotion gates or improved outcomes.

**Candidate action:** keep this item in the research radar only. Do not create a
Cordis source card, a DeepSeek Harness product card, a self-extension pattern or
an RSI synthesis. Reconsider promotion only when a concrete architecture case
requires runtime self-extension, or when multiple implementations and
operational evidence support a product-neutral comparison. Any future RSI link
still requires persistent candidates, external evaluation, canary promotion and
rollback.

Sources:

- https://github.com/deepseek-ai/deepseek-harness
- https://github.com/cordiverse/cordis
- https://github.com/cordiverse/paper

## Lane coverage and negative results

### RAG and retrieval

**Classification:** no-material-change

The new Sinhala/Tamil government-retrieval study is a useful 500-question,
1,699-context domain result, but it confirms the existing claim that embedding
selection is language- and workload-specific. The OpRAG preprint reports large
latency improvements for a resource-deterministic multi-stage runtime, but no
auditable implementation or experiment artifact was linked. Neither item
changes the current lexical/dense controls, measured fusion or end-to-end gate.

Affected claims/cards: `claim-embedding-benchmark-local`,
`claim-rag-end-to-end-property`, `claim-retrieval-controls-first`.

Sources:

- https://arxiv.org/abs/2608.12820
- https://arxiv.org/abs/2608.08340

### Evaluations and observability

**Classification:** no-material-change

OpenTelemetry Semantic Conventions 1.44.0 did not introduce a material agent
evaluation or trace-oracle contract in the inspected changes. ATOBench's paired
native/transformed episodes and source-linked verification chain agree with the
current process-aware evaluation pattern, but its public repository contained
only a one-line README, so it is not admitted as new evidence.

Affected claims/cards: `claim-agent-eval-multilayer`,
`claim-eval-deterministic-before-judge`.

Sources:

- https://github.com/open-telemetry/semantic-conventions/releases/tag/v1.44.0
- https://arxiv.org/abs/2608.12996
- https://github.com/daxtar2/ATOBench

### Bounded self-improvement

**Classification:** no-material-change

AQuA fixes data splits and evaluators while iterating quantitative-research
candidates, and SBCO reports a cheaper verifier-grounded harness optimizer than
a self-modifying baseline. Neither public paper linked code or run artifacts at
check time. AQuA's abstract does not establish that generation N becomes a
better optimizer for generation N+1 under equal search budget, while SBCO
co-learns verifier and harness surfaces. They remain bounded optimization
candidates and do not weaken the fixed-evaluator epoch, protected holdout,
paired comparison or rollback requirements.

Affected claims/cards: `claim-dgm-bounded-evidence`,
`claim-rsi-evaluator-epoch`, `claim-eval-protected-holdout`,
`rsi.fixed-evaluator-epoch`, `rsi.paired-promotion-gates`.

Sources:

- https://arxiv.org/abs/2608.12841
- https://arxiv.org/abs/2608.10157

## Unresolved evidence gaps

- Independent reproduction is missing for every newly reviewed security
  advisory in this page; repository advisories, GHSA mirrors, commits and
  release notes share upstream provenance.
- The Microsoft checkpoint reports need fixed-release verification and an
  effect-level replay showing whether snapshot corruption can cause duplicate,
  omitted or unauthorized external effects.
- ReFind and the memory-cost benchmark need code, prompts, cached inputs and
  raw outputs before their rankings or numeric break-even claims can be trusted.
- ToolHazard needs a clean-environment reproduction with pinned models and all
  training/evaluation dependencies.
- The graph-memory poisoning report needs public, upstream-versioned fixtures
  and maintainer confirmation.
