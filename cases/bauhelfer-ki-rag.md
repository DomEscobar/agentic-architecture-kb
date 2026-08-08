---
id: case-bauhelfer-ki-rag
type: case
title: Bauhelfer-KI RAG
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T17:05:00+02:00
updated_at: 2026-08-08T17:05:00+02:00
review_at: 2026-10-08
source_ids:
  - source-domescobar-bauhelfer-ki
relations:
  - predicate: derived_from
    target: source-domescobar-bauhelfer-ki
  - predicate: evaluated_by
    target: pattern-document-centric-hybrid-rag
---

# Case: Bauhelfer-KI RAG

## Kontext

Ein deutschsprachiger Angebotsassistent verarbeitet heterogene Bau- und
Handwerksunterlagen wie Leistungsverzeichnisse, Preislisten, Office-Dateien,
Scans und Fotos. Das Ergebnis ist kein freier Chattext, sondern ein prüfbarer,
editierbarer Angebotsentwurf mit Positionen, Mengen, Preisen, Annahmen und
Quellen.

## Relevante Constraints

- exakte IDs, Positionsnummern, Einheiten, Beträge und Seiten sind wichtiger als
  bloße semantische Ähnlichkeit;
- Tabellen, Layout und Reading Order tragen Bedeutung;
- Retrieval muss Organisation und Projekt strikt isolieren;
- falsche Zuordnung zwischen Kunden oder Projekten ist ein schwerer Fehler;
- unbekannte Werte müssen offen bleiben statt plausibel ergänzt zu werden;
- ein Nutzer genehmigt das Ergebnis vor PDF beziehungsweise externer Wirkung.

## Implementiertes Muster

```text
upload
 -> project/tenant scope
 -> Docling parsing
 -> Markdown + JSON + layout/table metadata
 -> structure-aware chunks + contextual header
 -> embeddings + German FTS
 -> dense top-40 + lexical top-40
 -> RRF(k=60)
 -> poison/overview filtering
 -> optional LLM reranking of top-30
 -> top-8 context
 -> typed evidence bundle
 -> structured offer/document snapshot
 -> blocking review issues
 -> human approval
```

Postgres hält App-Daten, Metadaten, Full-Text-Index und pgvector gemeinsam. Die
Embedding-Spalte hat 1536 Dimensionen; OpenAI und Gemini sind Provideroptionen,
wobei gekürzte Gemini-Vektoren normalisiert werden. Der Ingestion-Worker
verarbeitet Embeddings in Batches von 64.

## Was an diesem Pattern stark ist

- Tenant- und Projektfilter liegen innerhalb der Dense- und FTS-SQL-Abfragen,
  also vor der Ergebnisauswahl.
- Strukturierte Chunks behalten Seite, Heading Path und Typ.
- Contextual Headers verbessern die Selbstbeschreibung isolierter Chunks.
- RRF verbindet semantische und exakte Treffer ohne inkompatible Rohscores zu
  addieren.
- Evidence Bundles werden gegen tatsächlich zum Projekt gehörende Datei-IDs
  validiert.
- Dokument-Snapshots frieren Quellrevision und Evidence ein; stale Revisionen
  und Cross-project Evidence werden abgelehnt.
- Fehlende oder externe Evidenz erzeugt Review-Bedarf statt erfundener Sicherheit.

## Schwächen und offene Risiken

### Evaluation

Das eingecheckte Retrieval-Testset enthält nur eine Frage. Der Harness wertet
einen Source-Hit aus und gibt denselben Wert als Context Precision und Context
Recall aus. Das misst weder Rankingqualität noch echte Precision/Recall. Es
fehlen insbesondere harte Negativfälle, Tabellenzellen, OCR-Fehler,
Cross-project Leakage, widersprüchliche Dokumentversionen und temporale Updates.

### Reranking

Der optionale LLM-Reranker sieht nur die ersten 500 Zeichen jedes Chunks. Für
Tabellen oder spätere Evidenz kann das falsche Rankings erzeugen. Er benötigt
eine Offline-Baseline gegen RRF allein, Latenz-/Kostenmessung und ein
fehlertolerantes Fallback.

### Heuristische Poison-Filter

Bekannte Parser-Fallbacktexte und Mehrprojektübersichten werden über deutsche
Substring-Regeln entfernt. Das ist als Incident-Fix verständlich, aber fragil.
Die robustere Lösung sind typisierte Ingestion-Status-, Herkunfts- und
Scope-Metadaten, die schon vor Retrieval deterministisch gefiltert werden.

### Index- und Provider-Migration

Die Dimension ist an das Datenbankschema gekoppelt. Ein Wechsel von Modell,
Dimension, Normalisierung oder Chunker benötigt ein Index-Manifest, parallelen
Rebuild, Recall-Vergleich und atomaren Cutover.

### Repository-Hygiene

Upload- und Parsed-Verzeichnisse dürfen nicht in öffentlichen Source-Control-
Verläufen liegen. Löschen im aktuellen Commit entfernt sie nicht aus der
Git-Historie. Erforderlich sind Secret/PII-Prüfung, History-Bereinigung nach
Review, Storage außerhalb des Repos und CI-Guards gegen erneutes Einchecken.

## Empfohlene nächste Evals

1. 10–20 repräsentative Projektmappen, getrennt nach PDF, Scan, XLSX und Foto.
2. Mindestens 100 Retrieval-Fragen mit vollständigen Relevance Labels, nicht nur
   einer erwarteten Quelle.
3. Metriken pro Stufe: Parse Field Accuracy, Recall@k, nDCG@k, MRR, Context
   Precision, Citation Correctness, Unsupported Claim Rate und Position Field
   Accuracy.
4. Ablationen: FTS, Dense, Hybrid/RRF und Hybrid+Reranker.
5. Negativsuite für Tenant-/Projekt-Leakage, gelöschte Dateien, poisoned chunks,
   veraltete Versionen und fehlende Preise.
6. Replay mit Kosten und p50/p95-Latenz; Canary und Feature Flag für Reranking.

## Wiederverwendbares Ergebnis

Für dokumentzentrierte Fachanwendungen gewinnt eine pipelineweite Architektur:
Parsing-Qualität, Scope-Filter, strukturierte Chunks, Hybrid Retrieval,
Evidence-Verträge und deterministische Postconditions sind gemeinsam
entscheidend. Die Wahl der Vector-Datenbank allein erklärt die Qualität nicht.
