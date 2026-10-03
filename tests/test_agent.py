from core.agent_core import AgentCore
from adapters.registry import build_default_registry

def test_agent_lists_domain_tools():
    agent = AgentCore(build_default_registry())
    assert agent.list_tools() == ["calculate-power", "design-experiment", "generate-analysis-plan"]

def test_agent_executes_tool():
    agent = AgentCore(build_default_registry())
    result = agent.execute("design-experiment", {"title":"A","objective":"Compare","primary_outcome":"score","groups":["control","treatment"]})
    assert result["ok"] is True
