"""Provider construction from config.

build_providers() turns a validated ProviderConfig into a ProviderBundle, wrapping
the LLM and embedding providers in an on-disk cache when `cache: true`. Concrete
backends import their heavy deps lazily so this module imports without torch/openai.
"""
from __future__ import annotations

from pathlib import Path

from ..config.schema import ProviderConfig
from ..core.provider import ProviderBundle


def build_providers(cfg: ProviderConfig, *, cache_dir: Path | None = None) -> ProviderBundle:
    llm = _build_llm(cfg.llm)
    embeddings = _build_embeddings(cfg.embeddings) if cfg.embeddings else None
    rerank = _build_rerank(cfg.rerank) if cfg.rerank else None

    if cfg.cache:
        from .cache import CachedEmbedding, CachedLLM, open_cache

        cache = open_cache(cache_dir)
        llm = CachedLLM(llm, cache)
        if embeddings is not None:
            embeddings = CachedEmbedding(embeddings, cache)

    return ProviderBundle(llm=llm, embeddings=embeddings, rerank=rerank)


def _build_llm(cfg):
    if cfg.backend in ("deepseek", "openai"):
        from .deepseek_llm import OpenAICompatibleLLM

        return OpenAICompatibleLLM(
            backend=cfg.backend,
            model=cfg.model,
            base_url=cfg.base_url,
            temperature=cfg.temperature,
            seed=cfg.seed,
            max_tokens=cfg.max_tokens,
            **cfg.extra,
        )
    if cfg.backend == "ollama":
        from .ollama_llm import OllamaLLM

        return OllamaLLM(model=cfg.model, temperature=cfg.temperature,
                         max_tokens=cfg.max_tokens, **cfg.extra)
    raise ValueError(f"unknown llm backend '{cfg.backend}'")


def _build_embeddings(cfg):
    if cfg.backend == "local":
        from .local_embed import LocalEmbedding

        return LocalEmbedding(model=cfg.model, device=cfg.device, **cfg.extra)
    if cfg.backend == "openai":
        from .openai_embed import OpenAIEmbedding

        return OpenAIEmbedding(model=cfg.model, **cfg.extra)
    raise ValueError(f"unknown embedding backend '{cfg.backend}'")


def _build_rerank(cfg):
    if cfg.backend == "local":
        from .local_rerank import LocalReranker

        return LocalReranker(model=cfg.model, device=cfg.device, **cfg.extra)
    raise ValueError(f"unknown rerank backend '{cfg.backend}'")
