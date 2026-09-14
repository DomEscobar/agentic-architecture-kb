---
id: source-research-radar-2026-08-30
type: source
title: Biweekly Agentic Architecture Research Radar 2026-08-30
status: inbox
privacy: internal
confidence: 0.89
created_at: 2026-08-30T07:00:00+02:00
updated_at: 2026-08-30T07:00:00+02:00
review_at: 2026-09-13
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

# Biweekly Agentic Architecture Research Radar — 2026-08-30

This is an automated research candidate, not reviewed knowledge. All 18 queries
in the six configured packs were executed for the interval beginning
2026-08-16. Primary repositories, releases, commits, registries, reviewed
advisories, recent papers and artifacts, GitHub issues, and technical-forum
threads were inspected. The configured web-search provider and arXiv API were
unavailable or rate-limited, so discovery also used OpenAlex, direct arXiv page
retrieval, the GitHub API and Advisory Database, package registries, and the
Hacker News API. An upstream advisory, its GHSA mirror, its fix commit, and its
release note are one provenance chain, not independent corroboration.

## 1. Newly reviewed verifier, LLM gateway, URL-fetch and language-sandbox failures

**Classification:** security-critical  
**Evidence:** E2, reviewed upstream advisories with vulnerable code paths,
proofs of concept, regression fixes and obtainable patched artifacts; no
independent reproduction was found in this run.

Five advisories published on 2026-08-28 expose failures that deterministic
infrastructure is specifically expected to prevent:

- AIIR before 1.7.0 could return success from signing, CI, release-policy and
  signature-verification paths without enforcing the represented control. The
  maintainer explicitly classifies the review as internal, not third-party.
  PyPI provides 1.7.0.
- 9router before 0.5.2 had two distinct authorization bypasses. One treated a
  client-controlled `Host: localhost` header as proof of loopback origin while
  binding to `0.0.0.0` by default; this exposed the operator-funded LLM proxy
  and a caller-selected SearXNG base URL. The other authorized the pre-rewrite
  path but rewrote unprotected `/codex/*` requests into the protected LLM
  backend. The advisory includes a live default-configuration reproduction.
  npm currently provides 0.5.59.
- Bifrost core before 1.5.17 allowed CGNAT, 6to4, NAT64 and deprecated IPv6
  site-local destinations through the only address guard on caller-selected
  Bedrock and Vertex image or document URLs. The provided test proves that the
  real fetch path attempts a dial, but the metadata-service impact still
  depends on deployment routing. The named fixed release is available.
- RestrictedPython through 8.2 omitted positional-only argument names from its
  protected-hook validation. Sandboxed code could shadow `_getattr_`,
  `_getitem_`, `_write_` or `_print_` and bypass the embedding application's
  policy hook. PyPI provides 8.3 and later; 8.5 was current at check time.

These are direct counterexamples to treating a reported verifier result,
middleware prefix list, client header, IP deny-list or language-level rewrite
as a complete enforcement boundary. The RestrictedPython primitive is not by
itself a universal host escape; its worst effects depend on unsafe capabilities
provided by the embedding application.

**Affected claims/cards:**

- `claim-runtime-security-external-enforcement`
- `claim-runtime-side-effect-boundary`
- `claim-sandbox-boundary-configured`
- `claim-eval-deterministic-before-judge`
- `runtime.security.capability-policy-gateway`
- `runtime.security.strict-tool-contract`
- `runtime.security.isolated-tool-sandbox`
- `evaluation.deterministic-state-oracle`

Sources:

- https://github.com/advisories/GHSA-73p9-6hrp-8qhr
- https://pypi.org/project/aiir/1.7.0/
- https://github.com/advisories/GHSA-86m2-fcxq-5q7c
- https://github.com/advisories/GHSA-8gmq-j984-vp4r
- https://github.com/decolua/9router/releases/tag/v0.5.2
- https://www.npmjs.com/package/9router/v/0.5.59
- https://github.com/advisories/GHSA-w98g-5w9p-p3rc
- https://github.com/maximhq/bifrost/releases/tag/core/v1.5.17
- https://github.com/advisories/GHSA-ffg3-p8fm-mjx2
- https://pypi.org/project/RestrictedPython/8.3/

