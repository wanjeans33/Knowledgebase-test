"""HotpotQA (multi-hop QA) loader.

Uses the `distractor` setting from `hotpotqa/hotpot_qa`. Each example ships 10
context paragraphs (2 gold + 8 distractors) plus supporting-fact titles. We build a
shared corpus from the union of paragraphs (deduped by title) so retrieval must find
the right articles among many; gold support = the supporting-fact titles.
"""
from __future__ import annotations

import re

from ..core.registry import register_dataset
from ..core.types import Document, GoldAnswer, Query
from .base import InMemoryDataset

_HF_ID = "hotpotqa/hotpot_qa"
_CONFIG = "distractor"


def _doc_id(title: str) -> str:
    return "hpqa::" + re.sub(r"\s+", "_", title.strip())


@register_dataset("hotpotqa")
def load_hotpotqa(*, split: str = "validation", trust_remote_code: bool = True, **params) -> InMemoryDataset:
    from datasets import load_dataset  # lazy

    ds = load_dataset(_HF_ID, _CONFIG, split=split, trust_remote_code=trust_remote_code)

    docs: dict[str, Document] = {}
    queries: list[Query] = []
    gold: dict[str, GoldAnswer] = {}

    for ex in ds:
        qid = str(ex["id"])
        titles = ex["context"]["title"]
        sentences = ex["context"]["sentences"]
        for title, sents in zip(titles, sentences):
            did = _doc_id(title)
            if did not in docs:
                docs[did] = Document(doc_id=did, text=" ".join(sents), title=title)

        support_titles = ex["supporting_facts"]["title"]
        support_doc_ids = sorted({_doc_id(t) for t in support_titles})

        queries.append(Query(qid=qid, question=ex["question"],
                             metadata={"type": ex.get("type"), "level": ex.get("level")}))
        gold[qid] = GoldAnswer(answers=[ex["answer"]], supporting_doc_ids=support_doc_ids)

    return InMemoryDataset("hotpotqa", list(docs.values()), queries, gold)
