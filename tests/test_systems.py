"""Offline checks that each vector-based system runs index() + query() with fakes."""
from __future__ import annotations

import pytest

from ragbench.core.registry import SYSTEMS
from ragbench.core.types import Query, RunContext


def _run_ctx(fake_providers, tmp_path):
    return RunContext(run_id="t", seed=0, output_dir=tmp_path, providers=fake_providers)


def _index_and_query(system, fake_dataset, ctx):
    system.index(list(fake_dataset.corpus()), run=ctx)
    ans = system.query(Query("q1", "What is the capital of France?"), run=ctx)
    return ans


def test_vanilla_retrieves_relevant_doc(fake_providers, fake_dataset, tmp_path):
    ctx = _run_ctx(fake_providers, tmp_path)
    sys = SYSTEMS.create("vanilla", top_k=2)
    ans = _index_and_query(sys, fake_dataset, ctx)
    assert ans.retrieved_contexts
    assert ans.retrieved_contexts[0].doc_id == "d1"  # France doc ranks first


def test_rerank_falls_back_without_reranker(fake_providers, fake_dataset, tmp_path):
    ctx = _run_ctx(fake_providers, tmp_path)  # fake bundle has no rerank provider
    sys = SYSTEMS.create("rerank", top_k_retrieve=3, top_k_final=2)
    ans = _index_and_query(sys, fake_dataset, ctx)
    assert len(ans.retrieved_contexts) <= 2


@pytest.mark.parametrize("variant", ["hyde", "rag_fusion", "multi_query"])
def test_hyde_variants_run(fake_providers, fake_dataset, variant, tmp_path):
    ctx = _run_ctx(fake_providers, tmp_path)
    sys = SYSTEMS.create("hyde", variant=variant, n_queries=2, top_k=2)
    ans = _index_and_query(sys, fake_dataset, ctx)
    assert isinstance(ans.text, str)


def test_rrf_fusion_math():
    from ragbench.systems.hyde import reciprocal_rank_fusion

    fused = reciprocal_rank_fusion([["a", "b"], ["b", "a"]], k=60)
    # 'a' and 'b' each appear once at rank0 and once at rank1 -> equal scores
    assert abs(fused["a"] - fused["b"]) < 1e-9
