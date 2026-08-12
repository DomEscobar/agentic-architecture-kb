# MVP und Roadmap

## Phase 0 — Repository und Verträge

- [x] separates Git-Repository planen
- [x] Architektur und erste ADR dokumentieren
- [x] maschinenlesbares Seitenschema definieren
- [ ] Datenschutzklassen und Korrekturrechte mit Dom bestätigen
- [x] vorhandene Optimizer-Inhalte kontrolliert als Quellen und Patterns konsolidieren

## Phase 1 — Deterministische Wissensbasis

- [x] Markdown-Parser, Schema-Validator und Link-Linter
- [x] stabile IDs und Source-/Relationsreferenzen
- [x] reproduzierbarer Compile-Schritt für JSON-Projektion und Qualitätsreport
- [x] CI für Schema, Links, Provenienz, Duplikate und Privacy-Markierungen
- [x] explizites Claim-Ledger mit abschnittsgenauen Source-Referenzen eingeführt
- [x] Claim-Policy und Seitenabdeckung für alle reviewed Patterns, Syntheses, Concepts und Cases auditiert (55 Claims, 49/49 Seiten; Satzvollständigkeit bleibt reviewbar)
- Git-basierter Review- und Rollback-Prozess

Exit-Kriterium: Jeder kanonische Claim ist einer Quelle oder explizit einer
Entscheidung/Hypothese zugeordnet; ein frischer Clone lässt sich reproduzierbar
kompilieren.

## Phase 2 — Retrieval

- [x] SQLite FTS5 Baseline
- [x] stabile zitierfähige Abschnitts-IDs
- [x] Retrieval-Trace mit Filtern, Kandidaten und geladenen Abschnitten
- [x] lokaler Embedding-Index mit gepinnter Modellrevision und vollständigem Manifest
- [x] RRF-Fusion mit Privacy-/Status-/Typ-Prefilter, Stale-Index-Abbruch und Retrieval-Trace
- [x] FTS-vs-Dense-vs-RRF auf 12 gelabelten mehrsprachigen Development-Cases verglichen
- [ ] Relevanzlabels unabhängig menschlich auditieren und auf geschütztem Split bestätigen; erst dann promotionsfähig

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
- [x] erstes project-lokales Development-Eval-Pack
- [ ] menschlich kalibrierte Orakel für das Development-Eval-Pack
- [x] Judge-Validierungsset, Zwei-Labeler-/Adjudikationsschema und Kalibrierungsrunner implementiert
- [ ] echte unabhängige Labels und eingefrorene Judge-Predictions erheben
- [x] Split- und Informationsflussvertrag für Development/Selection/Holdout/Redteam
- [x] ungetrackter Private-Mount, Release-Zugriffsledger, Digest- und Evidence-Validator implementiert
- [ ] echte private Selection-/Holdout-Cases unter fachlicher Verantwortung einbringen
- [x] Consulting Intake, Brownfield Audit und Greenfield Design
- [x] workload-spezifische Eval-Blueprints und Metrikauswahl
- [x] Statistik-, Judge-, Online-, Toolauswahl- und Rollout-Patterns
- [x] Strategy-, Dataset-, Audit- und Go-live-Templates
- [x] Consulting-Coverage-Suite
- [ ] drei feldvalidierte Case Records mit realen Outcomes (aktuell zwei wiederverwendbare Cases, davon ein Public-Runtime-Case mit technischen Outcomes)

## Consumer Projection

- [x] deterministische, privacy-gefilterte Memory-Wiki-Projektion aus `build/wiki.json`
- [x] offizieller OpenClaw-Ingest, kanonische Synthese, Compile und Lint
- [x] Digest-Lock und dokumentierter Rollback; Legacy-Seiten bleiben historisch erhalten
- [ ] semantischen Memory-Core-Index neu aufbauen, sobald der konfigurierte Embedding-Provider wieder verfügbar ist; lokale Wiki-Suche ist funktionsfähig

## Phase 4 — Scale-up nach Messung

Postgres/pgvector, Reranker, Graphprojektion oder Workflow-Runtime werden jeweils
über ein eigenes ADR und eine Eval-basierte Entscheidung eingeführt.
