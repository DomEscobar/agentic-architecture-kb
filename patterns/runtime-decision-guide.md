---
id: pattern-runtime-decision-guide
type: pattern
title: Runtime Decision Guide
status: reviewed
privacy: internal
confidence: 0.85
created_at: 2026-08-08T16:45:00+02:00
updated_at: 2026-08-08T16:45:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-agentic-runtime-techniques
relations:
  - predicate: derived_from
    target: source-domescobar-agentic-runtime-techniques
---

# Runtime Decision Guide

## Auswahl nach dominanter Anforderung

- Kurze Tool-Aufgabe: Action Loop + Stopper + Fehlerbehandlung.
- Mehrstufige Aufgabe: Plan-and-Execute + typisierter Task-State.
- Objektiv prüfbares Ergebnis: Verifier Loop; deterministische Checks zuerst.
- Offene Recherche: Research Loop + Claim/Evidence-Ledger + Gap Analysis.
- Codeänderung: Coding Harness + Isolation + Tests + Rollback.
- Hintergrundarbeit: durable Workflow + Queue + Checkpoints + Idempotenz.
- Riskante externe Aktion: Approval Interrupt + Audit + Edit/Reject-Pfad.
- Mehrere Spezialisten: Supervisor/Planner-Executor nur bei separatem Kontext,
  Werkzeug, Authority oder messbarer Parallelität.
- Wiederkehrende Sitzungen: kontrollierte Memory-Promotion + Forgetting.
- Harte Reasoning-Aufgabe: Test-time Compute nur mit Budget und Verifier.

## Entscheidungsfragen

1. Welche objektive Done-Bedingung existiert?
2. Kann ein Schritt externe, finanzielle oder irreversible Wirkung haben?
3. Muss der Run Prozessausfälle überleben?
4. Welche Zustände müssen exakt replaybar sein?
5. Sind Schritte idempotent; falls nein, welche Kompensation existiert?
6. Brauchen Rollen getrennten Kontext, Tools oder Berechtigungen?
7. Welche maximale Zeit, Kosten, Toolcalls, Tiefe und Fan-out gelten?
8. Was ist der Kill Switch, und wie wird zurückgerollt?
9. Welche Offline-Replays und Online-Signale beweisen Verbesserung?

## Default

Starte mit einem Agenten, einer primären Schleife, typisiertem State,
deterministischen Checks, harten Budgets und vollständigem Trace. Füge
Orchestrierung erst hinzu, wenn ein konkretes Eval-Defizit die zusätzliche
Komplexität rechtfertigt.
