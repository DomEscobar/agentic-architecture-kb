# Agentic Architecture Knowledge Base

A Git-versioned knowledge base of evidence-backed architecture decisions for
RAG, agentic systems, and coding agents. It is opinionated about what it does
not know: patterns state their exclusion conditions and required evidence
instead of handing over a blueprint.

## What is inside

- **RAG and retrieval:** pipeline taxonomy, hybrid search, reranking, context
  assembly.
- **Document parsing and chunking:** parser routing, chunking strategies.
- **Embeddings and multimodal:** model selection, migration, visual retrieval.
- **Agent runtimes and orchestration:** control loops, build-versus-adopt.
- **Agent memory:** write and promotion, forgetting, poisoning defense.
- **Evaluation and observability:** judges, online rollout, statistical rules.
- **Agentic security:** sandboxing, MCP and extension security, red-teaming.
- **Bounded self-improvement:** evidence boundaries, eval-guided loops.
- **Coding-agent project harness:** instructions, skills, and replay evals.

96 pages, 132 technique cards, and 76 sourced claims as of this writing. See
[index.md](index.md) for the full map, including what is deliberately out of
scope.

## Use it

### With a coding agent

```bash
git clone https://github.com/DomEscobar/agentic-architecture-kb.git
```

Point the agent at [AGENTS.md](AGENTS.md) and ask it to search before
recommending, for example:

```text
Use this knowledge base to design recovery semantics for my tool-using agent.
Start with the relevant runtime patterns and technique cards, preserve exact
source references, and state which assumptions require repository inspection.
```

### Locally

```bash
python3 -m pip install -r requirements.txt
make compile
python3 tools/wiki.py search "tool-using agent recovery semantics" --limit 5
```

### Via the public API

For a quick, stateless single-turn lookup that does not inspect your
repository:

```bash
curl --fail-with-body https://ai-architect.huecki.com/api/v1/ask \
  --header 'content-type: application/json' \
  --data '{"question":"Design recovery semantics for a tool-using agent."}'
```

## How it works

Markdown with validated frontmatter is the canonical source; search indexes,
reports, and summaries are reproducible projections that never replace it.
See [ADR-0001](docs/adr/0001-markdown-git-source-of-truth.md) and
[System architecture](docs/architecture.md) for the write path, read path,
and failure boundaries.

## Quality checks

```bash
python3 -m pip install -r requirements.txt
make check
```

Validates schemas, links, provenance, and claims, then compiles and tests.
GitHub Actions runs the same check on every push and pull request. See
[Contributing](docs/contributing.md) for the repository layout, promotion
process, and full command reference.

## Documentation

**Start here:** [Knowledge Map](index.md) · [Agent consumption contract](AGENTS.md)

**Contributing:** [Contributing guide](docs/contributing.md) · [Evidence rubric](docs/evidence-rubric.md) · [MVP and roadmap](docs/roadmap.md)

**Internals:** [System architecture](docs/architecture.md) · [Page schema](schemas/page.schema.json) · [Dated change ledger](changes/ledger.jsonl) · [Memory evaluation](evals/README.md) · [Evaluation Consulting Playbook](docs/evaluation-consulting-playbook.md)
