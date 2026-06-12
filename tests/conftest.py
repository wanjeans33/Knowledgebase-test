"""Offline test fixtures: fake LLM / embedding providers and a tiny in-memory dataset.

These let the whole pipeline run in seconds with no network and no API key.
"""
from __future__ import annotations

import hashlib
from typing import Iterable

import pytest

from ragbench.core.provider import LLMMessage, LLMResult, ProviderBundle
from ragbench.core.types import Document, GoldAnswer, Query


# --- Fake providers ------------------------------------------------------------------
class FakeEmbeddingProvider:
    """Deterministic bag-of-words hashing embedding. No model download, stable across
    runs, and good enough that lexically-overlapping text scores higher in cosine."""

    name = "fake-embed"

    def __init__(self, dim: int = 64) -> None:
        self._dim = dim

    @property
    def dim(self) -> int:
        return self._dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        vecs = []
        for t in texts:
            v = [0.0] * self._dim
            for tok in t.lower().split():
                h = int(hashlib.md5(tok.encode()).hexdigest(), 16)
                v[h % self._dim] += 1.0
            vecs.append(v)
        return vecs


class FakeLLMProvider:
    """Returns a deterministic answer derived from the prompt: the first words of the
    first context block. Correctness is irrelevant for offline plumbing tests."""

    name = "fake-llm"
    model = "fake-llm"

    def __init__(self, n_words: int = 6) -> None:
        self.n_words = n_words

    def generate(self, messages: list[LLMMessage], *, temperature: float = 0.0,
                 seed: int | None = None, max_tokens: int = 1024,
                 stop: list[str] | None = None) -> LLMResult:
        user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        answer = "unknown"
        if "[1] " in user:
            after = user.split("[1] ", 1)[1]
            answer = " ".join(after.split()[: self.n_words])
        return LLMResult(text=answer, usage={"prompt_tokens": len(user.split()),
                                              "completion_tokens": len(answer.split())})


# --- Fake dataset --------------------------------------------------------------------
class FakeDataset:
    name = "fake"

    def __init__(self) -> None:
        self._docs = [
            Document("d1", "The capital of France is Paris.", title="France"),
            Document("d2", "The capital of Japan is Tokyo.", title="Japan"),
            Document("d3", "Mount Everest is the tallest mountain on Earth.", title="Everest"),
        ]
        self._queries = [
            Query("q1", "What is the capital of France?"),
            Query("q2", "What is the capital of Japan?"),
        ]
        self._gold = {
            "q1": GoldAnswer(answers=["Paris"], supporting_doc_ids=["d1"]),
            "q2": GoldAnswer(answers=["Tokyo"], supporting_doc_ids=["d2"]),
        }

    def corpus(self) -> Iterable[Document]:
        return list(self._docs)

    def queries(self) -> Iterable[Query]:
        return list(self._queries)

    def gold(self, qid: str) -> GoldAnswer:
        return self._gold[qid]

    def slice(self, n: int, *, seed: int) -> "FakeDataset":
        return self


@pytest.fixture
def fake_providers() -> ProviderBundle:
    return ProviderBundle(llm=FakeLLMProvider(), embeddings=FakeEmbeddingProvider())


@pytest.fixture
def fake_dataset() -> FakeDataset:
    return FakeDataset()
