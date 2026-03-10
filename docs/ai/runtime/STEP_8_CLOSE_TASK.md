# STEP 8: Close Task

## Purpose

Mark the task complete, update all tracking documents, and report the outcome.

## Required Reads

- `docs/project/TASKS.md`
- `docs/project/DONE.md`
- `docs/project/DECISIONS.md`
- `docs/project/PROJECT_STATE.md`
- `docs/ai/GOVERNANCE_CHECKS.md`

## Pre-Close Checks

Confirm all items in `docs/process/DEFINITION_OF_DONE.md` are satisfied. At minimum:

- Step 6 (analysis) passed — no FAIL results.
- Step 7 (audit) passed — status is green or yellow (not red).

`DEFINITION_OF_DONE.md` is the authoritative checklist. Do not close the task if any required item is unsatisfied.

If any check fails → **stop and report**. Do not close the task.

## Procedure

1. Set the task to `[x]` in `TASKS.md`. Remove the `progress:` field.
2. Append to `DONE.md`: `- [x] TASK-NNN: Name (YYYY-MM-DD)`
3. If the task produced a decision:
   - Create ADR file in `docs/project/decisions/`.
   - Update `DECISIONS.md` index.
4. Check if any `[!]` BLOCKED tasks are now unblocked → set to `[ ]`.
5. Update `docs/project/PROJECT_STATE.md`:
   - Current Phase and Current Focus (if changed)
   - What Changed Recently (prepend the completed task)
   - Active Risks (add or resolve as appropriate)
   - Next Likely Decisions (update based on upcoming work)
   - Next Session Start (instructions for the next `/next` invocation)
6. Report:
   - What was completed
   - Analysis summary
   - Audit status
   - Next eligible task

## Outputs

- TASKS.md updated (`[x]`)
- DONE.md entry appended
- ADR file and DECISIONS.md updated (if applicable)
- Blocked tasks unblocked (if applicable)
- PROJECT_STATE.md updated
- Completion report to user

## Stop Conditions

- Analysis failed (Step 6 had FAIL) → **do not close**
- Audit failed (Step 7 was red) → **do not close**
- Required ADR missing → **do not close**
- DONE.md update missing → **do not close**
