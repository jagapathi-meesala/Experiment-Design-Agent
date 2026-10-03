"""Create a structured experiment design from explicit study parameters."""
from __future__ import annotations

import math
from contracts.tool_contract import Tool, ToolError


def _execute(p: dict) -> dict:
    title = p["title"]
    objective = p["objective"]
    outcome = p["primary_outcome"]
    groups = p["groups"]
    if not isinstance(title, str) or not title.strip() or len(title) > 200:
        raise ToolError("title must be a non-empty string of at most 200 characters")
    if not isinstance(objective, str) or not objective.strip() or len(objective) > 1000:
        raise ToolError("objective must be a non-empty string of at most 1000 characters")
    if not isinstance(outcome, str) or not outcome.strip() or len(outcome) > 300:
        raise ToolError("primary_outcome must be a non-empty string of at most 300 characters")
    if not isinstance(groups, list) or len(groups) < 2 or len(groups) > 10:
        raise ToolError("groups must contain 2 to 10 groups")
    if any(not isinstance(g, str) or not g.strip() or len(g) > 100 for g in groups):
        raise ToolError("each group must be a non-empty string of at most 100 characters")
    if len({g.strip().lower() for g in groups}) != len(groups):
        raise ToolError("groups must have unique names")
    allocation = p.get("allocation", "equal")
    if allocation != "equal":
        raise ToolError("Only equal allocation is supported by this deterministic planner")
    return {
        "title": title.strip(),
        "objective": objective.strip(),
        "primary_outcome": outcome.strip(),
        "design": "parallel-group randomized controlled experiment",
        "groups": [g.strip() for g in groups],
        "allocation": {g.strip(): 1 / len(groups) for g in groups},
        "randomization": "individual-level randomization assumed",
        "analysis_note": "Choose the statistical test based on the outcome type and pre-specify covariates before observing outcomes.",
        "assumptions": ["Groups are mutually exclusive", "Randomization is feasible", "Primary outcome is measured consistently"],
        "limitations": ["Does not calculate sample size", "Does not establish ethical approval", "Individual randomization may be inappropriate for clustered interventions"],
    }


TOOL = Tool(
    name="design-experiment",
    description="Create a structured randomized parallel-group experiment design.",
    input_schema={"type": "object", "properties": {"title": {"type": "string"}, "objective": {"type": "string"}, "primary_outcome": {"type": "string"}, "groups": {"type": "array", "items": {"type": "string"}}, "allocation": {"type": "string", "enum": ["equal"]}}, "required": ["title", "objective", "primary_outcome", "groups"]},
    execute_fn=_execute,
)
