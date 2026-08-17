---
id: source-coding-agent-harness-and-skills-evidence-2026-08
type: source
title: Coding Agent Harness and Skills Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.92
created_at: 2026-08-16T13:05:00+02:00
updated_at: 2026-08-16T14:40:00+02:00
review_at: 2026-09-16
source_ids: []
relations: []
---

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
