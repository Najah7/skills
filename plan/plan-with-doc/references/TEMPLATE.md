# Goal (Requirement)

<!--
Describe the desired outcome.
This section is primarily written by the user.
The structure is flexible.
-->

# Background (Requirement)

<!--
Provide relevant context, motivation, current behavior, known problems,
and decisions that affect the implementation.
The structure is flexible.
-->

# Implementation (Design)

<!--
Describe the proposed implementation based on the requirements.
The structure is flexible.
-->

## Details

## Order

## Constraints

## Out of Scope

# Verification

<!--
General rules:

- "Update" lists existing tests that must be changed.
- "New" lists behaviors that require new tests.
- Add one block or bullet for each independently testable behavior.
- Add as many blocks or bullets as needed. Sections are not limited to one test.
- Do not combine unrelated behaviors into one test.
- Describe externally observable behavior instead of implementation details.
- Write "None — <reason>" when a section does not apply.
-->

## E2E Tests — Critical User Journeys Only

<!--
Cover only critical journeys through the real UI or external interface.

Include successful and failure scenarios when they are important to the user
journey. Do not use E2E tests for behavior that can be sufficiently verified at
a lower level.
-->

### Update

<!-- Add one bullet for every existing test to update. -->

- `path/to/test::test_name` — <required change>

### New

<!-- Repeat the following block for every new E2E scenario. -->

#### Scenario: <short descriptive name>

- GIVEN ...
- WHEN ...
- THEN ...
- AND ... <!-- Optional -->

<!-- Add more Scenario blocks as needed. -->

## Integration Tests

<!--
Cover behavior involving multiple components, persistence, APIs, or other
system boundaries.

- Write one independently testable use case per bullet.
- Describe the starting state and action on the left.
- Describe all observable outcomes on the right.
- Outcomes may include returned values, errors, persisted state, or emitted
  events.
- Do not describe internal calls or mocks.
-->

### Update

<!-- Add one bullet for every existing test to update. -->

- `path/to/test::test_name` — <required change>

### New

<!-- Add one bullet for every new integration test case. -->

- <starting state and action> -> <observable outcome>

## Unit Tests

<!--
Cover deterministic input-to-output behavior of individual units.

- Write one test case per bullet using natural-language input -> output form.
- Treat errors as outputs.
- Add as many test cases as needed.
- Use concrete values when they matter.
- Behavior involving side effects or system boundaries belongs in Integration
  Tests.
-->

### Update

<!-- Add one bullet for every existing test to update. -->

- `path/to/test::test_name` — <required change>

### New

<!-- Add one bullet for every new unit test case. -->

- <input or condition> -> <output or error>

# Done When

<!--
List observable conditions that must be satisfied for this work to be
considered complete.

Describe outcomes, not implementation steps or test procedures.
-->

- ...
