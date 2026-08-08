---
id: synthesis-rag-pipeline-taxonomy
type: synthesis
title: RAG Pipeline Taxonomy
status: reviewed
privacy: internal
confidence: 0.9
created_at: 2026-08-08T17:15:00+02:00
updated_at: 2026-08-08T17:15:00+02:00
review_at: 2026-11-08
source_ids:
  - source-domescobar-bauhelfer-ki
  - source-vectifyai-pageindex
relations:
  - predicate: derived_from
    target: source-domescobar-bauhelfer-ki
  - predicate: derived_from
    target: source-vectifyai-pageindex
---

# RAG Pipeline Taxonomy

## Why this split matters

“Use PageIndex”, “use GraphRAG” or “use a vector database” describes only part
of a system. RAG quality is an end-to-end property. We classify techniques by
the pipeline stage they change and evaluate both stage-local and final outcomes.

## 1. Ingestion and representation

Transforms source artifacts into retrievable units while preserving evidence.

- OCR and layout-aware parsing;
- tables, images and multimodal extraction;
- fixed, recursive, semantic or structure-aware segmentation;
- contextual headers and document summaries;
- entities, relations and knowledge-graph projection;
- PageIndex-style hierarchical document trees;
- versioning, deduplication, deletion and provenance.

Primary metrics: parse field accuracy, table fidelity, hierarchy accuracy,
coverage, duplication rate, index freshness and cost per document.

## 2. Retrieval and candidate generation

Finds potentially relevant evidence.

- metadata/ACL filtering;
- SQL and exact lookup;
- BM25/full-text/sparse retrieval;
- dense embedding retrieval;
- hybrid fusion such as RRF;
- multi-vector or late-interaction retrieval;
- PageIndex/tree navigation;
- graph traversal;
- query rewriting, decomposition and multi-query retrieval;
- iterative or agentic retrieval with stop conditions.

Primary metrics: Recall@k, Precision@k, MRR, nDCG, evidence coverage, diversity,
latency and cost. Retrieval must be evaluated before blaming generation.

## 3. Augmentation and context construction

Converts candidates into the evidence package actually shown to the model.

- reranking;
- deduplication and near-duplicate collapse;
- parent/neighbor expansion;
- section/page-window expansion;
- lost-in-the-middle ordering;
- diversity and sub-question coverage selection;
- compression and extractive evidence selection;
- contradiction detection;
- source trust, freshness and authority weighting;
- token-budget packing with stable citation anchors.

Primary metrics: context precision/recall, coverage per sub-question, token
efficiency, contradiction retention and citation-anchor validity.

## 4. Generation and answer contracts

Uses the evidence package to produce a bounded output.

- grounded prompts and explicit abstention;
- structured JSON/schema-constrained output;
- extract-then-synthesize;
- deterministic calculations outside the LLM;
- claim-level citations;
- assumptions, unknowns and conflicts as typed fields;
- answer decomposition and evidence-weighted synthesis;
- model routing by risk and complexity.

Primary metrics: field accuracy, faithfulness, unsupported claim rate, answer
relevance, calibration, completeness and cost.

## 5. Verification and control

Checks the output and decides whether to answer, retry or escalate.

- citation existence and entailment checks;
- deterministic business-rule validation;
- corrective retrieval when evidence is insufficient;
- cross-source corroboration;
- LLM judge only where deterministic checks are impossible;
- human approval for high-impact outputs;
- retry, latency and cost budgets.

Primary metrics: defect escape rate, false acceptance/rejection, abstention
quality, correction success and human-review load.

## 6. Evaluation and operations

- versioned golden datasets and realistic negative cases;
- stage-level ablations plus end-to-end replay;
- slices by document/query type, tenant, language and freshness;
- retrieval/generation traces with redaction;
- index manifests, canaries, feature flags and rollback;
- privacy, deletion and cross-scope leakage tests.

## Selection principle

Select one baseline per stage, then add complexity only where the error analysis
shows a bottleneck. For example, a reranker cannot repair missing OCR text, and
PageIndex cannot compensate for an incorrect page hierarchy. Likewise, strong
retrieval does not make an unconstrained generator safe.
