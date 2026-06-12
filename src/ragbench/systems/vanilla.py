"""Vanilla RAG: chunk -> embed -> top-k cosine retrieve -> generate.

This is the baseline every variant is measured against. It inherits the full
retrieve-then-read flow from BaseRAGSystem; the class exists mainly to register
the "vanilla" name and document the contract.
"""
from __future__ import annotations

from ..core.registry import register_system
from .base import BaseRAGSystem


@register_system("vanilla")
class VanillaRAG(BaseRAGSystem):
    name = "vanilla"
