---
id: pattern-visual-late-interaction-retrieval
type: pattern
title: Visual Late-interaction Retrieval
status: reviewed
privacy: internal
confidence: 0.88
created_at: 2026-08-08T18:20:00+02:00
updated_at: 2026-08-08T18:20:00+02:00
review_at: 2026-11-08
source_ids:
  - source-rag-developments-2026-batch-1
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-1
---

# Visual Late-interaction Retrieval

## Mechanism

Render each document page as an image, encode it into multiple visual-language
vectors and score a text query against page tokens/patches via late interaction.
ColPali is the canonical example.

```text
page image -> VLM multi-vector index
query text -> query vectors
late interaction -> ranked pages
selected page image/text -> extraction + generation
```

## Winning conditions

- layout, tables, figures, fonts or spatial relationships carry meaning;
- OCR order and text flattening destroy useful structure;
- page-level retrieval is an acceptable first-stage granularity;
- GPU/storage budget supports multi-vector indexing and search.

## Limitations

- finding the page is not extracting a precise cell or calculating an answer;
- page-level candidates can be too broad for long dense pages;
- multi-vector storage and late interaction can be expensive at corpus scale;
- accessibility, redaction and deterministic text search still need OCR/text;
- visual prompt injection and hidden content remain security concerns;
- citations require stable document/page identity and preferably extracted spans.

## Recommended composition

Use visual retrieval as another recall channel, not a replacement for every
representation:

```text
metadata filter
 -> visual page retrieval || OCR/BM25 || dense text retrieval
 -> fusion/reranking
 -> targeted text/table extraction from selected pages
 -> structured, cited generation
```

Evaluate on layout-heavy and OCR-hard slices using page Recall@k, downstream
field/table accuracy, citation correctness, storage, indexing throughput and
p95 query latency.
