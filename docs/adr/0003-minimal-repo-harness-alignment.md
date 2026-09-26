---
id: decision-minimal-repo-harness-alignment
type: decision
title: ADR-0003 Minimal Repository-Harness Alignment
status: reviewed
privacy: internal
confidence: 0.8
created_at: 2026-09-26T10:10:00+02:00
updated_at: 2026-09-26T10:10:00+02:00
review_at: 2026-12-26
source_ids: []
relations: []
---

# ADR-0003: Minimal Repository-Harness Alignment

## Context

`adobe/ai-repo-harness-guide` (v1.1.0, Apache-2.0) was reviewed on 2026-09-26.
It is a repository-layout and control-layer guide with ten chapters and two
shipped skills, not a measured effectiveness study.

The substance is already carried by
`patterns/project-coding-agent-harness.md`: instruction contract, tool and
retrieval contract, skill admission, enforcement and authority, project eval
suite and anti-slop gate. The guide contributes form: a five-layer taxonomy,
sensor severity tiers, a canonical-source rule, and a portable file layout.

Six agent failure classes are documented in this workspace: wrong or stale
anchors, stale handoff status, unproven "done" claims, test-archive
contamination, commit-author drift, and child tasks ending at raw artifacts.
The guide addresses one of these directly, two indirectly, and three not at all.

The guide itself reports that LLM-generated context files can reduce task
success and that human-written context files help inconsistently. This
workspace's own record points the same way: prose rules were followed
inconsistently while executable checks held.

## Decision

Adopt the guide's form in a deliberately thin, check-bound variant: three
artifacts and three missing sensors. Do not adopt the guide wholesale.

1. Keep one `INVARIANTS.md` per agent-operated repository. Every entry is a hard
   non-negotiable and points to the executable check that enforces it. No
   invariant without a check. Canonical-source rule: one location per rule, and
   `AGENTS.md` links rather than duplicates.
2. Keep `AGENTS.md` short and operational: commands, boundaries, footguns,
   escalation paths. Hard rules move out by link; duplicated copies are deleted.
3. Add the three missing sensors as code, not prose:
   - a commit-author expectation check, because repeated commits were made under
     an unintended default author identity;
   - a test-discovery exclusion so archived source copies under `evidence/` are
     not collected by the test runner, after 17 failed test files from stale
     archived copies;
   - a status supersede check so a newer review supersedes a stale "review
     unavailable" continuation pointer.

   Anchor validation already exists in the knowledge tooling and stays
   unchanged.
4. Place repo-local skills under `.agents/skills/` with pinned provenance, and
   admit them only after inspecting the source commit and digest, the declared
   tools, egress and write scope.

## Non-goals

Explicitly not adopted: the seven-component program, module-level `AGENTS.md`
everywhere, a second taxonomy beside the KB patterns, LLM-authored context
files, judge sensors as a default, and documentation as a substitute for
executable gates.

## Consequences

- Positive: one canonical location per hard rule; three observed failure classes
  gain an executable guard; repo-local skills become portable across agent
  hosts.
- Negative: another always-loaded file consumes context; the new sensors are
  code to maintain; the benefit is unproven until measured.
- Risk: drift returns if `AGENTS.md` copies rules instead of linking. The
  canonical-source rule is checked at each freshness cycle.

## Acceptance and measurement

Count, from the local artifact record, over two weeks before and after adoption:
failed agent runs caused by (1) wrong or stale anchors, (2) stale handoff status,
(3) unproven "done" claims, and (4) test-archive contamination. Revert the
convention if the counters do not move.

## Open items

- Chapters 4 and 5 of the guide and the two shipped skills (`harness-setup`,
  `harness-inspect`) are not yet audited. No adoption of those skills before
  that audit.
- Whether a separate `INVARIANTS.md` reduces or increases drift is itself
  untested here.

## Alternatives

- Full adoption of the guide's layout: rejected. Ceremony without measurement,
  added context cost and duplication against existing patterns.
- No change: rejected. The canonical-source rule and the three missing sensors
  target failures already observed in this workspace.
- Documentation-only convention without sensors: rejected. This workspace's
  record shows prose rules were followed inconsistently while executable checks
  held.