## 2. Previously missing security and checkpoint fixes reached releases

**Classification:** confirmed  
**Evidence:** E2 maintainer release notes, linked fix commits and regression
tests; no independent replay was performed in this run.

Google ADK Python 2.8.0, released 2026-08-25, includes the fixes previously
verified only on the default branch: it stops `RemoteA2aAgent` from forwarding
credential requests to a remote peer, restricts registry credentials to Google
API endpoints, attaches default credentials only to HTTPS endpoints, guards
BigQuery tools against SQL injection, redacts credentials from debug output,
and fences relayed agent output so it cannot pose as instruction. The release
also adds a configurable maximum LLM-call limit and per-workflow telemetry.

Temporal Python SDK 1.32.0, released 2026-08-24, provides worker-environment
references for hosted-tool and sandbox values so literal credentials do not
enter durable workflow history. It allowlists resolvable environment-variable
names, rejects sandbox host-path grants and caller-provided sandbox sessions,
and adds replay-safe OpenTelemetry providers so workflow replay does not
duplicate metrics and log events.

Microsoft Agent Framework Python 1.16.0, released 2026-08-28, fixes the
checkpoint aliasing reported in the 2026-08-16 radar: workflow checkpoints can
no longer be mutated outside storage implementations. The same release deep
copies state while discarding unsafe `Content` fields and preserves
backend-owned service-session snapshots. This confirms a fix for the mutable
snapshot report, but not for the adjacent concurrent-lineage and restricted-
deserialization resume reports; those remain open evidence gaps until their own
fixed releases and effect-level replays are identified.

**Classification of prior freshness statement:** possibly-stale

`reports/security-watch-latest.json` says that neither Google ADK nor Temporal
had a fixed general release at its 2026-08-21 check. That negative result was
correct at the time but is stale after 2.8.0 and 1.32.0. The report is a derived
machine artifact and was not edited by this run.

The 2026-08-16 radar's statement that Microsoft Agent Framework 1.14.0
checkpoint state was not a stable snapshot is also possibly stale for the
specific aliasing mechanism after Python 1.16.0. Its broader prerelease-quality
warning is not automatically cleared by this one fix.

**Affected claims/cards:**

- `claim-runtime-adoption-release-specific`
- `claim-runtime-side-effect-boundary`
- `claim-runtime-security-external-enforcement`
- `runtime.google-adk-runtime`
- `runtime.temporal-durable-substrate`
- `runtime.microsoft-agent-framework`
- `runtime.durable-checkpoint-ledger`
- `runtime.security.delegated-short-lived-identity`
- `runtime.security.strict-tool-contract`

Sources:

- https://github.com/google/adk-python/releases/tag/v2.8.0
- https://github.com/google/adk-python/commit/2aea8595fb1c5e0fddef7893a1985dc96dc82692
- https://github.com/google/adk-python/commit/cc275f0c75bc4d84a5fc315dd6f6bd8a82cb1155
- https://github.com/google/adk-python/commit/d6290a0b2e344a92b8879acfeab02e4252d1b47c
- https://github.com/temporalio/sdk-python/releases/tag/1.32.0
- https://github.com/temporalio/sdk-python/pull/1752
- https://github.com/temporalio/sdk-python/pull/1745
- https://github.com/microsoft/agent-framework/releases/tag/python-1.16.0
- https://github.com/microsoft/agent-framework/pull/7847

## 3. AnyDoc now fails explicitly on image-only pages instead of dropping them

**Classification:** confirmed  
**Evidence:** E2 maintainer release and typed error contract; no comparative
parser benchmark or independent reproduction was published with the release.

