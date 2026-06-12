"""Unit tests for the pure consistency metrics (no LLM, exact-match equivalence)."""
from __future__ import annotations

from ragbench.stability import consistency

eq = lambda a, b: a.strip().lower() == b.strip().lower()  # noqa: E731
contra = lambda a, b: {a.lower(), b.lower()} == {"yes", "no"}  # noqa: E731


def test_determinism_all_same():
    assert consistency.determinism_score(["Paris", "Paris", "Paris"], eq) == 1.0


def test_determinism_all_different():
    assert consistency.determinism_score(["a", "b", "c"], eq) == 0.0


def test_determinism_partial():
    # 3 answers, 2 clusters -> 1 - (2-1)/(3-1) = 0.5
    assert consistency.determinism_score(["a", "a", "b"], eq) == 0.5


def test_self_consistency_modal_fraction():
    assert consistency.self_consistency_at_n(["a", "a", "b"], eq) == 2 / 3


def test_cluster_by_equivalence():
    clusters = consistency.cluster_by_equivalence(["a", "b", "a"], eq)
    assert sorted(len(c) for c in clusters) == [1, 2]


def test_paraphrase_invariance():
    assert consistency.paraphrase_invariance(["Paris", "Paris"], eq) == 1.0
    assert consistency.paraphrase_invariance(["Paris", "Lyon"], eq) == 0.0


def test_paraphrase_invariance_single_answer_is_one():
    assert consistency.paraphrase_invariance(["Paris"], eq) == 1.0


def test_contradiction_rate():
    # pairs: (yes,no)=contradict, (yes,yes)=no, (no,no)=no -> among 3 answers yes,no,yes
    # pairs: (yes,no)c (yes,yes)- (no,yes)c => 2/3
    assert consistency.contradiction_rate(["yes", "no", "yes"], contra) == 2 / 3


def test_contradiction_rate_none():
    assert consistency.contradiction_rate(["yes", "yes"], contra) == 0.0
