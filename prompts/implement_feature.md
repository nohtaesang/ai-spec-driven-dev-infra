# Prompt Template: Implement Feature

## Context

- **Feature**: [Name of the feature]
- **Task ID**: [TASK-NNN from TASKS.md]
- **Target module(s)**: [e.g., core, data layer]
- **Related design doc**: [e.g., docs/model/DATA_MODEL.md]

## Requirements

[Copy the specific requirements from the design document or TASKS.md]

## Constraints

Before implementing, verify:

1. [ ] Does not contradict SPEC.md
2. [ ] All domain types used are in DEFINITIONS.md
3. [ ] Module/crate boundaries respected (see `docs/process/ARCHITECTURE_GUARDRAILS.md`)
4. [ ] Performance guardrails not violated (project-defined)
5. [ ] No non-goal conflicts

## Scope

- **Do**: [What to build]
- **Do not**: [What to avoid]

## Acceptance Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] Definition of Done checklist passes (see `docs/process/DEFINITION_OF_DONE.md`)

## Post-Implementation

1. Run `/check` to validate against infrastructure rules
2. Review change impact checklist (`docs/process/CHANGE_IMPACT_CHECKLIST.md`)
3. Update TASKS.md
4. Create ADR if any architectural decisions were made
