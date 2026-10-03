# Verification Report

This report is generated from the repository's local validation workflow.

- Readiness audit: executed by `verification/readiness_audit.py`.
- Unit tests: executed by `pytest -q`.
- OpenGAP CLI: checked at validation time; the repository does not bundle or fake the CLI.
- Scope: structural, behavioral, security-boundary, and documentation checks.
