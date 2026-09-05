# Phase 7 — Edge Case Test Plan

## Objective

To test how the TB drug discovery research dataset handles invalid, missing, and incomplete data.

## Required Edge Cases

1. Duplicate candidate ID
2. Missing compound name
3. Incomplete candidate record
4. Invalid evidence stage
5. Missing evidence fields
6. Comparison involving incomplete data
7. Invalid CSV structure

## Expected Behavior

The system should either:

* identify the data problem,
* report that information is missing/incomplete,
* or safely reject invalid data.

The system should not silently treat invalid or incomplete data as complete scientific evidence.

## Scope

These tests evaluate dataset and software robustness only.

They do not evaluate clinical effectiveness, safety, treatment suitability, or drug superiority.

## Status

**IN PROGRESS**
