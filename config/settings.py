"""Runtime configuration loaded exclusively from environment variables."""
from __future__ import annotations

import os


def _required(name: str) -> str:
    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Required environment variable {name} is not set")
    return value.strip()


def load_settings() -> dict[str, str]:
    """Load optional runtime settings without embedding production defaults."""
    settings = {}
    for key in ("EXPERIMENT_AGENT_LOG_LEVEL", "EXPERIMENT_AGENT_ENV"):
        value = os.getenv(key)
        if value is not None:
            settings[key] = value
    return settings
