---
name: analysis-plan
description: Generate a pre-analysis plan covering estimand, primary method, covariates, missing data, multiplicity, sensitivity, and reporting.
license: MIT
---
# Analysis Plan

## Purpose
Turn a declared primary outcome and outcome type into a concise, pre-specified analysis plan.

## Inputs
Provide a primary outcome, one supported outcome type, and optional covariate names.

## Processing
The tool selects a method family based on outcome type and adds explicit guidance for missing data, multiplicity, sensitivity analysis, and reporting.

## Outputs
The output is a structured analysis plan suitable for review and further domain-specific refinement.

## Limitations
The method family is not a substitute for specialist statistical review, especially for complex longitudinal, clustered, adaptive, or non-standard designs.

## Expected Behavior
Unsupported outcome types and malformed covariates are rejected.
