"""Shared scaffolding for vector-retrieval RAG systems.

BaseRAGSystem owns chunking + a pluggable vector index built on the run's
EmbeddingProvider, plus a default generation prompt. Concrete systems override
`retrieve()` and/or `query()`. All heavy imports are local to methods so the module
imports without optional extras installed.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..core.provider import LLMMessage
from ..core.types import Answer, Document, Query, RetrievedContext, RunContext


def simple_chunk(text: str, chunk_size: int, overlap: int) -> list[str]:
    """Whitespace-token chunking with overlap. Dependency-free fallback used when
    LangChain splitters aren't installed (keeps Phase-0/offline paths working)."""
    tokens = text.split()
    if not tokens:
        return []
    if len(tokens) <= chunk_size:
        return [" ".join(tokens)]
    step = max(1, chunk_size - overlap)
    chunks = []
    for start in range(0, len(tokens), step):
        chunk = tokens[start : start + chunk_size]
        if chunk:
            chunks.append(" ".join(chunk))
        if start + chunk_size >= len(tokens):
            break
    return chunks


@dataclass
class _Chunk:
    doc_id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


DEFAULT_SYSTEM_PROMPT = (
    "You are a precise question-answering assistant. Answer the question using ONLY "
    "the provided context. If the context is insufficient, say so briefly. Give the "
    "shortest correct answer (a few words or a short phrase) unless asked otherwise."
)


def build_qa_prompt(question: str, contexts: list[RetrievedContext]) -> list[LLMMessage]:
    ctx_block = "\n\n".join(
        f"[{i + 1}] {c.text}" for i, c in enumerate(contexts)
    ) or "(no context retrieved)"
    user = f"Context:\n{ctx_block}\n\nQuestion: {question}\nAnswer:"
    return [LLMMessage("system", DEFAULT_SYSTEM_PROMPT), LLMMessage("user", user)]


class BaseRAGSystem:
    """Vanilla-style retrieve-then-read base. Concrete systems set `name`."""

    name = "base"

    def __init__(
        self,
        *,
        chunk_size: int = 512,
        chunk_overlap: int = 64,
        top_k: int = 5,
        **kwargs: Any,
    ) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.top_k = top_k
        self.params = kwargs
        self._chunks: list[_Chunk] = []
        self._index = None  # set in index(); a NumpyVectorIndex by default

    # -- indexing -----------------------------------------------------------------
    def _chunk_documents(self, docs: list[Document]) -> list[_Chunk]:
        chunks: list[_Chunk] = []
        for d in docs:
            for piece in simple_chunk(d.text, self.chunk_size, self.chunk_overlap):
                chunks.append(_Chunk(doc_id=d.doc_id, text=piece, metadata=d.metadata))
        return chunks

    def index(self, docs: list[Document], *, run: RunContext) -> None:
        from .vector_index import NumpyVectorIndex

        self._chunks = self._chunk_documents(docs)
        embedder = run.providers.embeddings
        if embedder is None:
            raise RuntimeError(f"{self.name}: an embedding provider is required to index")
        vectors = embedder.embed([c.text for c in self._chunks])
        self._index = NumpyVectorIndex(dim=embedder.dim)
        self._index.add(vectors)

    # -- retrieval ----------------------------------------------------------------
    def retrieve(self, question: str, *, run: RunContext, k: int | None = None) -> list[RetrievedContext]:
        if self._index is None:
            return []
        k = k or self.top_k
        qvec = run.providers.embeddings.embed([question])[0]
        hits = self._index.search(qvec, k)
        out = []
        for rank, (idx, score) in enumerate(hits):
            ch = self._chunks[idx]
            out.append(
                RetrievedContext(
                    doc_id=ch.doc_id, text=ch.text, score=float(score), rank=rank,
                    metadata=ch.metadata,
                )
            )
        return out

    # -- generation ---------------------------------------------------------------
    def generate(self, question: str, contexts: list[RetrievedContext], *, run: RunContext) -> Answer:
        llm = run.providers.llm
        messages = build_qa_prompt(question, contexts)
        result = llm.generate(messages)
        usage = result.usage or {}
        return Answer(
            text=result.text.strip(),
            retrieved_contexts=contexts,
            metadata={
                "system": self.name,
                "model": getattr(llm, "model", getattr(llm, "name", "?")),
                "seed": run.seed,
                "usage": usage,
            },
        )

    def query(self, q: Query, *, run: RunContext) -> Answer:
        contexts = self.retrieve(q.question, run=run)
        return self.generate(q.question, contexts, run=run)

    # -- persistence (optional) ---------------------------------------------------
    def persist(self, path: Path) -> None:  # pragma: no cover - optional
        pass

    def load(self, path: Path) -> None:  # pragma: no cover - optional
        pass


_WS = re.compile(r"\s+")


def normalize_text(s: str) -> str:
    return _WS.sub(" ", s).strip().lower()
