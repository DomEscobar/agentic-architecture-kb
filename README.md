# Agentic Architect LLM Wiki

Git-versionierte, lokale Wissensbasis für belastbare Architekturentscheidungen zu
RAG, Agenten-Runtimes, Agenten-Memory, Evaluation und begrenzter
Selbstverbesserung.

## Leitidee

Markdown ist die kanonische Quelle. Suchindizes, Graphen, Reports und
LLM-Zusammenfassungen sind reproduzierbare Projektionen und dürfen nie die
Originalquellen ersetzen.

## Dokumentation

- [Systemarchitektur](docs/architecture.md)
- [Recherche und Werkzeugauswahl](docs/research.md)
- [MVP und Roadmap](docs/roadmap.md)
- [ADR-0001: Markdown und Git als Source of Truth](docs/adr/0001-markdown-git-source-of-truth.md)
- [Seitenschema](schemas/page.schema.json)
- [Memory-Evaluation](evals/README.md)
- [Runtime-Techniken: strukturierte Synthese](syntheses/agentic-runtime-techniques.md)
- [Runtime Decision Guide](patterns/runtime-decision-guide.md)
- [Runtime Safety Baseline](patterns/runtime-safety-baseline.md)
- [Document-centric Hybrid RAG](patterns/document-centric-hybrid-rag.md)
- [Case: Bauhelfer-KI RAG](cases/bauhelfer-ki-rag.md)
- [RAG Pipeline Taxonomy](syntheses/rag-pipeline-taxonomy.md)
- [PageIndex / Reasoning Tree Retrieval](patterns/pageindex-reasoning-tree-retrieval.md)

## Vault-Struktur

```text
inbox/       ungeprüfte Eingänge
sources/     Primärquellen und unveränderte Evidenz
concepts/    stabile Begriffe und Mechanismen
patterns/    Muster mit Einsatz- und Ausschlussbedingungen
cases/       konkrete Architekturentscheidungen und Ergebnisse
entities/    Personen, Projekte, Systeme und Organisationen
syntheses/   belegte, aus Quellen abgeleitete Übersichten
reports/     generierte Qualitäts- und Governance-Berichte
```

## Status

Planungs- und Bootstrap-Repository. Es ist noch kein autonomes Schreiben in den
kanonischen Bereich aktiviert.
