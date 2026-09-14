# Agentic Architecture KB review-gate proposal — 2026-08-31

Review state: **proposal only; human approval required**  
Promotion authority: **false**  
Inputs reviewed: `python3 tools/freshness.py due-reviews`,
`inbox/research-radar-2026-08-16.md`, and
`inbox/research-radar-2026-08-30.md`  
Due-review result: no due technique cards and no due claims as of 2026-08-31.

## Gate decision

Retain the August 30 security, release, parser, sandbox, bounded-optimization,
multimodal, memory-evaluation, auditability and extension-security findings as
reviewable proposals. None authorizes promotion. The release existence, advisory
ranges and public artifact surfaces were independently rechecked against GitHub,
PyPI/npm-linked release metadata and arXiv on 2026-08-31, but the empirical
results remain author or upstream-maintainer evidence without an independent
effect-level replay.

The August 16 inbox was re-inspected in full. Its six material candidates remain
bounded as in the 2026-08-24 review, except that Microsoft Agent Framework Python
1.16.0 now supplies an upstream fix for checkpoint aliasing. It does not resolve
the separate concurrent-lineage or restricted-deserialization reports. The six
older GHSA records retain the same affected and first-patched ranges and have not
been updated since August 12–14.

No reviewed canonical content was changed. Existing working-tree modifications,
including changes to canonical pages and ledgers, were treated as pre-existing
and were not reviewed or incorporated by this gate.

## Candidate integrity correction

The August 30 inbox names a nonexistent technique ID:
`multimodal.query-routing`. The current card is
`multimodal.routing.query-and-corpus` at
`techniques/multimodal/query-routing.json`. Correct the inbox reference before
any promotion review. All other named affected claims and technique IDs resolve.

## Proposed changes

### 1. New verifier, gateway, URL-fetch and language-sandbox advisories

**Provenance, independence and freshness.** GitHub Advisory Database APIs confirm
the five records were published on 2026-08-28 and retain these first-patched
versions: AIIR 1.7.0; 9router 0.5.2 for both authorization bypasses; Bifrost core
1.5.17; RestrictedPython 8.3. The advisory, repository fix, release note and
registry artifact are one upstream provenance chain per defect. No independent
replay was found.

**Contradictions and scope.** The incidents reinforce the current external-
enforcement, strict-contract, sandbox and deterministic-oracle claims. They are
counterexamples to treating a success flag, client `Host` header, pre-rewrite
path check, incomplete IP deny-list or language rewrite as the enforcement
boundary. RestrictedPython hook shadowing is a policy bypass inside the embedding
application, not by itself a universal host escape. Bifrost metadata access
depends on deployment routing; 9router impact requires network reachability and
operator credentials; AIIR scope is limited to the named verification paths.

**Proposal.** After isolated vulnerable/fixed replay, register the five
advisories and affected projects where the registry policy warrants it, add one
reviewed security source audit, and attach release-pinned failure modes to the
narrow high-risk cards. Do not raise claim evidence levels or treat a patched
artifact as proof that downstream compositions are safe.

**Affected evaluation slices.** Fail-open signing and release gates; falsified
success receipts; spoofed host/origin behind direct access and reverse proxies;
authorization before and after path rewriting; CGNAT, 6to4, NAT64, site-local,
redirect and DNS-resolution destinations; positional-only shadowing of every
protected hook; first-patched negative controls; authoritative external effects.

### 2. Google ADK, Temporal and Microsoft fixed releases

**Provenance, independence and freshness.** Official GitHub release APIs confirm
Google ADK Python 2.8.0, Temporal Python SDK 1.32.0 and Microsoft Agent Framework
Python 1.16.0. Their release notes name the candidate fixes. This closes the
older claim that no general fixed ADK or Temporal release existed and confirms a
fix for Microsoft checkpoint aliasing. Maintainer release notes, commits, pull
requests and regression tests are one upstream provenance chain; no independent
deployed-adapter replay was performed.

**Contradictions and scope.** `reports/security-watch-latest.json` is historically
correct at its 2026-08-21 timestamp but its negative release-availability
statement is now stale. Microsoft 1.16.0 does not resolve issue 7647's lineage or
issue 7618's restricted-deserialization path. Temporal worker-environment
references are experimental and must not be generalized to every secret-bearing
history path. ADK fixes do not make remote A2A peers, SQL dry runs or model-output
fencing authorization boundaries.

**Proposal.** On approval, add a dated source-audit addendum and update only the
release-specific evidence/freshness fields of the three runtime cards. Preserve
their situational lifecycle and E2 evidence. Regenerate the security-watch
projection rather than rewriting its historical report in place. Narrow the
Microsoft card's aliasing failure mode to affected releases while retaining the
two unresolved checkpoint failure modes.

