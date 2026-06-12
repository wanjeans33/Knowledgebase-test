"""Name -> factory registries for systems, datasets, metrics, and providers.

Components register themselves with a decorator, e.g.::

    @register_system("vanilla")
    class VanillaRAG: ...

The runner looks them up by the name used in the YAML config. Importing the
relevant package (ragbench.systems, ragbench.datasets, ...) triggers registration.
"""
from __future__ import annotations

from typing import Callable, Generic, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    def __init__(self, kind: str) -> None:
        self._kind = kind
        self._factories: dict[str, Callable[..., T]] = {}

    def register(self, name: str) -> Callable[[Callable[..., T]], Callable[..., T]]:
        def deco(factory: Callable[..., T]) -> Callable[..., T]:
            if name in self._factories:
                raise ValueError(f"{self._kind} '{name}' is already registered")
            self._factories[name] = factory
            return factory

        return deco

    def create(self, name: str, /, **kwargs) -> T:
        if name not in self._factories:
            raise KeyError(
                f"unknown {self._kind} '{name}'. Registered: {sorted(self._factories)}"
            )
        return self._factories[name](**kwargs)

    def names(self) -> list[str]:
        return sorted(self._factories)

    def __contains__(self, name: object) -> bool:
        return name in self._factories


SYSTEMS: Registry = Registry("system")
DATASETS: Registry = Registry("dataset")
METRICS: Registry = Registry("metric")
PROVIDERS: Registry = Registry("provider")


def register_system(name: str):
    return SYSTEMS.register(name)


def register_dataset(name: str):
    return DATASETS.register(name)


def register_metric(name: str):
    return METRICS.register(name)


def register_provider(name: str):
    return PROVIDERS.register(name)
