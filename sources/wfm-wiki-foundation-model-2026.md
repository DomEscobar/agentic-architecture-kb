---
id: source-wfm-wiki-foundation-model-2026
type: source
title: Wiki Foundation Model Evidence 2026
status: reviewed
privacy: public
confidence: 0.7
created_at: 2026-09-23T11:00:00+02:00
updated_at: 2026-09-23T11:00:00+02:00
review_at: 2026-10-23
source_ids: []
relations: []
---

# Wiki Foundation Model Evidence 2026

Primary paper: [WFM: Wiki Foundation Model for Complex Agentic Reasoning](https://arxiv.org/abs/2609.18182v1),
v1 submitted 2026-09-16, retrieved and inspected 2026-09-23. Tencent Youtu Lab,
Monash University and others. Author-reported preprint; no independent
reproduction, released training corpus or verified code path.

## Claimed contribution

- Represents an "LLM Wiki" substrate as a hybrid graph: typed entity-relation
  edges plus dense document passages kept as first-class nodes rather than
  reduced to triples.
- Propagates entity and passage states jointly in one embedding space using
  relation-aware attention.
- Applies attention variance regularization to prevent uniform-attention
  collapse on dense wikis.
- Uses an NCCL-native boundary exchange with hoisted static partition indices
  and fixed-shape GPU collectives instead of CPU-serialized boundary sync.

## Reported results

End-to-end LLM-judged accuracy: HotpotQA 89.6 open / 84.3 reject, 2Wiki 90.2 /
82.4, MuSiQue 69.8 / 52.6; reported gains over Youtu-GraphRAG of 2.8/4.1, 3.2/4.8
and 4.1/5.1 points. Reported Recall@20 of 93.20 / 90.15 / 75.24, with MuSiQue
within 0.66 points of the strongest baseline. Memory QA: PersonaMem 58.49 and
RHELM 52.17 accuracy, reported 8.39 and 5.37 points above the strongest
baseline, with Recall@20 of 52.63 and 60.03. Reported training speedup of 10.5x
(2.40s to 0.23s per step) with node states preserved.

## Limits

- Author-reported v1 preprint with no independent replication; the draft still
  carries template placeholders and no verified code artifact was inspected.
- The headline 10.5x is a distributed training-speed result for their own
  implementation change, not an inference, retrieval-quality or cost result.
- WFM is a pretrained graph foundation model over a large wiki corpus. It is not
  a drop-in retrieval component and is not adoptable without comparable corpus
  and multi-GPU training infrastructure.
- Reported gains concentrate at larger retrieval depth: the advantage over
  strong baselines is small at small k and grows with k, which shifts context
  budget and serving cost rather than removing them.
- MuSiQue recall is reported within 0.66 points of Youtu-GraphRAG at k=20, and
  PersonaMem recall is reported slightly below A-mem at k=5.
- No production evidence is reported for latency, deletion propagation, tenancy,
  ACL enforcement or freshness under corpus change.

## Use in this KB

Relevant to RAG representation choice and agentic-memory substrate design, and as
an evaluation-design reference for separating evidence-grounded from permissive
answer grading. It does not supersede hybrid or graph retrieval defaults.
