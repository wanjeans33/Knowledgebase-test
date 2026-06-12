"""Probes that generate the inputs the consistency metrics score.

- RepeatProbe: ask the same question N times (determinism under stochastic decoding).
- ParaphraseProbe: generate K meaning-preserving paraphrases (surface-form invariance).
- KnowledgeEditProbe: apply an edit through the KB's `edit()` path, then re-ask
  (ripple-effect / collateral-damage check); only for systems exposing `edit()`.
"""
from __future__ import annotations

from ..core.provider import LLMMessage
from ..core.types import Query, RunContext


def repeat_answers(system, q: Query, *, run: RunContext, repeats: int) -> list[str]:
    return [system.query(q, run=run).text for _ in range(repeats)]


def generate_paraphrases(question: str, *, run: RunContext, n: int) -> list[str]:
    if n <= 0:
        return []
    msgs = [
        LLMMessage("system", f"Rewrite the question in {n} different ways that preserve its "
                             "exact meaning. One per line, no numbering."),
        LLMMessage("user", question),
    ]
    text = run.providers.llm.generate(msgs, max_tokens=256).text
    lines = [ln.strip("-• ").strip() for ln in text.splitlines() if ln.strip()]
    return lines[:n]


def paraphrase_answers(system, q: Query, *, run: RunContext, n: int) -> list[str]:
    """Answer to the original plus each paraphrase."""
    answers = [system.query(q, run=run).text]
    for para in generate_paraphrases(q.question, run=run, n=n):
        answers.append(system.query(Query(qid=q.qid + "~p", question=para), run=run).text)
    return answers


def knowledge_edit_probe(system, q: Query, edit_fact: str, *, run: RunContext) -> dict[str, str]:
    """Answer before and after applying an edit. Requires system.edit()."""
    if not hasattr(system, "edit"):
        return {}
    before = system.query(q, run=run).text
    system.edit(edit_fact, run=run)
    after = system.query(q, run=run).text
    return {"before": before, "after": after}
