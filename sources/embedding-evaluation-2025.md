---
id: source-embedding-evaluation-2025
type: source
title: Multilingual Embedding Evaluation Evidence 2025
status: reviewed
privacy: public
confidence: 0.91
created_at: 2026-08-12T18:41:00+02:00
updated_at: 2026-08-12T18:41:00+02:00
review_at: 2026-11-12
source_ids: []
relations: []
---

# Multilingual Embedding Evaluation Evidence 2025

Primary sources checked on 2026-08-12:

- [MMTEB: Massive Multilingual Text Embedding Benchmark](https://arxiv.org/abs/2502.13595)
- [MTEB official benchmark documentation](https://docs.mteb.org/overview/)

## Evidence class

MMTEB is treated as E3: its public benchmark covers more than 500
quality-controlled tasks across more than 250 languages, including retrieval,
long-document and code tasks. The benchmark is broad and reproducible, but its
aggregate rankings are not application-specific evidence.

## Supported conclusion

Model size and a single leaderboard rank are poor selection rules. MMTEB reports
that a 560M-parameter multilingual E5 variant was the strongest public model in
its evaluated aggregate despite much larger alternatives winning some subsets.
This supports slice-aware evaluation, not adopting that model universally.

## Selection dimensions

- query and corpus languages, including code-switching;
- domain terminology and identifiers;
- query/passsage instruction format;
- passage length and truncation behavior;
- asymmetric query/document encoding;
- dense-only versus hybrid retrieval;
- embedding dimension, index size, throughput and licensing;
- hard negatives and temporal drift.

## Migration boundary

Changing an embedding model changes index identity. It requires a new index
manifest, paired replay, shadow or dual-read validation, migration cost
measurement and rollback. Never compare two embedders while silently changing
chunking, candidate depth or reranking.
