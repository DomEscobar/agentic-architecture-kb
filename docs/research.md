# Deep Research: Architecture and Tools

Status: 2026-08-08. Official documentation, repositories, and research papers
were preferred. Vendor claims count as implementation evidence, not independent
quality evidence.

## Findings

### Memory needs separate scopes and write timings

LangGraph documentation separates thread state from cross-session memory and
distinguishes semantic, episodic, and procedural memory. It also describes
hot-path and asynchronous writes with different latency and freshness
properties. This supports separate stores and an asynchronous, auditable
promotion path.

Source: https://docs.langchain.com/oss/python/concepts/memory

### The index must not be the truth layer

SQLite FTS5 provides local full-text search and BM25 without another service.
For the MVP, this is sufficient together with a reproducible embedding index.

Source: https://www.sqlite.org/fts5.html

pgvector supports exact and approximate vector search as well as hybrid search
with PostgreSQL full-text search. Its documentation also notes that ANN trades
recall for speed and that filtered ANN queries may return fewer results.
Postgres is therefore a scale-up option, not a required MVP component.

Source: https://github.com/pgvector/pgvector

### Evaluation must measure more than fact recall

MemoryAgentBench separates accurate retrieval, test-time learning, long-range
understanding, and selective forgetting. The broader agent-evaluation survey
also calls for more realistic, continuously updated tests of robustness,
security, and cost efficiency.

Sources:

- https://arxiv.org/abs/2507.05257
- https://arxiv.org/abs/2503.16416

### Checkpoints are runtime state, not knowledge-base content

LangGraph's persistence model stores state incrementally and enables resume,
human-in-the-loop, and time-travel debugging. This is useful for the runtime but
must not be mixed with reviewed knowledge claims.

Source: https://docs.langchain.com/oss/python/langgraph/persistence

## Tool decisions

### Recommended for the MVP

- **Git + Markdown:** canonical, diffable source and rollback.
- **Obsidian:** optional human interface for links and properties; not a runtime
  dependency.
- **JSON Schema + custom linter:** deterministic structure and policy checks.
- **SQLite FTS5:** local lexical index.
- **Embeddings + simple local vector store:** semantic recall; model and chunker
  versions are mandatory in the manifest.
- **Reciprocal Rank Fusion:** transparent fusion of full-text and vector results.
- **pytest/fixtures:** reproducible retrieval, update, privacy, and forgetting
  evaluations.
- **OpenTelemetry:** traces and metrics with redacted content; evolving GenAI
  conventions must be versioned.

Source: https://opentelemetry.io/docs/specs/semconv/

### Later, only when measurement justifies it

- **Postgres + pgvector:** multiple writers, ACL queries, high document counts,
  or a central service.
- **Cross-encoder reranker:** when offline evaluations show a meaningful
  precision gain within the latency budget.
- **Property graph:** only when multi-hop questions fail in the evaluation suite;
  initially project relationships from Markdown metadata.
- **LangGraph or a comparable runtime:** when long-running workflows,
  checkpoints, and recovery are genuinely needed. The knowledge base itself
  remains runtime-independent.

### Not recommended for the MVP

- autonomous promotion of chat content;
- a proprietary vector store as the only copy;
- automatic skill or prompt rewrites based on isolated successes;
- introducing a knowledge graph, vector database, and agent framework at once.
