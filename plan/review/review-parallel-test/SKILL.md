---
name: review-parallel-test
description: Review whether tests required by an implementation Plan can run safely in parallel without order dependence or shared-state interference. Use when the user invokes $review-parallel-test or requests this specific Plan review perspective.
---

# Review Parallel Test Safety

Review a supplied Plan without changing the Plan or code. Review whether its tests are safe under the stated runner or CI execution mode (workers, shards, retries, or reruns), not whether implementation tasks can be parallelized. The user decides whether to apply findings.

Require a Plan file path or Plan text. Read it completely, then inspect only the runner configuration, fixtures, tests, and resources relevant to concurrency. Treat an unspecified execution mode as unknown, not as a defect; report only evidence-supported findings. Cite Plan locations and code paths with line numbers when available. Separate facts, inferences, and unknowns; never invent missing risks.

## Decision procedure

Apply these propositions in order. Review test execution parallelism only; do not assess whether implementation tasks can run in parallel.

1. Is a permitted execution mode with concurrent workers, processes, shards, retries, or reruns identified in the Plan or runner configuration?
   - False or unknown: `No findings`.
   - True: continue.
2. Is there evidence that the reviewed tests depend on ordering or share mutable state, including a database, file/path, queue, cache, environment variable, clock, singleton, account, port, or process-global resource?
   - False or unknown: `No findings`.
   - True: continue.
3. Is the shared state isolated per test/worker, or is the smallest safe serial scope specified with a reason?
   - True: continue to proposition 4.
   - False: `Must` if concurrent execution can produce an incorrect assertion, corrupt shared state, or leave later tests contaminated; otherwise `Recommended`.
4. Does setup and cleanup remain isolated after assertion failures, retries, timeouts, aborts, or partial setup?
   - False: `Must` when the failure can contaminate or incorrectly affect another test; otherwise `Recommended`.
   - True or unknown: continue.
5. Does the proposed command actually exercise the claimed concurrent mode?
   - False: `Must` only when the Plan claims that command proves parallel safety or requires parallel verification; otherwise `Recommended`.
   - True or unknown: continue.
6. Is there a concrete, lower-severity improvement supported by the evidence, such as unique names/paths, namespacing, mocked external state, controlled time/randomness, or a relevant parallel verification run?
   - True: `Recommended`.
   - False: continue.
7. Would a focused repeated or higher-worker run add useful detection of an intermittent race, with evidence that the extra cost is justified?
   - True: `Optional`.
   - False: `No findings`.

Never convert missing or unspecified evidence into a risk. Report only branches supported by the Plan, runner configuration, tests, fixtures, or resources.

## Must

- A `Must` finding requires a known permitted concurrent execution mode, evidence of order dependence, unsafe shared mutable state, cleanup contamination, or a command/configuration mismatch, and a consequence that can make assertions incorrect, corrupt shared state, contaminate later tests, or invalidate a required parallel-safety claim.
- A serial-only command is `Must` only when the Plan claims it establishes parallel safety or requires parallel verification; otherwise classify it as `Recommended`.

## Recommended

- A `Recommended` finding requires known permitted concurrency and a concrete, evidence-supported isolation or verification gap that does not meet the `Must` consequence threshold, such as missing unique resource names, namespacing, mocks, controlled time/randomness, or relevant parallel-mode verification.

## Optional

- An `Optional` finding is limited to an evidence-supported proposal for additional repeated or higher-worker execution after no `Must` or `Recommended` finding exists, where the extra cost is justified by intermittent-race risk.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Return `No findings` when the Plan passes this review. Do not ask questions or edit files.
