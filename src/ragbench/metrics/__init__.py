"""Metric construction from config specs like "em", "f1", "recall@5", "ndcg@10", "mrr".

QA metrics register by name; parameterized retrieval metrics are parsed from "@k".
RAGAS metrics (faithfulness, context_precision/recall, answer_relevancy) are added in
Phase 2 and resolved here when the `ragas` extra is installed.
"""
from __future__ import annotations

from . import qa  # noqa: F401  (registers em, f1)
from .retrieval import MRR, NDCGAtK, RecallAtK

_RAGAS_NAMES = {"faithfulness", "context_precision", "context_recall", "answer_relevancy"}


def build_metric(spec: str):
    """Turn a config metric spec into a Metric instance."""
    base, _, suffix = spec.partition("@")
    if base == "recall":
        return RecallAtK(k=int(suffix or 5))
    if base == "ndcg":
        return NDCGAtK(k=int(suffix or 10))
    if base == "mrr":
        return MRR()
    if base in ("em", "f1"):
        from ..core.registry import METRICS

        return METRICS.create(base)
    if base in _RAGAS_NAMES:
        from .ragas_metrics import build_ragas_metric  # added in Phase 2

        return build_ragas_metric(base)
    raise KeyError(f"unknown metric spec '{spec}'")


def build_metrics(specs: list[str]) -> list:
    return [build_metric(s) for s in specs]
