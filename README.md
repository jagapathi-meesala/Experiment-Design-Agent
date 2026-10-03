# Experiment Design Agent

A framework-independent OpenGAP 0.1.0 agent for turning explicit research questions into reproducible experiment designs, approximate two-group power calculations, and pre-analysis plans.

## Architecture

The `core/` layer owns dynamic tool registration and execution. `contracts/` defines the provider-neutral tool interface, `tools/` contains domain implementations plus MCP-compatible YAML definitions, and `adapters/` exposes a thin framework-neutral transport surface.

## Installation

Create a Python environment and install `requirements.txt`. The runtime domain tools use the Python standard library; PyYAML and jsonschema are included for repository validation and tests.

## Configuration

Optional runtime settings are read from environment variables. No API keys, passwords, tokens, or production credentials are embedded in the repository.

## Tools

- `design-experiment`: constructs an equal-allocation parallel-group randomized design.
- `calculate-power`: estimates two-group sample size using a normal approximation for a standardized mean difference.
- `generate-analysis-plan`: generates a pre-analysis plan by outcome type.

## Skills

- `experimental-design`
- `power-analysis`
- `analysis-plan`

## Usage

```python
from adapters.registry import build_default_registry
from core.agent_core import AgentCore

agent = AgentCore(build_default_registry())
print(agent.execute("design-experiment", {
    "title": "Example Study",
    "objective": "Compare two interventions",
    "primary_outcome": "score",
    "groups": ["control", "treatment"]
}))
```

## Testing

Run `pytest -q` and `python3 verification/readiness_audit.py`. If the OpenGAP CLI is installed, run `opengap validate` from the repository root.

## Portability

The core has no dependency on OpenAI, CrewAI, Claude, Lyzr, LangChain, or other agent frameworks. The adapter exposes named integration targets for those ecosystems, but no SDK compatibility is claimed as tested merely by the presence of the adapter.

## Limitations

The experiment planner supports equal allocation only. Power analysis is a normal-approximation planning method for two independent groups and does not automatically model clustering, attrition, multiplicity, noncompliance, or complex designs. Analysis plans provide method families and must be reviewed for specialized studies.
