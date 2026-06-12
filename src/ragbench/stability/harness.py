"""Orchestrates the stability probes for one system over a query set and produces a
per-query StabilityRecord (determinism, paraphrase invariance, contradiction rate).

Writes stability.parquet; the markdown report aggregates it and flags threshold misses.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..config.schema import StabilityConfig
from ..core.types import Query, RunContext
from ..metrics.judge import LLMJudge
from . import consistency
from .probes import paraphrase_answers, repeat_answers


@dataclass
class StabilityRecord:
    system: str
    qid: str
    determinism: float = 1.0
    self_consistency: float = 1.0
    paraphrase_invariance: float = 1.0
    contradiction_rate: float = 0.0
    n_answers: int = 0
    extra: dict[str, Any] = field(default_factory=dict)


def run_stability(system, queries: list[Query], *, run: RunContext,
                  cfg: StabilityConfig) -> list[StabilityRecord]:
    judge = LLMJudge(run.providers.llm)
    records: list[StabilityRecord] = []

    for q in queries:
        repeats = repeat_answers(system, q, run=run, repeats=cfg.repeats)
        rec = StabilityRecord(system=getattr(system, "name", "?"), qid=q.qid,
                              n_answers=len(repeats))
        rec.determinism = consistency.determinism_score(repeats, judge.equivalent)
        rec.self_consistency = consistency.self_consistency_at_n(repeats, judge.equivalent)

        pool = list(repeats)
        if cfg.paraphrases_per_query > 0:
            para = paraphrase_answers(system, q, run=run, n=cfg.paraphrases_per_query)
            rec.paraphrase_invariance = consistency.paraphrase_invariance(para, judge.equivalent)
            pool += para

        if cfg.contradiction_check:
            rec.contradiction_rate = consistency.contradiction_rate(pool, judge.contradicts)

        records.append(rec)

    return records


def stability_records_to_rows(records: list[StabilityRecord]) -> list[dict]:
    return [
        {
            "system": r.system,
            "qid": r.qid,
            "determinism": r.determinism,
            "self_consistency": r.self_consistency,
            "paraphrase_invariance": r.paraphrase_invariance,
            "contradiction_rate": r.contradiction_rate,
            "n_answers": r.n_answers,
        }
        for r in records
    ]
