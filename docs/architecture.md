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

## Read path

1. Classify the request and determine scope.
2. Filter deterministically by user, project, privacy, status, and time.
3. Retrieve candidates in parallel through links/IDs, full text, and embeddings.
4. Merge rankings with Reciprocal Rank Fusion.
5. Optionally rerank a small candidate set.
6. Load source sections, generate the answer, and verify claim-to-source links.
7. Record a retrieval trace without unnecessary private content.

Vector search is a recall channel, not the arbiter of truth.

## Data model

Required fields are defined in `schemas/page.schema.json`. Key relationships:

- `supports`, `contradicts`, and `supersedes` for claims;
- `applies_to`, `depends_on`, and `evaluated_by` for architecture knowledge;
- `derived_from` for syntheses;
- `reviewed_at`, `valid_from`, and `valid_until` for temporal validity.

Every deletion removes the canonical page or permitted field, rebuilds all
projections, and then uses a negative test to confirm that the content is no
longer retrievable.

## Failure boundaries and detection

- **Incorrect promotion:** inbox/approval gate and audit log.
- **Stale knowledge:** review date, source freshness, and stale report.
- **Contradictions:** explicit edges and contradiction report.
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
contradictions, stale pages, and privacy markers. Git provides review, diffs, and
rollback. Backups must cover the repository and private raw sources separately;
derived indexes need no independent backup.

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
