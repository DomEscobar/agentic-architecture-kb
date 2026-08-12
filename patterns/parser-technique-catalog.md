---
id: pattern-parser-technique-catalog
type: pattern
title: Parser Technique Catalog
status: reviewed
privacy: public
confidence: 0.87
created_at: 2026-08-12T20:22:00+02:00
updated_at: 2026-08-12T20:29:00+02:00
review_at: 2026-10-12
source_ids:
  - source-parser-landscape-2026-08
relations:
  - predicate: derived_from
    target: source-parser-landscape-2026-08
  - predicate: depends_on
    target: pattern-parser-routing-matrix
---

# Parser Technique Catalog

The machine-readable cards under `techniques/parsers/` are the experiment
contract. This page makes the same catalog retrievable for architecture advice.
No entry is a universal winner; each must pass the private corpus slices.

## Native fast paths

- **PyMuPDF:** born-digital PDFs, bounding boxes, fast local extraction. Escalate
  scans, broken fonts, complex columns and layout-dependent tables.
- **Apache Tika:** broad format detection, metadata and text normalization. Use
  it as a front door and router, not as the final high-fidelity PDF parser.
- **AnyDoc:** fast local normalization of office, OpenDocument, EPUB, CSV, RTF
  and text PDFs to consistent Markdown. Route image-only PDFs to OCR.
- **pdfplumber:** detailed character and vector geometry plus debuggable table
  extraction for machine-generated PDFs; unsuitable as a scan parser.

## Local modular pipelines

- **Docling Standard:** mixed PDFs needing OCR, layout, tables and provenance;
  strong default when local inspectability matters.
- **MinerU:** scientific, multilingual and formula-heavy documents; validate its
  licence and each language/document slice.
- **Marker:** local PDF-to-Markdown with optional OCR and LLM escalation; gate
  unsupported content when LLM assistance is enabled.
- **PaddleOCR PP-StructureV3:** multilingual modular OCR plus layout, tables,
  formulas and charts; useful when stages must be replaceable or trainable.
- **Unstructured:** multi-format partitioning with fast, hi-res and OCR routing;
  convenient integration, but table and reading-order quality remain empirical.
- **Microsoft MarkItDown:** lightweight multi-format-to-Markdown integration with
  optional OCR, vision and Azure routes; sandbox untrusted file and URI inputs.
- **Xberg:** broad polyglot extraction framework with OCR/VLM plugins and code
  intelligence; evaluate each backend and review Elastic License 2.0.

## Local visual-language parsers

- **Docling VLM:** hard visual layouts while retaining Docling structure.
- **olmOCR:** difficult scans, handwriting, equations and complex reading order
  with GPU batch capacity.
- **PaddleOCR-VL:** multilingual and historical documents combining tables,
  formulas and charts in an end-to-end visual path.

These routes require explicit unsupported-content checks. Fluent structured
output is not proof that every emitted token or relationship exists on page.

## Managed document AI

- **LlamaParse:** agentic and chart-focused modes for irregular documents.
- **Mistral OCR:** ordered blocks, tables, images and coordinates with low local
  operational overhead.
- **Azure Document Intelligence:** enterprise layouts and typed invoice, receipt
  or custom-form extraction in Azure environments.
- **Google Document AI Layout Parser:** layout-aware parsing and optional RAG
  chunks in Google Cloud; verify endpoint residency and independently evaluate
  generated chunk boundaries.
- **Amazon Textract:** AWS forms, tables, queries, handwriting and signatures;
  not the default for scientific formulas or chart interpretation.

## Minimum routing policy

Start with PyMuPDF for clean born-digital pages. Escalate to a local structured
pipeline when text coverage, reading-order confidence or detected structure
falls below a calibrated threshold. Use a VLM or managed specialist only for
hard slices it demonstrably improves. Store route, parser version, render
settings, confidence signals and fallback history in parse provenance.
