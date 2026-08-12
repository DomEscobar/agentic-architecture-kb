---
id: decision-knowledge-promotion-dag
type: decision
title: ADR-0002 One-way Knowledge Promotion DAG
status: reviewed
privacy: internal
confidence: 0.96
created_at: 2026-08-12T22:30:00+02:00
updated_at: 2026-08-12T22:30:00+02:00
review_at: 2026-11-12
source_ids:
  - source-public-ai-architect-validation-2026-08
relations: []
---

# ADR-0002: One-way Knowledge Promotion DAG

## Decision

Primary evidence and reviewed project observations enter `llm-wiki`, which is the
canonical technical knowledge source. Two consumers are produced only downstream:

`evidence -> llm-wiki -> Memory Wiki projection`

`evidence -> llm-wiki -> approved public snapshot`

`wiki-sources` is frozen as legacy migration input. Chat history, `MEMORY.md` and
daily notes retain decisions and context; they do not become canonical technical
evidence without source-backed ingestion and review.

## Promotion controls

Every consumer release records the canonical build digest, compiler identity,
approved page identities, artifact digest, prior release and approval state.
Drift detection reports a stale consumer but never publishes automatically.
Memory Wiki updates use the supported ingest/compile/lint workflow and preserve
human blocks. Public release requires an explicit allowlist, privacy scan,
deterministic rebuild, evaluation evidence, human approval and rollback artifact.

## Failure boundary

No reverse sync may overwrite canonical pages. Deletion and supersession propagate
only during an approved rebuild. A consumer without a matching lock is stale, not
implicitly current.
