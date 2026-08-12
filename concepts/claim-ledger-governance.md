---
id: concept-claim-ledger-governance
type: concept
title: Claim Ledger Governance
status: reviewed
privacy: public
confidence: 0.94
created_at: 2026-08-12T18:40:00+02:00
updated_at: 2026-08-12T18:40:00+02:00
review_at: 2026-11-12
source_ids:
  - source-agent-evaluation-research-2026
relations:
  - predicate: derived_from
    target: source-agent-evaluation-research-2026
---

# Claim Ledger Governance

`claims/ledger.jsonl` is the machine-checkable registry for durable technical
claims. A claim points to the exact wiki section that states it, records its
evidence level, names source pages, bounds its scope and limitations, and has a
review date.

## Promotion contract

- E1 remains a hypothesis and cannot support a reviewed default.
- E2 may support a canary or provisional pattern.
- E3 may support a bounded recommendation for matching workloads.
- E4 requires convergent or reproduced evidence under comparable conditions.
- Numeric claims still require denominator, metric, evaluation scope and source.
- Contradictions change status to `contested`; they are never silently removed.

## Mechanical guarantees

The linter rejects malformed claims, duplicate claim IDs, missing section IDs
and references to unknown or non-source pages. The compiled JSON contains the
ledger so retrieval and evaluation systems can expose provenance with answers.
