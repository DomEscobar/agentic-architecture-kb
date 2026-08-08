---
id: pattern-contextual-retrieval
type: pattern
title: Contextual Retrieval
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-08T18:20:00+02:00
updated_at: 2026-08-08T18:20:00+02:00
review_at: 2026-11-08
source_ids:
  - source-rag-developments-2026-batch-1
relations:
  - predicate: derived_from
    target: source-rag-developments-2026-batch-1
---

# Contextual Retrieval

## Mechanism

Generate a short prefix that situates a retrievable unit inside its parent
document, then index `prefix + unit` in both sparse and dense channels.

```text
document + target unit
 -> grounded context generator
 -> 50–100 token prefix
 -> lexical index + embedding index
 -> hybrid retrieval + optional reranker
```

The prefix should contain only retrieval-disambiguating context: document type,
section, subject, time/version and relationship to surrounding material. It must
not introduce facts absent from the document.

## Winning conditions

- repeated terms have different meanings across sections or documents;
- small units lose entity, time, product or policy context;
- corpus is indexed offline and the added indexing cost is amortized;
- both semantic and exact retrieval are useful.

## Failure modes

- LLM-generated context hallucinates or launders untrusted instructions;
- prefixes become repetitive and dominate BM25 or embeddings;
- changed parent documents leave stale prefixes;
- sensitive metadata is copied into less restricted indexes;
- larger context reduces precision or increases reranker truncation.

## Controls and evaluation

- derive prefix from the exact document version and store prompt/model/hash;
- label generated context separately from source text;
- cap length and reject unsupported entities, dates and numbers;
- rebuild on source or generator change;
- compare raw chunks, deterministic metadata headers and LLM contextualization;
- measure Recall@k, nDCG, downstream field accuracy, index cost and leakage.

Anthropic's reported 49% and 67% relative failure reductions are useful priors,
not deployment targets.
