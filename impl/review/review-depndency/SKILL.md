---
name: review-depndency
description: Review uncommitted changes for unnecessary or misused imports, dependencies, interfaces, and dependency-injection wiring.
---

# Review Dependencies

Review dependencies affected by uncommitted code changes without changing code, configuration, tests, or documentation. The user decides whether to apply findings.

If there are no uncommitted changes, report that and stop. Start with the diff, then inspect only the relevant imports, consumers, interfaces, implementations, composition roots, container bindings, and tests. Evaluate each added or changed dependency edge independently. Report only evidence-supported findings, cite file paths and line numbers, and separate facts, inferences, and unknowns when material. Do not require dependency injection or an interface when direct construction is appropriate.

## Decision procedure

For each added or changed import, constructed, injected, or resolved dependency, interface, and binding, apply these propositions in order:

1. Does the dependency provide a referenced value or type, or an evidenced registration or initialization side effect required by the changed behavior?
   - Yes: continue.
   - No: the dependency is unnecessary; continue to severity classification.
   - Unknown: no finding.
2. Does the dependency serve a current requirement of this consumer?
   - Yes: continue.
   - No: the dependency is unnecessary; continue to severity classification.
   - Unknown: no finding.
3. Does its direction and import source respect an evidenced module, layer, ownership, or public-API boundary?
   - Yes or not applicable: continue.
   - No: continue to severity classification.
   - Unknown: no finding.
4. Does this dependency require substitution, ownership inversion, container-managed lifetime, or an established DI boundary?
   - No: direct construction is acceptable; skip to proposition 7.
   - Yes: continue.
   - Unknown: no finding.
5. Is it obtained through the established composition boundary instead of hidden construction, global lookup, or service location inside business logic?
   - Yes: continue.
   - No: continue to severity classification.
   - Unknown: no finding.
6. Does the consumer depend only on the declared contract, and does the configured implementation satisfy that contract with a compatible lifetime and scope?
   - Yes: continue.
   - No: continue to severity classification.
   - Unknown: no finding.
7. If an interface or DI indirection is introduced, is it justified by at least one evidenced need: multiple implementations, substitution at a real test or system boundary, ownership inversion, lifecycle management, or an established project extension point?
   - Yes or not applicable: no finding.
   - No: the indirection is unnecessary; continue to severity classification.
   - Unknown: no finding.
8. Classify the highest evidenced impact:
   - Incorrect behavior, broken build or runtime resolution, dependency cycle, security or architectural-boundary violation, incompatible contract, or unsafe lifetime: `Must`.
   - Unused or unnecessary dependency, bypassed established DI boundary, unjustified service location or indirection, overly broad contract, or concrete maintenance and testing cost: `Recommended`.
   - A correct dependency can be narrowed or aligned with low churn and clear discoverability value, without changing behavior: `Optional`.
   - No concrete impact: no finding.

Every finding must identify the dependency edge, its consumer, the evidence that it is unnecessary or inappropriate, its concrete impact, and the smallest correction. Do not infer misuse from a concrete dependency, single implementation, side-effect import, or lack of an interface alone.

## Must

- A dependency or binding causes incorrect behavior, failed build or runtime resolution, an import cycle, or a security, lifecycle, or enforced architectural-boundary violation.
- An injected implementation violates its declared contract, or its configured lifetime or scope can expose invalid, stale, or cross-request state.
- Hidden construction or lookup bypasses a required boundary and causes a concrete correctness, lifecycle, or integration failure.

## Recommended

- An import, constructor parameter, injected value, interface, binding, or dependency is unused or does not serve a current consumer requirement.
- Code bypasses an established composition boundary without evidence that the exception is necessary, creating concrete coupling, testing, or maintenance cost.
- A consumer downcasts, checks implementation types, or otherwise depends on details outside its declared contract.
- An interface exposes substantially more capability than the consumer needs, or DI indirection lacks an evidenced substitution, ownership, lifecycle, boundary, or extension-point purpose and creates concrete cost.

## Optional

- A correct dependency or contract can be narrowed or aligned with an established import or injection point when the change is low-churn and materially improves discoverability.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Evidence must identify both the dependency and its consumer, plus the relevant contract, binding, boundary, or current requirement. Recommend the smallest correction, such as removing the dependency, using the established import or composition boundary, narrowing the contract, or correcting the binding or lifetime. Avoid duplicate findings for the same dependency edge. Return `No findings` when the changes pass this review. Do not ask questions or edit files.
