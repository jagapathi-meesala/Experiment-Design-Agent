"""Generate a concise pre-analysis plan from explicit inputs."""
from __future__ import annotations
from contracts.tool_contract import Tool, ToolError

_ALLOWED = {"continuous", "binary", "count", "time-to-event"}


def _execute(p: dict) -> dict:
    outcome_type = p["outcome_type"]
    if outcome_type not in _ALLOWED:
        raise ToolError(f"outcome_type must be one of: {', '.join(sorted(_ALLOWED))}")
    primary = p["primary_outcome"]
    if not isinstance(primary, str) or not primary.strip():
        raise ToolError("primary_outcome must be a non-empty string")
    covariates = p.get("covariates", [])
    if not isinstance(covariates, list) or any(not isinstance(x, str) or not x.strip() for x in covariates):
        raise ToolError("covariates must be a list of non-empty strings")
    methods = {
        "continuous": "difference in means with a two-sample t-test or regression model",
        "binary": "risk difference/risk ratio or logistic regression, selected before analysis",
        "count": "rate comparison using Poisson or negative-binomial regression as justified",
        "time-to-event": "survival analysis such as Cox regression when proportional-hazards assumptions are appropriate",
    }
    return {
        "estimand": f"Effect of assigned group on {primary.strip()} under the specified analysis population",
        "primary_outcome": primary.strip(),
        "outcome_type": outcome_type,
        "primary_method": methods[outcome_type],
        "covariates": [x.strip() for x in covariates],
        "missing_data": "Document missingness before analysis and pre-specify an appropriate handling strategy; do not silently drop observations without justification.",
        "multiplicity": "If multiple confirmatory hypotheses are tested, pre-specify an error-control procedure.",
        "sensitivity": "Report a sensitivity analysis for important deviations from the primary assumptions when feasible.",
        "reporting": "Report effect estimates with uncertainty intervals and the pre-specified decision threshold; avoid interpreting statistical significance as practical importance by itself.",
    }


TOOL = Tool(
    name="generate-analysis-plan",
    description="Generate a pre-specified analysis plan based on outcome type and covariates.",
    input_schema={"type": "object", "properties": {"primary_outcome": {"type": "string"}, "outcome_type": {"type": "string", "enum": sorted(_ALLOWED)}, "covariates": {"type": "array", "items": {"type": "string"}}}, "required": ["primary_outcome", "outcome_type"]},
    execute_fn=_execute,
)
