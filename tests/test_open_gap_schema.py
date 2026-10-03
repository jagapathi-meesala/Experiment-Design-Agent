from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]

def test_manifest_static_opengap_constraints():
    data = yaml.safe_load((ROOT/"agent.yaml").read_text())
    assert data["spec_version"] == "0.1.0"
    assert data["name"] == "experiment-design-agent"
    assert set(data).issubset({"spec_version","name","version","description","author","license","model","extends","dependencies","skills","tools","agents","delegation","runtime","a2a","compliance","tags","metadata"})
    assert all(isinstance(x, str) for x in data["skills"])
    assert all(isinstance(x, str) for x in data["tools"])
    for skill in data["skills"]:
        assert (ROOT/"skills"/skill/"SKILL.md").is_file()
    for tool in data["tools"]:
        assert (ROOT/"tools"/(tool+".yaml")).is_file()
