---
name: experimental-design
description: Design structured randomized experiments from explicit research objectives, outcomes, groups, and allocation assumptions.
license: MIT
---
# Experimental Design

## Purpose
Create a reproducible experimental design with explicit groups, allocation, primary outcome, assumptions, and limitations.

## Inputs
Provide a research objective, primary outcome, at least two unique groups, and the supported allocation mode.

## Processing
The design tool validates inputs and constructs a parallel-group randomized design with equal allocation.

## Outputs
The output includes design type, group allocation, randomization assumption, analysis note, assumptions, and limitations.

## Limitations
This skill does not calculate power, establish ethics approval, or determine whether individual randomization is appropriate for clustered interventions.

## Expected Behavior
Malformed or ambiguous inputs are rejected with structured errors rather than silently corrected.
