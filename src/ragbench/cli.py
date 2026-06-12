"""`ragbench` command-line entrypoint."""
from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(add_completion=False, help="RAG / knowledge-base test bench.")
console = Console()


def _load_registries() -> None:
    """Import component packages so their @register_* decorators run."""
    import ragbench.systems  # noqa: F401
    # datasets/metrics packages are imported lazily where available
    try:
        import ragbench.datasets  # noqa: F401
    except Exception:
        pass
    try:
        import ragbench.metrics  # noqa: F401
    except Exception:
        pass


@app.command("list")
def list_components(
    kind: str = typer.Argument("systems", help="systems | datasets | metrics | all"),
) -> None:
    """List registered components."""
    _load_registries()
    from ragbench.core.registry import DATASETS, METRICS, SYSTEMS

    mapping = {"systems": SYSTEMS, "datasets": DATASETS, "metrics": METRICS}
    kinds = mapping.keys() if kind == "all" else [kind]
    for k in kinds:
        if k not in mapping:
            console.print(f"[red]unknown kind '{k}'. Use: systems | datasets | metrics | all")
            raise typer.Exit(code=1)
        table = Table(title=f"registered {k}")
        table.add_column("name", style="cyan")
        for name in mapping[k].names():
            table.add_row(name)
        console.print(table)


@app.command("run")
def run(
    config: Path = typer.Argument(..., exists=True, help="Path to an experiment YAML."),
) -> None:
    """Run an experiment from a config file."""
    from ragbench.runner.pipeline import run_experiment

    run_dir = run_experiment(config)
    console.print(f"[green]done[/green] -> {run_dir}")


@app.command("report")
def report(
    run_dir: Path = typer.Argument(..., exists=True, help="A runs/<id> directory."),
) -> None:
    """(Re)generate the markdown report for an existing run directory."""
    from ragbench.report.markdown import write_report

    out = write_report(run_dir)
    console.print(f"[green]report[/green] -> {out}")


if __name__ == "__main__":
    app()
