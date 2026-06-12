"""Optional cloud embedding backend: OpenAI text-embedding-3-*.

Only used when provider.embeddings.backend == "openai". Reads OPENAI_API_KEY.
"""
from __future__ import annotations

import os

from tenacity import retry, stop_after_attempt, wait_exponential

_DIMS = {"text-embedding-3-small": 1536, "text-embedding-3-large": 3072}


class OpenAIEmbedding:
    def __init__(self, *, model: str = "text-embedding-3-large", api_key: str | None = None, **extra) -> None:
        from openai import OpenAI  # lazy

        self.model = model
        self.name = f"openai:{model}"
        key = api_key or os.environ.get("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("missing OPENAI_API_KEY for openai embedding backend")
        self._client = OpenAI(api_key=key)
        self._dim = _DIMS.get(model)

    @property
    def dim(self) -> int:
        if self._dim is None:
            self._dim = len(self.embed(["dimension probe"])[0])
        return self._dim

    @retry(stop=stop_after_attempt(4), wait=wait_exponential(min=1, max=20), reraise=True)
    def embed(self, texts: list[str]) -> list[list[float]]:
        resp = self._client.embeddings.create(model=self.model, input=texts)
        return [d.embedding for d in resp.data]
