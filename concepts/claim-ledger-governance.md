---
id: concept-claim-ledger-governance
type: concept
title: Claim Ledger Governance
status: reviewed
privacy: public
confidence: 0.94
created_at: 2026-08-12T18:40:00+02:00
updated_at: 2026-08-24T09:55:00+02:00
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
kind, evidence level, source pages, scope, limitations, and a review date.

## Claim kinds

- `empirical`: a measured or observed property of a system, benchmark or
  workload. Promotion follows the evidence-level bar.
- `normative`: a design, governance or threat-model requirement. It may be
  accepted at E2 when the requirement is inspectable, but it does not inherit
  empirical authority from the citation apparatus.

## Promotion contract

- E1 remains a hypothesis and cannot be `accepted`, regardless of kind.
- Empirical E2 stays `provisional`; it may support a canary, not a default.
- Empirical E3 may be `accepted` as a bounded recommendation for matching
  workloads.
- Normative E2 may be `accepted` as a requirement, not as a performance result.
- E4 requires convergent or reproduced evidence under comparable conditions.
- Numeric claims still require denominator, metric, evaluation scope and source.
- `accepted` requires at least one source whose `auditability` is not `private`.
- Contradictions are bidirectional `contradicts` edges; both claims become
  `contested` or `superseded`. They are never silently removed.

## Utility gate

A paper, repository, release, benchmark, or scout result is never itself a
promotion unit. A candidate claim enters canonical content only when it:

- answers a concrete architecture or coding-agent decision;
- adds a mechanism, boundary, failure mode, or regression test not already
  represented by the KB;
- can state `use_when`, exclusions, evidence limits, and a verification path;
- is narrower than or equal to the supporting evidence; and
- improves retrieval precision enough to justify its maintenance cost.

Candidates that are indirect, redundant, unactionable, artifact-incomplete, or
only academically interesting remain in the research inbox or source registry.
Popularity and a `READ` scout verdict are discovery signals, not promotion
evidence.

## Dated change records

Every canonical novelty, correction, supersession, or reversion appends one
record to `changes/ledger.jsonl`. The record pins the decision date, affected
targets, rationale, practical impact, and status. Existing page timestamps,
claim review dates, and technique freshness metadata continue to describe the
target itself; the append-only ledger records why and when the KB changed.

## Mechanical guarantees

The linter rejects malformed claims or change records, duplicate IDs, missing
section IDs, unknown claim sources or change targets, kind/level/status
combinations that violate the promotion contract, accepted claims backed only
by private sources, and one-sided contradiction edges. The compiled JSON
contains both ledgers so retrieval and evaluation systems can expose provenance
and dated change history with answers.
