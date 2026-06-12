"""MuSiQue (2–4 hop QA) loader.

Each example provides ~20 paragraphs ({title, paragraph_text, is_supporting}) plus the
answer and supporting paragraph flags. We build a shared corpus from the union of
paragraphs (deduped by title) and mark supporting paragraphs as gold support.

The HuggingFace id varies by mirror; override with `hf_id`/`config` if the default
fails. Default targets the answerable MuSiQue mirror.
"""
from __future__ import annotations

import re

from ..core.registry import register_dataset
from ..core.types import Document, GoldAnswer, Query
from .base import InMemoryDataset

_DEFAULT_HF_ID = "dgslibisey/MuSiQue"


def _doc_id(title: str) -> str:
    return "musique::" + re.sub(r"\s+", "_", (title or "untitled").strip())


@register_dataset("musique")
def load_musique(*, split: str = "validation", hf_id: str = _DEFAULT_HF_ID,
                 config: str | None = None, **params) -> InMemoryDataset:
    from datasets import load_dataset  # lazy

    ds = load_dataset(hf_id, config, split=split) if config else load_dataset(hf_id, split=split)

    docs: dict[str, Document] = {}
    queries: list[Query] = []
    gold: dict[str, GoldAnswer] = {}

    for ex in ds:
        qid = str(ex["id"])
        support_ids: list[str] = []
        for para in ex["paragraphs"]:
            title = para.get("title") or ""
            text = para.get("paragraph_text") or para.get("text") or ""
            did = _doc_id(title)
            if did not in docs:
                docs[did] = Document(doc_id=did, text=text, title=title)
            if para.get("is_supporting"):
                support_ids.append(did)

        answers = [ex["answer"], *(ex.get("answer_aliases") or [])]
        queries.append(Query(qid=qid, question=ex["question"]))
        gold[qid] = GoldAnswer(answers=[a for a in answers if a],
                               supporting_doc_ids=sorted(set(support_ids)))

    return InMemoryDataset("musique", list(docs.values()), queries, gold)
