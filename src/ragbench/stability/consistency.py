"""Pure consistency metrics over sets of answers.

All functions take an `equivalent` callable (a -> b -> bool) so they can be unit-tested
with exact-match equivalence and run in production with an LLM semantic-equivalence
judge. No I/O here.
"""
from __future__ import annotations

from typing import Callable, Sequence

Equivalent = Callable[[str, str], bool]


def cluster_by_equivalence(answers: Sequence[str], equivalent: Equivalent) -> list[list[int]]:
    """Greedily group answer indices into clusters of mutually-equivalent answers."""
    clusters: list[list[int]] = []
    reps: list[str] = []
    for i, a in enumerate(answers):
        placed = False
        for c, rep in zip(clusters, reps):
            if equivalent(a, rep):
                c.append(i)
                placed = True
                break
        if not placed:
            clusters.append([i])
            reps.append(a)
    return clusters


def determinism_score(answers: Sequence[str], equivalent: Equivalent) -> float:
    """1.0 if all answers cluster together; decreases as distinct clusters appear.

    score = 1 - (num_clusters - 1) / (n - 1), for n > 1. n <= 1 -> 1.0.
    """
    n = len(answers)
    if n <= 1:
        return 1.0
    clusters = cluster_by_equivalence(answers, equivalent)
    return 1.0 - (len(clusters) - 1) / (n - 1)


def self_consistency_at_n(answers: Sequence[str], equivalent: Equivalent) -> float:
    """Fraction of answers that fall in the single largest (modal) cluster."""
    n = len(answers)
    if n == 0:
        return 0.0
    clusters = cluster_by_equivalence(answers, equivalent)
    return max(len(c) for c in clusters) / n


def paraphrase_invariance(answers: Sequence[str], equivalent: Equivalent) -> float:
    """Mean pairwise equivalence across answers to paraphrased questions.

    1.0 means every paraphrase yields an equivalent answer. With < 2 answers -> 1.0.
    """
    n = len(answers)
    if n < 2:
        return 1.0
    agree = 0
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += 1
            if equivalent(answers[i], answers[j]):
                agree += 1
    return agree / total if total else 1.0


def contradiction_rate(answers: Sequence[str], contradicts: Equivalent) -> float:
    """Fraction of answer pairs the `contradicts` judge marks as contradictory."""
    n = len(answers)
    if n < 2:
        return 0.0
    contra = 0
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            total += 1
            if contradicts(answers[i], answers[j]):
                contra += 1
    return contra / total if total else 0.0
