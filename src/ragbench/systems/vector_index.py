"""Small vector index abstraction.

NumpyVectorIndex is dependency-light (numpy only) cosine similarity — it always
works, including in offline tests, and is fine at medium scale. A FAISS-backed
index can be swapped in later behind the same .add()/.search() interface.
"""
from __future__ import annotations

import numpy as np


class NumpyVectorIndex:
    def __init__(self, dim: int) -> None:
        self.dim = dim
        self._mat: np.ndarray | None = None

    @staticmethod
    def _normalize(m: np.ndarray) -> np.ndarray:
        norms = np.linalg.norm(m, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return m / norms

    def add(self, vectors: list[list[float]]) -> None:
        m = np.asarray(vectors, dtype=np.float32)
        if m.ndim != 2:
            raise ValueError("vectors must be a 2D list")
        self._mat = self._normalize(m)

    def search(self, query: list[float], k: int) -> list[tuple[int, float]]:
        if self._mat is None or len(self._mat) == 0:
            return []
        q = np.asarray(query, dtype=np.float32).reshape(1, -1)
        q = self._normalize(q)
        sims = (self._mat @ q.T).ravel()
        k = min(k, len(sims))
        top = np.argpartition(-sims, k - 1)[:k]
        top = top[np.argsort(-sims[top])]
        return [(int(i), float(sims[i])) for i in top]
