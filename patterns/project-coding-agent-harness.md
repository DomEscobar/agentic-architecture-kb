---
id: pattern-project-coding-agent-harness
type: pattern
title: Project-Specific Coding Agent Harness
status: reviewed
privacy: public
confidence: 0.87
created_at: 2026-08-16T13:05:00+02:00
updated_at: 2026-08-16T14:40:00+02:00
review_at: 2026-09-16
source_ids:
  - source-coding-agent-harness-and-skills-evidence-2026-08
  - source-agentic-security-verification-2026-08
  - source-agent-evaluation-research-2026
relations:
  - predicate: derived_from
    target: source-coding-agent-harness-and-skills-evidence-2026-08
  - predicate: depends_on
    target: pattern-runtime-decision-guide
  - predicate: depends_on
    target: pattern-agentic-runtime-security-boundary
---

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
