---
id: source-document-parsing-evidence-2026
type: source
title: Document Parsing Evidence Audit 2025–2026
status: reviewed
privacy: public
confidence: 0.88
created_at: 2026-08-12T18:41:00+02:00
updated_at: 2026-08-12T18:41:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Document Parsing Evidence Audit 2025–2026

Primary sources checked on 2026-08-12:

- [OmniDocBench, CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_OmniDocBench_Benchmarking_Diverse_PDF_Document_Parsing_with_Comprehensive_Annotations_CVPR_2025_paper.html)
- [MPDocBench-Parse, 2026 preprint](https://arxiv.org/abs/2605.22100)
- [Dr. DocBench, 2026 preprint](https://arxiv.org/abs/2606.01393)
- [ParseBench, 2026 preprint and public harness](https://arxiv.org/abs/2604.08538)
- [Docling official repository](https://github.com/docling-project/docling)
- [Docling official releases](https://github.com/docling-project/docling/releases)

## Evidence class

OmniDocBench is E3: peer reviewed at CVPR 2025, with comprehensive annotations
over nine document sources. The three 2026 benchmarks are E2 until peer review
or independent reproduction. Docling documentation and releases establish
capabilities and version changes, not comparative quality, so they are E2 for
mechanism and E1 for superiority.

## Convergent observation

Parser quality is multidimensional. Text fidelity alone misses reading order,
tables, formulas, charts, heading hierarchy, cross-page continuity and visual
grounding. The newer multi-page and expert-domain benchmarks were created
because strong scores on clean or single-page data did not transfer reliably to
harder documents.

## Operational boundary

No source establishes one parser as universally best. Selection must use
representative private slices, record parser/model/version/configuration, and
measure downstream evidence retrieval and citation correctness. Native text
extraction should remain a low-cost baseline; OCR/VLM parsing is justified only
for slices where it improves the declared outcome enough to pay its latency,
cost and privacy burden.

## Failure slices to preserve

- scanned and degraded pages;
- multi-column reading order;
- merged and nested tables;
- formulas, footnotes and captions;
- charts whose values are not present in surrounding text;
- cross-page tables and section hierarchy;
- mixed languages and domain notation;
- malformed files, timeouts and partial conversion.