AnyDoc 0.2.4 reports every image-only page and page count through typed Rust,
Node, WebAssembly, Python and CLI errors. Earlier versions could silently omit
scanned pages or return a generic unsupported-document failure. Hosted OCR is
now an explicit opt-in fallback invoked only after the typed `needsOcr` result.

This confirms the current parser-routing requirement that coverage failures be
observable and routed, but it is not evidence that AnyDoc or Firecrawl Parse
has better OCR or downstream retrieval quality than competing parsers.

**Affected claims/cards:**

- `claim-parser-eval-by-slice`
- `claim-parser-routing-by-document`
- `claim-retrieval-diagnose-upstream-first`
- `parser.native.anydoc`

Source: https://github.com/firecrawl/anydoc/releases/tag/v0.2.4

## 4. Agent Sandbox v1.0.0 changes migration, routing and retry boundaries

**Classification:** confirmed  
**Evidence:** E2 official release notes and linked regression changes; no
independent isolation, migration or cross-site attack replay was performed.

Kubernetes Agent Sandbox 1.0.0 removes all `v1alpha1` APIs and conversion
webhooks. Direct upgrades from releases before 0.5.0 are unsupported: operators
must first migrate stored objects through 0.5.x and verify that every CRD stores
only `v1beta1`. The release also adds opt-in browser path routing with session
cookies and mandatory Origin validation, introduces the `sandboxd` runtime
which binds `0.0.0.0` by default, and prevents automatic retries of failed
non-idempotent `POST /execute` calls in the Python SDK.

This is a material adoption and migration change, not new evidence that the
sandbox boundary resists escape. Browser routing, externally reachable
`sandboxd`, session bootstrap and duplicate-execution recovery require new
release-pinned attack and migration cases before the card can be trusted for a
deployment.

**Affected claims/cards:**

- `claim-runtime-adoption-release-specific`
- `claim-runtime-side-effect-boundary`
- `claim-sandbox-boundary-configured`
- `runtime.security.isolated-tool-sandbox`
- `runtime.security.risk-tiered-sandbox-profile`

Source: https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v1.0.0

## 5. AutoSaddler is an artifact-backed bounded harness-optimization candidate

**Classification:** new-candidate  
**Evidence:** E2 preprint, MIT-licensed implementation, configurations, tests,
named baselines, test sets and ablations; all results are author-reported and
no independent reproduction was found.

AutoSaddler diagnoses mini-batches of failed traces, proposes typed prompt,
tool, middleware and loop patches, and retains updates through validation-aware
selection. The authors report absolute test gains of 9.0 percentage points on
GAIA2, 9.6 on SWE-Bench Pro and 10.0 on Terminal-Bench 2.0 over the respective
base harnesses. Their largest reported ablation is removal of
generalization-aware selection, which reduces GAIA2 Pass@1 from 62.0% to 50.6%.

This is evidence for a bounded, external harness search with validation and
regression control. It is not evidence of domain-general recursive
self-improvement: the mutable surface, benchmarks and selection procedure are
externally fixed, and the study does not show that generation N becomes a
better optimizer of generation N+1 under equal search budget.

**Affected claims/cards:**

- `claim-improvement-loop-bounded`
- `claim-eval-protected-holdout`
- `claim-runtime-one-primary-loop`
- `claim-coding-harness-replay-needs-hermetic-manifest`
- `rsi.paired-promotion-gates`
- `evaluation.protected-holdout`
- `evaluation.paired-perturbation-replay`

Sources:

- https://arxiv.org/abs/2608.23041
- https://github.com/microsoft/AutoSaddler
- https://autosaddler-projectpage.github.io/

## 6. VisDocAgentBench isolates where agentic visual retrieval helps

**Classification:** new-candidate  
**Evidence:** E2 recent preprint with balanced query construction, reviewed hard
negatives, shared output contracts and ablations; no public code, dataset or
independent reproduction was found.

