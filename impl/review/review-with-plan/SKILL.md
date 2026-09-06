---
name: review-with-plan
description: Review uncommitted implementation changes against a supplied Plan for unmet requirements, constraint violations, scope drift, and missing verification. Use when the user invokes $review-with-plan or asks whether an implementation matches its Plan.
---

# Review Implementation Against Plan

Review a supplied Plan against the current uncommitted implementation and its verification without changing code, configuration, tests, documentation, or the Plan. The user decides whether to apply findings.

Require a Plan file path or Plan text. If neither is provided, ask for it and stop. If there are no uncommitted changes, report that and stop.

Read the Plan completely, inspect the current diff, and gather only the codebase and verification evidence needed to interpret it. Extract atomic propositions from Required outcomes, Constraints, Out of Scope, Done When, and Verification. Compare each proposition to direct evidence; do not treat a different design, file layout, API shape, or test style as a mismatch when observable behavior remains compliant. Report only evidence-supported findings, cite Plan locations and code paths with line numbers, and label facts, inferences, and unknowns.

## Decision procedure

Evaluate each atomic proposition in this order:

1. Is it a normative requirement? If no, treat it as context; do not run a compliance check.
2. Is there direct evidence that satisfies it? If yes, classify it `Pass`.
3. Is there direct evidence confirming contradiction or omission? If yes, classify it `Fail`; otherwise classify it `Unknown` and emit no finding.
4. A `Fail` for a required outcome, Constraint, Out of Scope boundary, Done When condition, or security, data-integrity, compatibility, lifecycle, or destructive requirement is `Must`.
5. Explicitly required Verification that is missing, stale, non-exercising, or unproven where the Plan requires passing is `Must`. An unrun or unavailable check without an explicit pass requirement is `Unknown` and emits no finding.
6. A named scenario, boundary, or failure behavior that is satisfied but has unclear verification, and is not an explicit completion condition, is `Recommended`.
7. Required items may produce a `Recommended` finding when a changed path lacks traceability to a relevant Plan outcome and there is concrete review or maintenance impact, or when there is concrete maintenance, compatibility, or future Plan-drift risk.
8. A small clarification or terminology improvement is `Optional` only when it has clear review value.
9. A harmless internal design, file layout, API shape, or test-style difference with compliant observable behavior is no finding.

For every finding, cite the relevant Plan section and changed path, and distinguish `Fact`, `Inference`, and `Unknown` evidence. Apply severity in order: `Must`, then `Recommended`, then `Optional`.

## Must

- A required outcome, Constraint, Out of Scope boundary, or Done When condition is `Fail` under the decision procedure.
- The implementation materially violates a stated Plan boundary; do not infer scope drift from incidental internal differences.
- A security, data-integrity, compatibility, lifecycle, or destructive requirement is `Fail`.
- Explicitly required Verification is missing, stale, non-exercising, or unproven where the Plan requires it to pass. Treat unrun or unavailable checks as `Unknown` unless the Plan explicitly requires a passing result.

## Recommended

- A named scenario, boundary, or failure behavior is satisfied but verification is unclear and it is not an explicit completion condition.
- Required items pass, but a changed path lacks traceability to a relevant Plan outcome and the gap has concrete review or maintenance impact.
- The stated outcome is met, but an implementation or integration choice creates concrete maintenance, compatibility, or future Plan-drift risk; do not flag preference alone.

## Optional

- A small Plan clarification would make a correct implementation or verification result easier to review or maintain.
- Terminology can be aligned without changing behavior, only when the alignment has clear review value.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence; identify the relevant Plan section and changed path, and distinguish observed facts from inference or unknowns. Return `No findings` when outcomes, constraints, scope, and required verification match the Plan. Do not ask questions or edit files.
