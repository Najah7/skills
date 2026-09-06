---
name: review-test-coverage
description: Review an implementation Plan for missing verification and ineffective allocation across E2E, Integration, and Unit tests. Use when the user invokes $review-test-coverage or requests this specific Plan review perspective.
---

# Review Test Coverage

Review a supplied Plan's verification design without changing the Plan or code. The user decides whether to apply findings.

Require a Plan file path or Plan text. Read it completely, inspect only relevant implementation and test evidence, and report only supported findings. Cite Plan locations and code paths with line numbers when available. Separate facts, inferences, and unknowns; never infer missing coverage from absent documentation alone.

## Classification

Classify each behavior independently by answering these questions in order:

1. Does proving the expected outcome require exercising a real system or domain boundary?
   - `No`: Unit.
   - `Yes`: continue to question 2.
2. Does proving the expected outcome require the complete user-facing path from entry point to final observable result?
   - `No`: Integration.
   - `Yes`: E2E.
3. Is it a critical user journey or a high-impact failure path?
   - `No`: keep coverage at the lowest sufficient level selected above.
   - `Yes`: keep detailed cases at the lowest sufficient level and add one narrow E2E scenario only when it verifies a distinct end-to-end risk.

A system or domain boundary includes collaboration between independently owned components, domains, or modules; persistence and transactions; APIs and serialization; processes; queues and events; filesystems; caches; framework routing, middleware, and dependency wiring; and external services. A mocked call does not prove the real boundary contract. If replacing collaborators preserves the complete claim being tested, classify that claim as Unit.

## Must

- Every behavior in Done When and Verification maps to an explicit, executable check with an observable expected outcome.
- Every behavior is assigned using the Classification questions; a different level requires evidence that the selected level cannot prove the expected outcome.
- A journey whose correctness requires the complete user-facing path has E2E coverage; do not require E2E for behavior fully observable below that path.
- Behavior whose correctness requires a real system or domain boundary has Integration coverage; mocks alone do not verify that boundary.
- Behavior fully provable within one unit has Unit coverage when direct verification is required.
- No required behavior is covered only at a level that cannot observe its claimed outcome, and no proposed test level is treated as coverage for behavior outside its boundary.

## Recommended

- Each behavior is primarily tested at the lowest reliable level; higher-level checks are called out only when they verify a distinct boundary or user-visible contract.
- E2E coverage names the critical journey and externally observable result, rather than duplicating unit cases through the UI.
- Integration coverage identifies the real system or domain boundary and its concrete success, failure, or state outcome.
- Unit coverage identifies the input class and output or error assertion when branch behavior is material.
- The Plan distinguishes existing tests to update, new tests to add, and verification that is already present.

## Optional

- High-risk behavior has limited defense-in-depth coverage across levels when each level detects a distinct failure class.
- Closely related cases are consolidated when doing so preserves diagnostic clarity and does not hide a required boundary or outcome.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Return `No findings` when the Plan passes this review. Do not ask questions or edit files.