**Affected evaluation slices.** ADK credential-request forwarding, registry
endpoint allowlists, HTTP downgrade, SQL identifiers/subqueries and output
instruction fencing; Temporal workflow-history secret scanning, allowlisted
environment resolution, sandbox host paths/session IDs and replay-safe telemetry;
Microsoft nested mutation, storage-read isolation, lineage reachability,
pending-request round trip and crash-around-effect counters; vulnerable and
first-fixed versions for every case.

### 3. AnyDoc 0.2.4 typed OCR routing

**Provenance, independence and freshness.** The official v0.2.4 release exists
and documents typed `needsOcr` errors, page numbers and page count across Rust,
Node, WebAssembly, Python and CLI surfaces. Hosted OCR is an explicit opt-in after
that result. This is upstream mechanism evidence, not independent evidence of
coverage, OCR quality or downstream retrieval quality.

**Contradictions and scope.** The current AnyDoc card says image-only PDFs
"return unsupported" and the parser source audit says they are an explicit
unsupported case. That is now stale for error semantics: local conversion still
does not OCR them, but v0.2.4 identifies affected pages instead of silently
dropping them or returning only a generic failure.

**Proposal.** On approval, update the AnyDoc mechanism/failure-mode wording and
freshness link to state that scanned pages produce a typed routing signal. Add no
comparative accuracy claim and do not make hosted Firecrawl Parse a default.

**Affected evaluation slices.** Mixed text/scanned PDFs; fully scanned PDFs;
exact page-number and page-count reporting across bindings; no silent page loss;
typed-error compatibility; explicit hosted opt-in; egress, privacy and API-error
handling; downstream route to the existing OCR/VLM controls.

### 4. Kubernetes Agent Sandbox 1.0.0 adoption boundary

**Provenance, independence and freshness.** Official v1.0.0 release notes confirm
removal of `v1alpha1`, the required 0.5.x storage migration for older clusters,
browser path routing, `sandboxd` support and changed retry behavior. These are
maintainer claims and regression changes, not an independent isolation or
migration audit.

**Contradictions and scope.** This is a material adoption/migration change but no
evidence that the sandbox resists escape. Browser cookies and Origin validation
do not replace network authorization. A `0.0.0.0` runtime bind is safe only when
the surrounding network boundary is explicit. Suppressing automatic retry for a
failed non-idempotent request reduces one duplicate path but does not prove
exactly-once effects.

**Proposal.** On approval, add a release-specific adoption note to the sandbox
source audit and card evidence link; keep the technique situational and E2.

**Affected evaluation slices.** Upgrade from pre-0.5.0 through 0.5.x; stored-
version inventory and rollback; partial migration; browser session bootstrap,
cookie theft/fixation, Origin and cross-site requests; direct and proxied
`sandboxd` reachability; failed/ambiguous `POST /execute`, client retry, crash
recovery and duplicate-effect counters.

### 5. AutoSaddler bounded harness optimization

**Provenance, independence and freshness.** arXiv `2608.23041v1` and the MIT
repository are one Microsoft-authored project. The repository contains code,
tests, strict configs, split manifests, a deterministic local template and a
seven-scenario GAIA2 smoke path. The README reports the paper's GAIA2,
SWE-Bench Pro and Terminal-Bench gains, but the current V2 repository exposes
only synthetic and Meta-ARE/GAIA2 integrations and explicitly says
Terminal-Bench integration is forthcoming. Full paper results therefore are not
turn-key independently reproducible from the current V2 path.

**Contradictions and scope.** The mechanism supports the existing bounded-loop,
protected-holdout, hermetic-manifest and paired-promotion requirements. It is not
evidence of domain-general RSI or of generation-to-generation optimizer
improvement under equal search budget. Reported gains remain author-reported and
benchmark/harness specific.

**Proposal.** Admit only as an E2 source/candidate after an artifact-safety
review. Do not add it as a recommended technique or change the RSI boundary.
Require a local equal-budget replay before using it to justify a harness change.

**Affected evaluation slices.** Immutable train/dev/test manifests; semantic
deduplication; optimizer/task-model/judge separation; allowed prompt/tool/
middleware/loop mutation surfaces; patch provenance; validation regressions;
total model calls, tokens, wall time and dollar budget; repeated seeds; clean
baseline; held-out project cases; rollback to the exact prior harness.

### 6. VisDocAgentBench multimodal routing candidate

**Provenance, independence and freshness.** arXiv `2608.17889v1` is one
author-reported study. The checked arXiv record links no public code, corpus,
query manifest, predictions or run artifact. The reported 120 unique-target
queries are too small to support a default and the paper's closed 100-document
corpus bounds transfer.

**Contradictions and scope.** The direct versus two-bridge gap and visual versus
OCR route support the existing routed-multimodal architecture and the rule to
scale simple retrieval before adding an agentic branch. They do not justify
agentic search for direct lookup or replace text, ACL, provenance and exact
quotation lanes.

