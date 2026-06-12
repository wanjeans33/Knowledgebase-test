"""Memory-backed "LLM wiki" adapter (goal b).

Wraps an agent-memory library (default: mem0) behind the RAGSystem protocol so the
same runner + stability harness can probe it. index() writes the corpus into memory;
query() searches memory for context, then generates with the run's DeepSeek LLM.

This adapter has an `edit()` hook the stability harness uses for ripple-effect probes.

NOTE: needs the `memory` extra (`pip install -e .[memory]`) and live verification —
mem0's config surface changes across versions; adjust `_build_memory` as needed.
"""
from __future__ import annotations

from pathlib import Path

from ..core.registry import register_system
from ..core.types import Answer, Document, Query, RetrievedContext, RunContext
from .base import build_qa_prompt


@register_system("memory_wiki")
class MemoryWiki:
    name = "memory_wiki"

    def __init__(self, *, backend: str = "mem0", top_k: int = 5, user_id: str = "ragbench",
                 **params) -> None:
        self.backend = backend
        self.top_k = top_k
        self.user_id = user_id
        self.params = params
        self._mem = None

    def _build_memory(self):
        if self._mem is not None:
            return self._mem
        if self.backend == "mem0":
            from mem0 import Memory  # lazy; needs [memory] extra

            # Default mem0 config; point its LLM at DeepSeek and embedder at a local model
            # via env/config in a real run. Kept minimal here.
            self._mem = Memory()
        else:
            raise ValueError(f"unknown memory backend '{self.backend}'")
        return self._mem

    def index(self, docs: list[Document], *, run: RunContext) -> None:
        mem = self._build_memory()
        for d in docs:
            mem.add(d.text, user_id=self.user_id, metadata={"doc_id": d.doc_id,
                                                            "title": d.title})

    def _search(self, question: str) -> list[RetrievedContext]:
        mem = self._build_memory()
        hits = mem.search(question, user_id=self.user_id, limit=self.top_k)
        results = hits.get("results", hits) if isinstance(hits, dict) else hits
        ctxs = []
        for rank, h in enumerate(results or []):
            text = h.get("memory") or h.get("text") or ""
            meta = h.get("metadata") or {}
            ctxs.append(RetrievedContext(doc_id=meta.get("doc_id", f"mem{rank}"),
                                         text=text, score=float(h.get("score", 0.0)),
                                         rank=rank, metadata=meta))
        return ctxs

    def query(self, q: Query, *, run: RunContext) -> Answer:
        contexts = self._search(q.question)
        result = run.providers.llm.generate(build_qa_prompt(q.question, contexts))
        return Answer(text=result.text.strip(), retrieved_contexts=contexts,
                      metadata={"system": self.name, "seed": run.seed, "usage": result.usage})

    def edit(self, fact: str, *, run: RunContext) -> None:
        """Apply a knowledge edit (used by the stability ripple-effect probe)."""
        self._build_memory().add(fact, user_id=self.user_id, metadata={"edit": True})

    def persist(self, path: Path) -> None:  # pragma: no cover
        pass

    def load(self, path: Path) -> None:  # pragma: no cover
        pass
