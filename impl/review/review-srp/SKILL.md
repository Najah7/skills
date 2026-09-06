---
name: review-srp
description: Review uncommitted changes for files with multiple responsibilities and behavior placed outside its module's responsibility.
---

# Review Single Responsibility

Review responsibilities affected by uncommitted code changes without changing code, configuration, tests, or documentation. The user decides whether to apply findings.

If there are no uncommitted changes, report that and stop. Start with the diff, then inspect only the relevant files, module contracts, neighboring implementations, consumers, and tests. Treat a responsibility as one cohesive reason to change, not one function, class, or code path. Report only evidence-supported findings, cite file paths and line numbers, and separate facts, inferences, and unknowns when material. Do not infer an SRP violation from file length, symbol count, mixed syntax, or orchestration code alone.

## Decision procedure

Evaluate each materially changed file in this order:

1. Can its primary responsibility be stated from evidenced behavior, naming, location, consumers, module contracts, or nearby project patterns?
   - Yes: continue.
   - No or unknown: no finding.
2. Does every materially changed behavior directly implement, coordinate, validate, translate, or report the outcome of that primary responsibility?
   - Yes: continue to proposition 6.
   - No: continue.
   - Unknown: no finding.
3. Is the unrelated-looking behavior only a private implementation detail required to complete the primary responsibility, with no independent policy or owner?
   - Yes: continue to proposition 6.
   - No: continue.
   - Unknown: no finding.
4. Does the behavior have an independently changing policy, actor, data ownership, lifecycle, integration boundary, or reason to change?
   - No or unknown: no finding.
   - Yes: continue.
5. Can a concrete destination or boundary be named that would own the behavior without duplicating logic, obscuring control flow, or creating unnecessary fragmentation?
   - No or unknown: no finding.
   - Yes: record a file-responsibility violation and continue to severity classification.
6. Can the containing module's responsibility be established from its public API, documentation, directory structure, dependency direction, or consistent neighboring implementations?
   - No or unknown: do not report a module-placement finding.
   - Yes: continue.
7. Does the changed behavior belong to that module responsibility?
   - Yes: no module-placement finding.
   - No: continue.
   - Unknown: no finding.
8. Is this module an evidenced composition, adapter, facade, or integration boundary whose responsibility includes coordinating the behavior?
   - Yes: no finding.
   - No: record a module-responsibility violation and continue to severity classification.
   - Unknown: no finding.
9. Classify the highest evidenced impact:
   - Incorrect behavior, security or lifecycle failure, dependency cycle, or violation of an enforced architectural boundary: `Must`.
   - Independent reasons to change or out-of-module behavior create concrete coupling, ownership, testing, or maintenance cost: `Recommended`.
   - A low-churn move to a clearly better owner materially improves cohesion or discoverability without changing behavior: `Optional`.
   - No concrete impact: no finding.

Every finding must state the file's primary responsibility, the conflicting behavior and its independent reason to change, the containing module's responsibility when relevant, the concrete impact, and the smallest appropriate destination. Do not require extraction when it would only move a few cohesive helpers, duplicate knowledge, or make the behavior harder to follow.

## Must

- A file or module combines responsibilities in a way that causes incorrect behavior, a security or lifecycle failure, a dependency cycle, or violation of an enforced architectural boundary.
- Behavior placed outside its owning module bypasses a required contract or ownership boundary and creates a concrete correctness or integration failure.

## Recommended

- A changed file owns behaviors with independently changing policies, actors, data ownership, lifecycles, integration boundaries, or reasons to change, and a concrete destination can own the secondary responsibility.
- Changed behavior falls outside the evidenced responsibility of its containing module and creates concrete coupling, ownership ambiguity, testing difficulty, or maintenance cost.
- A file mixes domain policy with unrelated infrastructure or presentation behavior when the concerns can change independently and an existing boundary can own the secondary behavior.

## Optional

- A cohesive responsibility can be moved to a clearly better existing owner with low churn and material discoverability benefit, even when no correctness or maintenance risk is present.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Evidence must identify the primary and conflicting responsibilities, their independent reasons to change, the relevant module boundary when applicable, and the proposed owner. Recommend the smallest move or extraction that restores cohesion without introducing duplication or needless indirection. Avoid duplicate findings when one misplaced responsibility affects both a file and its module. Return `No findings` when the changes pass this review. Do not ask questions or edit files.
