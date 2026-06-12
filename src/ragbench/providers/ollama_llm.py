"""Optional local generation backend via Ollama. Used when llm.backend == "ollama"."""
from __future__ import annotations

from ..core.provider import LLMMessage, LLMResult


class OllamaLLM:
    def __init__(self, *, model: str = "qwen2.5", temperature: float = 0.0,
                 max_tokens: int = 1024, host: str | None = None, **extra) -> None:
        import ollama  # lazy

        self.model = model
        self.name = f"ollama:{model}"
        self.temperature = temperature
        self.max_tokens = max_tokens
        self._client = ollama.Client(host=host) if host else ollama.Client()

    def generate(self, messages: list[LLMMessage], *, temperature=None, seed=None,
                 max_tokens=None, stop=None) -> LLMResult:
        resp = self._client.chat(
            model=self.model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            options={
                "temperature": self.temperature if temperature is None else temperature,
                "num_predict": self.max_tokens if max_tokens is None else max_tokens,
                "seed": seed,
                "stop": stop,
            },
        )
        return LLMResult(text=resp["message"]["content"], usage={})
