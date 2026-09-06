---
name: review-plan
description: Review an implementation Plan by running the review-edge-cases, review-test-coverage, and review-parallel-test skills independently, then aggregate their read-only findings. Use when the user invokes $review-plan or requests a comprehensive Plan review.
---

# Review Plan

Run three independent Plan reviews and aggregate their results. Do not change the Plan, code, configuration, or tests. The user decides whether to apply findings.

Require a Plan file path or Plan text. If neither is provided, ask for it and stop.

## Review

1. Create one Luna-class subagent for each skill below:
   - `$review-edge-cases`
   - `$review-test-coverage`
   - `$review-parallel-test`
2. Give every subagent the same Plan and access to the relevant codebase. Tell it to use only its assigned skill, perform one read-only review turn, and return its final findings.
3. Run all three concurrently when slots permit and in waves when they do not.
4. If a subagent cannot run, do not replace its review in the main session. Mark that skill as incomplete while preserving completed results.
5. Aggregate the returned findings and present them to the user. Do not edit files or start a remediation workflow.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. Preserve each subagent's level and identify the originating skill.

For every finding include:

- Location
- Problem
- Impact
- Recommended change
- Evidence

Remove only exact duplicates. If findings conflict in content or level, retain both and identify the conflict. Do not reclassify findings, add main-agent findings, or decide which recommendations the user should apply. Include `No findings` for every completed skill with no findings and list incomplete skills.
