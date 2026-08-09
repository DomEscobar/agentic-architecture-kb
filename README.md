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
- [Contextual Retrieval](patterns/contextual-retrieval.md)
- [Graph-based Retrieval](patterns/graph-based-retrieval.md)
- [Agentic and Corrective Retrieval](patterns/agentic-corrective-retrieval.md)
- [Visual Late-interaction Retrieval](patterns/visual-late-interaction-retrieval.md)
- [Agent Evaluation Techniques](syntheses/agent-evaluation-techniques.md)
- [Evidence-first Agent Evaluation](patterns/evidence-first-agent-evaluation.md)
- [Eval-guided Bounded Improvement Loop](patterns/eval-guided-improvement-loop.md)

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

Die deterministische MVP-Toolchain validiert Schema, IDs, Seitentypen, lokale
Links, Provenienz und Relationsziele. Sie kompiliert alle kanonischen Seiten in
eine vollständig rekonstruierbare JSON-Projektion. Autonomes Schreiben in den
kanonischen Bereich ist nicht aktiviert.

## Lokale Qualitätsprüfung

```bash
python3 -m pip install -r requirements.txt
make check
```

`make lint` verändert keine Dateien. `make compile` schreibt ausschließlich die
ignorierten Projektionen `build/wiki.json` und `reports/quality.json`. GitHub
Actions führt denselben Check bei Pushes und Pull Requests aus.
