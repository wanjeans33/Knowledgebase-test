"""Benchmark dataset loaders. Importing this package registers all datasets."""
from . import hotpotqa, musique, popqa  # noqa: F401  (import side effect: registration)

__all__ = ["hotpotqa", "musique", "popqa"]
