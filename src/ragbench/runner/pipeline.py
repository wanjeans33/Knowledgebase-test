"""End-to-end experiment runner.

Flow: load config -> seed -> build providers -> for each dataset (load+slice) and
each system (index corpus), run every query `repeats` times -> write predictions ->
compute metrics -> persist parquet/csv -> write markdown report.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from ..config import load_config
from ..config.loader import load_raw
from ..core.registry import DATASETS, SYSTEMS
from ..core.types import Answer, GoldAnswer, Query, RetrievedContext, RunContext
from ..metrics import build_metrics
from ..providers import build_providers
from ..utils.hashing import stable_hash
from ..utils.seeding import seed_everything
from .persist import PredictionWriter, make_run_dir, snapshot_config


def _import_components() -> None:
    import ragbench.datasets  # noqa: F401
    import ragbench.metrics  # noqa: F401
    import ragbench.systems  # noqa: F401


def _make_run_id(name: str, resolved: dict) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"{name}-{ts}-{stable_hash(resolved, 8)}"


def _answer_to_record(system, dataset_name, q: Query, repeat, answer: Answer,
                      gold: GoldAnswer) -> dict:
    return {
        "system": system,
        "dataset": dataset_name,
        "qid": q.qid,
        "repeat": repeat,
        "question": q.question,
        "answer": answer.text,
        "retrieved": [
            {"doc_id": c.doc_id, "rank": c.rank, "score": c.score}
            for c in answer.retrieved_contexts
        ],
        "gold_answers": gold.answers,
        "gold_support": gold.supporting_doc_ids,
        "metadata": answer.metadata,
    }


def _record_to_answer(rec: dict) -> Answer:
    ctxs = [
        RetrievedContext(doc_id=r["doc_id"], text="", score=r.get("score", 0.0),
                         rank=r.get("rank", 0))
        for r in rec.get("retrieved", [])
    ]
    return Answer(text=rec["answer"], retrieved_contexts=ctxs, metadata=rec.get("metadata", {}))


def run_experiment(config_path: str | Path, *, providers=None) -> Path:
    """Run an experiment. `providers` may be injected (e.g. fakes in tests); otherwise
    they are built from the config's provider block."""
    cfg = load_config(config_path)
    resolved = load_raw(config_path)
    _import_components()

    run_id = _make_run_id(cfg.name, resolved)
    run_dir = make_run_dir(cfg.run.output_dir, run_id)
    snapshot_config(run_dir, resolved)
    seed_everything(cfg.seed)

    if providers is None:
        cache_dir = run_dir.parent.parent / ".cache" / "providers"
        providers = build_providers(cfg.provider, cache_dir=cache_dir)
    run_ctx = RunContext(run_id=run_id, seed=cfg.seed, output_dir=run_dir, providers=providers)

    metrics = build_metrics(cfg.metrics)
    records: list[dict] = []
    stability_rows: list[dict] = []

    with PredictionWriter(run_dir) as writer:
        for dcfg in cfg.datasets:
            ds = DATASETS.create(dcfg.name, split=dcfg.split, **dcfg.merged_params())
            if dcfg.slice:
                ds = ds.slice(dcfg.slice, seed=cfg.seed)
            corpus = list(ds.corpus())
            queries = list(ds.queries())

            for scfg in cfg.systems:
                system = SYSTEMS.create(scfg.name, **scfg.merged_params())
                system.index(corpus, run=run_ctx)

                def _run_one(q: Query, repeat: int):
                    ans = system.query(q, run=run_ctx)
                    gold = ds.gold(q.qid)
                    return _answer_to_record(scfg.name, dcfg.name, q, repeat, ans, gold)

                jobs = [(q, r) for q in queries for r in range(cfg.run.repeats)]
                if cfg.run.concurrency > 1:
                    with ThreadPoolExecutor(max_workers=cfg.run.concurrency) as ex:
                        results = list(ex.map(lambda jr: _run_one(*jr), jobs))
                else:
                    results = [_run_one(q, r) for q, r in jobs]

                for rec in results:
                    writer.write(rec)
                    records.append(rec)

                if cfg.stability is not None:
                    from ..stability.harness import run_stability, stability_records_to_rows

                    recs = run_stability(system, queries, run=run_ctx, cfg=cfg.stability)
                    rows = stability_records_to_rows(recs)
                    for r in rows:
                        r["dataset"] = dcfg.name
                    stability_rows.extend(rows)

    if stability_rows:
        import pandas as pd

        pd.DataFrame(stability_rows).to_parquet(run_dir / "stability.parquet", index=False)

    _evaluate_and_report(run_dir, records, metrics)
    return run_dir


def _evaluate_and_report(run_dir: Path, records: list[dict], metrics: list) -> None:
    import pandas as pd

    from ..report.markdown import write_report

    rows = []
    for rec in records:
        ans = _record_to_answer(rec)
        gold = GoldAnswer(answers=rec.get("gold_answers", []),
                          supporting_doc_ids=rec.get("gold_support", []))
        q = Query(qid=rec["qid"], question=rec["question"])
        scores: dict[str, float] = {}
        for m in metrics:
            try:
                scores.update(m.score(q, ans, gold, run=None))
            except Exception:
                continue
        rows.append({"system": rec["system"], "dataset": rec["dataset"],
                     "qid": rec["qid"], "repeat": rec["repeat"], **scores})

    df = pd.DataFrame(rows)
    df.to_parquet(run_dir / "metrics.parquet", index=False)

    metric_cols = [c for c in df.columns if c not in {"system", "dataset", "qid", "repeat"}]
    if metric_cols:
        summary = df.groupby(["system", "dataset"])[metric_cols].mean().reset_index()
    else:
        summary = df[["system", "dataset"]].drop_duplicates()
    summary.to_csv(run_dir / "summary.csv", index=False)

    write_report(run_dir)
