# MVP und Roadmap

## Phase 0 — Repository und Verträge

- [x] separates Git-Repository planen
- [x] Architektur und erste ADR dokumentieren
- [x] maschinenlesbares Seitenschema definieren
- [ ] Datenschutzklassen und Korrekturrechte mit Dom bestätigen
- [ ] vorhandene Wiki-Inhalte kontrolliert importieren

## Phase 1 — Deterministische Wissensbasis

- [x] Markdown-Parser, Schema-Validator und Link-Linter
- [x] stabile IDs und Source-/Relationsreferenzen
- [x] reproduzierbarer Compile-Schritt für JSON-Projektion und Qualitätsreport
- [x] CI für Schema, Links, Provenienz, Duplikate und Privacy-Markierungen
- [ ] explizites Claim-Ledger mit abschnittsgenauen Source-Referenzen
- Git-basierter Review- und Rollback-Prozess

Exit-Kriterium: Jeder kanonische Claim ist einer Quelle oder explizit einer
Entscheidung/Hypothese zugeordnet; ein frischer Clone lässt sich reproduzierbar
kompilieren.

## Phase 2 — Retrieval

- SQLite FTS5 Baseline
- Embedding-Index mit vollständigem Manifest
- RRF-Fusion und optionale Metadatenfilter
- Retrieval-Trace und zitierfähige Textabschnitte

Exit-Kriterium: Baseline-Evals schlagen Volltext allein messbar, ohne Privacy-
oder Löschregression.

## Phase 3 — Memory Promotion

- Chat-/Session-Extraktion nur in die Inbox
- Deduplikation, Konflikterkennung und Review-Queue
- Hintergrund-Konsolidierung
- Lösch- und Korrekturpropagation mit Negativtest

Exit-Kriterium: kein ungeprüfter Inhalt gelangt in kanonische Synthesen.

## Eval Foundation

- [x] Agent-Evaluation-Taxonomie und Evidence-first Pattern
- [x] bounded Improvement Loop mit Promotion- und Rollback-Grenzen
- [ ] erste project-lokale Eval Packs und kalibrierte Orakel
- [ ] Judge-Validierungsset und wiederholungsbasierte Konfidenz
- [ ] geschützte Development-/Selection-/Holdout-/Redteam-Splits

## Phase 4 — Scale-up nach Messung

Postgres/pgvector, Reranker, Graphprojektion oder Workflow-Runtime werden jeweils
über ein eigenes ADR und eine Eval-basierte Entscheidung eingeführt.
