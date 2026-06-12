"""Registry behavior: register, create, duplicate guard, unknown lookup."""
from __future__ import annotations

import pytest

from ragbench.core.registry import Registry


def test_register_and_create():
    reg: Registry = Registry("thing")

    @reg.register("a")
    def make_a(**kw):
        return ("a", kw)

    assert "a" in reg
    assert reg.names() == ["a"]
    assert reg.create("a", x=1) == ("a", {"x": 1})


def test_duplicate_registration_rejected():
    reg: Registry = Registry("thing")
    reg.register("a")(lambda **kw: 1)
    with pytest.raises(ValueError):
        reg.register("a")(lambda **kw: 2)


def test_unknown_lookup_raises():
    reg: Registry = Registry("thing")
    with pytest.raises(KeyError):
        reg.create("nope")
