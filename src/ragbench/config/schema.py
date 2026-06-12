"""Pydantic models for an experiment config (one YAML file == one experiment)."""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    backend: str = "deepseek"
    model: str = "deepseek-chat"
    base_url: str | None = None          # for OpenAI-compatible backends (DeepSeek)
    temperature: float = 0.0
    seed: int | None = None
    max_tokens: int = 1024
    extra: dict[str, Any] = Field(default_factory=dict)


class EmbeddingConfig(BaseModel):
    backend: str = "local"
    model: str = "BAAI/bge-m3"
    device: str = "auto"                 # "auto" | "cpu" | "cuda"
    extra: dict[str, Any] = Field(default_factory=dict)


class RerankConfig(BaseModel):
    backend: str = "local"
    model: str = "BAAI/bge-reranker-v2-m3"
    device: str = "auto"
    extra: dict[str, Any] = Field(default_factory=dict)


class ProviderConfig(BaseModel):
    llm: LLMConfig = Field(default_factory=LLMConfig)
    embeddings: EmbeddingConfig | None = Field(default_factory=EmbeddingConfig)
    rerank: RerankConfig | None = None
    cache: bool = True


class SystemConfig(BaseModel):
    name: str
    params: dict[str, Any] = Field(default_factory=dict)

    # Allow inline params: `{name: vanilla, top_k: 5}` collapses extras into `params`.
    model_config = {"extra": "allow"}

    def merged_params(self) -> dict[str, Any]:
        extras = {k: v for k, v in (self.__pydantic_extra__ or {}).items()}
        return {**extras, **self.params}


class DatasetConfig(BaseModel):
    name: str
    split: str = "validation"
    slice: int | None = None
    params: dict[str, Any] = Field(default_factory=dict)

    model_config = {"extra": "allow"}

    def merged_params(self) -> dict[str, Any]:
        extras = {
            k: v
            for k, v in (self.__pydantic_extra__ or {}).items()
            if k not in {"name", "split", "slice", "params"}
        }
        return {**extras, **self.params}


class KnowledgeEditConfig(BaseModel):
    enabled: bool = False
    edits_per_query: int = 1


class StabilityThresholds(BaseModel):
    determinism_min: float = 0.9
    paraphrase_invariance_min: float = 0.8
    contradiction_rate_max: float = 0.05


class StabilityConfig(BaseModel):
    repeats: int = 5
    paraphrases_per_query: int = 0
    contradiction_check: bool = False
    knowledge_edit: KnowledgeEditConfig = Field(default_factory=KnowledgeEditConfig)
    thresholds: StabilityThresholds = Field(default_factory=StabilityThresholds)


class RunConfig(BaseModel):
    repeats: int = 1
    output_dir: str = "runs/"
    concurrency: int = 4


class ExperimentConfig(BaseModel):
    name: str
    seed: int = 0
    provider: ProviderConfig = Field(default_factory=ProviderConfig)
    systems: list[SystemConfig] = Field(default_factory=list)
    datasets: list[DatasetConfig] = Field(default_factory=list)
    metrics: list[str] = Field(default_factory=list)
    run: RunConfig = Field(default_factory=RunConfig)
    stability: StabilityConfig | None = None

    model_config = {"extra": "forbid"}
