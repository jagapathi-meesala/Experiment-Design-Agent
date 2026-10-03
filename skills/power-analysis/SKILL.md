---
name: power-analysis
description: Perform deterministic two-group sample-size planning from standardized effect, alpha, target power, and allocation ratio.
license: MIT
---
# Power Analysis

## Purpose
Estimate the minimum group sizes needed for a two-sided two-group standardized mean-difference design using a normal approximation.

## Inputs
Supply a positive standardized effect, alpha between zero and one, target power between zero and one, and optionally the group-size ratio.

## Processing
The tool computes normal quantiles and applies the two-sample planning formula, then rounds each group size upward.

## Outputs
The result reports assumptions, integer group sizes, total sample size, and limitations.

## Limitations
The calculation is a planning approximation and does not account for clustering, attrition, multiplicity, noncompliance, or misspecified effect size.

## Expected Behavior
Non-finite values and out-of-range parameters are rejected.
