import os
from adapters.registry import build_default_registry

def test_missing_field_rejected():
    r = build_default_registry().execute("design-experiment", {})
    assert not r["ok"] and r["error"]["code"] == "validation_error"

def test_wrong_type_rejected():
    r = build_default_registry().execute("calculate-power", {"standardized_effect":"secret","alpha":0.05,"power":0.8})
    assert not r["ok"]
    assert "secret" not in str(r)

def test_secret_not_returned_from_environment():
    os.environ["TEST_SECRET"] = "should-not-leak"
    r = build_default_registry().execute("design-experiment", {"title":"x","objective":"y","primary_outcome":"z","groups":["a","b"]})
    assert "should-not-leak" not in str(r)
