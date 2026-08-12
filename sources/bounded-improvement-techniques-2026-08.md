---
id: source-bounded-improvement-techniques-2026-08
type: source
title: Bounded Improvement Technique Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.82
created_at: 2026-08-12T22:05:00+02:00
updated_at: 2026-08-12T22:05:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Bounded Improvement Technique Evidence Audit — August 2026

Primary sources checked on 2026-08-12:

- [MIPROv2](https://arxiv.org/abs/2406.11695)
- [GEPA, ICLR 2026](https://openreview.net/forum?id=RQm2KQTM5r)
- [Darwin Gödel Machine, 2025](https://arxiv.org/abs/2505.22954)
- [Red Queen Gödel Machine, 2026](https://arxiv.org/abs/2606.26294)
- [SePO, 2026](https://arxiv.org/abs/2606.04465)
- [Externally grounded verification of agent loops, 2026](https://arxiv.org/abs/2607.25152)
- [GEPA counterevidence from defective seeds, ACL SRW 2026](https://aclanthology.org/2026.acl-srw.8/) shows that prompt optimization can regress sharply when its starting material or feedback is defective.

## Evidence boundary

MIPROv2 and GEPA support bounded search over prompts and demonstrations on the
tested workloads. They do not prove transfer to a different model, task
distribution or production policy. DGM supports archive-based modification of
a coding-agent implementation under a fixed benchmark and search process, but
does not demonstrate domain-general or indefinitely safe recursive improvement.

RQGM and SePO explore objective or optimizer co-evolution. They are recent
preprints and remain E2 experimental evidence. A candidate that evaluates its
own work through the same information channel can mistake plausible activity
for external progress; the July 2026 externally grounded verification study is
fresh E2 evidence for keeping a world-state oracle outside the mutable surface.

## Promotion boundary

Safe improvement means a bounded, versioned mutable surface; fixed budgets;
shared baselines; protected selection and holdout tasks; immutable safety
sentinels; sandboxed execution; and human-controlled canary promotion with a
kill switch and rollback. Changing the evaluator starts a new governed epoch
and invalidates naive before/after comparisons.
