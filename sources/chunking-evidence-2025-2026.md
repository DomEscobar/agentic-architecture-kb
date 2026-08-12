---
id: source-chunking-evidence-2025-2026
type: source
title: Chunking Evidence Audit 2025–2026
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T18:41:00+02:00
updated_at: 2026-08-12T18:41:00+02:00
review_at: 2026-11-12
source_ids: []
relations: []
---

# Chunking Evidence Audit 2025–2026

Primary sources checked on 2026-08-12:

- [Is Semantic Chunking Worth the Computational Cost?, Findings NAACL 2025](https://aclanthology.org/2025.findings-naacl.114/)
- [MoC: Mixtures of Text Chunking Learners, ACL 2025](https://aclanthology.org/2025.acl-long.258/)
- [Structure-Aware Semantic Chunking with Title-Chain Prefixes, 2026 preprint](https://arxiv.org/abs/2608.00824)

## Evidence class

The two ACL Anthology papers are E3. The August 2026 structure-aware study is E2:
it reports a substantial, carefully sliced single-corpus evaluation, but is a
fresh preprint without independent replication.

## Supported conclusion

Semantic chunking is not a universal upgrade over fixed-size segmentation. The
NAACL study evaluates document retrieval, evidence retrieval and answer
generation and finds no consistent gain that justifies its computational cost.
MoC supplies evidence that query granularity and chunking policy can interact,
but its learned mixture adds complexity and does not establish a general
default. The 2026 title-chain study is promising for structured Markdown but
also identifies an evaluation trap: changing indexed prefixes can alter both
retrieval and relevance scoring unless the scorer uses a controlled view.

## Required baseline

Every chunking experiment keeps a simple token-window baseline and a
structure-aware baseline. It varies one factor at a time where possible:
boundary policy, target size, overlap, contextual prefix, parent expansion and
retrieval depth. Report index size, ingestion cost, Recall@k, evidence coverage,
context precision, answer quality and citation correctness.

## Transfer limits

Results depend on parser output, query granularity, embedding model, retriever,
reranker, context budget and relevance labels. A chunker cannot repair missing
or misordered source content.
