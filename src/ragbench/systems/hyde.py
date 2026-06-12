"""HyDE / multi-query / RAG-Fusion.

- variant="hyde": generate a hypothetical answer passage, embed IT, retrieve.
- variant="multi_query"/"rag_fusion": generate N query rewrites, retrieve for each,
  fuse the ranked lists with Reciprocal Rank Fusion (RRF).

All generation goes through the run's LLM; retrieval reuses BaseRAGSystem's index.
"""
from __future__ import annotations

from ..core.provider import LLMMessage
from ..core.registry import register_system
from ..core.types import RetrievedContext, RunContext
from .base import BaseRAGSystem


def reciprocal_rank_fusion(ranked_lists: list[list[str]], k: int = 60) -> dict[str, float]:
    """RRF over lists of doc/chunk ids. Returns id -> fused score."""
    scores: dict[str, float] = {}
    for lst in ranked_lists:
        for rank, item in enumerate(lst):
            scores[item] = scores.get(item, 0.0) + 1.0 / (k + rank + 1)
    return scores


@register_system("hyde")
class HydeRAG(BaseRAGSystem):
    name = "hyde"

    def __init__(self, *, variant: str = "hyde", n_queries: int = 4, rrf_k: int = 60, **kwargs) -> None:
        super().__init__(**kwargs)
        self.variant = variant
        self.n_queries = n_queries
        self.rrf_k = rrf_k

    def _hypothetical_doc(self, question: str, run: RunContext) -> str:
        msgs = [
            LLMMessage("system", "Write a short factual passage that would answer the question. "
                                 "Do not say you are unsure; just write the passage."),
            LLMMessage("user", question),
        ]
        return run.providers.llm.generate(msgs, max_tokens=256).text

    def _query_rewrites(self, question: str, run: RunContext) -> list[str]:
        msgs = [
            LLMMessage("system", f"Generate {self.n_queries} diverse search queries that capture "
                                 "different facets of the question. One per line, no numbering."),
            LLMMessage("user", question),
        ]
        text = run.providers.llm.generate(msgs, max_tokens=256).text
        rewrites = [ln.strip("-• ").strip() for ln in text.splitlines() if ln.strip()]
        return rewrites[: self.n_queries] or [question]

    def retrieve(self, question: str, *, run: RunContext, k: int | None = None) -> list[RetrievedContext]:
        k = k or self.top_k
        if self.variant == "hyde":
            probe = self._hypothetical_doc(question, run)
            return super().retrieve(probe, run=run, k=k)

        # multi_query / rag_fusion: retrieve per rewrite, fuse with RRF
        queries = [question, *self._query_rewrites(question, run)]
        per_query: list[list[RetrievedContext]] = [
            super(HydeRAG, self).retrieve(q, run=run, k=max(k, 10)) for q in queries
        ]
        ctx_by_id: dict[str, RetrievedContext] = {}
        ranked_lists: list[list[str]] = []
        for ctxs in per_query:
            ids = []
            for c in ctxs:
                key = f"{c.doc_id}#{hash(c.text) & 0xffff}"
                ctx_by_id.setdefault(key, c)
                ids.append(key)
            ranked_lists.append(ids)
        fused = reciprocal_rank_fusion(ranked_lists, k=self.rrf_k)
        top = sorted(fused.items(), key=lambda x: x[1], reverse=True)[:k]
        out = []
        for rank, (key, score) in enumerate(top):
            c = ctx_by_id[key]
            out.append(RetrievedContext(doc_id=c.doc_id, text=c.text, score=float(score),
                                        rank=rank, metadata=c.metadata))
        return out
