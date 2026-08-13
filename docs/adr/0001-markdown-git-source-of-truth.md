# ADR-0001: Markdown and Git as the Source of Truth

- Status: accepted
- Date: 2026-08-08

## Context

The knowledge base must be human-readable, locally operable, auditable,
correctable, and independent of embedding models or database products.

## Decision

Canonical content is stored in Git as Markdown with validated YAML frontmatter.
Full-text, vector, and graph indexes are derived artifacts.

## Consequences

Positive: simple reviews, diffs, backups, and rollbacks; no lock-in; a broken or
stale index can be rebuilt completely.

Negative: concurrent writers and very large corpora may eventually require a
transaction layer; schema changes require migrations; field-level access control
is limited in a filesystem.

## Alternatives

- Postgres is preferable for many concurrent writers and complex ACL queries.
- A property graph is preferable for frequent, evaluated multi-hop queries.
- A SaaS vector store is preferable only when reduced operational burden matters
  more than local control and portability.
