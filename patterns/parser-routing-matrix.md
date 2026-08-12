---
id: pattern-parser-routing-matrix
type: pattern
title: Parser Routing Matrix
status: reviewed
privacy: public
confidence: 0.87
created_at: 2026-08-12T20:20:00+02:00
updated_at: 2026-08-12T20:29:00+02:00
review_at: 2026-10-12
source_ids:
  - source-parser-landscape-2026-08
relations:
  - predicate: derived_from
    target: source-parser-landscape-2026-08
  - predicate: depends_on
    target: pattern-parser-selection-contract
---

# Parser Routing Matrix

## Practical shortlist by workload

- Clean born-digital PDF: PyMuPDF fast path; Docling Standard when hierarchy or
  tables matter.
- Broad mixed file archive: Apache Tika for detection/metadata/text, then route
  difficult PDFs to Docling, MinerU, Marker, PaddleOCR or a managed parser.
- Office-heavy local archive: AnyDoc for fast consistent Markdown; MarkItDown
  when Python plugins or multimodal extensions are useful; Xberg when broad
  bindings, OCR backends or code intelligence justify its larger surface.
- Geometry-sensitive machine-generated PDFs: pdfplumber when characters, ruling
  lines, rectangles and visually debugged table settings are needed.
- Scientific papers with equations: Marker, MinerU, Docling VLM, PaddleOCR-VL or
  olmOCR; evaluate formula and multi-column slices directly.
- Multilingual scans and historical documents: PaddleOCR, MinerU or a managed
  OCR service; validate each script and handwriting slice.
- Forms, invoices and signatures: Azure Document Intelligence, Google Document
  AI or Textract when their typed fields reduce application code; compare with a
  generic layout parser plus deterministic extraction.
- Charts and visually encoded values: LlamaParse agentic/chart modes or a VLM
  parser, with chart datapoint and attribution tests.
- Strict on-premise/privacy: native/local cards only; remote VLM presets and
  managed APIs are ineligible unless a separately approved deployment exists.

## Router signals

Use MIME type, text-layer coverage, scan probability, layout complexity, table/
formula/chart detectors, language, page count, confidentiality and latency tier.
Low-confidence output escalates to the next tier; it is not silently accepted.

## Promotion

The router and each parser version are part of the candidate manifest. Promote
on sliced downstream outcomes, not visual inspection alone. Preserve failed and
fallback routes in traces so coverage gains cannot hide cost or defect shifts.
