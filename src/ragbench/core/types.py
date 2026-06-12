"""Immutable data types passed across the system / dataset / metric boundaries.

These are deliberately plain (frozen dataclasses) so they are cheap to create,
hashable where useful, and trivially serializable to JSON for predictions.jsonl.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Document:
    """A unit of the corpus to be indexed."""

    doc_id: str
    text: str
    title: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Query:
    """A single evaluation question."""

    qid: str
    question: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GoldAnswer:
    """Ground truth for a query: acceptable answer strings + supporting doc ids."""

    answers: list[str] = field(default_factory=list)
    supporting_doc_ids: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RetrievedContext:
    """One retrieved passage, with its retrieval rank and score."""

    doc_id: str
    text: str
    score: float = 0.0
    rank: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Answer:
    """A system's response to a query.

    `retrieved_contexts` may be empty for closed-book / memory-backed systems.
    `metadata` carries latency, token counts, cost, model id, seed, sub-queries, etc.
    so the stability harness can attribute non-determinism.
    """

    text: str
    retrieved_contexts: list[RetrievedContext] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RunContext:
    """Carried through every index()/query() call: ids, seed, providers, logging, cost.

    Providers/logger are attached at runtime by the pipeline; kept as ``Any`` here to
    avoid import cycles with the provider protocols.
    """

    run_id: str
    seed: int
    output_dir: Path
    providers: Any = None      # ProviderBundle, set by the runner
    logger: Any = None
    cost: dict[str, float] = field(default_factory=dict)

    def add_cost(self, key: str, amount: float) -> None:
        self.cost[key] = self.cost.get(key, 0.0) + amount
