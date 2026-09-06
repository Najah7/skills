---
name: review-kiss
description: Review uncommitted changes for avoidable complexity, unnecessary abstractions, and YAGNI violations.
---

# Review KISS

Review uncommitted changes without changing code, configuration, tests, or documentation. The user decides whether to apply findings.

If there are no uncommitted changes, report that and stop. Compare added complexity with the current requirement, changed behavior, and nearby project patterns. Report only evidence-supported YAGNI or avoidable-complexity findings; do not treat unfamiliar, abstract, or lengthy code as a problem by itself. Cite file paths and line numbers, separate facts, inferences, and unknowns when material, and suggest a smaller concrete alternative only when it preserves the requirement.

## Decision procedure

Evaluate each suspected complexity separately:

1. Identify the current required behavior, contract, constraint, or caller need.
   - `No` or `Unknown`: no finding.
2. Is the added abstraction, branch, state, dependency, configuration, or extension point necessary for that requirement?
   - `Yes` or `Unknown`: no finding.
   - `No`: continue.
3. Is there a concrete complexity delta compared with the prior implementation or an existing project pattern?
   - `No`: no finding.
4. Can you name a smaller alternative that preserves all required behavior, contracts, edge cases, and side-effect ordering?
   - `No`: no finding.
5. Assign severity only from evidenced impact:
   - `Must`: correctness, lifecycle, performance, security, or integration impact.
   - `Recommended`: maintenance, testing, reasoning, or duplication impact, or cost from unneeded behavior or configuration.
   - `Optional`: a clearly equivalent, low-churn simplification with no material risk.
   - No concrete effect: no finding.

Each finding must state the current requirement, concrete impact, and smaller alternative that preserves the requirement. Do not use code length, unfamiliarity, abstraction alone, or hypothetical future reuse as evidence. If the requirement, callers, project pattern, or impact cannot be verified from available repository evidence, treat it as `Unknown` and do not report a finding or invent evidence.

## Must

- Complexity that is not necessary for the current requirement creates an evidence-supported correctness, lifecycle, performance, security, or integration risk, and a smaller behavior-preserving alternative is available.
- New behavior, configurability, extensibility, or infrastructure exceeds the stated requirement, creates a concrete failure risk, and can be removed without changing required behavior.
- Complexity duplicates or conflicts with an existing mechanism or established project pattern, with a concrete resulting risk and no requirement that justifies the difference.

## Recommended

- Unneeded features, abstractions, configuration, or extension points have no current requirement or demonstrated caller need, create a concrete maintenance, testing, or reasoning cost, and can be deferred or removed while preserving behavior.
- Unnecessary branching, state, indirection, or control flow can be replaced by a smaller implementation with the same required behavior and materially lower reasoning or maintenance cost.
- Coupled business logic and external side effects create a concrete testing, modification, or failure-handling risk, and separation preserves side-effect ordering and required behavior.
- A smaller existing utility or project convention satisfies the requirement and avoids a concrete duplication or maintenance risk without obscuring intent.

## Optional

- Equivalent code can be made smaller or clearer with low churn and no material risk; report only when the improvement is concrete, not as a style preference.
- A local abstraction has one trivial caller, no demonstrated reuse, and a smaller behavior-preserving replacement is available; do not flag deliberate ownership or testing boundaries.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Explain which current requirement fails to justify the complexity and why the proposed smaller alternative preserves required behavior. Do not report style preferences, hypothetical future reuse, or complexity with no concrete risk. Return `No findings` when the changes pass this review. Do not ask questions or edit files.
