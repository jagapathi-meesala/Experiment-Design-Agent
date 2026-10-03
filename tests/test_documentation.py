from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def test_required_docs_exist():
    for name in ["README.md","AGENTS.md","DUTIES.md","RULES.md","SOUL.md","EXPLAINABILITY.md"]:
        assert (ROOT/name).is_file()

def test_explainability_headings():
    text = (ROOT/"EXPLAINABILITY.md").read_text()
    assert "## Inputs and Data Sources" in text
    assert "## Decision and Reasoning" in text
    assert "## Limits and Constraints" in text
    assert "\n## Inputs\n" not in text
    assert "\n## Decision\n" not in text
    assert "\n## Limits\n" not in text
