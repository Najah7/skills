---
name: plan2impl
description: Implement an existing Plan autonomously through completion after checking that its exit conditions and safe parallelization are clear. Use when the user provides a Plan and asks to execute, implement, or finish it.
---

# Plan to Implementation

Execute an existing Plan through verified completion. Treat the Plan as the implementation contract; do not create a new Plan from scratch.

## Required Input

Require a Plan file path or the Plan text. If neither is provided, do not start implementation. Ask for the Plan once and, when useful, suggest `$plan-with-doc` for creating it.

## Preflight

Read the Plan and relevant codebase before editing. Confirm that the Plan is sufficient for autonomous execution.

### Exit Conditions

Verify that:

- completion conditions are observable and unambiguous;
- each completion condition has a test or another explicit verification method;
- required test levels and verification commands are identifiable;
- constraints and out-of-scope behavior are clear;
- no unresolved placeholder or decision can materially change the result.

### Parallelization

Determine whether work can be split into independent units. Identify prerequisites, dependencies, shared boundaries, file ownership, and the final integration path.

If exit conditions or consequential parallelization decisions remain unclear:

- investigate facts available from the Plan and codebase before asking the user;
- ask exactly one question at a time;
- provide a recommended answer and its relevant tradeoff;
- resolve prerequisite decisions before dependent ones;
- update the Plan after each answer, then continue the preflight.

Do not ask about minor implementation details that can be decided safely from existing patterns. If the Plan is already clear, begin implementation without extra ceremony.

## Plan Maintenance

Keep the Plan as the source of truth for requirements, design, and verification.

- Update it when clarification changes or completes its instructions.
- Update it when implementation reveals a necessary change to an assumption, design, or verification method.
- Do not add progress logs, task status, or completion checkboxes.
- Do not change user-visible behavior, scope, compatibility, destructive behavior, or completion conditions without user confirmation.

## Execution

Build a dependency-aware execution plan and parallelize as much as is safely useful.

- Let the main agent choose independent work units from the Plan and codebase.
- Assign a work unit and its corresponding tests to the same implementation agent.
- Give each parallel agent exclusive ownership of its files or clearly isolated subsystem.
- Never assign overlapping file edits to concurrent agents.
- Complete shared prerequisites before starting dependent parallel work.
- Keep shared infrastructure, conflict resolution, and final integration with the main agent.
- Do not force parallelism when the work is small, sequential, or tightly coupled.
- When the reason for sequential execution is clear, proceed without asking the user.

Each implementation assignment must state its scope, owned files or subsystem, dependencies, required tests, and instruction not to modify unrelated code.

## Tests

Map every completion condition to concrete verification before or during implementation.

- Prefer adding or updating tests before production code when practical.
- When practical, confirm that a new or changed test fails for the intended reason before implementing the fix.
- Allow implementation-first ordering when repository structure, parallel ownership, or safety makes it more appropriate.
- Keep tests at the levels required by the Plan.
- If a completion condition cannot be tested or otherwise verified, stop before relying on it and ask the user to define an acceptable verification method.
- Do not weaken, delete, or skip relevant tests merely to obtain a passing result.

## Replanning

When implementation invalidates a Plan assumption:

- autonomously resolve and record small differences that do not alter completion conditions;
- recompute work-unit dependencies and parallelization when needed;
- stop and ask one question when the choice affects user-visible behavior, scope, data compatibility, destructive operations, or the meaning of completion;
- stop and ask when tests contradict the Plan's stated completion conditions.

Investigate transient failures and retry when safe. If the same blocker cannot be resolved, report the evidence and remaining work without claiming completion.

## Verification and Completion

Before declaring completion:

1. Run every Verification Command specified by the Plan.
2. Run focused tests for each work unit.
3. Run affected Integration and E2E tests.
4. When practical, run relevant broader tests, linting, type checks, and builds.
5. Review the integrated diff for scope, conflicts, and alignment with the Plan.
6. Confirm every completion condition using its mapped evidence.

Fix every failure caused by the implementation. Do not expand scope to fix unrelated pre-existing failures; identify them with evidence. If required verification cannot run, state what remains unverified and do not claim full completion.

Do not invoke an independent final code-review workflow. Final review is intentionally handled outside this skill.
