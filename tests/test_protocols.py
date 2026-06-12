"""Every registered system satisfies RAGSystem; the axiomatic slot satisfies AxiomaticKB."""
from __future__ import annotations

import ragbench.systems  # noqa: F401  (registers systems)
from ragbench.core.rag_system import AxiomaticKB, RAGSystem
from ragbench.core.registry import SYSTEMS


def test_systems_registered():
    names = SYSTEMS.names()
    assert "vanilla" in names
    assert "axiomatic" in names


def test_all_systems_implement_rag_protocol():
    for name in SYSTEMS.names():
        inst = SYSTEMS.create(name)
        assert isinstance(inst, RAGSystem), f"{name} does not satisfy RAGSystem"


def test_axiomatic_slot_satisfies_axiomatic_protocol():
    inst = SYSTEMS.create("axiomatic")
    assert isinstance(inst, AxiomaticKB)
