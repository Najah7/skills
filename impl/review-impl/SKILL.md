---
name: review-impl
description: Review uncommitted implementation changes by running the review-comment, review-consistency, review-kiss, and review-ssot skills independently, then aggregate their read-only findings. Use when the user invokes $review-impl or requests a comprehensive implementation review.
---

# Review Implementation

Run four independent implementation reviews and aggregate their results. Do not change code, configuration, tests, or documentation. The user decides whether to apply findings.

Review the repository's uncommitted changes. If there are no uncommitted changes, report that and stop. Use the user request or implementation Plan as context when provided.

## Review

1. Create one Luna-class subagent for each skill below:
   - `$review-comment`
   - `$review-consistency`
   - `$review-kiss`
   - `$review-ssot`
2. Give every subagent the same uncommitted changes and available requirement or Plan context. Tell it to use only its assigned skill, perform one read-only review turn, and return its final findings.
3. Run them concurrently when slots permit and in waves when they do not.
4. If a subagent cannot run, do not replace its review in the main session. Mark that skill as incomplete while preserving completed results.
5. Aggregate the returned findings and present them to the user. Do not edit files or start a remediation workflow.

## Output

Group findings by originating skill. For every finding include:

- Location
- Problem
- Impact
- Recommended change
- Evidence

Remove only exact duplicates. If findings conflict, retain both and identify the conflict. Do not add main-agent findings or decide which recommendations the user should apply. Include `No findings` for every completed skill with no findings and list incomplete skills.
