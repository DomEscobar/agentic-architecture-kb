The canonical technical source is the digest-pinned `llm-wiki` projection, not
the frozen legacy `wiki-sources` pages. It contains the reviewed architecture
knowledge across RAG, runtimes, memory, evaluation and bounded self-improvement,
plus the validated Technique Card catalog.

Use the smallest architecture that passes workload-specific evaluation. Keep
deterministic filters and checks before probabilistic ranking or judging. Treat
memory as governed derived state with provenance, forgetting and privacy. Treat
runtime recovery and side-effect safety as separate concerns. Any optimizer must
use protected evidence, paired comparisons, canaries, kill switches and rollback.

The projection is one-way and may be rebuilt only from a matching canonical
digest. Legacy pages remain historical inputs and must not override newer
canonical claims when they conflict.