**Proposal.** Keep as an E2 source candidate only. Correct the broken affected
technique ID. Do not change the visual late-interaction card until public
artifacts and an external replay exist.

**Affected evaluation slices.** Direct, one-bridge and two-bridge queries;
complete support-set recall; reviewed hard negatives; text-only, OCR, visual,
fused and agentic routes with equal budgets; page/region citations; task transfer;
query count uncertainty; index bytes, p95 latency and cost.

### 7. DreamBench-SWE memory-hygiene audit

**Provenance, independence and freshness.** arXiv `2608.20664v1` and the
Apache-2.0 v2.1.0 release are one author-controlled provenance. GitHub confirms
checksummed release assets, a manifest, public verifier and selected regression
tests. The public artifact explicitly excludes hidden oracles, raw hosted-model
logs and private analyzer inputs. The inbox phrase "executable hidden oracles"
therefore overstates public replayability and must be corrected. The null result,
conformance rejections and unavailable contrasts are important negative evidence.

**Contradictions and scope.** The findings reinforce an immutable raw event-log
baseline, source/derived separation and multi-session executable evaluation.
They neither prove equality in the original null fold nor superiority among
memory-bearing mechanisms, and one pinned literal-storage configuration cannot
establish general Mem0 fit.

**Proposal.** Admit a reviewed source audit only after the public verifier and
checksums are run in isolation. Retain the existing memory architecture and
baseline; do not add a product default or inferred result for rejected contrasts.

**Affected evaluation slices.** No-memory, verbatim event, typed-plus-raw and
pinned external-memory controls; inferable versus non-inferable evidence;
cross-session provenance; conformance before scoring; clustered paired inference;
hidden-oracle availability; deletion and tenant isolation; literal-store versus
semantic-retrieval mechanisms.

### 8. CatchBench evidence-state auditability

**Provenance, independence and freshness.** arXiv `2608.22808v1` and the MIT
repository are one single-author project. The repository contains packaged data,
fixed predictions, offline boards and tests; its README explicitly separates
borrowed human/outcome labels from constructed PRE and injected labels. No
independent replay was found.

**Contradictions and scope.** The unresolved contrasts, configuration-source
shortcut and inability to flag tau-bench failures early support current judge
admission, abstention and evidence-state requirements. Constructed labels and
source-specific shortcuts limit external validity. The benchmark does not
establish a universal failure detector or authorize replacing deterministic
state oracles.

**Proposal.** After clean offline-board replay, admit as an optional E3 evaluation
source with explicit label-provenance limits. Do not change judge priority or
promotion thresholds.

**Affected evaluation slices.** PRE/LIVE/POST information masks; borrowed versus
constructed labels; capability-order and flag-all/none shortcuts; source-held-out
validation; abstention/unresolved comparisons; early-warning lead time at fixed
false-positive budget; outcome, localization and cause tasks reported separately.

### 9. HarnessRisk, MaliciousSkillBench and SkillSpector 2.11.0

**Provenance, independence and freshness.** The two arXiv papers and their public
repositories/datasets are separate projects but each result remains author-
reported. GitHub confirms code/data surfaces for both. MaliciousSkillBench
documents random, structural-disjoint and source-disjoint protocols and warns
that its source-disjoint result is source-conditioned shift, not universal OOD
generalization. SkillSpector 2.11.0 exists and its maintainer reports expanded
npm lockfile and bundled-hook coverage; the release and its regressions are one
upstream provenance and provide no independent benchmark validation.

**Contradictions and scope.** HarnessRisk reinforces configuration as part of the
deployed security boundary and shows risk recognition is not effect prevention.
MaliciousSkillBench reinforces source-disjoint plus benign evaluation and shows
that random-split quality does not transfer automatically. SkillSpector's new
capabilities do not close that generalization gap, cover Yarn/pnpm, or turn a
scanner verdict into authorization.

**Proposal.** After malware-artifact safety review, admit the benchmarks as
optional development suites and add the SkillSpector release as a bounded
capability note. Keep the supply-chain scanner situational and E2. Do not use any
single benchmark or scanner as a release oracle.

**Affected evaluation slices.** Model-plus-harness configurations; configuration,
extension, runtime, persistence, action and recovery phases; benign utility;
authoritative state effects; random, structural-disjoint, source-disjoint and
new-source holdouts; benign false positives; staged behavior; npm lockfile
versions and transitive copies; Yarn/pnpm negative coverage; bundled hooks,
permissions and sensitive transfer; scanner isolation and adaptive evasions.

## Rejected or watch-only evidence

