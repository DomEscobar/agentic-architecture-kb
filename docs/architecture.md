# System Architecture

## Goals and assumptions

The system initially supports one user and one architecture agent, runs locally,
processes mostly Markdown, and should produce traceable technical
recommendations. Correctness, provenance, correction rights, and simple recovery
take priority; extreme scale is not an MVP goal.

## Layers

1. **Run State:** current context and checkpoints; not automatically durable.
2. **Episodic Log:** condensed sessions with decisions, actions, outcomes, and
   open items.
3. **Personal Memory:** stable preferences, projects, and constraints, strictly
   separated by user and privacy class.
4. **Architecture Knowledge Base:** sources, concepts, patterns, cases, and
   syntheses.
5. **Derived Indexes:** full text, embeddings, and relationships; fully
   disposable and reconstructable from Git.

## Write path

```text
Chat/source -> immutable input -> extraction -> inbox
            -> schema and policy checks -> human approval
            -> canonical page -> compile/lint -> derived indexes
```

Automated extraction creates candidates, not truth. Promotion requires a page
type, stable ID, provenance, privacy class, confidence, temporal scope, and
review date. Changes to existing knowledge are modeled as corrections,
additions, or contradictions.

Research papers are discovery inputs, not canonical knowledge units. A durable
addition must close a specific decision gap, add a mechanism or test that is
new to this KB, state its scope and exclusions, and improve retrieval for a
concrete architecture or coding-agent question. Interesting but indirect,
redundant, unactionable, or weakly reproducible findings remain in the research
inbox or source registry.

Every canonical novelty, correction, supersession, or reversion also appends a
dated record to `changes/ledger.jsonl`. The record identifies the affected page,
claim, technique, or governance file and states why the change passed the
utility and evidence gates. Page timestamps and freshness dates remain the
local validity metadata; the change ledger is the cross-cutting audit trail.

## Read path

1. Classify the request and determine scope.
2. Filter deterministically by user, project, privacy, status, and time.
3. Retrieve candidates in parallel through links/IDs, full text, and embeddings.
4. Merge rankings with Reciprocal Rank Fusion.
5. Optionally rerank a small candidate set.
6. Load source sections, generate the answer, and verify claim-to-source links.
7. Record a retrieval trace without unnecessary private content.

Vector search is a recall channel, not the arbiter of truth.

## Local retrieval implementation

Canonical Markdown sections are indexed in SQLite FTS5, weighted 5.0 for
title, 2.0 for heading path, and 1.0 for body text. Every section gets a
stable, citable ID derived from its page ID and heading path.

Strict AND matching over all query tokens runs first. If it returns nothing,
the fallback is restricted to corpus-selective terms — tokens at or below a
document-frequency threshold — rather than a plain OR over every token, so
filler words like "a" or "for" cannot manufacture a match on an unrelated
page. Results report `match_mode` (`strict` or `relaxed`), `term_coverage` per
section, an overall `confidence` (`high`, `medium`, `low`, or `none`), and an
`advisory` string. The `low`/`none` floor is calibrated against the labelled
cases in `evals/wiki-retrieval-v1.json`: every case whose retrieved page was
independently labelled relevant clears the floor, and confidence describes
term-match strength only, never answer correctness.

Dense embeddings and Reciprocal Rank Fusion across lexical and semantic
rankings are opt-in via `make hybrid-index` and are not built by `make
compile`. JSON traces under `reports/retrieval-traces/` record the query,
filters, all ranked candidates, and the full sections that were loaded.

## Data model

Required fields are defined in `schemas/page.schema.json`. Key relationships:

- `supports`, `contradicts`, and `supersedes` for claims, with `claim_kind`
  distinguishing empirical results from normative requirements;
- `applies_to`, `depends_on`, and `evaluated_by` for architecture knowledge;
- `derived_from` for syntheses;
- `reviewed_at`, `valid_from`, and `valid_until` for temporal validity;
- `auditability: private` for sources whose artifacts cannot be retrieved by a
  reader of this repository.

Every deletion removes the canonical page or permitted field, rebuilds all
projections, and then uses a negative test to confirm that the content is no
longer retrievable.

## Failure boundaries and detection

- **Incorrect promotion:** inbox/approval gate and audit log.
- **Stale knowledge:** review date, source freshness, and stale report.
- **Contradictions:** bidirectional claim edges; both endpoints must be
  `contested` or `superseded`.
- **Retrieval leakage:** ACL enforcement before semantic search and tenant
  negative tests.
- **Index drift:** index manifest with model, dimensions, chunker, and hash;
  changes force a complete rebuild.
- **Fabricated provenance:** only existing IDs and sections are citable; answer
  claims are checked against loaded sources.
- **Agentic self-mutation:** no automatic policy, prompt, or skill changes
  without evaluation, review, canary, and rollback.

## Operations

Every build validates JSON Schema, dead links, duplicate IDs, missing sources,
contradictions, dated change records, stale pages, and privacy markers. Git
provides review, diffs, and rollback. Backups must cover the repository and
private raw sources separately; derived indexes need no independent backup.

Telemetry includes query class, filters, candidate IDs, ranks, latency, token
cost, sources used, and user feedback. Prompts or content are recorded only as
allowed by their privacy class.

## Freshness operations

Freshness is split into detection, evidence review, and promotion. The explicit
project registry in `freshness/projects.json` maps GitHub projects to affected
technique cards. `tools/freshness.py repo-pulse` records default-branch heads,
releases, archive state, and license signals without treating activity as
evidence. `freshness/research-query-packs.json` defines the lane-specific
research radar and forbids direct promotion.

Automated runs may write ignored machine reports or `status: inbox` candidates.
They may not rewrite reviewed claims, patterns, syntheses, or technique cards.
Promotion still requires source admission, contradiction review, schema and
retrieval tests, compile/lint, human approval, and a separately approved
consumer release. Security-critical findings may alert immediately and mark a
review as urgent, but do not bypass the evidence gate.
