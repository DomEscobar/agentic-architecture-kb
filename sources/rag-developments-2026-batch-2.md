---
id: source-rag-developments-2026-batch-2
type: source
title: RAG Developments 2026 Research Batch 2
status: reviewed
privacy: public
confidence: 0.86
created_at: 2026-08-08T18:35:00+02:00
updated_at: 2026-08-08T18:35:00+02:00
review_at: 2026-10-08
source_ids: []
relations: []
---

# RAG Developments 2026 — Research Batch 2

Primary sources reviewed on 2026-08-08:

- RAG paradigm scaling study: https://arxiv.org/abs/2607.26497
- MarginMerge: https://arxiv.org/abs/2608.02969
- InfoGain-RAG: https://aclanthology.org/2025.emnlp-main.365/
- REFRAG: https://arxiv.org/abs/2509.01092
- Search-R3: https://arxiv.org/abs/2510.07048
- R3-RAG: https://arxiv.org/abs/2505.23794
- ReSearch: https://arxiv.org/abs/2503.19470
- Chain-of-Retrieval Augmented Generation: https://arxiv.org/abs/2501.14342
- CORAG cost-constrained retrieval: https://arxiv.org/abs/2411.00744
- GraphRAG-Bench: https://openreview.net/forum?id=i9q9xDMjG7
- T2-RAGBench: https://aclanthology.org/2026.eacl-long.8/

## Claim audit

### Scaling evidence

The 2026 scaling study compares lexical, dense, graph-based and file-system
agent paradigms over 28 nested corpus tiers from about 1,000 to 512,000
documents. In that controlled setting, BM25 occupied the low-cost Pareto edge at
all measured tiers and led accuracy from mid-scale onward. A raw file-system
agent degraded at scale, while replacing its file navigation with BM25 produced
the strongest full-scale result reported by the study.

This is important evidence, not a universal ranking. The study holds 150
questions, relevant/adversarial bedrock documents, reader and judging protocol
fixed. Its result may not transfer to semantic paraphrase-heavy, multilingual,
visual or relation-centric workloads. It establishes BM25 and Agent+BM25 as
mandatory scaling baselines.

### Visual index compression

MarginMerge compresses the patch embeddings stored by frozen multi-vector
visual retrievers. Across six datasets and two backbones, its authors report
retaining 97–99% of average nDCG@5 while removing 90–95% of stored document
vectors. It does not compress source files, replace the VLM generator or prove
equivalent end-to-end answer quality. The preprint was released on 2026-08-04;
independent replication and operational latency measurements are still absent.

### Generation-aware evidence selection

InfoGain-RAG defines document information gain using the change in a generator's
confidence with versus without a document, then trains a reranker from that
signal. This is a generator-conditioned utility objective rather than ordinary
query-document relevance. Reported gains are benchmark- and generator-specific;
the method adds costly counterfactual scoring during data construction and can
inherit generator calibration errors.

CORAG uses Monte Carlo Tree Search to select correlated chunk combinations under
a cost budget. This is context-set optimization, not the same method as
Chain-of-Retrieval Augmented Generation, which iteratively reformulates queries.

### Efficient decoding is not retrieval compression

REFRAG exploits sparse/block-structured attention over retrieved passages to
compress, sense and selectively expand context during decoding. The authors
report large time-to-first-token and context-capacity improvements. It changes
model inference and KV-cache behavior; it does not improve candidate recall,
reduce the retrieval index, or substitute for context selection. Deployment
requires model/runtime integration and independent validation on the target
hardware.

### Learned retrieval policies

Search-R3 trains an LLM to reason and emit retrieval embeddings. R3-RAG and
ReSearch use reinforcement learning to interleave reasoning and search. These
are trained policies, not prompt-only agent loops. They offer evidence that
retrieval behavior can be optimized against downstream outcomes, but introduce
training-data, reward-hacking, reproducibility and corpus-transfer risks.

### Evaluation

GraphRAG-Bench tests graph-oriented retrieval and generation under domain and
question slices; T2-RAGBench targets mixed text/table evidence. Both improve
coverage over generic QA sets, but neither replaces application-specific replay.
Retrieval, evidence packing and answer generation need separate metrics because
improvements at one stage need not survive downstream.

