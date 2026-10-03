# Rules

1. Validate required fields and types before execution.
2. Reject non-finite numeric values and unsupported parameter ranges.
3. Use deterministic formulas for supported calculations.
4. Never fabricate experimental observations, p-values, or effect estimates.
5. Keep runtime configuration in environment variables.
6. Never log or return environment secrets.
7. Do not read or write user files from domain tools.
8. Return structured errors for invalid requests.
9. State limitations when a method relies on simplifying assumptions.
