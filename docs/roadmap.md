# MVP und Roadmap

## Phase 0 — Repository und Verträge

- [x] separates Git-Repository planen
- [x] Architektur und erste ADR dokumentieren
- [x] maschinenlesbares Seitenschema definieren
- [ ] Datenschutzklassen und Korrekturrechte mit Dom bestätigen
- [ ] vorhandene Wiki-Inhalte kontrolliert importieren

## Phase 1 — Deterministische Wissensbasis

- Markdown-Parser, Schema-Validator und Link-Linter
- stabile IDs und Claim-/Source-Referenzen
- Compile-Schritt für Indizes und Reports
- CI für Schema, Links, Provenienz, Duplikate und Privacy
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

## Phase 4 — Scale-up nach Messung

Postgres/pgvector, Reranker, Graphprojektion oder Workflow-Runtime werden jeweils
über ein eigenes ADR und eine Eval-basierte Entscheidung eingeführt.
