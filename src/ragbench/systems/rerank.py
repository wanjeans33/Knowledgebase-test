"""Rerank RAG: retrieve a wide top-k with the bi-encoder, then re-rank with a local
cross-encoder and keep the top-n. Falls back to vector order if no reranker is set.
"""
from __future__ import annotations

from ..core.registry import register_system
from ..core.types import RetrievedContext, RunContext
from .base import BaseRAGSystem


@register_system("rerank")
class RerankRAG(BaseRAGSystem):
    name = "rerank"

    def __init__(self, *, top_k_retrieve: int = 20, top_k_final: int = 5, **kwargs) -> None:
        super().__init__(top_k=top_k_final, **kwargs)
        self.top_k_retrieve = top_k_retrieve
        self.top_k_final = top_k_final

    def retrieve(self, question: str, *, run: RunContext, k: int | None = None) -> list[RetrievedContext]:
        candidates = super().retrieve(question, run=run, k=self.top_k_retrieve)
        reranker = getattr(run.providers, "rerank", None)
        if not reranker or not candidates:
            return candidates[: self.top_k_final]
        order = reranker.rerank(question, [c.text for c in candidates], self.top_k_final)
        out = []
        for new_rank, (idx, score) in enumerate(order):
            c = candidates[idx]
            out.append(RetrievedContext(doc_id=c.doc_id, text=c.text, score=float(score),
                                        rank=new_rank, metadata=c.metadata))
        return out
