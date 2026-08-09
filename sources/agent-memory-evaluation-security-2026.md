---
id: source-agent-memory-evaluation-security-2026
type: source
title: Agent Memory Evaluation Security and Privacy 2026
status: reviewed
privacy: public
confidence: 0.87
created_at: 2026-08-09T16:10:00+02:00
updated_at: 2026-08-09T16:10:00+02:00
review_at: 2026-10-09
source_ids: []
relations: []
---

# Agent Memory Evaluation, Security and Privacy — August 2026

Primary sources:

- LongMemEval (ICLR 2025): https://openreview.net/forum?id=wIonk5yTDq
- LongMemEval-V2: https://github.com/xiaowu0162/LongMemEval-V2
- LoCoMo (ACL 2024): https://aclanthology.org/2024.acl-long.747/
- MemBench (ACL Findings 2025): https://aclanthology.org/2025.findings-acl.989/
- Mem2ActBench (ACL 2026): https://aclanthology.org/2026.acl-long.370/
- MemoryArena: https://arxiv.org/abs/2602.16313
- HaluMem: https://arxiv.org/abs/2511.03506
- WorldMemArena: https://arxiv.org/abs/2605.29341
- Agent Security Bench: https://openreview.net/forum?id=V4y0CpX4hK
- Memory poisoning study: https://arxiv.org/abs/2606.04329
- GhostWriter: https://arxiv.org/abs/2607.06595
- MEXTRA: https://aclanthology.org/2025.acl-long.1227/
- AgentLeak: https://arxiv.org/abs/2602.11510

## Evidence audit

LoCoMo and LongMemEval are useful conversational recall baselines but do not
fully test whether an agent recognizes when memory is needed, performs the
right action or avoids side effects. LongMemEval-V2, Mem2ActBench,
MemoryArena and WorldMemArena move toward state, workflow and action-dependent
memory. End-to-end accuracy still hides whether failure occurred during write,
maintenance, retrieval or use.

GhostWriter reports about 98 percent injection and 60 percent activation in
its tested setup; these are threat-model-specific figures, not universal
deployment rates. The systematic poisoning study identifies multiple write
channels and structural vulnerabilities. MEXTRA and AgentLeak show that output
inspection alone misses private information exposed through memory and
internal agent channels.

Deletion research remains less mature than retrieval. External memory should
first use lineage-aware deletion, index rebuild and adversarial verification;
model-weight unlearning is relevant only when data entered model weights.

