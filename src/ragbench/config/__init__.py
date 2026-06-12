"""Experiment configuration: Pydantic schema + YAML loader with env interpolation."""
from .schema import ExperimentConfig
from .loader import load_config

__all__ = ["ExperimentConfig", "load_config"]
