---
id: source-stair-structure-aware-retrieval-2026
type: source
title: STAIR Structure-Aware Retrieval Evidence 2026
status: reviewed
privacy: public
confidence: 0.72
created_at: 2026-09-25T07:15:00+02:00
updated_at: 2026-09-25T07:15:00+02:00
review_at: 2026-11-25
source_ids: []
relations: []
---

# STAIR Structure-Aware Retrieval Evidence 2026

Primary: STAIR (STructure Aware Information Retriever), Kumar et al., IBM,
[arXiv:2609.03874v1](https://arxiv.org/abs/2609.03874v1), submitted 2026-09-03,
retrieved and inspected 2026-09-25 from the HTML version. Author-reported
preprint; no independent reproduction.

## Reported design

- Retrieval unit is a Table of Contents leaf node, not a fixed-length chunk.
- Query plus the complete ToC is the input; one leaf title is generated under
  constrained decoding restricted to valid section titles.
- Base model Mistral-7B-Instruct-v0.2 with LoRA (r=16, alpha=32); maximum input
  14k tokens for STAIR against 512 tokens for DSI; maximum output 64 tokens.
- Training data is synthetic: a Mixtral 8x7B model generates questions per
  paragraph, and the gold label is the section containing that paragraph. Most
  generated questions are used for testing.

## Reported results

- Recall@1: STAIR 82.6, DSI 76.9, DPR 68.7, BM25 59.5, out-of-the-box Mistral
  13.8.
- Error rate: Mistral 86.20 percent, DSI 24.31 percent, STAIR 18.67 percent.
- Non-leaf outputs reported at 0.05 percent for STAIR.
- Randomisation test per domain, reported as significant in all domains.

## Load-bearing finding

The DSI and STAIR arms share base model, training data and task. The only
difference is that structure is supplied in the input. The reported gap widens
for section nodes with the fewest training examples. This is the transferable
part: supplying structure at query time is cheaper than expecting the retriever
to memorise hierarchy.

## Limits

- Unresolved internal inconsistency: the abstract states 18 books across 6
  domains, while the introduction and conclusion state 1818 books across 66
  domains, and the construction text describes selecting three books per domain.
  Do not cite either book or domain count without resolving it against the paper
  tables.
- Synthetic, partly circular evaluation: questions are model-generated from
  paragraphs and the gold label is that paragraph's section. No human-written
  queries, no adversarial distractors, no separation between section-level and
  passage-level metrics.
- The reported low non-leaf rate is substantially a decoding artefact: output is
  constrained to valid leaf titles, so invalid identifiers are near-impossible
  by construction rather than by better knowledge.
- The DPR baseline is not fine-tuned for this task format.
- The system is a parametric index. Knowledge is baked into weights per corpus,
  so incremental update, deletion, ACL propagation, provenance and freshness are
  not addressed.
- Retrieving a section title is coarser than retrieving a passage; downstream
  passage selection and citation binding remain necessary.
- The released artefact link is anonymous; code availability and licence are
  unverified.

## Use in this KB

Supports structure-aware retrieval units and structure supplied at query time.
Compose it as a routing layer above passage retrieval. Cite the ablation
contrast, not the headline percentages.
