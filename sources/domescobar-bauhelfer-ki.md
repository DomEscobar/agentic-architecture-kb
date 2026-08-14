---
id: source-domescobar-bauhelfer-ki
type: source
title: DomEscobar bauhelfer-ki
status: reviewed
privacy: public
confidence: 0.55
created_at: 2026-08-08T17:05:00+02:00
updated_at: 2026-08-14T10:47:00+02:00
review_at: 2026-11-08
auditability: private
source_ids: []
relations: []
---

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
