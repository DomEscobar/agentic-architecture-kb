---
id: source-runtime-techniques-2026-08
type: source
title: Agent Runtime Mechanisms Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-12T22:05:00+02:00
updated_at: 2026-08-12T22:05:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

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

