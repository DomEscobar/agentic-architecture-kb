---
id: pattern-runtime-safety-baseline
type: pattern
title: Runtime Safety Baseline
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

# Runtime Safety Baseline

Diese Baseline gilt unabhängig vom gewählten Agenten-Framework.

## Vor dem Run

- Originalintention unveränderlich erfassen.
- Nutzer, Projekt und Datenschutz-Scope bestimmen.
- Kontext als trusted instruction, trusted data oder untrusted evidence labeln.
- minimale, zeitlich begrenzte Capabilities ausstellen.
- Budgets für Zeit, Tokens, Kosten, Calls, Delegationstiefe und Fan-out setzen.

## Während des Runs

Separate conversational checkpoints from external side effects. Non-idempotent
effects need runtime-generated causal IDs, commit-time authority checks and a
transactional or reconcilable effect ledger; replaying chat state is insufficient.

- jeden Zustandsübergang und Toolversuch append-only protokollieren;
- Toolargumente gegen Schema und Policy prüfen;
- vorgeschlagene Aktionen erneut gegen Originalintention und Trust Zone prüfen;
- Side Effects mit Idempotency Key oder Saga/Compensation schützen;
- No-progress-, Repeat- und Budget-Breaker erzwingen;
- vor riskanten oder irreversiblen Aktionen resumable Approval Interrupt.

## Nach dem Run

- Verifier entscheidet anhand expliziter Akzeptanzkriterien;
- Run Receipt enthält Inputs/Outputs als Referenzen, Toolresultate, Kosten,
  Zustandsübergänge und Provenienz;
- Secrets und private Inhalte gemäß Policy redigieren;
- Memory-Lektionen nur als Inbox-Kandidaten schreiben;
- Recovery-, Replay- und Rollback-Pfad regelmäßig testen.

## Minimale Evals

- Prompt-Injection über Toolresultat, Webseite und Memory;
- Capability-Eskalation und Cross-project-Zugriff;
- doppelte Zustellung und Crash zwischen Side Effect und Checkpoint;
- unendliche Schleife, No-progress und Budgetüberschreitung;
- fehlerhafter Verifier und falsche Fertigmeldung;
- Replay nach Schema-/State-Migration;
- Löschung eines Memory-Eintrags einschließlich aller Projektionen.
