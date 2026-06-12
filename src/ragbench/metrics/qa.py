"""Answer-correctness metrics: Exact Match and token-F1 (SQuAD/HotpotQA style)."""
from __future__ import annotations

import re
import string
from collections import Counter

from ..core.registry import register_metric
from ..core.types import Answer, GoldAnswer, Query, RunContext

_ARTICLES = re.compile(r"\b(a|an|the)\b")
_PUNCT_TABLE = str.maketrans("", "", string.punctuation)


def normalize_answer(s: str) -> str:
    """Lowercase, remove punctuation/articles, collapse whitespace (SQuAD normalization)."""
    s = s.lower()
    s = s.translate(_PUNCT_TABLE)
    s = _ARTICLES.sub(" ", s)
    return " ".join(s.split())


def _em(pred: str, golds: list[str]) -> float:
    p = normalize_answer(pred)
    return 1.0 if any(p == normalize_answer(g) for g in golds) else 0.0


def _f1(pred: str, golds: list[str]) -> float:
    best = 0.0
    p_tokens = normalize_answer(pred).split()
    for g in golds:
        g_tokens = normalize_answer(g).split()
        if not p_tokens or not g_tokens:
            best = max(best, 1.0 if p_tokens == g_tokens else 0.0)
            continue
        common = Counter(p_tokens) & Counter(g_tokens)
        num_same = sum(common.values())
        if num_same == 0:
            continue
        precision = num_same / len(p_tokens)
        recall = num_same / len(g_tokens)
        best = max(best, 2 * precision * recall / (precision + recall))
    return best


@register_metric("em")
class ExactMatch:
    name = "em"
    requires = {"gold_answer"}

    def score(self, query: Query, answer: Answer, gold: GoldAnswer | None, *, run: RunContext):
        if not gold or not gold.answers:
            return {}
        return {"em": _em(answer.text, gold.answers)}


@register_metric("f1")
class TokenF1:
    name = "f1"
    requires = {"gold_answer"}

    def score(self, query: Query, answer: Answer, gold: GoldAnswer | None, *, run: RunContext):
        if not gold or not gold.answers:
            return {}
        return {"f1": _f1(answer.text, gold.answers)}
