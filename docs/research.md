# Deep Research: Architektur und Tools

Stand: 2026-08-08. Bevorzugt wurden offizielle Dokumentationen, Repositories und
Forschungsarbeiten. Vendor-Aussagen gelten als Implementierungsbelege, nicht als
unabhängiger Qualitätsnachweis.

## Befunde

### Memory braucht getrennte Scopes und Schreibzeitpunkte

LangGraphs Dokumentation trennt Thread-State von sitzungsübergreifendem Memory
und unterscheidet semantisches, episodisches und prozedurales Gedächtnis. Sie
beschreibt außerdem Hot-Path- und asynchrones Schreiben mit unterschiedlichen
Latenz- und Freshness-Eigenschaften. Das stützt getrennte Stores und einen
asynchronen, prüfbaren Promotion-Pfad.

Quelle: https://docs.langchain.com/oss/python/concepts/memory

### Der Index darf nicht die Wahrheitsschicht sein

SQLite FTS5 bietet lokale Volltextsuche und BM25 ohne zusätzlichen Dienst. Für
den MVP genügt das zusammen mit einem reproduzierbaren Embedding-Index.

Quelle: https://www.sqlite.org/fts5.html

pgvector unterstützt exakte und approximative Vektorsuche sowie Hybrid Search
mit PostgreSQL Full Text Search. Die Dokumentation weist zugleich darauf hin,
dass ANN Recall gegen Geschwindigkeit tauscht und gefilterte ANN-Abfragen zu
weniger Treffern führen können. Postgres ist deshalb eine Scale-up-Option, kein
notwendiger MVP-Baustein.

Quelle: https://github.com/pgvector/pgvector

### Evaluation muss mehr als Fact Recall messen

MemoryAgentBench benennt accurate retrieval, test-time learning, long-range
understanding und selective forgetting als getrennte Fähigkeiten. Der allgemeine
Agent-Eval-Survey fordert zusätzlich realistischere, fortlaufend aktualisierte
Tests für Robustheit, Sicherheit und Kosteneffizienz.

Quellen:

- https://arxiv.org/abs/2507.05257
- https://arxiv.org/abs/2503.16416

### Checkpoints sind Runtime-State, nicht Wiki-Wissen

LangGraphs Persistence-Modell speichert Zustand schrittweise und ermöglicht
Resume, Human-in-the-loop und Time-travel Debugging. Das ist sinnvoll für die
Runtime, darf aber nicht mit geprüften Wissensclaims vermischt werden.

Quelle: https://docs.langchain.com/oss/python/langgraph/persistence

## Werkzeugentscheidung

### MVP: empfohlen

- **Git + Markdown:** kanonische, diffbare Quelle und Rollback.
- **Obsidian:** optionale menschliche Oberfläche für Links und Properties; kein
  Laufzeit-Dependency.
- **JSON Schema + eigener Linter:** deterministische Struktur- und Policy-Checks.
- **SQLite FTS5:** lokaler lexikalischer Index.
- **Embeddings + einfacher lokaler Vector Store:** semantischer Recall; Modell-
  und Chunker-Version zwingend im Manifest.
- **Reciprocal Rank Fusion:** transparente Fusion von Volltext und Vektoren.
- **pytest/Fixtures:** reproduzierbare Retrieval-, Update-, Privacy- und
  Forgetting-Evals.
- **OpenTelemetry:** Traces und Metriken mit redigierten Inhalten; die GenAI-
  Konventionen entwickeln sich weiter und müssen versioniert werden.

Quelle: https://opentelemetry.io/docs/specs/semconv/

### Später, nur bei gemessenem Bedarf

- **Postgres + pgvector:** mehrere Writer, ACL-Abfragen, hohe Dokumentzahl oder
  zentraler Dienst.
- **Cross-Encoder-Reranker:** wenn Offline-Evals einen relevanten Precision-Gewinn
  innerhalb des Latenzbudgets zeigen.
- **Property Graph:** erst wenn Multi-Hop-Fragen in der Eval-Suite scheitern;
  Beziehungen zunächst aus Markdown-Metadaten projizieren.
- **LangGraph oder vergleichbare Runtime:** wenn langlaufende Workflows,
  Checkpoints und Recovery tatsächlich gebraucht werden. Das Wiki selbst bleibt
  runtime-unabhängig.

### Nicht empfohlen im MVP

- autonome Promotion von Chat-Inhalten;
- ein proprietärer Vector Store als einzige Kopie;
- automatische Skill-/Prompt-Umschreibung aus einzelnen Erfolgen;
- Knowledge Graph, Vector DB und Agent-Framework gleichzeitig einzuführen.
