"""Stable content hashing for cache keys and index identity."""
from __future__ import annotations

import hashlib
import json
from typing import Any


def stable_hash(obj: Any, length: int = 12) -> str:
    payload = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(payload).hexdigest()[:length]
