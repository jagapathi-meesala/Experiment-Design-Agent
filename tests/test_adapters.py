import pytest
from adapters import PortableAdapter
from adapters.registry import build_default_registry
from core.agent_core import AgentCore

def test_supported_adapter_invokes_core():
    adapter = PortableAdapter(AgentCore(build_default_registry()), "openai-sdk")
    r = adapter.invoke("generate-analysis-plan", {"primary_outcome":"rate","outcome_type":"binary"})
    assert r.framework == "openai-sdk" and r.result["ok"]

def test_unknown_adapter_rejected():
    with pytest.raises(ValueError): PortableAdapter(AgentCore(build_default_registry()), "unknown")
