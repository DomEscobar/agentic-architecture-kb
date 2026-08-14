---
id: source-parser-landscape-2026-08
type: source
title: Parser Landscape and Use-Case Audit August 2026
status: reviewed
privacy: public
confidence: 0.87
created_at: 2026-08-12T20:20:00+02:00
updated_at: 2026-08-12T20:29:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Parser Landscape and Use-Case Audit — August 2026

Primary sources checked on 2026-08-12:

- benchmarks: [OmniDocBench, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html), [ParseBench](https://arxiv.org/abs/2604.08538), [MPDocBench-Parse](https://arxiv.org/abs/2605.22100), [olmOCR-Bench](https://github.com/allenai/olmocr);
- local/native: [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/faq/index.html), [Apache Tika](https://tika.apache.org/3.0.0/formats.html);
- local multi-format: [AnyDoc](https://github.com/firecrawl/anydoc), [Microsoft MarkItDown](https://github.com/microsoft/markitdown), [Xberg, formerly Kreuzberg](https://github.com/xberg-io/xberg), [pdfplumber](https://github.com/jsvine/pdfplumber);
- local pipelines and VLMs: [Docling](https://docling-project.github.io/docling/usage/), [MinerU](https://github.com/opendatalab/MinerU/blob/master/docs/en/index.md), [Marker](https://github.com/datalab-to/marker/blob/master/README.md), [olmOCR](https://github.com/allenai/olmocr), [PaddleOCR](https://www.paddleocr.ai/main/en/version3.x/algorithm/PP-StructureV3/PP-StructureV3.html), [Unstructured](https://unstructured.readthedocs.io/en/latest/best_practices/table_extraction_pdf.html);
- managed: [LlamaParse](https://developers.api.llamaindex.ai/api/python/resources/parsing/methods/create/), [Mistral OCR](https://docs.mistral.ai/studio-api/document-processing/basic_ocr), [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout?view=doc-intel-3.1.0), [Google Document AI](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk), [Amazon Textract](https://aws.amazon.com/documentation-overview/textract/).

## Evidence interpretation

Official documentation is E2 evidence for supported mechanisms, formats and
deployment options—not comparative accuracy. OmniDocBench is E3 benchmark
evidence. ParseBench, MPDocBench-Parse and current vendor/project benchmarks are
E2 pending peer review or independent replication. ParseBench's main finding is
more useful than its leaderboard: capability is fragmented and no method is
consistently strong across tables, charts, formatting, faithfulness and visual
grounding.

## Parser families

- **Native extraction:** cheapest and fastest for born-digital files; weak when
  reading order or visual structure is not encoded correctly.
- **Modular layout/OCR pipeline:** inspectable stages and local deployment;
  detector/OCR/table errors can cascade but are diagnosable.
- **End-to-end VLM:** often stronger on visually difficult pages and natural
  reading order; requires GPU/API capacity and can generate plausible structure.
- **Managed document AI:** low operational burden and specialized form/table
  features; adds data-boundary, pricing, version-drift and lock-in concerns.

## Selection rule

Route by document slice rather than selecting one global parser. Preserve a
native fast path for clean text, a structured local path for layout-heavy pages,
and an expensive VLM/API fallback for hard cases. Every candidate is evaluated
on identical pages with field fidelity, reading order, table/figure/formula
structure, downstream retrieval/citation correctness, latency, cost and failure
rate. Parser changes always create a new immutable parse and index identity.

## Important non-comparability

Benchmark versions, page subsets, rendering DPI, prompts, model revisions,
hardware and output normalization materially change results. Project-owned
leaderboards are useful discovery evidence, not proof that their own parser is
best for a private corpus. Licensing and residency must be checked at adoption
time rather than inferred from model weights or SDK licences.

## Multi-format converter addendum

AnyDoc is a distinct useful class: a pure-Rust, local, non-ML converter for Word,
PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV and text-based PDF. It normalizes
these formats through a shared document model into GitHub-Flavored Markdown and
also exposes Node, Python, Rust and browser-WASM bindings. Image-only PDFs are an
explicit unsupported case and require routing to OCR. Its published 100-document
benchmark is project-owned, uses an undistributed corpus and an LLM judge, so its
quality and speed claims remain E2 until independently reproduced.

MarkItDown is a lightweight Python conversion layer across office documents,
PDF, images, audio, HTML, archives and other formats. Local converters can be
augmented by plugins, vision models or Azure services. Its permissive conversion
entry point can access local or remote resources with process privileges, so
untrusted ingestion must use narrow byte/stream APIs and URI restrictions.

Xberg (formerly Kreuzberg) is a Rust-core polyglot document-intelligence framework
covering documents, office formats, images, email, archives, academic formats and
code. It supports multiple OCR/VLM backends, plugins, CLI, libraries, REST and MCP.
These broad capability claims are project documentation, and its Elastic License
2.0 requires a commercial-use review before adoption.

pdfplumber remains a valuable narrow instrument for machine-generated PDFs when
character, line, rectangle and table geometry or visual table debugging matter.
Its documentation explicitly says it works best on machine-generated rather
than scanned PDFs; it is not an OCR fallback.

Pandoc, Mammoth and headless LibreOffice remain converter or rendering fallbacks,
not general parser cards. They may be evaluated for their specific native formats,
but they do not replace OCR, layout analysis or visual document understanding.
