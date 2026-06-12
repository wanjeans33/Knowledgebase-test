"""Dataset protocol: a benchmark exposes a corpus, queries, and gold answers."""
from __future__ import annotations

from typing import Iterable, Protocol, runtime_checkable

from .types import Document, GoldAnswer, Query


@runtime_checkable
class Dataset(Protocol):
    name: str

    def corpus(self) -> Iterable[Document]:
        """Documents to index. For closed-corpus QA this is the passage pool."""
        ...

    def queries(self) -> Iterable[Query]:
        """Evaluation questions."""
        ...

    def gold(self, qid: str) -> GoldAnswer:
        """Ground truth for a query id."""
        ...

    def slice(self, n: int, *, seed: int) -> "Dataset":
        """A reproducible subset of `n` queries (and the docs they need)."""
        ...
