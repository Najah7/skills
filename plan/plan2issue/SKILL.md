---
name: plan2issue
description: Convert an implementation Plan into a concise human-facing GitHub Issue and create it after confirming the target repository. Use when the user supplies a Plan and asks to publish it as an Issue.
---

# Plan to GitHub Issue

Convert a supplied implementation Plan into a human-readable GitHub Issue. Do not review, correct, or modify the Plan. The responsibility of this skill begins with abstraction and ends with Issue creation.

## Boundaries

- Require a Plan file path or Plan text. Read it completely without assessing its format, completeness, test coverage, or implementation quality.
- Make a best effort to create the Issue from any usable Plan. Stop as invalid only when the input is blank or no goal can reasonably be identified without invention.
- Confirm only the target GitHub repository. After approval, do not ask the user to review the title, body, labels, or other content before creation.
- Default the Issue title and body to English. Use Japanese when the user explicitly requests Japanese.
- Do not implement the Plan, edit repository files, or invoke a Plan-review workflow.

## Workflow

1. Resolve the target repository from an explicit user selection or the current repository's GitHub remote. Verify it read-only and immediately ask the user to confirm the exact `owner/repo`. Do not create or modify anything before this confirmation.
2. After confirmation, read the Plan and identify its goal. If the Plan is blank or no goal can reasonably be established, report that an Issue cannot be created and stop. Do not reject it for any other formatting or completeness problem.
3. Generate a concise outcome-oriented title from the Goal. Do not add a fixed prefix or describe the implementation mechanism.
4. Produce the Issue body in the order below. Preserve requirement meaning, remove implementation-only detail, and omit an optional section when no supported content exists rather than adding filler.
5. Infer labels from direct Plan evidence, reuse matching existing labels, and create required missing labels as described below.
6. Search open Issues in the confirmed repository before creating anything. Treat an exact title match or clearly equivalent Goal as a duplicate. If a clear duplicate exists, do not create an Issue or labels; return its URL. Similarity alone is insufficient—when equivalence is uncertain, continue.
7. Create any missing selected labels, then create the Issue. Return its number and URL. If creation fails after a label was created, report the partial mutation and error; before retrying, repeat the duplicate check to avoid creating two Issues.

## Issue Body

Use these sections: @TEMPLATE.md

Transform the Plan as follows:

- **Goal:** State the intended human-visible or system-visible outcome concisely.
- **Background:** Preserve context, motivation, current behavior, and relevant decisions. Remove details useful only to an implementing agent.
- **Requirements:** Preserve the substance of Requirement sections and Constraints. Use concise bullets, merge duplicates, and retain important security, compatibility, lifecycle, and data-integrity conditions.
- **High-level Design:** Summarize the proposed components, boundaries, and behavior flow. Omit file paths, symbols, exact APIs, implementation order, internal algorithms, and step-by-step coding instructions unless they are themselves externally required constraints.
- **Acceptance Criteria:** Convert Done When and Verification into a short list of observable outcomes. Remove test levels, test paths, test names, fixtures, mocks, commands, GIVEN/WHEN/THEN formatting, and descriptions of how tests will be implemented. Merge equivalent criteria without weakening them.
- **Out of Scope:** Preserve explicit exclusions without expanding them.

Do not copy the Plan verbatim. Do not invent requirements, redesign the solution, or silently discard a requirement because it is technical. Translate technical detail into its human-relevant constraint or outcome when one exists.

## Labels

Apply every supported surface label:

- `frontend` for user-interface, browser, client, or other frontend behavior.
- `backend` for server, API, application or domain logic, persistence, or backend processing.
- `infra` for deployment, CI/CD, cloud, networking, runtime platform, or operational infrastructure.

Apply every directly affected domain as `domain:<kebab-case>`. Reuse an existing matching `domain:*` label when available. Use multiple domain labels when the Plan directly affects multiple domains, including an existing domain touched by a new feature. Use `domain:shared` for common foundations or cross-domain shared infrastructure. If no domain can be supported by the Plan, omit the domain label instead of guessing or creating `domain:unknown`.

Create any selected label that is missing, including `frontend`, `backend`, `infra`, and `domain:*`. Preserve existing label metadata. For a new label, follow an evidenced repository color and description convention when one exists; otherwise use a stable neutral color and a concise description of the label's scope. Do not create unused labels.

## GitHub Operations

- Use available authenticated GitHub tooling and always target the confirmed `owner/repo` explicitly for reads and writes.
- Verify repository access before asking for confirmation. If authentication, repository resolution, or required permissions fail, report the error and stop without mutation.
- Search only open Issues for duplication and cite the existing Issue when creation is skipped.
- Do not assign an assignee or milestone. Do not apply labels other than the inferred surface and domain labels unless the user explicitly requested them.
- After repository confirmation, proceed through transformation, duplicate detection, label creation, and Issue creation without further content confirmation.

## Output

On success, return the confirmed repository, Issue title, applied labels, Issue number, and URL. For a duplicate, return the repository, existing Issue title, number, and URL. For failure, state the exact blocking reason and any partial external mutation. Do not output the full Issue body unless the user asks for it after creation.
