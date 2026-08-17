# Agentic Architect canonical projection

Canonical SHA-256: `caf7208e8f090042aed37cfbd1352e4431a4b9ed745a79a0f214698583d9210d`

This is a generated, one-way projection. The canonical source is `agentic-architecture-kb`;
edits here must never reverse-sync into the canonical repository.

## Agent Memory Consulting Regression Cases

Canonical ID: `case-agent-memory-consulting-regressions`  
Type: `case` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-systems-2026`, `source-agent-memory-evaluation-security-2026`

# Agent Memory Consulting Regression Cases

Each answer must state assumptions, minimum architecture, failure detection,
evaluation, rollout/rollback and alternatives.

1. Personal assistant: preferences change over years; private email is
   untrusted; user demands correction and deletion.
2. Tool agent: resume after crashes without replaying payments; remember local
   workflow constraints across sessions.
3. Enterprise multi-tenant support: shared product knowledge plus isolated
   customer histories and zero cross-tenant retrieval.
4. Coding agent: learn repository procedures while APIs, branches and tests
   change; reject stale or unsafe skills.
5. Healthcare-adjacent assistant: contested temporal facts, strict provenance,
   human approval and abstention.
6. Multi-agent research: agents share findings without allowing one poisoned
   source to become authoritative collective memory.
7. Existing vector-only memory: high recall but stale preferences, duplicates,
   no correction lineage and unverifiable deletes.
8. Graph proposal: determine whether temporal relationship queries justify
   extraction error, operational cost and deletion complexity.

Fail the consulting regression if the answer recommends a vendor before the
case, treats raw transcripts as canonical memory, omits write authority,
merges run state with durable facts, relies only on QA accuracy, or promises
deletion without lineage-aware verification.

## Bauhelfer AI RAG

Canonical ID: `case-bauhelfer-ki-rag`  
Type: `case` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-domescobar-bauhelfer-ki`

# Case: Bauhelfer AI RAG

## Evidence boundary

The implementation repository is private and not independently auditable from
this knowledge base. The architecture below is owner-reported. Treat it as an
E1 project snapshot: useful for hypothesizing eval slices, not as a measured
field outcome or a public default.

## Context

A German-language estimating assistant processes heterogeneous construction and
trade documents such as bills of quantities, price lists, office files, scans,
and photos. Its output is not unconstrained chat text, but an auditable, editable
offer draft with line items, quantities, prices, assumptions, and sources.

## Relevant constraints

- Exact IDs, item numbers, units, amounts, and pages matter more than semantic
  similarity alone.
- Tables, layout, and reading order carry meaning.
- Retrieval must strictly isolate organizations and projects.
- Misattributing content across customers or projects is a severe failure.
- Unknown values must remain explicit rather than being plausibly completed.
- A user approves the result before PDF generation or any external effect.

## Implemented pattern

```text
upload
 -> project/tenant scope
 -> Docling parsing
 -> Markdown + JSON + layout/table metadata
 -> structure-aware chunks + contextual header
 -> embeddings + German FTS
 -> dense top-40 + lexical top-40
 -> RRF(k=60)
 -> poison/overview filtering
 -> optional LLM reranking of top-30
 -> top-8 context
 -> typed evidence bundle
 -> structured offer/document snapshot
 -> blocking review issues
 -> human approval
```

Postgres stores application data, metadata, the full-text index, and pgvector
together. The embedding column has 1,536 dimensions; OpenAI and Gemini are
provider options, with truncated Gemini vectors normalized. The ingestion worker
processes embeddings in batches of 64.

## Strengths of this pattern

- Tenant and project filters are enforced inside dense and FTS SQL queries,
  before result selection.
- Structured chunks preserve page, heading path, and type.
- Contextual headers improve the self-description of isolated chunks.
- RRF combines semantic and exact matches without adding incompatible raw scores.
- Evidence bundles are validated against file IDs that actually belong to the
  project.
- Document snapshots freeze source revision and evidence; stale revisions and
  cross-project evidence are rejected.
- Missing or external evidence creates a review requirement instead of false
  confidence.

## Weaknesses and open risks

### Evaluation

The committed retrieval test set contains only one question. The harness scores
a source hit and reports the same value as both context precision and context
recall. This measures neither ranking quality nor genuine precision/recall.
Missing cases include hard negatives, table cells, OCR errors, cross-project
leakage, conflicting document versions, and temporal updates.

### Reranking

The optional LLM reranker sees only the first 500 characters of each chunk. For
tables or evidence appearing later, this can produce incorrect rankings. It
needs an offline baseline against RRF alone, latency and cost measurements, and
a fault-tolerant fallback.

### Heuristic poison filters

Known parser fallback text and multi-project summaries are removed through
German substring rules. This is understandable as an incident fix but fragile.
The more robust solution is typed ingestion status, origin, and scope metadata
that is filtered deterministically before retrieval.

### Index and provider migration

The embedding dimension is coupled to the database schema. Changes to model,
dimension, normalization, or chunker require an index manifest, parallel
rebuild, recall comparison, and atomic cutover.

### Repository hygiene

Upload and parsed-output directories must not appear in public source-control
history. Deleting them in the current commit does not remove them from Git
history. Required controls are secret/PII scanning, reviewed history cleanup,
storage outside the repository, and CI guards against recommitting the data.

## Recommended next evaluations

1. Use 10–20 representative project folders, sliced by PDF, scan, XLSX, and
   photo.
2. Create at least 100 retrieval questions with complete relevance labels, not
   merely one expected source.
3. Measure each stage: parse-field accuracy, Recall@k, nDCG@k, MRR, context
   precision, citation correctness, unsupported-claim rate, and line-item field
   accuracy.
4. Run ablations for FTS, dense, hybrid/RRF, and hybrid plus reranker.
5. Add a negative suite for tenant/project leakage, deleted files, poisoned
   chunks, stale versions, and missing prices.
6. Replay with cost and p50/p95 latency; protect reranking with a canary and
   feature flag.

## Reusable conclusion

Document-centric domain applications need a pipeline-wide architecture. Parsing
quality, scope filters, structured chunks, hybrid retrieval, evidence contracts,
and deterministic postconditions jointly determine quality. Vector-database
choice alone does not.

## Public AI Architect V1

Canonical ID: `case-public-ai-architect-v1`  
Type: `case` · Privacy: `internal` · Confidence: `0.91`  
Sources: `source-public-ai-architect-validation-2026-08`

# Case: Public AI Architect V1

## Context and constraints

A public, stateless architecture-advice chat serves a curated public wiki. It
must not connect to the privileged internal agent, private filesystem, shell or
tools. It runs in a hardened container and calls a bounded model API.

## Selected pattern

`browser → host TLS proxy → stateless bounded controller → structured public wiki v3 → model API`

The runtime decomposes each turn into checkable questions, retrieves candidate
sections and claims, assesses support, scope and gaps, and may execute one
targeted follow-up search. The draft streams to the browser, but only a final
answer that passes exact-citation, runtime-consistency, disclosure and diagram
schema gates is accepted. One bounded repair is allowed. The model has no tools;
sessions stay in the browser.

## Measured outcome

The structured public artifact contains 342 exact-addressable chunks, 24 public
claims, 31 relations and six navigation lanes. No private page was promoted to
expose the two canonical contradiction edges; contradiction traversal is tested
synthetically and will activate only when public-reviewed edges exist.

The deployed evidence-investigator runtime passed 23 deterministic unit,
contract, privacy and release tests. A real three-turn support-agent conversation
passed streaming, evidence-metadata, citation-resolution and context checks. A
second adversarial live run passed 9/9 turns across irreversible side effects,
prompt injection and deliberate evidence gaps; two turns used repair, no provider
retry occurred, and observed turn latency ranged from 22.2 to 75.5 seconds.

## Decision

The runtime no longer treats top-k retrieval as grounded truth: retrieved text is
candidate evidence, the model-assisted assessor must select exact IDs and retain
scope, limitations and missing support, and deterministic gates reject unresolved
labels or hidden evidence gaps. This improves investigation discipline but is not
a truth proof; semantic support and source independence still require evals.

## Next evidence

Expand the private promotion split with human claim-to-span support labels,
upstream-provenance independence checks, contradiction cases and calibrated
abstention scoring. Compare the v3 investigator against the former flat-RAG
baseline under paired quality, latency and cost slices.

## Claim Ledger Governance

Canonical ID: `concept-claim-ledger-governance`  
Type: `concept` · Privacy: `public` · Confidence: `0.94`  
Sources: `source-agent-evaluation-research-2026`

# Claim Ledger Governance

`claims/ledger.jsonl` is the machine-checkable registry for durable technical
claims. A claim points to the exact wiki section that states it, records its
kind, evidence level, source pages, scope, limitations, and a review date.

## Claim kinds

- `empirical`: a measured or observed property of a system, benchmark or
  workload. Promotion follows the evidence-level bar.
- `normative`: a design, governance or threat-model requirement. It may be
  accepted at E2 when the requirement is inspectable, but it does not inherit
  empirical authority from the citation apparatus.

## Promotion contract

- E1 remains a hypothesis and cannot be `accepted`, regardless of kind.
- Empirical E2 stays `provisional`; it may support a canary, not a default.
- Empirical E3 may be `accepted` as a bounded recommendation for matching
  workloads.
- Normative E2 may be `accepted` as a requirement, not as a performance result.
- E4 requires convergent or reproduced evidence under comparable conditions.
- Numeric claims still require denominator, metric, evaluation scope and source.
- `accepted` requires at least one source whose `auditability` is not `private`.
- Contradictions are bidirectional `contradicts` edges; both claims become
  `contested` or `superseded`. They are never silently removed.

## Mechanical guarantees

The linter rejects malformed claims, duplicate claim IDs, missing section IDs,
unknown or non-source pages, kind/level/status combinations that violate the
promotion contract, accepted claims backed only by private sources, and
one-sided contradiction edges. The compiled JSON contains the ledger so
retrieval and evaluation systems can expose provenance with answers.

## Evaluation Metric Catalog and Selection Rules

Canonical ID: `concept-evaluation-metric-catalog`  
Type: `concept` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-evaluation-consulting-research-2026`

# Evaluation Metric Catalog and Selection Rules

## Metric contract

Every metric declares: decision, unit, oracle, scale/direction, aggregation,
uncertainty, required sample, slices, threshold owner, cost, version and blind
spots. A number without this contract is telemetry, not a gate.

## Metric families

- **Task outcome:** exact state, acceptance tests, completion, human acceptance,
  abstention correctness.
- **Retrieval:** Recall@k, Precision@k, MRR, nDCG, evidence coverage, ACL leakage,
  stale retrieval and latency.
- **Grounded generation:** claim support precision, evidence completeness,
  citation correctness, contradiction and unsupported-claim rate.
- **Tool agents:** capability/argument correctness, side effects, forbidden and
  duplicate calls, recovery and terminal reason.
- **Coding agents:** tests, resolution, regression, forbidden files, diff scope,
  static analysis and reproducibility.
- **Memory:** write precision, recall, update, temporal validity, contradiction,
  privacy isolation and verified forgetting.
- **Conversation:** goal resolution, instruction retention, correction,
  escalation, consistency and turn efficiency.
- **Multimodal/voice:** correctness plus OCR/layout, transcription, temporal
  alignment, interruption and perceptual slices.
- **Operations:** p50/p95/p99 latency, cost per success, availability, retries,
  queue age and incidents.

## Selection rules

1. Choose one primary outcome tied to user value.
2. Add hard gates for safety, privacy, permissions and irreversible effects.
3. Add component metrics only for likely failure boundaries.
4. Keep latency and cost separate from correctness.
5. Report aggregate and decision-critical slices.
6. Pair every proxy with periodic outcome validation.
7. Report rates with denominators and confidence intervals.
8. Do not infer recall from source presence without a relevance set.
9. Do not infer correctness from citations or fluent prose alone.
10. Version semantics; threshold/rubric changes create a new lineage.

## Agent Memory Brownfield Audit and Greenfield Intake

Canonical ID: `pattern-agent-memory-consulting-intake`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-systems-2026`, `source-agent-memory-evaluation-security-2026`

# Agent Memory Brownfield Audit and Greenfield Intake

## Intake variables

Establish users/tenants, workloads, memory purpose, data classes, horizon,
freshness, acceptable false recall, correction authority, deletion SLA,
latency/cost budget, deployment, compliance, action risk and operating maturity.

## Brownfield audit

Trace representative memories from observation through write, update,
retrieval, use and deletion. Inventory stores, indexes, caches, graphs, traces,
backups, models, prompts, schemas and access boundaries. Reproduce stale facts,
conflicts, leaks, poison writes, failed deletes and crash recovery. Baseline
quality by lifecycle stage rather than relying on end-QA.

## Greenfield decision

Start with checkpointed run state, append-only events, versioned records and
FTS. Add semantic retrieval for demonstrated paraphrase recall; add a temporal
graph for relationship/time queries; add autonomous consolidation only with
provenance and promotion gates; add procedures only with executable validation.
The smallest design that passes workload and risk gates wins.

## Agent Memory Evaluation Blueprint

Canonical ID: `pattern-agent-memory-evaluation-blueprint`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.91`  
Sources: `source-agent-memory-evaluation-security-2026`, `source-memory-operational-baselines-and-tenancy-2026-08`

# Agent Memory Evaluation Blueprint

Evaluate `write -> maintain/update -> retrieve -> use/action -> delete` with
stage-level oracles and end-to-end outcomes.

## Minimum suite

- LoCoMo/LongMemEval for conversational recall and temporal updates.
- LongMemEval-V2 or Mem2ActBench for experienced workflows and actions.
- HaluMem-style cases to localize extraction and update errors.
- Private cases for project facts, preferences, conflicts and abstention.
- Adversarial poisoning, extraction, cross-tenant and internal-channel probes.
- Lineage-aware deletion and rebuild tests.
- An immutable raw-event-log BM25 control with temporal narrowing and bounded
  local expansion under the same model, prompt, context and reranking budgets.

## Metrics and gates

Write: extraction precision/recall, fabrication, unauthorized writes,
provenance completeness. Update: conflict recall, stale survival, current-value
accuracy. Retrieval: Recall/Precision@k, MRR/nDCG, distractors and abstention.
Use: task success, constraint grounding, exact tool arguments and side effects.
Operations: p50/p95 latency, storage, tokens and calls, with ingest, extraction,
retrieval, consolidation and answer cost metered separately. Report total cost
per correct answer and warm/cold behavior rather than query-serving cost alone.
Security: injection/activation, secret extraction and cross-tenant exposure.
Deletion: canonical/derived coverage, retrievability and rebuild consistency.

Use dev, selection, hidden holdout and red-team splits with corpus/config hashes.
Repeat stochastic runs and report confidence/flakiness. Zero cross-tenant leak,
zero forbidden side effect and complete required erasure are non-compensatory.

## Agent Memory Framework Selection

Canonical ID: `pattern-agent-memory-framework-selection`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.86`  
Sources: `source-agent-memory-systems-2026`

# Agent Memory Framework Selection

- LangGraph wins when recoverable tool execution, checkpoints, replay and HITL
  dominate. Build the memory lifecycle explicitly.
- Letta wins when the agent must actively manage a visible self/user memory and
  platform coupling is acceptable. Add admission controls for writes.
- Mem0 wins as an embeddable fact-extraction/retrieval service. Pin version and
  evaluate current ADD-only behavior and deletion lineage.
- Graphiti/Zep wins for temporal entity relationships and provenance. Test
  extraction quality, tenant namespaces and semantic erasure.
- Client-owned files win for minimal transparent memory. Add schema, ACL,
  search, versioning and backups.
- Provider conversation state wins only for conversation continuity; do not
  represent it as a complete memory architecture.

Score candidates against workload success, write correctness, update/conflict
semantics, recovery, deletion coverage, privacy, latency, cost, portability and
operational burden. Vendor benchmark deltas are hypotheses until reproduced
under identical models, budgets, corpus and evaluator.

## Agent Sandbox Selection and Validation

Canonical ID: `pattern-agent-sandbox-selection`  
Type: `pattern` · Privacy: `public` · Confidence: `0.89`  
Sources: `source-agentic-security-verification-2026-08`, `source-agentic-security-landscape-2026-08`

# Agent Sandbox Selection and Validation

## Selection rule

Choose the isolation boundary from the adversary and consequence, not startup
time. Hardened containers fit trusted single-tenant tools and build isolation.
User-controlled or model-generated code with secrets, multiple tenants or high-
impact access generally needs a stronger userspace-kernel or per-workload VM
boundary. Regulated deployments may require dedicated nodes or accounts in
addition to a microVM.

Kubernetes SIGs Agent Sandbox is a lifecycle abstraction, not one fixed security
boundary. OpenSandbox supports several runtime classes, including standard
containers, gVisor and Kata or Firecracker configurations. Azure Container Apps
dynamic sessions provide a managed Hyper-V-isolated option. These are candidates
whose exact version and configuration must pass the same application tests.

## Non-negotiable profile

- non-root execution, dropped capabilities and no host or container-runtime
  socket;
- explicit read-only and writable mounts with tenant-specific storage;
- no ambient cloud or developer credentials; broker narrowly scoped tokens;
- deny-by-default egress through an authenticated allowlist proxy;
- CPU, memory, process, disk, output, time and concurrent-session limits;
- immutable base image, signed provenance, vulnerability policy and bounded
  dependency installation;
- per-tenant identity, logs and lifecycle cleanup; no cross-session reuse unless
  explicitly scrubbed and tested;
- kill, revoke, snapshot-for-forensics and destroy operations controlled outside
  the guest.

Validate host escape, metadata and secret access, DNS and redirect egress,
symlink and mount traversal, fork and disk exhaustion, cross-tenant state,
snapshot restoration, cleanup failure and control-plane authorization. Product
claims of strong isolation are implementation evidence, not substitutes for
these tests.

## Agent Security Evaluation and Tooling

Canonical ID: `pattern-agent-security-evaluation-and-tooling`  
Type: `pattern` · Privacy: `public` · Confidence: `0.91`  
Sources: `source-agentic-security-verification-2026-08`

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

## Agentic and Corrective Retrieval

Canonical ID: `pattern-agentic-corrective-retrieval`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-rag-developments-2026-batch-1`

# Agentic and Corrective Retrieval

## Minimal adaptive controller

```text
classify query
 -> no retrieval | single retrieval | decomposed retrieval
 -> assess evidence sufficiency
 -> answer | rewrite/retry | alternate source | abstain/escalate
```

The controller owns budgets and state. Retrieval tools remain deterministic
services where possible.

## Distinct mechanisms

- **Adaptive/router RAG:** chooses pipeline complexity from query features.
- **CRAG:** evaluates retrieved evidence and triggers correction or web fallback.
- **Self-RAG:** a specially trained model emits reflection tokens to decide when
  to retrieve and critique evidence/output.
- **Agentic retrieval:** a runtime plans subqueries, calls sources iteratively,
  tracks coverage and stops under explicit criteria.

These names should not be collapsed into a generic “agent loop”.

## Winning conditions

- queries vary substantially in complexity and source needs;
- multi-source or multi-hop evidence is common;
- failed first retrieval can be detected with useful precision;
- added latency and token cost are justified by task value.

## Controls

- hard limits for iterations, subqueries, sources, tokens, time and spend;
- typed evidence ledger and coverage by sub-question;
- no-progress and duplicate-query detection;
- untrusted web/tool content remains data, never policy;
- external-source fallback respects privacy and authorization;
- abstention when the evaluator is uncertain;
- trace every rewrite, route, retrieval and stop decision.

## Evaluation

Compare against a fixed hybrid+rereanker baseline and slice simple versus
complex queries. Measure answer/evidence accuracy, correction precision,
unnecessary-retrieval rate, steps, latency, cost and failure recovery. A gain on
complex cases can still lose overall if the router overuses expensive paths.

## Agentic RAG Security Architecture

Canonical ID: `pattern-agentic-rag-security-architecture`  
Type: `pattern` · Privacy: `public` · Confidence: `0.9`  
Sources: `source-agentic-security-landscape-2026-08`

# Agentic RAG Security Architecture

## Combined threat boundary

Agentic RAG compounds risks because retrieved content can influence planning,
tool calls and durable memory. A poisoned document can become an instruction;
delegated authority can drift across retrieval and agent hops; a malicious
summary can persist after the original session; and retries can amplify one
compromised decision into cascading effects.

```text
identity + intent
      |
      v
bounded controller ---- budgets / kill switch / trace
      |
      v
authorization-first retrieval <---- governed corpus + provenance
      |
      v
untrusted evidence gate ---- injection / integrity / diversity signals
      |
      v
planner proposes action ---- no authority is inherited from evidence
      |
      v
policy gateway ---- approval if high risk ---- isolated tool executor
      |
      +---- effect receipt
      +---- quarantined memory candidate, never direct canonical write
```

## Decision rule

Break the combination of sensitive data, untrusted input and external action at
multiple independent boundaries. If all three are present, require strict
runtime isolation, current identity propagation, authorization-first retrieval,
deterministic tool policy, and human approval for high-impact effects. If the
system is read-only over a public curated corpus, a smaller bounded controller
can omit credentials, code execution and approval while retaining corpus
integrity, citation, injection and budget gates.

## Practical release checklist

1. Inventory and risk-classify agents, corpora, tools, identities and effects.
2. Threat-model every data and authority transition, including cache, memory,
   reranker, verifier and observability sinks.
3. Implement least privilege, short-lived delegation, source admission,
   authorization-first retrieval, isolated execution and deterministic policy.
4. Add multi-source verification where independent sources exist; otherwise
   make abstention and human escalation explicit.
5. Run OWASP-aligned adversarial traces plus corpus-specific poisoning,
   cross-tenant, MCP, sandbox, recovery and cascading-failure tests.
6. Canary with read-only or shadow execution, monitor policy decisions and
   anomalous retrieval, and rehearse kill, revoke, quarantine and rollback.

No deployment is promoted from checklist completion alone. The release record
must identify the tested versions, threat model, protected cases, deterministic
oracle results, residual probabilistic detection rates and unresolved risks.

## Agentic Runtime Security Boundary

Canonical ID: `pattern-agentic-runtime-security-boundary`  
Type: `pattern` · Privacy: `public` · Confidence: `0.9`  
Sources: `source-agentic-security-landscape-2026-08`

# Agentic Runtime Security Boundary

## Control-plane invariant

The model proposes; deterministic infrastructure authorizes and executes. A
prompt, model guardrail, verifier agent or behavior certificate may inform a
decision but cannot be the only enforcement point for data access, code
execution, privilege changes or irreversible effects.

```text
user + agent identity + delegated scope
                  |
untrusted input -> planner -> proposed action
                              |
                              v
                 deterministic policy gateway
                   | deny | approve | allow
                   v                  v
             audit + alert      isolated executor
                                      |
                           effect ledger + receipt
```

## Required layers

1. Inventory every agent, owner, model, tool, MCP server, data source, memory
   store and downstream effect. Version the inventory and expire unused agents.
2. Assign a unique agent identity and preserve the invoking user's delegation
   chain. Mint short-lived, task-scoped credentials after policy evaluation.
3. Allowlist tool operations and validate canonical arguments. Recheck current
   authority immediately before execution and commit.
4. Run generated code and risky parsers in an isolated, disposable environment
   with bounded CPU, memory, processes, storage, time and network egress.
5. Require an approval interrupt for irreversible, financial, external,
   privilege-changing or ambiguous actions. Bind approval to the exact action.
6. Keep append-only decision and effect records with redacted inputs, policy
   version, identity, causal operation ID and authoritative result.
7. Enforce step, token, cost, fan-out, delegation and wall-time limits outside
   the model. Provide a tested kill switch and credential revocation path.

## Trust and adoption gate

An open-source governance or sandbox project is a component candidate, not a
trusted system. Evaluate a pinned release for adapter completeness, default
policy, bypass paths, credential handling, isolation boundary, telemetry,
security response, migration and rollback. Compare it against a minimal custom
policy gateway on the same adversarial traces.

## Minimum security evaluations

- direct and indirect goal hijacking through users, documents, tool output,
  memory and peer-agent messages;
- unauthorized tool, parameter, resource and tenant access;
- stale delegation, approval replay and privilege escalation after resume;
- sandbox escape, secret access, egress bypass and resource exhaustion;
- MCP manifest drift, tool-name collision and dependency compromise;
- duplicate side effects, cascading retries, budget bypass and kill-switch
  response;
- audit gaps, log injection, trace correlation failure and incident replay.

Promotion requires zero deterministic authorization bypasses in the protected
suite. Detection rates for probabilistic scanners must be reported separately
with false positives and adaptive attacks.

## Bounded RAG Architecture Search

Canonical ID: `pattern-bounded-rag-architecture-search`  
Type: `pattern` · Privacy: `public` · Confidence: `0.84`  
Sources: `source-rag-architecture-search-2026`, `source-agent-evaluation-research-2026`

# Bounded RAG Architecture Search

## Search space

Represent the champion and candidates as typed manifests. Begin with reversible
query rewriting, filters, retrieval depth, fusion weights, reranking and context
packing. Parser, chunking and embedding changes form a later reindexing tier.
Every experiment changes one declared unit or uses a declared combinatorial
search budget.

## Architect loop

`baseline → sliced diagnosis → technique evidence → candidate manifest → isolated replay → paired comparison → promote/reject → archive`

The proposer sees aggregate development failures and allowed technique cards,
not hidden expected answers or promotion-gate details.

## Promotion rule

Optimizer rankings are task-dependent. Apply hard privacy/safety/citation gates,
then compare quality, latency and cost under the same data, seeds and budgets.
Repeat ambiguous comparisons. Promotion requires an untouched holdout,
immutable artifacts, canary, kill switch and rollback.

## Stopping

Stop on target attainment, exhausted budget, patience without improvement,
unstable judge agreement, repeated invalid patches or evaluator-integrity
failure. “Perfect on development” is not evidence of universal improvement.

## Chunking Baseline and Ablation

Canonical ID: `pattern-chunking-baseline-ablation`  
Type: `pattern` · Privacy: `public` · Confidence: `0.9`  
Sources: `source-chunking-evidence-2025-2026`

# Chunking Baseline and Ablation

## Decision rule

Start with two controls: fixed token windows and structure-aware sections with a
hard maximum size. Semantic, LLM-based, late or mixture chunking is promoted
only after paired application replay. No strategy is a universal default.

## Manifest

Version parser identity, boundary policy, target/min/max tokens, overlap,
contextual prefix, parent/neighbor expansion, embedding model, index identity
and retrieval depth. Chunk IDs must be stable for unchanged source elements.

## Eval matrix

Cross query granularity (fact, section, synthesis) with document shape (short,
long, table-heavy, hierarchical). Measure Recall@k, evidence coverage, context
precision, answer completeness, citation correctness, index size, ingestion
cost and latency. Score relevance against an invariant evidence view when the
candidate changes contextual prefixes.

## Failure interpretation

Missing evidence before chunking indicates a parser defect. Evidence retrieved
but omitted from context indicates packing/reranking. Evidence present but the
answer is wrong indicates generation or grounding. Do not tune chunk boundaries
to mask another stage's failure.

## Chunking Technique Catalog and Routing Matrix

Canonical ID: `pattern-chunking-technique-catalog`  
Type: `pattern` · Privacy: `public` · Confidence: `0.9`  
Sources: `source-chunking-landscape-2026-08`

# Chunking Technique Catalog and Routing Matrix

## Controls

- Fixed token windows provide a reproducible size baseline.
- Recursive splitting provides a cheap boundary-aware baseline.
- Sliding overlap tests whether boundary recall justifies duplicate index cost.

## Natural and document structure

- Sentence windows suit local claims whose neighbors disambiguate them.
- Paragraph or section-aware chunks preserve author structure with a size cap.
- Markdown title-chain chunks retain hierarchical location in technical content.
- Table-aware chunks preserve headers, rows and key-value relationships.
- AST chunks preserve functions, classes and sibling code nodes.
- Conversation chunks preserve complete turns, speakers and bounded episodes.

## Generated or contextual units

- Semantic splitting detects embedding-distance topic boundaries but is not a
  universal improvement over cheaper controls.
- Proposition chunking indexes atomic self-contained claims for fine fact lookup.
- Contextual prefixes add document-specific explanatory text before indexing.
- Late chunking embeds long context before pooling into chunk embeddings.

## Multi-granular retrieval

- Parent-child retrieval searches small units and returns their larger parent.
- Neighbor expansion retrieves a hit and bounded adjacent source units.
- Hierarchical summary trees support questions spanning multiple abstraction levels.
- Adaptive or mixture selection chooses granularity per document or query class.
- Tree navigation avoids a flat chunk index but still creates hierarchical nodes;
  “no chunking” must not be interpreted as no segmentation or summarization.

## Routing defaults

Start with fixed and structure-aware candidates. Use proposition units for atomic
fact questions, parent-child for fine matching plus broad answer context, AST for
code, table-aware for relational rows, turn-aware for conversations, and hierarchy
for synthesis across long documents. Promote prefixes, semantic, late, adaptive or
LLM-generated structures only when paired evaluation pays for their added cost and
failure surface.

## Contextual Retrieval

Canonical ID: `pattern-contextual-retrieval`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-rag-developments-2026-batch-1`

# Contextual Retrieval

## Mechanism

Generate a short prefix that situates a retrievable unit inside its parent
document, then index `prefix + unit` in both sparse and dense channels.

```text
document + target unit
 -> grounded context generator
 -> 50–100 token prefix
 -> lexical index + embedding index
 -> hybrid retrieval + optional reranker
```

The prefix should contain only retrieval-disambiguating context: document type,
section, subject, time/version and relationship to surrounding material. It must
not introduce facts absent from the document.

## Winning conditions

- repeated terms have different meanings across sections or documents;
- small units lose entity, time, product or policy context;
- corpus is indexed offline and the added indexing cost is amortized;
- both semantic and exact retrieval are useful.

## Failure modes

- LLM-generated context hallucinates or launders untrusted instructions;
- prefixes become repetitive and dominate BM25 or embeddings;
- changed parent documents leave stale prefixes;
- sensitive metadata is copied into less restricted indexes;
- larger context reduces precision or increases reranker truncation.

## Controls and evaluation

- derive prefix from the exact document version and store prompt/model/hash;
- label generated context separately from source text;
- cap length and reject unsupported entities, dates and numbers;
- rebuild on source or generator change;
- compare raw chunks, deterministic metadata headers and LLM contextualization;
- measure Recall@k, nDCG, downstream field accuracy, index cost and leakage.

Anthropic's reported 49% and 67% relative failure reductions are useful priors,
not deployment targets.

## Document-centric Hybrid RAG

Canonical ID: `pattern-document-centric-hybrid-rag`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-domescobar-bauhelfer-ki`, `source-rag-radar-2026-08`

# Document-centric Hybrid RAG

## Evidence boundary

The originating implementation is a private repository. Winning conditions and
pipeline shape below are a project-derived candidate. Lexical-plus-dense hybrid
retrieval is independently evidenced; the typed offer-output contract is not.
Do not treat this pattern as an accepted default until a public or otherwise
auditable paired evaluation exists.

## Winning conditions

This pattern fits when document structure and exact values are equally
important: offers, contracts, technical specifications, bills of quantities,
invoices, or regulatory documents.

## Architecture

### Ingestion

1. Store the original immutably and outside the code repository.
2. Set tenant, project, document type, and retention before parsing.
3. Extract layout, table, OCR, and page information.
4. Store parser output and parser/configuration versions.
5. Segment by heading, table, line item, or page; use fixed token windows only
   as a fallback.
6. Attach a stable ID, document version, page anchor, type, confidence, and
   compact context header to each chunk.
7. Build lexical and semantic indexes reproducibly.

### Retrieval

```text
intent/scope
 -> deterministic ACL + metadata filter
 -> dense retrieval || lexical retrieval
 -> RRF
 -> optional reranker
 -> diversity/coverage selection
 -> evidence pack with stable anchors
```

ACL and project filters must apply before ANN and ranking. RRF is a strong
default because it fuses ranks instead of uncalibrated scores. Top-k values are
dataset-specific parameters, not universal best practices.

### Generation

- Separate the evidence pack explicitly from the output schema.
- Link every domain claim and critical field to a source ID and page anchor.
- Model assumed, unknown, and contradictory as distinct states.
- Compute and validate calculable values deterministically.
- Require human approval before external or irreversible output.

## Do not use

- For small, fully structured datasets: direct SQL or API queries are simpler
  and more precise.
- For exact table aggregation: a parser plus structured database often
  outperforms text RAG.
- For one-off short documents: long context may be the cheaper baseline.

## Failure detection

- Parse goldens per document type
- Retrieval ablations and per-slice metrics
- Cross-scope canaries
- Citation and anchor validation
- Unsupported-claim and missing-field checks
- Index-manifest and deletion checks
- Latency, cost, and reranker fallback in the trace

## Embedding Selection and Migration

Canonical ID: `pattern-embedding-selection-migration`  
Type: `pattern` · Privacy: `public` · Confidence: `0.91`  
Sources: `source-embedding-evaluation-2025`

# Embedding Selection and Migration

## Selection rule

Shortlist from public benchmarks, select on private retrieval slices. Always
include BM25 and the current embedder. Compare dense-only and hybrid retrieval
under fixed chunking, candidate depth and reranking.

## Required slices

Languages, domain terms, identifiers, paraphrases, long passages, hard
negatives, freshness and unanswerable queries. Report Recall@k/nDCG by slice,
not only an aggregate mean, plus encoding throughput, query latency, index size,
licence and data-residency constraints.

## Migration

Build a new immutable index with model revision, dimension, normalization,
instruction template, tokenizer/truncation and source-manifest hashes. Shadow or
dual-read it. Promote only after paired replay and rollback rehearsal; never
rewrite the champion index in place.

## Drift

Re-run sentinel queries after model/provider revisions and on a schedule tied to
corpus and query-distribution change. A stable API name does not guarantee a
stable embedding space.

## Embedding Technique Catalog and Migration Routing

Canonical ID: `pattern-embedding-technique-catalog`  
Type: `pattern` · Privacy: `public` · Confidence: `0.92`  
Sources: `source-embedding-landscape-2026-08`

# Embedding Technique Catalog and Migration Routing

## Baselines and modes

- A general dense encoder is the semantic control; multilingual dense is required when query and corpus languages differ.
- Learned sparse retrieval preserves inspectable term dimensions and lexical expansion, but needs compatible sparse infrastructure.
- Dense-sparse hybrid retrieval protects both paraphrase and exact-identifier slices; fusion weights are evaluation parameters.
- Multi-vector late interaction preserves token-level evidence at higher index and scoring cost.

## Specialization

- Domain adaptation is justified only after a zero-shot model fails stable domain slices and trustworthy positives or carefully audited pseudo-labels exist.
- Long-input encoders prevent silent truncation but do not prove that embedding an entire document is better than structure-aware units.
- Matryoshka-compatible truncation reduces index bytes only for models explicitly trained or adapted for nested dimensions.
- Quantized indexes are a memory/latency candidate only after full-precision replay; preserve a rescoring path when ranking drift matters.
- Asymmetric encoders require a pinned query/passage instruction, tokenizer, pooling and normalization contract across every client.

## Migration contract

Every index manifest records model and tokenizer revisions, instructions, normalization, dimension, truncation, chunk manifest and source hashes. Re-embedding uses an immutable challenger index. Promotion requires coverage checks, paired replay, shadow or dual-read, latency/cost gates and alias rollback rehearsal.

## Default route

Start with BM25, incumbent dense and one strong multilingual dense challenger under fixed chunking. Add hybrid for identifier-heavy corpora, multi-vector for fine-grained matching, long-input only for measured truncation failures, and adaptation only after cheaper failures are localized.

## Eval-guided Bounded Improvement Loop

Canonical ID: `pattern-eval-guided-improvement-loop`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.87`  
Sources: `source-domescobar-eval-oigl`, `source-domescobar-agentic-eval-research`, `source-agent-evaluation-research-2026`

# Eval-guided Bounded Improvement Loop

## Control loop

```text
accepted baseline
 -> select failing development slices
 -> diagnose from bounded traces
 -> propose one typed mutation
 -> validate patch surface and policy
 -> development + regression evaluation
 -> candidate-selection comparison
 -> archive candidate and evidence
 -> independent full + confirmation on hidden promotion gates
 -> human acceptance
 -> canary
 -> promote or rollback
```

## Separate mutation modes

- **Prompt/config:** prompt text, routing thresholds, retrieval depth, model or
  tool policy within a typed schema.
- **Code patch:** application or agent scaffold files within an allowlist, with
  executable tests and forbidden evaluator/guardrail files.
- **Dataset:** never part of the same automatic optimization transaction;
  changes alter metric meaning and require review/versioning.

## Non-negotiable boundaries

- The optimizer cannot read hidden expected outputs or detailed holdout errors.
- Evaluator, policies, hidden tests and acceptance logic are read-only to the
  candidate patcher.
- Every candidate stores parent, diff, rationale, model/config identities,
  traces, scores, cost and terminal reason.
- Hard safety or privacy regressions reject regardless of aggregate gain.
- Compare against the same baseline, dataset and environment identity.
- Ambiguous deltas require repeated evidence; one successful replay is not an
  improvement.
- Promotion has a kill switch, bounded canary and automatic rollback trigger.

## Selection

Do not collapse all objectives into one score. First apply hard gates, then use
a declared ordering or Pareto frontier over quality, safety, latency and cost.
Report slice regressions even when the aggregate improves.

## Stopping conditions

- target quality reached without gate regression;
- budget exhausted;
- no improvement beyond epsilon for declared patience;
- variance or judge disagreement makes ranking unreliable;
- repeated invalid/reverted patches;
- policy violation or evaluator-integrity event.

## Fit

Use this loop only where the mutable surface is bounded and outcome evidence is
strong. It is unsuitable when correctness depends mainly on an uncalibrated
LLM judge, the environment cannot be reset, or hidden promotion data cannot be
protected.

## Evaluation Consulting Intake and Decision Process

Canonical ID: `pattern-evaluation-consulting-intake`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.91`  
Sources: `source-evaluation-consulting-research-2026`

# Evaluation Consulting Intake and Decision Process

## Intake

Establish user/decision/harm, workload and long tail, available deterministic
state, modalities and effects, provenance/freshness/privacy, current system and
traces, latency/cost/scale, obligations, incidents and team maturity before
recommending metrics or tools.

## Brownfield audit

1. Inventory prompts, models, tools, datasets, scorers, environments and gates.
2. Reproduce the last baseline from immutable identities.
3. Trace representative successes and failures end to end.
4. Validate cases, oracles and judges with known controls.
5. Check leakage, duplication, contamination and holdout access.
6. Separate system, evaluator, infrastructure and data failures.
7. Compare offline gates with production incidents and corrections.
8. Produce a risk-ranked gap register before proposing migration.

## Greenfield design

1. Define user outcome and unacceptable effects.
2. Build 20–50 reviewed seed cases across dominant/high-risk slices.
3. Implement deterministic outcome and safety gates first.
4. Add trace diagnostics only where actionable.
5. Add calibrated judges for residual semantic criteria.
6. Freeze identities, artifacts and split access.
7. Establish paired regression, confirmation and human acceptance.
8. Add shadow/canary telemetry and rollback before more autonomy.

## Deliverables

Evaluation Strategy, Dataset Card, metric/oracle registry, evaluator validation,
baseline scorecard, go-live gates, rollout/rollback, ownership and unresolved
evidence register.

## Statistical Decision Rules for Agent Evaluations

Canonical ID: `pattern-evaluation-statistical-decision-rules`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.89`  
Sources: `source-evaluation-consulting-research-2026`

# Statistical Decision Rules for Agent Evaluations

## Default comparison

- Pair candidate and baseline on the same cases, environment and evaluator.
- Predeclare primary metric, important effect, gates, slices, repetitions and
  stopping rule.
- For binary paired outcomes report wins/losses/ties and paired inference such
  as exact McNemar; bootstrap case-level deltas for complex metrics.
- Preserve hierarchy: repeated attempts within one case are not independent
  additional tasks.
- Report intervals, effect sizes and denominators; p-values are not effect size.

## Sample sizing and search

Size from baseline, smallest important delta, power/error tolerance and slice
needs; no universal minimum exists. Separate a primary decision from exploratory
metrics. Correct/control multiplicity when many variants or slices are searched.
Repeated holdout use turns it into selection data.

## Promotion rule

Promote only if hard gates pass, primary outcome meets its declared margin, no
critical slice exceeds regression tolerance, operational constraints hold, an
independent protected confirmation passes, and all identities match.

Sequential monitoring needs a declared confidence-sequence or alpha-spending
design. Repeatedly checking ordinary intervals until favorable inflates error.

## Evaluation Tool Selection

Canonical ID: `pattern-evaluation-tool-selection`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.85`  
Sources: `source-domescobar-eval-oigl`, `source-evaluation-consulting-research-2026`

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

## Evidence-first Agent Evaluation

Canonical ID: `pattern-evidence-first-agent-evaluation`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-domescobar-eval-oigl`, `source-agent-evaluation-research-2026`

# Evidence-first Agent Evaluation

## Core pattern

```text
versioned task + environment + policy
 -> repeated agent attempts
 -> final outcome + causal trace + environment state
 -> deterministic invariants and safety gates
 -> calibrated semantic/process judges only for residual ambiguity
 -> slice metrics + uncertainty + artifacts
 -> independent confirmation
 -> explicit acceptance or rejection
```

The unit of evidence is an attempt bound to task version, environment snapshot,
agent/runtime identity, judge identity, policy and evaluator hash.

## Evaluation layers

1. **Task validity:** Is the task real, solvable and unambiguous enough?
2. **Outcome validity:** Did the required external state or answer result?
3. **Safety invariants:** Were forbidden actions, permissions and side effects
   respected? These are hard gates.
4. **Causal grounding:** Can claims and observations be traced to valid calls,
   accessible evidence and the correct time/state?
5. **Process diagnostics:** Routing, retries, recovery, escalation and budgets.
   These explain failure but should not demand one exact successful path.
6. **Efficiency:** Calls, tokens, wall time and cost, reported as a vector or
   Pareto frontier rather than hidden in correctness.
7. **Robustness:** Repeat variance, perturbations, alternate environments and
   failure slices.

## Judge policy

- Use schema checks, database state, executable tests and causal IDs first.
- Use an LLM judge only for criteria that cannot be represented reliably as an
  executable oracle.
- Freeze rubric, prompt, model, decoding configuration and input projection.
- Calibrate each criterion against human labels and adversarial examples.
- Measure agreement, false positives/negatives and instability per slice.
- Abstain or escalate uncertain/disagreeing cases instead of forcing a score.
- An Agent-as-a-Judge may inspect the environment, but its acquired evidence
  and actions must themselves be recorded and evaluated.

## Dataset contract

- visible development set for iteration;
- candidate-selection set not used for mutation feedback;
- hidden holdout used sparingly for promotion;
- separate safety/redteam suite;
- immutable split manifests and content hashes;
- duplicate and semantic-near-duplicate checks across splits;
- case ownership, review record, provenance and expiry;
- production failure promotion goes to development first, not directly into a
  repeatedly exposed holdout.

## Required reports

- pass rate with confidence intervals and repeat distribution;
- results by task/risk/failure slice;
- hard-gate violations separately from quality scores;
- delta against the same baseline identity;
- cost/latency vector;
- judge calibration and disagreement;
- missing/invalid traces and infrastructure failures separated from agent
  failures.

## Failure modes

- **Goodharting:** candidate optimizes visible proxy; detect with hidden gates
  and counterfactual/adversarial cases.
- **Trace theater:** plausible trace without causal correspondence; bind calls,
  observations and state transitions through runtime-generated IDs.
- **Over-specified trajectory:** correct alternative path fails; assert causal
  invariants, not one golden chain unless compliance requires it.
- **Judge drift:** scores change after model/prompt update; hash and re-calibrate.
- **Flaky environment:** agent variance confused with infrastructure variance;
  snapshot/reset state and classify infra failures separately.
- **Contamination:** benchmark memorized or repeatedly exposed; use private and
  rotating holdouts plus fresh executable tasks.

## Generation-aware Context Efficiency

Canonical ID: `pattern-generation-aware-context-efficiency`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.82`  
Sources: `source-rag-developments-2026-batch-2`

# Generation-aware Context Efficiency

## Distinct optimization surfaces

- **Index compression:** reduce stored retrieval representations, as
  MarginMerge does for visual patch vectors.
- **Candidate utility:** select documents or document sets for downstream answer
  value, as in InfoGain-RAG and CORAG.
- **Context compression:** shorten or encode the evidence shown to the model.
- **Inference optimization:** reduce prefill/decoding work and KV-cache pressure,
  as in REFRAG.

These mechanisms are complementary but not interchangeable. Every optimization
must state which surface and metric it changes.

## Evaluation contract

Measure retrieval nDCG/Recall, evidence coverage, final grounded accuracy,
unsupported claims, stored bytes, index/query latency, time to first token,
throughput and total cost. Compare at equal evidence and answer-quality targets.

For learned utility scorers, test generator swaps and calibration drift. For
visual compression, retain hard slices with small text, tables, diagrams and
cross-page references. For runtime-specific decoding, require hardware-local
benchmarks and a fallback to the standard model serving path.

## Maturity rule

Do not make a days-old preprint or a custom decoding kernel the default path.
Run it as an optional projection or canary until independent or internal replay
confirms quality retention and operating benefit.

## Graph-based Retrieval

Canonical ID: `pattern-graph-based-retrieval`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.87`  
Sources: `source-rag-developments-2026-batch-1`

# Graph-based Retrieval

## Choose the graph for the query class

### Entity/relation graph

Extract entities, claims and relations; retrieve local neighborhoods. Useful for
explicit relationship and multi-hop questions. Main risk: extraction errors
become graph facts.

### Community-summary graph

Cluster the graph and summarize communities at multiple levels. Useful for
global questions such as themes, trends and corpus-wide comparison. Expensive to
index and refresh; summary loss can hide minority evidence.

### Co-occurrence/lazy graph

Build cheap noun-phrase/co-occurrence structure and defer interpretation to
query time. Reduces indexing cost but moves cost and latency into reads.

### Personalized PageRank memory graph

Seed a graph from query-linked entities/passages and diffuse relevance through
relationships. Useful for associative multi-hop retrieval; sensitive to graph
construction, edge weighting and seed quality.

## Default composition

```text
metadata/ACL filter
 -> sparse+dense candidate retrieval
 -> graph expansion only for relational/global query classes
 -> evidence-level rerank and coverage
 -> source passages, not graph summaries alone, feed generation
```

## Winning conditions

- questions repeatedly require relations across passages or corpus-wide themes;
- entities can be resolved with acceptable precision;
- update frequency allows graph maintenance;
- graph-specific evals beat strong hybrid and long-context baselines.

## Losing conditions

- exact lookup or single-passage QA dominates;
- corpus changes rapidly and graph invalidation is expensive;
- names/entities are ambiguous or extraction quality is weak;
- deletion, ACL propagation or provenance cannot be guaranteed.

## Required evaluation

Evaluate local factual, multi-hop, global thematic and negative-premise slices
separately. Measure extraction precision/recall, path validity, source coverage,
answer quality, indexing/update cost, query latency and deletion propagation.
LLM-judge comprehensiveness alone is insufficient.

## LLM Judge Calibration and Governance

Canonical ID: `pattern-llm-judge-calibration`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-agent-evaluation-research-2026`, `source-evaluation-consulting-research-2026`

# LLM Judge Calibration and Governance

## Admission test

Use labeled controls covering clear pass/fail, boundaries, adversarial prose,
missing evidence, contradictions and each critical slice. Measure confusion,
sensitivity/specificity, repeat agreement, calibration, position/order,
verbosity/style/self-preference, slice performance and escalation quality.
Aggregate correlation alone cannot expose rare catastrophic false passes.

## Runtime contract

Freeze model, provider, prompt, rubric, examples, decoding, input projection and
parser. Keep judge identity separate from the evaluated runtime. Blind model
identity and randomize pair order; test reversals rather than assuming they fix
bias.

## Policy and kill conditions

- deterministic gates override judge plausibility;
- use atomic criteria instead of one holistic score;
- rationales are diagnostics, not proof;
- uncertain/high-risk cases abstain or go to human adjudication;
- re-calibrate after any identity/semantic change and on production controls;
- disable promotion use when false-pass tolerance, slice coverage,
  reproducibility or parsing fails.

## MCP and Agent Extension Security

Canonical ID: `pattern-mcp-and-agent-extension-security`  
Type: `pattern` · Privacy: `public` · Confidence: `0.92`  
Sources: `source-agentic-security-verification-2026-08`

# MCP and Agent Extension Security

## Authority chain

```text
extension source -> admission -> pinned artifact + manifest
       -> user/client consent -> resource-bound identity
       -> strict tool contract -> deterministic policy
       -> isolated execution -> validated result -> audit
```

Project files, pull requests, skills, plugins, tool descriptions and one-click
MCP installation commands are untrusted until reviewed. Never auto-enable
project-supplied servers in a privileged CI or developer session. Display the
exact command, arguments, requested directories, network destinations and
scopes before consent; bind approval to the immutable artifact and manifest.

For protected remote MCP servers, validate issuer, audience and resource,
rotate short-lived tokens and never pass an inbound token through to an
upstream API. Sessions are correlation state, not authentication. Scope consent
per client and tool, reject unknown realms and fail closed on missing policy.

Tool schemas use strict types, enums, path roots, URL allowlists, byte and item
limits and explicit side-effect classification. Reject undeclared arguments,
traversal, shell interpolation and ambiguous free-form parameters. Treat tool
output as untrusted evidence and keep it unable to grant further authority.

## Supply-chain and operations gate

- pin immutable releases and transitive dependencies;
- require security policy, advisory monitoring and an upgrade owner;
- rescan manifest, code and dependencies on every change;
- isolate local servers from host secrets, broad filesystem and unrestricted
  egress;
- test SSRF, command injection, path traversal, serialization, session mix-up,
  confused deputy, prompt injection and malicious update paths;
- retain a fast disable/revoke path and previous known-good artifact.

Static or LLM-assisted scanners reduce review load but can miss encrypted,
multimodal, staged or environment-dependent behavior. A clean scan never grants
runtime authority by itself.

## Memory Conflict and Temporal Validity

Canonical ID: `pattern-memory-conflict-temporal-validity`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.89`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-systems-2026`

# Memory Conflict and Temporal Validity

Keep append-only evidence plus a reconstructable current view. Every mutable
claim carries event time, ingestion time, valid-from/to, source, status and a
supersession link. Never overwrite contradictory history silently.

Classify changes as duplicate, extension, correction, temporal transition or
unresolved contradiction. Source authority, freshness and corroboration inform
promotion but do not mechanically collapse contested claims. Measure conflict
detection precision/recall, stale-fact survival, latest-valid-value accuracy,
temporal interval accuracy and cascading invalidation completeness.

A temporal graph wins when relationship history and multi-hop temporal queries
are central. It is unnecessary overhead for simple stable preferences.

## Memory Poisoning Defense

Canonical ID: `pattern-memory-poisoning-defense`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-agent-memory-evaluation-security-2026`, `source-memory-operational-baselines-and-tenancy-2026-08`

# Memory Poisoning Defense

## Trust boundary

External content, tool output, messages, shared-agent memories and model
reflections are untrusted observations. They enter quarantine, not active
personal or procedural memory.

Use schema and allowlist checks, source authentication, tenant isolation,
write-rate limits, provenance, anomaly checks and human approval for sensitive
classes. At retrieval, screen both query and candidate, preserve trust labels
in context and prevent recalled text from acquiring system-level authority.

Red-team delayed triggers, indirect injection, conflicting updates, shared-
memory propagation and sleeper activation. Measure injection, retrieval and
activation success; persistence half-life; blast radius; defense false
positive/negative rates; and clean-utility loss. Kill promotion if forbidden
authority changes or cross-tenant exposure occur.

For shared graph memory, attach owner or tenant scope to nodes, edges, facts and
derived summaries. Exercise identical entity names across two owners and verify
every read, write, merge, refresh, consolidation, deletion and rebuild path.
Missing ownership metadata must fail closed; a query-time filter does not prove
that background graph maintenance preserves scope.

## Type-Aware Memory Read and Retrieval

Canonical ID: `pattern-memory-read-routing`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-evaluation-security-2026`, `source-memory-operational-baselines-and-tenancy-2026-08`

# Type-Aware Memory Read and Retrieval

## Read contract

1. Classify intent and required memory types.
2. Apply tenant, user, project, privacy, status and validity filters before
   lexical or semantic retrieval.
3. Load run state by exact identity; retrieve episodes by time plus lexical/
   semantic similarity; retrieve facts by hybrid search; use graph traversal
   only for relational questions; select procedures by verified preconditions.
4. Fuse/rerank candidates without discarding provenance or trust metadata.
5. Surface active contradictions and superseded values when relevant.
6. Load a bounded evidence packet, then log what was used and the outcome.

Evaluate retrieval separately from reading and action. Report Recall@k,
Precision@k, MRR/nDCG, abstention, distractor robustness, latency and cost.
Cross-tenant retrieval is a zero-tolerance gate.

Before promoting dense, graph, tree or learned memory retrieval, compare it
with the immutable raw event log searched by BM25 plus temporal narrowing and
bounded local expansion. Keep backbone, prompts, context and reranking budgets
equal and report exact-identifier, fact-tracking, multi-hop and event-order
slices separately.

## Controlled Memory Write and Promotion

Canonical ID: `pattern-memory-write-and-promotion`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.91`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-evaluation-security-2026`

# Controlled Memory Write and Promotion

## Pipeline

1. Record the immutable source event with actor, timestamp, scope and origin.
2. Qualify retention purpose, expected reuse, novelty, sensitivity and risk.
3. Extract a typed candidate: episode, claim, preference, relation or procedure.
4. Compare with active memory for duplicate, amendment, conflict, correction or
   temporal supersession.
5. Keep candidates quarantined until deterministic validation and required
   approval pass.
6. Promote with provenance, confidence, validity, privacy, retention and model/
   extractor identity.
7. Update rebuildable indexes; never make an index the only copy.

Untrusted documents, emails, tool output and other agents cannot directly
author authoritative preferences, permissions or procedures. High-risk writes
need human approval. Promotion metrics include extraction precision/recall,
fabrication rate, unauthorized-write rate and provenance completeness.

## Routed Multimodal Document Retrieval

Canonical ID: `pattern-multimodal-document-retrieval`  
Type: `pattern` · Privacy: `public` · Confidence: `0.88`  
Sources: `source-multimodal-document-retrieval-2025`, `source-document-parsing-evidence-2026`

# Routed Multimodal Document Retrieval

## Architecture boundary

Maintain text and visual candidate lanes behind the same ACL/version filter.
Route or fan out visual-heavy queries, fuse candidates, rerank, then assemble a
context package with exact page/region anchors. The visual lane supplements; it
does not silently replace text retrieval or provenance.

## Fit

Use for tables, diagrams, forms, slides, scanned pages and layout-dependent
questions. Prefer text-only retrieval for clean prose when it meets the evals at
lower cost.

## Evaluation

Slice by modality and compare text-only, OCR+text, visual-only and fused lanes.
Measure page and region recall, answer/citation correctness, index bytes per
page, ingestion/query latency and cost. Include visually similar negatives,
wrong-page citations and text-visible-but-layout-wrong cases.

## Failure controls

Preserve page images and parser output identities, cap visual candidate depth,
deduplicate text/visual hits, redact sensitive images, and fall back to exact
text extraction for quotations and numbers.

## Multimodal RAG Technique Catalog and Routing Matrix

Canonical ID: `pattern-multimodal-rag-technique-catalog`  
Type: `pattern` · Privacy: `public` · Confidence: `0.91`  
Sources: `source-multimodal-rag-landscape-2026-08`

# Multimodal RAG Technique Catalog and Routing Matrix

## Candidate lanes

- OCR and parsed text remain the cheap exact-text lane.
- Single-vector image embeddings are a compact visual baseline.
- Visual late interaction preserves patch-level evidence for layout-heavy pages at greater storage and scoring cost.
- OCR/text plus visual fusion hedges modality-specific failures but requires deduplication and calibrated fusion.

## Specialized structures

- Chart derendering maps plots to table-like data and should be fused with direct visual retrieval for complex charts.
- SQL-backed table retrieval preserves relational operations for multi-hop aggregation instead of flattening all rows into prose.
- Multimodal reranking spends a larger model only on a bounded candidate set.
- Region-anchored citation carries page, bounding box or cell coordinates into the answer contract.
- Layout-symbolic plus neural retrieval is a candidate for cross-page dependencies where graph construction can be inspected.
- Utility-oriented evidence selection reranks a bounded visual pool by downstream usefulness, not similarity alone.
- Hybrid single-/multi-vector retrieval uses a compact first stage and a fine-grained visual rescore.
- Interleaved representations are candidates for documents where text and visuals jointly define document-level relevance.

## Routing defaults

Use text-only retrieval for clean prose. Fan out to visual retrieval for layout, diagrams, slides and OCR uncertainty. Route chart questions to direct-image plus derendered-table lanes, and relational table questions to structured execution. All lanes share ACL/version filters and return stable page/region identities.

## Promotion gates

Compare text-only, OCR+text, visual-only and fused candidates by modality slice. Measure page and region recall, answer and citation correctness, exact-number accuracy, index bytes per page, ingestion throughput, p95 query latency and cost. A visual lane is not promoted from page-retrieval scores alone.

## Online Evaluation Canary and Rollback

Canonical ID: `pattern-online-evaluation-and-rollout`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-evaluation-consulting-research-2026`

# Online Evaluation, Canary and Rollback

## Rollout ladder

```text
offline replay -> no-effect shadow -> internal cohort
 -> bounded canary by risk/tenant -> staged expansion -> general availability
```

Each stage declares entry evidence, exposure/time budget, success metrics, hard
stops, owner and tested rollback.

## Telemetry and signals

Record release/run identity, workload slice, terminal reason, tool effects,
grounding, latency/cost, corrections and safety events. Apply purpose-bound
redaction/retention; do not log hidden reasoning or unrestricted content.

Use verified outcome/state, safety/privacy/permission violations, abstention,
escalation, retries, duplicate effects, corrections/undo/handover, SLOs and
distribution drift. Clicks, thumbs and conversation length are ambiguous
signals, not standalone correctness.

## Incident and rollback

Turn incidents into reviewed development/redteam cases, not an exposed hidden
holdout. Reproduce, patch, regress and canary again. Rollback restores model,
prompt, tools, retrieval and runtime as one compatible release identity, with
automatic hard-safety triggers and an accountable owner.

## PageIndex Reasoning Tree Retrieval

Canonical ID: `pattern-pageindex-reasoning-tree-retrieval`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.84`  
Sources: `source-vectifyai-pageindex`

# PageIndex / Reasoning Tree Retrieval

## Mechanism

```text
document
 -> parse pages and structure
 -> TOC/tree detection or generation
 -> align titles to physical pages
 -> summarize nodes
 -> persist versioned JSON tree

query
 -> inspect document/tree metadata
 -> reason over titles + summaries
 -> select nodes/page ranges
 -> fetch raw content
 -> answer/verify with page citations
```

This is **structure-guided agentic retrieval**. It changes the candidate
generation mechanism; it does not remove the need for parsing, context assembly,
generation, grounding checks or evaluation.

## Winning conditions

- one or a few long, strongly hierarchical documents;
- meaningful TOC, headings, numbered sections, appendices and cross-references;
- high value per query and tolerance for seconds rather than millisecond search;
- questions whose relevant evidence is structurally related but not lexically or
  semantically similar to the query;
- page-level traceability is more important than high throughput.

Typical candidates are financial filings, contracts, regulations, manuals and
technical reports.

## Losing conditions

- very large, heterogeneous multi-document corpora without a reliable document
  router;
- short, flat, noisy, scanned or weakly structured content;
- high-QPS autocomplete or interactive search with tight tail latency;
- queries dominated by exact identifiers, names or rare strings where lexical
  search is cheaper and deterministic;
- environments where document content may not be sent to the configured LLM.

## Recommended production composition

Do not choose “tree or vectors” globally. Use an adaptive front door:

```text
query classifier
  -> exact/entity query: metadata + BM25/FTS
  -> semantic cross-corpus query: dense + sparse + RRF
  -> structure/multi-hop query within selected long docs: PageIndex tree search
  -> union evidence -> rerank/coverage -> grounded generation
```

For multi-document use, first select candidate documents using metadata,
lexical/dense retrieval or a separately evaluated document tree. Then use
PageIndex inside only the selected documents. This bounds prompt size, cost and
latency.

## Required controls

- pin parser, prompt, model and tree-schema versions;
- store tree-build trace and validate page-range coverage;
- treat document text as untrusted evidence, never instructions;
- enforce maximum navigation steps, tokens, pages and cost;
- use cache keys derived from document hash and index configuration;
- fall back to lexical/dense retrieval when tree creation or navigation fails;
- keep tenant/ACL filtering outside and before agentic navigation;
- prevent model-generated node IDs from accessing unauthorized documents;
- verify final citations against fetched page ranges.

## Evaluation

Compare at least four paired systems on the same corpus and generator:

1. full/long context baseline where feasible;
2. BM25 or database FTS;
3. dense+sparse hybrid with RRF and optional reranking;
4. PageIndex tree retrieval;
5. adaptive router combining the preceding methods.

Measure retrieval Recall@k/nDCG, evidence coverage, answer field accuracy,
faithfulness, citation correctness, abstention, indexing cost, per-query cost,
p50/p95 latency and failure rate. Slice by document length, hierarchy quality,
scan/OCR quality, query type and corpus size.

## Parser Routing Matrix

Canonical ID: `pattern-parser-routing-matrix`  
Type: `pattern` · Privacy: `public` · Confidence: `0.87`  
Sources: `source-parser-landscape-2026-08`

# Parser Routing Matrix

## Practical shortlist by workload

- Clean born-digital PDF: PyMuPDF fast path; Docling Standard when hierarchy or
  tables matter.
- Broad mixed file archive: Apache Tika for detection/metadata/text, then route
  difficult PDFs to Docling, MinerU, Marker, PaddleOCR or a managed parser.
- Office-heavy local archive: AnyDoc for fast consistent Markdown; MarkItDown
  when Python plugins or multimodal extensions are useful; Xberg when broad
  bindings, OCR backends or code intelligence justify its larger surface.
- Geometry-sensitive machine-generated PDFs: pdfplumber when characters, ruling
  lines, rectangles and visually debugged table settings are needed.
- Scientific papers with equations: Marker, MinerU, Docling VLM, PaddleOCR-VL or
  olmOCR; evaluate formula and multi-column slices directly.
- Multilingual scans and historical documents: PaddleOCR, MinerU or a managed
  OCR service; validate each script and handwriting slice.
- Forms, invoices and signatures: Azure Document Intelligence, Google Document
  AI or Textract when their typed fields reduce application code; compare with a
  generic layout parser plus deterministic extraction.
- Charts and visually encoded values: LlamaParse agentic/chart modes or a VLM
  parser, with chart datapoint and attribution tests.
- Strict on-premise/privacy: native/local cards only; remote VLM presets and
  managed APIs are ineligible unless a separately approved deployment exists.

## Router signals

Use MIME type, text-layer coverage, scan probability, layout complexity, table/
formula/chart detectors, language, page count, confidentiality and latency tier.
Low-confidence output escalates to the next tier; it is not silently accepted.

## Promotion

The router and each parser version are part of the candidate manifest. Promote
on sliced downstream outcomes, not visual inspection alone. Preserve failed and
fallback routes in traces so coverage gains cannot hide cost or defect shifts.

## Parser Selection and Ingestion Contract

Canonical ID: `pattern-parser-selection-contract`  
Type: `pattern` · Privacy: `public` · Confidence: `0.88`  
Sources: `source-document-parsing-evidence-2026`

# Parser Selection and Ingestion Contract

## Selection rule

Choose parsers by document-slice and downstream task. Keep native text parsing
as the latency/cost control, then add layout OCR or a VLM parser only for slices
where paired replay shows a material outcome gain.

## Typed output contract

Each parsed element carries document/version/page identity, element type,
reading order, hierarchy path, bounding box when available, raw text, normalized
text, parser/model/config identity and confidence/failure flags. Tables, formulas
and figures remain typed objects rather than flattened prose.

## Evaluation

- field and character fidelity where deterministic labels exist;
- reading-order and hierarchy accuracy;
- table cell/record fidelity and cross-page continuity;
- formula, caption, footnote and figure retention;
- downstream evidence Recall@k and citation-anchor validity;
- latency, cost, failure rate and manual-review load by slice.

## Rollout

Shadow-index the candidate parser, dual-read a stable query set, and retain the
old parse/index until promotion. Kill on missing pages, ACL/provenance loss,
silent truncation or a hard downstream regression.

## Parser Technique Catalog

Canonical ID: `pattern-parser-technique-catalog`  
Type: `pattern` · Privacy: `public` · Confidence: `0.87`  
Sources: `source-parser-landscape-2026-08`

# Parser Technique Catalog

The machine-readable cards under `techniques/parsers/` are the experiment
contract. This page makes the same catalog retrievable for architecture advice.
No entry is a universal winner; each must pass the private corpus slices.

## Native fast paths

- **PyMuPDF:** born-digital PDFs, bounding boxes, fast local extraction. Escalate
  scans, broken fonts, complex columns and layout-dependent tables.
- **Apache Tika:** broad format detection, metadata and text normalization. Use
  it as a front door and router, not as the final high-fidelity PDF parser.
- **AnyDoc:** fast local normalization of office, OpenDocument, EPUB, CSV, RTF
  and text PDFs to consistent Markdown. Route image-only PDFs to OCR.
- **pdfplumber:** detailed character and vector geometry plus debuggable table
  extraction for machine-generated PDFs; unsuitable as a scan parser.

## Local modular pipelines

- **Docling Standard:** mixed PDFs needing OCR, layout, tables and provenance;
  strong default when local inspectability matters.
- **MinerU:** scientific, multilingual and formula-heavy documents; validate its
  licence and each language/document slice.
- **Marker:** local PDF-to-Markdown with optional OCR and LLM escalation; gate
  unsupported content when LLM assistance is enabled.
- **PaddleOCR PP-StructureV3:** multilingual modular OCR plus layout, tables,
  formulas and charts; useful when stages must be replaceable or trainable.
- **Unstructured:** multi-format partitioning with fast, hi-res and OCR routing;
  convenient integration, but table and reading-order quality remain empirical.
- **Microsoft MarkItDown:** lightweight multi-format-to-Markdown integration with
  optional OCR, vision and Azure routes; sandbox untrusted file and URI inputs.
- **Xberg:** broad polyglot extraction framework with OCR/VLM plugins and code
  intelligence; evaluate each backend and review Elastic License 2.0.

## Local visual-language parsers

- **Docling VLM:** hard visual layouts while retaining Docling structure.
- **olmOCR:** difficult scans, handwriting, equations and complex reading order
  with GPU batch capacity.
- **PaddleOCR-VL:** multilingual and historical documents combining tables,
  formulas and charts in an end-to-end visual path.

These routes require explicit unsupported-content checks. Fluent structured
output is not proof that every emitted token or relationship exists on page.

## Managed document AI

- **LlamaParse:** agentic and chart-focused modes for irregular documents.
- **Mistral OCR:** ordered blocks, tables, images and coordinates with low local
  operational overhead.
- **Azure Document Intelligence:** enterprise layouts and typed invoice, receipt
  or custom-form extraction in Azure environments.
- **Google Document AI Layout Parser:** layout-aware parsing and optional RAG
  chunks in Google Cloud; verify endpoint residency and independently evaluate
  generated chunk boundaries.
- **Amazon Textract:** AWS forms, tables, queries, handwriting and signatures;
  not the default for scientific formulas or chart interpretation.

## Minimum routing policy

Start with PyMuPDF for clean born-digital pages. Escalate to a local structured
pipeline when text coverage, reading-order confidence or detected structure
falls below a calibrated threshold. Use a VLM or managed specialist only for
hard slices it demonstrably improves. Store route, parser version, render
settings, confidence signals and fallback history in parse provenance.

## Project-Specific Coding Agent Harness

Canonical ID: `pattern-project-coding-agent-harness`  
Type: `pattern` · Privacy: `public` · Confidence: `0.87`  
Sources: `source-coding-agent-harness-and-skills-evidence-2026-08`, `source-agentic-security-verification-2026-08`, `source-agent-evaluation-research-2026`

# Project-Specific Coding Agent Harness

## Fit

Use this pattern when a team wants coding agents to work reliably inside a
specific repository. The output is not a universal dotfiles bundle. It is the
smallest evidence-backed instruction, capability and verification stack that
fits the repository's tasks and risks.

Do not claim project-specific fit without inspecting the repository or a
complete, verified project manifest. Current product documentation supplies
candidate mechanisms; project evidence and evals decide which ones belong.

## Required case facts

Collect before recommending a setup:

1. Repository topology, languages, package boundaries and generated code.
2. Canonical setup, build, test, lint, type-check and security commands.
3. Typical agent tasks and their acceptance conditions.
4. Protected files, secrets, production paths and external systems.
5. Local, CI and cloud execution environments.
6. Required coding-agent products and exact versions or release channels.
7. Latency, token, compute and human-review budgets.
8. Existing failure evidence: rejected patches, review comments, CI failures,
   incidents and repeated corrections.

Unknown facts stay unknown. Do not fill them with framework conventions or
model guesses.

Also capture the current harness as a versioned manifest: model and release,
instruction and skill digests, tool schemas, hooks, sandbox and network policy,
container or environment image, dependency lock, memory state and evaluator
version. Without this, later comparisons cannot attribute an outcome.

## Minimal architecture

```text
task goal + done condition
  -> verified project facts and applicable scoped instructions
  -> one coding agent in an isolated branch or worktree
  -> least-privilege files, commands, network and credentials
  -> edit with complete trace and diff
  -> deterministic local checks
  -> independent review for residual semantic risk
  -> accept, repair within budget, or revert
```

Begin with one agent, one workspace and existing repository commands. Skills,
hooks, MCP servers, subagents, persistent memory and durable orchestration are
optional additions, not baseline requirements.

## Put each concern on the smallest correct surface

| Concern | Default surface | Do not use as substitute |
| --- | --- | --- |
| Current task, scope and done condition | Prompt or task record | Permanent repository rule |
| Stable project layout, commands and conventions | Root `AGENTS.md` or supported project instructions | Repeated prompt |
| Package-specific commands or constraints | Nested or path-scoped instructions | One huge root file |
| Reusable multi-step procedure | Focused Agent Skill | Always-loaded project prose |
| Mechanical invariant | Existing test, linter, policy gate, hook or CI | Prompt reminder |
| Live external data or action | Narrow tool or MCP server | Copied stale documentation |
| Separate exploration or specialist context | Bounded subagent | Default multi-agent fan-out |
| Filesystem and execution authority | Sandbox and capability policy | Skill frontmatter or persona |
| Cross-session operational fact | Governed project documentation or memory | Unreviewed chat summary |

Product-specific files belong in thin adapters. Keep the underlying project
facts and acceptance criteria vendor-neutral so a new agent can reproduce the
same decisions.

## Instruction contract

Repository instructions should contain only facts that apply broadly and are
expensive for an agent to rediscover:

- authoritative commands and their working directories;
- important package and ownership boundaries;
- canonical examples to imitate;
- explicit protected paths and prohibited effects;
- what must be tested for each change class;
- PR and review expectations;
- an observable definition of done.

Prefer concise, verifiable statements. Point to authoritative files instead of
copying long style guides. Remove rules already enforced by formatters or CI.
Use nested scope for monorepos and test the actual discovery and precedence
behavior in every supported agent surface.

Do not add a repository overview merely because a product recommends one.
Current studies disagree on efficiency and find no general correctness gain.
Every always-loaded section consumes budget and can conflict with closer facts.
Prefer non-standard commands, boundaries, routing hints and repeated correction
evidence; measure the candidate against the current file and no customization.

Give each retained rule an observable compliance opportunity. Include
against-default cases so coincidental model behavior is not miscounted as
instruction following. Keep each rule on one canonical surface and test
conflicts across system, project, task, tool and skill instructions; do not
assume prompt depth alone determines precedence.

## Tool and retrieval contract

Tool architecture is part of the evaluated harness, not a neutral transport.
Expose bounded search, view, edit, diff and test operations with explicit
inputs, outputs, side effects and failure modes. Preserve a sandboxed compound
execution path when it reduces repeated-call overhead. Avoid overlapping tools
without a selection rule and do not add a scratchpad unless the controller uses
its state for routing, recovery or verification.

Evaluate retrieval together with delivery. Compare lexical, semantic and
hybrid search plus inline and file-based results where applicable. Measure
whether retrieved evidence is actually opened and incorporated into a verified
artifact; a high retrieval score alone does not establish agent utility.

## Skill admission contract

Create a project skill only after a workflow has repeated or repository
evidence shows that the agent lacks a specific method. Each admitted skill must
declare:

- the user goal and should-trigger conditions;
- should-not-trigger boundaries;
- required inputs and project prerequisites;
- ordered procedure and default tools;
- output artifact and success conditions;
- facts it must not invent;
- stop, ask, decline and escalation conditions;
- references or scripts and exactly when to load or run them;
- compatible products, versions and required authority;
- eval cases and a rollback target.

Use the portable Agent Skills fields and directory structure for the common
core. Keep product-only frontmatter, dynamic shell injection, invocation
controls and discovery paths in documented adapters. Treat `allowed-tools` as
host-specific and experimental unless the target runtime proves enforcement.

Third-party skills enter through an admission gate, not a copy command. Pin the
source commit and content digest, inspect instructions, scripts, references and
assets together, enumerate tools, credentials, egress and write scope, and
rerun admission whenever content or authority changes. Registry presence,
stars and repeated copies do not establish safety or quality.

Current empirical evidence is distribution-dependent: curated focused skills
can produce large gains, while many public SWE skills produce no gain and some
regress because guidance is stale or mismatched. Admit one narrow candidate at
a time and retain it only when project replays justify its context and tool
cost.

## Enforcement and authority

Instructions and skills influence model behavior but do not create a security
boundary. Enforce limits independently:

- default-deny write, network and external-action capabilities;
- workspace or ephemeral worktree isolation;
- no reusable secrets in model-visible files or environment state;
- short-lived, audience-bound credentials from a broker when required;
- protected-file and command policy before execution;
- deterministic tests and schemas before model-based review;
- immutable logs for commands, tool calls, diffs and approvals;
- explicit stop budget and kill switch.

Repository-local skills, hooks, MCP configuration and scripts from an
untrusted branch remain quarantined until their exact artifact digest and
requested authority are reviewed. Approval of a repository does not imply
approval of later mutable commits.

## Project-specific eval suite

Maintain three related eval layers.

### 1. Instruction and discovery checks

- active instruction files and precedence match expectation;
- path-scoped rules activate only for matching files;
- critical instructions survive the actual local, IDE, CI and cloud surfaces;
- conflicting and stale instructions fail a lint or review gate.

### 2. Skill checks

- should-trigger recall and should-not-trigger precision;
- incomplete input causes a question or safe stop;
- required artifacts and assertions pass;
- deterministic scripts handle mechanical checks;
- with-skill performance beats no-skill or the prior version;
- token, latency and tool-call overhead remain within budget.

### 3. End-to-end coding tasks

- representative bugs, features, refactors and review tasks from the project;
- clean-environment setup and dependency restoration;
- correct patch, regression checks and minimal diff;
- unauthorized action and secret-access sentinels;
- recovery from failed commands, partial edits and context compaction;
- human review of unanticipated quality and maintainability failures.
- rule-level compliance, including rules that oppose the model's baseline;
- execution alignment between claims, tool results and workspace state;
- trajectory-level permission, information-flow and side-effect checks.

Run from a pinned clean image and repository commit with a fresh session. Audit
all model-visible channels for reference patches, holdout metadata and cached
answers. Pin model, harness, dependencies, network and evaluator versions;
repeat stochastic conditions; report task slices and confidence rather than a
single aggregate pass rate. A test pass is insufficient if the patch took an
unauthorized action or exploited a weak oracle.

Keep protected tasks outside the authoring loop. A change is promoted only
when paired runs show no material regression and every safety sentinel passes.

## Bounded harness improvement loop

Treat harness tuning as an experiment, not accumulated prompt folklore:

1. Diagnose a repeated failure from traces and authoritative outcomes.
2. Select one bounded editable component and preserve a rollback digest.
3. State the predicted task slice, metric and expected direction before edit.
4. Replay baseline and candidate under the same pinned environment.
5. Inspect task-level outcomes, side effects, cost and trajectory evidence.
6. Replicate ambiguous improvements and reject unexplained regressions.
7. Canary the winner; never let the candidate mutate protected tasks, graders,
   promotion rules, budgets or rollback state.

Automatic harness evolution is research-stage evidence. The reusable pattern
is observability plus bounded attribution, not autonomous promotion.

## Long-horizon state and project memory

For multi-session or dependency-rich work, externalize completed units,
remaining units, prerequisites, current failure classification, regression
obligations, checkpointed workspace state and next action. Previously passing
units remain live obligations after compaction, restart or delegation. Retry
only after classifying the failure and changing relevant evidence or state.

Persistent project memory is optional. Add it only when measured rediscovery or
repeated-failure costs justify ongoing maintenance. Prefer append-only dated
events as the source of truth and deterministic summaries as disposable views.
Scope facts to repository and subsystem, preserve superseded history, attach
source locators and revalidation triggers, and begin pre-action warnings as
advisory rather than hard policy.

## Anti-slop gate

Reject a proposed harness when any of these hold:

- it cites no repository facts or authoritative current sources;
- it invents files, commands, services or organizational constraints;
- it adds agents, memory, MCP or orchestration without a measured deficit;
- it duplicates deterministic CI behavior as prose;
- it places security requirements only in prompts or skills;
- it mixes product-specific configuration into a supposedly portable core;
- it provides many options without a selected default and winning conditions;
- it has no baseline, eval tasks, failure budget or rollback path;
- it changes model, tools, instructions and environment together and still
  attributes the result to one component;
- its eval can access reference patches, holdout metadata or mutable caches;
- it treats copied, popular or registry-listed skills as trusted dependencies;
- it infers rule compliance from final task success rather than rule-level
  execution evidence;
- it evaluates retrieval without testing delivery and evidence use;
- it stores long-horizon state only in a growing conversation transcript;
- its completion claims disagree with the workspace, tool results or required
  artifacts;
- exact product guidance has no version and freshness date.

## Rollout

1. Record the current workflow and baseline task results.
2. Add or correct project instructions only.
3. Evaluate and retain only instructions that reduce observed errors.
4. Add one skill for one repeated workflow and compare paired fresh-context
   runs.
5. Add deterministic enforcement only for an identified invariant.
6. Add external tools or subagents only after a remaining eval deficit
   justifies their authority and operational cost.
7. Canary with reviewable changes, preserve the previous configuration and
   roll back on quality, security, latency or cost regression.

## Alternatives and winning conditions

- **Prompt only:** one-off, low-risk work with no durable project convention.
- **Instructions only:** ordinary repository work where existing commands and
  CI already cover the workflow.
- **Instructions plus one or two skills:** repeated project procedures with
  demonstrated baseline improvement.
- **Opinionated coding harness:** long-horizon work requiring several evaluated
  capabilities together.
- **Custom controller:** narrow regulated or high-authority workflow needing an
  auditable loop and exact policy state.

## Confidence and freshness

Confidence is high in the layered separation and eval requirements, moderate
in cross-product portability, and low for any untested product-specific path or
frontmatter. Evidence on the average effect of `AGENTS.md` and skills is
contested across task distributions; project-level paired replays decide.
Recheck named-product documentation before implementation and review this
pattern monthly while coding-agent customization surfaces are changing rapidly.

## RAG Security and Retrieval Governance

Canonical ID: `pattern-rag-security-and-retrieval-governance`  
Type: `pattern` · Privacy: `public` · Confidence: `0.91`  
Sources: `source-agentic-security-landscape-2026-08`

# RAG Security and Retrieval Governance

## Security pipeline

```text
source admission -> quarantine -> parse in sandbox -> classify + ACL + lineage
       -> immutable version/hash -> embed/index -> authorization-first retrieval
       -> injection and anomaly signals -> independent-source corroboration
       -> bounded untrusted context -> cited answer -> output policy -> audit
```

Authorization must run before or inside candidate generation. Post-retrieval
filtering can already disclose forbidden content to caches, logs, rerankers or
the model. Tenant, user, document, field, purpose, jurisdiction, time and
version scopes must travel with every candidate and parent or neighbor
expansion. Missing or stale ACL metadata fails closed.

## Ingestion and index controls

- Admit only authenticated connectors and attributed sources. Quarantine new,
  changed, user-uploaded and externally synchronized content until policy and
  malware or hidden-content checks complete.
- Parse untrusted files without host credentials or unrestricted network and
  filesystem access. Preserve the original blob, parser version, extracted
  structure, hashes and transformations.
- Separate trust domains and tenants physically or with independently tested
  logical controls. Encrypt source objects, indexes, caches and transport.
- Monitor index membership, source hashes, ACL drift, unusual embedding
  distributions, targeted query dominance and deletion propagation.
- Treat embeddings as sensitive derived data. Test extraction and inversion
  risk; do not assume vectors anonymize their source.

## Retrieval and context controls

- Propagate user and agent identity into retrieval. Apply deny-by-default ACL,
  privacy, retention and version predicates before scoring.
- Label retrieved content as untrusted evidence, delimit it from instructions
  and cap chunks, tokens, source concentration and recursion.
- Use multi-source verification only across independently governed provenance
  domains. Require source diversity or abstain for consequential claims; two
  chunks derived from one compromised source count as one source.
- Use injection classifiers, LLM verification prompts and anomaly detectors as
  defense signals. They can quarantine or escalate but cannot grant access or
  authorize tools.
- Bind citations to exact retrieved source versions and validate that claims
  are supported. If retrieval, ACL, integrity or citation validation fails,
  abstain or return a scoped error rather than silently fall back to model-only
  generation.

## Required evaluations

- poisoned documents, hidden text, conflicting sources and targeted retriever
  manipulation;
- cross-tenant, revoked-access, stale-cache, parent-expansion and metadata-
  missing leakage;
- embedding inversion and index-exfiltration probes appropriate to the data;
- indirect prompt injection that attempts tool use, memory writes or source
  suppression;
- source-diversity spoofing and correlated upstream compromise;
- deletion through source, chunks, embeddings, indexes, caches and traces;
- citation entailment, unsupported synthesis, PII and secret output leakage;
- fail-closed behavior for unavailable policy, integrity and verification
  services.

## Retrieval, Reranking, and Context Assembly Technique Catalog

Canonical ID: `pattern-retrieval-context-technique-catalog`  
Type: `pattern` · Privacy: `public` · Confidence: `0.9`  
Sources: `source-retrieval-context-landscape-2026-08`

# Retrieval, Reranking, and Context Assembly Technique Catalog

## Baseline ladder

1. Apply authorization and hard metadata predicates before ranking.
2. Measure BM25 and dense retrieval independently under the same candidate depth.
3. Add deterministic hybrid fusion only for complementary failure slices.
4. Tune retrieve-k, rerank-k and final-k from Recall@k and context-precision curves.
5. Rerank only when relevant evidence is found but ordered too low.
6. Select or compress evidence only when context noise or budget is the bottleneck.
7. Bind citations to stable source spans and abstain on calibrated missing evidence.
8. Route rewriting, decomposition, multi-query or iterative retrieval to queries
   that justify their extra calls and drift surface.

## Query routing

- Exact identifiers, versions, names and quoted text: BM25 first.
- Paraphrases and vocabulary mismatch: dense retrieval candidate.
- Mixed exact and conceptual workload: BM25 plus dense with RRF candidate.
- Conversational follow-up: intent-preserving standalone-query rewrite.
- Heterogeneous repeated workload: a logged sparse/dense/hybrid router only after oracle-route and confusion-matrix evaluation.
- Multi-facet request: bounded multi-query only if unique evidence yield improves.
- Multi-hop request: dependency-preserving decomposition or iterative retrieval.
- Direct lookup: no agent loop; keep one retrieval call as the control.

## Reranking and context routing

- Adequate Recall@k but poor rank: cross-encoder over a bounded candidate set.
- Redundant top results: MMR or coverage selection, sliced by query type.
- Long passages with local textual evidence: extractive sentence selection with
  adjacency and provenance.
- Context exceeds budget: evidence-preserving compression with an uncompressed
  fallback for high-risk or layout-dependent evidence.
- Missing evidence: bounded abstention or approved alternate source, never silent
  fallback to parametric memory where provenance is required.
- Every sourced answer: claim-to-span citation binding and post-generation checks.
- Long contexts: position-aware packing with deduplication and contradiction retention, not blind relevance concatenation.

## Diagnostic order

If required evidence is absent from the candidate pool, fix parsing, indexing,
filters, query transformation or first-stage retrieval. If it is present but ranks
low, inspect fusion and reranking. If it ranks high but is omitted from the prompt,
inspect diversity, compression and packing. If it is in the prompt but the answer
is unsupported, inspect generation, attribution and abstention. This ordering stops
downstream techniques from masking upstream defects.

## Promotion contract

Use paired replay with immutable corpus, relevance labels and permission sentinels.
Promote one bounded surface at a time. Require intended-slice gains without
regressions in exact identifiers, negative questions, citation attribution,
latency, cost or ACL leakage. Keep the previous manifest as rollback and log query
rewrites, fused ranks, reranker scores, selected spans, stop reasons and citations.

## Recursive Self-Improvement Evidence Boundary

Canonical ID: `pattern-rsi-evidence-boundary`  
Type: `pattern` · Privacy: `public` · Confidence: `0.81`  
Sources: `source-bounded-self-improvement-2025-2026`

# Recursive Self-Improvement Evidence Boundary

## What is demonstrated

DGM is evidence that an archived population of coding-agent variants can modify
its agent implementation and discover variants that score better on the tested
coding benchmarks. This is genuine self-referential agent improvement within a
bounded domain and evaluator.

## What is not demonstrated

It does not prove domain-general RSI, indefinite improvement, safe objective
evolution, autonomous production deployment, or that a better task agent is
also a better future optimizer. Prompt/config optimization alone is not RSI.

## Required RSI test

Generation N must produce a statistically supported improvement on untouched
tasks. Then, under equal search budget and information, generation N must also
produce better N+1 candidates than its predecessor. Evaluator and task-set
identity remain fixed during that comparison.

## Evaluator evolution

Changing the objective invalidates direct before/after claims. If utility must
evolve, use explicit epochs: freeze evaluation within each epoch, audit old/new
objective compatibility at the boundary, retain old sentinels and require human
approval. Treat recent co-evolving-evaluator research as experimental only.

## Agent Runtime Build Versus Adopt Decision

Canonical ID: `pattern-runtime-build-vs-adopt`  
Type: `pattern` · Privacy: `public` · Confidence: `0.86`  
Sources: `source-agent-runtime-framework-landscape-2026-08`, `source-runtime-techniques-2026-08`

# Agent Runtime Build Versus Adopt Decision

## Decision rule

Do not begin with a framework name. Select the smallest implementation tier
that satisfies the workload's state, recovery, authority, isolation and
operational requirements. A GitHub project is a candidate dependency, not a
trusted runtime, until its pinned version passes the application's own contract.

## Implementation tiers

1. **Custom minimal loop:** one agent, typed tools, hard step and cost limits,
   explicit stop conditions and a complete trace. Prefer this for narrow,
   short-lived, low-authority work where the complete control loop remains small
   enough to audit.
2. **Agent SDK:** adopt tool schemas, streaming, sessions, guardrails and
   tracing while retaining application-owned control and hosting. OpenAI Agents
   SDK, Pydantic AI and Google ADK are candidates with different ecosystem and
   typing trade-offs.
3. **Graph runtime:** use explicit nodes, state, checkpoints and interrupts when
   branching, pause/resume or inspectable workflow state justifies the graph.
   LangGraph is the principal reviewed candidate.
4. **Opinionated harness:** use Deep Agents or DeerFlow when long-horizon work,
   workspaces, subagents, skills and context management would otherwise be
   rebuilt. Remove or disable unused capabilities.
5. **Operational agent platform:** use OpenClaw when channels, persistent
   sessions, gateway policy, plugins, skills and multi-agent operations are part
   of the product boundary.
6. **Durable workflow substrate:** add Temporal or a comparable durable engine
   when runs must survive restarts, long waits, timers and distributed workers.
   This can wrap an SDK or harness; it is not a replacement for tool policy.

## Practical shortlist

- **Narrow embedded service:** custom minimal loop or OpenAI Agents SDK.
- **Typed Python application with provider choice:** Pydantic AI; add a durable
  integration only when recovery requirements justify it.
- **Explicit state machine and approval resume:** LangGraph.
- **Long-horizon repository or research worker:** Deep Agents, with an actual
  sandbox and least-privilege tools.
- **Full research/coding super-agent with gateway and channels:** DeerFlow,
  after a migration and sandbox review.
- **Persistent multi-channel personal or team agent host:** OpenClaw.
- **Google-centered agent application:** Google ADK.
- **Microsoft/Azure-centered workflows:** Microsoft Agent Framework, while
  preview surfaces remain behind an upgrade gate.
- **Days-long or failure-sensitive business process:** agent library plus
  Temporal or another evaluated durable workflow engine.

## When custom wins

Custom is rational when the action space is small, the run is short, state is
easy to serialize, side effects are absent or separately controlled, and a team
can own tests and on-call responsibility. It avoids hidden defaults, dependency
churn and abstraction leakage.

Custom stops being the lazy option when the team begins rebuilding checkpoint
migrations, streaming backpressure, approval suspension, cancellation,
concurrency control, context compaction, sandbox lifecycle, trace propagation,
provider normalization and recovery. At that point, framework adoption usually
reduces undifferentiated work.

## When adoption wins

Adopt when the required mechanism already exists, is testable through a narrow
adapter and its operational model matches the application. Prefer composition:
keep domain state, tool policy, effect identity and evals outside the framework
so a replacement remains possible.

Do not adopt a full harness merely to obtain one utility. A framework that saves
initial code can increase the permanent permission surface, upgrade load and
debugging distance.

## Trust and adoption gate

Score the exact release, not the project name, on:

- license and redistribution fit;
- signed or reproducible release provenance and pinned dependency graph;
- security policy, advisory history and response path;
- maintenance cadence, review depth and bus-factor exposure;
- stable state schema, checkpoint migration and rollback compatibility;
- documented authority, sandbox, network and filesystem boundaries;
- telemetry defaults, secret handling, data egress and tenant isolation;
- cancellation, retry, duplicate-effect and crash-recovery behavior;
- trace export, deterministic replay hooks and error transparency;
- adapter escape hatch and cost of replacing the dependency.

Repository popularity is only a discovery signal. Organization reputation and
recent commits do not replace this gate.

## Minimum comparative spike

Compare the smallest custom baseline with no more than two shortlisted
candidates on the same versioned cases. Include normal success, tool timeout,
model timeout, process crash after tool execution, duplicate delivery,
approval wait, cancellation, context overflow and dependency upgrade.

Measure task success, unsupported-action rate, duplicate-effect rate, recovery
time, human interventions, p50/p95 latency, tokens, tool calls, trace
completeness, cold-start and operator effort. The candidate wins only when the
measured benefit justifies its new operational and supply-chain surface.

## Adoption sequence

1. Pin a release and record its transitive lockfile and configuration.
2. Place it behind an application-owned runtime adapter.
3. Start with read-only tools and a disposable sandbox.
4. Run contract, failure-injection, security and cost evaluations.
5. Canary one workload slice with a kill switch and rollback artifact.
6. Promote capabilities separately; do not enable shell, network, memory and
   subagents as one bundle.
7. Re-run the gate for upgrades that change state, tools, sandbox or telemetry.

## Non-negotiable boundary

No reviewed framework eliminates the need for explicit effect identity,
authorization at execution or resume time, idempotency or compensation,
reconciliation, budgets, tenant boundaries and application-specific evals.

## Runtime Decision Guide

Canonical ID: `pattern-runtime-decision-guide`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.85`  
Sources: `source-domescobar-agentic-runtime-techniques`, `source-agent-runtime-framework-landscape-2026-08`

# Runtime Decision Guide

## Select by dominant requirement

- Short tool task: action loop, stopper, and error handling.
- Multi-stage task: plan-and-execute with typed task state.
- Objectively verifiable result: verifier loop; deterministic checks first.
- Open-ended research: research loop, claim/evidence ledger, and gap analysis.
- Code change: coding harness, isolation, tests, and rollback.
- Background work: durable workflow, queue, checkpoints, and idempotency.
- Risky external action: approval interrupt, audit, and edit/reject path.
- Multiple specialists: supervisor or planner/executor only when roles require
  separate context, tools, authority, or measurable parallelism.
- Recurring sessions: controlled memory promotion and forgetting.
- Difficult reasoning task: test-time compute only with a budget and verifier.

## Decision questions

1. What objective done condition exists?
2. Can a step have an external, financial, or irreversible effect?
3. Must the run survive process failure?
4. Which states must be exactly replayable?
5. Are steps idempotent; if not, what compensation exists?
6. Do roles need separate context, tools, or permissions?
7. What are the maximum time, cost, tool-call, depth, and fan-out budgets?
8. What is the kill switch, and how is the system rolled back?
9. Which offline replays and online signals demonstrate improvement?

## Select the implementation tier

- Use a custom minimal loop when the complete runtime is narrow, short-lived,
  auditable and low-authority.
- Use an SDK when tools, sessions, streaming, guardrails or tracing are required
  but application code should own hosting and policy.
- Use a graph runtime when explicit branching, checkpoints and approval resume
  are material requirements.
- Use an opinionated harness when workspaces, subagents, skills and long-context
  management are all required and evaluated together.
- Use an operational platform when gateways, channels, persistent sessions and
  plugin operations are inside the product boundary.
- Add a durable workflow substrate for long waits, distributed recovery and
  process restarts; do not confuse checkpointing with external-effect safety.

Apply the full release-specific trust and comparative-spike contract in
[[runtime-build-vs-adopt]].

## Default

Start with one agent, one primary loop, typed state, deterministic checks, hard
budgets, and a complete trace. Add orchestration only when a concrete evaluation
deficit justifies the additional complexity.

## Runtime Safety Baseline

Canonical ID: `pattern-runtime-safety-baseline`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.85`  
Sources: `source-domescobar-agentic-runtime-techniques`

# Runtime Safety Baseline

This baseline applies regardless of the selected agent framework.

## Before the run

- Record the original intent immutably.
- Determine user, project, and privacy scope.
- Label context as trusted instruction, trusted data, or untrusted evidence.
- Issue minimal, time-limited capabilities.
- Set budgets for time, tokens, cost, calls, delegation depth, and fan-out.

## During the run

Separate conversational checkpoints from external side effects. Non-idempotent
effects need runtime-generated causal IDs, commit-time authority checks, and a
transactional or reconcilable effect ledger; replaying chat state is
insufficient.

- Record every state transition and tool attempt in an append-only log.
- Validate tool arguments against schema and policy.
- Recheck proposed actions against the original intent and trust zone.
- Protect side effects with idempotency keys or saga/compensation semantics.
- Enforce no-progress, repetition, and budget breakers.
- Use a resumable approval interrupt before risky or irreversible actions.

## After the run

- Let a verifier decide against explicit acceptance criteria.
- Include referenced inputs/outputs, tool results, cost, state transitions, and
  provenance in the run receipt.
- Redact secrets and private content according to policy.
- Write memory lessons only as inbox candidates.
- Test recovery, replay, and rollback paths regularly.

## Minimum evaluations

- Prompt injection through tool output, web pages, and memory
- Capability escalation and cross-project access
- Duplicate delivery and crash between side effect and checkpoint
- Infinite loops, no progress, and budget overruns
- Faulty verifier and false completion report
- Replay after schema or state migration
- Deletion of a memory entry across all projections

## Scaling RAG Baselines

Canonical ID: `pattern-scaling-rag-baselines`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-rag-developments-2026-batch-2`

# Scaling RAG Baselines

## Pattern

Scale the candidate generator before scaling the agent. Keep an inverted index
as a cheap, inspectable control and expose retrieval to agents through bounded
search/read tools instead of unconstrained corpus browsing.

Baseline ladder:

1. ACL and metadata filters plus BM25;
2. BM25 plus dense retrieval and deterministic fusion;
3. reranking and evidence-budget optimization;
4. bounded query decomposition or an Agent+Search controller;
5. graph, visual or learned retrieval only for measured failure slices.

## Why it wins

Lexical retrieval scales without generative construction and is unusually
strong for identifiers, names and domain terminology. Agents are more useful as
query planners and evidence readers when a scalable search primitive narrows the
space. This keeps latency, cost and failure attribution observable.

## Failure modes and detection

- Vocabulary mismatch: compare against dense/hybrid Recall@k by query slice.
- Agent query drift: log query rewrites, read paths and stop reasons.
- Corpus growth regression: replay the same questions over nested corpus tiers.
- Graph construction wall: record indexed coverage, tokens per source token and
  freshness lag, not just quality on the completed subset.
- Answer gains that do not follow retrieval gains: evaluate evidence coverage
  and grounded answer accuracy separately.

## Rollout

Canary new retrieval paths behind a router. Preserve the lexical baseline,
per-query budgets and a kill switch. Promote only when paired replay shows gains
on the intended slice without unacceptable latency, cost or leakage regressions.

## Verifiable Memory Forgetting and Erasure

Canonical ID: `pattern-verifiable-memory-forgetting`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.92`  
Sources: `source-agent-memory-systems-2026`, `source-agent-memory-evaluation-security-2026`

# Verifiable Memory Forgetting and Erasure

Distinguish expiry, retrieval decay, supersession, archival and privacy/legal
erasure. Time decay alone is not forgetting: old facts can remain true and new
facts can be false.

## Erasure protocol

1. Tombstone and synchronously exclude the target from all reads.
2. Resolve lineage across raw events, claims, summaries, embeddings, graph
   nodes/edges, caches, traces and linked procedures.
3. Delete or redact canonical artifacts according to authority and retention.
4. Cascade deletion through derived stores or rebuild them from allowed data.
5. Probe exact text, paraphrases, semantic neighbors, graph neighborhoods and
   cross-session queries.
6. Issue a receipt with scope, artifacts, failures, completion time and backup
   expiry. Retry incomplete cascades.

Measure primary and derived deletion coverage, post-delete retrievability,
inference leakage, deletion latency and rebuild consistency. API success alone
is not evidence of forgetting.

## Verified Procedural and Skill Memory

Canonical ID: `pattern-verified-procedural-memory`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-evaluation-security-2026`

# Verified Procedural and Skill Memory

A procedure is executable capability, not a prose fact. Store purpose,
preconditions, postconditions, tool/API versions, permissions, dependencies,
known failures, producing traces, test results, owner and expiry.

Candidates come from successful trajectories but are admitted only after
isolated replay, forbidden-side-effect checks, regression comparison and human
approval where risk warrants. Selection requires task fit and satisfied
preconditions. Execute with least privilege, budget and kill switch. Record the
actual outcome and demote on drift or repeated failure.

Promotion uses development/selection/hidden holdout; canary before broad use;
rollback restores the accepted procedure. A successful historical trajectory
does not prove transfer to a changed environment.

## Visual Late-interaction Retrieval

Canonical ID: `pattern-visual-late-interaction-retrieval`  
Type: `pattern` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-rag-developments-2026-batch-1`

# Visual Late-interaction Retrieval

## Mechanism

Render each document page as an image, encode it into multiple visual-language
vectors and score a text query against page tokens/patches via late interaction.
ColPali is the canonical example.

```text
page image -> VLM multi-vector index
query text -> query vectors
late interaction -> ranked pages
selected page image/text -> extraction + generation
```

## Winning conditions

- layout, tables, figures, fonts or spatial relationships carry meaning;
- OCR order and text flattening destroy useful structure;
- page-level retrieval is an acceptable first-stage granularity;
- GPU/storage budget supports multi-vector indexing and search.

## Limitations

- finding the page is not extracting a precise cell or calculating an answer;
- page-level candidates can be too broad for long dense pages;
- multi-vector storage and late interaction can be expensive at corpus scale;
- accessibility, redaction and deterministic text search still need OCR/text;
- visual prompt injection and hidden content remain security concerns;
- citations require stable document/page identity and preferably extracted spans.

## Recommended composition

Use visual retrieval as another recall channel, not a replacement for every
representation:

```text
metadata filter
 -> visual page retrieval || OCR/BM25 || dense text retrieval
 -> fusion/reranking
 -> targeted text/table extraction from selected pages
 -> structured, cited generation
```

Evaluate on layout-heavy and OCR-hard slices using page Recall@k, downstream
field/table accuracy, citation correctness, storage, indexing throughput and
p95 query latency.

## Agent Evaluation Research August 2026

Canonical ID: `source-agent-evaluation-research-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.88`  
Sources: none

# Agent Evaluation Research — August 2026

Current primary sources, reviewed on 2026-08-09:

- Agentic Benchmark Checklist:
  https://arxiv.org/abs/2507.02825
- AgentRewardBench:
  https://arxiv.org/abs/2504.08942
- AJ-Bench / Agent-as-a-Judge:
  https://arxiv.org/abs/2604.18240
- TRACE / cross-step trajectory monitoring:
  https://arxiv.org/abs/2606.07054
- GroundEval / deterministische stateful evaluation:
  https://arxiv.org/abs/2606.22737
- GEPA / reflective prompt evolution:
  https://arxiv.org/abs/2507.19457
- SWE-bench Live:
  https://arxiv.org/abs/2505.23419
- SWE-bench Illusion:
  https://arxiv.org/abs/2506.12286

## Evidence audit

### Benchmark validity — E4 direction, E3 measurements

The Agentic Benchmark Checklist identifies concrete errors in task setup and
reward design that can materially distort rankings. The generalizable conclusion
is not a particular percentage: evaluators and tasks themselves require tests,
adversarial negatives, and validity checks.

### Trajectory judges — E3, workload-bound

AgentRewardBench compares automated evaluators against expert-labeled web-agent
trajectories. AJ-Bench extends the judge with active environment interaction.
Both support calibration against human or deterministic references; neither
demonstrates a universal judge.

### Long-horizon evidence — E2–E3, new

TRACE accumulates evidence across distant steps instead of judging only local
windows or final output. This is relevant to sabotage and long causal chains,
but the evidence comes from ten SHADE-Arena domains and is not yet a general
production standard.

### Deterministic stateful evaluation — E2, strong pattern

GroundEval checks search, fetch, access, and temporal paths against state truth.
The pattern fits agentic systems with controlled environments. The publication
is very recent, and its case studies do not replace independent replication.

### Evaluation-guided optimization — E3 within tested tasks

GEPA uses trajectories and textual reflection to evolve prompt variants through
Pareto selection. Its reported sample efficiency applies to the tested tasks.
Safe self-improvement still requires holdouts, immutable gates, patch
boundaries, canaries, and rollback.

### Contamination resistance — converging E3 evidence

SWE-bench Illusion finds indications of memorization and artifact exploitation.
SWE-bench Live uses newer executable repository tasks. Public static benchmarks
are therefore development baselines, not sufficient final evidence of
generalizable coding-agent capability.

## Agent Memory Evaluation Security and Privacy 2026

Canonical ID: `source-agent-memory-evaluation-security-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.87`  
Sources: none

# Agent Memory Evaluation, Security and Privacy — August 2026

Primary sources:

- LongMemEval (ICLR 2025): https://openreview.net/forum?id=wIonk5yTDq
- LongMemEval-V2: https://github.com/xiaowu0162/LongMemEval-V2
- LoCoMo (ACL 2024): https://aclanthology.org/2024.acl-long.747/
- MemBench (ACL Findings 2025): https://aclanthology.org/2025.findings-acl.989/
- Mem2ActBench (ACL 2026): https://aclanthology.org/2026.acl-long.370/
- MemoryArena: https://arxiv.org/abs/2602.16313
- HaluMem: https://arxiv.org/abs/2511.03506
- WorldMemArena: https://arxiv.org/abs/2605.29341
- Agent Security Bench: https://openreview.net/forum?id=V4y0CpX4hK
- Memory poisoning study: https://arxiv.org/abs/2606.04329
- GhostWriter: https://arxiv.org/abs/2607.06595
- MEXTRA: https://aclanthology.org/2025.acl-long.1227/
- AgentLeak: https://arxiv.org/abs/2602.11510

## Evidence audit

LoCoMo and LongMemEval are useful conversational recall baselines but do not
fully test whether an agent recognizes when memory is needed, performs the
right action or avoids side effects. LongMemEval-V2, Mem2ActBench,
MemoryArena and WorldMemArena move toward state, workflow and action-dependent
memory. End-to-end accuracy still hides whether failure occurred during write,
maintenance, retrieval or use.

GhostWriter reports about 98 percent injection and 60 percent activation in
its tested setup; these are threat-model-specific figures, not universal
deployment rates. The systematic poisoning study identifies multiple write
channels and structural vulnerabilities. MEXTRA and AgentLeak show that output
inspection alone misses private information exposed through memory and
internal agent channels.

Deletion research remains less mature than retrieval. External memory should
first use lineage-aware deletion, index rebuild and adversarial verification;
model-weight unlearning is relevant only when data entered model weights.

## Agent Memory Foundations and Mechanisms 2026

Canonical ID: `source-agent-memory-foundations-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.88`  
Sources: none

# Agent Memory Foundations and Mechanisms — August 2026

Primary sources checked on 2026-08-09:

- MemGPT: https://arxiv.org/abs/2310.08560
- Generative Agents: https://arxiv.org/abs/2304.03442
- Reflexion: https://arxiv.org/abs/2303.11366
- A-MEM: https://arxiv.org/abs/2502.12110
- Mem0: https://arxiv.org/abs/2504.19413
- Agent Workflow Memory: https://arxiv.org/abs/2409.07429
- Voyager: https://arxiv.org/abs/2305.16291
- Zep/Graphiti: https://arxiv.org/abs/2501.13956
- HippoRAG: https://arxiv.org/abs/2405.14831
- MemoryBank: https://arxiv.org/abs/2305.10250
- LongMemEval: https://arxiv.org/abs/2410.10813

## Evidence audit

The literature supports distinct working, episodic, semantic, procedural and
entity-temporal mechanisms. It does not establish one universal architecture.
MemGPT demonstrates hierarchical paging; Generative Agents and Reflexion show
useful episodic reflection; A-MEM and Mem0 explore semantic consolidation;
AWM and Voyager demonstrate reusable procedures; Graphiti and HippoRAG support
relational retrieval. Each result is workload-bound.

Reflection and consolidation are transformations, not ground truth. Derived
notes must retain their source episode, model/config identity and version.
MemoryBank's forgetting curve is an application heuristic, not evidence that
biological decay is a correct retention policy. Expiry, rank decay,
supersession, archival and verified erasure are separate operations.

## Agent Memory Systems Audit 2026

Canonical ID: `source-agent-memory-systems-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.86`  
Sources: none

# Agent Memory Systems Audit — August 2026

Primary documentation and repositories:

- Letta context hierarchy: https://docs.letta.com/guides/core-concepts/memory/context-hierarchy
- Letta repository: https://github.com/letta-ai/letta
- LangGraph memory: https://docs.langchain.com/oss/python/langgraph/add-memory
- LangGraph persistence: https://docs.langchain.com/oss/python/langgraph/persistence
- Mem0 migration: https://docs.mem0.ai/migration/platform-v2-to-v3
- Mem0 releases: https://github.com/mem0ai/mem0/releases
- Graphiti repository: https://github.com/getzep/graphiti
- Graphiti deletion: https://help.getzep.com/deleting-data-from-the-graph
- OpenAI Conversations: https://platform.openai.com/docs/api-reference/conversations
- Anthropic memory tool: https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/tool-use-concepts.md

## Observed boundaries

- LangGraph separates thread checkpoints from cross-thread stores and has the
  strongest recovery primitives, but supplies no complete memory policy.
- Letta exposes agent-editable in-context blocks and larger external stores;
  autonomous writes need application-level admission controls.
- Mem0 is an embeddable extraction/retrieval service. Its newer automatic
  ingest is ADD-only; old descriptions of automatic ADD/UPDATE/DELETE should
  not be assumed current.
- Graphiti models episodes and temporally valid edges. Episode deletion may
  leave information in shared node names or summaries, so API deletion is not
  proof of erasure.
- OpenAI Conversations provides conversation state, not a complete long-term
  memory lifecycle. Anthropic's memory tool is a client-implemented file
  primitive without built-in semantic retrieval or access control.

Versions, managed services and open-source implementations must be evaluated
separately. Product benchmark claims remain vendor evidence until replicated.

## Agent Runtime Framework Landscape Evidence Audit August 2026

Canonical ID: `source-agent-runtime-framework-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.86`  
Sources: none

# Agent Runtime Framework Landscape Evidence Audit — August 2026

This audit separates implementation libraries, opinionated agent harnesses,
operational platforms and durable workflow substrates. They are adjacent
options, not interchangeable products. Primary documentation, repositories,
release metadata and security-policy presence were checked on 2026-08-13.

## Primary sources

- [LangGraph repository](https://github.com/langchain-ai/langgraph) and
  [interrupt documentation](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [Deep Agents repository](https://github.com/langchain-ai/deepagents)
- [DeerFlow repository](https://github.com/bytedance/deer-flow)
- [OpenClaw repository](https://github.com/openclaw/openclaw),
  [runtime architecture](https://github.com/openclaw/openclaw/blob/main/docs/agent-runtime-architecture.md)
  and [agent configuration](https://github.com/openclaw/openclaw/blob/main/docs/gateway/config-agents.md)
- [OpenAI Agents SDK documentation](https://openai.github.io/openai-agents-python/),
  [sessions](https://openai.github.io/openai-agents-python/sessions/),
  [human approval](https://openai.github.io/openai-agents-python/human_in_the_loop/)
  and [durable integrations](https://openai.github.io/openai-agents-python/running_agents/)
- [Pydantic AI durable execution](https://pydantic.dev/docs/ai/capabilities/durable_execution/overview/)
- [Google ADK repository](https://github.com/google/adk-python)
- [Microsoft Agent Framework documentation](https://learn.microsoft.com/en-us/agent-framework/),
  [workflow execution](https://learn.microsoft.com/en-us/agent-framework/workflows/workflows)
  and [self-hosting](https://learn.microsoft.com/en-us/agent-framework/hosting/self-hosting)
- [Temporal Python SDK](https://github.com/temporalio/sdk-python)
- [Anthropic, Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)

## Landscape observations

### Libraries and graph runtimes

**LangGraph** exposes explicit graph state, checkpointers and interrupts. It is
a fit when an application needs to own control flow and state transitions while
avoiding a custom checkpoint and resume implementation. An interrupt persists
graph state, but production use still requires a durable checkpointer and a
stable thread identity. Node replay means side effects must remain idempotent or
be moved behind a separate effect boundary.

**OpenAI Agents SDK** is a comparatively small agent-loop SDK with tools,
handoffs, guardrails, sessions, serialized approval state, streaming and
tracing. Its documentation distinguishes conversational sessions from durable
orchestration and points to Dapr, Temporal, Restate and DBOS integrations for
long waits and process recovery. Tracing is enabled by default and its data
handling must be configured deliberately.

**Pydantic AI** emphasizes typed inputs, outputs and dependency injection. Its
durable-execution layer officially integrates Temporal, DBOS, Prefect and
Restate, making it a useful typed agent layer over a separate reliability
substrate rather than evidence that one in-process loop is durable by itself.

**Google ADK** provides a runner, sessions, event persistence, artifacts,
memory, tools, plugins and sequential, parallel and loop agents. It is optimized
for the Google ecosystem while documenting model- and deployment-agnostic
interfaces. Storage and deployment choices still determine isolation,
residency, recovery and lock-in.

**Microsoft Agent Framework** provides agents, sessions, workflows,
checkpointing, approval-required tools and hosting integrations. The current
documentation marks some hosting packages and language surfaces as preview or
prerelease. Its bulk-synchronous workflow execution has explicit superstep
barriers, which affects latency and parallel branch design.

### Opinionated harnesses

**Deep Agents** is a batteries-included harness built on LangGraph for
long-horizon work. It adds planning, subagents, filesystem abstractions,
context offloading, skills, memory, shell access and human approval. Its own
security guidance places the hard boundary at the tools and sandbox: a capable
model can exercise whatever authority the harness exposes. Use LangGraph or a
smaller loop when those harness defaults are unnecessary.

**DeerFlow 2.0** is a full super-agent harness built around LangGraph and
LangChain with planning, subagents, memory, skills, filesystem workspaces,
channels, gateway APIs and sandbox providers. The local sandbox is explicitly
not secure isolation and host shell access is disabled by default. Version 2.0
was rebuilt rather than incrementally upgraded from version 1, so migration and
API-stability risk need their own gate.

### Operational platform

**OpenClaw** combines an agent runtime with a gateway, sessions, channels,
tools, skills, plugins, policy hooks and operational configuration. It is a
strong candidate when the product needs a persistent multi-channel agent host
rather than an embeddable Python control-loop library. Its runtime architecture
supports built-in and plugin harnesses and fails closed when an explicitly
selected plugin runtime is unavailable. The larger control plane also creates a
larger configuration, upgrade and authority surface.

### Durable workflow substrate

**Temporal** is not an agent harness. It supplies durable workflow and activity
execution for long-running asynchronous business logic. It becomes relevant
when process restarts, timers, human waits and retries are first-class
requirements. Workflow replay still does not make an arbitrary external API
effect exactly-once; activities need idempotency keys, transactional sinks or
reconciliation.

## Repository health snapshot

All reviewed repositories were active and non-archived when checked. Recent
releases existed for Deep Agents, DeerFlow, OpenClaw, LangGraph, OpenAI Agents
SDK, Pydantic AI, Google ADK and Microsoft Agent Framework. Some repositories
publish a dedicated security policy and some do not expose one at the expected
GitHub path. These are maintenance signals only. Stars, organization name,
release recency and a security file do not establish runtime safety,
compatibility or workload fit.

## Evidence boundary

Most capability claims above are E2 implementation evidence from maintainers.
They show what an interface intends to support, not comparative production
quality. No primary source establishes a universal winner across coding agents,
research agents, customer-facing chat, multi-channel personal agents and
irreversible business workflows. Adoption therefore requires a version-pinned
application replay, threat-model review and failure-injection test.

Conversational persistence, checkpoint persistence and external-effect safety
are distinct. A framework can implement the first two while leaving causal
effect identity, current authorization, compensation and reconciliation to the
application.

## Agentic Runtime and RAG Security Evidence Audit August 2026

Canonical ID: `source-agentic-security-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.9`  
Sources: none

# Agentic Runtime and RAG Security Evidence Audit — August 2026

This audit covers the security boundary created when probabilistic model output
can influence retrieval, memory, tools, code execution, other agents and
external side effects. It distinguishes taxonomies and implementation guidance
from controls with independently measured effectiveness.

## Primary sources

- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)
- [OWASP LLM01 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/),
  [LLM06 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/),
  [LLM08 Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)
  and [RAG Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html)
- [Microsoft zero-trust guidance for autonomous agents](https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems)
  and [least privilege for agent identities](https://learn.microsoft.com/en-us/security/zero-trust/sfi/least-privilege-for-ai-agents)
- [AWS security principles for agentic AI](https://aws.amazon.com/blogs/security/four-security-principles-for-agentic-ai-systems/)
  and [Agentic AI Lens security principles](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/security-design-principles.html)
- [NIST CAISI analysis of agent-security RFI responses](https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai)
- [PoisonedRAG, USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/zou)
- [Kubernetes SIGs Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
  and [Azure Container Apps dynamic sessions](https://learn.microsoft.com/en-us/azure/container-apps/sessions)
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)
- [A2AS paper](https://arxiv.org/abs/2510.13825) and
  [IBM runtime-security article](https://www.ibm.com/think/insights/agentic-ai-runtime-security)
- [Databricks DASF v3 conference description](https://www.databricks.com/dataaisummit/session/move-fast-stay-secure-enterprise-ai-agent-security-practice)

## Confirmed security model

OWASP's agentic taxonomy names goal hijacking, tool misuse, identity and
privilege abuse, agentic supply-chain vulnerabilities and unexpected code
execution among its top risks. The LLM taxonomy separately covers prompt
injection, excessive agency and vector or embedding weaknesses. These lists are
threat taxonomies, not proof that one product or prompt mitigates the risks.

The strongest repeated architecture principle across OWASP, AWS and Microsoft
is to keep authorization and safety enforcement outside model reasoning.
Retrieved text, tool output, memory, peer-agent messages and generated code are
untrusted inputs. Every action must be checked against current user delegation,
agent identity, resource scope, arguments, risk, budget and effect state by a
deterministic policy boundary.

PoisonedRAG demonstrates that a small number of crafted corpus entries can
steer selected answers in a large retrieval corpus. Its reported attack rates
are benchmark-specific; they establish a practical attack surface, not a
universal production compromise rate. The defensive implication is broader:
source approval, lineage, quarantine, index integrity, authorization-before-
retrieval, cross-source corroboration and fail-closed behavior must be tested as
one pipeline.

## Tool and framework corrections

The Microsoft repository found during this audit is
`microsoft/agent-governance-toolkit`, not `microsoft/agent-rag-governance`. It
implements a policy-interception and audit layer and includes RAG-related
controls, but it is a public-preview implementation candidate, not a security
standard or automatic trust boundary. Pin a release and test policy bypass,
adapter coverage, identity propagation, fail-closed behavior and upgrade
rollback before adoption.

A2AS defines behavior certificates, authenticated prompts, security boundaries,
in-context defenses and codified policies. Its paper and vendor descriptions
make it E2 design evidence. A signed declaration describes intended authority;
it does not prove runtime conformance unless an external monitor enforces and
audits it.

Kubernetes Agent Sandbox and Azure Container Apps sessions provide concrete
isolation substrates. Their existence does not make arbitrary configuration
safe: egress, host mounts, secrets, kernel boundary, resource quotas, image
provenance, lifecycle cleanup and tenant mapping remain deployment tests.

## Evidence boundaries and unresolved claims

Databricks publicly describes DASF v3 and its focus on the combination of
sensitive data, untrusted inputs and external actions. The exact claim of
"35 new agentic risks plus six controls" was not confirmed in an accessible
primary artifact during this review, so it is not promoted into the knowledge
base. DASF remains E2 vendor framework guidance until the versioned artifact and
control inventory can be audited directly.

No reviewed source establishes perfect prompt-injection detection, universally
safe verification prompting or a universally trusted agent framework. Multiple
retrieval sources improve resilience only when they have independent trust
provenance; duplicating the same poisoned upstream through two indexes is not
corroboration. Model-based scanners and verifier prompts are signals, never the
sole authorization or action-safety control.

## Agentic Security Cross-verification Audit August 2026

Canonical ID: `source-agentic-security-verification-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.91`  
Sources: none

# Agentic Security Cross-verification Audit — August 2026

This second-pass audit cross-checks security claims against peer-reviewed
benchmarks, official protocol specifications, reviewed advisories, current
repository state and community failure reports. Community posts are used only
to discover cases that can be reproduced or verified elsewhere.

## Benchmarks and attack evidence

- [AgentDojo, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)
  provides a dynamic tool-use environment with benign utility tasks and prompt-
  injection security cases.
- [InjecAgent, Findings of ACL 2024](https://aclanthology.org/2024.findings-acl.624/)
  covers indirect prompt injection, harmful actions and data exfiltration across
  tool-integrated agents.
- [AgentDyn](https://arxiv.org/abs/2602.03117) and
  [Indirect Prompt Injections: Are Firewalls All You Need?](https://arxiv.org/abs/2510.05244)
  are recent preprints showing that static benchmark saturation can hide weak
  attacks, flawed oracles and over-defense. They support adaptive attacks and
  utility controls, but remain E2 until peer review or independent replication.
- [AgentSecBench](https://arxiv.org/abs/2605.26269) formalizes instruction,
  retrieval-confidentiality and capability-integrity games. Its key distinction
  between model-visible annotations and enforcing projections is useful E2
  methodology rather than a universal security proof.

The convergent result is not a reliable universal attack percentage. It is that
tool-using agents need paired utility/security evaluation, adaptive attacks,
deterministic external-state oracles and explicit authority boundaries. A
defense that reaches zero attacks on one frozen benchmark is not established as
secure against changed tools, models, tasks or adaptive attackers.

## Protocol and extension evidence

The [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
requires resource or audience binding for protected HTTP servers and forbids
token passthrough. The current
[MCP security guidance](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)
also covers per-client consent, session hijacking, one-click local server
installation and least privilege. MCP provides interoperability; it does not
make tool descriptions, local commands, project configuration or server output
trusted.

Reviewed advisories establish concrete cross-layer failures:

- [GHSA-8q5r-mmjf-575q](https://github.com/advisories/GHSA-8q5r-mmjf-575q):
  attacker-controlled project MCP configuration in a pull request could execute
  on a privileged automation runner before version 1.0.74.
- [GHSA-7r34-79r5-rcc9](https://github.com/advisories/GHSA-7r34-79r5-rcc9):
  unauthenticated SSRF in an MCP server could reach internal services and inject
  attacker-controlled responses into agent context before version 0.17.0.
- [GHSA-3q26-f695-pp76](https://github.com/advisories/GHSA-3q26-f695-pp76):
  indirect instructions in Git history could reach command-injection-prone MCP
  tools.
- [GHSA-9mqq-jqxf-grvw](https://github.com/advisories/GHSA-9mqq-jqxf-grvw):
  path traversal through an MCP tool could become persistent code execution.
- [GHSA-c67j-w6g6-q2cm](https://github.com/advisories/GHSA-c67j-w6g6-q2cm):
  model-controlled serialized fields could reach a deserialization path and
  extract secrets in affected LangChain versions.

These incidents do not imply that MCP or one framework is inherently unsafe.
They show why configuration, transport, tool schema, serialization, network and
runtime execution must be evaluated as one authority chain.

## Security tooling and repository verification

Repository metadata and latest releases were checked on 2026-08-13. All listed
projects were active and non-archived at that time.

- [AgentDojo](https://github.com/ethz-spylab/agentdojo): benchmark environment;
  latest observed release `v0.1.35`. No root `SECURITY.md` was found at the
  expected path.
- [Microsoft PyRIT](https://github.com/microsoft/PyRIT): flexible red-team
  orchestration; latest observed release `v1.0.1`; security policy present.
- [NVIDIA garak](https://github.com/NVIDIA/garak): model vulnerability scanner;
  latest observed release `v0.16.0`; security policy present.
- [promptfoo](https://github.com/promptfoo/promptfoo): eval and red-team runner;
  latest observed release `0.122.0`; its security policy explicitly states that
  configurations and referenced code are trusted and not sandboxed.
- [Cisco Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner) and
  [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector): best-effort
  static and optional model-assisted extension scanners. Passing scans are not
  proof of benign behavior.
- [Kubernetes SIGs Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
  and [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox): sandbox
  control planes with current releases and security policies. The configured
  runtime, mounts, egress, secrets and tenancy determine the actual boundary.
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit):
  policy and audit implementation candidate; latest observed release `v4.1.0`;
  version-specific application tests remain required.

Tool claims are E2 maintainer evidence. Activity, releases and a security policy
are health signals, not comparative effectiveness. The
[PyRIT v0.12.1 security release](https://github.com/microsoft/PyRIT/releases/tag/v0.12.1)
is an especially important counterexample: a remotely loaded poisoned dataset
could reach unsafe template rendering. Security evaluation tooling must itself
run with isolated credentials, filesystem and egress.

## Community and forum signals

Recent Reddit and GitHub discussions surfaced weak regex-only injection filters,
multi-turn attacks, agent-team trust gaps and proxy defenses reporting perfect
scores on selected benchmarks. These are useful hypothesis generators, but the
reports use small or self-selected datasets and sometimes promote the author's
own product. No performance number from a forum post is promoted here. Their
reproducible lesson is converted into tests: preserve benign controls, include
multi-turn and adaptive variants, record seeds and versions, and verify claimed
blocks against authoritative tool state.

## Durable conclusions

1. Test security and benign utility together; otherwise refusal is mistaken for
   protection.
2. Add adaptive attacks and changed tool schemas after tuning; frozen public
   suites are development sets, not final holdouts.
3. Enforce authority by projection, policy, isolation and validation, not by
   prompt annotations or scanner verdicts alone.
4. Treat skills, MCP configuration, eval fixtures, reports and red-team tools as
   executable supply-chain inputs.
5. Keep the exact component version, configuration, model, attack corpus,
   oracle and residual failures in every security release record.

## Bounded Improvement Technique Evidence Audit August 2026

Canonical ID: `source-bounded-improvement-techniques-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.82`  
Sources: none

# Bounded Improvement Technique Evidence Audit — August 2026

Primary sources checked on 2026-08-12:

- [MIPROv2](https://arxiv.org/abs/2406.11695)
- [GEPA, ICLR 2026](https://openreview.net/forum?id=RQm2KQTM5r)
- [Darwin Gödel Machine, 2025](https://arxiv.org/abs/2505.22954)
- [Red Queen Gödel Machine, 2026](https://arxiv.org/abs/2606.26294)
- [SePO, 2026](https://arxiv.org/abs/2606.04465)
- [Externally grounded verification of agent loops, 2026](https://arxiv.org/abs/2607.25152)
- [GEPA counterevidence from defective seeds, ACL SRW 2026](https://aclanthology.org/2026.acl-srw.8/) shows that prompt optimization can regress sharply when its starting material or feedback is defective.

## Evidence boundary

MIPROv2 and GEPA support bounded search over prompts and demonstrations on the
tested workloads. They do not prove transfer to a different model, task
distribution or production policy. DGM supports archive-based modification of
a coding-agent implementation under a fixed benchmark and search process, but
does not demonstrate domain-general or indefinitely safe recursive improvement.

RQGM and SePO explore objective or optimizer co-evolution. They are recent
preprints and remain E2 experimental evidence. A candidate that evaluates its
own work through the same information channel can mistake plausible activity
for external progress; the July 2026 externally grounded verification study is
fresh E2 evidence for keeping a world-state oracle outside the mutable surface.

## Promotion boundary

Safe improvement means a bounded, versioned mutable surface; fixed budgets;
shared baselines; protected selection and holdout tasks; immutable safety
sentinels; sandboxed execution; and human-controlled canary promotion with a
kill switch and rollback. Changing the evaluator starts a new governed epoch
and invalidates naive before/after comparisons.

## Bounded Self-Improvement Evidence 2025–2026

Canonical ID: `source-bounded-self-improvement-2025-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.8`  
Sources: none

# Bounded Self-Improvement Evidence 2025–2026

Primary sources checked on 2026-08-12:

- [Darwin Gödel Machine, 2025](https://arxiv.org/abs/2505.22954)
- [Red Queen Gödel Machine, 2026](https://arxiv.org/abs/2606.26294)
- [GEPA repository and paper](https://github.com/gepa-ai/gepa)

## Evidence class

All three are E2 for durable recommendations here. DGM has unusually detailed
experiments, ablations and artifacts but remains narrow coding-agent evidence.
RQGM is a recent preprint. GEPA supports reflective evolution of prompts and
code-like text, but does not by itself prove recursive improvement of the
optimizer.

## What DGM demonstrates

DGM branches an archive of coding agents, lets selected agents modify their own
codebase, and evaluates descendants. After 80 iterations, the paper reports
SWE-bench improvement from 20.0% to 50.0% and full-Polyglot improvement from
14.2% to 30.7%, with ablations for self-improvement and open-ended exploration.
Experiments used sandboxing and human oversight.

## What remains unproven

The result does not demonstrate domain-general recursive self-improvement,
indefinite capability growth, safe evaluator self-modification or reliable
transfer to production RAG. The archive-selection mechanism remained fixed.
RQGM proposes changing utilities only at epoch boundaries while keeping each
within-epoch objective fixed; this is a useful control concept, not yet strong
production evidence.

## Safety interpretation

Production systems should begin with a fixed evaluator, bounded mutable surface,
paired replay, hidden gates, budgets, sandboxing, human promotion, canaries and
rollback. Evaluator evolution is a separate governed transaction with an old-
and-new objective compatibility audit.

## Chunking Evidence Audit 2025–2026

Canonical ID: `source-chunking-evidence-2025-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.9`  
Sources: none

# Chunking Evidence Audit 2025–2026

Primary sources checked on 2026-08-12:

- [Is Semantic Chunking Worth the Computational Cost?, Findings NAACL 2025](https://aclanthology.org/2025.findings-naacl.114/)
- [MoC: Mixtures of Text Chunking Learners, ACL 2025](https://aclanthology.org/2025.acl-long.258/)
- [Structure-Aware Semantic Chunking with Title-Chain Prefixes, 2026 preprint](https://arxiv.org/abs/2608.00824)

## Evidence class

The two ACL Anthology papers are E3. The August 2026 structure-aware study is E2:
it reports a substantial, carefully sliced single-corpus evaluation, but is a
fresh preprint without independent replication.

## Supported conclusion

Semantic chunking is not a universal upgrade over fixed-size segmentation. The
NAACL study evaluates document retrieval, evidence retrieval and answer
generation and finds no consistent gain that justifies its computational cost.
MoC supplies evidence that query granularity and chunking policy can interact,
but its learned mixture adds complexity and does not establish a general
default. The 2026 title-chain study is promising for structured Markdown but
also identifies an evaluation trap: changing indexed prefixes can alter both
retrieval and relevance scoring unless the scorer uses a controlled view.

## Required baseline

Every chunking experiment keeps a simple token-window baseline and a
structure-aware baseline. It varies one factor at a time where possible:
boundary policy, target size, overlap, contextual prefix, parent expansion and
retrieval depth. Report index size, ingestion cost, Recall@k, evidence coverage,
context precision, answer quality and citation correctness.

## Transfer limits

Results depend on parser output, query granularity, embedding model, retriever,
reranker, context budget and relevance labels. A chunker cannot repair missing
or misordered source content.

## Chunking Landscape and Use-Case Audit August 2026

Canonical ID: `source-chunking-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.9`  
Sources: none

# Chunking Landscape and Use-Case Audit — August 2026

Primary research checked on 2026-08-12:

- [Semantic Chunking, Findings NAACL 2025](https://aclanthology.org/2025.findings-naacl.114/)
- [MoC: Mixtures of Text Chunking Learners, ACL 2025](https://aclanthology.org/2025.acl-long.258/)
- [Mix-of-Granularity, COLING 2025](https://aclanthology.org/2025.coling-main.384/)
- [Dense X Retrieval / propositions, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.845/)
- [RAPTOR, ICLR 2024](https://openreview.net/forum?id=GN921JHCRw)
- [cAST code chunking, Findings EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.430/)
- [HiChunk and HiCBench, ACL 2026](https://aclanthology.org/2026.acl-long.1372/)
- [Late Chunking](https://arxiv.org/abs/2409.04701)
- [Adaptive Chunking, LREC 2026 paper and implementation](https://arxiv.org/abs/2603.25333)
- [Structure-Aware Tabular Chunking](https://arxiv.org/abs/2605.00318)
- [Structure-Aware Semantic Chunking with Title Chains](https://arxiv.org/abs/2608.00824)
- [Anthropic Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
- [PageIndex tree navigation](https://github.com/VectifyAI/PageIndex)

## Evidence classes

ACL, EMNLP, NAACL, COLING, ICLR and LREC publications are E3 for the evaluated
mechanism under their reported datasets. Current arXiv preprints, project-owned
repositories and vendor experiments are E2. None establishes a universal best
chunker because parser output, corpus structure, query granularity, retriever,
embedding model, context budget and evidence labels materially interact.

## Supported conclusions

Fixed token windows and structure-aware sections remain mandatory controls.
Semantic splitting has inconsistent benefits relative to its compute cost.
Fine-grained propositions can improve fact retrieval but add generation cost and
can detach qualifiers. Hierarchical and multi-granular methods help when questions
span levels of abstraction, but expand index and retrieval complexity. Code and
tables benefit from preserving their native structures rather than generic text
boundaries. HiCBench highlights that sparse-evidence QA benchmarks can conceal
chunking differences; evidence-dense, boundary-annotated evaluation is preferable.

## Selection dimensions

Select by source structure, answer locality, query granularity, atomicity needs,
embedding context limit, update frequency, access boundaries and ingestion budget.
Small units improve pinpoint retrieval but lose context and multiply vectors;
large units preserve context but dilute similarity and consume generation budget.
Overlap reduces boundary misses while duplicating evidence and index size.

## Evaluation contract

Use identical parsed source elements and question/evidence labels. Measure boundary
integrity, evidence Recall@k, MRR or nDCG, context precision, answer completeness,
citation correctness, duplicate evidence rate, vector count, ingestion time and
retrieval/generation latency. For prefixes, summaries or propositions, score
relevance against an invariant source view so generated text cannot make its own
candidate appear relevant. Parser defects remain parser defects.

## Coding Agent Harness and Skills Evidence Audit August 2026

Canonical ID: `source-coding-agent-harness-and-skills-evidence-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.92`  
Sources: none

# Coding Agent Harness and Skills Evidence Audit — August 2026

This audit examines how current coding-agent systems represent project
instructions, reusable skills, lifecycle enforcement, external tools,
permissions and isolated work. Primary specifications and vendor documentation
were checked on 2026-08-16. Product behavior is release- and surface-specific;
the short review interval is intentional.

The expanded audit also searched recent arXiv and OpenReview papers, active
GitHub repositories, releases and issues, plus Reddit and Hacker News. These
are separate evidence classes: specifications and shipped code establish
interfaces, controlled studies estimate effects, repository issues expose
failure hypotheses, and community posts are discovery signals only. Stars,
votes, benchmark positions and repeated claims are not independent evidence.

## Primary sources

- [Agent Skills specification](https://agentskills.io/specification),
  [skill-creation guidance](https://agentskills.io/skill-creation/best-practices)
  and [evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills)
- [AGENTS.md open format](https://agents.md/)
- OpenAI Codex manual and official guidance for
  [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
  [skills](https://learn.chatgpt.com/docs/build-skills) and
  [coding-agent setup](https://learn.chatgpt.com/guides/best-practices)
- Anthropic Claude Code documentation for
  [project instructions](https://code.claude.com/docs/en/memory),
  [skills](https://code.claude.com/docs/en/skills),
  [hooks](https://code.claude.com/docs/en/hooks-guide),
  [subagents](https://code.claude.com/docs/en/sub-agents) and
  [security](https://code.claude.com/docs/en/security)
- GitHub Copilot
  [customization matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet),
  [skill guidance](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
  and [hook reference](https://docs.github.com/en/copilot/reference/hooks-reference)
- Cursor [project rules](https://docs.cursor.com/context/rules-for-ai) and
  [agent setup guidance](https://cursor.com/blog/agent-best-practices)
- Model Context Protocol
  [security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices)

## Expanded implementation and research sources

Maintained implementations checked on 2026-08-16 include OpenAI
[Codex](https://github.com/openai/codex), Anthropic
[Claude Code](https://github.com/anthropics/claude-code), Google
[Gemini CLI](https://github.com/google-gemini/gemini-cli),
[OpenHands](https://github.com/OpenHands/OpenHands),
[Cline](https://github.com/cline/cline),
[Continue](https://github.com/continuedev/continue),
[Goose](https://github.com/aaif-goose/goose) and
[mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent). Classic
SWE-agent points users to mini-swe-agent. Aider's repository-map and lint/test
mechanisms remain relevant, but its latest release was from 2025. Roo Code was
archived on 2026-05-15 and is historical evidence only.

The implementation review covered Codex
[customization](https://learn.chatgpt.com/docs/customization/overview),
[subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
[hooks](https://learn.chatgpt.com/docs/hooks),
[security](https://learn.chatgpt.com/docs/agent-approvals-security) and preview
[execpolicy](https://github.com/openai/codex/blob/main/codex-rs/execpolicy/README.md);
Claude Code [features](https://code.claude.com/docs/en/features-overview),
[agent teams](https://code.claude.com/docs/en/agent-teams) and Anthropic's
[skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md);
Gemini [Plan Mode](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/plan-mode.md)
and [sandbox](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/sandbox.md);
OpenHands [skills](https://github.com/OpenHands/OpenHands/blob/main/skills/README.md),
[AGENTS.md](https://github.com/OpenHands/OpenHands/blob/main/AGENTS.md) and
[benchmarks](https://github.com/OpenHands/benchmarks); SWE-agent
[trajectories](https://github.com/SWE-agent/SWE-agent/blob/main/docs/usage/trajectories.md);
and Aider's [repository map](https://github.com/Aider-AI/aider/blob/main/aider/website/docs/repomap.md).

Controlled and empirical sources include:

- [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988),
  [AGENTS.md efficiency](https://arxiv.org/abs/2601.20404),
  [two-agent context ablation](https://arxiv.org/abs/2607.27250),
  [configuration smells](https://arxiv.org/abs/2606.15828) and Vercel's scoped
  [AGENTS.md versus Skills eval](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)
- [SkillsBench](https://arxiv.org/abs/2602.12670),
  [SWE-Skills-Bench](https://arxiv.org/abs/2603.15401),
  [skills in the wild](https://arxiv.org/abs/2604.04323),
  [From Registry to Repository](https://arxiv.org/abs/2607.00911) and
  [GitSkills](https://arxiv.org/abs/2608.10906)
- [ContextBench](https://arxiv.org/abs/2602.05892),
  [Agent Retrieval Bench](https://arxiv.org/abs/2607.24882),
  [Agentic Harness Engineering](https://arxiv.org/abs/2604.25850) and
  [Claw-SWE-Bench](https://arxiv.org/abs/2606.12344)
- [SWE-EVO](https://arxiv.org/abs/2512.18470),
  [Saving SWE-Bench](https://arxiv.org/abs/2510.08996),
  [E2EDevBench](https://arxiv.org/abs/2511.04064) and
  [SecureAgentBench](https://arxiv.org/abs/2509.22097)
- [Skill-Inject](https://arxiv.org/abs/2602.20156),
  [Agent Skills in the Wild](https://arxiv.org/abs/2601.10338),
  [credential leakage](https://arxiv.org/abs/2604.03070) and
  [SkillSec-Eval](https://arxiv.org/abs/2607.13987)
- [HarnessAudit](https://arxiv.org/abs/2605.14271),
  [Harness-Bench](https://arxiv.org/abs/2605.27922),
  [LoopsBench](https://arxiv.org/abs/2608.00267) and
  [Harness-IF](https://arxiv.org/abs/2608.11727)
- [tool-architecture comparison](https://arxiv.org/abs/2608.11386),
  [agentic retrieval and delivery comparison](https://arxiv.org/abs/2605.15184),
  [scaffolding-release study](https://arxiv.org/abs/2607.03691) and
  [HarnessOpt-Bench](https://arxiv.org/abs/2608.06301)
- [PROJECTMEM](https://arxiv.org/abs/2606.12329),
  [filesystem-memory study](https://arxiv.org/abs/2607.26637),
  [global skill evolution](https://arxiv.org/abs/2608.06153),
  [programmatic skill learning](https://arxiv.org/abs/2608.11338),
  [skill-induced failure analysis](https://arxiv.org/abs/2608.11888) and
  [malicious skill-file assessment](https://arxiv.org/abs/2608.05223)

Current evaluation and measurement sources also include OpenAI's July 2026
[coding-evaluation audit](https://openai.com/index/separating-signal-from-noise-coding-evaluations/),
[SWE-bench-Live](https://swe-bench-live.github.io/) and the independent
[Harness Bench](https://www.harness-bench.ai/). These inform evaluation design,
not a universal ranking of products.

## Evidence observations

### 1. The reusable architecture is layered, not a single prompt file

The reviewed systems expose different filenames and configuration syntax, but
their useful control surfaces converge:

1. A task prompt carries the current goal, context, constraints and done
   condition.
2. Repository instructions carry stable project facts, commands, conventions
   and review expectations.
3. Path-scoped instructions narrow those rules for a package or service.
4. Skills carry reusable procedures and load only when relevant.
5. Hooks and CI run deterministic checks or block actions at lifecycle points.
6. Tool policy, sandboxing and credentials constrain actual authority.
7. MCP or equivalent connectors provide live external data and actions.
8. Subagents or worktrees provide context or workspace isolation when the task
   warrants their coordination cost.

These layers are not substitutes. A skill is context, not a security boundary;
a hook may enforce a check but also executes code; MCP adds capability but also
adds identity, authorization and network attack surfaces.

### 2. `AGENTS.md` is a portable base, not a portable full configuration

The open `AGENTS.md` format is plain Markdown intended for project overview,
setup, build, test, style, security and PR guidance. It supports nested files
with closer instructions overriding broader ones. Codex documents a concrete
root-to-working-directory discovery chain and a default combined byte limit.

Portability stops at the content layer. Discovery, precedence, size limits,
cloud support and vendor-specific alternatives differ by product and surface.
GitHub documents different support matrices across IDE, cloud agent and code
review. Claude Code has its own `CLAUDE.md` and path-scoped rule mechanisms.
Cursor supports project rules and documents product-version limitations for
`AGENTS.md`. A project therefore needs a tested compatibility matrix rather
than assuming that one file behaves identically everywhere.

### 3. Agent Skills has a small portable core

The Agent Skills specification defines a directory containing a required
`SKILL.md` plus optional `scripts/`, `references/` and `assets/`. The portable
frontmatter requires `name` and `description`; optional standard fields include
license, compatibility, metadata and the experimental `allowed-tools` field.
The body contains the workflow instructions.

The specification uses progressive disclosure: hosts initially expose skill
metadata, load the full `SKILL.md` after activation and load supporting files
only when required. It recommends keeping the main instructions under 500
lines and about 5,000 tokens, with shallow, explicit references to supporting
files.

OpenAI Codex, Claude Code and GitHub Copilot document support for Agent Skills
or compatible `SKILL.md` packages, but vendor extensions and discovery paths
differ. Claude Code explicitly distinguishes standard frontmatter from its own
invocation, subagent and dynamic-context extensions. Portable skills should
keep a standard core and place host-specific behavior in adapters or clearly
declared compatibility metadata.

### 4. A useful skill starts from project evidence

The Agent Skills guidance identifies an LLM-generated skill without domain
context as a common source of vague, generic procedures. Recommended source
material includes actual runbooks, API specifications, schemas, configuration,
review comments, version history and real failure cases.

The reviewed guidance converges on these design properties:

- one coherent job with recognizable trigger conditions;
- a description that states what the skill does and when to use it;
- explicit inputs, steps, outputs, stop conditions and non-inference rules;
- project-specific facts and non-obvious edge cases rather than generic
  explanations the model already knows;
- a clear default rather than an unranked menu of tools;
- deterministic scripts only where computation or file processing benefits
  from repeatability;
- references loaded only under stated conditions;
- precision proportional to task fragility.

Large instruction collections can reduce adherence and waste context. More
rules are not evidence of better alignment.

### 5. Skill activation and task quality are separate eval targets

Official Agent Skills and Claude Code guidance recommend evaluating a skill in
fresh contexts both with and without the skill, or against a previous version.
Activation tests need should-trigger and should-not-trigger cases. Task tests
need realistic prompts, input files, expected behavior, edge cases and
assertions.

Mechanical assertions should use scripts where possible. Semantic or visual
qualities may need calibrated model grading and human review. The comparison
must retain pass rate, evidence, tokens and duration because a skill can improve
quality while imposing unacceptable context, latency or cost overhead.

A skill that activates is not necessarily useful. A skill that produces a good
single demonstration is not necessarily reliable. Promotion requires paired
evidence across representative cases.

### 6. Deterministic enforcement belongs outside prose

Claude Code and GitHub Copilot document lifecycle hooks that can format files,
run tests, validate commands, block protected-file edits or gate tool use.
These mechanisms are stronger than asking the model to remember a mandatory
check, but hooks are executable code and inherit the environment's authority.

Repository-controlled hooks, skills, MCP configuration and package scripts are
untrusted when an agent opens a third-party repository or pull-request branch.
They require admission, immutable version binding and least privilege before
execution. Prompt instructions cannot grant authority or override an external
policy boundary.

### 7. The smallest harness remains the default

The vendor guidance does not establish a universally best coding-agent setup.
The defensible baseline is a single agent with accurate project instructions,
a narrow workspace boundary, relevant build and test commands, a reviewable
diff and a hard done condition. Add a skill only after a repeated workflow is
observed. Add hooks when a mechanical invariant must execute reliably. Add MCP
only for necessary live context or controlled actions. Add subagents only for
separate context, authority or measurable parallelism.

### 8. Repository context has contradictory measured effects

The current evidence rejects a simple claim that an `AGENTS.md` file generally
makes coding agents better. One 2026 study found no general task-success gain
and more than 20 percent average inference-cost overhead across generated and
developer-committed context files. A second study over 10 repositories and 124
pull requests associated `AGENTS.md` with lower median runtime and output-token
use while preserving comparable completion behavior. A July two-agent ablation
over 288 runs found no measurable correctness effect and attributed most
failures to implementation skill rather than missing repository knowledge.

These results are not directly interchangeable: they use different agents,
tasks, repositories, context files and outcomes. The defensible conclusion is
narrower. Context files are useful carriers for non-standard rules and project
facts, but their marginal effect on correctness, cost and runtime must be
measured on the target project. Repository overview prose has no presumption of
value.

Repository mining adds a maintenance warning. The July 2026 revision of the
configuration-smell study found lint leakage, context bloat, skill leakage and
conflicting instructions frequently in 100 popular repositories. These labels
come from proposed heuristics rather than causal task experiments, but they
identify concrete lint and review targets.

### 9. Skill efficacy is sharply conditional

Two current paired-evaluation programs reach apparently different aggregate
results. SkillsBench v4 reports a 16.6 percentage-point average gain across 87
expertise-heavy tasks and 18 model-harness configurations, with focused skills
of at most three modules outperforming larger bundles. SWE-Skills-Bench reports
only a 1.2-point average gain across roughly 565 real-software-engineering task
instances: 39 of 49 public skills did not improve pass rate, three regressed,
and token overhead reached 451 percent in some unchanged-outcome conditions.

The difference is informative rather than resolvable by averaging the numbers.
Curated expertise tasks and public SWE skills exercise different distributions.
Both support paired evaluation; together they reject treating skill adoption,
format validity or a successful demo as evidence of project benefit. Narrow,
version-compatible skills with deterministic acceptance criteria are the most
credible candidates.

### 10. Harness performance requires component and decision observability

Recent harness research treats the prompt, tool schemas, repository context,
execution loop, environment and feedback as one measured system. Agentic
Harness Engineering proposes file-level, revertible harness components,
trajectory distillation and an explicit prediction for each edit that is
checked against later task outcomes. This is promising preprint evidence, not
proof that automatic harness evolution is production-ready.

The reusable mechanism is bounded experimental discipline:

- version every editable harness component and environment dependency;
- retain task-level trajectories, diffs, tool effects, cost and outcome;
- change a bounded surface and state the expected effect before running;
- compare against the same baseline and protected tasks;
- promote only replicated improvements and keep immediate rollback.

Changing the model, harness, environment and tests together destroys
attribution. A high aggregate score cannot reveal which component helped.

### 11. Coding-agent evaluation needs hermeticity and leakage audits

OpenAI's 2026 SWE-bench audit documents contamination and weak-test problems
that can erase useful frontier signal. SWE-bench-Live responds with regularly
updated tasks, while newer project and long-horizon benchmarks emphasize clean
environments and execution-based oracles. Community reports independently flag
agents discovering reference patches or hidden answers through repository,
network, cache or tool paths; these reports are hypotheses until reproduced.

A project harness evaluation should therefore record the exact repository
commit, image, dependencies, model, harness digest and network policy; start
paired runs from clean workspaces and fresh sessions; deny access to reference
patches and holdout metadata; inspect every model-visible channel; and score
authoritative external state and unauthorized effects in addition to tests.
Repeated runs and task slices are needed because one trajectory is not a stable
estimate.

### 12. Skills are a software supply chain

GitSkills counted 3,797,117 `skill.md` occurrences in 282,200 public GitHub
repositories in July 2026, with extensive copying and no central package
manager or compiler governing selection. The count establishes rapid,
decentralized diffusion, not quality or independent adoption.

SkillSec-Eval evaluates 327 real skills across repository admission, semantic
retrieval, planner selection, execution and evolution. HarmfulSkillBench and
MalSkillBench separately show that malicious or harmful skills can influence
agent behavior and that detectors covering only code or only prompt text miss
cross-layer attacks. These are early papers with their own datasets and threat
models, but they agree on the architectural boundary: installing a skill is
admitting executable procedural capability.

Treat third-party skills like dependencies. Pin an immutable source and digest,
review instructions plus scripts and referenced assets, enumerate requested
tools and data flows, test trigger collisions and adversarial content, run with
least privilege, and require review again when the artifact or authority
changes. Popularity and registry presence are not admission evidence.

### 13. GitHub and community evidence is a radar, not a standard

Active repositories reveal recurring implementation directions: provider-
neutral source formats compiled into product adapters; tracked skill, hook and
agent manifests; sandbox-first execution; uniform headless run records; and
trajectory capture for evals. Maintained agents such as Codex, Claude Code,
Gemini CLI, OpenHands, Cline, Continue, Goose and mini-swe-agent remain stronger
implementation references than small configuration packs, but none proves a
best setup for another repository.

Recent Reddit and Hacker News discussion repeatedly reports four operational
pressures: giant instruction files become ignored or contradictory; small
project docs and focused skills survive longer; multi-agent role packs often
add coordination without measured gain; and users struggle to compare harness
changes because token caching, model upgrades and workspace state confound the
result. These are useful query generators and failure hypotheses only. They
must not be promoted as claims without a reproducible repository, trace or
controlled comparison.

### 14. Instruction compliance must be scored per operational rule

Harness-IF evaluates rules placed across system prompts, project files, user
instructions, tool descriptions and skills. Its against-prior measure shows
that aggregate compliance overstates performance when the requested rule
already matches model defaults. The conflict pilot also rejects a universal
"deeper prompt wins" rule: precedence varied by surface and configuration.

Convert every retained instruction into an observable opportunity for
compliance or violation and test rules that oppose the agent's unprompted
default. Keep one canonical owner for each rule and test conflicts explicitly.
Do not infer instruction following from final task success alone.

### 15. Tool architecture changes behavior even when capabilities match

The 11,700-trajectory tool-interface comparison found that alternative
interfaces exposing broadly similar capabilities changed exploration,
consistency, step count and token use. Structured low-level tools improved
repeat-attempt consistency by up to 4.7 times; natural-language search reached
more relevant files; and the evaluated CodeAct-style interface used 41.6
percent fewer steps and 56.3 percent fewer tokens at similar task performance.
Lightweight scratchpad tools had limited effect in that experiment.

These are configuration-specific effects, not a universal winner. Benchmark
the tool schema together with the model, repository, result-delivery method and
loop. Prefer precise bounded tools for common actions while retaining an
audited compound-execution path where repeated inspection or transformation
would otherwise fragment into many calls.

### 16. Retrieval and result delivery are one intervention

The grep-versus-vector study changes rankings across harnesses and between
inline tool output and file-based results. It therefore does not establish
grep as universally superior. It establishes that retrieval cannot be scored
independently of how evidence enters context and whether the agent reads and
uses it.

Project evals should compare lexical, semantic and hybrid retrieval jointly
with delivery, context pressure and evidence use. Exact identifiers favor
lexical search; paraphrases may favor semantic retrieval. Retrieval success
requires a trace from selected evidence to a verified claim or artifact.

### 17. Long-horizon work needs durable state and live regressions

LoopsBench represents tasks as dependency graphs of testable development units
and retains completed units as regression obligations. Its strongest reported
configuration resolved only 25 percent of 112 tasks, and regressions appeared
across all evaluated loop profiles. The result does not prove that one planner
or outer loop is best, but it exposes why a growing transcript is insufficient.

Track completed and unresolved units, dependencies, current failure class,
active regression obligations, workspace checkpoint and next action outside
the transient conversation. After context renewal or delegation, restore that
state and acceptance contract. Classify new failure, regression, environment
failure and insufficient evidence before retrying.

### 18. Evaluate execution alignment and trajectory safety

Harness-Bench reports 5,194 trajectories and shows material variation across
model-harness pairs under shared tasks, environments and budgets. Its
execution-alignment failures include plausible reasoning detached from tool
feedback, workspace state, evidence or required artifacts. HarnessAudit adds
that a correct terminal answer can conceal unauthorized resource access or
information flow, with violations accumulating over longer trajectories.

Every important completion claim should terminate in a verified artifact,
test result or evidence locator. Score boundary compliance, execution fidelity
and system stability over the complete trace, not only the final patch. Report
the model-harness-environment configuration rather than a model score alone.

### 19. Project memory mechanisms are candidates, not defaults

PROJECTMEM demonstrates an append-only event log with deterministic summaries
and advisory pre-action warnings, but its evaluation is a two-month self-study
across ten projects and cannot establish general outcome gains. The larger
filesystem-memory study finds that organization can roughly halve retrieval
cost on large stores while failing to improve answer quality; store quality
also decays unless a strong manager maintains it.

When durable project memory is justified, preserve immutable dated evidence
and derive disposable summaries. Scope every fact, retain superseded history
and attach revalidation triggers. Begin warnings as advisory because old
failures may no longer apply. Do not add project memory without a cross-session
deficit and a maintenance budget.

### 20. Skill procedure and permissions are primary risk surfaces

The differential skill-failure study attributes 125 functional failures and
182 efficiency regressions to loaded skills. Relevant-looking skills caused
implementation omissions or errors; excessive procedure, especially repeated
verification, dominated the measured cost regressions. The malicious-skill
assessment independently found explicit safety recognition in only 1.99
percent of runs in its benchmark and high harmful-execution attempt rates.

Eligibility therefore requires more than topic similarity. Check repository,
language, dependency, artifact-path, permission and cost compatibility before
loading. Keep mandatory skill procedure narrow, make supplementary material
conditional, prevent skills from silently changing environment or authority,
and compare against no skill or a semantically matched alternative. Treat the
malicious-skill rates as benchmark-specific threat evidence, not field rates.

## Evidence boundary and negative claims

- The sources establish current formats, interfaces and maintainer guidance;
  they do not prove comparative project outcomes.
- No primary source establishes one universal coding harness, instruction file,
  skill set, agent count or permission profile as optimal.
- Cross-product support for `AGENTS.md` and `SKILL.md` does not imply identical
  discovery, precedence, extensions or execution semantics.
- Skills, prompts and model-based hooks do not enforce security boundaries.
- A generated setup is a candidate until repository facts are verified and
  paired project-task evals show improvement over the existing workflow.
- Current studies conflict on the aggregate effect of repository instructions
  and skills; their results should not be pooled across task distributions.
- GitHub popularity, registry counts, Reddit votes and benchmark leaderboard
  positions do not establish project fit, security or causal harness benefit.
- Documentation freshness must be checked again before emitting exact paths,
  flags or frontmatter for a named product.
- New April-August 2026 papers remain preprints. Their sample sizes, actor and
  harness choices, task distributions and evaluators bound every reported
  effect; numerical results are not portable defaults.
- PROJECTMEM's event-sourced design is an implementation candidate supported
  by a small self-study, not evidence that every repository needs persistent
  memory.

## Document Parsing Evidence Audit 2025–2026

Canonical ID: `source-document-parsing-evidence-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.88`  
Sources: none

# Document Parsing Evidence Audit 2025–2026

Primary sources checked on 2026-08-12:

- [OmniDocBench, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html)
- [MPDocBench-Parse, 2026 preprint](https://arxiv.org/abs/2605.22100)
- [Dr. DocBench, 2026 preprint](https://arxiv.org/abs/2606.01393)
- [ParseBench, 2026 preprint and public harness](https://arxiv.org/abs/2604.08538)
- [Docling official repository](https://github.com/docling-project/docling)
- [Docling official releases](https://github.com/docling-project/docling/releases)

## Evidence class

OmniDocBench is E3: peer reviewed at CVPR 2025, with comprehensive annotations
over nine document sources. The three 2026 benchmarks are E2 until peer review
or independent reproduction. Docling documentation and releases establish
capabilities and version changes, not comparative quality, so they are E2 for
mechanism and E1 for superiority.

## Convergent observation

Parser quality is multidimensional. Text fidelity alone misses reading order,
tables, formulas, charts, heading hierarchy, cross-page continuity and visual
grounding. The newer multi-page and expert-domain benchmarks were created
because strong scores on clean or single-page data did not transfer reliably to
harder documents.

## Operational boundary

No source establishes one parser as universally best. Selection must use
representative private slices, record parser/model/version/configuration, and
measure downstream evidence retrieval and citation correctness. Native text
extraction should remain a low-cost baseline; OCR/VLM parsing is justified only
for slices where it improves the declared outcome enough to pay its latency,
cost and privacy burden.

## Failure slices to preserve

- scanned and degraded pages;
- multi-column reading order;
- merged and nested tables;
- formulas, footnotes and captions;
- charts whose values are not present in surrounding text;
- cross-page tables and section hierarchy;
- mixed languages and domain notation;
- malformed files, timeouts and partial conversion.

## DomEscobar Agentic Eval Evolution Research

Canonical ID: `source-domescobar-agentic-eval-research`  
Type: `source` · Privacy: `public` · Confidence: `0.82`  
Sources: none

# Agentic Eval Evolution Runtime — Research Audit

- Repository: https://github.com/DomEscobar/agentic-eval-evolution-runtime
- Reviewed commit: `f890e15790f4a1a60adcd835f3c7993c38efaf09`
- Research permalink: https://github.com/DomEscobar/agentic-eval-evolution-runtime/tree/f890e15790f4a1a60adcd835f3c7993c38efaf09/research
- Retrieved: 2026-08-09

## Included research lanes

- Generic agent evaluation and evolution harness
- Evaluation-guided code patch loops
- Evaluation-dataset quality and leakage protection

Each lane contains a plan, source ledger, claims, evidence excerpts, pages, and
a report. This is more auditable than a prose-only research report.

## Defensible core findings

- Evaluation execution, mutation, and promotion are distinct roles.
- Deterministic oracles and hard gates take precedence over weighted soft scores.
- Training/development, candidate selection, and hidden holdout data require
  separate information boundaries.
- A patch loop needs immutable evaluator surfaces, diff/file boundaries, a
  budget, archive, canary, and rollback.
- A dataset architecture is not yet a valid dataset; case validity, oracles,
  representativeness, and leakage must be measured.
- Benchmark success demonstrates performance only on the bound dataset, commit,
  and configuration.

## Claims requiring lower confidence

- New 2026 preprints on autonomous evolution are mostly E2–E3 and not broadly
  replicated.
- Isolated improvement figures from small SWE-bench subsets do not generalize to
  other repositories or task distributions.
- GitHub stars measure attention, not evaluation validity or production
  readiness.
- A separate model does not automatically make an LLM judge independent;
  rubric, data, model family, and correlated errors require calibration.
- A composite dataset-quality score must not hide missing oracles or leakage
  behind an average.

## Assessment

The research structure is a useful hypothesis and source base. It is used as a
secondary synthesis source; strong architecture claims are also checked against
the relevant papers, official repositories, or standards.

## DomEscobar agentic-runtime-techniques

Canonical ID: `source-domescobar-agentic-runtime-techniques`  
Type: `source` · Privacy: `public` · Confidence: `0.95`  
Sources: none

# DomEscobar/agentic-runtime-techniques

- Repository: https://github.com/DomEscobar/agentic-runtime-techniques
- Reviewed commit: `fad44983c626e27e86554a7afac2cbfb2473ddad`
- Commit permalink: https://github.com/DomEscobar/agentic-runtime-techniques/tree/fad44983c626e27e86554a7afac2cbfb2473ddad
- Retrieved: 2026-08-08
- Repository license: MIT

## Reviewed artifacts

- `README.md`
- `docs/taxonomy.md`
- `docs/decision-guide.md`
- `docs/security-governance-patterns.md`
- `docs/2026-emerging-patterns.md`
- `docs/tier-list.md`
- `data/techniques.yml`
- `data/security-governance-patterns.yml`
- Claim, evidence, and source ledgers under `research/`

## Observation

The repository catalogs runtime mechanisms rather than frameworks alone. It
separates ten loop shapes from eight cross-cutting runtime layers and contains a
machine-readable catalog with 79 entries. Many entries cite primary sources,
but evidence strength ranges from established papers and official
specifications to individual recent preprints or implementation notes.

## Use rule

Definitions, categories, and tool references are treated as repository
observations. Tiers, benchmark values, and effectiveness statements remain
claims of that repository until the linked primary source is reviewed; only then
may they be promoted to independent knowledge-base claims.

## DomEscobar bauhelfer-ki

Canonical ID: `source-domescobar-bauhelfer-ki`  
Type: `source` · Privacy: `public` · Confidence: `0.55`  
Sources: none

# DomEscobar/bauhelfer-ki

- Repository: `DomEscobar/bauhelfer-ki` (private; not publicly resolvable)
- Reviewed commit: `6671de4277b57e6aa06c1cf06abdad43fd72ac20`
- Retrieved: 2026-08-08

## Auditability

This repository is private. The commit hash identifies the reviewed snapshot for
the repository owner, but no reader outside that account can retrieve the code,
re-run the review or contradict it. Everything below is therefore uncorroborated
first-party testimony in the sense of the evidence rubric, regardless of how
directly the artifacts were inspected.

Claims resting only on this source stay `provisional` at E1 and may not be
promoted to an accepted default. Where a claim also cites public evidence, the
public source carries the promotion and this page supplies implementation
detail only.

## Reviewed artifacts

- `RAG.md`, `RAG_METHODIK_2026.md`, `docs/RAG-DeepResearch-2026.md`
- `apps/api/src/services/ingestion.ts`
- `apps/api/src/services/retrieval.ts`
- `apps/api/src/providers/embeddings.ts`
- `apps/api/src/providers/reranker.ts`
- `apps/api/src/services/agent/contextAssembly.ts`
- `apps/api/src/services/agent/citations.ts`
- `apps/api/src/services/documentEvidence.ts` and related tests
- `apps/api/migrations/001_init.sql`
- Retrieval and offer evaluation harness under `eval/`

## Privacy boundary

The reviewed snapshot contained uploaded and parsed project artifacts under
`apps/api/data/`. They were neither evaluated as knowledge sources nor imported
into this knowledge base.

## Use rule

This page records an owner-reviewed private snapshot. It is not a public
implementation reference. Figures, rankings, and market comparisons in its
research documents remain repository claims and are promoted to general
recommendations only after independently auditable primary sources are reviewed.

## DomEscobar Eval-Oigl

Canonical ID: `source-domescobar-eval-oigl`  
Type: `source` · Privacy: `public` · Confidence: `0.55`  
Sources: none

# DomEscobar/Eval-Oigl

- Repository: `DomEscobar/Eval-Oigl` (private; not publicly resolvable)
- Reviewed commit: `b8d6a13d3220afb3f6ddc4d5f0e350f70142653f`
- Retrieved: 2026-08-09
- Language/toolchain: Go 1.23
- License: no LICENSE file was found in the reviewed commit; do not assume an
  open-source license.

## Reported state

The owner reported that `go test ./...` passed across all packages at the
reviewed commit. That result is not independently reproducible from this
knowledge base. Even if re-run, it would demonstrate internal test consistency,
not external validity of the evaluation metrics.

The snapshot is reported to implement an evaluation harness separated from the
system under test with:

- Versioned evaluation packs for targets, capabilities, cases, and manifest
- Complete pack, manifest, and configuration hashes
- Independent identities for the runtime and optional LLM judge
- Mechanical scorers for tool choice, arguments, forbidden tools, trace steps,
  grounding, terminal state, and budgets
- Causal linking of tool calls and observations through IDs
- Attempt receipts, campaigns, events, recovery, and read-only reports
- Separate full, targeted, and confirmation runs
- Explicit acceptance that rechecks pack hash, commit, coverage, scorers, and
  bindings

## Strong architecture decisions

1. The harness does not import the production runtime; HTTP/JSON is the boundary.
2. Evaluation semantics live in the versioned pack, not CLI defaults.
3. Mechanical evidence is checked before semantic plausibility.
4. A PASS is explicitly accepted only after separate confirmation.
5. Reports present persisted evidence but do not mutate a campaign.

## Limits and open risks

- A passing internal test run calibrates neither cases nor the LLM judge against
  human labels.
- One confirmation does not protect against stochastic flakiness; required
  repetitions must be determined empirically per slice.
- The pack model has no separate holdout/red-team management isolated from the
  optimizer.
- No universal trace should be imposed: alternative correct trajectories must
  remain valid while causal invariants are enforced.
- Live targets and judge endpoints can create cost or side effects; packs are
  therefore executable configurations that require review.
- This audit found no external outcome or judge validation.

## Auditability

This repository is private. The commit hash identifies the reviewed snapshot for
the repository owner, but no reader outside that account can retrieve the code,
re-run `go test ./...` or contradict the observations above. The passing test run
is reported, not independently reproducible.

Claims resting only on this source stay `provisional` at E1. The accepted claims
that cite this page also cite public evidence, which carries the promotion; this
page contributes design detail and a worked implementation, not proof.

## Evidence level

E1 as published evidence, because the artifacts are unavailable for external
audit. The implementation observations and passing repository tests would rate
E3 for the owner, and that gap is exactly what the private boundary costs.
General measurement validity remains E1 for everyone until OIGL is calibrated
against human-labeled trajectories, deliberately defective agents, and real
failure slices.

## Multilingual Embedding Evaluation Evidence 2025

Canonical ID: `source-embedding-evaluation-2025`  
Type: `source` · Privacy: `public` · Confidence: `0.91`  
Sources: none

# Multilingual Embedding Evaluation Evidence 2025

Primary sources checked on 2026-08-12:

- [MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/abs/2502.13595)
- [MTEB official benchmark documentation](https://docs.mteb.org/overview/)

## Evidence class

MMTEB is treated as E3: its public benchmark covers more than 500
quality-controlled tasks across more than 250 languages, including retrieval,
long-document and code tasks. The benchmark is broad and reproducible, but its
aggregate rankings are not application-specific evidence.

## Supported conclusion

Model size and a single leaderboard rank are poor selection rules. MMTEB reports
that a 560M-parameter multilingual E5 variant was the strongest public model in
its evaluated aggregate despite much larger alternatives winning some subsets.
This supports slice-aware evaluation, not adopting that model universally.

## Selection dimensions

- query and corpus languages, including code-switching;
- domain terminology and identifiers;
- query/passsage instruction format;
- passage length and truncation behavior;
- asymmetric query/document encoding;
- dense-only versus hybrid retrieval;
- embedding dimension, index size, throughput and licensing;
- hard negatives and temporal drift.

## Migration boundary

Changing an embedding model changes index identity. It requires a new index
manifest, paired replay, shadow or dual-read validation, migration cost
measurement and rollback. Never compare two embedders while silently changing
chunking, candidate depth or reranking.

## Embedding Selection and Migration Evidence Audit 2026-08

Canonical ID: `source-embedding-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.92`  
Sources: none

# Embedding Selection and Migration Evidence Audit 2026-08

## Primary evidence

- [MMTEB, ICLR 2025](https://openreview.net/forum?id=zl3pfz4VCV) evaluates more than 500 tasks and 250 languages. It supports slice-aware shortlisting, not universal adoption from an aggregate rank.
- [M3-Embedding, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.137/) evaluates dense, learned-sparse and multi-vector modes, multilingual and cross-lingual retrieval, and inputs up to 8,192 tokens.
- [ColBERTv2, NAACL 2022](https://aclanthology.org/2022.naacl-main.272/) supports token-level late interaction with compression, trading a larger index and scoring cost for fine-grained matching.
- [SPLADE v2, arXiv record for SIGIR 2021](https://arxiv.org/abs/2109.10086) supports learned lexical expansion with sparse inverted-index retrieval. Public code/model licensing must be checked separately.
- [DADA, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.825/) shows that target-domain distribution feedback can improve generative domain adaptation on BEIR; it does not make synthetic labels trustworthy by default.
- [Matryoshka-Adaptor, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.576/) and [SMEC, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1332/) support explicitly trained or adapted dimensional truncation. Arbitrary truncation of an incompatible model is unsupported.
- [MIPIC, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.676/) strengthens evidence that cross-dimension consistency is a training property, not a generic post-processing guarantee.
- [A Fresh Take on Stale Embeddings, ICML 2024](https://proceedings.mlr.press/v235/monath24a.html) demonstrates that stale target embeddings matter during retriever training. Production index migration remains an operational architecture question rather than a settled benchmark result.
- [Qdrant collection aliases](https://qdrant.tech/documentation/manage-data/collections/) document atomic alias changes as an implementation mechanism for reversible collection cutover. This is authoritative product documentation, not comparative evidence for the entire migration contract.

## Evidence boundary

Peer-reviewed benchmark and method results are E3. Model cards, provider documentation and the immutable-index/dual-read migration pattern are E2. Public leaderboards are discovery tools. They do not replace a private replay with fixed chunks, candidate depth, filters and reranking.

Long-input support, mixed-document OCR/visual fusion and compact single-vector image retrieval are capabilities or scoped benchmark observations. They remain E2 architecture candidates until length-, modality- and document-specific replay demonstrates end-to-end benefit.

## Selection controls

Always retain BM25 and the incumbent. Evaluate language, code-switching, domain terminology, identifiers, paraphrases, long passages, hard negatives and unanswerable queries separately. Record tokenizer, query/document instructions, normalization, dimension, truncation and model revision as index identity.

## Migration conclusion

Embedding spaces from different revisions are not assumed compatible. Build a new immutable index, verify manifest coverage, shadow or dual-read, run paired replay, rehearse rollback, then switch an alias. Never overwrite the champion vectors in place.

## Evaluation Consulting Research August 2026

Canonical ID: `source-evaluation-consulting-research-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.88`  
Sources: none

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

## Agent Evaluation Technique Evidence Audit August 2026

Canonical ID: `source-evaluation-techniques-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.89`  
Sources: none

# Agent Evaluation Technique Evidence Audit — August 2026

Primary sources checked on 2026-08-12:

- [Agentic Benchmark Checklist, 2025](https://arxiv.org/abs/2507.02825)
- [AgentRewardBench, 2025](https://arxiv.org/abs/2504.08942)
- [RAGChecker, NeurIPS 2024 Datasets and Benchmarks](https://arxiv.org/abs/2408.08067)
- [GroundEval, 2026](https://arxiv.org/abs/2606.22737)
- [Procedure-Aware Evaluation, 2026](https://arxiv.org/abs/2603.03116)
- [SWE-bench Live, 2025](https://arxiv.org/abs/2505.23419)
- [SWE-bench Illusion, 2025](https://arxiv.org/abs/2506.12286)
- [Sell Me This Stock: Unsafe Recommendation Drift in LLM Agents, 2026](https://arxiv.org/abs/2603.12564), narrow evidence for paired clean/manipulated tool-data replay in a financial workload.

## Evidence hierarchy

External state, executable tests, authorization logs and causal tool IDs are
stronger oracles than a plausible final answer. GroundEval and Procedure-Aware
Evaluation are recent E2 evidence for state- and process-aware scoring; their
specific results are not yet universal. AgentRewardBench supports calibrating
trajectory judges against expert labels, not trusting an unvalidated judge.

Public static benchmarks are useful development controls. SWE-bench Live and
SWE-bench Illusion reinforce the need for fresh executable tasks, duplicate
checks and private holdouts when making generalization claims. The Agentic
Benchmark Checklist shows that task and reward defects can distort rankings;
the evaluator itself therefore needs tests and adversarial negatives.

## Durable recommendation

Combine deterministic invariants with calibrated semantic judging only for
residual ambiguity. Report outcome, safety, causal grounding, process,
efficiency and robustness separately. Promotion requires paired comparison on
the same task/environment identities, repeated attempts, uncertainty, hard
regression gates and protected selection/holdout splits.

## Memory Operational Baselines and Tenancy Evidence Audit August 2026

Canonical ID: `source-memory-operational-baselines-and-tenancy-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.72`  
Sources: none

# Memory Operational Baselines and Tenancy Evidence Audit — August 2026

Primary sources checked on 2026-08-17:

- [ReFind raw-log memory retrieval](https://arxiv.org/abs/2608.12888)
- [Memory serving-cost study](https://arxiv.org/abs/2608.11879)
- [neo4j-agent-memory issue 155](https://github.com/neo4j-labs/agent-memory/issues/155)
- [Owner-scoped agent-memory-dotnet implementation](https://github.com/joslat/agent-memory-dotnet)

## Evidence boundary

ReFind and the serving-cost study are recent author-reported preprints without
public run artifacts at review time. Their numerical rankings and break-even
observations are not admitted as generally transferable results. ReFind is
useful counterevidence to selecting graph or tree memory without an equal-budget
immutable raw-log lexical baseline. The cost study supports stage-level
measurement, not a universal cost ordering.

Issue 155 is an unconfirmed public report whose detailed proof of concept is
not public. The separate .NET implementation demonstrates the plausibility of
owner-scoped controls but is not an independent reproduction of the reported
Neo4j failure. Treat cross-user graph poisoning as a threat hypothesis, not an
accepted product vulnerability.

## Durable recommendation

Compare memory candidates with an immutable event log searched by BM25 plus
temporal narrowing and bounded local expansion under the same model, prompt,
context and reranking budgets. Meter ingest, extraction, retrieval,
consolidation and answer generation separately and report cost per correct
answer. Shared graph memory must stamp and enforce owner or tenant scope on
nodes, edges, facts and derived summaries across read, write, merge, refresh,
consolidation, deletion and rebuild paths.

## Agent Memory Technique Evidence Audit August 2026

Canonical ID: `source-memory-techniques-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.88`  
Sources: none

# Agent Memory Technique Evidence Audit — August 2026

Primary sources checked on 2026-08-12:

- [MemGPT](https://arxiv.org/abs/2310.08560)
- [Generative Agents](https://arxiv.org/abs/2304.03442)
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)
- [Graphiti](https://arxiv.org/abs/2501.13956)
- [LongMemEval, ICLR 2025](https://openreview.net/forum?id=wIonk5yTDq)
- [MemBench, Findings ACL 2025](https://aclanthology.org/2025.findings-acl.989/)
- [Amory, EACL 2026](https://aclanthology.org/2026.eacl-long.183/)
- [CTIM-Rover negative result, REALM 2025](https://aclanthology.org/2025.realm-1.30/)
- [Memory poisoning study, 2026](https://arxiv.org/abs/2606.04329)
- [When Experience Hurts, ACL 2026](https://aclanthology.org/2026.acl-long.27/) provides a peer-reviewed negative result for uncritically reusing retrieved experience.
- [AgeMem, ACL 2026](https://aclanthology.org/2026.acl-long.981/) and [Memory-R1, ACL 2026](https://aclanthology.org/2026.acl-long.583/) evaluate learned memory-management mechanisms within their tested workloads.
- [Visual Inception, ACL 2026](https://aclanthology.org/2026.acl-long.954/) provides narrow peer-reviewed evidence for multimodal memory poisoning.

## Evidence boundary

The evidence distinguishes working context, immutable episodes, consolidated
semantic facts, temporally scoped relations and reusable procedures. No paper
establishes one universal memory architecture. Amory supplies peer-reviewed,
workload-specific evidence for narrative consolidation; CTIM-Rover is an
important negative result showing that retrieved episodes can add distracting
noise and reduce software-agent performance.

LongMemEval and MemBench support multi-session recall evaluation but cannot by
themselves prove correct writes, action selection, permissions or deletion.
Memory transformations are derived claims, not ground truth. They need lineage
to immutable source events, extractor identity, temporal validity and a
rebuildable index.

## Security and lifecycle conclusion

Untrusted content must not directly author preferences, permissions or
procedures. Write admission, quarantine and conflict handling are separate
from read ranking. Expiry, supersession, archival, index removal and verified
erasure are also distinct operations. Evaluate the full write-maintain-read-use
chain and include poisoned, stale, conflicting and irrelevant memories.

## Multimodal Document Retrieval Evidence 2025

Canonical ID: `source-multimodal-document-retrieval-2025`  
Type: `source` · Privacy: `public` · Confidence: `0.9`  
Sources: none

# Multimodal Document Retrieval Evidence 2025

Primary sources checked on 2026-08-12:

- [ColPali, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/99e9e141aafc314f76b0ca3dd66898b3-Abstract-Conference.html)
- [ColPali paper and ViDoRe benchmark](https://arxiv.org/abs/2407.01449)
- [ViDoRe artifacts](https://huggingface.co/vidore/collections)

## Evidence class

ColPali is E3 peer-reviewed evidence for page-level retrieval over visually rich
documents. ViDoRe spans several domains, languages and practical page retrieval
settings. It does not evaluate every downstream generator or operational stack.

## Mechanism

ColPali embeds page images with a vision-language backbone and uses late
interaction between query and visual patch representations. It can retrieve
layout, tables, figures and typography without first reducing the page to plain
text. The tradeoff is a larger multi-vector index and more expensive scoring
than a single-vector text retriever.

## Architecture boundary

Visual retrieval is a candidate-generation lane. It does not replace document
versioning, ACL filters, text/OCR extraction for exact citations, freshness,
reranking, answer grounding or end-to-end application replay. A practical
system can route visual-heavy queries to the visual lane and fuse those
candidates with lexical and dense text retrieval.

## Required evaluation

Measure page Recall@k and nDCG, evidence-region coverage, downstream answer and
citation correctness, index bytes per page, query latency, ingestion throughput
and modality-specific failure slices. Compare against text-only, OCR+text and
long-context baselines under the same corpus and query set.

## Multimodal RAG Evidence Audit 2026-08

Canonical ID: `source-multimodal-rag-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.91`  
Sources: none

# Multimodal RAG Evidence Audit 2026-08

## Primary evidence

- [ColPali, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/99e9e141aafc314f76b0ca3dd66898b3-Abstract-Conference.html) and ViDoRe provide peer-reviewed page-image late-interaction retrieval evidence across visually rich tasks, domains and languages.
- [Multimodal Chart Retrieval, NAACL 2024](https://aclanthology.org/2024.naacl-long.307/) directly compares OCR text, chart derendering to tables, direct image retrieval and fusion. There is no universal lane winner; the combined method is strongest in its setting.
- [TableRAG, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.710/) shows why flattening heterogeneous tables can destroy structure and evaluates query decomposition plus SQL execution for multi-hop table/text reasoning.
- [MIEB, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Xiao_MIEB_Massive_Image_Embedding_Benchmark_ICCV_2025_paper.html) broadens image-embedding evaluation and documents weaknesses with interleaved inputs and confounders.
- [M3DocVQA, ICCV Workshop 2025](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html) evaluates multi-page, multi-document retrieval and understanding; workshop evidence is useful but narrower than main-track replication.
- [FinRAGBench-V, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.211/) evaluates multimodal financial RAG with visual citation and makes citation localization an explicit end-to-end requirement.
- [Roles of MLLMs in Visually Rich Document Retrieval, IJCNLP-AACL 2025](https://aclanthology.org/2025.ijcnlp-long.2/) synthesizes captioning, embedding and end-to-end representation roles and their fidelity, latency and index-size trade-offs.
- [LAD-RAG, ACL 2026](https://aclanthology.org/2026.acl-long.724/) evaluates a symbolic layout graph alongside neural indexes for cross-page visually rich document retrieval.
- [Utility-Oriented Visual Evidence Selection, ACL 2026](https://aclanthology.org/2026.acl-long.1620/) evaluates evidence utility rather than similarity alone for bounded visual candidate selection.
- [Hybrid-Vector Retrieval, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.54/) evaluates single-vector first-stage efficiency combined with multi-vector accuracy.
- [Unified Multimodal Interleaved Document Representation, Findings EACL 2026](https://aclanthology.org/2026.findings-eacl.83/) evaluates document and passage retrieval for interleaved multimodal content.

## Evidence boundary

Peer-reviewed claims tied to the evaluated task are E3. New model repositories, vendor OCR, workshop-only systems and architecture inferences are E2. Page Recall@k does not establish answer correctness, exact numeric extraction, regional citation correctness or production latency.

## Architecture implications

Preserve page images and text/OCR identities. Put text, visual and structured-table lanes behind identical ACL and version filters. Fuse only after per-lane retrieval, deduplicate page hits, and retain coordinates or region identifiers through context assembly. Use exact extracted text for quotations and numbers even when visual retrieval found the page.

## Required slices

Evaluate clean prose, scans, forms, tables, charts, diagrams, slides, handwriting and mixed-language pages. Include visually similar wrong pages, correct text with wrong layout, OCR corruption, cross-page evidence, stale versions, hidden or redacted regions and questions whose answer is absent.

## Parser Landscape and Use-Case Audit August 2026

Canonical ID: `source-parser-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.87`  
Sources: none

# Parser Landscape and Use-Case Audit — August 2026

Primary sources checked on 2026-08-12:

- benchmarks: [OmniDocBench, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html), [ParseBench](https://arxiv.org/abs/2604.08538), [MPDocBench-Parse](https://arxiv.org/abs/2605.22100), [olmOCR-Bench](https://github.com/allenai/olmocr);
- local/native: [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/faq/index.html), [Apache Tika](https://tika.apache.org/3.0.0/formats.html);
- local multi-format: [AnyDoc](https://github.com/firecrawl/anydoc), [Microsoft MarkItDown](https://github.com/microsoft/markitdown), [Xberg, formerly Kreuzberg](https://github.com/xberg-io/xberg), [pdfplumber](https://github.com/jsvine/pdfplumber);
- local pipelines and VLMs: [Docling](https://docling-project.github.io/docling/usage/), [MinerU](https://github.com/opendatalab/MinerU/blob/master/docs/en/index.md), [Marker](https://github.com/datalab-to/marker/blob/master/README.md), [olmOCR](https://github.com/allenai/olmocr), [PaddleOCR](https://www.paddleocr.ai/main/en/version3.x/algorithm/PP-StructureV3/PP-StructureV3.html), [Unstructured](https://unstructured.readthedocs.io/en/latest/best_practices/table_extraction_pdf.html);
- managed: [LlamaParse](https://developers.api.llamaindex.ai/api/python/resources/parsing/methods/create/), [Mistral OCR](https://docs.mistral.ai/studio-api/document-processing/basic_ocr), [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-3.1.0), [Google Document AI](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk), [Amazon Textract](https://aws.amazon.com/documentation-overview/textract/).

## Evidence interpretation

Official documentation is E2 evidence for supported mechanisms, formats and
deployment options—not comparative accuracy. OmniDocBench is E3 benchmark
evidence. ParseBench, MPDocBench-Parse and current vendor/project benchmarks are
E2 pending peer review or independent replication. ParseBench's main finding is
more useful than its leaderboard: capability is fragmented and no method is
consistently strong across tables, charts, formatting, faithfulness and visual
grounding.

## Parser families

- **Native extraction:** cheapest and fastest for born-digital files; weak when
  reading order or visual structure is not encoded correctly.
- **Modular layout/OCR pipeline:** inspectable stages and local deployment;
  detector/OCR/table errors can cascade but are diagnosable.
- **End-to-end VLM:** often stronger on visually difficult pages and natural
  reading order; requires GPU/API capacity and can generate plausible structure.
- **Managed document AI:** low operational burden and specialized form/table
  features; adds data-boundary, pricing, version-drift and lock-in concerns.

## Selection rule

Route by document slice rather than selecting one global parser. Preserve a
native fast path for clean text, a structured local path for layout-heavy pages,
and an expensive VLM/API fallback for hard cases. Every candidate is evaluated
on identical pages with field fidelity, reading order, table/figure/formula
structure, downstream retrieval/citation correctness, latency, cost and failure
rate. Parser changes always create a new immutable parse and index identity.

## Important non-comparability

Benchmark versions, page subsets, rendering DPI, prompts, model revisions,
hardware and output normalization materially change results. Project-owned
leaderboards are useful discovery evidence, not proof that their own parser is
best for a private corpus. Licensing and residency must be checked at adoption
time rather than inferred from model weights or SDK licences.

## Multi-format converter addendum

AnyDoc is a distinct useful class: a pure-Rust, local, non-ML converter for Word,
PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV and text-based PDF. It normalizes
these formats through a shared document model into GitHub-Flavored Markdown and
also exposes Node, Python, Rust and browser-WASM bindings. Image-only PDFs are an
explicit unsupported case and require routing to OCR. Its published 100-document
benchmark is project-owned, uses an undistributed corpus and an LLM judge, so its
quality and speed claims remain E2 until independently reproduced.

MarkItDown is a lightweight Python conversion layer across office documents,
PDF, images, audio, HTML, archives and other formats. Local converters can be
augmented by plugins, vision models or Azure services. Its permissive conversion
entry point can access local or remote resources with process privileges, so
untrusted ingestion must use narrow byte/stream APIs and URI restrictions.

Xberg (formerly Kreuzberg) is a Rust-core polyglot document-intelligence framework
covering documents, office formats, images, email, archives, academic formats and
code. It supports multiple OCR/VLM backends, plugins, CLI, libraries, REST and MCP.
These broad capability claims are project documentation, and its Elastic License
2.0 requires a commercial-use review before adoption.

pdfplumber remains a valuable narrow instrument for machine-generated PDFs when
character, line, rectangle and table geometry or visual table debugging matter.
Its documentation explicitly says it works best on machine-generated rather
than scanned PDFs; it is not an OCR fallback.

Pandoc, Mammoth and headless LibreOffice remain converter or rendering fallbacks,
not general parser cards. They may be evaluated for their specific native formats,
but they do not replace OCR, layout analysis or visual document understanding.

## Public AI Architect Validation Artifacts August 2026

Canonical ID: `source-public-ai-architect-validation-2026-08`  
Type: `source` · Privacy: `internal` · Confidence: `0.96`  
Sources: none

# Public AI Architect Validation Artifacts — August 2026

Local primary artifacts inspected on 2026-08-12:

- `public-ai-architect/test/live-multiturn.mjs`
- `public-ai-architect/test/live-visual-diagram.mjs`
- `public-ai-architect/test-artifacts/live/`
- `public-ai-architect/src/server.mjs`
- `public-ai-architect/content/public-wiki.manifest.json`

## Reproduced technical result

The live visual run completed with eight nodes, eight edges, three groups, no
browser-console errors, a white diagram canvas, all node rectangles visible,
and mobile horizontal overflow. Fullscreen opacity/background/position and
title/group non-overlap were asserted. The runtime suite passed 9/9 tests,
dependency audit reported zero known vulnerabilities, and container health was
`healthy` at the time of the run.

## Semantic result and limits

A three-turn live architecture discussion completed without streaming errors
and retained context. Manual review found an unrealistic zero-percent
false-negative gate and a shortened invalid Knowledge Base citation. Therefore
runtime and UI readiness are demonstrated; semantic reliability, citation
correctness and calibrated architecture advice are not.

## Evidence class

E3 for the exact local technical checks because scripts and artifacts are
re-runnable. E1/E2 for general answer quality because the manually reviewed
sample is tiny and lacks blinded annotation or a calibrated judge.

## RAG Architecture Search Evidence 2026

Canonical ID: `source-rag-architecture-search-2026`  
Type: `source` · Privacy: `public` · Confidence: `0.82`  
Sources: none

# RAG Architecture Search Evidence 2026

Primary sources checked on 2026-08-12:

- [RAISE: RAG Design as an Architecture Search Problem](https://arxiv.org/abs/2605.30029)
- [AutoRAGTuner](https://arxiv.org/abs/2605.02967)
- [GEPA](https://github.com/gepa-ai/gepa)

## Evidence class

RAISE and AutoRAGTuner are recent preprints and therefore E2. They directly
support modular, configuration-driven and budgeted RAG optimization, but do not
establish a production standard. GEPA is supporting evidence for reflective
candidate proposal and selection.

## Strongest direct observation

RAISE standardizes search spaces and budgets, implements 13 search algorithms,
and evaluates seven text and multimodal datasets with three random seeds. Its
important result for architecture practice is negative: optimizer performance
is task-dependent, so aggregate rankings do not establish a universal winner.

AutoRAGTuner supports declarative component registration and Bayesian
optimization across pipeline configurations. Its reported reduction in code
churn is author-reported framework evidence, not a quality guarantee.

## Production implication

Treat architecture search as controlled experimentation over a typed manifest.
Freeze evaluator meaning during a promotion epoch, compare candidates under the
same dataset and budgets, repeat ambiguous comparisons, reject hard-gate
regressions, and keep an immutable champion plus rollback path.

## RAG Developments 2026 Research Batch 1

Canonical ID: `source-rag-developments-2026-batch-1`  
Type: `source` · Privacy: `public` · Confidence: `0.9`  
Sources: none

# RAG Developments 2026 — Research Batch 1

Primary sources reviewed on 2026-08-08:

- Anthropic Contextual Retrieval:
  https://www.anthropic.com/engineering/contextual-retrieval
- Microsoft GraphRAG publications:
  https://www.microsoft.com/en-us/research/project/graphrag/publications/
- Microsoft LazyGraphRAG:
  https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/
- LightRAG paper: https://arxiv.org/abs/2410.05779
- LightRAG repository: https://github.com/HKUDS/LightRAG
- HippoRAG: https://arxiv.org/abs/2405.14831
- HippoRAG 2: https://arxiv.org/abs/2502.14802
- Self-RAG: https://arxiv.org/abs/2310.11511
- Corrective RAG: https://arxiv.org/abs/2401.15884
- Azure agentic retrieval:
  https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept
- Azure API maturity:
  https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-migrate
- ColPali: https://arxiv.org/abs/2407.01449
- mixed text/table retrieval comparison:
  https://arxiv.org/abs/2604.01733
- RAG versus long-context benchmark: https://arxiv.org/abs/2502.09977

## Claim audit

### Contextual Retrieval

Anthropic reports that prepending 50–100 token, document-aware context to chunks
before both embedding and BM25 indexing reduced top-20 retrieval failures by 49%
on its evaluated corpora; adding reranking yielded a 67% reduction. These are
relative reductions on Anthropic's evaluation setup, not guaranteed downstream
answer gains. Anthropic also recommends full-context prompting as a baseline for
knowledge bases below roughly 200k tokens when economics permit.

### Hybrid plus reranking

A 2026 financial text/table benchmark with 23,088 queries reports hybrid
retrieval plus neural reranking as its best tested two-stage pipeline, while BM25
beat dense-only retrieval for precise financial content. This supports a strong
baseline for similar document workloads, not a universal law across domains.

### Graph techniques are heterogeneous

- Microsoft GraphRAG extracts entity/relationship graphs and hierarchical
  community summaries, targeting global corpus questions.
- LazyGraphRAG defers LLM work to query time and uses noun-phrase co-occurrence
  plus iterative relevance testing. Microsoft's cost/quality figures are from
  its own 5,590-article, 100-synthetic-query evaluation with LLM pairwise judges.
- LightRAG combines graph and vector representations with low/high-level query
  modes and incremental updates. The current repository has grown well beyond
  the original paper into a substantial server and multimodal ecosystem.
- HippoRAG uses a knowledge graph and Personalized PageRank for associative and
  multi-hop retrieval. HippoRAG 2 adds passage integration and online LLM use.

No single “GraphRAG” score should be transferred between these mechanisms.

### Agentic and corrective techniques

Self-RAG trains a model to emit reflection tokens controlling retrieval,
relevance and generation critique. It is not merely a prompt loop around an
arbitrary hosted model. CRAG instead places a retrieval-quality evaluator in a
pipeline and routes between acceptance, corrective decomposition/recomposition
and web augmentation. Azure agentic retrieval is a managed multi-query pipeline;
its minimal extractive API is stable in `2026-04-01`, while message planning,
answer synthesis and additional features remain in `2026-05-01-preview`.

### Visual retrieval

ColPali directly embeds document page images into multi-vector representations
and scores them with late interaction. It targets retrieval over visually rich
pages and avoids an OCR-first dependency for candidate generation. It does not
by itself produce structured table values, execute calculations, enforce ACLs or
guarantee grounded final answers.

### Long context

Long context is a required baseline, not the automatic successor to RAG. The
appropriate choice varies with corpus size, repeated-query economics, evidence
density and query type. Routing among full context and retrieval should be
measured; existing benchmarks do not establish one silver bullet.

## RAG Developments 2026 Research Batch 2

Canonical ID: `source-rag-developments-2026-batch-2`  
Type: `source` · Privacy: `public` · Confidence: `0.86`  
Sources: none

# RAG Developments 2026 — Research Batch 2

Primary sources reviewed on 2026-08-08:

- RAG paradigm scaling study: https://arxiv.org/abs/2607.26497
- MarginMerge: https://arxiv.org/abs/2608.02969
- InfoGain-RAG: https://aclanthology.org/2025.emnlp-main.365/
- REFRAG: https://arxiv.org/abs/2509.01092
- Search-R3: https://arxiv.org/abs/2510.07048
- R3-RAG: https://arxiv.org/abs/2505.23794
- ReSearch: https://arxiv.org/abs/2503.19470
- Chain-of-Retrieval Augmented Generation: https://arxiv.org/abs/2501.14342
- CORAG cost-constrained retrieval: https://arxiv.org/abs/2411.00744
- GraphRAG-Bench: https://openreview.net/forum?id=i9q9xDMjG7
- T2-RAGBench: https://aclanthology.org/2026.eacl-long.8/

## Claim audit

### Scaling evidence

The 2026 scaling study compares lexical, dense, graph-based and file-system
agent paradigms over 28 nested corpus tiers from about 1,000 to 512,000
documents. In that controlled setting, BM25 occupied the low-cost Pareto edge at
all measured tiers and led accuracy from mid-scale onward. A raw file-system
agent degraded at scale, while replacing its file navigation with BM25 produced
the strongest full-scale result reported by the study.

This is important evidence, not a universal ranking. The study holds 150
questions, relevant/adversarial bedrock documents, reader and judging protocol
fixed. Its result may not transfer to semantic paraphrase-heavy, multilingual,
visual or relation-centric workloads. It establishes BM25 and Agent+BM25 as
mandatory scaling baselines.

### Visual index compression

MarginMerge compresses the patch embeddings stored by frozen multi-vector
visual retrievers. Across six datasets and two backbones, its authors report
retaining 97–99% of average nDCG@5 while removing 90–95% of stored document
vectors. It does not compress source files, replace the VLM generator or prove
equivalent end-to-end answer quality. The preprint was released on 2026-08-04;
independent replication and operational latency measurements are still absent.

### Generation-aware evidence selection

InfoGain-RAG defines document information gain using the change in a generator's
confidence with versus without a document, then trains a reranker from that
signal. This is a generator-conditioned utility objective rather than ordinary
query-document relevance. Reported gains are benchmark- and generator-specific;
the method adds costly counterfactual scoring during data construction and can
inherit generator calibration errors.

CORAG uses Monte Carlo Tree Search to select correlated chunk combinations under
a cost budget. This is context-set optimization, not the same method as
Chain-of-Retrieval Augmented Generation, which iteratively reformulates queries.

### Efficient decoding is not retrieval compression

REFRAG exploits sparse/block-structured attention over retrieved passages to
compress, sense and selectively expand context during decoding. The authors
report large time-to-first-token and context-capacity improvements. It changes
model inference and KV-cache behavior; it does not improve candidate recall,
reduce the retrieval index, or substitute for context selection. Deployment
requires model/runtime integration and independent validation on the target
hardware.

### Learned retrieval policies

Search-R3 trains an LLM to reason and emit retrieval embeddings. R3-RAG and
ReSearch use reinforcement learning to interleave reasoning and search. These
are trained policies, not prompt-only agent loops. They offer evidence that
retrieval behavior can be optimized against downstream outcomes, but introduce
training-data, reward-hacking, reproducibility and corpus-transfer risks.

### Evaluation

GraphRAG-Bench tests graph-oriented retrieval and generation under domain and
question slices; T2-RAGBench targets mixed text/table evidence. Both improve
coverage over generic QA sets, but neither replaces application-specific replay.
Retrieval, evidence packing and answer generation need separate metrics because
improvements at one stage need not survive downstream.

## RAG Research and Practitioner Radar August 2026

Canonical ID: `source-rag-radar-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.84`  
Sources: none

# RAG Research and Practitioner Radar — August 2026

This radar separates research evidence, product capability, technical guidance
and practitioner testimony. It does not infer adoption or superiority from news
volume, GitHub stars or repeated vendor narratives.

## Evidence-bearing research

### Text and table retrieval — E3

The T2-RAGBench study compares retrieval methods on 23,088 financial text/table
queries. Hybrid retrieval followed by neural reranking was its strongest tested
two-stage pipeline; BM25 beat dense-only retrieval for precise content.

Source: https://arxiv.org/abs/2604.01733

Boundary: one domain and document/query distribution. It supports workload
testing, not “hybrid always wins.”

### Multi-domain conversational QA — E3

An EACL 2026 comparison reports that relatively simple hybrid/reranking/HyDE
methods can outperform vanilla RAG across its conversational QA setup.

Source: https://aclanthology.org/2026.eacl-srw.17/

Boundary: performance is method-, model- and benchmark-specific; “advanced” is
not synonymous with better.

### Biomedical retrieval comparison — E2

A 250-question controlled study compares dense, hybrid, cross-encoder reranking,
multi-query and MMR. Cross-encoder reranking leads its composite score, but the
dense baseline is only 0.005 behind; multi-query lowers contextual precision.

Source: https://arxiv.org/abs/2605.02520

Boundary: preprint, small domain sample, and several metrics use LLM evaluation.
The useful result is the negative one: extra retrieval stages can add noise.

### Corpus-scale paradigm comparison — E2/E3

The 28-tier scaling study finds BM25 on the low-cost Pareto edge and Agent+BM25
strong at full scale under its fixed 150-question protocol.

Source: https://arxiv.org/abs/2607.26497

Boundary: recent preprint without independent replication. Keep lexical search
as a mandatory control; do not declare a universal winner.

### Multi-turn RAG evaluation — E3

SemEval 2026 Task 8 establishes a shared multi-turn setting and documents
systems using rewriting, sparse/dense retrieval, fusion and reranking.

Sources:

- https://aclanthology.org/2026.semeval-1.447/
- https://arxiv.org/abs/2605.12028

Boundary: competition results demonstrate performance on the task, not an
off-the-shelf production architecture.

## Product and engineering developments

### Google agentic RAG — E2 product/research claim

Google Research describes a multi-agent enterprise workflow that decomposes
multi-source, multi-hop questions and iteratively searches for sufficient
context.

Source: https://research.google/blog/unlocking-dependable-responses-with-gemini-enterprise-agent-platforms-agentic-rag/

What it establishes: a concrete managed capability and design direction.
What it does not establish: vendor-neutral superiority, cost effectiveness or
transfer to simple lookup workloads without a comparable public evaluation.

### Azure agentic retrieval — E2 product claim

Azure exposes query planning and parallel subquery execution over search
indexes. Stable and preview surfaces must be tracked separately.

Sources:

- https://learn.microsoft.com/en-us/azure/search/search-agentic-retrieval-concept
- https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-migrate

### Oracle production-evaluation guidance — E1/E2

Oracle's July 2026 engineering article recommends comparing keyword, vector, SQL
and hybrid paths against application questions rather than choosing features by
reputation.

Source: https://blogs.oracle.com/developers/production-rag-evaluation-keyword-vector-sql-or-hybrid-search

Value: concrete evaluation framing. Limitation: vendor blog, not comparative
scientific evidence.

## Voices and counter-signals — E1

Recent practitioner discussions contain both “hybrid/reranking helped more than
model swaps” and measured counterexamples where reranking or hybrid fusion
reduced retrieval scores. These reports are not proof, but they invalidate any
unqualified default claim and create useful eval slices.

Sources:

- production failure discussion:
  https://www.reddit.com/r/Rag/comments/1u88gi7/
- reranker counterexample over 10,000 queries:
  https://www.reddit.com/r/Rag/comments/1vbnqj3/
- hybrid/reranking counterexample and workload conditions:
  https://www.reddit.com/r/Rag/comments/1v7g3oe/
- complex-PDF production lessons:
  https://www.reddit.com/r/Rag/comments/1v46rni/

Hypotheses to test:

- candidate depth and truncation can make a reranker worse than its retriever;
- small curated corpora may not benefit from lexical fusion;
- exact identifiers, polarity, code and domain jargon need dedicated slices;
- reranking can mask but cannot repair ingestion, OCR and chunk-boundary errors;
- real-query drift and out-of-domain traffic dominate polished demo sets.

## Rejected or downgraded narratives

- “Hybrid plus reranking is the 2026 universal production baseline”: downgraded
  to a strong candidate baseline; counterexamples and domain variance exist.
- “Agentic RAG reduces hallucinations by 60%+”: rejected without a named task,
  denominator, comparator and independently auditable evaluation.
- “RAG is used by a large majority of production LLM applications”: rejected
  as an unsourced adoption statistic.
- “Latest framework support proves production maturity”: rejected; feature
  availability does not prove recovery, security, cost or quality.
- GitHub stars, trending rank and social excitement: E0 discovery signals only.

## Current synthesis

The leading development is not a single retriever. It is controlled routing over
heterogeneous evidence interfaces, with stage-local evaluation and explicit
operational budgets. The smallest credible default remains deterministic scope
filters plus lexical and/or dense baselines, measured fusion, optional reranking,
bounded evidence construction and claim-level verification. Graph, visual,
long-context and agentic paths are workload-specific branches.

## Retrieval, Reranking, and Context Assembly Evidence Audit August 2026

Canonical ID: `source-retrieval-context-landscape-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.9`  
Sources: none

# Retrieval, Reranking, and Context Assembly Evidence Audit — August 2026

Primary research checked on 2026-08-12:

- [BEIR, NeurIPS Datasets and Benchmarks 2021](https://openreview.net/forum?id=wCu6T5xFjeJ)
- [Dense Passage Retrieval, EMNLP 2020](https://aclanthology.org/2020.emnlp-main.550/)
- [Reciprocal Rank Fusion, CIKM 2009](https://doi.org/10.1145/1571941.1572114)
- [Query2doc, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.585/)
- [HyDE, ACL 2023](https://aclanthology.org/2023.acl-long.99/)
- [IRCoT, ACL 2023](https://aclanthology.org/2023.acl-long.557/)
- [Cross-encoding reranking, DialDoc 2022](https://aclanthology.org/2022.dialdoc-1.13/)
- [Joint Passage Ranking for diverse evidence, EMNLP 2021](https://aclanthology.org/2021.emnlp-main.560/)
- [Maximal Marginal Relevance, SIGIR 1998](https://doi.org/10.1145/290941.291025)
- [RECOMP, ICLR 2024](https://openreview.net/forum?id=mlJLVigNHp)
- [LongLLMLingua, ACL 2024](https://aclanthology.org/2024.acl-long.91/)
- [Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9/)
- [ALCE citation evaluation, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.398/)
- [Attributable to Identified Sources, Computational Linguistics 2023](https://aclanthology.org/2023.cl-4.2/)
- [Self-RAG, ICLR 2024](https://openreview.net/forum?id=hSyW5go0v8)
- [SemEval 2026 multi-turn retrieval system](https://aclanthology.org/2026.semeval-1.225/)
- [MTRAGEval organizer paper, SemEval 2026](https://aclanthology.org/2026.semeval-1.447/)
- [S2G-RAG, ACL 2026](https://aclanthology.org/2026.acl-long.1185/)
- [Mixture of Retrievers, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.601/)
- [Abstain-QA, COLING 2025](https://aclanthology.org/2025.coling-main.627/)

## Evidence classes

Peer-reviewed benchmark and mechanism papers are E3 for the workloads they
actually evaluate, not universal production guarantees. Metadata and permission
filtering is an architectural invariant but lacks a single comparable benchmark,
so its operational card remains E2. Multi-query expansion and hard abstention
also remain E2: positive mechanisms exist, but recent controlled task evidence
shows query expansion can degrade precision, and evidence-sufficiency thresholds
are strongly application- and risk-dependent.

## Supported conclusions

BM25 remains a mandatory, inspectable control, especially for identifiers and
domain terms. Dense retrieval addresses vocabulary mismatch, while deterministic
rank fusion can combine complementary lexical and dense candidate sets without
requiring comparable score scales. Neither dense nor hybrid is a universal winner:
BEIR shows large dataset-to-dataset variation and the 2026 SemEval system reports
that more complex multi-query variants degraded its development results.

Reranking only reorders candidates that first-stage retrieval found. Cross-encoders
can improve relevance ordering but add pairwise compute and can suppress necessary
diversity. MMR-like selection trades some individual relevance for novelty; this is
useful for multi-facet evidence, not as a default for single-answer questions.

Query rewriting, decomposition and iterative retrieval should be routed to the
failure they address. Query2doc and HyDE improve selected zero-shot retrieval
settings, but generated expansions can inject false anchors. IRCoT supports
interleaved retrieval for multi-hop questions; it does not justify an agent loop
for direct lookup.

Context compression and sentence selection can reduce tokens and distractors.
RECOMP and LongLLMLingua provide peer-reviewed evidence, while Lost in the Middle
shows why simply filling a long context can still fail. Compression is lossy:
qualifiers, negation, table structure and stable citation spans need explicit
retention checks and an uncompressed fallback.

ALCE and AIS establish that citation presence is weaker than attribution. A valid
citation must identify the evidence, support the attached claim and cover the
material claims in the answer. Abstention requires negative examples and calibrated
thresholds; a self-reported model confidence is not evidence sufficiency.

## Evaluation contract

Hold parser, chunks, corpus snapshot and permissions fixed while comparing the
retrieval stages. Report Recall@k curves, MRR or nDCG, required-evidence coverage,
unique evidence yield, ACL leakage, latency and cost. Then freeze the candidate
set when evaluating rerankers and freeze the ordered evidence when evaluating
compression or packing. Score answer correctness, unsupported-claim rate, citation
precision and recall, attribution entailment and calibrated abstention separately.
Use simple, multi-facet, multi-hop, exact-identifier, conversational, negative and
permission-boundary slices. No component may be promoted from aggregate answer
quality alone.

## Runtime Boundary Regression Evidence Audit August 2026

Canonical ID: `source-runtime-boundary-regression-evidence-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.8`  
Sources: none

# Runtime Boundary Regression Evidence Audit — August 2026

Primary advisories and maintainer reports checked on 2026-08-17:

- [Pydantic AI provider-file confused deputy](https://github.com/advisories/GHSA-h7p7-w5gc-xj3w)
- [Token Optimizer MCP command injection](https://github.com/advisories/GHSA-49mq-fc6q-3h46)
- [Token Optimizer MCP path traversal](https://github.com/advisories/GHSA-76pc-mqxp-3rq5)
- [Stata MCP newline command injection](https://github.com/advisories/GHSA-49m4-vp58-wgc9)
- [ContextForge DNS-rebinding SSRF](https://github.com/advisories/GHSA-9hgc-g3w5-67cm)
- [atomic-agents-stack dashboard path traversal](https://github.com/advisories/GHSA-rm43-82j9-r4mj)
- [Microsoft Agent Framework snapshot isolation issue](https://github.com/microsoft/agent-framework/issues/7683)
- [Microsoft Agent Framework checkpoint lineage issue](https://github.com/microsoft/agent-framework/issues/7647)
- [Microsoft Agent Framework pending-request restore issue](https://github.com/microsoft/agent-framework/issues/7618)

## Evidence boundary

The advisories establish affected and patched release ranges through upstream
provenance. They are not independent reproductions and do not show that schema
validation, a container or framework checkpointing is sufficient on its own.
The Microsoft reports are open maintainer-repository issues; they establish
release-specific adoption risks but do not demonstrate duplicate or omitted
external effects.

## Durable recommendation

Treat model- or client-controlled references and arguments as delegated
authority requests. Canonicalize and authorize the resolved object, path,
hostname and effect immediately before execution, and retain fixed-version
negative controls when an affected dependency is adopted. A checkpointing
runtime must pass immutable-snapshot, storage-read isolation, lineage,
serialization, upgrade and crash-around-effect tests on the exact release. Run
product-specific vulnerable/fixed replays only during adoption or when the
dependency is deployed; the architecture knowledge base retains the generic
failure contract rather than a permanent vulnerable-product test farm.

## Agent Runtime Mechanisms Evidence Audit August 2026

Canonical ID: `source-runtime-techniques-2026-08`  
Type: `source` · Privacy: `public` · Confidence: `0.88`  
Sources: none

# Agent Runtime Mechanisms Evidence Audit — August 2026

Primary sources and specifications checked on 2026-08-12:

- [ReAct, ICLR 2023](https://openreview.net/forum?id=WE_vluYUL-X)
- [Anthropic, Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [OpenAI Agents SDK: Human in the loop](https://openai.github.io/openai-agents-python/human_in_the_loop/)
- [Model Context Protocol specification, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)
- [Crab checkpoint/restore runtime, 2026](https://arxiv.org/abs/2604.28138)
- [CapLease durable authorization, 2026](https://arxiv.org/abs/2608.01710)
- [AgentTrust runtime interception, 2026](https://arxiv.org/abs/2605.04785)

## Evidence boundary

ReAct supports bounded interleaving of reasoning and tool observations, but it
does not establish that an unconstrained loop is safe or superior for every
workflow. Anthropic's workflow taxonomy and the OpenAI SDK document concrete
implementations of routing, parallelization, evaluator loops, approvals and
resumable state; these are authoritative implementation observations rather
than independent comparative evidence.

Checkpointing conversation state is not equivalent to recovering external
side effects. Crab provides recent workload-bound evidence for aligning agent
turns with sandbox state. CapLease identifies durable authorization state and
an idempotent sink as requirements for replay-resistant side effects. Both are
fresh preprints and remain E2 for general production claims.

## Durable recommendation

Use the smallest loop that fits the task, explicit typed state, hard budgets,
runtime-generated causal IDs and deterministic completion checks. Risky tools
need least privilege and a pre-execution policy decision. Non-idempotent side
effects require an execution ledger or transactional boundary; chat replay and
a single-use call identifier are insufficient.

## VectifyAI PageIndex and Mafin 2.5 FinanceBench

Canonical ID: `source-vectifyai-pageindex`  
Type: `source` · Privacy: `public` · Confidence: `0.92`  
Sources: none

# VectifyAI PageIndex

## Primary artifacts

- PageIndex repository: https://github.com/VectifyAI/PageIndex
- inspected PageIndex commit: `d5c4e62c20172ce400aef84545dfba3a0580b9ae`
- permalink: https://github.com/VectifyAI/PageIndex/tree/d5c4e62c20172ce400aef84545dfba3a0580b9ae
- Mafin evaluation repository: https://github.com/VectifyAI/Mafin2.5-FinanceBench
- inspected Mafin commit: `1c890d5e0fd9929953d38282614555847727011d`
- FinanceBench paper: https://arxiv.org/abs/2311.11944
- accessed: 2026-08-08

PageIndex is MIT-licensed. At retrieval time on 2026-08-08 GitHub reported
35,072 stars, 3,078 forks and 150 open issues; popularity is not evidence of
retrieval quality.

## Observed OSS mechanism

The indexer parses PDF or Markdown into a hierarchical JSON structure containing
node IDs, titles, page/line ranges, optional summaries and children. PDF tree
construction uses TOC detection where possible and LLM-assisted generation,
alignment, verification and repair otherwise. A preview `flash` path uses
heuristics for structure extraction and an LLM for optional summaries.

The retrieval module exposes document metadata, a tree without full node text,
and raw content for selected page ranges. The included agentic demo lets an LLM
inspect structure and request pages. Thus the open-source package supplies tree
construction and retrieval tools; the agent policy and final generation remain
separate components.

## Claim audit

### Supported

- No embeddings or vector database are required by the OSS path.
- Natural document hierarchy and page ranges replace fixed embedding chunks.
- Selected pages and node IDs provide explicit navigation provenance.
- PDF and Markdown are supported; a vision cookbook and commercial enhanced OCR
  path are documented.
- PageIndex and hosted API/MCP/enterprise options exist as separate offerings.

### Needs qualification

- **“No chunking”:** there are no conventional vector chunks, but indexing and
  retrieval still partition content into nodes, page groups and page ranges.
- **“Two calls per query”:** not guaranteed by the OSS implementation. Agentic
  navigation can make a variable number of model/tool calls.
- **Indexing/query cost multipliers:** workload-, model- and document-dependent;
  no general 5–25× factor was established from the primary artifacts reviewed.
- **Millions of documents:** presented by VectifyAI for PageIndex File System;
  not established here as an independently reproduced capability of the basic
  OSS package.
- **MCTS:** advanced hosted/product descriptions must not be attributed to the
  minimal OSS retrieval module unless the corresponding code and license are
  identified.

## 98.7% FinanceBench audit

The Mafin repository publishes 150 answers for GPT-4o and 150 for DeepSeek-v3,
an LLM-judge script and manual labels for 14 disputed cases. This is materially
more transparent than a bare chart. However:

- the result is produced and reported by PageIndex/VectifyAI, not an independent
  replication;
- the judge prompt accepts supersets, inferred answers and reasonable subjective
  interpretations, making it permissive;
- six of 14 manually reviewed disputes are labelled benchmark errors and five
  multiple-valid-approach;
- the public repository contains outputs rather than the full Mafin pipeline,
  exact retrieval traces, cost/latency logs and a one-command end-to-end replay;
- FinanceBench itself is primarily single-document QA and its authors describe
  the public evaluation sample as 150 cases from a 10,231-question dataset.

Conclusion: 98.7% is a vendor-reported result with inspectable outputs and partial
evaluation transparency, not proof that PageIndex dominates hybrid RAG across
domains or workloads.

## Maturity and security observations

The inspected PageIndex commit has a small unit-test surface relative to the
pipeline and no root `SECURITY.md`. Open issues visible during review included
malformed JSON, Markdown edge cases and a missing security policy. The code now
contains delimiter-neutralization tests, which is useful but not a complete
prompt-injection or document-security boundary.

## Agent Evaluation Techniques

Canonical ID: `synthesis-agent-evaluation-techniques`  
Type: `synthesis` · Privacy: `internal` · Confidence: `0.88`  
Sources: `source-domescobar-eval-oigl`, `source-domescobar-agentic-eval-research`, `source-agent-evaluation-research-2026`

# Agent Evaluation Techniques

## What must be evaluated

Agent evaluation is not a single answer score. It spans:

1. task and dataset validity;
2. external outcome/state correctness;
3. safety, permissions and side effects;
4. evidence provenance and causal trace integrity;
5. routing, planning, recovery and termination diagnostics;
6. robustness under repeats and perturbations;
7. latency, calls, tokens and cost;
8. evaluator/judge reliability;
9. regression and promotion evidence.

## Technique ladder

Start with the cheapest reliable oracle and add ambiguity handling only where
needed:

```text
schema/invariant checks
 -> environment state and executable tests
 -> trace causality and forbidden-action gates
 -> reference/rubric scoring
 -> calibrated LLM judge
 -> environment-aware Agent-as-a-Judge
 -> human adjudication for disagreement/high risk
```

## Outcome versus process

Outcome decides whether the task succeeded. Process evidence diagnoses why and
enforces critical constraints. Process should become a decisive gate only for
safety, compliance, causal validity or an explicitly required mechanism.
Otherwise, demanding one reference trajectory can reject legitimate solutions.

## Online and offline loop

- **Offline:** frozen cases, repeats, perturbations, judge calibration,
  baseline comparison and hidden promotion gates.
- **Replay:** production-derived traces executed against versioned simulators or
  fixtures without reusing unsafe side effects.
- **Online:** sampled telemetry, deterministic invariants, canary comparison,
  user correction and incident capture.
- **Dataset maintenance:** cluster production failures, review new cases,
  monitor slice coverage and rotate exposed holdouts.

## Recommended OIGL next steps

1. Add explicit `development`, `selection`, `holdout` and `redteam` split
   contracts with information-flow tests.
2. Create an evaluator-validation pack containing known-good, known-bad,
   trace-tampered and ambiguous attempts.
3. Calibrate every LLM-judge rubric against human labels; record criterion-wise
   confusion and disagreement.
4. Add repeat-aware confidence and flakiness reporting instead of assuming one
   confirmation is sufficient.
5. Add environment snapshot/reset identity and separate infrastructure errors.
6. Treat eval-pack changes as metric-semantic changes requiring review and a
   new baseline lineage.
7. Add private project-local cases before making capability or improvement
   claims.

## Current verdict on OIGL

OIGL already has a stronger acceptance and provenance model than many basic
eval runners: mechanical-first scoring, pack identity, causal traces, receipts,
confirmation and explicit acceptance are implemented. The main missing layer
is not another scorer collection. It is empirical validation of the evaluator
itself, protected dataset splits, repeat statistics and environment-grounded
oracles on real project cases.

## Agentic Memory Architecture and Lifecycle

Canonical ID: `synthesis-agentic-memory-architecture`  
Type: `synthesis` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-agent-memory-foundations-2026`, `source-agent-memory-systems-2026`, `source-agent-memory-evaluation-security-2026`

# Agentic Memory Architecture and Lifecycle

## Definition

Agentic memory is a governed lifecycle, not a vector database:

`observe -> qualify -> write -> consolidate -> retrieve -> use -> verify/correct -> supersede/forget`

Memory must improve future decisions under explicit correctness, privacy,
latency and deletion constraints. Raw transcript accumulation is not memory.

## Storage classes

1. Run state: current plan, variables, permissions and commit state; loaded
   deterministically and checkpointed.
2. Event/action ledger: append-only observations, actions, outcomes and side
   effects with actor, time and provenance.
3. Episodic memory: compact, source-linked summaries of relevant events.
4. Semantic memory: versioned claims, preferences and constraints.
5. Procedural memory: verified workflows or skills with preconditions,
   dependencies, evidence and kill switch.
6. Entity-temporal memory: relations with event time, ingestion time and
   validity intervals; add only when relational queries justify it.
7. Derived indexes: lexical, vector and graph projections rebuilt from the
   canonical stores.

## Minimal reference architecture

```text
durable run state
  -> append-only event/action ledger
  -> extraction into quarantined candidates
  -> policy and evidence admission
  -> versioned fact store / verified skill registry
  -> optional temporal graph
  -> rebuildable lexical, vector and graph indexes
  -> retrieval policy enforcement and evidence packet
  -> outcome logging, correction, supersession and verified erasure
```

No single audited framework supplies every layer. Start with records and FTS;
add embeddings, graph structure or autonomous consolidation only after a
workload eval shows material benefit.

## Non-negotiable invariants

- Run state is not long-term personal memory.
- An extracted claim never replaces its source event.
- Add, amend, supersede and delete are distinct operations.
- Tenant, privacy and validity filters run before semantic ranking.
- Conflicts remain inspectable; materialized current truth is reconstructable.
- Procedures are executable artifacts and require stronger admission than facts.
- Delete covers canonical and derived artifacts and produces a verified receipt.
- Quality scores cannot compensate for privacy, safety or forbidden-side-effect failures.

## Agentic Runtime Techniques

Canonical ID: `synthesis-agentic-runtime-techniques`  
Type: `synthesis` · Privacy: `internal` · Confidence: `0.84`  
Sources: `source-domescobar-agentic-runtime-techniques`, `source-coding-agent-harness-and-skills-evidence-2026-08`

# Agentic Runtime Techniques

## Core claim

A runtime is not a single agent loop. The smallest useful architecture combines
exactly **one primary control loop** with the cross-cutting layers required by
risk, duration, and operating environment. More loops and more agents are not an
automatic improvement.

## A. Control loops

### 1. Action loop

`observe -> reason/plan -> act -> observe -> stop/repeat`

For short, interactive tool tasks. Requires tool contracts, error handling, a
stop condition, and hard budgets. Insufficient by itself for long-running,
irreversible, or correctness-critical work.

### 2. Plan and execute

`plan -> execute step -> observe -> revise -> next step`

For multi-stage work with visible progress. Store the plan as a versioned
artifact and detect stale plans. Do not use when the task is solvable in one
step or is primarily exploratory.

### 3. Verifier loop

`attempt -> deterministic check -> fix/finish/escalate`

For tasks with verifiable acceptance criteria. Tests, schemas, and invariants
take precedence over an LLM judge. Verifier independence and retry limits are
necessary because a weak checker legitimizes false completion.

### 4. Bounded retry

`bounded attempt -> explicit result/failure -> retry/fresh context/escalate`

Time, cost, step, and context limits make failure an explicit state. Transfer
only typed state between attempts; otherwise a fresh context carries the same
errors forward.

### 5. Reflection and memory

`act -> evaluate -> candidate lesson -> validate/promote -> reuse`

Reflections must not be written directly to canonical memory. Promotion requires
repeated evidence, provenance, expiry, and rollback.

### 6. Research loop

`question -> query batch -> read -> claim/evidence ledger -> gap analysis -> repeat`

The decisive runtime component is the claim/evidence ledger, not web access.
Stop when core claims are covered, the budget is exhausted, or no new evidence
appears.

### 7. Experiment loop

`propose -> isolated run -> measure -> paired comparison -> keep/revert`

Use only with a fixed baseline, controlled variance, and immutable experiment
log. One successful run is insufficient for promotion.

### 8. Multi-agent orchestration

`decompose -> typed tasks -> isolated workers -> typed results -> review/merge`

Use only when separate contexts, tools, authorities, or genuine parallelism
outweigh coordination cost. Bound depth, turns, and fan-out; make ownership and
merge semantics explicit.

### 9. Durable runtime

`load -> work -> checkpoint -> wait -> resume`

Requires a persistent state machine, idempotent steps, lease or single-runner
semantics, retry/backoff, migrations, and recovery semantics. A long chat turn is
not a durable workflow.

### 10. Coding harness

`isolate -> edit -> test -> review -> merge/revert`

Git diffs, worktree or branch isolation, executable checks, review, and rollback
form the runtime boundary. Without strong tests, even multi-agent review remains
weak. Project instructions carry stable facts, skills carry repeated procedures,
and hooks or CI enforce mechanical invariants. None of those prose surfaces
replace sandbox and capability policy. Apply the full design and evaluation
contract in [[project-coding-agent-harness]].

## B. Cross-cutting runtime layers

1. **Test-time compute:** generate multiple candidates only under a hard compute
   budget and with a reliable selector.
2. **HITL/governance:** model risky actions as resumable interrupts, not informal
   questions.
3. **Security/capabilities:** enforce trust zones, least privilege, and an action
   firewall before tool execution.
4. **Context/memory:** packing, paging, retrieval caps, promotion, and forgetting.
5. **Harness/composition:** separate the agent core from session, UI, queue, and
   persistence.
6. **Protocols:** use MCP/A2A only at boundaries that genuinely require
   portability or remote interoperability.
7. **Observability/provenance:** append-only events, run receipts, claim and
   artifact IDs, and replayable state transitions.
8. **Cost/serving:** budgets, model routing, caching, and latency SLOs as runtime
   policy rather than prompt suggestions.

## Composition rule

```text
request
  -> identity + trust classification
  -> capability + budget policy
  -> one primary control loop
  -> verifier / approval where required
  -> append-only events + checkpoints
  -> result with provenance
```

## Evidence status

The taxonomy is a useful synthesis but has not been experimentally validated as
a whole. Individual techniques have different evidence strength. In particular,
2026 patterns from isolated preprints remain hypotheses or candidates until
independent replication or local evaluations exist.

## Evaluation Workload Blueprints

Canonical ID: `synthesis-evaluation-workload-blueprints`  
Type: `synthesis` · Privacy: `internal` · Confidence: `0.89`  
Sources: `source-agent-evaluation-research-2026`, `source-evaluation-consulting-research-2026`

# Evaluation Workload Blueprints

## RAG

Corpus/snapshot identity, ACL tests, lexical/dense baselines, Recall@k/nDCG with
relevance sets, evidence coverage, claim support/citations, abstention,
staleness/contradiction, latency and cost. Measure ingestion, retrieval, context
and generation separately plus end to end.

## Tool agents

Outcome/state oracle, capability/arguments, forbidden actions, idempotency,
causal trace, recovery, terminal reason, budgets and permission attacks. A
plausible answer cannot replace the required external effect.

## Coding agents

Immutable task/repository, visible and hidden executable tests, regression,
forbidden evaluator files, diff scope, static checks, fresh/private tasks, cost
and reproducibility.

## Agentic memory

Write precision, recall, update/supersession, temporal validity, contradiction,
selective forgetting, privacy isolation, provenance and long-run utility. Test
the decision not to remember; retaining everything is failure.

## Multi-agent

Outcome, routing/delegation, authority, handoff, duplicate work/effects,
fan-out/cost, containment and recovery. Compare with a single-agent baseline.

## Conversation, multimodal and voice

Conversation needs multi-turn goal resolution, retention, correction,
clarification, escalation and efficiency. Multimodal adds layout/table/OCR and
perceptual grounding; voice adds transcription, speaker/noise/accent,
interruption and timing slices.

## High stakes

Add deterministic policy, approval/dual control, misuse and counterfactual
tests, audit completeness, fail-closed behavior, incident drills and rollback.
LLM-only judging cannot authorize irreversible effects.

## Current RAG Evidence August 2026

Canonical ID: `synthesis-rag-current-evidence-2026-08`  
Type: `synthesis` · Privacy: `internal` · Confidence: `0.86`  
Sources: `source-rag-developments-2026-batch-1`, `source-rag-developments-2026-batch-2`, `source-rag-radar-2026-08`

# Current RAG Evidence — August 2026

## What is holding up

- Exact/lexical retrieval remains a first-class baseline, especially for names,
  identifiers, numeric and terminology-heavy questions.
- Dense retrieval remains useful for paraphrase and semantic mismatch.
- Fusion and reranking often help, but only after candidate-depth, truncation,
  domain and latency tuning; they can regress quality.
- Structure-aware and visual retrieval address real failure classes that text
  chunks cannot recover after destructive parsing.
- Agentic retrieval earns its cost for decomposable multi-source and multi-hop
  queries, not routine fact lookup.
- Long context is an evaluated branch, not an excuse to skip evidence selection.
- Stage-local metrics plus final grounded task success are necessary; neither
  retrieval nor answer scores alone diagnose the system.

## Contested reranking and fusion benefit

The audited evidence disagrees about whether adding a reranking or fusion stage
reliably improves retrieval, and the disagreement is recorded rather than
averaged away.

For the added stage: the T2-RAGBench comparison over 23,088 financial text/table
queries found hybrid retrieval followed by neural reranking to be its strongest
tested two-stage pipeline, and the EACL 2026 conversational QA comparison found
hybrid, reranking and HyDE methods outperforming vanilla RAG.

Against the added stage: the 250-question biomedical controlled comparison put
cross-encoder reranking only 0.005 ahead of a dense baseline on its composite
score while multi-query lowered contextual precision, and practitioner reports
include a measured reranker counterexample over roughly 10,000 queries.

Neither side generalizes. The studies do not share a corpus, query distribution
or relevance protocol, so the comparison that would settle the question has not
been run. Treat the added stage as a measured candidate per workload, keep the
single-stage baseline as a control, and slice by candidate depth and truncation,
which is the mechanism both sides implicate.

## Recommended evaluation matrix

Every case should compare at least:

1. exact/SQL/metadata lookup where applicable;
2. BM25;
3. dense retrieval;
4. measured hybrid fusion;
5. the best candidate path with and without reranking;
6. long/full-context baseline when the corpus fits;
7. specialist branch only for its target slice.

Slice by exact identifiers, paraphrase, multi-hop, tables, visual layout,
negation/polarity, temporal freshness, conflicts, insufficient evidence,
cross-tenant attempts and corpus growth. Report Recall/nDCG, evidence coverage,
grounded task success, unsupported claims, latency and cost together.

## Architecture consequence

Use a query router only when the eval matrix identifies distinct winning paths.
Keep deterministic filters before probabilistic ranking. Preserve source-native
evidence and stable citation anchors. Put every expensive or learned branch
behind budgets, tracing, feature flags and a fallback to the simplest passing
baseline.

## Open questions

- How well do recent scaling results transfer to multilingual and multimodal
  corpora?
- When does generator-aware utility survive a generator/model upgrade?
- Can visual multi-vector compression retain answer quality on small-text and
  table-calculation slices?
- Which online signals detect retrieval drift without rewarding fluent but
  unsupported answers?
- What independent evidence exists for managed agentic-retrieval cost and
  reliability claims?

## RAG Pipeline Taxonomy

Canonical ID: `synthesis-rag-pipeline-taxonomy`  
Type: `synthesis` · Privacy: `internal` · Confidence: `0.9`  
Sources: `source-domescobar-bauhelfer-ki`, `source-vectifyai-pageindex`, `source-rag-developments-2026-batch-1`, `source-rag-developments-2026-batch-2`

# RAG Pipeline Taxonomy

## Why this split matters

“Use PageIndex”, “use GraphRAG” or “use a vector database” describes only part
of a system. RAG quality is an end-to-end property. We classify techniques by
the pipeline stage they change and evaluate both stage-local and final outcomes.

## 1. Ingestion and representation

Transforms source artifacts into retrievable units while preserving evidence.

- OCR and layout-aware parsing;
- tables, images and multimodal extraction;
- fixed, recursive, semantic or structure-aware segmentation;
- contextual headers and document summaries;
- entities, relations and knowledge-graph projection;
- PageIndex-style hierarchical document trees;
- versioning, deduplication, deletion and provenance.

Primary metrics: parse field accuracy, table fidelity, hierarchy accuracy,
coverage, duplication rate, index freshness and cost per document.

## 2. Retrieval and candidate generation

Finds potentially relevant evidence.

- metadata/ACL filtering;
- SQL and exact lookup;
- BM25/full-text/sparse retrieval;
- dense embedding retrieval;
- hybrid fusion such as RRF;
- multi-vector or late-interaction retrieval;
- PageIndex/tree navigation;
- graph traversal;
- query rewriting, decomposition and multi-query retrieval;
- iterative or agentic retrieval with stop conditions.

Primary metrics: Recall@k, Precision@k, MRR, nDCG, evidence coverage, diversity,
latency and cost. Retrieval must be evaluated before blaming generation.

## 3. Augmentation and context construction

Converts candidates into the evidence package actually shown to the model.

- reranking;
- deduplication and near-duplicate collapse;
- parent/neighbor expansion;
- section/page-window expansion;
- lost-in-the-middle ordering;
- diversity and sub-question coverage selection;
- compression and extractive evidence selection;
- contradiction detection;
- source trust, freshness and authority weighting;
- token-budget packing with stable citation anchors.

Primary metrics: context precision/recall, coverage per sub-question, token
efficiency, contradiction retention and citation-anchor validity.

## 4. Generation and answer contracts

Uses the evidence package to produce a bounded output.

- grounded prompts and explicit abstention;
- structured JSON/schema-constrained output;
- extract-then-synthesize;
- deterministic calculations outside the LLM;
- claim-level citations;
- assumptions, unknowns and conflicts as typed fields;
- answer decomposition and evidence-weighted synthesis;
- model routing by risk and complexity.

Primary metrics: field accuracy, faithfulness, unsupported claim rate, answer
relevance, calibration, completeness and cost.

## 5. Verification and control

Checks the output and decides whether to answer, retry or escalate.

- citation existence and entailment checks;
- deterministic business-rule validation;
- corrective retrieval when evidence is insufficient;
- cross-source corroboration;
- LLM judge only where deterministic checks are impossible;
- human approval for high-impact outputs;
- retry, latency and cost budgets.

Primary metrics: defect escape rate, false acceptance/rejection, abstention
quality, correction success and human-review load.

## 6. Evaluation and operations

- versioned golden datasets and realistic negative cases;
- stage-level ablations plus end-to-end replay;
- slices by document/query type, tenant, language and freshness;
- retrieval/generation traces with redaction;
- index manifests, canaries, feature flags and rollback;
- privacy, deletion and cross-scope leakage tests.

## Selection principle

Select one baseline per stage, then add complexity only where the error analysis
shows a bottleneck. For example, a reranker cannot repair missing OCR text, and
PageIndex cannot compensate for an incorrect page hierarchy. Likewise, strong
retrieval does not make an unconstrained generator safe.

## 2026 technique placement

- Contextual Retrieval changes **representation/indexing** and can improve both
  sparse and dense candidate generation.
- GraphRAG, LightRAG, HippoRAG and PageIndex are different **retrieval
  representations and traversal policies**, not generation methods.
- Rerankers, coverage selection and compression belong to **augmentation**.
- Self-RAG spans **retrieval control and generation** because reflection is part
  of a trained generator; CRAG primarily adds **verification and corrective
  routing** around retrieval.
- ColPali changes **multimodal candidate generation**; extraction and grounded
  generation still follow.
- Long context is a competing or complementary **context-construction baseline**
  and should participate in routing and evaluation.
- MarginMerge changes **visual index size**; InfoGain-RAG and CORAG change
  **candidate/context utility**; REFRAG changes **model inference**. Reporting
  all three merely as “compression” hides different costs and failure modes.
- RL-trained systems such as Search-R3, R3-RAG and ReSearch are **learned
  retrieval policies**, not generic agent prompts. They require reward,
  transfer, canary and rollback evaluation.

## Scale-aware default

BM25 is a mandatory control at every corpus tier. The 2026 controlled scaling
study makes a strong case for Agent+BM25 over raw file-system navigation at
large scale, but does not establish lexical retrieval as universally superior.
Use nested-corpus replay to identify the crossover for the actual query mix.

## Validated technique cards

### Adaptive or Mixture Chunking

Technique ID: `chunking.adaptive.mixture` · Stage: `segmentation` · Risk: `high`

Chooses among multiple chunkers or granularities using document features intrinsic metrics learned selection or query class rather than one global policy.

Use when: The corpus mixes structurally different document classes; Sufficient labeled replay exists to justify routing complexity

Avoid when: A single simple policy already meets all sliced gates; Selection features drift without monitoring and rollback

Failure modes: Router overfits visible development cases; Multiple indexes increase cost and operational drift; Selection errors hide behind aggregate metrics

Required evals: paired performance by document and query slice; router selection accuracy; index and ingestion cost; holdout generalization and rollback test

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Late Chunking

Technique ID: `chunking.contextual.late` · Stage: `segmentation` · Risk: `high`

Encodes a long document before pooling token representations into bounded chunk embeddings so each chunk vector retains surrounding document context.

Use when: Long-context embedding models are available; Local chunks lose essential document-level context

Avoid when: Documents exceed the embedding model context limit; The vector infrastructure cannot reproduce token-level pooling and model versions

Failure modes: Long documents are truncated or inconsistently segmented; Embedding model changes alter every chunk vector; Token pooling implementation mismatches tokenizer boundaries

Required evals: Recall@k on context-dependent queries; long-document coverage; embedding throughput and memory; reproducibility across model versions

Evidence: `E2` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Neighbor Expansion

Technique ID: `chunking.contextual.neighbor-expansion` · Stage: `segmentation` · Risk: `medium`

Retrieves fine source units and then adds a bounded number of immediately preceding and following units from the same document version.

Use when: Evidence often spans adjacent prose units; Source order and document-version links are reliable

Avoid when: Adjacent units cross ACL or topic boundaries; Retrieved hits already contain sufficient context

Failure modes: Irrelevant neighbors reduce precision; Expansion crosses structural or access boundaries; Multiple hits produce overlapping duplicate ranges

Required evals: evidence coverage gain; context precision loss; duplicate token rate; authorization and version-integrity tests

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Contextual Prefixing

Technique ID: `chunking.contextual.prefix` · Stage: `segmentation` · Risk: `high`

Generates or deterministically constructs a short document-aware explanation for each raw chunk and prepends it to dense and optionally sparse index representations.

Use when: Chunks contain ambiguous entities dates or section-local references; Document context can be added without violating access boundaries

Avoid when: Generated prefix claims cannot be verified; Ingestion cost or frequent document updates make regeneration impractical

Failure modes: Prefix invents or overstates context; Restricted metadata leaks into a broader index; Prefix dominates the original chunk embedding

Required evals: retrieval failure rate versus raw chunks; prefix entailment; access-control leakage tests; ingestion cost and token overhead

Evidence: `E2` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Recursive Boundary-Aware Split

Technique ID: `chunking.fixed.recursive-split` · Stage: `segmentation` · Risk: `medium`

Recursively tries coarse-to-fine separators such as sections, paragraphs, sentences and tokens until every unit satisfies a hard size limit.

Use when: A cheap boundary-aware baseline is needed; Documents contain ordinary prose separators but inconsistent hierarchy

Avoid when: Domain structures such as tables or AST nodes need dedicated handling; Separator rules are unreliable across the corpus languages

Failure modes: Long blocks fall back to arbitrary token cuts; Separator choice creates unstable chunk sizes; Headers remain separated from child content

Required evals: boundary integrity; size distribution; evidence Recall@k; index size and latency

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Sliding Window with Overlap

Technique ID: `chunking.fixed.sliding-overlap` · Stage: `segmentation` · Risk: `medium`

Creates fixed windows with repeated boundary tokens so evidence near a cut appears in more than one retrievable unit.

Use when: Boundary misses are measured in contiguous prose; Index duplication is affordable

Avoid when: Access controls or deletion semantics cannot tolerate duplicated text; Redundant retrieval already consumes context budget

Failure modes: Duplicate evidence crowds retrieval results; Index and embedding cost increase; Citation deduplication becomes ambiguous

Required evals: boundary evidence recall; duplicate hit rate; context precision; vector count and cost

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Fixed Token Window

Technique ID: `chunking.fixed.token-window` · Stage: `segmentation` · Risk: `medium`

Splits source text into deterministic token-count windows with an optional fixed overlap and no semantic boundary model.

Use when: A reproducible low-cost control is required; Source text has weak or unreliable structure

Avoid when: Tables code blocks or sections must remain indivisible; Answer evidence regularly crosses arbitrary window boundaries

Failure modes: Claims split across boundaries; Headings detach from their content; Large windows dilute retrieval similarity

Required evals: evidence Recall@k by query granularity; context precision; duplicate evidence rate; index size and ingestion latency

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Parent-Child Small-to-Big Retrieval

Technique ID: `chunking.hierarchical.parent-child` · Stage: `segmentation` · Risk: `medium`

Indexes fine child units for matching while linking each child to a larger parent section returned for generation and citation context.

Use when: Queries need precise matching but answers require broader context; Reliable parent boundaries and stable source identifiers exist

Avoid when: Parents exceed generation budgets or access boundaries; Child-to-parent mappings change frequently without versioned provenance

Failure modes: Large parents dilute context precision; Multiple child hits duplicate the same parent; Parent expansion crosses authorization boundaries

Required evals: child Recall@k; parent evidence coverage; deduplicated context precision; access boundary tests and token cost

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Hierarchical Summary Tree

Technique ID: `chunking.hierarchical.summary-tree` · Stage: `segmentation` · Risk: `high`

Clusters fine source units recursively and generates summary nodes at multiple levels so retrieval can select leaves or higher-level abstractions.

Use when: Questions synthesize evidence across long documents or abstraction levels; Generated summaries can remain linked to verifiable descendants

Avoid when: Summaries cannot be checked for unsupported claims; Frequent source updates make tree regeneration too expensive

Failure modes: Summary nodes hallucinate or omit critical details; Cluster boundaries mix unrelated evidence; Updates leave stale ancestor summaries

Required evals: multi-hop and synthesis answer completeness; summary entailment; leaf citation traceability; build cost and update consistency

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Document Tree Navigation

Technique ID: `chunking.hierarchical.tree-navigation` · Stage: `segmentation` · Risk: `high`

Builds a hierarchical table-of-contents-like tree with page ranges and summaries, then navigates nodes to select source pages instead of searching one flat vector-chunk index.

Use when: Long structured documents support human-like hierarchical navigation; Page-level provenance and synthesis are more important than millisecond flat retrieval

Avoid when: Documents lack reliable hierarchy; Claims of no chunking would hide generated summaries and node segmentation from evaluation

Failure modes: Generated tree omits or misroutes evidence; Navigation latency grows with depth; Page-level leaves remain too coarse for exact facts

Required evals: node routing recall; page and evidence coverage; end-to-end latency and model calls; tree faithfulness and citation correctness

Evidence: `E2` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Proposition Chunking

Technique ID: `chunking.semantic.proposition` · Stage: `segmentation` · Risk: `high`

Uses a language model to rewrite passages into atomic self-contained factual propositions that become fine-grained retrieval units linked to their source spans.

Use when: Queries target atomic facts hidden in dense passages; Fine retrieval granularity is worth higher ingestion cost

Avoid when: Exact source wording and qualifiers must never be rewritten; Claims depend on tables formulas or multi-sentence argument structure

Failure modes: Generated propositions omit qualifiers; Unsupported propositions enter the index; Vector count and ingestion cost multiply

Required evals: proposition entailment against source; fact Recall@k; qualifier preservation; vector count cost and citation traceability

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Semantic Similarity Chunking

Technique ID: `chunking.semantic.similarity` · Stage: `segmentation` · Risk: `high`

Embeds sentences or blocks and creates boundaries where adjacent semantic similarity drops below a configured threshold or change-point rule.

Use when: Topic transitions do not align with visible formatting; Offline compute is available for a measured candidate

Avoid when: A simple structure-aware baseline already meets the gates; Embedding drift would make boundaries operationally unstable

Failure modes: No consistent gain over fixed baselines; Embedding cost and model changes alter boundaries; Semantically related but structurally separate content merges

Required evals: paired Recall@k versus controls; boundary coherence; ingestion compute and latency; answer quality and citation correctness

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### AST-Aware Code Chunking

Technique ID: `chunking.specialized.code-ast` · Stage: `segmentation` · Risk: `medium`

Uses abstract syntax tree nodes to keep functions classes and other semantic code units intact, recursively splitting large nodes and merging bounded siblings.

Use when: Repositories contain supported parseable programming languages; Retrieval and generation depend on complete code structures

Avoid when: Files are generated malformed or unsupported by the AST parser; Cross-file dependency retrieval is required without symbol or graph expansion

Failure modes: Parser errors drop or misnest code; Large functions still require destructive splits; AST chunks omit cross-file dependencies

Required evals: RepoEval Recall@k; complete-symbol coverage; generation Pass@1; language coverage and parse failure rate

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Conversation Turn and Episode Chunking

Technique ID: `chunking.specialized.conversation-turn` · Stage: `segmentation` · Risk: `high`

Keeps speaker turns atomic and groups adjacent turns into bounded episodes using thread session time-gap or topic-transition signals.

Use when: Chat or support transcripts require speaker and temporal provenance; Questions refer to decisions or exchanges across nearby turns

Avoid when: Messages have independent ACL or retention policies that cannot be grouped; Topic boundaries cannot be inferred reliably and full-thread retrieval is cheap

Failure modes: Episodes combine unrelated topic shifts; Speaker metadata leaks or is misattributed; Edited or deleted turns invalidate grouped chunks

Required evals: speaker attribution accuracy; decision retrieval Recall@k; temporal and thread boundary integrity; privacy deletion and update tests

Evidence: `E2` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Structure-Aware Table Chunking

Technique ID: `chunking.specialized.table-aware` · Stage: `segmentation` · Risk: `high`

Treats table headers rows and key-value relationships as structural units, repeating necessary header context while packing complete rows under a token limit.

Use when: Questions depend on relationships between columns and rows; The parser provides reliable cell topology and header spans

Avoid when: Tables were flattened or misparsed upstream; Answers require visual chart interpretation rather than tabular relations

Failure modes: Parser topology errors become false relationships; Repeated headers inflate vectors; Rows split when a single record exceeds the limit

Required evals: cell and header relationship fidelity; table query Recall@k; numeric answer accuracy; token utilization and vector count

Evidence: `E2` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Paragraph and Section-Aware Chunking

Technique ID: `chunking.structural.section-aware` · Stage: `segmentation` · Risk: `medium`

Uses parsed paragraph and section boundaries as atomic units, merging small siblings and splitting oversized sections under a hard token cap.

Use when: Documents have trustworthy headings and paragraph structure; Section-level questions need author-defined context

Avoid when: Parser hierarchy is missing or incorrect; Single sections contain unrelated long content without substructure

Failure modes: Parser hierarchy errors become chunk errors; Oversized sections dilute similarity; Merged siblings cross topic boundaries

Required evals: section boundary integrity; fact and section Recall@k; context precision; answer completeness

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Sentence Window

Technique ID: `chunking.structural.sentence-window` · Stage: `segmentation` · Risk: `medium`

Indexes a sentence or small sentence group as the retrieval key while retaining a bounded number of adjacent sentences for answer context.

Use when: Questions target local claims or definitions; Sentence boundaries are reliable and neighboring context resolves references

Avoid when: Evidence is primarily tabular code-like or cross-sectional; Sentence tokenization is unreliable for the corpus language

Failure modes: Pronouns and qualifiers detach from antecedents; Neighbor expansion introduces irrelevant content; Abbreviations create false sentence boundaries

Required evals: fact retrieval Recall@k; reference resolution coverage; context precision; answer citation correctness

Evidence: `E3` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Markdown Title-Chain Chunking

Technique ID: `chunking.structural.title-chain` · Stage: `segmentation` · Risk: `medium`

Splits structured Markdown at heading boundaries and prepends the root-to-leaf heading path to each bounded content chunk.

Use when: Technical or policy documents have reliable nested headings; Repeated local terms require hierarchical disambiguation

Avoid when: Headings are noisy or synthetic; Prefixes could leak restricted parent metadata across access boundaries

Failure modes: Long title paths dominate short chunks; Generated or wrong headings bias retrieval; Prefix text contaminates relevance grading

Required evals: hierarchical query Recall@k; prefix token overhead; context precision; relevance scoring against raw source view

Evidence: `E2` from `source-chunking-landscape-2026-08`; reviewed `2026-10-12`.

### Post-Generation Attribution Verifier

Technique ID: `context.citation.attribution-verifier` · Stage: `context-assembly` · Risk: `high`

Resolves every cited stable identifier and verifies claim-to-span support and material-claim citation coverage after generation.

Use when: Answers make source-backed factual claims; Citations must be exact and auditable

Avoid when: No stable source-span identifiers exist; Verifier false rejects cannot be calibrated

Failure modes: Valid label points to the wrong version; Entailment judge accepts citation laundering; Strict verification over-rejects qualified claims

Required evals: citation precision and recall; human-labeled attribution entailment; stable-ID and version resolution; false-reject rate by claim type

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Claim-to-Evidence Citation Binding

Technique ID: `context.citation.binding` · Stage: `context-assembly` · Risk: `high`

Carries stable source and span identifiers through retrieval and requires each material answer claim to bind to evidence that entails it.

Use when: Answers synthesize external evidence; Users or auditors must verify claims against exact source regions

Avoid when: The task contains no external evidence; Stable source identities and retrievable spans cannot be preserved

Failure modes: Citation laundering attaches a relevant source to unsupported prose; Correct support is cited at the wrong span or version; Over-citation obscures which source supports which claim

Required evals: citation precision and recall; claim-level entailment or AIS; stable-ID version and span resolution; privacy and path-leakage checks

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Evidence-Preserving Context Compression

Technique ID: `context.evidence.compression` · Stage: `context-assembly` · Risk: `high`

Reduces retrieved passages with query-aware extractive or abstractive compression while retaining source anchors qualifiers and required claims.

Use when: Retrieved evidence exceeds the generation budget; Distractor text lowers answer quality despite adequate retrieval recall

Avoid when: Layout tables or long-range discourse carry the meaning; Omission risk is high and preservation cannot be verified

Failure modes: Negation dates or qualifiers are dropped; Abstractive compression invents unsupported synthesis; Citation anchors drift away from original spans

Required evals: required-claim and qualifier retention; citation-span validity and attribution; answer correctness under fixed retrieved evidence; tokens latency and compression fallback rate

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Missing-Evidence Abstention

Technique ID: `context.missing-evidence.abstention` · Stage: `context-assembly` · Risk: `high`

Applies an explicit evidence-sufficiency contract and returns bounded uncertainty or an approved escalation instead of unsupported completion.

Use when: Answers require external provenance or high-stakes grounding; Negative and unanswerable questions occur in production

Avoid when: The task explicitly permits unsourced general knowledge; No labeled negative cases exist to calibrate the threshold

Failure modes: Over-abstention suppresses supported answers; False sufficiency accepts merely related text; Hidden fallback to model memory violates the contract

Required evals: negative and unanswerable case precision; supported-answer recall; unsupported-claim rate; threshold calibration and fallback-policy sentinels

Evidence: `E2` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Position-Aware Evidence Packing

Technique ID: `context.selection.position-aware-packing` · Stage: `context-assembly` · Risk: `medium`

Deduplicates and orders required evidence under a token budget while protecting decisive spans from weak middle positions.

Use when: Long contexts bury relevant evidence; Multiple retrieved chunks duplicate the same source

Avoid when: Candidate recall is the actual bottleneck; The task needs original document layout rather than linear packing

Failure modes: Decisive evidence remains buried; Deduplication removes complementary qualifiers; Contradictory evidence is dropped

Required evals: required-evidence coverage by position; answer and citation correctness; duplicate and contradiction retention rates; token count and latency

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Sentence-Level Evidence Selection

Technique ID: `context.sentence.evidence-selection` · Stage: `context-assembly` · Risk: `high`

Selects query-relevant source sentences plus bounded adjacent context while retaining stable passage and character-span provenance.

Use when: Long textual passages contain small evidence-bearing regions; Extractive context reduction is preferred over generated summaries

Avoid when: Meaning depends on tables diagrams layout or long discourse; Sentence segmentation is unreliable for the corpus language or format

Failure modes: Selected sentences lose negation or antecedents; List and table semantics break at sentence boundaries; Repeated isolated sentences conceal document-level contradiction

Required evals: required-claim and qualifier retention; citation span correctness; context tokens and duplicate rate; layout-dependent and discourse-dependent failure slices

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Quantized Embedding Index

Technique ID: `embedding.compression.quantized-index` · Stage: `embedding` · Risk: `high`

Stores reduced-precision or product-quantized vectors and optionally rescoring a larger shortlist with higher-precision vectors.

Use when: Vector memory or ANN bandwidth is a measured bottleneck; A full-precision champion and paired ranking replay exist

Avoid when: The corpus is small enough for full precision; Rare-term or tail-language losses cannot be measured

Failure modes: Quantization changes nearest-neighbor order; Tail languages and hard negatives regress; Index and query precision contracts diverge

Required evals: paired Recall@k and nDCG; language and hard-negative slices; bytes per vector and total index size; p50 and p95 latency

Evidence: `E2` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Asymmetric Embedding Instruction Contract

Technique ID: `embedding.contract.asymmetric-instructions` · Stage: `embedding` · Risk: `high`

Pins distinct query and passage prefixes, tokenizer, pooling and normalization as part of the immutable index identity.

Use when: The encoder was trained with asymmetric retrieval instructions; Multiple services produce queries or passage vectors

Avoid when: The model explicitly documents symmetric encoding; The deployed model card does not specify an instruction contract

Failure modes: Query and passage prefixes are swapped; Pooling differs between indexing and serving; A model upgrade silently changes tokenization

Required evals: prefix parity matrix; known-neighbor sentinel tests; cross-client vector equivalence; paired retrieval replay

Evidence: `E2` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Domain-Adapted Dense Retriever

Technique ID: `embedding.dense.domain-adapted` · Stage: `embedding` · Risk: `high`

Fine-tunes a dense retriever on audited target-domain positives and hard negatives or carefully validated synthetic relevance labels.

Use when: A strong zero-shot baseline fails stable domain slices; Representative positives and hard negatives can be governed

Avoid when: Labels are weak or leakage-prone; Chunking or parsing defects explain the misses

Failure modes: Synthetic labels reinforce generator errors; Catastrophic loss on general or multilingual slices; False negatives teach relevant documents as negatives

Required evals: paired target-domain Recall@k; general-domain regression suite; label audit and leakage checks; training and reindex cost

Evidence: `E3` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Long-Input Dense Embedding

Technique ID: `embedding.dense.long-input` · Stage: `embedding` · Risk: `high`

Encodes passages longer than conventional sentence windows with a retriever trained and evaluated for extended token inputs.

Use when: Relevant units exceed short encoder limits; Silent truncation is a measured retrieval failure

Avoid when: Structure-aware smaller units already retrieve correctly; Long inputs add topic dilution or unacceptable compute

Failure modes: Long passages dilute the relevant signal; Advertised context length is not retrieval quality; Encoding throughput collapses on long-tail documents

Required evals: length-bucketed Recall@k; truncation sentinel cases; encoding throughput by token length; answer and citation correctness

Evidence: `E2` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Matryoshka-Compatible Dimension Truncation

Technique ID: `embedding.dense.matryoshka-truncation` · Stage: `embedding` · Risk: `high`

Uses an encoder explicitly trained or adapted so prefixes of the full embedding remain useful at smaller indexed dimensions.

Use when: Index memory or ANN latency is binding; The exact model documents nested-dimension training

Avoid when: The model was not trained for nested dimensions; Quality at the target dimension lacks private replay evidence

Failure modes: Arbitrary truncation destroys retrieval geometry; Extreme compression harms hard negatives; Dimension and normalization mismatch query and document indexes

Required evals: nDCG across candidate dimensions; index size and ANN latency; hard-negative and multilingual regressions; query-document configuration parity

Evidence: `E3` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Multilingual Dense Bi-Encoder

Technique ID: `embedding.dense.multilingual` · Stage: `embedding` · Risk: `high`

Encodes queries and passages into single dense vectors trained for multilingual and cross-lingual semantic retrieval.

Use when: Queries and corpus span multiple languages; Paraphrase or cross-lingual matching matters

Avoid when: Exact identifiers dominate and lexical retrieval already meets gates; Private replay does not cover the deployed languages

Failure modes: Aggregate benchmark rank hides weak languages; Identifiers and rare terms collapse semantically; Wrong query instruction or normalization silently degrades recall

Required evals: Recall@k and nDCG by language; cross-lingual and code-switching slices; identifier and hard-negative slices; throughput latency and index bytes

Evidence: `E3` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Dense and Sparse Hybrid Retrieval

Technique ID: `embedding.hybrid.dense-sparse` · Stage: `retrieval` · Risk: `high`

Runs dense semantic and lexical or learned-sparse retrieval independently, then fuses ranked candidates before reranking.

Use when: Both paraphrases and exact identifiers appear; Per-lane scores or ranks can be logged and evaluated

Avoid when: One lane consistently adds only duplicates; Latency budget cannot support dual candidate generation

Failure modes: Uncalibrated score fusion suppresses a good lane; Duplicate candidates consume reranker depth; Added latency yields no answer-quality gain

Required evals: per-lane and fused Recall@k; identifier and paraphrase slices; deduplication and reranker-depth analysis; p95 latency and cost

Evidence: `E3` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Immutable Dual-Index Embedding Migration

Technique ID: `embedding.migration.immutable-dual-index` · Stage: `embedding` · Risk: `high`

Builds a versioned challenger index from a frozen manifest, validates coverage, dual-reads or shadows it, and promotes by reversible alias switch.

Use when: Changing model revision dimension instructions or normalization; Rollback and uninterrupted service are required

Avoid when: Source and chunk manifests cannot be reproduced; Storage cannot temporarily hold champion and challenger

Failure modes: Manifest drift makes comparisons invalid; Partial challenger coverage creates silent misses; Mixed embedding spaces are queried as one index

Required evals: manifest and document coverage; paired retrieval replay; latency cost and capacity during dual-read; rollback rehearsal

Evidence: `E2` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Text Multi-Vector Late Interaction

Technique ID: `embedding.multivector.late-interaction` · Stage: `retrieval` · Risk: `high`

Stores token-level passage vectors and computes query-token maximum similarities at retrieval time for fine-grained matching.

Use when: Single-vector pooling loses local evidence; Retrieval quality justifies larger indexes and scoring cost

Avoid when: Index footprint or query latency is tightly bounded; A cross-encoder over a small dense candidate set already meets gates

Failure modes: Multi-vector index growth exceeds capacity; Maximum similarity overweights spurious token matches; Compression changes ranking on rare terms

Required evals: Recall@k and nDCG versus dense; index bytes per passage; p50 and p95 scoring latency; token-match error inspection

Evidence: `E3` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Learned Sparse Retrieval

Technique ID: `embedding.sparse.learned` · Stage: `embedding` · Risk: `high`

Produces vocabulary-aligned sparse vectors with learned term expansion and scores them through an inverted or sparse-vector index.

Use when: Exact terms and semantic lexical expansion both matter; Sparse postings and term-level diagnostics are operationally available

Avoid when: The serving engine lacks efficient sparse scoring; Model or weights licensing conflicts with deployment

Failure modes: Index expansion increases storage and latency; Rare domain vocabulary is poorly represented; Aggressive pruning removes useful expansion terms

Required evals: Recall@k versus BM25 and dense; identifier and rare-term slices; postings size and p95 latency; licence and deployment audit

Evidence: `E3` from `source-embedding-landscape-2026-08`; reviewed `2026-10-12`.

### Calibrated Trajectory Judge

Technique ID: `evaluation.calibrated-trajectory-judge` · Stage: `evaluation` · Risk: `high`

Applies a frozen criterion-specific rubric to trace evidence and final output, with abstention and calibration against expert or deterministic reference labels.

Use when: Important quality criteria cannot be fully encoded as executable rules; Trajectory quality matters beyond the final answer

Avoid when: A deterministic invariant can directly decide the criterion; No representative human-labeled calibration set exists

Failure modes: Judge rewards confident plausible traces; Model or prompt drift invalidates calibration; Single scalar hides safety gate violations

Required evals: agreement with expert labels; false positive and negative rate by slice; repeat stability; adversarial rubric gaming set

Evidence: `E3` from `source-evaluation-techniques-2026-08`; reviewed `2026-10-12`.

### Coding-Agent Project Replay

Technique ID: `evaluation.coding-agent-project-replay` · Stage: `evaluation` · Risk: `high`

Replays representative repository tasks in clean isolated workspaces against a fixed baseline and candidate harness while pinning every component and checking patch correctness unauthorized effects leakage cost latency recovery behavior and execution alignment.

Use when: A team is changing coding-agent instructions skills tools or orchestration; A harness recommendation claims project-specific quality or efficiency improvement

Avoid when: No representative tasks or authoritative state oracles exist; The candidate cannot be isolated from protected baseline and holdout cases; Reference patches holdout metadata or mutable caches remain model-visible

Failure modes: Visible tasks are overfit by instructions or skills; Weak tests reward superficial patches; Shared session workspace cache or network state contaminates paired runs; Aggregate pass rate hides unauthorized effects or task-class regressions; Model harness environment and evaluator change together and destroy attribution; The agent discovers a reference patch or hidden answer through an uninspected channel; Plausible final claims disagree with tool feedback workspace state or required artifacts; Context renewal forgets completed units and reintroduces regressions

Required evals: paired fresh-context task success with pinned manifest; deterministic patch and external-state oracle checks; protected safety secret-access information-flow and leakage sentinels; claim-to-tool-result workspace and artifact execution-alignment checks; long-horizon checkpoint recovery with completed units retained as regression obligations; latency token tool-call and human-review cost comparison; failed-command partial-edit and restart recovery replay; repeated-run variance and task-slice report

Evidence: `E3` from `source-coding-agent-harness-and-skills-evidence-2026-08`, `source-agent-evaluation-research-2026`; reviewed `2026-09-16`.

### Deterministic External-state Oracle

Technique ID: `evaluation.deterministic-state-oracle` · Stage: `evaluation` · Risk: `high`

Scores outcomes and causal evidence paths against executable tests, database state, permissions and time-bounded environment truth instead of response plausibility.

Use when: Task success has an observable machine-checkable state; Agents must use authorized evidence available at the relevant time

Avoid when: The criterion is inherently subjective and lacks a deterministic proxy; The evaluator shares mutable state that the candidate can manipulate

Failure modes: Oracle encodes the wrong task requirement; Simulator artifact creates accidental success; Agent gains access to hidden evaluator state

Required evals: oracle unit and mutation tests; human audit agreement; false pass and false fail rate; evaluator tamper resistance

Evidence: `E2` from `source-evaluation-techniques-2026-08`; reviewed `2026-09-12`.

### Paired Perturbation Replay

Technique ID: `evaluation.paired-perturbation-replay` · Stage: `evaluation` · Risk: `high`

Runs baseline and candidate on matched task and environment identities under clean and controlled perturbations to isolate regressions and robustness effects.

Use when: A change claim needs causal comparison against the current baseline; Tool noise memory contamination or environment variance are material risks

Avoid when: Task or environment identities differ between variants; One stochastic attempt is being treated as conclusive

Failure modes: Perturbation is unrealistic or leaks the expected answer; Runs share contaminated state; Aggregate score hides a high-risk regression slice

Required evals: paired effect and confidence interval; safety violations by perturbation; repeat variance; slice-level regression gates

Evidence: `E2` from `source-evaluation-techniques-2026-08`; reviewed `2026-09-12`.

### Protected Fresh Executable Holdout

Technique ID: `evaluation.protected-holdout` · Stage: `evaluation` · Risk: `high`

Separates visible development, candidate selection, hidden promotion and red-team tasks with immutable manifests, access control and duplicate checks.

Use when: Repeated optimization can overfit visible evaluations; Generalization or production promotion claims are being made

Avoid when: The same optimizer receives holdout-level feedback repeatedly; Tasks cannot be versioned reset or checked for leakage

Failure modes: Holdout scores leak into mutation feedback; Semantic near-duplicates cross splits; Static public tasks become contaminated

Required evals: cross-split duplicate audit; task solvability review; holdout access audit; fresh-task versus public-task delta

Evidence: `E3` from `source-evaluation-techniques-2026-08`; reviewed `2026-10-12`.

### Adaptive Agent Attack Replay

Technique ID: `evaluation.security.adaptive-attack-replay` · Stage: `evaluation` · Risk: `high`

Generates and manually reviews attacks after inspecting the deployed defense, then repeats them across changed models, tools, message order and multi-turn contexts with fixed state oracles.

Use when: A defense performs strongly on frozen public suites; Attackers can observe policy responses or adapt payloads

Avoid when: No stable external-state oracle exists; Adaptive generation can reach production credentials or effects

Failure modes: Attack generator optimizes a weak proxy metric; Generated cases leak into final holdouts; No benign controls reveal over-defense

Required evals: attack success by round; benign utility by round; changed tool and model transfer; protected post-tuning holdout

Evidence: `E2` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Paired Agent Security Benchmark Suite

Technique ID: `evaluation.security.agent-benchmark-suite` · Stage: `evaluation` · Risk: `high`

Runs benign utility and adversarial tool-use cases against a complete agent environment and scores authoritative external state rather than model text alone.

Use when: Tool-using agents process untrusted data; Security controls must preserve legitimate task utility

Avoid when: Only a chatbot response with no tools data access or memory is evaluated; Benchmark tools and schemas do not resemble the deployed workload

Failure modes: Frozen public attacks are overfit; Refusal is mistaken for security; Text graders disagree with actual tool state

Required evals: benign utility controls; direct and indirect injection; unauthorized external-state effects; protected workload-specific replay

Evidence: `E3` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Isolated Red-team Runner

Technique ID: `evaluation.security.isolated-redteam-runner` · Stage: `evaluation` · Risk: `high`

Executes red-team tools, configs, plugins, graders and datasets inside a disposable environment with scoped credentials, bounded filesystem access and controlled egress.

Use when: Evaluations load remote datasets templates or executable plugins; CI runs adversarial model outputs or untrusted pull requests

Avoid when: The runner has no isolation and shares production secrets; The test target can perform irreversible production effects

Failure modes: A malicious config executes with runner privileges; Reports or caches leak secrets; Provider tokens allow production actions

Required evals: malicious template and dataset execution; filesystem and secret denial; egress destination enforcement; cleanup and artifact redaction

Evidence: `E2` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Shadow and Canary Online Evaluation

Technique ID: `evaluation.shadow-canary-monitoring` · Stage: `evaluation` · Risk: `high`

Observes a candidate on production-shaped traffic without effects, then exposes a bounded canary while monitoring quality safety latency cost and rollback triggers.

Use when: Offline replay cannot reproduce production traffic or dependencies; A candidate has passed protected offline gates

Avoid when: No reliable rollback or traffic isolation exists; Shadow outputs could themselves trigger external actions

Failure modes: Shadow path differs materially from real execution; Rare safety events escape a small sample; Rollback is too slow for irreversible actions

Required evals: shadow-live parity; hard-gate alert latency; canary delta with uncertainty; rollback drill success

Evidence: `E2` from `source-evaluation-techniques-2026-08`; reviewed `2026-10-12`.

### Immutable Episodic Event Log

Technique ID: `memory.episodic-event-log` · Stage: `memory-write` · Risk: `high`

Records selected source events as immutable episodes with actor, time, scope, origin, permissions and causal links before any derived summarization.

Use when: Future tasks need auditable recall of prior interactions or outcomes; Derived memories must remain traceable to original evidence

Avoid when: Retention has no explicit purpose or lawful basis; Raw events contain secrets that should not be persisted

Failure modes: Overcapture retains irrelevant or sensitive content; Missing actor or time corrupts later interpretation; Mutable updates erase the original evidence

Required evals: capture precision and recall; provenance completeness; sensitive-data retention violations; event replay fidelity; equal-budget raw-log BM25 temporal and local-expansion baseline; ingest storage retrieval and answer cost per correct answer

Evidence: `E2` from `source-memory-techniques-2026-08`, `source-memory-operational-baselines-and-tenancy-2026-08`; reviewed `2026-09-17`.

### Typed Hybrid Memory Read Router

Technique ID: `memory.hybrid-read-router` · Stage: `memory-read` · Risk: `high`

Classifies the memory need and searches only eligible episodic semantic relational or procedural stores before bounded fusion and abstention.

Use when: Multiple memory types have different retrieval semantics; Privacy scope and temporal validity must filter every read

Avoid when: One small store already provides sufficient recall; Routing errors would hide critical evidence without a fallback

Failure modes: Router skips the store containing the answer; Scores from incompatible retrievers are fused naively; Retrieved memory violates actor or tenant scope

Required evals: need-detection precision and recall; memory Recall@k by type; irrelevant memory rate; cross-scope leakage tests; equal-budget raw-log BM25 temporal and local-expansion control; exact-identifier fact-tracking multi-hop and event-order slices

Evidence: `E2` from `source-memory-techniques-2026-08`, `source-memory-operational-baselines-and-tenancy-2026-08`; reviewed `2026-09-17`.

### Lineage-aware Verified Forgetting

Technique ID: `memory.lineage-forgetting` · Stage: `memory-write` · Risk: `high`

Expires supersedes archives or erases canonical memories and traces every derived summary embedding cache and graph edge for rebuild or deletion verification.

Use when: Retention limits correction requests or consent changes require removal; Derived indexes and summaries can be enumerated from lineage

Avoid when: The canonical source and derived copies cannot be identified; A retrieval filter is being presented as physical erasure

Failure modes: Shared summary retains deleted information; Orphan embedding remains retrievable; Supersession is mistaken for erasure

Required evals: lineage coverage; adversarial post-delete retrieval; rebuild consistency; retention policy compliance

Evidence: `E2` from `source-memory-techniques-2026-08`; reviewed `2026-09-12`.

### Verified Procedural Memory Promotion

Technique ID: `memory.procedural-promotion` · Stage: `memory-write` · Risk: `high`

Promotes a reusable workflow only after repeated successful traces are generalized into explicit preconditions, steps, postconditions and rollback instructions.

Use when: Tasks recur with stable interfaces and objective verification; A successful procedure can be replayed safely in a sandbox

Avoid when: A single success is the only supporting evidence; The environment or permissions differ across future executions

Failure modes: Overgeneralized procedure runs outside its preconditions; Stored steps reference stale tools or schemas; A successful but unsafe trace is promoted

Required evals: replay success on fresh cases; precondition classification accuracy; safety invariant violations; rollback execution success

Evidence: `E2` from `source-memory-techniques-2026-08`; reviewed `2026-10-12`.

### Influence-gated Memory Write

Technique ID: `memory.security.influence-gated-write` · Stage: `memory-write` · Risk: `high`

Routes owner-scoped user, retrieved, tool and model-derived observations into a quarantined candidate store and promotes only policy-compliant lineage-preserving memories after conflict and authority checks.

Use when: Retrieved evidence or tool output can become durable agent memory; Procedures or preferences can influence future actions

Avoid when: The system persists no cross-run memory; Candidate and canonical stores cannot be isolated

Failure modes: A summary hides malicious source instructions; Repeated low-risk candidates accumulate into high influence; Deletion misses derived memories and indexes; Merge refresh or consolidation crosses owner scope

Required evals: retrieval-to-memory poisoning; conflict and supersession handling; procedural promotion authority; deletion across source derived and indexed state; owner stamping and fail-closed missing-owner behavior; owner-scoped write merge refresh consolidation and derived-summary paths

Evidence: `E2` from `source-agentic-security-landscape-2026-08`, `source-agent-memory-evaluation-security-2026`, `source-memory-operational-baselines-and-tenancy-2026-08`; reviewed `2026-09-17`.

### Lineage-aware Semantic Consolidation

Technique ID: `memory.semantic-consolidation` · Stage: `memory-write` · Risk: `high`

Extracts candidate facts or preferences from one or more episodes, resolves duplicates and conflicts, and promotes a typed claim with lineage and validity.

Use when: Repeated episodes contain stable reusable facts; Full-history retrieval is too costly or noisy

Avoid when: Source evidence is ambiguous or rapidly changing; The extractor cannot preserve qualifiers and provenance

Failure modes: Extractor fabricates a fact; Consolidation drops temporal or conditional qualifiers; A new claim silently overwrites contested memory

Required evals: fact extraction precision and recall; qualifier preservation; conflict resolution accuracy; downstream answer gain versus episode-only baseline

Evidence: `E3` from `source-memory-techniques-2026-08`; reviewed `2026-10-12`.

### Temporal Entity and Relation Graph

Technique ID: `memory.temporal-entity-graph` · Stage: `memory-read` · Risk: `high`

Stores owner-scoped entities and relations with event time, ingestion time, validity intervals and source episodes for relational and temporally constrained retrieval.

Use when: Questions traverse relationships across people objects and events; Facts change over time and current versus historical truth matters

Avoid when: The corpus is small and flat retrieval already meets recall; Entity resolution errors cannot be reviewed or corrected

Failure modes: Entity resolution merges different actors or tenant-owned entities; Stale edges remain active after supersession; Multi-hop expansion introduces unrelated context; Merge refresh or consolidation drops owner scope; Missing ownership metadata fails open

Required evals: entity resolution precision and recall; temporal answer accuracy; path evidence precision; latency and graph growth; identical entity names across two owners or tenants; owner stamping on nodes edges facts and derived summaries; owner-scoped read write merge refresh consolidation deletion and rebuild; fail-closed behavior for missing ownership metadata; equal-budget raw-log BM25 and hybrid controls

Evidence: `E2` from `source-memory-techniques-2026-08`, `source-memory-operational-baselines-and-tenancy-2026-08`; reviewed `2026-09-17`.

### Region-Anchored Visual Citation

Technique ID: `multimodal.citation.region-anchored` · Stage: `context-assembly` · Risk: `high`

Carries stable document version page and bounding-box or table-cell identifiers from retrieval through generation into verifiable citations.

Use when: Answers depend on charts tables figures forms or layout; Users must inspect the exact visual evidence

Avoid when: Coordinates are discarded during parsing or rendering; Page versions cannot be pinned

Failure modes: Coordinates drift after document re-rendering; Citation points to a page but not supporting region; Sensitive hidden regions appear in crops

Required evals: region citation precision and recall; answer-citation entailment; version and coordinate stability; redaction and access-control tests

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Chart Derendering and Direct-Visual Fusion

Technique ID: `multimodal.fusion.chart-derender` · Stage: `retrieval` · Risk: `high`

Converts charts into structured table-like representations for retrieval while retaining a direct image lane and fusing their candidates.

Use when: Questions target values trends legends or axes in charts; Both regular and complex chart types occur

Avoid when: Charts are decorative and never queried; Derendering errors cannot be traced to the source image

Failure modes: Derenderer invents or swaps values; Complex charts lose relationships in tables; Fusion ranks a visually similar but numerically wrong chart

Required evals: chart Recall@1 and Recall@k; exact value and legend accuracy; complex-chart failure slices; latency and model cost

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Interleaved Multimodal Document Representation

Technique ID: `multimodal.fusion.interleaved-document-representation` · Stage: `embedding` · Risk: `high`

Encodes interleaved document text, images and structural segments into linked document- and passage-level representations.

Use when: Document questions depend on interleaved text and visuals; Both document retrieval and local passage grounding are needed

Avoid when: The workload is page-local text lookup; Long-document dilution and citation localization cannot be measured

Failure modes: Holistic vectors hide decisive passages; Long documents dilute rare visual evidence; Document retrieval loses exact citation locality

Required evals: document and passage Recall@k; length-bucketed retrieval; answer and regional citation correctness; index size and latency

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Layout-Symbolic plus Neural Retrieval

Technique ID: `multimodal.fusion.layout-symbolic-neural` · Stage: `retrieval` · Risk: `high`

Combines a symbolic document-layout and cross-page graph with neural indexes for adaptive retrieval over visually rich multi-page documents.

Use when: Questions depend on cross-page or layout relationships; Graph extraction quality can be inspected and replayed

Avoid when: The workload is simple page-local prose; Graph fan-out or extraction errors cannot be bounded

Failure modes: Incorrect topology routes retrieval away from evidence; Graph fan-out exceeds context budget; Graph nodes bypass document ACL filters

Required evals: perfect recall and noise by page budget; cross-page answer accuracy; graph extraction error slices; ACL leakage latency and token cost

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### OCR Text and Visual Candidate Fusion

Technique ID: `multimodal.fusion.ocr-visual` · Stage: `retrieval` · Risk: `high`

Retrieves independently from OCR or parsed text and page-image indexes, then fuses and deduplicates candidates using stable page identities.

Use when: Corpus mixes clean text scans charts and diagrams; Text and visual lanes have complementary measured errors

Avoid when: One lane consistently dominates every slice; ACL or version filters cannot be enforced identically

Failure modes: Duplicate page hits crowd out diversity; Score calibration suppresses one useful lane; Different ACL filters leak unauthorized visual pages

Required evals: per-lane and fused Recall@k; OCR-quality and modality slices; deduplication and candidate-depth analysis; latency cost and ACL parity

Evidence: `E2` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Bounded Multimodal Reranker

Technique ID: `multimodal.reranking.cross-modal` · Stage: `reranking` · Risk: `high`

Applies a vision-language relevance scorer to a bounded set of text and page-image candidates after cheaper first-stage retrieval.

Use when: First-stage visual recall is adequate but top ranks are noisy; The latency budget supports bounded vision-language scoring

Avoid when: Relevant pages are absent from candidate generation; The reranker cannot honor ACL or page-version identity

Failure modes: Reranker cannot recover first-stage misses; Page resize hides the decisive region; Latency spikes on many high-resolution pages

Required evals: nDCG before and after reranking; oracle-candidate upper bound; visual confounder and OCR slices; p95 latency GPU memory and cost

Evidence: `E2` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Utility-Oriented Visual Evidence Selection

Technique ID: `multimodal.reranking.utility-evidence-selection` · Stage: `reranking` · Risk: `high`

Reranks a bounded visual candidate set by estimated downstream evidence utility rather than semantic similarity alone.

Use when: First-stage visual recall is adequate but plausible images are unhelpful; Answer utility can be evaluated by modality slice

Avoid when: The relevant page is absent from the candidate pool; The utility surrogate is unvalidated for the serving model

Failure modes: Utility surrogate is model-specific; Reranking suppresses diverse required evidence; Extra scoring erases latency savings

Required evals: answer delta under fixed candidates; nDCG and required-evidence coverage; oracle-candidate gap; p95 latency and model-call cost

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Query and Corpus Modality Routing

Technique ID: `multimodal.routing.query-and-corpus` · Stage: `retrieval` · Risk: `high`

Routes or fans out each query to text visual chart or structured-table lanes using query intent and document modality metadata.

Use when: Visual processing cost should be selective; Modality labels and route decisions can be logged

Avoid when: Routing recall cannot be measured; A wrong route would irreversibly hide all relevant evidence

Failure modes: Ambiguous queries take the wrong lane; Metadata misclassifies scanned or mixed pages; Router drift changes recall without visible errors

Required evals: route accuracy and oracle-route gap; end-to-end Recall@k by modality; fallback rate and missed-evidence audit; latency and cost by route

Evidence: `E2` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Structured Table Retrieval with SQL Execution

Technique ID: `multimodal.routing.structured-table-sql` · Stage: `retrieval` · Risk: `high`

Routes relational table questions to schema-aware query decomposition and bounded SQL execution while retrieving accompanying prose separately.

Use when: Questions require aggregation filtering joins or multi-hop table reasoning; Tables can be parsed into governed schemas with cell provenance

Avoid when: Tables are mostly images with unreliable extraction; Generated SQL cannot be sandboxed and validated

Failure modes: Parser assigns wrong headers or cell types; Generated SQL executes the wrong relation; Cross-table joins lose document provenance

Required evals: table and text retrieval recall; SQL execution and exact-answer accuracy; schema corruption and adversarial query tests; cell-level citation correctness

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Hybrid Single- and Multi-Vector Visual Retrieval

Technique ID: `multimodal.visual.hybrid-vector` · Stage: `retrieval` · Risk: `high`

Uses compact single-vector retrieval for the first stage and multi-vector late interaction to rescore a bounded shortlist.

Use when: Single-vector speed and local visual detail are both required; Shortlist recall can be measured before multi-vector scoring

Avoid when: The single-vector stage misses required pages; Storage or scoring cost cannot support a second representation

Failure modes: First-stage misses are unrecoverable; Dual representations cause storage creep; Single- and multi-vector scores are mixed incorrectly

Required evals: first-stage oracle recall; page and region nDCG; index bytes per page; p50 and p95 query latency

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Page-Image Late Interaction Retrieval

Technique ID: `multimodal.visual.late-interaction` · Stage: `retrieval` · Risk: `high`

Stores multiple visual patch vectors per page and scores query tokens against them with maximum-similarity late interaction.

Use when: Tables figures typography or layout drive relevance; Page-level visual retrieval gains justify a multi-vector index

Avoid when: Text retrieval already meets modality gates; Index footprint and scoring latency are tightly constrained

Failure modes: Multi-vector storage grows rapidly; Patch matches retrieve a visually similar wrong page; Retrieved page lacks exact textual grounding

Required evals: ViDoRe-style page nDCG and Recall@k; region coverage and wrong-page negatives; index bytes per page and p95 latency; answer and citation correctness

Evidence: `E3` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Page-Image Single-Vector Retrieval

Technique ID: `multimodal.visual.single-vector` · Stage: `embedding` · Risk: `high`

Encodes each rendered page image into one vector and retrieves it from a standard approximate nearest-neighbor index.

Use when: A compact visual baseline is needed; Layout or figures matter beyond extracted text

Avoid when: Exact text quotation is the only workload; Page-level pooling loses small relevant regions

Failure modes: Small text vanishes during resize; Single-vector pooling hides local evidence; Visually similar templates dominate results

Required evals: page Recall@k by modality; visually similar negative pages; index bytes and query latency; downstream answer and citation correctness

Evidence: `E2` from `source-multimodal-rag-landscape-2026-08`; reviewed `2026-10-12`.

### Amazon Textract

Technique ID: `parser.managed.aws-textract` · Stage: `ingestion` · Risk: `high`

Extracts printed and handwritten text plus forms, tables, queries and signatures through AWS-managed synchronous or asynchronous document APIs.

Use when: AWS workloads need forms, tables, signatures or queried fields; Managed typed extraction is more valuable than general document Markdown

Avoid when: Scientific formulas, charts or narrative hierarchy dominate; Documents cannot be processed by the managed AWS service

Failure modes: Key-value relationships fail on novel forms; Complex merged tables lose topology; Async quotas or regional outages delay jobs

Required evals: field-level precision and recall; table topology accuracy; signature and query accuracy; API cost latency and residency

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Azure Document Intelligence

Technique ID: `parser.managed.azure-document-intelligence` · Stage: `ingestion` · Risk: `high`

Applies managed layout and prebuilt document models for OCR, structure, tables, figures and field-oriented extraction across documents.

Use when: Microsoft-hosted enterprise workflows need forms, tables or figures; Typed prebuilt models reduce application extraction code

Avoid when: Documents require strict local processing; The workload cannot accept Azure pricing, quotas or model-version coupling

Failure modes: Prebuilt fields mismatch domain-specific forms; API version changes field schemas; Regional capacity or quotas delay ingestion

Required evals: field-level precision and recall; table and figure accuracy; API latency and cost; privacy residency and retention review

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Google Document AI Layout Parser

Technique ID: `parser.managed.google-document-ai` · Stage: `ingestion` · Risk: `high`

Uses managed layout parsing and Gemini-backed document understanding to create structure-aware output and chunks for retrieval-oriented workflows.

Use when: Google Cloud is the approved boundary and layout-aware RAG chunks are desired; Managed parsing and processor operations are preferred

Avoid when: Required data residency conflicts with the parser endpoint behavior; Provider-generated chunks cannot replace an independently evaluated chunker

Failure modes: Generated chunks cross semantic or access boundaries; Endpoint residency differs from project assumptions; Processor revisions change document structure

Required evals: layout and reading-order accuracy; chunk boundary quality; downstream retrieval correctness; privacy residency cost and latency

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### LlamaParse Managed Parser

Technique ID: `parser.managed.llamaparse` · Stage: `ingestion` · Risk: `high`

Provides managed document parsing with efficient and agentic modes, including chart-oriented extraction and structured Markdown or JSON outputs.

Use when: Complex charts or irregular documents justify an agentic managed path; Low operational burden matters more than on-premise control

Avoid when: Documents cannot leave the approved environment; High-volume variable API cost or provider dependency is unacceptable

Failure modes: Agentic parsing produces unsupported interpretations; Provider revisions change output; Rate limits or outages block ingestion

Required evals: chart datapoint fidelity; unsupported-content rate; API latency and cost per page; privacy residency and retention review

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Mistral OCR Managed Parser

Technique ID: `parser.managed.mistral-ocr` · Stage: `ingestion` · Risk: `high`

Returns ordered structured document blocks with text, tables, images and coordinate information through a managed OCR and document-processing API.

Use when: Managed OCR with ordered blocks and bounding boxes is acceptable; PDF and image parsing should require minimal local infrastructure

Avoid when: Strict on-premise or unapproved cross-border processing applies; A provider-independent deterministic parser is required

Failure modes: Model alias or API revision changes output; Tables lose merged-cell semantics; Service limits or outages interrupt ingestion

Required evals: text and reading-order fidelity; table structure accuracy; bounding-box provenance; API cost latency and residency

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Firecrawl AnyDoc

Technique ID: `parser.native.anydoc` · Stage: `ingestion` · Risk: `medium`

Uses pure Rust format-specific parsers and a shared document model to convert office, OpenDocument, RTF, EPUB, CSV and text-based PDF files into consistent Markdown without ML or external services.

Use when: Office-heavy mixed corpora need fast local Markdown normalization; Browser WASM or Rust, Node and Python bindings reduce integration cost

Avoid when: PDFs are image-only or require OCR; Visual layout, handwriting, charts or formula semantics are primary

Failure modes: Image-only PDFs return unsupported; Format-specific structure is flattened during normalization; Malformed or deeply nested files hit safety limits

Required evals: completeness by file format; heading list and table fidelity; conversion latency and memory; unsupported and malformed-file rate

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Apache Tika Format Router

Technique ID: `parser.native.apache-tika` · Stage: `ingestion` · Risk: `medium`

Detects file types and extracts text and metadata across a broad format set through delegated parsers, with optional Tesseract OCR.

Use when: The corpus contains many office, archive and document formats; A uniform detection and metadata front door is needed

Avoid when: High-fidelity page layout or formulas are primary outputs; Complex PDFs need reliable visual reading order

Failure modes: Flattened layout loses document structure; Delegated parser behavior varies by format; Embedded files cause latency or resource spikes

Required evals: format detection coverage; text fidelity by MIME type; metadata accuracy; latency and failure rate by file class

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### pdfplumber Geometry Extraction

Technique ID: `parser.native.pdfplumber` · Stage: `ingestion` · Risk: `medium`

Exposes characters, lines, rectangles, curves, coordinates and configurable table extraction from machine-generated PDFs through pdfminer-based layout analysis and visual debugging.

Use when: Exact PDF geometry or custom rule-based table extraction matters; Developers need visual debugging of table boundaries and coordinates

Avoid when: Documents are predominantly scanned or handwritten; A turnkey multi-format or semantic-layout parser is required

Failure modes: Scanned pages contain no extractable text; Tolerance settings merge or split columns incorrectly; Complex borderless or merged tables lose topology

Required evals: character and coordinate fidelity; table cell topology; reading-order accuracy; memory and latency on large PDFs

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### PyMuPDF Native Extraction

Technique ID: `parser.native.pymupdf` · Stage: `ingestion` · Risk: `medium`

Extracts encoded text, words, blocks, coordinates and tables directly from PDF structure, with optional Tesseract OCR fallback.

Use when: Born-digital PDFs have a reliable text layer; High throughput and coordinate-level provenance matter

Avoid when: Pages are predominantly scans or handwriting; Visual reading order is not represented in the PDF structure

Failure modes: Incorrect multi-column reading order; Missing or malformed table structure; Garbled text from broken font encodings

Required evals: character and word fidelity; reading-order accuracy; table structure accuracy; downstream retrieval and citation correctness

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Docling Standard Pipeline

Technique ID: `parser.pipeline.docling-standard` · Stage: `ingestion` · Risk: `medium`

Combines deterministic PDF parsing with configurable OCR, layout analysis, reading order and table-structure recognition in an inspectable local pipeline.

Use when: Mixed born-digital and scanned PDFs need one local pipeline; Tables, hierarchy and page provenance matter

Avoid when: Only plain clean text is needed at maximum throughput; Hard handwriting or chart semantics dominate the corpus

Failure modes: OCR errors cascade into layout and tables; Reading order fails on unusual page designs; Accurate table mode increases latency

Required evals: reading-order accuracy; table cell topology; OCR accuracy by language; downstream answer and citation correctness

Evidence: `E2` from `source-parser-landscape-2026-08`, `source-document-parsing-evidence-2026`; reviewed `2026-10-12`.

### Marker PDF Conversion

Technique ID: `parser.pipeline.marker` · Stage: `ingestion` · Risk: `high`

Converts PDFs to Markdown or structured output using native text and layout models, with OCR and optional LLM-assisted recovery for difficult pages.

Use when: Local PDF-to-Markdown conversion is the primary need; Scientific PDFs and tables need stronger structure than native extraction

Avoid when: The archive is mostly non-PDF formats; LLM-assisted parsing cannot be allowed or audited

Failure modes: LLM assistance invents plausible content; Tables or columns are serialized incorrectly; Resource use spikes on scanned documents

Required evals: Markdown structural fidelity; table accuracy; unsupported-content rate with LLM assist; latency and GPU memory by page type

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Microsoft MarkItDown

Technique ID: `parser.pipeline.markitdown` · Stage: `ingestion` · Risk: `high`

Routes many document, media, web and archive formats through lightweight Python converters to Markdown, with optional plugins, vision OCR and Azure-managed extraction paths.

Use when: A lightweight Python multi-format conversion layer is needed; Optional plugins or Azure escalation fit the existing environment

Avoid when: Untrusted paths or URLs cannot be tightly sandboxed; High-fidelity visual PDF parsing is required without an external backend

Failure modes: Permissive I/O accesses unintended local or network resources; Optional OCR silently does not run when its client is absent; Plugin or cloud backends produce inconsistent structures

Required evals: completeness by format; security tests for path URI and archive inputs; structure fidelity; latency cost and unsupported-file rate

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### MinerU Document Pipeline

Technique ID: `parser.pipeline.mineru` · Stage: `ingestion` · Risk: `high`

Parses PDFs, images and office documents with layout, OCR, reading-order, table and formula components and can emit HTML tables and LaTeX formulas.

Use when: Scientific or multilingual documents contain formulas and complex layouts; Local execution and structured Markdown-like output are required

Avoid when: The project cannot accept MinerU licensing conditions; A small CPU-only footprint and very low latency are mandatory

Failure modes: Formula or table detectors produce malformed markup; Language-specific OCR quality varies; Backend and dependency changes alter output

Required evals: formula exactness; table structure accuracy; reading-order accuracy; licensing and deployment review

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### PaddleOCR PP-StructureV3

Technique ID: `parser.pipeline.paddleocr-structure` · Stage: `ingestion` · Risk: `high`

Runs configurable layout detection, multilingual OCR, table, formula and chart modules as a local structured-document pipeline.

Use when: Multilingual OCR and modular document structure are required; Teams need trainable or replaceable pipeline stages

Avoid when: The deployment cannot support the Paddle stack; A single end-to-end semantic parser is preferred over staged diagnostics

Failure modes: Detector misses propagate to later stages; Script-specific OCR quality varies; Module version mismatch changes output

Required evals: OCR accuracy per language; layout element detection; table and formula structure; latency per enabled module

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Unstructured Partition Strategies

Technique ID: `parser.pipeline.unstructured` · Stage: `ingestion` · Risk: `medium`

Partitions many document types with selectable fast, high-resolution, OCR-only or automatic strategies and optional table-structure extraction.

Use when: One integration must partition many common file types; Per-document routing between fast and layout-aware paths is useful

Avoid when: Highest-fidelity complex tables are mandatory without corpus evaluation; Strictly deterministic output is required across dependency updates

Failure modes: Auto strategy selects a weak path; High-resolution layout reorders multi-column text; Table extraction depends on strategy and model

Required evals: strategy routing accuracy; element classification; table structure accuracy; latency and failure rate by format

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Xberg Polyglot Document Intelligence

Technique ID: `parser.pipeline.xberg` · Stage: `ingestion` · Risk: `high`

Provides a Rust-core multi-format extraction framework with polyglot bindings, pluggable OCR and VLM backends, metadata, structured output and code intelligence across documents and archives.

Use when: One local framework must serve multiple programming languages and many formats; Code intelligence or configurable OCR and VLM plugins materially reduce integration work

Avoid when: Elastic License 2.0 is incompatible with the deployment; A small fixed parser surface is preferred over a broad plugin framework

Failure modes: Selected plugins expand attack and dependency surface; Backend-specific outputs differ despite one interface; Large breadth hides weak fidelity on particular document slices

Required evals: fidelity by format and backend; OCR accuracy by language; plugin sandbox and resource limits; licence and operational review

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### Docling VLM Pipeline

Technique ID: `parser.vlm.docling` · Stage: `ingestion` · Risk: `high`

Renders pages for a vision-language model and converts visual document understanding into structured Docling output, optionally retaining native text signals.

Use when: Layouts, diagrams, formulas or degraded scans defeat deterministic parsing; Local VLM deployment is required

Avoid when: GPU capacity or latency budget is tight; Unsupported generated structure cannot be independently checked

Failure modes: Plausible but unsupported text or structure; Model-version drift changes parse output; GPU memory exhaustion on large pages

Required evals: visual text fidelity; formula and table accuracy; unsupported-content rate; GPU latency and memory by page class

Evidence: `E2` from `source-parser-landscape-2026-08`, `source-document-parsing-evidence-2026`; reviewed `2026-10-12`.

### olmOCR VLM Parser

Technique ID: `parser.vlm.olmocr` · Stage: `ingestion` · Risk: `high`

Uses a document-focused vision-language model to transcribe rendered pages into linearized text with support for equations, tables, handwriting and complex layouts.

Use when: Degraded scans, handwriting or mathematical pages defeat conventional OCR; GPU batch processing of difficult PDFs is acceptable

Avoid when: Only CPU execution is available; Typed form fields and key-value extraction are the main requirement

Failure modes: Generated text is plausible but absent from page; Long pages truncate or reorder content; GPU memory and throughput vary by rendering

Required evals: edit distance on hard scans; reading-order accuracy; formula and table fidelity; unsupported-content and truncation rate

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### PaddleOCR-VL

Technique ID: `parser.vlm.paddleocr-vl` · Stage: `ingestion` · Risk: `high`

Uses a compact vision-language document model with layout detection to recognize multilingual text, tables, formulas, charts and complex page structures.

Use when: Multilingual or historical pages require end-to-end visual parsing; Tables, formulas and charts coexist on difficult scans

Avoid when: CPU-only low-latency processing is required; Every extraction error must be attributable to a deterministic stage

Failure modes: Visually plausible content is generated without support; Dense pages overflow context or lose elements; Model and runtime updates change output

Required evals: OCR accuracy per language; table formula and chart fidelity; unsupported-content rate; GPU latency and memory

Evidence: `E2` from `source-parser-landscape-2026-08`; reviewed `2026-10-12`.

### BM25 Lexical Retrieval

Technique ID: `retrieval.bm25` · Stage: `retrieval` · Risk: `medium`

Uses an inverted index with term-frequency saturation and document-length normalization to rank exact and weighted lexical matches.

Use when: Queries contain identifiers, names, error codes, quoted phrases or domain terminology; A cheap reproducible and inspectable first-stage control is required

Avoid when: Relevant evidence shares few lexical anchors with the query; The selected analyzer cannot represent the corpus languages or token conventions

Failure modes: Synonym and paraphrase misses; Analyzer mismatch destroys important tokens; Frequent boilerplate dominates scoring

Required evals: Recall@k and nDCG by query class; exact-identifier and quoted-text slice; latency and index-size curve; permission-filter correctness

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Dense Vector Retrieval

Technique ID: `retrieval.dense` · Stage: `retrieval` · Risk: `high`

Encodes queries and passages into a shared vector space and retrieves approximate nearest neighbors by embedding similarity.

Use when: Paraphrases and vocabulary mismatch cause lexical recall failures; The corpus language and domain are covered by a versioned embedding model

Avoid when: Exact identifiers dominate and dense retrieval loses their distinctions; Embedding versions or index builds cannot be reproduced and rolled back

Failure modes: Exact-term and rare-entity misses; Domain or language mismatch; Embedding drift requires a full index migration

Required evals: Recall@k by semantic and exact-query slice; nDCG or MRR; index reproducibility and migration replay; latency memory and index-size curve

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Retrieval and Reranking Depth Tuning

Technique ID: `retrieval.depth.tuning` · Stage: `retrieval` · Risk: `medium`

Tunes retrieve-k, rerank-k and final-k independently from recall, precision, latency and context-budget curves rather than using one inherited top-k.

Use when: Relevant evidence is missed at low candidate depth; High depth dilutes context or makes reranking too expensive

Avoid when: Required evidence is absent from the index; Changing depth would hide a parser filter or chunk-boundary defect

Failure modes: Tail evidence is missed at an undersized retrieve-k; Large rerank-k causes latency spikes; Large final-k creates context dilution and position bias

Required evals: Recall@k saturation curve; context precision and required-evidence coverage; answer quality under fixed ordered candidates; p50 p95 latency and token cost

Evidence: `E2` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Hybrid Lexical-Dense Retrieval with RRF

Technique ID: `retrieval.hybrid.rrf` · Stage: `retrieval` · Risk: `high`

Runs lexical and dense retrieval independently and merges their ranked lists with deterministic reciprocal-rank fusion.

Use when: The workload mixes exact identifiers with conceptual questions; Lexical and dense paths show complementary relevant-document recall

Avoid when: One retriever already saturates intended-slice recall; A second index and query path exceed the latency or maintenance budget

Failure modes: Duplicate or near-duplicate candidates consume depth; Weak-path noise displaces strong-path evidence; Latency and operational cost increase without material gain

Required evals: paired Recall@k versus each component; nDCG by exact and semantic slices; duplicate and unique-evidence yield; p50 and p95 latency plus index cost

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Gap-Guided Iterative Retrieval

Technique ID: `retrieval.iterative.gap-guided` · Stage: `retrieval` · Risk: `high`

Alternates bounded reasoning with retrieval queries derived from explicit missing-evidence gaps until sufficient evidence or a hard stop is reached.

Use when: Multi-hop evidence dependencies cannot be expressed fully before the first retrieval; Offline replay shows later queries recover required missing hops

Avoid when: Direct questions dominate; Evidence-sufficiency judgments are uncalibrated or no hard iteration budget exists

Failure modes: Self-confirming queries reinforce an early false premise; False sufficiency stops before required evidence; Repeated queries inflate latency and cost without new evidence

Required evals: hop and final evidence recall; new-evidence yield per iteration; stop correctness and loop-limit sentinels; latency token cost and tool calls

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Metadata and Permission Filtering

Technique ID: `retrieval.metadata.permission-filter` · Stage: `retrieval` · Risk: `high`

Applies typed tenant, authorization, document, time and version predicates before or inside candidate generation rather than after disclosure.

Use when: The corpus has tenant or authorization boundaries; Dates versions document types or jurisdictions materially constrain relevance

Avoid when: Required metadata is incomplete or untrusted; The search backend cannot enforce predicates before candidate materialization

Failure modes: Stale ACLs expose forbidden content; Fail-open behavior on missing metadata; Over-restrictive predicates create silent false negatives

Required evals: cross-tenant and revoked-access sentinels; missing and malformed metadata cases; recall under each filter slice; as-of-time and version correctness

Evidence: `E2` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Dependency-Preserving Question Decomposition

Technique ID: `retrieval.query.decomposition` · Stage: `retrieval` · Risk: `high`

Splits a composite or multi-hop request into bounded subquestions with explicit dependencies and separately traceable retrieval results.

Use when: Answering requires evidence from multiple entities pages or hops; A single query consistently misses an identifiable evidence dependency

Avoid when: Direct lookup dominates and decomposition adds no coverage; The task constraints cannot be reliably propagated to every subquestion

Failure modes: Incorrect decomposition makes the original question unsolvable; Global constraints or negation disappear from a subquestion; Duplicate or cyclic work expands cost

Required evals: hop-level evidence recall; final required-claim coverage; constraint propagation and dependency correctness; tool calls latency and stop behavior

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Bounded Multi-Query Expansion

Technique ID: `retrieval.query.multi-query` · Stage: `retrieval` · Risk: `high`

Generates a small set of complementary retrieval queries and fuses their candidate sets under one fixed total evidence budget.

Use when: A request has distinct facets or terminology that one query misses; Offline labels show additional queries add unique required evidence

Avoid when: Distractor density is high or precision already fails; Latency budget cannot tolerate parallel retrieval or generation

Failure modes: Redundant queries amplify the same results; Generated facets drift from user constraints; Noise cost and latency grow faster than useful evidence

Required evals: unique required-evidence yield per added query; context precision and nDCG; intent-drift and identifier preservation; latency tool calls and cost

Evidence: `E2` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Intent-Preserving Query Rewriting

Technique ID: `retrieval.query.rewrite` · Stage: `retrieval` · Risk: `high`

Transforms conversational or underspecified input into a standalone retrieval query while preserving entities, constraints and exact identifiers.

Use when: Follow-up questions depend on conversation context; Verbose or ambiguous wording consistently lowers first-stage recall

Avoid when: Exact strings could be mutated without detection; The original query already retrieves the required evidence

Failure modes: Semantic drift changes the requested task; Identifiers dates or negation are lost; Prompt injection is propagated into generated queries

Required evals: intent and constraint preservation; Recall@k versus original query; exact-identifier and negation slice; latency token cost and rewrite rejection rate

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Per-Query Retriever Router

Technique ID: `retrieval.query.router` · Stage: `retrieval` · Risk: `high`

Selects sparse, dense, hybrid or bounded fan-out retrieval per query using explicit query features and a logged fallback policy.

Use when: Query classes have measurably different winning retrievers; Route decisions and oracle-route gaps can be evaluated

Avoid when: One retriever dominates every slice; A wrong route can hide critical evidence without fallback

Failure modes: Wrong-path routing hides evidence; Router oscillates after model updates; Hidden fan-out cost exceeds the static baseline

Required evals: routing confusion matrix; oracle-route Recall and nDCG gap; exact identifier and paraphrase slices; p95 latency and cost by route

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Cross-Encoder Reranking

Technique ID: `retrieval.rerank.cross-encoder` · Stage: `reranking` · Risk: `high`

Jointly encodes each query-passage pair and rescores a bounded first-stage candidate set before final evidence selection.

Use when: Required evidence appears in candidates but ranks too low; The latency budget supports pairwise relevance scoring

Avoid when: First-stage recall is the bottleneck; Candidate passages exceed the reranker input limit or required throughput

Failure modes: Cannot recover evidence absent from candidates; Domain mismatch misranks relevant passages; Truncation hides the decisive span and latency scales with pairs

Required evals: nDCG MRR and required-passage rank; fixed-candidate-set comparison; domain and long-passage slices; p50 p95 latency throughput and cost

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### MMR Diversity Selection

Technique ID: `retrieval.rerank.mmr-diversity` · Stage: `reranking` · Risk: `medium`

Greedily balances query relevance against similarity to already selected passages to reduce redundancy within a fixed evidence budget.

Use when: Top candidates repeat the same claim while multi-facet evidence is missing; Answer completeness depends on covering distinct sources or subtopics

Avoid when: The question has one precise answer and pure relevance is preferred; Apparently redundant passages provide necessary corroboration or chronology

Failure modes: Novel but weakly relevant passages displace decisive evidence; Corroborating passages are treated as waste; Similarity representation makes selection unstable across domains

Required evals: unique required-claim coverage; duplicate and source-diversity rate; answer completeness and precision; single-answer versus multi-facet slices

Evidence: `E3` from `source-retrieval-context-landscape-2026-08`; reviewed `2026-10-12`.

### Authorization-first Candidate Generation

Technique ID: `retrieval.security.authorization-first` · Stage: `retrieval` · Risk: `high`

Propagates user and agent identity into the search backend and applies tenant, resource, field, purpose, time and version predicates before candidate materialization.

Use when: The corpus contains protected or tenant-scoped data; Caches rerankers or models must never observe unauthorized candidates

Avoid when: All corpus content is intentionally public; The backend can filter only after returning raw candidates

Failure modes: Stale ACL replicas grant revoked access; Parent or neighbor expansion crosses a boundary; Caches omit identity or policy version from keys

Required evals: cross-tenant and cross-user sentinels; revocation and stale-ACL tests; parent neighbor and cache boundary tests; missing malformed metadata fail-closed

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Fail-closed Citation and Output Security Gate

Technique ID: `retrieval.security.citation-gate` · Stage: `context-assembly` · Risk: `high`

Validates source identity, version, authorization, claim support and output policy before returning an answer or permitting downstream agent actions.

Use when: Answers must be traceable to governed evidence; Unsupported or sensitive output can cause material harm

Avoid when: The application cannot bind generated claims to exact retrieved versions; A verifier model is used as the sole allow or deny authority

Failure modes: Exact citation exists but does not entail the claim; Output policy misses transformed secrets or PII; Model-only fallback bypasses the gate

Required evals: fabricated and mismatched citations; entailment and qualifier preservation; PII and secret transformation probes; verifier outage and model-only fallback denial

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Independent-source Retrieval Corroboration

Technique ID: `retrieval.security.independent-source-corroboration` · Stage: `reranking` · Risk: `high`

Groups candidates by upstream provenance and requires consequential claims to be supported by multiple independently governed source domains or to abstain and escalate.

Use when: High-impact claims have genuinely independent evidence sources; Poisoning or single-source compromise is a material risk

Avoid when: All apparent sources derive from one shared upstream; The domain has one authoritative source that should not be outvoted

Failure modes: Mirrors are counted as independent sources; Several sources repeat the same upstream error; A true single authority is incorrectly rejected

Required evals: shared-upstream diversity spoofing; single-authority exception handling; poisoned minority and majority cases; coverage latency and abstention calibration

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Retrieval Index Integrity Monitor

Technique ID: `retrieval.security.index-integrity-monitor` · Stage: `retrieval` · Risk: `high`

Links every indexed chunk to versioned source hashes, ACL state and transformation lineage and alerts on membership drift, targeted dominance, deletion gaps and abnormal embedding distributions.

Use when: Indexes are updated continuously or by multiple pipelines; Poisoning deletion and unauthorized membership must be detected

Avoid when: The index is rebuilt as one signed immutable release with equivalent verification; Monitoring has no authoritative source manifest for comparison

Failure modes: The source manifest is compromised with the index; Sampling misses targeted poisoned chunks; Embedding drift alerts on benign model migration

Required evals: hash and membership tampering; targeted query dominance; deletion propagation across projections; benign migration false-positive rate

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Source Admission and Quarantine

Technique ID: `retrieval.security.source-admission-quarantine` · Stage: `ingestion` · Risk: `high`

Authenticates connectors and provenance, quarantines new or changed content, scans untrusted files in isolation and promotes only versioned policy-compliant artifacts into retrieval indexes.

Use when: Users or external connectors can add or change corpus content; Retrieved evidence can influence consequential answers or actions

Avoid when: The corpus is a fixed application-owned build artifact with equivalent release controls; Quarantine state is not excluded from all production indexes and caches

Failure modes: A compromised trusted connector bypasses review; Hidden or multimodal instructions evade scanning; Quarantined chunks leak through stale indexes

Required evals: poisoned and hidden-content documents; connector identity compromise; quarantine index exclusion; change and rollback propagation

Evidence: `E3` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Retrieved Instruction and Data Separation

Technique ID: `retrieval.security.untrusted-context-separation` · Stage: `context-assembly` · Risk: `high`

Labels, delimits and bounds retrieved material as untrusted evidence and prevents it from directly supplying system instructions, credentials, tool authority or canonical memory writes.

Use when: External or user-controlled content enters the model context; Retrieved evidence may influence tools or memory

Avoid when: The generator cannot preserve message roles or content boundaries; The application treats delimiters as a complete prompt-injection defense

Failure modes: The model follows malicious text despite delimiters; Generated summaries erase trust labels; Tool parameters are copied from evidence without policy review

Required evals: direct and indirect injection; context flooding and source concentration; summary trust-label preservation; tool and memory influence attempts

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Archive-based Agent Variant Search

Technique ID: `rsi.archive-variant-search` · Stage: `improvement` · Risk: `high`

Branches versioned agent variants over a bounded code or configuration surface and retains diverse validated stepping stones instead of one greedy lineage.

Use when: The agent implementation has modular sandbox-testable components; Diverse variants may solve different task slices

Avoid when: The evaluator or deployment authority is inside the mutable surface; Generated changes cannot be sandboxed and code-reviewed

Failure modes: Benchmark exploitation masquerades as capability gain; Unsafe code escapes the sandbox; Archive selection collapses to one noisy metric

Required evals: untouched-task improvement; archive diversity by failure slice; sandbox escape tests; equal-budget comparison to fixed optimizer

Evidence: `E2` from `source-bounded-improvement-techniques-2026-08`; reviewed `2026-09-12`.

### Bounded Prompt and Demonstration Search

Technique ID: `rsi.bounded-prompt-search` · Stage: `improvement` · Risk: `high`

Searches a declared prompt and demonstration surface under a fixed task metric, rollout budget, baseline and protected selection split.

Use when: Behavior can improve without changing model weights or runtime authority; A representative development and selection set exists

Avoid when: The target failure is caused by missing tools data or deterministic logic; Prompt changes can silently expand permissions or mutable policy

Failure modes: Optimizer overfits visible examples; Prompt grows in cost or brittleness; Gain fails to transfer across model versions

Required evals: selection and hidden-holdout delta; token latency and cost delta; cross-model transfer check; immutable safety sentinel pass

Evidence: `E3` from `source-bounded-improvement-techniques-2026-08`; reviewed `2026-10-12`.

### Canary Promotion with Kill Switch and Rollback

Technique ID: `rsi.canary-kill-rollback` · Stage: `improvement` · Risk: `high`

Deploys an approved variant to bounded traffic with immutable monitors, automatic kill thresholds, version-pinned rollback and retained baseline capacity.

Use when: A candidate passed offline promotion gates but production uncertainty remains; Traffic and side effects can be isolated or compensated

Avoid when: Irreversible actions can occur before monitoring reacts; Baseline artifacts or rollback dependencies are unavailable

Failure modes: Candidate mutates the monitor or kill path; Rollback restores code but not corrupted state; Low traffic misses rare catastrophic failures

Required evals: kill-switch fire drill; state rollback verification; canary-baseline online delta; rare-event risk review

Evidence: `E2` from `source-bounded-improvement-techniques-2026-08`; reviewed `2026-09-12`.

### Fixed Evaluator Improvement Epoch

Technique ID: `rsi.fixed-evaluator-epoch` · Stage: `improvement` · Risk: `high`

Freezes task manifests, metrics, judges, safety sentinels and evaluator hashes within an optimization epoch and governs objective changes at explicit boundaries.

Use when: Candidates are generated iteratively from evaluation feedback; Evaluator changes may otherwise invalidate comparisons

Avoid when: The candidate can read or modify hidden evaluator artifacts; Before and after scores come from incompatible task versions

Failure modes: Candidate indirectly influences evaluator inputs; Silent judge update changes historical scores; New objective drops old safety constraints

Required evals: artifact hash verification; old-new objective compatibility audit; sentinel continuity; rescore stability

Evidence: `E2` from `source-bounded-improvement-techniques-2026-08`; reviewed `2026-09-12`.

### Paired Multi-objective Promotion Gates

Technique ID: `rsi.paired-promotion-gates` · Stage: `improvement` · Risk: `high`

Promotes only candidates that beat the same baseline on paired protected tasks while passing immutable safety regressions and explicit cost latency budgets.

Use when: An optimizer proposes changes for production consideration; Quality safety and efficiency must not collapse into one scalar

Avoid when: Candidate and baseline use different tasks or environment snapshots; A single successful replay is the only evidence

Failure modes: Aggregate gain hides a protected-slice regression; Repeated trials are correlated; Selection set becomes optimization training data

Required evals: paired delta and confidence interval; hard-gate violations by slice; cost and latency Pareto report; independent holdout confirmation

Evidence: `E2` from `source-bounded-improvement-techniques-2026-08`; reviewed `2026-10-12`.

### Risk-scoped Approval Interrupt

Technique ID: `runtime.approval-interrupt` · Stage: `runtime` · Risk: `high`

Pauses before a sensitive tool call, presents the canonical action and arguments to an authorized reviewer, then durably records approve edit or reject.

Use when: An action is irreversible financial external or privilege-changing; Policy requires accountable human authorization

Avoid when: The reviewer cannot inspect the real action and consequences; High-volume low-risk calls would create approval fatigue

Failure modes: Approval replay authorizes a semantically new action; Reviewer rubber-stamps unclear requests; Resumed state executes stale arguments

Required evals: unauthorized execution rate; approval decision comprehension; semantic replay tests; pause resume state integrity

Evidence: `E2` from `source-runtime-techniques-2026-08`; reviewed `2026-09-12`.

### Bounded Action and Observation Loop

Technique ID: `runtime.bounded-action-loop` · Stage: `runtime` · Risk: `medium`

Interleaves model decisions with typed tool observations until a deterministic stop condition or hard execution budget is reached.

Use when: The task requires a short adaptive sequence of tool calls; The next useful action depends on the latest tool observation

Avoid when: A deterministic workflow fully specifies the steps; External actions are unsafe without a separate policy gateway

Failure modes: Looping without measurable progress; Hallucinated completion despite unmet state; Budget exhaustion after repeated equivalent calls

Required evals: task success from external state; tool argument validity; stagnation and duplicate-call rate; steps latency and cost distribution

Evidence: `E3` from `source-runtime-techniques-2026-08`; reviewed `2026-10-12`.

### Scoped Coding-Agent Instruction Stack

Technique ID: `runtime.coding-agent-instruction-stack` · Stage: `runtime` · Risk: `medium`

Separates current task constraints, stable repository instructions, nested package rules and product-specific adapters so only applicable verified guidance enters the coding agent context.

Use when: A repository is used with one or more coding-agent products; Project commands conventions and protected boundaries must persist across sessions

Avoid when: The task is a one-off outside a maintained repository; The target agent surface does not support or has not been tested for the chosen instruction files; The proposed content is a generic repository overview with no observed project deficit

Failure modes: Conflicting nested rules cause nondeterministic behavior; A product or cloud surface discovers different files than expected; Copied documentation becomes stale while appearing authoritative; Context bloat increases tokens without improving correctness; Rules duplicate deterministic lint or leak task-specific procedures into always-loaded context; Final task success hides violation of an individual operational rule

Required evals: instruction discovery and precedence test; path-scope activation and exclusion test; rule-level compliance including against-default cases; cross-surface conflict test; paired representative task comparison with and without instructions; runtime token and cost comparison; stale conflict lint leakage and context-budget regression test

Evidence: `E3` from `source-coding-agent-harness-and-skills-evidence-2026-08`; reviewed `2026-09-16`.

### Custom Minimal Agent Runtime

Technique ID: `runtime.custom-minimal-runtime` · Stage: `runtime` · Risk: `medium`

Implements one application-owned model and tool loop with typed state, deterministic stop rules, hard budgets and explicit policy boundaries.

Use when: The workflow is narrow enough that the entire control loop remains auditable; The application needs exact control without graph or harness abstractions

Avoid when: Runs require durable pause and resume across process failure; The team is beginning to rebuild generic checkpoint, sandbox, streaming or concurrency infrastructure

Failure modes: Home-grown retry duplicates external effects; State migration and cancellation logic remain incomplete; Observability and provider edge cases accumulate without dedicated ownership

Required evals: task success against external state; crash and duplicate-delivery recovery; unauthorized action rate; latency cost and operator-effort comparison

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`, `source-runtime-techniques-2026-08`; reviewed `2026-10-13`.

### Deep Agents Long-Horizon Harness

Technique ID: `runtime.deepagents-harness` · Stage: `runtime` · Risk: `high`

Adds planning, subagents, filesystem workspaces, context offloading, skills, memory, shell tools and human approval over a LangGraph runtime.

Use when: A long-horizon research or coding worker needs most harness capabilities together; Workspace isolation and delegated subagent contexts are explicit requirements

Avoid when: Only a small embedded tool loop is required; No real sandbox can constrain filesystem, shell and network authority

Failure modes: Broad default capabilities exceed workload authority; Tool or sandbox configuration exposes host data and commands; Harness and LangGraph upgrade behavior leaks through the abstraction

Required evals: sandbox escape and filesystem boundary tests; subagent fan-out cost and completion rate; context offload retrieval fidelity; pinned-version upgrade and checkpoint compatibility

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### DeerFlow Super-Agent Harness

Technique ID: `runtime.deerflow-harness` · Stage: `runtime` · Risk: `high`

Provides a full agent harness with planning, subagents, memory, skills, workspaces, channels, gateway APIs and selectable local or isolated sandbox providers.

Use when: The product needs an integrated research or coding super-agent surface; Gateway, channels, skills and workspace execution would otherwise be assembled separately

Avoid when: The application needs an embeddable minimal runtime library; The deployment would enable host shell access without isolation and tenant controls

Failure modes: Local sandbox is mistaken for a security boundary; Large integrated surface increases patch and configuration burden; Major-version rewrites create migration and compatibility risk

Required evals: sandbox and host-access threat tests; gateway authentication and tenant-isolation tests; v1 or prior-system migration rehearsal; end-to-end workload cost latency and recovery

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### Durable Checkpoint and Side-effect Ledger

Technique ID: `runtime.durable-checkpoint-ledger` · Stage: `runtime` · Risk: `high`

Persists typed run state at safe boundaries and records idempotency keys, authorization consumption and external effects before retry or resume.

Use when: Runs must survive process failures or long approval delays; Retries can duplicate costly or irreversible effects

Avoid when: The task is short read-only and safely restartable; Only chat history is available while external state cannot be reconciled

Failure modes: Checkpoint omits operating-system or remote state; Non-idempotent sink duplicates an accepted action; Schema migration makes pending runs unreadable

Required evals: crash injection recovery correctness; duplicate side-effect rate; checkpoint overhead; old-state migration and resume tests

Evidence: `E2` from `source-runtime-techniques-2026-08`; reviewed `2026-09-12`.

### Evaluated Project Skill Package

Technique ID: `runtime.evaluated-project-skill-package` · Stage: `runtime` · Risk: `high`

Packages one repeated project workflow as a progressively disclosed SKILL.md with explicit triggers inputs outputs stop conditions and optional deterministic scripts or references, admits it as a pinned dependency, then promotes it only after paired fresh-context evaluation.

Use when: A project workflow is repeated and requires non-obvious repository knowledge; Baseline tasks show a specific procedure improves agent reliability

Avoid when: The model already performs the workflow reliably without the skill; The content is an always-applicable project fact or a mechanical invariant better placed in instructions or CI; The skill source scripts assets or required authority cannot be reviewed and pinned

Failure modes: Generic LLM-written guidance adds no value over the baseline; Description causes false activation or misses relevant requests; Vendor extensions make the skill non-portable or silently change authority; Large instructions crowd out task context and reduce adherence; Version-mismatched advice conflicts with the repository; Copied skill instructions or scripts create a supply-chain path to unauthorized effects; Relevant-looking guidance causes implementation omissions or excessive verification

Required evals: should-trigger and should-not-trigger activation set; repository language dependency artifact-path permission and cost eligibility checks; fresh-context with-skill versus baseline or semantically matched task comparison; deterministic artifact and assertion checks; token latency and tool-call overhead comparison; unsupported input and unsafe-action stop tests; content digest authority and adversarial admission review

Evidence: `E3` from `source-coding-agent-harness-and-skills-evidence-2026-08`; reviewed `2026-09-16`.

### Google Agent Development Kit Runtime

Technique ID: `runtime.google-adk-runtime` · Stage: `runtime` · Risk: `medium`

Uses a stateless runner over session, artifact and memory services with event persistence, tools, plugins and sequential, parallel, loop and LLM agents.

Use when: The application needs modular sessions, events, tools and multi-agent patterns; Google ecosystem integration is useful but model and deployment adapters remain explicit

Avoid when: A very small control loop would avoid the service abstractions; Cross-provider parity, residency or non-Google deployment has not been tested

Failure modes: In-memory services are carried into production without durability; Ecosystem-optimized defaults create practical provider or hosting lock-in; Session compaction loses evidence needed for later decisions

Required evals: session persistence and event ordering; provider and deployment parity; compaction fidelity and provenance retention; tool authorization and multi-tenant isolation

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### LangGraph Explicit State Runtime

Technique ID: `runtime.langgraph-runtime` · Stage: `runtime` · Risk: `medium`

Executes an application-defined graph over typed state with checkpointers, resumable threads and explicit interrupts for external input or approval.

Use when: Control flow requires inspectable branches, cycles or approval suspension; Application code must own state transitions while reusing checkpoint and resume machinery

Avoid when: A short linear loop is sufficient; The team expects graph checkpointing to make arbitrary external effects exactly-once

Failure modes: Replayed nodes repeat non-idempotent effects; Thread identity or checkpoint schema is migrated incorrectly; Fine-grained graphs add debugging and synchronization overhead

Required evals: checkpoint crash and resume replay; duplicate external-effect rate; interrupt authorization and stale-approval handling; state-schema migration and rollback

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### Microsoft Agent Framework Runtime

Technique ID: `runtime.microsoft-agent-framework` · Stage: `runtime` · Risk: `medium`

Combines agents, sessions, graph workflows, checkpoint storage, approval-required tools and optional self-hosted or durable Microsoft infrastructure integrations.

Use when: Python or .NET teams need explicit workflows and Microsoft ecosystem integrations; Checkpointed workflows, approval and hosting helpers match the application boundary

Avoid when: Required language or hosting surfaces remain preview and cannot be isolated; Bulk-synchronous superstep barriers conflict with latency or independent branch requirements

Failure modes: Preview package changes break state or hosting contracts; Checkpoint objects or storage reads alias mutable state instead of preserving snapshots; Concurrent branches create unreachable sibling lineage; Pending request types fail restricted serialization or resume; Superstep barriers serialize progress behind slow parallel branches; Application assumes hosting helpers provide authentication or tenant authorization

Required evals: release-pinned immutable checkpoint snapshot after restore; storage-read isolation including nested mutable state; concurrent sibling lineage and latest-lineage reachability; pending-request serialization round trip; upgrade downgrade resume and rollback rehearsal; crash injection around authoritative effects with duplicate omitted and unauthorized-effect counters; superstep latency under asymmetric fan-out; session-key authorization and tenant isolation

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`, `source-runtime-boundary-regression-evidence-2026-08`; reviewed `2026-09-17`.

### OpenAI Agents SDK Runtime

Technique ID: `runtime.openai-agents-sdk` · Stage: `runtime` · Risk: `medium`

Provides a lightweight runner for tools, handoffs, guardrails, sessions, serialized approvals, streaming, usage accounting and trace emission.

Use when: A Python application needs a small conventional agent SDK with sessions and approvals; OpenAI Responses integration is preferred while third-party model adapters remain optional

Avoid when: Durable multi-day recovery is required without an additional workflow integration; Default trace export or provider coupling conflicts with governance requirements

Failure modes: Session history is mistaken for durable side-effect recovery; Sensitive trace data is exported under unsafe defaults; Provider or hosted-tool assumptions leak into application design

Required evals: multi-turn and serialized approval resume; trace redaction and egress audit; max-turn retry and tool-error behavior; durable integration crash and duplicate-effect tests

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### OpenClaw Operational Agent Platform

Technique ID: `runtime.openclaw-platform` · Stage: `runtime` · Risk: `high`

Hosts persistent agents behind a gateway with sessions, channels, tools, skills, plugins, runtime selection and policy-aware operational configuration.

Use when: A persistent multi-channel personal or team agent host is the product boundary; Gateway, session, tool, skill and plugin operations need one managed control plane

Avoid when: The application only needs an embeddable model-tool loop; The team cannot operate and harden the larger gateway and plugin surface

Failure modes: Gateway or channel binding crosses tenant or identity boundaries; Plugins expand authority or dependency risk without review; Frequent platform changes outpace configuration and rollback testing

Required evals: gateway authentication and channel-routing isolation; plugin fail-closed and permission tests; session recovery and stale-state handling; versioned configuration migration and rollback

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### Typed Plan and Execute State Machine

Technique ID: `runtime.plan-execute-state-machine` · Stage: `runtime` · Risk: `medium`

Separates planning from execution and records typed task states, dependencies, results and replanning decisions in an explicit state machine.

Use when: Tasks have multiple dependent steps and inspectable milestones; Recovery or audit requires explicit intermediate state

Avoid when: A single bounded action loop is sufficient; The environment changes too quickly for a reusable plan

Failure modes: Plan becomes stale after environment changes; Planner invents dependencies or impossible steps; Executor follows a flawed plan without verification

Required evals: milestone completion accuracy; plan validity before execution; replan precision and recall; task success versus action-loop baseline

Evidence: `E2` from `source-runtime-techniques-2026-08`; reviewed `2026-10-12`.

### Pydantic AI Typed Agent Runtime

Technique ID: `runtime.pydantic-ai-runtime` · Stage: `runtime` · Risk: `medium`

Builds typed Python agents with validated dependencies, tools and outputs and attaches optional Temporal, DBOS, Prefect or Restate durable execution.

Use when: Typed Python boundaries and provider flexibility are primary requirements; Durability should be composed through a supported workflow integration

Avoid when: The product requires a complete multi-channel operational agent platform; The team cannot test replay constraints imposed by the selected durable backend

Failure modes: Schema validation creates false confidence in semantic correctness; A client-supplied provider object reference is resolved with application credentials; Durable replay conflicts with dynamic or non-deterministic tool behavior; Rapid capability API evolution breaks wrappers or plugins

Required evals: typed-output validity and semantic correctness; cross-principal provider-file and object-reference authorization; affected and patched UI-adapter negative controls when adopted; provider parity on application cases; durable crash and replay compatibility; upgrade migration for capability and tool interfaces

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`, `source-runtime-boundary-regression-evidence-2026-08`; reviewed `2026-09-17`.

### Transactional Side-Effect Ledger

Technique ID: `runtime.safety.transactional-effect-ledger` · Stage: `runtime` · Risk: `high`

Assigns runtime-generated causal operation identities and records authorization, intent, commit and reconciliation state around non-idempotent external effects.

Use when: Retries or resume can repeat irreversible effects; External sinks support idempotency or reconciliation

Avoid when: The task is read-only; No authoritative commit or reconciliation signal exists

Failure modes: Semantic duplicates use different operation IDs; Authority expires between plan and commit; Remote effect succeeds while ledger commit fails

Required evals: crash injection around commit boundaries; duplicate-effect rate under retry and concurrency; commit-time authorization revocation; reconciliation and compensation drill

Evidence: `E2` from `source-runtime-techniques-2026-08`; reviewed `2026-09-12`.

### Security Budget Breaker and Kill Switch

Technique ID: `runtime.security.budget-kill-switch` · Stage: `runtime` · Risk: `high`

Enforces external step, time, token, cost, fan-out, retry and delegation limits and can revoke credentials and stop execution independent of model cooperation.

Use when: Agent loops can retry delegate or execute costly actions; Operators need bounded incident containment

Avoid when: The breaker cannot terminate workers or revoke downstream authority; Limits are embedded only in the system prompt

Failure modes: Workers continue with cached credentials; Nested agents evade parent budgets; Breaker state is unavailable during incident

Required evals: budget bypass and nested fan-out; credential revocation propagation; kill-switch recovery time; partial failure and restart behavior

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Deterministic Capability Policy Gateway

Technique ID: `runtime.security.capability-policy-gateway` · Stage: `runtime` · Risk: `high`

Intercepts every proposed tool or peer-agent action and evaluates canonical identity, delegation, operation, resource, arguments, risk and budget before execution.

Use when: Model output can cause external actions or data access; Multiple tools or agents need one enforceable policy boundary

Avoid when: The workload has no tool data or external-action authority; The gateway cannot observe or block every execution path

Failure modes: A tool bypasses the gateway through a direct client; Adapters normalize arguments inconsistently; Policy outage or error fails open

Required evals: direct and indirect policy bypass; canonical argument ambiguity; policy outage fail-closed behavior; revocation and audit correlation

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Delegated Short-lived Agent Identity

Technique ID: `runtime.security.delegated-short-lived-identity` · Stage: `runtime` · Risk: `high`

Uses a stable auditable agent identity plus task-scoped short-lived credentials that preserve the invoking user and delegated resource scope across calls.

Use when: Agents access protected data or external systems; Actions must be attributed to both agent and invoking principal

Avoid when: The workload is anonymous and limited to public read-only data; Downstream services cannot enforce scoped identity

Failure modes: A broad service credential replaces user delegation; Tokens outlive approval or task state; Peer agents drop or forge delegation context

Required evals: cross-user and cross-tenant denial; token expiry during long run; revocation before execution; delegation integrity across agent hops

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### Agent Extension Supply-chain Scan

Technique ID: `runtime.security.extension-supply-chain-scan` · Stage: `runtime` · Risk: `high`

Scans skills plugins hooks MCP manifests scripts binaries and dependencies with deterministic rules and optional semantic analysis before human review and pinned admission.

Use when: Agents install portable skills plugins or third-party MCP servers; Extension code and instructions change independently of the application

Avoid when: A scanner verdict would automatically grant authority; Encrypted compiled multimodal or staged behavior cannot be inspected

Failure modes: Clean scan is mistaken for proof of safety; LLM scanner misses staged behavior or creates false positives; Scanner itself receives broad secrets or egress

Required evals: known malicious extension corpus; benign false-positive corpus; staged and environment-dependent behavior; scanner isolation and version regression

Evidence: `E2` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Isolated Tool and Code Sandbox

Technique ID: `runtime.security.isolated-tool-sandbox` · Stage: `runtime` · Risk: `high`

Executes generated code and high-risk tools in a disposable tenant-scoped environment with bounded resources, explicit mounts, no inherited secrets and deny-by-default egress.

Use when: Agents execute generated code or untrusted parsers; Tenant workloads require a containment boundary from host and peers

Avoid when: All operations are schema-bound remote APIs with no local execution; The sandbox configuration exposes host sockets broad mounts or ambient credentials

Failure modes: Writable host mounts or container socket defeat isolation; Shared credentials or caches cross tenant boundaries; Unrestricted egress enables exfiltration or command-and-control

Required evals: escape and host-access probes; secret and metadata-service denial; egress allowlist bypass; resource exhaustion and cleanup

Evidence: `E2` from `source-agentic-security-landscape-2026-08`; reviewed `2026-10-13`.

### MCP and Plugin Admission Control

Technique ID: `runtime.security.mcp-plugin-admission` · Stage: `runtime` · Risk: `high`

Inventories, pins, scans and approves MCP servers, plugins and tool manifests, then monitors identity, schema, advisories and behavior drift before exposing capabilities to agents.

Use when: Tools are discovered or updated independently of application releases; Third-party MCP servers or plugins extend runtime authority

Avoid when: The application has a fixed internal tool set compiled into one release; The control plane cannot block unknown or changed manifests

Failure modes: A trusted name points to a changed server or package; An admitted pinned release contains a reachable implementation vulnerability; Tool descriptions contain hidden instructions; Runtime auto-discovers an unregistered endpoint

Required evals: manifest drift signature and advisory-policy failure; typosquatting and name-collision tests; hidden instruction and schema-change probes; unknown endpoint fail-closed behavior; vulnerable and first-patched release replay when an affected server is adopted

Evidence: `E2` from `source-agentic-security-landscape-2026-08`, `source-runtime-boundary-regression-evidence-2026-08`; reviewed `2026-09-17`.

### MCP Resource-bound Authorization

Technique ID: `runtime.security.mcp-resource-bound-authorization` · Stage: `runtime` · Risk: `high`

Validates issuer, audience, resource, scope and user delegation for each protected remote MCP request and obtains separate credentials for downstream APIs instead of forwarding inbound tokens.

Use when: Remote MCP servers expose user-specific or sensitive operations; MCP proxies call protected downstream APIs

Avoid when: A local stdio server has no remote authorization surface; The server accepts generic bearer audiences or uses sessions as authentication

Failure modes: Inbound tokens are passed to upstream APIs; Generic audience tokens work across servers; Session identifiers substitute for authenticated identity

Required evals: wrong audience issuer and realm; token passthrough denial; consent replay and scope escalation; expiry revocation and session mix-up

Evidence: `E2` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Risk-tiered Agent Sandbox Profile

Technique ID: `runtime.security.risk-tiered-sandbox-profile` · Stage: `runtime` · Risk: `high`

Maps workload adversary, tenancy, secrets and consequence to a hardened container, userspace-kernel, microVM or dedicated-node profile with explicit mounts, credentials, egress and lifecycle controls.

Use when: Agents execute generated code parsers browsers or shell commands; Different workloads justify different isolation cost and strength

Avoid when: The selected runtime is treated as secure without configuration tests; Host sockets broad mounts or ambient credentials remain exposed

Failure modes: Control-plane authorization exposes other sandboxes; Persistent snapshots retain secrets or poison; Network redirects bypass domain allowlists

Required evals: escape and host interface denial; cross-tenant state and snapshot restore; credential and metadata service access; DNS redirect egress and cleanup failure

Evidence: `E2` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Strict Agent Tool Contract

Technique ID: `runtime.security.strict-tool-contract` · Stage: `runtime` · Risk: `high`

Constrains tool calls with closed schemas, typed enums, canonical paths and URLs, bounded sizes and explicit effect classes before policy and execution.

Use when: Model-generated arguments reach filesystem network shell or mutable APIs; Tool ambiguity can expand agent authority

Avoid when: The operation cannot be represented without unrestricted code or shell text; Validation occurs only after interpolation or side effects

Failure modes: Validated strings are later shell-interpolated; Newlines or command substitutions create a second command; Symlinks encoded separators or dashboard identifiers escape canonical roots; DNS is validated before a later re-resolution or redirect; An opaque object reference is resolved with broader application authority; Schema labels a destructive operation as read-only

Required evals: newline command substitution and shell metacharacters; path traversal with encoded mixed separators symlinks and archive escape; DNS rebinding redirects link-local and metadata endpoints; cross-principal object-reference authorization; undeclared fields size and type confusion; fixed-version negative controls for adopted affected dependencies

Evidence: `E2` from `source-agentic-security-verification-2026-08`, `source-runtime-boundary-regression-evidence-2026-08`; reviewed `2026-09-17`.

### Untrusted Project Configuration Admission

Technique ID: `runtime.security.untrusted-project-config-admission` · Stage: `runtime` · Risk: `high`

Prevents repository branches, pull requests and downloaded workspaces from auto-enabling agent configuration, skills, hooks or MCP commands until an immutable diff and authority request are approved.

Use when: Coding agents run against third-party branches or pull requests; Repositories can define agent hooks skills or MCP servers

Avoid when: The workspace is an immutable application-owned release with equivalent admission; Privileged automation cannot disable project-local configuration

Failure modes: A mutable branch changes configuration after approval; Transitive scripts or package hooks remain hidden; Automation loads user-level and project-level settings together

Required evals: malicious pull request MCP config; post-approval branch mutation; transitive hook and package execution; secret access from untrusted workspace

Evidence: `E2` from `source-agentic-security-verification-2026-08`; reviewed `2026-10-13`.

### Temporal Durable Workflow Substrate

Technique ID: `runtime.temporal-durable-substrate` · Stage: `runtime` · Risk: `high`

Runs deterministic workflows and retryable activities on a durable orchestration service so long waits and process failures can resume from persisted history.

Use when: Agent work spans process restarts, timers, human waits or distributed workers; A separate durable substrate is justified by recovery-time and reliability objectives

Avoid when: A short in-process task can safely restart from the beginning; The team expects workflow durability to provide exactly-once external effects automatically

Failure modes: Non-deterministic workflow code fails replay; Activities duplicate non-idempotent external effects; Operational complexity exceeds the workload reliability benefit

Required evals: worker crash and workflow replay; activity idempotency and duplicate delivery; long-wait cancellation and authorization refresh; recovery time objective and operational load

Evidence: `E2` from `source-agent-runtime-framework-landscape-2026-08`; reviewed `2026-10-13`.

### Pre-execution Tool Policy Gateway

Technique ID: `runtime.tool-policy-gateway` · Stage: `runtime` · Risk: `high`

Normalizes every proposed tool action and enforces identity, scope, argument, destination and risk policy before dispatch.

Use when: Agents can access sensitive data or side-effecting tools; Tool descriptions or observations may contain untrusted instructions

Avoid when: The runtime exposes no tools or external resources; A post-hoc output filter is being mistaken for pre-execution control

Failure modes: Ambiguous actions are incorrectly allowed; Obfuscated arguments bypass normalization; Policy decision ignores multi-step action chains

Required evals: adversarial tool-call block recall; benign-call false block rate; policy decision latency; cross-step escalation detection

Evidence: `E2` from `source-runtime-techniques-2026-08`; reviewed `2026-09-12`.
