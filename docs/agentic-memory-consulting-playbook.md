# Agentic Memory Consulting Playbook

Start at [Agentic Memory Architecture and Lifecycle](../syntheses/agentic-memory-architecture.md).

## Brownfield

1. Complete the intake in [Agent Memory Brownfield Audit and Greenfield Intake](../patterns/agent-memory-consulting-intake.md).
2. Trace real records across write, update, retrieval, use and deletion.
3. Compare the runtime/store against [Framework Selection](../patterns/agent-memory-framework-selection.md).
4. Run the [Evaluation Blueprint](../patterns/agent-memory-evaluation-blueprint.md).
5. Produce risk slices, minimum remediation, rollout gates and rollback.

## Greenfield

Start with checkpointed run state, an event ledger, versioned records and FTS.
Add embeddings, temporal graphs, consolidation and skill memory only when the
corresponding workload slice improves under equal budgets without violating
privacy, safety, recovery or deletion gates.

Required design artifacts: data-flow/threat model, memory schema, write and
read policies, correction/supersession policy, retention/erasure map, eval
strategy, go-live scorecard, observability plan, kill switches and rollback.

