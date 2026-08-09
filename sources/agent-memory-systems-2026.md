---
id: source-agent-memory-systems-2026
type: source
title: Agent Memory Systems Audit 2026
status: reviewed
privacy: public
confidence: 0.86
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

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

