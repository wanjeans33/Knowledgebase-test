"""Experiment execution: load -> build -> index -> query -> evaluate -> persist -> report."""
from .pipeline import run_experiment

__all__ = ["run_experiment"]
