"""The central contract: every system under test implements RAGSystem.

vanilla RAG, each variant, memory-backed wikis, and the future axiomatic wiki all
satisfy RAGSystem, so the runner / evaluator / stability harness never special-case
a system. AxiomaticKB extends it with the extra hooks the paper will exercise.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from .types import Answer, Document, Query, RunContext


@runtime_checkable
class RAGSystem(Protocol):
    name: str

    def index(self, docs: list[Document], *, run: RunContext) -> None:
        """Build whatever internal index/memory the system needs from the corpus."""
        ...

    def query(self, q: Query, *, run: RunContext) -> Answer:
        """Answer a query. MUST populate Answer.retrieved_contexts (may be empty)
        and SHOULD record seed/temperature in Answer.metadata."""
        ...

    def persist(self, path: Path) -> None:
        """Persist index/state to disk (no-op allowed)."""
        ...

    def load(self, path: Path) -> None:
        """Load previously persisted state (no-op allowed)."""
        ...


# --- Axiomatic pluggable slot (goal c) -------------------------------------------------
# These types are placeholders the paper work will flesh out. Phase 1 never calls them.


@dataclass(frozen=True)
class Axiom:
    """A constraint the knowledge base should satisfy (form TBD by the research)."""

    aid: str
    statement: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ConsistencyReport:
    consistent: bool
    violations: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class ConstrainedAnswer:
    answer: Answer
    enforced_axioms: list[str] = field(default_factory=list)


@dataclass
class Derivation:
    """Which axioms / facts support a given answer (for explainability)."""

    supporting_axioms: list[str] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)


@runtime_checkable
class AxiomaticKB(RAGSystem, Protocol):
    """A knowledge base that exposes axiom assertion, consistency checking,
    answer-constraining, and derivation/explanation on top of RAGSystem."""

    def assert_axioms(self, axioms: list[Axiom], *, run: RunContext) -> None: ...

    def check_consistency(self, *, run: RunContext) -> ConsistencyReport: ...

    def constrain(self, answer: Answer, *, run: RunContext) -> ConstrainedAnswer: ...

    def explain(self, answer: Answer) -> Derivation: ...
