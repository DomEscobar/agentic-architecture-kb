---
id: source-agent-runtime-framework-landscape-2026-08
type: source
title: Agent Runtime Framework Landscape Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.86
created_at: 2026-08-13T12:45:00+02:00
updated_at: 2026-08-13T12:45:00+02:00
review_at: 2026-10-13
source_ids: []
relations: []
---

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
