"""Provider-neutral adapter surface for external agent frameworks."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from core.agent_core import AgentCore

@dataclass(frozen=True)
class AdapterResponse:
    framework: str
    result: dict[str, Any]

class PortableAdapter:
    """Thin transport adapter; no provider SDK is imported."""
    supported_targets = ("openai-sdk", "crewai", "claude-code", "lyzr")

    def __init__(self, core: AgentCore, framework: str):
        if framework not in self.supported_targets:
            raise ValueError(f"Unsupported adapter target: {framework}")
        self.core = core
        self.framework = framework

    def invoke(self, tool_name: str, payload: dict[str, Any]) -> AdapterResponse:
        return AdapterResponse(self.framework, self.core.execute(tool_name, payload))
