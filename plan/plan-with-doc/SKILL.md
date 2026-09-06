---
name: plan-with-doc
description: Create and iteratively refine an implementation Plan file through a one-question-at-a-time design interview and delegated codebase research. Use when the user invokes $plan-with-doc or asks to create a documented implementation plan before coding.
---

# Plan with Doc

Create a Plan document, refine it with the user, and stop before implementation.

## Required Resources

Read [TEMPLATE.md](references/TEMPLATE.md) and [EXAMPLE.md](references/EXAMPLE.md) before creating the Plan. Use the template as the required document structure and the example to calibrate content and test-case granularity.

## Boundaries

- Create and update the Plan only. Implementation is out of scope.
- Do not change source code, configuration, dependencies, or tests.
- The main agent may directly read the files specified by the user, this skill's resources, and the Plan it creates.
- Delegate all other codebase investigation to research subagents. Do not silently replace delegated research with main-agent investigation.

## Workflow

1. Resolve the Plan location:
   - Use a path supplied by the user without additional discovery.
   - Otherwise, use delegated research to find and follow an existing repository convention.
   - If no convention exists, use `<repo-root>/plans/<goal-in-kebab-case>.md`.
   - If the target already exists, ask before overwriting it.
2. Immediately create the Plan from [TEMPLATE.md](references/TEMPLATE.md). Populate only facts supported by the user's request or delegated research; mark unresolved decisions clearly instead of guessing.
3. Interview the user about unresolved design decisions:
   - Ask exactly one question at a time.
   - Provide a recommended answer and its relevant tradeoff.
   - Resolve prerequisite decisions before dependent ones.
   - If the answer is discoverable from the codebase, delegate research instead of asking the user.
   - After every answer or material research result, update the Plan before asking the next question.
4. Continue until:
   - Goal and Background are sufficient for implementation planning.
   - Consequential design branches are resolved.
   - Constraints and Out of Scope are explicit.
   - Required E2E, Integration, and Unit coverage is specified.
   - No unresolved item remains unless explicitly deferred or excluded.
5. Check that the completed Plan follows the template, contains no unintended unresolved items, aligns verification with requirements and design, and keeps every Done When item observable. Fix confirmed issues, present the Plan, and stop.

## Delegated Research

- Use a Luna-class subagent first for codebase investigation.
- Run independent, bounded investigations in parallel when useful.
- Escalate the same bounded investigation to a Terra-class subagent when Luna cannot establish the answer, returns insufficient evidence, or reports conflicting evidence.
- If no suitable research subagent is available, wait or tell the user that research is blocked. The main agent must not perform the investigation itself.
- Research subagents must not modify files.

Include these requirements in every research assignment:

```text
Report only claims supported by evidence.
For each material claim, cite the file path and line number.
Separate verified facts, inferences, and unknowns.
If the evidence is insufficient, say that the answer is unknown.
Do not invent missing details or present assumptions as facts.
Do not make design decisions or modify files.
Stay within the assigned investigation scope.
```
