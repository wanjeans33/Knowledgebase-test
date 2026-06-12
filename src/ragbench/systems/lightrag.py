"""LightRAG (graph RAG) adapter.

Wraps HKUDS/LightRAG behind the RAGSystem protocol: index() inserts the corpus and
builds the entity/relation graph; query() runs LightRAG's hybrid retrieval+generation.

NOTE: needs the `graph` extra (`pip install -e .[graph]`) and live verification.
LightRAG manages its own LLM/embedding callables — wire them to DeepSeek + local bge
in `_build` for a real run. Imports are lazy so registration works without the extra.
"""
from __future__ import annotations

from pathlib import Path

from ..core.registry import register_system
from ..core.types import Answer, Document, Query, RunContext


@register_system("lightrag")
class LightRAGSystem:
    name = "lightrag"

    def __init__(self, *, top_k: int = 5, working_dir: str = "data/indexes/lightrag",
                 mode: str = "hybrid", **params) -> None:
        self.top_k = top_k
        self.working_dir = working_dir
        self.mode = mode
        self.params = params
        self._rag = None

    def _build(self, run: RunContext):
        if self._rag is not None:
            return self._rag
        from lightrag import LightRAG  # lazy; needs [graph] extra

        Path(self.working_dir).mkdir(parents=True, exist_ok=True)
        # In a real run, pass llm_model_func / embedding_func that call the run's
        # DeepSeek LLM and local bge embedder. Left to live wiring.
        self._rag = LightRAG(working_dir=self.working_dir)
        return self._rag

    def index(self, docs: list[Document], *, run: RunContext) -> None:
        rag = self._build(run)
        rag.insert([d.text for d in docs])

    def query(self, q: Query, *, run: RunContext) -> Answer:
        from lightrag import QueryParam  # lazy

        rag = self._build(run)
        text = rag.query(q.question, param=QueryParam(mode=self.mode, top_k=self.top_k))
        # LightRAG returns a generated answer; it does not expose ranked contexts the
        # same way, so retrieved_contexts is left empty (retrieval metrics N/A here).
        return Answer(text=str(text).strip(), retrieved_contexts=[],
                      metadata={"system": self.name, "mode": self.mode, "seed": run.seed})

    def persist(self, path: Path) -> None:  # pragma: no cover
        pass

    def load(self, path: Path) -> None:  # pragma: no cover
        pass
