"""Framework-independent agent core and dynamic tool registry."""
from __future__ import annotations
from typing import Any
from contracts.tool_contract import Tool

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        if not isinstance(tool, Tool):
            raise TypeError("Only Tool instances can be registered")
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def discover(self) -> list[str]:
        return sorted(self._tools)

    def get(self, name: str) -> Tool:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise KeyError(f"Unknown tool: {name}") from exc

    def execute(self, name: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.get(name).execute(payload).to_dict()

class AgentCore:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def list_tools(self) -> list[str]:
        return self.registry.discover()

    def execute(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.registry.execute(tool_name, payload)
