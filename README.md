# Codex Agent Skills

A Codex-first personal skill library. These skills are designed and maintained for Codex's `SKILL.md` discovery and `$skill-name` invocation workflow. Other coding agents may adapt them, but Codex compatibility is the primary target.

[日本語 README](README.ja.md)

Codex-first:
- Install the skills you need with Codex's `$skill-installer`.
- Invoke a skill directly in Codex with `$skill-name`.
- `SKILL.md` contains the agent instructions; `agents/openai.yaml`, when present, provides Codex-facing UI metadata.

# Layout

Top-level directories are grouped by the work domain their skills serve:

- `plan/` covers planning, Plan review, and Plan-to-Issue work.
- `impl/` covers implementation, implementation review, and commit preparation.
- `chat/` covers conversational and communication-style skills.

`templates/` contains reusable source templates rather than invokable skills. `deprecated/` retains superseded skills for reference and is not part of the active workflow.

# Skills

## Plan

| Skill | Purpose |
| --- | --- |
| `plan-with-doc` | Create and refine an implementation Plan through a structured design interview and delegated research |
| `plan2issue` | Convert a Plan into a concise human-facing GitHub Issue and create it after repository confirmation |
| `review-plan` | Orchestrate independent Plan reviews and aggregate the read-only findings |
| `review-edge-cases` | Review a Plan for missing abnormal paths, failure behavior, and boundary values |
| `review-test-coverage` | Review a Plan for verification gaps and ineffective allocation across E2E, Integration, and Unit tests |
| `review-parallel-test` | Review whether a Plan's tests can run safely in parallel |

## Impl

| Skill | Purpose |
| --- | --- |
| `git-commit` | Review changes, stage one coherent commit, and suggest a Gitmoji Conventional Commit message without committing |
| `plan2impl` | Verify that a Plan is implementable, then execute it through tested completion |
| `review-impl` | Orchestrate independent reviews of uncommitted implementation changes |
| `review-comment` | Review comments in uncommitted changes for missing, stale, or unhelpful intent |
| `review-consistency` | Review uncommitted changes for meaningful inconsistencies with established project patterns |
| `review-depndency` | Review imports, dependencies, interfaces, and dependency-injection wiring in uncommitted changes |
| `review-kiss` | Review uncommitted changes for avoidable complexity, unnecessary abstractions, and YAGNI violations |
| `review-srp` | Review uncommitted changes for mixed file responsibilities and behavior outside its module responsibility |
| `review-ssot` | Review uncommitted changes for duplicated logic, data, configuration, and single-source-of-truth issues |
| `review-with-plan` | Review uncommitted implementation changes against a supplied Plan |

## Chat

| Skill | Purpose |
| --- | --- |
| `caveman` | Compress responses while preserving technical accuracy; supports lite, full, and ultra modes |
| `grill-me` | Interview a plan or design one decision at a time until the important branches are resolved |

# Recommended Codex workflow

```text
$plan-with-doc → $review-plan → $plan2issue
                               └→ $plan2impl → $review-impl → $git-commit
```

Use `grill-me` when a design decision needs clarification. Use an individual `review-*` skill when a single review perspective is sufficient.

# Setup

## Install for Codex

Ask Codex to install only the skills you need from this repository. For example:

```text
$skill-installer Install plan-with-doc from Najah7/skills at plan/plan-with-doc
```

You can install multiple skills in one request:

```text
$skill-installer Install these skills from Najah7/skills:
- plan/plan-with-doc
- plan/plan2issue
- impl/plan2impl
- chat/grill-me
```

Installed skills are available in a new Codex turn.

# Usage

Invoke skills from a Codex prompt.

```md
$git-commit
$plan-with-doc Add password reset
$review-plan plans/add-password-reset.md
$plan2issue plans/add-password-reset.md
$plan2impl plans/add-password-reset.md
$review-impl
```

`plan2issue` first confirms the target GitHub repository, then creates a human-facing Issue from the Plan. Use `review-plan` and `review-impl` for aggregated reviews, or an individual `review-*` skill for one perspective.

# Acknowledgements

Some skills in this project are based on or inspired by the following repositories:

- https://github.com/github/awesome-copilot
- https://github.com/JuliusBrussee/caveman
- https://github.com/mattpocock/skills
