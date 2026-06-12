"""RAGAS-based metrics (faithfulness, context precision/recall, answer relevancy).

These need the `ragas` extra and the run's LLM + embeddings. RAGAS evaluates per-sample
given (question, answer, contexts, ground_truth). We adapt our Answer/GoldAnswer into a
single-row evaluation. Heavy imports are local so this module loads without ragas.

NOTE: RAGAS's API surface shifts between versions; verify wiring on a live run and pin
the version in requirements.txt once green.
"""
from __future__ import annotations

from ..core.types import Answer, GoldAnswer, Query, RunContext

_RAGAS_REQUIRES = {
    "faithfulness": {"contexts", "llm_judge"},
    "context_precision": {"contexts", "gold_answer", "llm_judge"},
    "context_recall": {"contexts", "gold_answer", "llm_judge"},
    "answer_relevancy": {"contexts", "llm_judge"},
}


class RagasMetric:
    """Thin per-sample adapter over a single RAGAS metric name."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.requires = _RAGAS_REQUIRES.get(name, {"contexts", "llm_judge"})
        self._metric = None

    def _ensure(self):
        if self._metric is None:
            import ragas.metrics as rm  # lazy; needs [ragas] extra

            mapping = {
                "faithfulness": "faithfulness",
                "context_precision": "context_precision",
                "context_recall": "context_recall",
                "answer_relevancy": "answer_relevancy",
            }
            self._metric = getattr(rm, mapping[self.name])
        return self._metric

    def score(self, query: Query, answer: Answer, gold: GoldAnswer | None, *, run: RunContext):
        from datasets import Dataset as HFDataset  # lazy
        from ragas import evaluate  # lazy

        row = {
            "question": [query.question],
            "answer": [answer.text],
            "contexts": [[c.text for c in answer.retrieved_contexts]],
            "ground_truth": [gold.answers[0] if gold and gold.answers else ""],
        }
        ds = HFDataset.from_dict(row)
        result = evaluate(ds, metrics=[self._ensure()])
        try:
            value = float(result[self.name])
        except Exception:
            df = result.to_pandas()
            value = float(df[self.name].iloc[0])
        return {self.name: value}


def build_ragas_metric(name: str) -> RagasMetric:
    return RagasMetric(name)
