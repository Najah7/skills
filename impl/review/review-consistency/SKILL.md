---
name: review-consistency
description: Review uncommitted changes for meaningful inconsistencies with established project patterns.
---

# Review Consistency

Review uncommitted implementation changes without changing code, configuration, tests, or documentation. The user decides whether to apply findings.

If there are no uncommitted changes, report that and stop. Start with the diff, then actively find the smallest relevant set of existing implementations that solve the same responsibility or use case. Compare their structure, behavior, lifecycle, failure handling, integration boundaries, and tests. The default rule is: the same responsibility under materially the same constraints should follow the established structural pattern. A new pattern requires evidence that the difference is necessary.

Report only evidence-supported inconsistencies, cite changed and reference locations with file paths and line numbers, separate facts, inferences, and unknowns when material, and suggest the smallest aligned change. Treat formatting or naming differences as findings only when they impair correctness, maintenance, or discoverability. Do not report intentional or requirement-driven deviations merely because they differ from existing code.

## Pattern Comparison

Evaluate each materially changed responsibility independently:

1. Is there an existing implementation of the same responsibility or use case?
   - No: allow a new pattern.
   - Yes: continue.
2. Are its requirements, constraints, boundaries, and lifecycle materially comparable?
   - No: allow a different implementation and state the relevant difference when needed.
   - Yes: continue.
3. Does the changed code follow the same structural pattern and conventions?
   - Yes: pass this check.
   - No: continue.
4. Is the deviation necessary according to requirements, code constraints, or another explicit source of evidence?
   - Yes: treat it as a justified deviation.
   - No or unknown: report the inconsistency.

Compare only dimensions relevant to the responsibility: layer and responsibility split, API or function shape, data flow, state and lifecycle, validation and error handling, side effects, dependency injection and extension points, naming and location, and test or fixture structure. Similar syntax alone does not make two implementations comparable; different syntax alone does not make their patterns inconsistent.

## Must

- A changed public API, error contract, data contract, security behavior, or lifecycle contract conflicts with an established contract without an explicit migration or justification.
- A changed integration, state transition, or failure-handling convention can cause incorrect behavior, data loss, or break a supported caller.

## Recommended

- Error handling, logging, cleanup, validation, and documentation preserve established behavior where callers or operators rely on it.
- Code solving the same responsibility under materially the same constraints follows the established structural pattern. Report an unsupported new pattern even when it does not yet break a contract, because it creates an unnecessary second way to perform the same task.
- Established APIs and extension points are reused when they fit the current requirement; deviations have concrete evidence that the established mechanism is insufficient.
- Naming, structure, and organization match relevant nearby patterns when the difference impairs discoverability or makes the implementation easy to misuse.

## Optional

- Local naming or organization differences are aligned when doing so improves discoverability without obscuring the change or creating churn.
- A small consistency improvement is suggested only when its evidence and benefit are clear; otherwise report `No findings`.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence; identify the established reference pattern and explain why the deviation matters. Keep findings specific to the changed implementation, avoid style-only preferences and duplicate findings, and return `No findings` when the changes pass this review. Do not ask questions or edit files.