VisDocAgentBench contains 2,375 pages from 100 visually rich documents and 120
unique-target queries balanced across direct, one-bridge and two-bridge
evidence. A visual late-interaction retriever reports 97.50% Recall@1 on direct
items but 2.50% on two-bridge items. Agentic planners recover some multi-bridge
loss, and the best visual route reports 67.50% Recall@1 versus 37.50% for the
OCR-text route. Ablations attribute gains to iterative search, page inspection
and complete support context.

The result supports modality-preserving retrieval and a specialist agentic
branch for relational queries. It does not justify agentic search for direct
lookup, nor establish transfer beyond this small closed corpus.

**Affected claims/cards:**

- `claim-visual-retrieval-separate-stage`
- `claim-visual-retrieval-page-stage`
- `claim-rag-search-task-dependent`
- `claim-scale-retrieval-before-agent`
- `multimodal.visual.late-interaction`
- `multimodal.query-routing`

Source: https://arxiv.org/abs/2608.17889

## 7. DreamBench-SWE adds a preregistered executable memory-hygiene audit

**Classification:** new-candidate  
**Evidence:** E3 unusually complete preprint with Apache-2.0 artifacts,
checksums, executable hidden oracles, preregistration, paired inference and
explicit conformance rejections; no independent reproduction was found.

DreamBench-SWE tests whether later software tasks use non-inferable evidence
from earlier sessions. Its original scaled fold preserves a null result: the
primary DF-hybrid versus B5 contrast was 95/180 versus 89/180 with clustered
`p=.518` and Holm-adjusted `p=1`; this is not evidence of equivalence. In the
separately preregistered successor, no external memory passed 21/180 cases,
deterministic verbatim event memory 82/180, a typed-plus-raw reference probe
83/180, and one pinned hosted Mem0 literal-storage configuration 97/180.

All three available comparisons against no memory rejected after Holm
correction, but both preregistered mechanism contrasts were unavailable after
pre-evaluation conformance rejection. The secondary literal-storage comparison
was nonconfirmatory or sensitivity-dependent. The result supports an immutable
event-log baseline and executable multi-session evaluation; it does not prove
superiority among memory-bearing mechanisms or general Mem0 product fit.

**Affected claims/cards:**

- `claim-memory-framework-workload-fit`
- `claim-memory-eval-full-lifecycle`
- `claim-memory-retrieval-can-hurt`
- `claim-memory-source-derived-separation`
- `memory.episodic-event-log`
- `memory.hybrid-read-router`
- `evaluation.deterministic-state-oracle`
- `evaluation.paired-perturbation-replay`

Sources:

- https://arxiv.org/abs/2608.20664
- https://github.com/iroiro147/dreambench-swe/releases/tag/v2.1.0

## 8. CatchBench makes auditability conditional on the available record

**Classification:** new-candidate  
**Evidence:** E3 unusually complete preprint, MIT-licensed code, packaged data,
fixed predictions and reproducible offline boards; borrowed and constructed
labels still limit external validity and no independent reproduction was found.

CatchBench evaluates auditing at three information states: declared
configuration before a run, a growing live prefix, and the finished trace. It
reports 72 entrants over 1,187 configurations and 1,162 recorded runs. Only 47
of 118 predeclared contrasts separate; unresolved comparisons remain
unranked. A trivial capability-order rule achieves perfect F1 on one of six
configuration sources, exposing a corpus-construction shortcut, and no tested
method flags a failing tau-bench run before completion.

This supports the current requirement to bind audit claims to available
evidence and to report unresolved comparisons and shortcut baselines. It does
not establish one universal agent-failure detector.

**Affected claims/cards:**

