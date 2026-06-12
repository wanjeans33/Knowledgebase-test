"""Stability / consistency harness for LLM wikis (goal b).

Probes a system's answers for determinism, paraphrase invariance, cross-answer
contradiction, and knowledge-edit ripple effects. The consistency math is pure and
unit-tested; the probes use the run's LLM for paraphrasing and equivalence judging.
"""
from .consistency import (
    cluster_by_equivalence,
    contradiction_rate,
    determinism_score,
    paraphrase_invariance,
    self_consistency_at_n,
)

__all__ = [
    "cluster_by_equivalence",
    "determinism_score",
    "self_consistency_at_n",
    "paraphrase_invariance",
    "contradiction_rate",
]
