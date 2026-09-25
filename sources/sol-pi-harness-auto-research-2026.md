---
id: source-sol-pi-harness-auto-research-2026
type: source
title: SoL-Pi Harness Auto-Research Evidence 2026
status: reviewed
privacy: public
confidence: 0.76
created_at: 2026-09-25T07:30:00+02:00
updated_at: 2026-09-25T07:30:00+02:00
review_at: 2026-11-25
source_ids: []
relations: []
---

# SoL-Pi Harness Auto-Research Evidence 2026

Primary: SoL-Pi, Recursively Scaling Auto-Research Loops for Efficient Agent
Harness, NVIDIA, NTU and MIT,
[arXiv:2609.20519v1](https://arxiv.org/abs/2609.20519v1), submitted 2026-09-17,
retrieved and inspected 2026-09-25. Code and project page released
([github.com/NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi)). Author-reported
preprint; no independent replication inspected.

## Reported method

- An optimizer inspects execution traces from a separate agent running the base
  harness, proposes candidate harness changes, and tests them in prepared
  environments.
- Scale reported: 152 proposed directions across six proposal families, 535
  executable environments (495 derived from GitHub issue and pull-request pairs
  with hidden regression tests verified to fail before and pass after the
  accepted patch, plus 40 synthetic verifier-driven tasks), more than 3,000 runs
  and more than 60,000 agent-environment interactions. The authors state these
  counts describe scope and do not establish a scaling law.
- Capability metrics, tolerances and efficiency metrics are fixed before
  experimentation and kept outside the optimizing agent's control. Acceptance
  applies two sequential gates: every capability metric within its predeclared
  tolerance, and at least one declared efficiency metric improved. Nondominated
  candidates are retained.
- EdgeBench is reserved for validation and kept out of search. Of its 51 public
  tasks, 11 are used for one-way acceptance of frozen candidates and 40 are
  reserved for final generalization. Held-out results never return to search.

## Retained mechanisms

- Action Fusion: combines a file mutation and its follow-up command into one
  request, removing an intermediate model round trip.
- Online Context Compact: compacts at plan-step boundaries only, and only when
  projected input savings exceed the estimated prompt-cache rewrite cost.
- ObservationPack: archives results above 10 KiB, sends them in full for two
  requests, then substitutes a stable handle, size and a short head-and-tail
  excerpt, with exact pages retrievable on demand.
- Evidence-Preserving Reducer: compresses build and test logs above 4 KiB with a
  lower-cost model into a receipt; a deterministic verifier checks schema,
  source hash, exit status, exact quotes and size, and the harness falls back to
  the original log on failure. File reads and search results bypass it.

## Reported results

- GPT-5.6 Sol, full four-mechanism stack: 1.10 B tokens, 49.0 percent fewer than
  the base harness, token cost 33.2 percent lower, average score 42.0 against
  44.8 (retaining 93.7 percent).
- Same backend, best single mechanism (ObservationPack): average score 44.8 to
  47.2, token traffic 6.1 percent lower, token efficiency 9.8 percent better.
- Transfer to Opus 5 without further search: 94.3 percent of base-harness score,
  44.7 percent less token traffic, 33.5 percent lower API cost.
- Cache trade-off reported: cache-read traffic falls from 2.1326 B to 1.0605 B
  while cache-write traffic rises from 0.0141 B to 0.0316 B; total cost falls
  from 1,339 to 894 USD.
- Terminal-Bench 4, 63 CPU-only tasks: base harness and a native harness each
  solve 18 tasks, SoL-Pi solves 15; total cost 211.12 against 286.45 USD and
  cost per solved task 14.07 against 15.91 USD.
- IMO 2026: six problems, SoL-Pi passes three at the lowest cost per passed
  problem (20.90 USD against 22.89 and 25.32), with a 150-minute cap per problem.
- Add-one ablation: every component reduces tokens under both backends. The
  authors state that comparisons on each configuration's own triggered-task
  subset do not isolate interaction effects.

## Limits

- Capability claims rest on small samples: 40 final EdgeBench tasks, 63
  Terminal-Bench tasks and six IMO problems. No confidence intervals were seen
  in the inspected text.
- The abstract's "comparable performance" understates a measured 6.3 percent
  score reduction at the efficiency operating point and fewer solved tasks on
  Terminal-Bench 4. Efficiency is robust; capability parity is not established.
- Cost figures use fixed API prices, and hourly savings are estimates that
  depend on utilization assumptions.
- Only two frontier backends were evaluated. Mechanism activation was lower on
  the backend the harness was not optimized on.
- Because 11 of the 51 public EdgeBench tasks took part in acceptance, "unseen"
  effectively means the remaining 40 tasks.
- ObservationPack depends on the agent retrieving handles later; silent evidence
  loss is plausible but not measured in the inspected text.
- The reducer adds a second model call and a second failure surface, mitigated
  by deterministic verification and fallback to the original log.

## Use in this KB

Supports the search-process view of harness improvement and supplies a concrete
gate-isolation design. Treat the four mechanisms as a configurable
efficiency operating point, not as a free improvement.
