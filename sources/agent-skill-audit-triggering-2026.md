---
id: source-agent-skill-audit-triggering-2026
type: source
title: Agent Skill Triggering in Smart Contract Audits 2026
status: reviewed
privacy: public
confidence: 0.73
created_at: 2026-10-03T12:46:00+02:00
updated_at: 2026-10-03T12:46:00+02:00
review_at: 2026-12-02
auditability: public
source_ids: []
relations:
  - predicate: supports
    target: pattern-project-coding-agent-harness
---

# Agent Skill Triggering in Smart Contract Audits — 2026

Primary: [Demystifying Agent Skills for Smart Contract Auditing, arXiv:2609.29454v1](https://arxiv.org/html/2609.29454v1), inspected 2026-10-03. The user-supplied research ZIP contained an unauthenticated text copy; the original arXiv page was checked separately. Author-run preprint, not independently reproduced here. The paper reports a corpus of 83 audit skills and seven agent/model configurations on EVMBench; its domain is smart-contract security, not generic repository maintenance.

## Triggering and downstream result

In the reported Codex/GPT-5.5 condition the with-skill arm found 97 of 120 benchmark vulnerabilities against 79/120 without skills. This is an author-reported matched condition, not a general skill effect. In a DeepSeek-V4-Pro CLI condition no skill was triggered in 40 audits; zero triggers does not say what a *correctly invoked* skill would have accomplished. The paper's main contribution for a project harness is diagnostic: separate **eligible skill**, **trigger**, **content loaded**, **content actually used**, **valid finding**, **false finding**, and **final project outcome**, each by model, task and skill. End-to-end quality alone hides failure to load a skill at all.

## Limits and decision

The sampled skills are heterogeneous and the observed effects are model/host dependent. These comparisons do not isolate skill prose from trigger/routing, nor establish utility for non-audit code changes. Add an activation/use funnel to a project-specific skill admission replay; treat a skill that is never eligible or never triggered as a routing failure before judging its body. Require a paired fresh-context project holdout with identical executor/tool permissions and measured false positives before accepting a skill edit. No blanket skill recommendation follows from 97/120.
