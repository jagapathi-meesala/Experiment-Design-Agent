from adapters.registry import build_default_registry

def test_design_experiment():
    r = build_default_registry().execute("design-experiment", {"title":"Study","objective":"Compare","primary_outcome":"score","groups":["A","B"]})
    assert r["data"]["allocation"] == {"A": 0.5, "B": 0.5}

def test_power_calculation():
    r = build_default_registry().execute("calculate-power", {"standardized_effect":0.5,"alpha":0.05,"power":0.8})
    assert r["ok"] and r["data"]["total_sample_size"] > 0

def test_analysis_plan():
    r = build_default_registry().execute("generate-analysis-plan", {"primary_outcome":"score","outcome_type":"continuous"})
    assert "t-test" in r["data"]["primary_method"]
