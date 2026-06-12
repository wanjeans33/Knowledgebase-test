# ragbench — RAG / knowledge-base test bench

A test environment for (a) comparing naive RAG vs RAG variants on standard
benchmarks, (b) measuring the **stability/consistency** of an "LLM wiki"
(LLM-maintained knowledge base), and (c) plugging in a future **axiomatic LLM wiki**
for "axiomatic vs non-axiomatic knowledge base" research.

Everything under test implements one `RAGSystem` protocol, so the runner, evaluator,
and stability harness never special-case a system. New systems / datasets / metrics
are registered plugins.

## Backends

- **Generation:** DeepSeek API (OpenAI-compatible). Set `DEEPSEEK_API_KEY` in `.env`.
- **Embedding:** local `sentence-transformers` (bge-m3 / bge-small). No key, first use
  downloads weights.
- **Rerank:** local CrossEncoder (bge-reranker). No key.
- Optional drop-ins: OpenAI embeddings, Ollama generation (see `src/ragbench/providers/`).

## Setup (Windows / PowerShell)

```powershell
.\tasks.ps1 setup        # creates .venv, installs [local,vanilla,ragas,dev], copies .env
# then edit .env and set DEEPSEEK_API_KEY=...
```

Or manually:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[local,vanilla,ragas,dev]"
Copy-Item .env.example .env   # then fill in DEEPSEEK_API_KEY
```

## Verify

```powershell
.\tasks.ps1 test                 # offline test suite — no API key, no network (CI gate)
.\.venv\Scripts\ragbench.exe list all
.\tasks.ps1 smoke                # online: configs/smoke.yaml (20 HotpotQA Qs, deepseek-chat)
```

`smoke` writes `runs/<run_id>/report.md` with EM / F1 / Recall@5.

## Experiments

```powershell
.\tasks.ps1 eval configs\exp_a_variants.yaml     # goal (a): variant comparison
.\tasks.ps1 eval configs\exp_b_stability.yaml    # goal (b): wiki stability harness
.\tasks.ps1 report runs\<run_id>                 # (re)generate report.md offline
```

Each config starts with a tiny `slice:` so you can smoke it in minutes, then raise
`slice` for the medium-scale run.

## Layout

```
configs/      experiment YAMLs (one file == one experiment)
src/ragbench/
  core/       protocols + data types (RAGSystem, AxiomaticKB, Provider, Dataset, Metric)
  providers/  DeepSeek LLM, local embed/rerank, on-disk cache
  systems/    vanilla, rerank, hyde (HyDE/RAG-Fusion), lightrag, memory_wiki, axiomatic_slot
  datasets/   hotpotqa, musique, popqa (HuggingFace loaders -> normalized corpus)
  metrics/    em, f1, recall@k, ndcg@k, mrr, ragas_*, llm judge
  stability/  determinism / paraphrase-invariance / contradiction / ripple harness
  runner/     load -> build -> index -> query -> evaluate -> persist
  report/     markdown report
runs/         per-run outputs (gitignored)
```

## Status / notes

- **vanilla, rerank, hyde** and **hotpotqa, popqa** are exercised by offline tests.
- **lightrag** and **memory_wiki** are lazy adapters over external libs
  (`[graph]` / `[memory]` extras) and need a live run to verify their wiring —
  the libraries' APIs shift between versions; see the module docstrings.
- **musique** uses a community HuggingFace mirror; override `hf_id` if the default 404s.
- **axiomatic** is a documented pluggable slot (`systems/axiomatic_slot.py`) — it raises
  `NotImplementedError` until the axiomatic design is implemented. It already satisfies
  the `AxiomaticKB` protocol so it runs through the same pipeline once filled in.
- **RAGAS** metrics need the `[ragas]` extra and a live LLM; pin the version once green.

## The axiomatic slot (goal c)

`AxiomaticKB` (in `core/rag_system.py`) extends `RAGSystem` with `assert_axioms`,
`check_consistency`, `constrain`, and `explain`. Fill in
`systems/axiomatic_slot.py::AxiomaticWiki` to run the axiomatic wiki through the exact
same benchmarks and stability harness as the baselines — the intended core comparison
for the paper is its `contradiction_rate` and knowledge-edit ripple behavior vs.
non-axiomatic wikis.
