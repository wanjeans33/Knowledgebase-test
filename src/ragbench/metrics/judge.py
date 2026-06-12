"""LLM-as-judge helpers, shared by RAGAS-style metrics and the stability harness.

Judgments are deterministic (temperature 0) and the underlying LLM provider is cached,
so repeated equivalence/contradiction checks over the same pair are free and stable.
"""
from __future__ import annotations

from ..core.provider import LLMMessage


class LLMJudge:
    def __init__(self, llm) -> None:
        self._llm = llm

    def _yes(self, system: str, user: str) -> bool:
        out = self._llm.generate(
            [LLMMessage("system", system), LLMMessage("user", user)],
            temperature=0.0, max_tokens=5,
        ).text.strip().lower()
        return out.startswith("y")

    def equivalent(self, a: str, b: str) -> bool:
        if a.strip().lower() == b.strip().lower():
            return True
        return self._yes(
            "You judge whether two answers convey the same factual claim. "
            "Reply with exactly 'yes' or 'no'.",
            f"Answer A: {a}\nAnswer B: {b}\nDo they assert the same thing?",
        )

    def contradicts(self, a: str, b: str) -> bool:
        return self._yes(
            "You judge whether two answers directly contradict each other. "
            "Reply with exactly 'yes' or 'no'.",
            f"Answer A: {a}\nAnswer B: {b}\nDo they contradict?",
        )
