# Explainability

## Inputs and Data Sources
Inputs are supplied directly by the caller as structured JSON-like objects to the domain tools. The data source is therefore the caller's declared research objective, outcome definition, group specification, statistical assumptions, and optional covariates; no external data source is silently added.

The data used by the agent is limited to the fields required by each tool. Input mechanisms are framework-neutral tool calls, so the same validated payload can be transported through an external adapter without changing the domain logic.

### Input Requirements
The experiment designer requires a title, objective, primary outcome, and at least two unique groups. Power analysis requires a positive standardized effect, alpha, target power, and an optional allocation ratio.

### Failure Handling
Missing fields, wrong types, non-finite numbers, duplicate groups, and unsupported values produce structured validation errors. Unexpected execution failures are converted into a generic execution error so internal details and secrets are not returned.

## Decision and Reasoning
The decision is produced from explicit rules rather than hidden model state. The design tool constructs an equal-allocation parallel-group randomized design, the power tool applies a two-group normal-approximation formula, and the analysis-plan tool maps outcome type to a documented statistical method family.

The reasoning is therefore auditable: inputs determine the formula or rule, and the resulting structured output exposes assumptions and limitations. Power planning uses z-quantiles with n1 = (1 + 1/r) * ((z_alpha + z_power) / d)^2 and n2 = r*n1, where r is the group-2/group-1 size ratio.

### Rules Applied
The agent rejects unsupported allocation modes, invalid probability ranges, non-positive effect sizes, and malformed outcome types. It rounds calculated sample sizes upward because fractional participants cannot be enrolled.

### Expected Outputs
Each successful tool call returns a structured object containing the tool name, success flag, and domain-specific data. The domain output distinguishes planning assumptions from empirical observations and never invents observed results.

### Worked Example
For a two-group planning request, a caller can supply a standardized effect, alpha, target power, and allocation ratio to receive calculated integer group sizes. A separate design request can describe the groups and primary outcome to receive a reproducible experiment structure without fabricating any study results.

## Limits and Constraints
A limitation of this implementation is that its power calculation is a normal-approximation planning method for a two-group standardized mean difference. It does not automatically account for clustering, attrition, multiplicity, noncompliance, adaptive designs, or uncertainty in the assumed effect size.

A constraint is that the agent only supports the explicitly documented experiment and outcome types. Known issues include the need for specialist review for complex longitudinal, clustered, survival, or otherwise non-standard studies, and unsupported behavior includes claiming achieved power or causal validity from the planning tools alone.

### Constraints
The agent does not read arbitrary files, access external services, or require model credentials for domain calculations. Ethical approval, feasibility, recruitment, and domain-specific regulatory decisions remain outside the tool's scope.
