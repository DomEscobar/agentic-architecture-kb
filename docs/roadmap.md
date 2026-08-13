# MVP and Roadmap

## Phase 0 — Repository and contracts

- [x] Plan a separate Git repository
- [x] Document the architecture and first ADR
- [x] Define a machine-readable page schema
- [ ] Confirm privacy classes and correction rights with Dom
- [x] Consolidate existing optimizer content into sources and patterns under
  controlled review

## Phase 1 — Deterministic knowledge base

- [x] Markdown parser, schema validator, and link linter
- [x] Stable IDs and source/relation references
- [x] Reproducible compilation to a JSON projection and quality report
- [x] CI for schemas, links, provenance, duplicates, and privacy markers
- [x] Explicit claim ledger with section-level source references
- [x] Claim policy and page coverage audited for every reviewed pattern,
  synthesis, concept, and case (55 claims, 49/49 pages; sentence-level
  completeness remains reviewable)
- Git-based review and rollback process

Exit criterion: every canonical claim is assigned to a source or explicitly to
a decision/hypothesis, and a fresh clone compiles reproducibly.

## Phase 2 — Retrieval

- [x] SQLite FTS5 baseline
- [x] Stable, citable section IDs
- [x] Retrieval traces with filters, candidates, and loaded sections
- [x] Local embedding index with pinned model revision and complete manifest
- [x] RRF fusion with privacy/status/type prefilters, stale-index failure, and
  retrieval traces
- [x] Compare FTS, dense, and RRF on 12 labeled development cases
- [ ] Have relevance labels independently audited by humans and confirm results
  on a protected split before promotion

Exit criterion: baseline evaluations measurably outperform full text alone
without privacy or deletion regressions.

## Phase 3 — Memory promotion

- Extract chat/session content only into the inbox
- Deduplicate, detect conflicts, and maintain a review queue
- Consolidate in the background
- Propagate deletions and corrections with negative tests

Exit criterion: no unreviewed content enters canonical syntheses.

## Evaluation foundation

- [x] Agent-evaluation taxonomy and evidence-first pattern
- [x] Bounded improvement loop with promotion and rollback boundaries
- [x] First project-local development evaluation pack
- [ ] Human-calibrated oracles for the development evaluation pack
- [x] Judge validation set, two-labeler/adjudication schema, and calibration runner
- [ ] Collect real independent labels and frozen judge predictions
- [x] Split and information-flow contract for development, selection, holdout,
  and red-team data
- [x] Untracked private mount, release access ledger, digest checks, and evidence
  validator
- [ ] Add real private selection and holdout cases under domain ownership
- [x] Consulting intake, brownfield audit, and greenfield design
- [x] Workload-specific evaluation blueprints and metric selection
- [x] Statistical, judge, online, tool-selection, and rollout patterns
- [x] Strategy, dataset, audit, and go-live templates
- [x] Consulting coverage suite
- [ ] Three field-validated case records with real outcomes (currently two
  reusable cases, including one public-runtime case with technical outcomes)

## Consumer projection

- [x] Deterministic, privacy-filtered Memory Wiki projection from
  `build/wiki.json`
- [x] Official OpenClaw ingest, canonical synthesis, compilation, and linting
- [x] Digest lock and documented rollback; legacy pages remain historical
- [ ] Rebuild the semantic Memory Core index when the configured embedding
  provider becomes available; local knowledge-base search is functional

## Phase 4 — Scale up after measurement

Postgres/pgvector, reranking, graph projection, and workflow runtimes each
require their own ADR and evaluation-backed decision before adoption.
