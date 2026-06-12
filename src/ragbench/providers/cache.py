"""On-disk caching wrappers for LLM and embedding providers.

Keyed by a stable hash of (model, params, content). Cuts API cost and makes re-runs
deterministic. Disabled for stability experiments that need real repeated calls.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ..core.provider import LLMMessage, LLMResult

_DEFAULT_DIR = Path(".cache") / "providers"


def open_cache(cache_dir: Path | None = None):
    from diskcache import Cache  # lazy

    d = cache_dir or _DEFAULT_DIR
    d.mkdir(parents=True, exist_ok=True)
    return Cache(str(d))


def _hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()


class CachedLLM:
    def __init__(self, inner, cache) -> None:
        self._inner = inner
        self._cache = cache
        self.name = getattr(inner, "name", "llm")
        self.model = getattr(inner, "model", self.name)

    def generate(self, messages: list[LLMMessage], *, temperature=None, seed=None,
                 max_tokens=None, stop=None) -> LLMResult:
        key = _hash({
            "kind": "llm", "model": self.model,
            "messages": [(m.role, m.content) for m in messages],
            "temperature": temperature, "seed": seed,
            "max_tokens": max_tokens, "stop": stop,
        })
        hit = self._cache.get(key)
        if hit is not None:
            return LLMResult(text=hit["text"], usage=hit.get("usage", {}), raw=None)
        res = self._inner.generate(messages, temperature=temperature, seed=seed,
                                   max_tokens=max_tokens, stop=stop)
        self._cache.set(key, {"text": res.text, "usage": res.usage})
        return res


class CachedEmbedding:
    def __init__(self, inner, cache) -> None:
        self._inner = inner
        self._cache = cache
        self.name = getattr(inner, "name", "embed")

    @property
    def dim(self) -> int:
        return self._inner.dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        out: list[list[float] | None] = [None] * len(texts)
        missing_idx: list[int] = []
        missing_txt: list[str] = []
        for i, t in enumerate(texts):
            key = _hash({"kind": "embed", "model": self.name, "text": t})
            hit = self._cache.get(key)
            if hit is not None:
                out[i] = hit
            else:
                missing_idx.append(i)
                missing_txt.append(t)
        if missing_txt:
            fresh = self._inner.embed(missing_txt)
            for j, i in enumerate(missing_idx):
                out[i] = fresh[j]
                key = _hash({"kind": "embed", "model": self.name, "text": texts[i]})
                self._cache.set(key, fresh[j])
        return [v for v in out]  # type: ignore[return-value]
