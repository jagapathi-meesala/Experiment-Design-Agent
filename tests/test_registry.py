import pytest
from adapters.registry import build_default_registry
from contracts.tool_contract import Tool

def test_discovery_is_dynamic():
    reg = build_default_registry()
    assert "design-experiment" in reg.discover()

def test_duplicate_registration_rejected():
    reg = build_default_registry()
    from tools import DESIGN_EXPERIMENT
    with pytest.raises(ValueError): reg.register(DESIGN_EXPERIMENT)

def test_unknown_tool_rejected():
    with pytest.raises(KeyError): build_default_registry().get("missing")
