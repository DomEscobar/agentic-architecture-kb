---
id: source-domescobar-eval-oigl
type: source
title: DomEscobar Eval-Oigl
status: reviewed
privacy: public
confidence: 0.94
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-11-09
source_ids: []
relations: []
---

# DomEscobar/Eval-Oigl

- Repository: https://github.com/DomEscobar/Eval-Oigl
- untersuchter Commit: `b8d6a13d3220afb3f6ddc4d5f0e350f70142653f`
- Permalink: https://github.com/DomEscobar/Eval-Oigl/tree/b8d6a13d3220afb3f6ddc4d5f0e350f70142653f
- abgerufen: 2026-08-09
- Sprache/Toolchain: Go 1.23
- Lizenz: Im untersuchten Commit wurde keine LICENSE-Datei gefunden; daher keine
  Open-Source-Lizenz annehmen.

## Verifizierter Stand

`go test ./...` lief am untersuchten Commit über alle Pakete erfolgreich. Das
belegt interne Testkonsistenz, nicht die externe Validität der Eval-Metriken.

OIGL implementiert einen vom System under Test getrennten Eval-Harness mit:

- versionierten Eval Packs für Targets, Capabilities, Cases und Manifest;
- vollständigem Pack-, Manifest- und Konfigurations-Hash;
- unabhängiger Identität von Runtime und optionalem LLM-Judge;
- mechanischen Scorern für Toolwahl, Argumente, verbotene Tools, Trace-Schritte,
  Grounding, Terminalzustand und Budgets;
- kausaler Verknüpfung von Tool Calls und Observations über IDs;
- Attempt Receipts, Campaigns, Events, Recovery und read-only Reports;
- separaten Full-, Targeted- und Confirmation-Runs;
- expliziter Acceptance, die Pack-Hash, Commit, Coverage, Scorer und Bindings
  erneut prüft.

## Starke Architekturentscheidungen

1. Der Harness importiert keine Produktionsruntime; HTTP/JSON ist die Grenze.
2. Eval-Bedeutung lebt im versionierten Pack, nicht in CLI-Defaults.
3. Mechanische Evidenz wird vor semantischer Plausibilität geprüft.
4. Ein PASS wird erst nach separater Confirmation explizit akzeptiert.
5. Reports präsentieren persistierte Evidenz, ändern aber keine Kampagne.

## Grenzen und offene Risiken

- Ein grüner interner Testlauf kalibriert weder Cases noch LLM-Judge gegen
  menschliche Labels.
- Eine einzige Confirmation schützt nicht gegen stochastische Flakiness; die
  nötige Wiederholungszahl muss pro Slice empirisch bestimmt werden.
- Das Packmodell enthält keine eigenständige, für den Optimierer abgeschottete
  Holdout-/Redteam-Verwaltung.
- Kein universeller Trace darf erzwungen werden: alternative korrekte
  Trajektorien müssen erlaubt bleiben, während kausale Invarianten gelten.
- Live Targets und Judge-Endpunkte können Kosten oder Side Effects erzeugen;
  Packs sind deshalb ausführbare, reviewpflichtige Konfiguration.
- Externe Outcome- und Judge-Validierung wurde in diesem Audit nicht gefunden.

## Evidenzgrad

E3 für die beobachtete Implementierung und die erfolgreichen Repositorytests.
E1–E2 für Aussagen über allgemeine Messvalidität, bis OIGL gegen menschlich
gelabelte Trajektorien, absichtlich defekte Agents und reale Failure Slices
kalibriert wurde.
