---
id: pattern-runtime-build-vs-adopt
type: pattern
title: Agent Runtime Build Versus Adopt Decision
status: reviewed
privacy: public
confidence: 0.86
created_at: 2026-08-13T12:45:00+02:00
updated_at: 2026-08-13T12:45:00+02:00
review_at: 2026-10-13
source_ids:
  - source-agent-runtime-framework-landscape-2026-08
  - source-runtime-techniques-2026-08
relations:
  - predicate: derived_from
    target: source-agent-runtime-framework-landscape-2026-08
  - predicate: depends_on
    target: pattern-runtime-safety-baseline
---

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
