"""Metric / Evaluator protocols.

`requires` lets the runner skip metrics a dataset/system can't support:
  - "gold_answer"  : needs GoldAnswer.answers
  - "gold_support" : needs GoldAnswer.supporting_doc_ids (retrieval metrics)
  - "contexts"     : needs Answer.retrieved_contexts (RAGAS context metrics)
  - "llm_judge"    : uses an LLM judge (cost/seed implications)
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable

from .types import Answer, GoldAnswer, Query, RunContext


@runtime_checkable
class Metric(Protocol):
    name: str
    requires: set[str]

    def score(
        self,
        query: Query,
        answer: Answer,
        gold: GoldAnswer | None,
        *,
        run: RunContext,
    ) -> dict[str, float]:
        """Return a mapping of metric-component name -> value (usually {self.name: v})."""
        ...


@runtime_checkable
class Evaluator(Protocol):
    def evaluate(self, predictions: list[dict], metrics: list[Metric]) -> object:
        """Compute all applicable metrics over predictions; return a tabular result."""
        ...
