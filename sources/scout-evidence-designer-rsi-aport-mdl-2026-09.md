---
id: source-scout-evidence-designer-rsi-aport-mdl-2026-09
type: source
title: September 2026 Evidence — Procedural Memory, Authorization, and Memory Abstention
status: reviewed
privacy: public
confidence: 0.74
created_at: 2026-09-21T08:15:00+02:00
updated_at: 2026-09-21T08:15:00+02:00
review_at: 2026-10-21
source_ids: []
relations: []
---

# September 2026 Evidence — Procedural Memory, Authorization, and Memory Abstention

Primary sources reviewed on 2026-09-21:

- [Designer-RSI](https://arxiv.org/abs/2609.22086)
- [APort Vault](https://arxiv.org/abs/2609.22076)
- [APort Vault dataset](https://huggingface.co/datasets/aporthq/vault-benchmark-v1)
- [Interpretable Memory Decision Controller](https://arxiv.org/abs/2609.22043)

## Evidence boundaries

Designer-RSI is E3 provisional evidence for evolving natural-language skills
around frozen agents. The reported held-out comparison supports testing coupled
skill acquisition and revision against either mechanism alone. It does not
establish domain-general self-improvement: the workload is graphic design, user
traffic and the tool environment are private, graders are substantially
automated, and generation latency increased.

APort Vault is E3 provisional evidence for a deterministic authorization
boundary around agent payment actions. Its large matched replay and separate
request, policy and execution events are stronger than an aggregate safety
score. The result remains specific to one payment policy, attack cohort and
public CTF; it does not establish zero risk for other tools or adaptive attacks.

The Memory Decision Controller is E2 evidence for evaluating an abstention layer
before retrieved memory enters model context. In a small constructed TruthfulQA
conflict setting, conflicting memory harmed the baseline and the controller
reduced that loss. Its lexical risk signals, preview-model dependencies, narrow
sample and absent independent implementation do not justify a default
controller architecture.

## Durable evaluation implications

- Evaluate procedural-memory patches with frozen-context paired replay, shared
  baselines, isolated acquisition/revision arms and protected no-regression
  slices. A bounded admission rule may require at least one demonstrated win and
  no detected protected-slice loss; it is not proof of universal improvement.
- Record authorization as separate request, policy-decision, tool-call and
  externally observed effect events. Deterministic policy enforcement remains
  outside the model and must be tested with permitted as well as denied actions.
- Compare memory-augmented answers with a memory-free control under clean,
  stale, contradictory and adversarial evidence. Evaluate pre-injection
  abstention independently from retrieval recall and generation quality.

