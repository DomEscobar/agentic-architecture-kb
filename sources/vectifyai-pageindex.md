---
id: source-vectifyai-pageindex
type: source
title: VectifyAI PageIndex and Mafin 2.5 FinanceBench
status: reviewed
privacy: public
confidence: 0.92
created_at: 2026-08-08T17:15:00+02:00
updated_at: 2026-08-08T17:15:00+02:00
review_at: 2026-10-08
source_ids: []
relations: []
---

# VectifyAI PageIndex

## Primary artifacts

- PageIndex repository: https://github.com/VectifyAI/PageIndex
- inspected PageIndex commit: `d5c4e62c20172ce400aef84545dfba3a0580b9ae`
- permalink: https://github.com/VectifyAI/PageIndex/tree/d5c4e62c20172ce400aef84545dfba3a0580b9ae
- Mafin evaluation repository: https://github.com/VectifyAI/Mafin2.5-FinanceBench
- inspected Mafin commit: `1c890d5e0fd9929953d38282614555847727011d`
- FinanceBench paper: https://arxiv.org/abs/2311.11944
- accessed: 2026-08-08

PageIndex is MIT-licensed. At retrieval time on 2026-08-08 GitHub reported
35,072 stars, 3,078 forks and 150 open issues; popularity is not evidence of
retrieval quality.

## Observed OSS mechanism

The indexer parses PDF or Markdown into a hierarchical JSON structure containing
node IDs, titles, page/line ranges, optional summaries and children. PDF tree
construction uses TOC detection where possible and LLM-assisted generation,
alignment, verification and repair otherwise. A preview `flash` path uses
heuristics for structure extraction and an LLM for optional summaries.

The retrieval module exposes document metadata, a tree without full node text,
and raw content for selected page ranges. The included agentic demo lets an LLM
inspect structure and request pages. Thus the open-source package supplies tree
construction and retrieval tools; the agent policy and final generation remain
separate components.

## Claim audit

### Supported

- No embeddings or vector database are required by the OSS path.
- Natural document hierarchy and page ranges replace fixed embedding chunks.
- Selected pages and node IDs provide explicit navigation provenance.
- PDF and Markdown are supported; a vision cookbook and commercial enhanced OCR
  path are documented.
- PageIndex and hosted API/MCP/enterprise options exist as separate offerings.

### Needs qualification

- **“No chunking”:** there are no conventional vector chunks, but indexing and
  retrieval still partition content into nodes, page groups and page ranges.
- **“Two calls per query”:** not guaranteed by the OSS implementation. Agentic
  navigation can make a variable number of model/tool calls.
- **Indexing/query cost multipliers:** workload-, model- and document-dependent;
  no general 5–25× factor was established from the primary artifacts reviewed.
- **Millions of documents:** presented by VectifyAI for PageIndex File System;
  not established here as an independently reproduced capability of the basic
  OSS package.
- **MCTS:** advanced hosted/product descriptions must not be attributed to the
  minimal OSS retrieval module unless the corresponding code and license are
  identified.

## 98.7% FinanceBench audit

The Mafin repository publishes 150 answers for GPT-4o and 150 for DeepSeek-v3,
an LLM-judge script and manual labels for 14 disputed cases. This is materially
more transparent than a bare chart. However:

- the result is produced and reported by PageIndex/VectifyAI, not an independent
  replication;
- the judge prompt accepts supersets, inferred answers and reasonable subjective
  interpretations, making it permissive;
- six of 14 manually reviewed disputes are labelled benchmark errors and five
  multiple-valid-approach;
- the public repository contains outputs rather than the full Mafin pipeline,
  exact retrieval traces, cost/latency logs and a one-command end-to-end replay;
- FinanceBench itself is primarily single-document QA and its authors describe
  the public evaluation sample as 150 cases from a 10,231-question dataset.

Conclusion: 98.7% is a vendor-reported result with inspectable outputs and partial
evaluation transparency, not proof that PageIndex dominates hybrid RAG across
domains or workloads.

## Maturity and security observations

The inspected PageIndex commit has a small unit-test surface relative to the
pipeline and no root `SECURITY.md`. Open issues visible during review included
malformed JSON, Markdown edge cases and a missing security policy. The code now
contains delimiter-neutralization tests, which is useful but not a complete
prompt-injection or document-security boundary.
