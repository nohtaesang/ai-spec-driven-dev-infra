# STEP 8: Close Task

## Purpose

Mark the task complete, update all tracking documents, and report the outcome.

## Required Reads

- `docs/project/TASKS.md`
- `docs/project/DONE.md`
- `docs/project/DECISIONS.md`
- `docs/ai/GOVERNANCE_CHECKS.md`

## Pre-Close Checks

Before closing, confirm against `docs/process/DEFINITION_OF_DONE.md`:

1. Step 6 (analysis) passed — no FAIL results.
2. Step 7 (audit) passed — status is green or yellow (not red).
3. If the task produced a decision, an ADR file exists.
4. All new domain terms are registered in DEFINITIONS.md.
5. Change impact checklist reviewed (`docs/process/CHANGE_IMPACT_CHECKLIST.md`).
6. For `implement` tasks: build passes, tests pass, no new lint violations.

If any check fails → **stop and report**. Do not close the task.

## Procedure

1. Set the task to `[x]` in `TASKS.md`. Remove the `progress:` field.
2. Append to `DONE.md`: `- [x] TASK-NNN: Name (YYYY-MM-DD)`
3. If the task produced a decision:
   - Create ADR file in `docs/project/decisions/`.
   - Update `DECISIONS.md` index.
4. Check if any `[!]` BLOCKED tasks are now unblocked → set to `[ ]`.
5. Report:
   - What was completed
   - Analysis summary
   - Audit status
   - Next eligible task

## Outputs

- TASKS.md updated (`[x]`)
- DONE.md entry appended
- ADR file and DECISIONS.md updated (if applicable)
- Blocked tasks unblocked (if applicable)
- Completion report to user

## Stop Conditions

- Analysis failed (Step 6 had FAIL) → **do not close**
- Audit failed (Step 7 was red) → **do not close**
- Required ADR missing → **do not close**
- DONE.md update missing → **do not close**
