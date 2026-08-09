---
id: source-agent-evaluation-research-2026
type: source
title: Agent Evaluation Research August 2026
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-09T08:20:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

# Agent Evaluation Research — August 2026

Aktuelle Primärquellen, geprüft am 2026-08-09:

- Agentic Benchmark Checklist:
  https://arxiv.org/abs/2507.02825
- AgentRewardBench:
  https://arxiv.org/abs/2504.08942
- AJ-Bench / Agent-as-a-Judge:
  https://arxiv.org/abs/2604.18240
- TRACE / cross-step trajectory monitoring:
  https://arxiv.org/abs/2606.07054
- GroundEval / deterministische stateful evaluation:
  https://arxiv.org/abs/2606.22737
- GEPA / reflective prompt evolution:
  https://arxiv.org/abs/2507.19457
- SWE-bench Live:
  https://arxiv.org/abs/2505.23419
- SWE-bench Illusion:
  https://arxiv.org/abs/2506.12286

## Evidence audit

### Benchmark validity — E4 direction, E3 measurements

Die Agentic Benchmark Checklist zeigt konkrete Fehler in Task Setup und Reward
Design, die Rankings stark verzerren können. Der generalisierbare Schluss ist
nicht eine bestimmte Prozentzahl, sondern: Der Evaluator und die Aufgaben
selbst brauchen Tests, adversariale Negativfälle und eine Validitätsprüfung.

### Trajectory judges — E3, workload-bound

AgentRewardBench vergleicht automatische Evaluatoren gegen expertengelabelte
Web-Agent-Trajektorien. AJ-Bench erweitert den Judge um aktive
Umgebungsinteraktion. Beide stützen Kalibrierung gegen menschliche oder
deterministische Referenzen; sie beweisen keinen universellen Judge.

### Long-horizon evidence — E2–E3, neu

TRACE akkumuliert Evidenz über entfernte Schritte statt nur einzelne Fenster
oder den finalen Output zu beurteilen. Das ist besonders für Sabotage und lange
kausale Ketten relevant, stammt aber aus zehn SHADE-Arena-Domains und ist noch
kein allgemeiner Produktionsstandard.

### Deterministische stateful evaluation — E2, starkes Pattern

GroundEval prüft Search-, Fetch-, Access- und Zeitpfade gegen Zustandswahrheit.
Das Pattern passt zu agentischen Systemen mit kontrollierbarer Umgebung. Die
Publikation ist sehr neu und ihre Fallstudien ersetzen keine unabhängige
Replikation.

### Eval-guided optimization — E3 innerhalb getesteter Tasks

GEPA verwendet Trajektorien und textuelle Reflexion, um Promptvarianten über
eine Pareto-Selektion zu entwickeln. Die berichtete Sample Efficiency gilt für
die untersuchten Tasks. Für sichere Selbstverbesserung bleiben Holdout,
unveränderliche Gates, Patchgrenzen, Canary und Rollback zusätzlich nötig.

### Contamination resistance — konvergierende E3-Evidenz

SWE-bench Illusion findet Hinweise auf Memorisation und Artefaktnutzung.
SWE-bench Live verwendet neuere, ausführbare Repositoryaufgaben. Daraus folgt:
öffentliche statische Benchmarks sind Entwicklungsbaselines, aber keine
ausreichende finale Evidenz für generalisierbare Coding-Agent-Fähigkeit.
