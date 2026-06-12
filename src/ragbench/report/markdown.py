"""Generate report.md from a run directory's metrics.parquet / summary.csv.

Produces a per-(system, dataset) metric table and flags the best system per metric.
If stability.parquet exists, appends a stability section with threshold flags.
"""
from __future__ import annotations

from pathlib import Path


def write_report(run_dir: str | Path) -> Path:
    import pandas as pd

    run_dir = Path(run_dir)
    lines: list[str] = [f"# Run report: {run_dir.name}", ""]

    metrics_path = run_dir / "metrics.parquet"
    if metrics_path.exists():
        df = pd.read_parquet(metrics_path)
        metric_cols = [c for c in df.columns if c not in {"system", "dataset", "qid", "repeat"}]
        n_q = df["qid"].nunique() if "qid" in df else 0
        lines += [f"- systems: {sorted(df['system'].unique())}",
                  f"- datasets: {sorted(df['dataset'].unique())}",
                  f"- questions per (system,dataset): {n_q}",
                  f"- metrics: {metric_cols}", ""]

        if metric_cols:
            summary = df.groupby(["system", "dataset"])[metric_cols].mean().reset_index()
            lines += ["## Results (mean per system × dataset)", ""]
            lines.append("| system | dataset | " + " | ".join(metric_cols) + " |")
            lines.append("|" + "---|" * (2 + len(metric_cols)))
            for _, row in summary.iterrows():
                vals = " | ".join(f"{row[c]:.4f}" if pd.notna(row[c]) else "—" for c in metric_cols)
                lines.append(f"| {row['system']} | {row['dataset']} | {vals} |")
            lines.append("")

            lines += ["## Best system per metric (averaged over datasets)", ""]
            per_sys = df.groupby("system")[metric_cols].mean()
            lines.append("| metric | best system | value |")
            lines.append("|---|---|---|")
            for c in metric_cols:
                if per_sys[c].notna().any():
                    best = per_sys[c].idxmax()
                    lines.append(f"| {c} | {best} | {per_sys[c].max():.4f} |")
            lines.append("")
    else:
        lines.append("_no metrics.parquet found_\n")

    stability_path = run_dir / "stability.parquet"
    if stability_path.exists():
        df = pd.read_parquet(stability_path)
        lines += ["## Stability / consistency", ""]
        cols = [c for c in df.columns if c not in {"system", "dataset", "qid"}]
        agg = df.groupby("system")[cols].mean().reset_index()
        lines.append("| system | " + " | ".join(cols) + " |")
        lines.append("|" + "---|" * (1 + len(cols)))
        for _, row in agg.iterrows():
            vals = " | ".join(f"{row[c]:.4f}" if isinstance(row[c], float) else str(row[c]) for c in cols)
            lines.append(f"| {row['system']} | {vals} |")
        lines.append("")

    out = run_dir / "report.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out
