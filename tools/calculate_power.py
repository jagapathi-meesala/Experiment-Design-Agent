"""Two-sample normal-approximation power planning."""
from __future__ import annotations

import math
from statistics import NormalDist
from contracts.tool_contract import Tool, ToolError


def _finite(x: object, name: str) -> float:
    if not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(float(x)):
        raise ToolError(f"{name} must be a finite number")
    return float(x)


def _execute(p: dict) -> dict:
    effect = abs(_finite(p["standardized_effect"], "standardized_effect"))
    alpha = _finite(p["alpha"], "alpha")
    power = _finite(p["power"], "power")
    ratio = _finite(p.get("allocation_ratio", 1.0), "allocation_ratio")
    if effect <= 0:
        raise ToolError("standardized_effect must be greater than 0")
    if not 0 < alpha < 1:
        raise ToolError("alpha must be between 0 and 1")
    if not 0 < power < 1:
        raise ToolError("power must be between 0 and 1")
    if ratio <= 0:
        raise ToolError("allocation_ratio must be greater than 0")
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    # n1 = (1 + 1/r) * ((z_alpha + z_power)/d)^2; r=n2/n1
    n1 = (1 + 1 / ratio) * ((z_alpha + z_power) / effect) ** 2
    n2 = ratio * n1
    n1_i, n2_i = math.ceil(n1), math.ceil(n2)
    return {
        "method": "two-sample normal approximation for a standardized mean difference",
        "alpha": alpha,
        "target_power": power,
        "standardized_effect": effect,
        "allocation_ratio_n2_over_n1": ratio,
        "minimum_group_sizes": {"group_1": n1_i, "group_2": n2_i},
        "total_sample_size": n1_i + n2_i,
        "assumptions": ["Two-sided test", "Independent observations", "Approximately normal outcome or large-sample validity", "Common standardized-effect interpretation"],
        "limitations": ["Planning approximation, not a guarantee of achieved power", "Does not account for attrition, clustering, multiplicity, or noncompliance", "Effect size must be justified externally"],
    }


TOOL = Tool(
    name="calculate-power",
    description="Calculate approximate sample size for a two-group standardized mean difference.",
    input_schema={"type": "object", "properties": {"standardized_effect": {"type": "number"}, "alpha": {"type": "number"}, "power": {"type": "number"}, "allocation_ratio": {"type": "number"}}, "required": ["standardized_effect", "alpha", "power"]},
    execute_fn=_execute,
)
