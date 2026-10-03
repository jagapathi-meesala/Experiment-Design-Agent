"""Framework-independent contract shared by all domain tools."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


class ToolError(ValueError):
    """Expected validation or domain failure."""


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    tool: str
    data: dict[str, Any] | None = None
    error: dict[str, str] | None = None

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"ok": self.ok, "tool": self.tool}
        if self.ok:
            payload["data"] = self.data or {}
        else:
            payload["error"] = self.error or {"code": "unknown", "message": "Unknown error"}
        return payload


@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    input_schema: dict[str, Any]
    execute_fn: Callable[[dict[str, Any]], dict[str, Any]]

    def validate(self, payload: Any) -> None:
        if not isinstance(payload, dict):
            raise ToolError("Input must be a JSON object")
        required = self.input_schema.get("required", [])
        for field in required:
            if field not in payload:
                raise ToolError(f"Missing required field: {field}")

    def execute(self, payload: Any) -> ToolResult:
        try:
            self.validate(payload)
            return ToolResult(True, self.name, data=self.execute_fn(payload))
        except ToolError as exc:
            return ToolResult(False, self.name, error={"code": "validation_error", "message": str(exc)})
        except (TypeError, ValueError, OverflowError) as exc:
            return ToolResult(False, self.name, error={"code": "domain_error", "message": str(exc)})
        except Exception as exc:  # defensive boundary; do not leak internals
            return ToolResult(False, self.name, error={"code": "execution_error", "message": "Tool execution failed safely"})
