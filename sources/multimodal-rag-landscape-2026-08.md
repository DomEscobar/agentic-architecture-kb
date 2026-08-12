---
id: source-multimodal-rag-landscape-2026-08
type: source
title: Multimodal RAG Evidence Audit 2026-08
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-12T22:08:00+02:00
updated_at: 2026-08-12T22:08:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Multimodal RAG Evidence Audit 2026-08

## Primary evidence

- [ColPali, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/99e9e141aafc314f76b0ca3dd66898b3-Abstract-Conference.html) and ViDoRe provide peer-reviewed page-image late-interaction retrieval evidence across visually rich tasks, domains and languages.
- [Multimodal Chart Retrieval, NAACL 2024](https://aclanthology.org/2024.naacl-long.307/) directly compares OCR text, chart derendering to tables, direct image retrieval and fusion. There is no universal lane winner; the combined method is strongest in its setting.
- [TableRAG, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.710/) shows why flattening heterogeneous tables can destroy structure and evaluates query decomposition plus SQL execution for multi-hop table/text reasoning.
- [MIEB, ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/html/Xiao_MIEB_Massive_Image_Embedding_Benchmark_ICCV_2025_paper.html) broadens image-embedding evaluation and documents weaknesses with interleaved inputs and confounders.
- [M3DocVQA, ICCV Workshop 2025](https://openaccess.thecvf.com/content/ICCV2025W/Findings/html/Cho_M3DocVQA_Multi-modal_Multi-page_Multi-document_Understanding_ICCVW_2025_paper.html) evaluates multi-page, multi-document retrieval and understanding; workshop evidence is useful but narrower than main-track replication.
- [FinRAGBench-V, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.211/) evaluates multimodal financial RAG with visual citation and makes citation localization an explicit end-to-end requirement.
- [Roles of MLLMs in Visually Rich Document Retrieval, IJCNLP-AACL 2025](https://aclanthology.org/2025.ijcnlp-long.2/) synthesizes captioning, embedding and end-to-end representation roles and their fidelity, latency and index-size trade-offs.
- [LAD-RAG, ACL 2026](https://aclanthology.org/2026.acl-long.724/) evaluates a symbolic layout graph alongside neural indexes for cross-page visually rich document retrieval.
- [Utility-Oriented Visual Evidence Selection, ACL 2026](https://aclanthology.org/2026.acl-long.1620/) evaluates evidence utility rather than similarity alone for bounded visual candidate selection.
- [Hybrid-Vector Retrieval, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.54/) evaluates single-vector first-stage efficiency combined with multi-vector accuracy.
- [Unified Multimodal Interleaved Document Representation, Findings EACL 2026](https://aclanthology.org/2026.findings-eacl.83/) evaluates document and passage retrieval for interleaved multimodal content.

## Evidence boundary

Peer-reviewed claims tied to the evaluated task are E3. New model repositories, vendor OCR, workshop-only systems and architecture inferences are E2. Page Recall@k does not establish answer correctness, exact numeric extraction, regional citation correctness or production latency.

## Architecture implications

Preserve page images and text/OCR identities. Put text, visual and structured-table lanes behind identical ACL and version filters. Fuse only after per-lane retrieval, deduplicate page hits, and retain coordinates or region identifiers through context assembly. Use exact extracted text for quotations and numbers even when visual retrieval found the page.

## Required slices

Evaluate clean prose, scans, forms, tables, charts, diagrams, slides, handwriting and mixed-language pages. Include visually similar wrong pages, correct text with wrong layout, OCR corruption, cross-page evidence, stale versions, hidden or redacted regions and questions whose answer is absent.
