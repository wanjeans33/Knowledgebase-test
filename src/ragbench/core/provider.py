"""Provider protocols: the thin abstraction over LLM generation, embeddings, rerank.

Default implementations (see ragbench.providers):
  - LLM:        DeepSeek via the OpenAI-compatible client.
  - Embeddings: local sentence-transformers (bge-m3 / nomic).
  - Rerank:     local CrossEncoder (bge-reranker).

Keeping these as Protocols means alternative backends (OpenAI embeddings, Ollama
generation, Cohere rerank) drop in without changing any caller.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable


@dataclass(frozen=True)
class LLMMessage:
    role: str   # "system" | "user" | "assistant"
    content: str


@dataclass
class LLMResult:
    text: str
    usage: dict[str, int] = field(default_factory=dict)   # prompt_tokens, completion_tokens
    raw: Any = None


@runtime_checkable
class LLMProvider(Protocol):
    name: str

    def generate(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.0,
        seed: int | None = None,
        max_tokens: int = 1024,
        stop: list[str] | None = None,
    ) -> LLMResult: ...


@runtime_checkable
class EmbeddingProvider(Protocol):
    name: str

    def embed(self, texts: list[str]) -> list[list[float]]: ...

    @property
    def dim(self) -> int: ...


@runtime_checkable
class RerankProvider(Protocol):
    name: str

    def rerank(self, query: str, docs: list[str], top_n: int) -> list[tuple[int, float]]:
        """Return [(original_index, score), ...] sorted by descending relevance."""
        ...


@dataclass
class ProviderBundle:
    """The set of providers a run uses, attached to RunContext."""

    llm: LLMProvider
    embeddings: EmbeddingProvider | None = None
    rerank: RerankProvider | None = None
