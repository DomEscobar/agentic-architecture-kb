---
id: source-multimodal-document-retrieval-2025
type: source
title: Multimodal Document Retrieval Evidence 2025
status: reviewed
privacy: public
confidence: 0.9
created_at: 2026-08-12T18:41:00+02:00
updated_at: 2026-08-12T18:41:00+02:00
review_at: 2026-11-12
source_ids: []
relations: []
---

# Multimodal Document Retrieval Evidence 2025

Primary sources checked on 2026-08-12:

- [ColPali, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/99e9e141aafc314f76b0ca3dd66898b3-Abstract-Conference.html)
- [ColPali paper and ViDoRe benchmark](https://arxiv.org/abs/2407.01449)
- [ViDoRe artifacts](https://huggingface.co/vidore/collections)

## Evidence class

ColPali is E3 peer-reviewed evidence for page-level retrieval over visually rich
documents. ViDoRe spans several domains, languages and practical page retrieval
settings. It does not evaluate every downstream generator or operational stack.

## Mechanism

ColPali embeds page images with a vision-language backbone and uses late
interaction between query and visual patch representations. It can retrieve
layout, tables, figures and typography without first reducing the page to plain
text. The tradeoff is a larger multi-vector index and more expensive scoring
than a single-vector text retriever.

## Architecture boundary

Visual retrieval is a candidate-generation lane. It does not replace document
versioning, ACL filters, text/OCR extraction for exact citations, freshness,
reranking, answer grounding or end-to-end application replay. A practical
system can route visual-heavy queries to the visual lane and fuse those
candidates with lexical and dense text retrieval.

## Required evaluation

Measure page Recall@k and nDCG, evidence-region coverage, downstream answer and
citation correctness, index bytes per page, query latency, ingestion throughput
and modality-specific failure slices. Compare against text-only, OCR+text and
long-context baselines under the same corpus and query set.
