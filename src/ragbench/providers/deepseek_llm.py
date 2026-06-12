"""DeepSeek (and any OpenAI-compatible) chat-completions LLM provider.

DeepSeek exposes an OpenAI-compatible API, so we reuse the `openai` SDK pointed at
DEEPSEEK_BASE_URL. The API key is read from DEEPSEEK_API_KEY (or OPENAI_API_KEY for
the openai backend). Calls are retried with exponential backoff on transient errors.
"""
from __future__ import annotations

import os

from tenacity import retry, stop_after_attempt, wait_exponential

from ..core.provider import LLMMessage, LLMResult

_DEFAULT_BASE_URL = "https://api.deepseek.com"


class OpenAICompatibleLLM:
    def __init__(
        self,
        *,
        backend: str = "deepseek",
        model: str = "deepseek-chat",
        base_url: str | None = None,
        temperature: float = 0.0,
        seed: int | None = None,
        max_tokens: int = 1024,
        api_key: str | None = None,
        **extra,
    ) -> None:
        from openai import OpenAI  # lazy

        self.backend = backend
        self.model = model
        self.name = f"{backend}:{model}"
        self.temperature = temperature
        self.seed = seed
        self.max_tokens = max_tokens
        self.extra = extra

        if backend == "deepseek":
            key = api_key or os.environ.get("DEEPSEEK_API_KEY")
            url = base_url or os.environ.get("DEEPSEEK_BASE_URL") or _DEFAULT_BASE_URL
        else:  # openai
            key = api_key or os.environ.get("OPENAI_API_KEY")
            url = base_url
        if not key:
            raise RuntimeError(
                f"missing API key for backend '{backend}'. Set "
                f"{'DEEPSEEK_API_KEY' if backend == 'deepseek' else 'OPENAI_API_KEY'} in .env"
            )
        self._client = OpenAI(api_key=key, base_url=url)

    @retry(stop=stop_after_attempt(4), wait=wait_exponential(min=1, max=20), reraise=True)
    def generate(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float | None = None,
        seed: int | None = None,
        max_tokens: int | None = None,
        stop: list[str] | None = None,
    ) -> LLMResult:
        resp = self._client.chat.completions.create(
            model=self.model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=self.temperature if temperature is None else temperature,
            seed=self.seed if seed is None else seed,
            max_tokens=self.max_tokens if max_tokens is None else max_tokens,
            stop=stop,
        )
        choice = resp.choices[0]
        usage = {}
        if resp.usage is not None:
            usage = {
                "prompt_tokens": resp.usage.prompt_tokens,
                "completion_tokens": resp.usage.completion_tokens,
            }
        return LLMResult(text=choice.message.content or "", usage=usage, raw=resp)
