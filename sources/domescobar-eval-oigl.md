---
id: source-domescobar-eval-oigl
type: source
title: DomEscobar Eval-Oigl
status: reviewed
privacy: public
confidence: 0.55
created_at: 2026-08-09T08:20:00+02:00
updated_at: 2026-08-14T10:47:00+02:00
review_at: 2026-11-09
auditability: private
source_ids: []
relations: []
---

# DomEscobar/Eval-Oigl

- Repository: `DomEscobar/Eval-Oigl` (private; not publicly resolvable)
- Reviewed commit: `b8d6a13d3220afb3f6ddc4d5f0e350f70142653f`
- Retrieved: 2026-08-09
- Language/toolchain: Go 1.23
- License: no LICENSE file was found in the reviewed commit; do not assume an
  open-source license.

## Reported state

The owner reported that `go test ./...` passed across all packages at the
reviewed commit. That result is not independently reproducible from this
knowledge base. Even if re-run, it would demonstrate internal test consistency,
not external validity of the evaluation metrics.

The snapshot is reported to implement an evaluation harness separated from the
system under test with:

- Versioned evaluation packs for targets, capabilities, cases, and manifest
- Complete pack, manifest, and configuration hashes
- Independent identities for the runtime and optional LLM judge
- Mechanical scorers for tool choice, arguments, forbidden tools, trace steps,
  grounding, terminal state, and budgets
- Causal linking of tool calls and observations through IDs
- Attempt receipts, campaigns, events, recovery, and read-only reports
- Separate full, targeted, and confirmation runs
- Explicit acceptance that rechecks pack hash, commit, coverage, scorers, and
  bindings

## Strong architecture decisions

1. The harness does not import the production runtime; HTTP/JSON is the boundary.
2. Evaluation semantics live in the versioned pack, not CLI defaults.
3. Mechanical evidence is checked before semantic plausibility.
4. A PASS is explicitly accepted only after separate confirmation.
5. Reports present persisted evidence but do not mutate a campaign.

## Limits and open risks

- A passing internal test run calibrates neither cases nor the LLM judge against
  human labels.
- One confirmation does not protect against stochastic flakiness; required
  repetitions must be determined empirically per slice.
- The pack model has no separate holdout/red-team management isolated from the
  optimizer.
- No universal trace should be imposed: alternative correct trajectories must
  remain valid while causal invariants are enforced.
- Live targets and judge endpoints can create cost or side effects; packs are
  therefore executable configurations that require review.
- This audit found no external outcome or judge validation.

## Auditability

This repository is private. The commit hash identifies the reviewed snapshot for
the repository owner, but no reader outside that account can retrieve the code,
re-run `go test ./...` or contradict the observations above. The passing test run
is reported, not independently reproducible.

Claims resting only on this source stay `provisional` at E1. The accepted claims
that cite this page also cite public evidence, which carries the promotion; this
page contributes design detail and a worked implementation, not proof.

## Evidence level

E1 as published evidence, because the artifacts are unavailable for external
audit. The implementation observations and passing repository tests would rate
E3 for the owner, and that gap is exactly what the private boundary costs.
General measurement validity remains E1 for everyone until OIGL is calibrated
against human-labeled trajectories, deliberately defective agents, and real
failure slices.
