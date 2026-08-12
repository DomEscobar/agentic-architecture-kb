---
id: source-retrieval-context-landscape-2026-08
type: source
title: Retrieval, Reranking, and Context Assembly Evidence Audit August 2026
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T22:05:00+02:00
updated_at: 2026-08-12T22:05:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Retrieval, Reranking, and Context Assembly Evidence Audit — August 2026

Primary research checked on 2026-08-12:

- [BEIR, NeurIPS Datasets and Benchmarks 2021](https://openreview.net/forum?id=wCu6T5xFjeJ)
- [Dense Passage Retrieval, EMNLP 2020](https://aclanthology.org/2020.emnlp-main.550/)
- [Reciprocal Rank Fusion, CIKM 2009](https://doi.org/10.1145/1571941.1572114)
- [Query2doc, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.585/)
- [HyDE, ACL 2023](https://aclanthology.org/2023.acl-long.99/)
- [IRCoT, ACL 2023](https://aclanthology.org/2023.acl-long.557/)
- [Cross-encoding reranking, DialDoc 2022](https://aclanthology.org/2022.dialdoc-1.13/)
- [Joint Passage Ranking for diverse evidence, EMNLP 2021](https://aclanthology.org/2021.emnlp-main.560/)
- [Maximal Marginal Relevance, SIGIR 1998](https://doi.org/10.1145/290941.291025)
- [RECOMP, ICLR 2024](https://openreview.net/forum?id=mlJLVigNHp)
- [LongLLMLingua, ACL 2024](https://aclanthology.org/2024.acl-long.91/)
- [Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9/)
- [ALCE citation evaluation, EMNLP 2023](https://aclanthology.org/2023.emnlp-main.398/)
- [Attributable to Identified Sources, Computational Linguistics 2023](https://aclanthology.org/2023.cl-4.2/)
- [Self-RAG, ICLR 2024](https://openreview.net/forum?id=hSyW5go0v8)
- [SemEval 2026 multi-turn retrieval system](https://aclanthology.org/2026.semeval-1.225/)
- [MTRAGEval organizer paper, SemEval 2026](https://aclanthology.org/2026.semeval-1.447/)
- [S2G-RAG, ACL 2026](https://aclanthology.org/2026.acl-long.1185/)
- [Mixture of Retrievers, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.601/)
- [Abstain-QA, COLING 2025](https://aclanthology.org/2025.coling-main.627/)

## Evidence classes

Peer-reviewed benchmark and mechanism papers are E3 for the workloads they
actually evaluate, not universal production guarantees. Metadata and permission
filtering is an architectural invariant but lacks a single comparable benchmark,
so its operational card remains E2. Multi-query expansion and hard abstention
also remain E2: positive mechanisms exist, but recent controlled task evidence
shows query expansion can degrade precision, and evidence-sufficiency thresholds
are strongly application- and risk-dependent.

## Supported conclusions

BM25 remains a mandatory, inspectable control, especially for identifiers and
domain terms. Dense retrieval addresses vocabulary mismatch, while deterministic
rank fusion can combine complementary lexical and dense candidate sets without
requiring comparable score scales. Neither dense nor hybrid is a universal winner:
BEIR shows large dataset-to-dataset variation and the 2026 SemEval system reports
that more complex multi-query variants degraded its development results.

Reranking only reorders candidates that first-stage retrieval found. Cross-encoders
can improve relevance ordering but add pairwise compute and can suppress necessary
diversity. MMR-like selection trades some individual relevance for novelty; this is
useful for multi-facet evidence, not as a default for single-answer questions.

Query rewriting, decomposition and iterative retrieval should be routed to the
failure they address. Query2doc and HyDE improve selected zero-shot retrieval
settings, but generated expansions can inject false anchors. IRCoT supports
interleaved retrieval for multi-hop questions; it does not justify an agent loop
for direct lookup.

Context compression and sentence selection can reduce tokens and distractors.
RECOMP and LongLLMLingua provide peer-reviewed evidence, while Lost in the Middle
shows why simply filling a long context can still fail. Compression is lossy:
qualifiers, negation, table structure and stable citation spans need explicit
retention checks and an uncompressed fallback.

ALCE and AIS establish that citation presence is weaker than attribution. A valid
citation must identify the evidence, support the attached claim and cover the
material claims in the answer. Abstention requires negative examples and calibrated
thresholds; a self-reported model confidence is not evidence sufficiency.

## Evaluation contract

Hold parser, chunks, corpus snapshot and permissions fixed while comparing the
retrieval stages. Report Recall@k curves, MRR or nDCG, required-evidence coverage,
unique evidence yield, ACL leakage, latency and cost. Then freeze the candidate
set when evaluating rerankers and freeze the ordered evidence when evaluating
compression or packing. Score answer correctness, unsupported-claim rate, citation
precision and recall, attribution entailment and calibrated abstention separately.
Use simple, multi-facet, multi-hop, exact-identifier, conversational, negative and
permission-boundary slices. No component may be promoted from aggregate answer
quality alone.
