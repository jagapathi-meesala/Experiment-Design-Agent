"""Default registry construction without framework dependencies."""
from core.agent_core import ToolRegistry
from tools import DESIGN_EXPERIMENT, CALCULATE_POWER, GENERATE_ANALYSIS_PLAN

def build_default_registry() -> ToolRegistry:
    registry = ToolRegistry()
    for tool in (DESIGN_EXPERIMENT, CALCULATE_POWER, GENERATE_ANALYSIS_PLAN):
        registry.register(tool)
    return registry
