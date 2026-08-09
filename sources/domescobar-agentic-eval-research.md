---
id: source-domescobar-agentic-eval-research
type: source
title: DomEscobar Agentic Eval Evolution Research
status: reviewed
privacy: public
confidence: 0.82
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

# Agentic Eval Evolution Runtime — Research Audit

- Repository: https://github.com/DomEscobar/agentic-eval-evolution-runtime
- untersuchter Commit: `f890e15790f4a1a60adcd835f3c7993c38efaf09`
- Research-Permalink: https://github.com/DomEscobar/agentic-eval-evolution-runtime/tree/f890e15790f4a1a60adcd835f3c7993c38efaf09/research
- abgerufen: 2026-08-09

## Enthaltene Research-Lanes

- generischer Agentic-Eval- und Evolution-Harness;
- eval-geführte Code-Patch-Loops;
- Qualität und Leakage-Schutz von Eval-Datensätzen.

Jede Lane enthält Plan, Quellenledger, Claims, Evidence-Auszüge, Pages und
Bericht. Das ist auditierbarer als ein reiner Fließtext-Research-Report.

## Belastbare Kernaussagen

- Eval-Ausführung, Mutation und Promotion sind verschiedene Rollen.
- Deterministische Orakel und harte Gates gehen vor gewichteten Soft Scores.
- Train/Development, Candidate Selection und versteckter Holdout benötigen
  getrennte Informationsgrenzen.
- Ein Patch Loop braucht unveränderliche Evaluatorflächen, Diff-/Dateigrenzen,
  Budget, Archiv, Canary und Rollback.
- Eine Dataset-Architektur ist noch kein valider Datensatz; Case-Gültigkeit,
  Orakel, Repräsentativität und Leakage müssen gemessen werden.
- Benchmark-Erfolg beweist nur Leistung auf dem gebundenen Dataset, Commit und
  der gebundenen Konfiguration.

## Claims mit notwendiger Herabstufung

- Neue 2026-Preprints zu autonomer Evolution sind meist E2–E3 und nicht breit
  repliziert.
- Einzelne Verbesserungszahlen aus kleinen SWE-bench-Subsets generalisieren
  nicht auf andere Repositories oder Aufgabenverteilungen.
- GitHub-Stars messen Aufmerksamkeit, nicht Eval-Validität oder Production
  Readiness.
- Ein LLM-Judge ist nicht durch ein separates Modell automatisch unabhängig;
  Rubrik, Daten, Modellfamilie und Fehlerkorrelation müssen kalibriert werden.
- Ein zusammengesetzter Dataset-Quality-Score darf keine fehlenden Orakel oder
  Leakage hinter einem Mittelwert verstecken.

## Urteil

Die Research-Struktur ist eine gute Hypothesen- und Quellenbasis. Sie wird als
sekundäre Synthesequelle verwendet; starke Architekturclaims werden zusätzlich
gegen die jeweiligen Papers, offiziellen Repositories oder Standards geprüft.
