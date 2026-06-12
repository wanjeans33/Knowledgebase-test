"""Axiomatic LLM wiki — PLUGGABLE SLOT (goal c).

This is a documented placeholder for the paper's contribution: a knowledge base
that enforces axioms / consistency constraints on top of ordinary RAG. It satisfies
the AxiomaticKB protocol structurally; every method raises NotImplementedError until
the axiomatic design is finalized. Nothing in phases 1-3 calls these methods.

To implement later, fill in:
  - index()/query()            : the RAGSystem retrieve-then-read path (may subclass BaseRAGSystem)
  - assert_axioms()            : register/learn axioms (coherence, retrieval, update rules)
  - check_consistency()        : detect internal contradictions across stored knowledge
  - constrain()                : filter/repair an answer so it satisfies the axioms
  - explain()                  : produce the derivation (which axioms support the answer)
"""
from __future__ import annotations

from pathlib import Path

from ..core.rag_system import (
    Axiom,
    ConsistencyReport,
    ConstrainedAnswer,
    Derivation,
)
from ..core.registry import register_system
from ..core.types import Answer, Document, Query, RunContext

_NOT_READY = (
    "AxiomaticWiki is a pluggable slot (goal c) and is not implemented yet. "
    "See src/ragbench/systems/axiomatic_slot.py for the contract to fill in."
)


@register_system("axiomatic")
class AxiomaticWiki:
    """Placeholder implementation of the AxiomaticKB protocol."""

    name = "axiomatic"

    def __init__(self, **params: object) -> None:
        self.params = params

    # --- RAGSystem ---------------------------------------------------------------
    def index(self, docs: list[Document], *, run: RunContext) -> None:
        raise NotImplementedError(_NOT_READY)

    def query(self, q: Query, *, run: RunContext) -> Answer:
        raise NotImplementedError(_NOT_READY)

    def persist(self, path: Path) -> None:
        raise NotImplementedError(_NOT_READY)

    def load(self, path: Path) -> None:
        raise NotImplementedError(_NOT_READY)

    # --- AxiomaticKB extras ------------------------------------------------------
    def assert_axioms(self, axioms: list[Axiom], *, run: RunContext) -> None:
        raise NotImplementedError(_NOT_READY)

    def check_consistency(self, *, run: RunContext) -> ConsistencyReport:
        raise NotImplementedError(_NOT_READY)

    def constrain(self, answer: Answer, *, run: RunContext) -> ConstrainedAnswer:
        raise NotImplementedError(_NOT_READY)

    def explain(self, answer: Answer) -> Derivation:
        raise NotImplementedError(_NOT_READY)
