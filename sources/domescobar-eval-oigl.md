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
- Reviewed commit: `b8d6a13d3220afb3f6ddc4d5f0e350f70142653f`
- Permalink: https://github.com/DomEscobar/Eval-Oigl/tree/b8d6a13d3220afb3f6ddc4d5f0e350f70142653f
- Retrieved: 2026-08-09
- Language/toolchain: Go 1.23
- License: no LICENSE file was found in the reviewed commit; do not assume an
  open-source license.

## Verified state

`go test ./...` passed across all packages at the reviewed commit. This
demonstrates internal test consistency, not external validity of the evaluation
metrics.

OIGL implements an evaluation harness separated from the system under test with:

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

## Evidence level

E3 for the observed implementation and passing repository tests. E1–E2 for
claims about general measurement validity until OIGL is calibrated against
human-labeled trajectories, deliberately defective agents, and real failure
slices.
