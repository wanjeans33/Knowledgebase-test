"""Load + validate an experiment config.

Steps: read YAML -> deep-merge under configs/_defaults.yaml (if present) ->
interpolate ${ENV:NAME} from the environment / .env -> validate with Pydantic.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

import yaml

try:  # optional: load .env if python-dotenv is present
    from dotenv import load_dotenv

    load_dotenv()
except Exception:  # pragma: no cover - dotenv is a hard dep but stay defensive
    pass

from .schema import ExperimentConfig

_ENV_PATTERN = re.compile(r"\$\{ENV:([A-Z0-9_]+)(?::([^}]*))?\}")


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    out = dict(base)
    for key, val in override.items():
        if key in out and isinstance(out[key], dict) and isinstance(val, dict):
            out[key] = _deep_merge(out[key], val)
        else:
            out[key] = val
    return out


def _interpolate(obj: Any) -> Any:
    if isinstance(obj, str):
        def repl(m: re.Match) -> str:
            name, default = m.group(1), m.group(2)
            return os.environ.get(name, default if default is not None else "")

        return _ENV_PATTERN.sub(repl, obj)
    if isinstance(obj, dict):
        return {k: _interpolate(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_interpolate(v) for v in obj]
    return obj


def load_raw(path: str | Path) -> dict[str, Any]:
    """Return the merged + interpolated dict without Pydantic validation."""
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    defaults_path = path.parent / "_defaults.yaml"
    if defaults_path.exists() and defaults_path.resolve() != path.resolve():
        with open(defaults_path, "r", encoding="utf-8") as f:
            defaults = yaml.safe_load(f) or {}
        data = _deep_merge(defaults, data)

    return _interpolate(data)


def load_config(path: str | Path) -> ExperimentConfig:
    return ExperimentConfig.model_validate(load_raw(path))
