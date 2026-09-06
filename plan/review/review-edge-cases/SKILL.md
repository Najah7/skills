---
name: review-edge-cases
description: Review an implementation Plan for missing abnormal paths, failure behavior, and boundary values. Use when the user invokes $review-edge-cases or requests this specific Plan review perspective.
---

# Review Edge Cases

Review a supplied Plan without changing the Plan or code. The user decides whether to apply findings.

Require a Plan file path or Plan text. Read it completely, trace only changed or affected behavior, and inspect only relevant codebase evidence. Identify omitted input, state, failure, or boundary partitions that could change the required outcome. Report only supported findings; cite Plan locations and code paths with line numbers when available. Separate facts, inferences, and unknowns; never invent missing risks.

## Decision procedure

For each candidate case, apply these propositions in order:

- **In scope** means the case is in the Plan's changed or affected behavior, supported by the Plan or relevant code/test evidence. If false, do not report it.
- **Covered** means the Plan states the expected observable outcome and includes verification wherever the applicable rule requires it. Delegation counts only when relevant invariant, shared-component, or test evidence confirms it.
- **Finding** means `In scope` is true and `Covered` is false. If `In scope` or `Covered` is unknown, do not infer a finding; record `Unknown—insufficient evidence` only when the uncertainty materially limits the review.
- **Severity** is the highest applicable level, in this order: `Must`, then `Recommended`, then `Optional`. If no level applies, do not report the case.

## Must

- Security, authorization, data-integrity, and destructive operations define expected outcomes for denied, failed, and interrupted execution, plus verification.
- Any correctness-sensitive empty, missing, malformed, duplicate, or out-of-range input has a defined outcome when applicable.
- Numeric, size, time, retry, and lifecycle limits specify the exact boundary, behavior below and above it, and behavior at the boundary.
- Multi-step or externally visible work defines the outcome for partial failure, interruption, retry, and recovery; it must not silently leave inconsistent state.
- Each abnormal behavior required by a Done When condition appears in Verification with an observable assertion.

## Recommended

- Common validation, not-found, conflict, timeout, retry, and duplicate-operation paths are covered when the affected code can encounter them.
- Stateful operations cover repeated calls, invalid transitions, expiration, and idempotency where state or side effects make those behaviors relevant.
- Failure cases are verified at the lowest test level that can reliably observe the required outcome, with integration or E2E coverage when recovery or external state is part of the contract.
- Findings distinguish a missing requirement from a case already delegated to an existing invariant, shared component, or test suite; verify that delegation in codebase evidence.

## Optional

- Rare infrastructure faults or defensive boundaries receive coverage only when likelihood or impact justifies the cost and the Plan can observe the outcome.
- Additional examples clarify complex boundary behavior without duplicating equivalent cases or turning implementation details into requirements.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Return `No findings` when the Plan passes this review. Do not ask questions or edit files.
