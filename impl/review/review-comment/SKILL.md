---
name: review-comment
description: Review uncommitted code changes for comments that obscure, repeat, or omit useful intent.
---

# Review Comments

Review comments affected by uncommitted code changes, especially added or changed comments and comments made stale by the implementation. Do not edit code, configuration, tests, or documentation; the user decides whether to apply findings.

If there are no uncommitted changes, report that and stop. Inspect relevant nearby code as needed. Report only findings supported by the comment, its code, or repository context, citing file paths and line numbers. Separate facts, inferences, and unknowns when material. Do not require comments for self-explanatory code.

## Decision procedure

For each comment affected by the uncommitted changes, evaluate these checks in order:

1. Is the comment false, contradictory, or stale relative to the changed implementation? If yes, flag **Must**. Unknown is not stale; do not flag without evidence.
2. Does the changed code contain a non-obvious decision, constraint, or behavior that could cause incorrect maintenance or use? If yes and the rationale is absent, flag **Must**. If rationale is present, continue. If unknown, do not flag. Do not require comments for self-explanatory code.
3. Does the comment merely restate nearby code? If yes, flag **Recommended** only when it adds no intent, constraint, or non-obvious maintenance value. Otherwise, do not flag; unknown maintenance value is not enough.
4. Is the comment correct but materially harder to understand because of wording or placement? If yes, flag **Optional**. Style preferences or unknown concerns are not findings.

Stop at the first applicable severity and report only the highest severity for each distinct problem.

## Must

- Misstate behavior, contradict the code, or are stale relative to the changed implementation; unknown is not stale.
- Omit rationale for an evidenced non-obvious decision, constraint, or behavior when the missing context could plausibly cause incorrect maintenance or use.

## Recommended

- Merely restate nearby code without explaining intent, a constraint, or a non-obvious behavior, when the repetition adds no maintenance value; unknown value is not enough.

## Optional

- Improve wording or placement when a correct comment is materially harder to understand for that reason; style preferences or unknown concerns are not findings.

Q/A style: use only when it makes a substantial rationale easier to understand; do not introduce it for routine comments.

```
// Q: Why implement this function this way?
// A: It follows the existing pattern and keeps the behavior consistent.
// Ref: UserProfileService
```

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Return `No findings` when the changes pass this review. Do not ask questions or edit files.
