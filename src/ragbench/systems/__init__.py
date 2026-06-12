"""RAGSystem implementations. Importing this package registers all systems.

Heavy/optional dependencies (langchain, faiss, torch) are imported lazily inside
each system's methods, so registration works even when an extra isn't installed.
"""
from . import (  # noqa: F401  (import side effect: registration)
    axiomatic_slot,
    hyde,
    lightrag,
    memory_wiki,
    rerank,
    vanilla,
)

__all__ = ["vanilla", "rerank", "hyde", "lightrag", "memory_wiki", "axiomatic_slot"]
