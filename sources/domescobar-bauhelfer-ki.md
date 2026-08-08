---
id: source-domescobar-bauhelfer-ki
type: source
title: DomEscobar bauhelfer-ki
status: reviewed
privacy: public
confidence: 0.95
created_at: 2026-08-08T17:05:00+02:00
updated_at: 2026-08-08T17:05:00+02:00
review_at: 2026-11-08
source_ids: []
relations: []
---

# DomEscobar/bauhelfer-ki

- Repository: https://github.com/DomEscobar/bauhelfer-ki
- untersuchter Commit: `6671de4277b57e6aa06c1cf06abdad43fd72ac20`
- Commit-Permalink: https://github.com/DomEscobar/bauhelfer-ki/tree/6671de4277b57e6aa06c1cf06abdad43fd72ac20
- abgerufen: 2026-08-08

## Untersuchte Artefakte

- `RAG.md`, `RAG_METHODIK_2026.md`, `docs/RAG-DeepResearch-2026.md`
- `apps/api/src/services/ingestion.ts`
- `apps/api/src/services/retrieval.ts`
- `apps/api/src/providers/embeddings.ts`
- `apps/api/src/providers/reranker.ts`
- `apps/api/src/services/agent/contextAssembly.ts`
- `apps/api/src/services/agent/citations.ts`
- `apps/api/src/services/documentEvidence.ts` und zugehörige Tests
- `apps/api/migrations/001_init.sql`
- Retrieval- und Angebots-Eval-Harness unter `eval/`

## Datenschutzgrenze

Das Repository enthält hochgeladene und geparste Projektartefakte unter
`apps/api/data/`. Diese wurden weder als Wissensquelle ausgewertet noch in das
Wiki übernommen. Ein öffentliches Code-Repository sollte keine realen Uploads,
abgeleiteten Texte, Kundeninformationen oder lokale Storage-Pfade enthalten.

## Verwendungsregel

Der Code belegt die konkrete Implementierung des Cases. Zahlen, Rankings und
Marktvergleiche aus den Research-Dokumenten sind Repo-Claims und werden erst
nach Prüfung ihrer Primärquellen in allgemeine Empfehlungen promoted.
