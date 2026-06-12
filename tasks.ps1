# Simple task runner for ragbench (PowerShell).
#   .\tasks.ps1 setup     # create .venv and install (core + local + vanilla + ragas + dev)
#   .\tasks.ps1 test      # run the offline test suite (no API key needed)
#   .\tasks.ps1 smoke     # run configs/smoke.yaml (needs DEEPSEEK_API_KEY in .env)
#   .\tasks.ps1 eval <cfg> # run an experiment config
#   .\tasks.ps1 report <run_dir>

param(
    [Parameter(Position = 0)] [string] $Task = "help",
    [Parameter(Position = 1)] [string] $Arg
)

$py = ".\.venv\Scripts\python.exe"

switch ($Task) {
    "setup" {
        python -m venv .venv
        & $py -m pip install --upgrade pip setuptools wheel
        & $py -m pip install -e ".[local,vanilla,ragas,dev]"
        if (-not (Test-Path ".env")) { Copy-Item ".env.example" ".env"; Write-Host "Created .env -- fill in DEEPSEEK_API_KEY" -ForegroundColor Yellow }
    }
    "test"   { & $py -m pytest }
    "smoke"  { & $py -m ragbench.cli run configs/smoke.yaml }
    "eval"   { & $py -m ragbench.cli run $Arg }
    "report" { & $py -m ragbench.cli report $Arg }
    "list"   { & $py -m ragbench.cli list ($(if ($Arg) { $Arg } else { "all" })) }
    default  {
        Write-Host "Tasks: setup | test | smoke | eval <cfg> | report <run_dir> | list [kind]"
    }
}
