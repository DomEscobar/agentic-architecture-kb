---
id: synthesis-agentic-runtime-techniques
type: synthesis
title: Agentic Runtime Techniques
status: reviewed
privacy: internal
confidence: 0.82
created_at: 2026-08-08T16:45:00+02:00
updated_at: 2026-08-08T16:45:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-agentic-runtime-techniques
relations:
  - predicate: derived_from
    target: source-domescobar-agentic-runtime-techniques
---

# Agentic Runtime Techniques

## Kernaussage

Eine Runtime ist keine einzelne Agentenschleife. Die kleinste brauchbare
Architektur kombiniert genau **eine primäre Kontrollschleife** mit den
querschnittlichen Schichten, die Risiko, Dauer und Betriebsumgebung verlangen.
Mehr Schleifen und mehr Agenten sind keine automatische Verbesserung.

## A. Kontrollschleifen

### 1. Action Loop

`observe -> reason/plan -> act -> observe -> stop/repeat`

Für kurze, interaktive Tool-Aufgaben. Erforderlich sind Tool-Verträge,
Fehlerbehandlung, Stop-Kriterium und harte Budgets. Allein ungeeignet für lange,
irreversible oder korrektheitskritische Arbeit.

### 2. Plan-and-Execute

`plan -> execute step -> observe -> revise -> next step`

Für mehrstufige Arbeit mit sichtbarem Fortschritt. Plan als versioniertes
Artefakt speichern und Stale-Plan-Erkennung vorsehen. Nicht einsetzen, wenn die
Aufgabe in einem Schritt lösbar oder überwiegend explorativ ist.

### 3. Verifier Loop

`attempt -> deterministic check -> fix/finish/escalate`

Für Aufgaben mit überprüfbaren Akzeptanzkriterien. Tests, Schemas und Invarianten
haben Vorrang vor einem LLM-Judge. Verifier-Unabhängigkeit und Retry-Limit sind
notwendig, weil ein schwacher Checker falsche Fertigmeldungen legitimiert.

### 4. Bounded Retry

`bounded attempt -> explicit result/failure -> retry/fresh context/escalate`

Zeit-, Kosten-, Schritt- und Kontextgrenzen machen Scheitern zu einem expliziten
Zustand. Zwischen Versuchen wird nur typisierter State übertragen; sonst trägt
ein frischer Kontext dieselben Fehler weiter.

### 5. Reflection/Memory

`act -> evaluate -> candidate lesson -> validate/promote -> reuse`

Reflexionen dürfen nicht direkt in kanonisches Memory geschrieben werden.
Promotion benötigt wiederholte Evidenz, Provenienz, Ablaufdatum und Rollback.

### 6. Research Loop

`question -> query batch -> read -> claim/evidence ledger -> gap analysis -> repeat`

Die entscheidende Runtime-Komponente ist der Claim-/Evidence-Ledger, nicht der
Webzugriff. Stoppen bei gedeckten Kernclaims, ausgeschöpftem Budget oder fehlender
neuer Evidenz.

### 7. Experiment Loop

`propose -> isolated run -> measure -> paired comparison -> keep/revert`

Nur mit fixierter Baseline, kontrollierter Varianz und unveränderlichem
Experiment-Log. Einzelne erfolgreiche Runs reichen nicht zur Promotion.

### 8. Multi-Agent Orchestration

`decompose -> typed tasks -> isolated workers -> typed results -> review/merge`

Nur einsetzen, wenn getrennte Kontexte, Werkzeuge, Autoritäten oder echte
Parallelität den Koordinationsaufwand überwiegen. Tiefe, Turns und Fan-out
begrenzen; Ownership und Merge-Semantik explizit machen.

### 9. Durable Runtime

`load -> work -> checkpoint -> wait -> resume`

Benötigt persistente Zustandsmaschine, idempotente Schritte, Lease/Single-runner,
Retry/Backoff, Migrationen und Recovery-Semantik. Ein langer Chatturn ist kein
durabler Workflow.

### 10. Coding Harness

`isolate -> edit -> test -> review -> merge/revert`

Git-Diff, Worktree/Branch, ausführbare Checks, Reviewer und Rollback bilden die
Runtime-Grenze. Ohne belastbare Tests bleibt auch ein Multi-Agent-Review schwach.

## B. Querschnittliche Runtime-Schichten

1. **Test-time Compute:** mehrere Kandidaten nur unter hartem Compute-Budget und
   mit belastbarem Selektor.
2. **HITL/Governance:** riskante Aktionen als resumable Interrupt modellieren,
   nicht als informelle Rückfrage.
3. **Security/Capabilities:** Trust Zones, Least Privilege und Action Firewall
   vor Toolausführung.
4. **Context/Memory:** Packing, Paging, Retrieval-Caps, Promotion und Forgetting.
5. **Harness/Composition:** Agentenkern von Session, UI, Queue und Persistenz
   trennen.
6. **Protocols:** MCP/A2A nur an Grenzen, an denen Portabilität oder Remote-
   Interoperabilität tatsächlich gebraucht wird.
7. **Observability/Provenance:** append-only Events, Run Receipts, Claim- und
   Artifact-IDs sowie replaybare Zustandsübergänge.
8. **Cost/Serving:** Budgets, Model Routing, Caching und Latenz-SLOs als Runtime-
   Policy statt Prompt-Hinweis.

## Kompositionsregel

```text
request
  -> identity + trust classification
  -> capability + budget policy
  -> one primary control loop
  -> verifier / approval where required
  -> append-only events + checkpoints
  -> result with provenance
```

## Evidenzstatus

Die Taxonomie ist eine nützliche Synthese, aber nicht experimentell als Ganzes
validiert. Einzelne Techniken besitzen unterschiedliche Evidenz. Insbesondere
2026-Patterns aus einzelnen Preprints bleiben Hypothesen beziehungsweise
Kandidaten, bis unabhängige Replikation oder eigene Evals vorliegen.
