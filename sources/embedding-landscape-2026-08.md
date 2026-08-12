---
id: source-embedding-landscape-2026-08
type: source
title: Embedding Selection and Migration Evidence Audit 2026-08
status: reviewed
privacy: public
confidence: 0.92
created_at: 2026-08-12T22:08:00+02:00
updated_at: 2026-08-12T22:08:00+02:00
review_at: 2026-10-12
source_ids: []
relations: []
---

# Embedding Selection and Migration Evidence Audit 2026-08

## Primary evidence

- [MMTEB, ICLR 2025](https://openreview.net/forum?id=zl3pfz4VCV) evaluates more than 500 tasks and 250 languages. It supports slice-aware shortlisting, not universal adoption from an aggregate rank.
- [M3-Embedding, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.137/) evaluates dense, learned-sparse and multi-vector modes, multilingual and cross-lingual retrieval, and inputs up to 8,192 tokens.
- [ColBERTv2, NAACL 2022](https://aclanthology.org/2022.naacl-main.272/) supports token-level late interaction with compression, trading a larger index and scoring cost for fine-grained matching.
- [SPLADE v2, arXiv record for SIGIR 2021](https://arxiv.org/abs/2109.10086) supports learned lexical expansion with sparse inverted-index retrieval. Public code/model licensing must be checked separately.
- [DADA, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.825/) shows that target-domain distribution feedback can improve generative domain adaptation on BEIR; it does not make synthetic labels trustworthy by default.
- [Matryoshka-Adaptor, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.576/) and [SMEC, EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1332/) support explicitly trained or adapted dimensional truncation. Arbitrary truncation of an incompatible model is unsupported.
- [MIPIC, Findings ACL 2026](https://aclanthology.org/2026.findings-acl.676/) strengthens evidence that cross-dimension consistency is a training property, not a generic post-processing guarantee.
- [A Fresh Take on Stale Embeddings, ICML 2024](https://proceedings.mlr.press/v235/monath24a.html) demonstrates that stale target embeddings matter during retriever training. Production index migration remains an operational architecture question rather than a settled benchmark result.
- [Qdrant collection aliases](https://qdrant.tech/documentation/manage-data/collections/) document atomic alias changes as an implementation mechanism for reversible collection cutover. This is authoritative product documentation, not comparative evidence for the entire migration contract.

## Evidence boundary

Peer-reviewed benchmark and method results are E3. Model cards, provider documentation and the immutable-index/dual-read migration pattern are E2. Public leaderboards are discovery tools. They do not replace a private replay with fixed chunks, candidate depth, filters and reranking.

Long-input support, mixed-document OCR/visual fusion and compact single-vector image retrieval are capabilities or scoped benchmark observations. They remain E2 architecture candidates until length-, modality- and document-specific replay demonstrates end-to-end benefit.

## Selection controls

Always retain BM25 and the incumbent. Evaluate language, code-switching, domain terminology, identifiers, paraphrases, long passages, hard negatives and unanswerable queries separately. Record tokenizer, query/document instructions, normalization, dimension, truncation and model revision as index identity.

## Migration conclusion

Embedding spaces from different revisions are not assumed compatible. Build a new immutable index, verify manifest coverage, shadow or dual-read, run paired replay, rehearse rollback, then switch an alias. Never overwrite the champion vectors in place.