- `claim-agent-eval-multilayer`
- `claim-eval-deterministic-before-judge`
- `claim-judge-needs-admission-test`
- `evaluation.calibrated-trajectory-judge`
- `evaluation.deterministic-state-oracle`
- `evaluation.paired-perturbation-replay`

Sources:

- https://arxiv.org/abs/2608.22808
- https://github.com/yzhao062/catchbench

## 9. HarnessRisk and MaliciousSkillBench add lifecycle and source-disjoint security slices

**Classification:** new-candidate  
**Evidence:** E2 recent preprints plus public MIT/Apache-2.0 repositories and
datasets; results are author-reported and not independently reproduced.

HarnessRisk provides 128 sandboxed cases across configuration, capability
extension, runtime operation, state persistence, action control and incident
recovery. It evaluates three harnesses, six models and 14 model-harness
configurations over three sampling seeds. Reported attack success ranges from
12.6% to 80.9% while benign utility remains 75.0% to 97.6%. Configuration is
the weakest phase in all three harnesses, and high explicit risk recognition
does not imply that unsafe actions or persistent state changes are blocked.

MaliciousSkillBench normalizes 8,414 malicious records into 7,539 identities
and 4,588 structural families, then evaluates 9,740 skills after conflict
exclusion. Learned detectors report 0.882–0.932 Random Macro-F1 but only
0.653–0.665 under source-disjoint evaluation. The strongest reported TF-IDF
SVM retains 95.6% malicious recall but produces 62.4% benign false positives on
held-out sources. Off-the-shelf scanners occupy different but still weak
recall/false-positive regimes.

Together these results strengthen two existing evaluation requirements:
security belongs to the deployed model-plus-harness configuration, and an
extension scanner must be tested on structural/source-disjoint and benign
controls. Neither benchmark turns detection into authorization.

**Classification of registered scanner release:** confirmed

SkillSpector 2.11.0 now resolves exact direct and transitive npm versions from
`package-lock.json` and `npm-shrinkwrap.json`, and adds bounded inspection of
bundled lifecycle hooks, direct sensitive-data transfer and broad project
permission settings. Its maintainer reports 1,070 targeted regressions passing,
but Yarn and pnpm lockfiles remain out of scope and the release has no
independent source-disjoint evaluation. This capability change does not repair
the generalization gap measured by MaliciousSkillBench.

**Affected claims/cards:**

- `claim-agent-security-paired-state-evals`
- `claim-runtime-security-external-enforcement`
- `claim-coding-instructions-not-security-boundary`
- `runtime.security.extension-supply-chain-scan`
- `evaluation.security.adaptive-attack-replay`
- `evaluation.deterministic-state-oracle`

Sources:

- https://arxiv.org/abs/2608.17597
- https://github.com/Baiyajing/HarnessRisk
- https://huggingface.co/datasets/YajingB/HarnessRisk
- https://arxiv.org/abs/2608.19901
- https://github.com/protectskills/MaliciousSkillBench
- https://huggingface.co/datasets/ProtectSkills/MaliciousSkillBench
- https://github.com/NVIDIA/SkillSpector/releases/tag/v2.11.0

## Lane coverage, contradictions and negative results

### Agentic runtime release watch

**Classification:** no-material-change

Pydantic AI 2.36.0 adds named `@durable_operation` capabilities and a public
backend API for third-party durable engines. OpenSandbox server 0.2.3 adds
lifecycle hooks, opt-in QEMU VM-state pause/resume and machine-readable capacity
exhaustion while fixing caller-spoofable egress attribution and an informer
cache that could continue serving frozen status. Deep Agents 0.7.11 adds rubric-
grader hooks, and LangGraph SDK 0.4.4 adds thread-stream trace routing. These
are release-specific capability or defect changes; none supplies comparative
recovery, duplicate-effect, sandbox-escape or evaluator-calibration evidence.
They therefore do not change the current build-versus-adopt or safety defaults.

Sources:

