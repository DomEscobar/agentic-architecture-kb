---
id: pattern-document-centric-hybrid-rag
type: pattern
title: Document-centric Hybrid RAG
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T17:05:00+02:00
updated_at: 2026-08-08T17:05:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-bauhelfer-ki
relations:
  - predicate: derived_from
    target: source-domescobar-bauhelfer-ki
  - predicate: applies_to
    target: case-bauhelfer-ki-rag
---

# Document-centric Hybrid RAG

## Winning Conditions

Dieses Pattern passt, wenn Dokumentstruktur und exakte Werte gleichermaßen
wichtig sind: Angebote, Verträge, technische Spezifikationen,
Leistungsverzeichnisse, Rechnungen oder regulatorische Unterlagen.

## Architektur

### Ingestion

1. Original unveränderlich und außerhalb des Code-Repositories speichern.
2. Tenant, Projekt, Dokumenttyp und Retention vor Parsing festlegen.
3. Layout-, Tabellen-, OCR- und Seiteninformationen extrahieren.
4. Parseroutput und Parser-/Konfigurationsversion speichern.
5. Nach Überschrift, Tabelle, Position oder Seite strukturieren; fixe
   Tokenfenster nur als Fallback.
6. Chunk mit stabiler ID, Dokumentversion, Seitenanker, Typ, Confidence und
   kompaktem Kontextkopf versehen.
7. Lexikalischen und semantischen Index reproduzierbar erzeugen.

### Retrieval

```text
intent/scope
 -> deterministic ACL + metadata filter
 -> dense retrieval || lexical retrieval
 -> RRF
 -> optional reranker
 -> diversity/coverage selection
 -> evidence pack with stable anchors
```

ACL und Projektfilter müssen vor ANN/Ranking gelten. RRF ist ein guter Default,
weil es Ränge statt unkalibrierter Scores fusioniert. Top-k-Werte sind keine
Best Practices, sondern per Dataset zu bestimmende Parameter.

### Generation

- Evidence Pack und Output-Schema explizit trennen.
- Jede fachliche Aussage und jedes kritische Feld auf Source-ID und Seitenanker
  beziehen.
- Annahme, unbekannt und widersprüchlich als eigene Zustände modellieren.
- Rechenbare Werte deterministisch berechnen und validieren.
- Externe oder irreversible Ausgabe erst nach menschlicher Freigabe.

## Nicht verwenden

- Für kleine, vollständig strukturierte Datensätze: direkte SQL/API-Abfrage ist
  einfacher und präziser.
- Für exakte Tabellenaggregation: Parser plus strukturierte Datenbank gewinnt
  häufig gegen Text-RAG.
- Für einmalige, kurze Dokumente: Long-context kann als Baseline günstiger sein.

## Failure Detection

- Parse-Goldens pro Dokumenttyp;
- Retrieval-Ablationen und per-slice Metriken;
- Cross-scope Canaries;
- Citation-/Anchor-Validator;
- Unsupported-Claim- und Missing-field-Checks;
- Indexmanifest- und Löschungsprüfung;
- Latenz, Kosten und Reranker-Fallback im Trace.
