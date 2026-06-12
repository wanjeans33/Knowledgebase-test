"""Run-directory management and prediction/metric serialization."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def make_run_dir(output_dir: str | Path, run_id: str) -> Path:
    d = Path(output_dir) / run_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def snapshot_config(run_dir: Path, resolved: dict[str, Any]) -> None:
    with open(run_dir / "config.resolved.yaml", "w", encoding="utf-8") as f:
        yaml.safe_dump(resolved, f, sort_keys=False, allow_unicode=True)


class PredictionWriter:
    """Append predictions to predictions.jsonl as they are produced, so metrics can be
    recomputed offline without re-querying the LLM."""

    def __init__(self, run_dir: Path) -> None:
        self.path = run_dir / "predictions.jsonl"
        self._fh = open(self.path, "w", encoding="utf-8")

    def write(self, record: dict[str, Any]) -> None:
        self._fh.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
        self._fh.flush()

    def close(self) -> None:
        self._fh.close()

    def __enter__(self) -> "PredictionWriter":
        return self

    def __exit__(self, *exc) -> None:
        self.close()


def read_predictions(run_dir: Path) -> list[dict[str, Any]]:
    path = Path(run_dir) / "predictions.jsonl"
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