- **August 16 residual candidates:** ReFind, memory cost, ToolHazard and the
  graph-memory poisoning hypothesis remain at their 2026-08-24 gates. The older
  advisories retain their upstream ranges. No new independent replay clears a
  promotion gate. Microsoft snapshot aliasing is now fixed upstream in Python
  1.16.0, but the other two checkpoint reports remain unresolved.
- **Runtime release activity:** Pydantic AI durable-operation APIs,
  OpenSandbox lifecycle/VM-state changes, Deep Agents grader hooks and LangGraph
  trace routing are capability or defect signals, not comparative durability,
  isolation or judge-calibration evidence.
- **ECHO and InjecMEM:** ECHO's negative matched sample and contamination audit
  reinforce local selection and contamination controls without adding a default.
  InjecMEM lacks sufficient public denominators/artifacts for a quantitative
  durable claim.
- **Prime Agent, OptiMAS and CONTRAMEM:** retain as bounded adaptation discovery.
  Code availability or multi-benchmark gains do not demonstrate the required
  equal-budget generation-N-to-N+1 optimizer test, safe objective evolution or
  autonomous promotion.
- **Other parser/evaluation papers and forum threads:** keep at E0/E1 discovery
  where no linked artifact, controlled reproduction or decision-grade comparison
  exists. Correlated technical-forum discussion is not independent evidence.

## Tests required before any canonical change

1. Replay every new advisory on the exact vulnerable and first-patched artifact
   in credential-free isolation, score authoritative effects, and retain patched
   negative controls.
2. Replay ADK 2.8.0, Temporal 1.32.0 and Microsoft 1.16.0 on the actual adapter
   compositions; retain lineage, deserialization and crash-around-effect tests
   that the Microsoft alias fix does not cover.
3. Test AnyDoc 0.2.4 on mixed and fully scanned PDFs across bindings, including
   silent-page-loss sentinels and explicit OCR-routing/privacy behavior.
4. Rehearse Kubernetes Agent Sandbox migration and rollback on pre-0.5, 0.5.x
   and 1.0.0 states; attack browser routing and ambiguous non-idempotent execution.
5. Run AutoSaddler with frozen manifests and equal total optimization budgets on
   a protected local harness slice; verify forbidden mutation boundaries and
   byte-exact rollback.
6. Wait for VisDocAgentBench public data/predictions, then replay all routing
   baselines and relational-depth slices under equal context and search budgets.
7. Verify DreamBench-SWE v2.1.0 checksums and public tests, explicitly record
   which hidden-oracle and raw-log claims cannot be replayed, and reproduce
   preregistered contrasts without substituting rejected comparisons.
8. Recompute CatchBench offline boards and validate on a new source before using
   it for detector selection.
9. Inspect HarnessRisk and MaliciousSkillBench artifacts as untrusted content,
   run them in a disposable environment, add private benign/malicious controls,
   and evaluate scanners on source-disjoint and adaptive holdouts.
10. Before promotion, validate IDs/schemas, run claim-coverage and contradiction
    checks, compile and lint, execute protected retrieval/runtime/security slices,
    obtain human approval, and release consumers separately.

## Rollback impact

This gate adds one report and refreshes only the deterministic due-review output
written by the requested command. It changes no canonical claim, source, card,
synthesis, evaluation dataset, threshold, index or release consumer. Rollback of
this proposal is deletion of this report; the due-review JSON is reproducible by
rerunning the command for the same date.

Any later approved source or card update must be independently revertible. Parser
or retrieval changes require retention of the previous parse/index identity.
Runtime and sandbox migrations require a rehearsed state rollback. Harness or
evaluator changes require the previous manifest, fixed evaluator epoch, paired
results and consumer release lock.

## Unresolved questions

- Who will independently replay the new advisories and the three fixed runtime
  releases against the deployed wrappers?
- Should AIIR, 9router, Bifrost and RestrictedPython be registered as persistent
  freshness projects, or should only their advisories live in the source audit?
- Which Microsoft releases resolve checkpoint lineage and restricted-
  deserialization resume, and can either defect cause an external-effect error?
- Can AnyDoc's typed page list remain complete across malformed, encrypted and
  partially scanned documents and every supported binding?
- What supported rollback path exists after an Agent Sandbox 1.0.0 CRD storage
  migration?
- Will AutoSaddler publish full paper-run manifests and turn-key SWE-Bench Pro
  and Terminal-Bench integrations for independent replay?
- Will VisDocAgentBench publish its corpus, query construction, hard negatives,
  predictions and run configuration?
- Can DreamBench-SWE's headline mechanism comparisons be independently rerun
  without the excluded hidden oracles and raw hosted-model logs?
- Does CatchBench transfer to new trace/configuration sources without its known
  construction shortcuts?
- Who owns artifact safety review and protected source-disjoint thresholds for
  HarnessRisk, MaliciousSkillBench and future scanner releases?
