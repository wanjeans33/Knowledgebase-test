"""PopQA (entity-centric QA, long-tail popularity) loader: akariasai/PopQA.

PopQA is open-domain with no bundled passages. For a knowledge-base / wiki test we
synthesize one fact document per question (subject–property–object as a sentence) so
the wiki has something to ingest; gold support is that fact. Answers come from
`possible_answers` (a JSON list) plus the object string.
"""
from __future__ import annotations

import ast
import json

from ..core.registry import register_dataset
from ..core.types import Document, GoldAnswer, Query
from .base import InMemoryDataset

_HF_ID = "akariasai/PopQA"


def _parse_answers(raw, obj) -> list[str]:
    answers: list[str] = []
    if isinstance(raw, str):
        for parser in (json.loads, ast.literal_eval):
            try:
                answers = list(parser(raw))
                break
            except Exception:
                continue
    elif isinstance(raw, list):
        answers = list(raw)
    if obj and obj not in answers:
        answers.append(obj)
    return [str(a) for a in answers if a]


@register_dataset("popqa")
def load_popqa(*, split: str = "test", **params) -> InMemoryDataset:
    from datasets import load_dataset  # lazy

    ds = load_dataset(_HF_ID, split=split)

    docs: list[Document] = []
    queries: list[Query] = []
    gold: dict[str, GoldAnswer] = {}

    for ex in ds:
        qid = str(ex["id"])
        subj, prop, obj = ex.get("subj"), ex.get("prop"), ex.get("obj")
        fact = f"{subj} — {prop}: {obj}." if subj and prop and obj else ex["question"]
        did = f"popqa::{qid}"
        docs.append(Document(doc_id=did, text=fact, title=str(subj)))

        answers = _parse_answers(ex.get("possible_answers"), obj)
        queries.append(Query(qid=qid, question=ex["question"],
                             metadata={"prop": prop, "s_pop": ex.get("s_pop")}))
        gold[qid] = GoldAnswer(answers=answers, supporting_doc_ids=[did])

    return InMemoryDataset("popqa", docs, queries, gold)
