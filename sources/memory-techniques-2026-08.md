---
id: source-memory-techniques-2026-08
type: source
title: Agent Memory Technique Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-12T22:05:00+02:00
updated_at: 2026-08-12T22:05:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Agent Memory Technique Evidence Audit — August 2026

Primary sources checked on 2026-08-12:

- [MemGPT](https://arxiv.org/abs/2310.08560)
- [Generative Agents](https://arxiv.org/abs/2304.03442)
- [Agent Workflow Memory](https://arxiv.org/abs/2409.07429)
- [Graphiti](https://arxiv.org/abs/2501.13956)
- [LongMemEval, ICLR 2025](https://openreview.net/forum?id=wIonk5yTDq)
- [MemBench, Findings ACL 2025](https://aclanthology.org/2025.findings-acl.989/)
- [Amory, EACL 2026](https://aclanthology.org/2026.eacl-long.183/)
- [CTIM-Rover negative result, REALM 2025](https://aclanthology.org/2025.realm-1.30/)
- [Memory poisoning study, 2026](https://arxiv.org/abs/2606.04329)
- [When Experience Hurts, ACL 2026](https://aclanthology.org/2026.acl-long.27/) provides a peer-reviewed negative result for uncritically reusing retrieved experience.
- [AgeMem, ACL 2026](https://aclanthology.org/2026.acl-long.981/) and [Memory-R1, ACL 2026](https://aclanthology.org/2026.acl-long.583/) evaluate learned memory-management mechanisms within their tested workloads.
- [Visual Inception, ACL 2026](https://aclanthology.org/2026.acl-long.954/) provides narrow peer-reviewed evidence for multimodal memory poisoning.

## Evidence boundary

The evidence distinguishes working context, immutable episodes, consolidated
semantic facts, temporally scoped relations and reusable procedures. No paper
establishes one universal memory architecture. Amory supplies peer-reviewed,
workload-specific evidence for narrative consolidation; CTIM-Rover is an
important negative result showing that retrieved episodes can add distracting
noise and reduce software-agent performance.

LongMemEval and MemBench support multi-session recall evaluation but cannot by
themselves prove correct writes, action selection, permissions or deletion.
Memory transformations are derived claims, not ground truth. They need lineage
to immutable source events, extractor identity, temporal validity and a
rebuildable index.

## Security and lifecycle conclusion

Untrusted content must not directly author preferences, permissions or
procedures. Write admission, quarantine and conflict handling are separate
from read ranking. Expiry, supersession, archival, index removal and verified
erasure are also distinct operations. Evaluate the full write-maintain-read-use
chain and include poisoned, stale, conflicting and irrelevant memories.
