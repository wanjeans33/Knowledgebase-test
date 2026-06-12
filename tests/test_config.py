"""Config loading: defaults merge, env interpolation, schema validation."""
from __future__ import annotations

from pathlib import Path

from ragbench.config import load_config
from ragbench.config.loader import load_raw

CONFIGS = Path(__file__).resolve().parents[1] / "configs"


def test_smoke_config_loads():
    cfg = load_config(CONFIGS / "smoke.yaml")
    assert cfg.name == "smoke"
    assert cfg.systems[0].name == "vanilla"
    assert cfg.systems[0].merged_params()["top_k"] == 3
    assert cfg.datasets[0].slice == 20
    assert "em" in cfg.metrics


def test_defaults_merge_fills_provider():
    cfg = load_config(CONFIGS / "smoke.yaml")
    # output_dir comes from _defaults.yaml's run block (smoke also sets it; either way present)
    assert cfg.run.output_dir.startswith("runs")
    assert cfg.provider.llm.backend == "deepseek"


def test_env_interpolation(monkeypatch):
    monkeypatch.setenv("DEEPSEEK_BASE_URL", "https://example.test")
    raw = load_raw(CONFIGS / "_defaults.yaml")
    assert raw["provider"]["llm"]["base_url"] == "https://example.test"


def test_env_interpolation_default_when_unset(monkeypatch):
    monkeypatch.delenv("DEEPSEEK_BASE_URL", raising=False)
    raw = load_raw(CONFIGS / "_defaults.yaml")
    assert raw["provider"]["llm"]["base_url"] == "https://api.deepseek.com"


def test_all_configs_validate():
    for name in ["smoke.yaml", "exp_a_variants.yaml", "exp_b_stability.yaml"]:
        cfg = load_config(CONFIGS / name)
        assert cfg.name
