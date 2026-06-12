"""Offline end-to-end: vanilla RAG over a fake dataset with fake providers.

No network, no API key, runs in well under a second. This is the CI gate that the
load -> index -> query -> evaluate -> persist -> report pipeline stays wired together.
"""
from __future__ import annotations

import yaml

from ragbench.core.registry import DATASETS


def _register_fake_dataset():
    from conftest import FakeDataset

    if "fake" not in DATASETS:
        DATASETS.register("fake")(lambda **kw: FakeDataset())


def test_pipeline_end_to_end(tmp_path, fake_providers):
    _register_fake_dataset()

    cfg = {
        "name": "offline_smoke",
        "seed": 0,
        "provider": {"llm": {"backend": "deepseek"}, "cache": False},
        "systems": [{"name": "vanilla", "top_k": 2, "chunk_size": 64}],
        "datasets": [{"name": "fake", "split": "test"}],
        "metrics": ["em", "f1", "recall@5", "mrr"],
        "run": {"repeats": 1, "output_dir": str(tmp_path), "concurrency": 1},
    }
    cfg_path = tmp_path / "offline.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")

    from ragbench.runner.pipeline import run_experiment

    run_dir = run_experiment(cfg_path, providers=fake_providers)

    assert (run_dir / "predictions.jsonl").exists()
    assert (run_dir / "metrics.parquet").exists()
    assert (run_dir / "summary.csv").exists()
    assert (run_dir / "report.md").exists()

    import pandas as pd

    df = pd.read_parquet(run_dir / "metrics.parquet")
    assert len(df) == 2  # two queries, one repeat
    for col in ["em", "f1", "recall@5", "mrr"]:
        assert col in df.columns
    # Fake embeddings should retrieve the gold paragraph -> perfect retrieval.
    assert df["recall@5"].mean() == 1.0
    # All scores are valid probabilities.
    for col in ["em", "f1", "recall@5", "mrr"]:
        assert df[col].between(0.0, 1.0).all()


def test_report_regenerates(tmp_path, fake_providers):
    _register_fake_dataset()
    cfg = {
        "name": "offline_smoke2",
        "provider": {"llm": {"backend": "deepseek"}, "cache": False},
        "systems": [{"name": "vanilla", "top_k": 2}],
        "datasets": [{"name": "fake"}],
        "metrics": ["em", "f1"],
        "run": {"output_dir": str(tmp_path), "concurrency": 1},
    }
    cfg_path = tmp_path / "c.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg), encoding="utf-8")

    from ragbench.report.markdown import write_report
    from ragbench.runner.pipeline import run_experiment

    run_dir = run_experiment(cfg_path, providers=fake_providers)
    out = write_report(run_dir)
    assert out.exists()
    assert "Run report" in out.read_text(encoding="utf-8")
