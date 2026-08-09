---
id: pattern-verified-procedural-memory
type: pattern
title: Verified Procedural and Skill Memory
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: [source-agent-memory-foundations-2026, source-agent-memory-evaluation-security-2026]
relations:
  - predicate: derived_from
    target: source-agent-memory-foundations-2026
  - predicate: evaluated_by
    target: source-agent-memory-evaluation-security-2026
---

# Verified Procedural and Skill Memory

A procedure is executable capability, not a prose fact. Store purpose,
preconditions, postconditions, tool/API versions, permissions, dependencies,
known failures, producing traces, test results, owner and expiry.

Candidates come from successful trajectories but are admitted only after
isolated replay, forbidden-side-effect checks, regression comparison and human
approval where risk warrants. Selection requires task fit and satisfied
preconditions. Execute with least privilege, budget and kill switch. Record the
actual outcome and demote on drift or repeated failure.

Promotion uses development/selection/hidden holdout; canary before broad use;
rollback restores the accepted procedure. A successful historical trajectory
does not prove transfer to a changed environment.

