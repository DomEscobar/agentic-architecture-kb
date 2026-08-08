---
id: pattern-pageindex-reasoning-tree-retrieval
type: pattern
title: PageIndex Reasoning Tree Retrieval
status: reviewed
privacy: internal
confidence: 0.84
created_at: 2026-08-08T17:15:00+02:00
updated_at: 2026-08-08T17:15:00+02:00
review_at: 2026-10-08
source_ids:
  - source-vectifyai-pageindex
relations:
  - predicate: derived_from
    target: source-vectifyai-pageindex
---

# PageIndex / Reasoning Tree Retrieval

## Mechanism

```text
document
 -> parse pages and structure
 -> TOC/tree detection or generation
 -> align titles to physical pages
 -> summarize nodes
 -> persist versioned JSON tree

query
 -> inspect document/tree metadata
 -> reason over titles + summaries
 -> select nodes/page ranges
 -> fetch raw content
 -> answer/verify with page citations
```

This is **structure-guided agentic retrieval**. It changes the candidate
generation mechanism; it does not remove the need for parsing, context assembly,
generation, grounding checks or evaluation.

## Winning conditions

- one or a few long, strongly hierarchical documents;
- meaningful TOC, headings, numbered sections, appendices and cross-references;
- high value per query and tolerance for seconds rather than millisecond search;
- questions whose relevant evidence is structurally related but not lexically or
  semantically similar to the query;
- page-level traceability is more important than high throughput.

Typical candidates are financial filings, contracts, regulations, manuals and
technical reports.

## Losing conditions

- very large, heterogeneous multi-document corpora without a reliable document
  router;
- short, flat, noisy, scanned or weakly structured content;
- high-QPS autocomplete or interactive search with tight tail latency;
- queries dominated by exact identifiers, names or rare strings where lexical
  search is cheaper and deterministic;
- environments where document content may not be sent to the configured LLM.

## Recommended production composition

Do not choose “tree or vectors” globally. Use an adaptive front door:

```text
query classifier
  -> exact/entity query: metadata + BM25/FTS
  -> semantic cross-corpus query: dense + sparse + RRF
  -> structure/multi-hop query within selected long docs: PageIndex tree search
  -> union evidence -> rerank/coverage -> grounded generation
```

For multi-document use, first select candidate documents using metadata,
lexical/dense retrieval or a separately evaluated document tree. Then use
PageIndex inside only the selected documents. This bounds prompt size, cost and
latency.

## Required controls

- pin parser, prompt, model and tree-schema versions;
- store tree-build trace and validate page-range coverage;
- treat document text as untrusted evidence, never instructions;
- enforce maximum navigation steps, tokens, pages and cost;
- use cache keys derived from document hash and index configuration;
- fall back to lexical/dense retrieval when tree creation or navigation fails;
- keep tenant/ACL filtering outside and before agentic navigation;
- prevent model-generated node IDs from accessing unauthorized documents;
- verify final citations against fetched page ranges.

## Evaluation

Compare at least four paired systems on the same corpus and generator:

1. full/long context baseline where feasible;
2. BM25 or database FTS;
3. dense+sparse hybrid with RRF and optional reranking;
4. PageIndex tree retrieval;
5. adaptive router combining the preceding methods.

Measure retrieval Recall@k/nDCG, evidence coverage, answer field accuracy,
faithfulness, citation correctness, abstention, indexing cost, per-query cost,
p50/p95 latency and failure rate. Slice by document length, hierarchy quality,
scan/OCR quality, query type and corpus size.
