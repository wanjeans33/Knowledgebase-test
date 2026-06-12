"""Local embedding provider via sentence-transformers (bge-m3 / nomic / bge-small).

The model is loaded lazily on first use so importing this module is cheap and works
without torch installed. `device="auto"` picks cuda when available, else cpu.
"""
from __future__ import annotations


class LocalEmbedding:
    def __init__(self, *, model: str = "BAAI/bge-m3", device: str = "auto",
                 batch_size: int = 32, normalize: bool = True, **extra) -> None:
        self.model_name = model
        self.name = f"local:{model}"
        self._device = device
        self._batch_size = batch_size
        self._normalize = normalize
        self._model = None
        self._dim: int | None = None

    def _ensure(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer  # lazy

            device = self._device
            if device == "auto":
                try:
                    import torch

                    device = "cuda" if torch.cuda.is_available() else "cpu"
                except Exception:
                    device = "cpu"
            self._model = SentenceTransformer(self.model_name, device=device)
            self._dim = int(self._model.get_sentence_embedding_dimension())
        return self._model

    @property
    def dim(self) -> int:
        if self._dim is None:
            self._ensure()
        return self._dim  # type: ignore[return-value]

    def embed(self, texts: list[str]) -> list[list[float]]:
        model = self._ensure()
        vecs = model.encode(
            texts,
            batch_size=self._batch_size,
            normalize_embeddings=self._normalize,
            show_progress_bar=False,
            convert_to_numpy=True,
        )
        return vecs.tolist()
