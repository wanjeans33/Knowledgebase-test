"""Local cross-encoder reranker via sentence-transformers CrossEncoder (bge-reranker).

Loaded lazily on first use. Returns (original_index, score) pairs sorted by descending
relevance, matching the RerankProvider protocol.
"""
from __future__ import annotations


class LocalReranker:
    def __init__(self, *, model: str = "BAAI/bge-reranker-v2-m3", device: str = "auto", **extra) -> None:
        self.model_name = model
        self.name = f"local-rerank:{model}"
        self._device = device
        self._model = None

    def _ensure(self):
        if self._model is None:
            from sentence_transformers import CrossEncoder  # lazy

            device = self._device
            if device == "auto":
                try:
                    import torch

                    device = "cuda" if torch.cuda.is_available() else "cpu"
                except Exception:
                    device = "cpu"
            self._model = CrossEncoder(self.model_name, device=device)
        return self._model

    def rerank(self, query: str, docs: list[str], top_n: int) -> list[tuple[int, float]]:
        if not docs:
            return []
        model = self._ensure()
        scores = model.predict([(query, d) for d in docs])
        ranked = sorted(enumerate(scores), key=lambda x: float(x[1]), reverse=True)
        return [(i, float(s)) for i, s in ranked[:top_n]]
