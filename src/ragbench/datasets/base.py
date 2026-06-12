"""Shared dataset machinery: an in-memory dataset with reproducible slicing.

Concrete loaders (hotpotqa, musique, ...) download from HuggingFace, normalize into
Documents + Queries + GoldAnswers, and return an InMemoryDataset. Slicing selects a
deterministic subset of queries and prunes the corpus to documents those queries need
(plus, when relevant, the full pool so retrieval still has distractors).
"""
from __future__ import annotations

import random
from typing import Iterable

from ..core.types import Document, GoldAnswer, Query


class InMemoryDataset:
    def __init__(
        self,
        name: str,
        docs: list[Document],
        queries: list[Query],
        gold: dict[str, GoldAnswer],
    ) -> None:
        self.name = name
        self._docs = docs
        self._queries = queries
        self._gold = gold

    def corpus(self) -> Iterable[Document]:
        return list(self._docs)

    def queries(self) -> Iterable[Query]:
        return list(self._queries)

    def gold(self, qid: str) -> GoldAnswer:
        return self._gold[qid]

    def slice(self, n: int, *, seed: int) -> "InMemoryDataset":
        if n >= len(self._queries):
            return self
        rng = random.Random(seed)
        chosen = rng.sample(self._queries, n)
        chosen_ids = {q.qid for q in chosen}
        gold = {qid: self._gold[qid] for qid in chosen_ids if qid in self._gold}

        # Keep gold-supporting docs, then top up with other docs as distractors so
        # retrieval difficulty is preserved (cap total to keep indexing fast).
        needed_doc_ids = {
            did for g in gold.values() for did in g.supporting_doc_ids
        }
        by_id = {d.doc_id: d for d in self._docs}
        kept = [by_id[d] for d in needed_doc_ids if d in by_id]
        kept_ids = set(needed_doc_ids)
        extra_cap = max(200, n * 10)
        for d in self._docs:
            if len(kept) >= extra_cap:
                break
            if d.doc_id not in kept_ids:
                kept.append(d)
                kept_ids.add(d.doc_id)
        return InMemoryDataset(self.name, kept, chosen, gold)
