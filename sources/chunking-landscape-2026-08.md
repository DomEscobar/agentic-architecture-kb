---
id: source-chunking-landscape-2026-08
type: source
title: Chunking Landscape and Use-Case Audit August 2026
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T20:50:00+02:00
updated_at: 2026-08-12T20:50:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Chunking Landscape and Use-Case Audit — August 2026

Primary research checked on 2026-08-12:

- [Semantic Chunking, Findings NAACL 2025](https://aclanthology.org/2025.findings-naacl.114/)
- [MoC: Mixtures of Text Chunking Learners, ACL 2025](https://aclanthology.org/2025.acl-long.258/)
- [Mix-of-Granularity, COLING 2025](https://aclanthology.org/2025.coling-main.384/)
- [Dense X Retrieval / propositions, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.845/)
- [RAPTOR, ICLR 2024](https://openreview.net/forum?id=GN921JHCRw)
- [cAST code chunking, Findings EMNLP 2025](https://aclanthology.org/2025.findings-emnlp.430/)
- [HiChunk and HiCBench, ACL 2026](https://aclanthology.org/2026.acl-long.1372/)
- [Late Chunking](https://arxiv.org/abs/2409.04701)
- [Adaptive Chunking, LREC 2026 paper and implementation](https://arxiv.org/abs/2603.25333)
- [Structure-Aware Tabular Chunking](https://arxiv.org/abs/2605.00318)
- [Structure-Aware Semantic Chunking with Title Chains](https://arxiv.org/abs/2608.00824)
- [Anthropic Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
- [PageIndex tree navigation](https://github.com/VectifyAI/PageIndex)

## Evidence classes

ACL, EMNLP, NAACL, COLING, ICLR and LREC publications are E3 for the evaluated
mechanism under their reported datasets. Current arXiv preprints, project-owned
repositories and vendor experiments are E2. None establishes a universal best
chunker because parser output, corpus structure, query granularity, retriever,
embedding model, context budget and evidence labels materially interact.

## Supported conclusions

Fixed token windows and structure-aware sections remain mandatory controls.
Semantic splitting has inconsistent benefits relative to its compute cost.
Fine-grained propositions can improve fact retrieval but add generation cost and
can detach qualifiers. Hierarchical and multi-granular methods help when questions
span levels of abstraction, but expand index and retrieval complexity. Code and
tables benefit from preserving their native structures rather than generic text
boundaries. HiCBench highlights that sparse-evidence QA benchmarks can conceal
chunking differences; evidence-dense, boundary-annotated evaluation is preferable.

## Selection dimensions

Select by source structure, answer locality, query granularity, atomicity needs,
embedding context limit, update frequency, access boundaries and ingestion budget.
Small units improve pinpoint retrieval but lose context and multiply vectors;
large units preserve context but dilute similarity and consume generation budget.
Overlap reduces boundary misses while duplicating evidence and index size.

## Evaluation contract

Use identical parsed source elements and question/evidence labels. Measure boundary
integrity, evidence Recall@k, MRR or nDCG, context precision, answer completeness,
citation correctness, duplicate evidence rate, vector count, ingestion time and
retrieval/generation latency. For prefixes, summaries or propositions, score
relevance against an invariant source view so generated text cannot make its own
candidate appear relevant. Parser defects remain parser defects.