- https://github.com/pydantic/pydantic-ai/releases/tag/v2.36.0
- https://github.com/opensandbox-group/OpenSandbox/releases/tag/server/v0.2.3
- https://github.com/langchain-ai/deepagents/releases/tag/deepagents%3D%3D0.7.11
- https://github.com/langchain-ai/langgraph/releases/tag/sdk%3D%3D0.4.4

### Agentic memory

**Classification:** no-material-change

ECHO's self-audit preserves negative evidence rather than presenting only its
development retrieval scores. On a separate matched 91-question QA sample,
Mem0 OSS scored 64.84% against ECHO's 41.76% with exact McNemar `p=.00107`,
while a history-cluster interval crossed zero. A post-hoc audit also found
source-specific phrases in ECHO's query-expansion rules, so expansion-enabled
retrieval results are explicitly descriptive rather than confirmatory. This
does not contradict the current architecture; it reinforces local framework
selection and contamination controls.

InjecMEM describes a single-interaction topic-conditioned memory injection
accepted at COLM 2026, but the abstract provides neither artifact link nor
denominators and exact attack-success results. It remains `weak-evidence` for
new quantitative claims while confirming the existing influence-gated write
and adversarial memory-replay test hypotheses.

Sources:

- https://arxiv.org/abs/2608.21755
- https://arxiv.org/abs/2608.23471

### Bounded self-improvement

**Classification:** weak-evidence

Prime Agent exposes code, persistent sessions, local harness refinement,
snapshot history and rollback, but its technical report's large Best@1 and
cross-task capability claims were not accompanied by an independent matched
reproduction in this run. Its `/refine` mechanism edits supplemental prompts,
memory and reusable specifications while leaving the base system prompt
immutable. That is bounded harness adaptation, not evidence that a better task
agent becomes a better future optimizer.

OptiMAS and CONTRAMEM report multi-benchmark improvements from evolving
multi-agent structure and procedural memory, respectively, but neither arXiv
page linked public code or cached runs at check time. Neither demonstrates the
generation-N-to-N+1 optimizer test required by the RSI boundary. They do not
change protected-holdout, fixed-evaluator epoch, paired promotion or rollback
requirements.

Sources:

- https://arxiv.org/abs/2608.23552
- https://github.com/PrimeIntellect-ai/prime-agent
- https://arxiv.org/abs/2608.21918
- https://arxiv.org/abs/2608.22533

### RAG, evaluations and technical forums

**Classification:** no-material-change

Recent parser and evaluation papers without linked artifacts did not establish
a new default or independently overturn a reviewed claim. Technical-forum
threads surfaced new runtime, memory and sandbox projects, but none supplied a
controlled reproduction or decision-grade comparison. They remain E1 discovery
signals and were not used to corroborate the paper or advisory findings above.

## Unresolved evidence gaps

- No newly published advisory above has an independent reproduction. GHSA,
  repository advisory, fix commit and release notes share upstream provenance.
- Google ADK 2.8.0 and Temporal 1.32.0 need fixed-version negative controls on
  the deployed adapters; release inclusion does not prove every downstream
  composition is safe.
- AutoSaddler needs an independent replay with immutable split manifests,
  budget accounting and forbidden mutation surfaces.
- VisDocAgentBench needs public corpus/query artifacts and transfer tests before
  its visual-agentic ranking can guide architecture selection.
- DreamBench-SWE needs independent execution of the published v2.1.0 bundle;
  its conformance-rejected mechanism contrasts must remain unavailable rather
  than inferred from secondary comparisons.
- CatchBench needs external replay and new-source validation; its own shortcut
  findings show why a single corpus cannot establish detector quality.
- HarnessRisk and MaliciousSkillBench need source-disjoint external validation,
  artifact safety review and workload-local authoritative state oracles.
- Current evidence still does not demonstrate domain-general RSI, indefinite
  safe self-improvement, or generation-to-generation optimizer improvement
  under equal information and search budgets.
