"""Retrieval-quality metrics over the doc_ids of Answer.retrieved_contexts.

Relevance is binary: a retrieved doc is relevant iff its doc_id is in
GoldAnswer.supporting_doc_ids. Parameterized by cutoff k (recall@k, ndcg@k).
"""
from __future__ import annotations

import math

from ..core.types import Answer, GoldAnswer, Query, RunContext


def _ranked_doc_ids(answer: Answer) -> list[str]:
    seen, ordered = set(), []
    for c in sorted(answer.retrieved_contexts, key=lambda x: x.rank):
        if c.doc_id not in seen:
            seen.add(c.doc_id)
            ordered.append(c.doc_id)
    return ordered


class RecallAtK:
    requires = {"gold_support", "contexts"}

    def __init__(self, k: int = 5) -> None:
        self.k = k
        self.name = f"recall@{k}"

    def score(self, query: Query, answer: Answer, gold: GoldAnswer | None, *, run: RunContext):
        if not gold or not gold.supporting_doc_ids:
            return {}
        relevant = set(gold.supporting_doc_ids)
        retrieved = _ranked_doc_ids(answer)[: self.k]
        hit = len(relevant & set(retrieved))
        return {self.name: hit / len(relevant)}


class NDCGAtK:
    requires = {"gold_support", "contexts"}

    def __init__(self, k: int = 10) -> None:
        self.k = k
        self.name = f"ndcg@{k}"

    def score(self, query: Query, answer: Answer, gold: GoldAnswer | None, *, run: RunContext):
        if not gold or not gold.supporting_doc_ids:
            return {}
        relevant = set(gold.supporting_doc_ids)
        retrieved = _ranked_doc_ids(answer)[: self.k]
        dcg = sum(1.0 / math.log2(i + 2) for i, d in enumerate(retrieved) if d in relevant)
        ideal_n = min(len(relevant), self.k)
        idcg = sum(1.0 / math.log2(i + 2) for i in range(ideal_n))
        return {self.name: (dcg / idcg) if idcg > 0 else 0.0}


class MRR:
    requires = {"gold_support", "contexts"}
    name = "mrr"

    def score(self, query: Query, answer: Answer, gold: GoldAnswer | None, *, run: RunContext):
        if not gold or not gold.supporting_doc_ids:
            return {}
        relevant = set(gold.supporting_doc_ids)
        for i, d in enumerate(_ranked_doc_ids(answer)):
            if d in relevant:
                return {"mrr": 1.0 / (i + 1)}
        return {"mrr": 0.0}
