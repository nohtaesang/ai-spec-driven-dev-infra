# STEP 3: Pick or Resume Task

## Purpose

Determine which task to work on. Resume an in-progress task, or select the next eligible task.

## Required Reads

- `docs/project/TASKS.md`
- `docs/ai/GOVERNANCE_CHECKS.md`

## Procedure

1. If a task is `[-]` → **resume it**. Read its `progress:` field to understand what was already done. Do not start another.
2. If more than one `[-]` task exists → **stop and report violation**. This is a governance failure.
3. If no task is `[-]` → select the next `[ ]` task where:
   - All `depends:` are `[x]`.
   - It appears earliest in the active phase.
4. Set the selected task to `[-]` in `TASKS.md`.
5. Write `progress: started` immediately. Save **before any other work**.

## Handling `/next <request>`

When the user provides a request alongside `/next`:

1. **Classify the request** as one of:
   - **(a) Continuation** — relates to the `[-]` task → incorporate the input and continue from Step 4.
   - **(b) New task** — does not conflict → create a new task in `TASKS.md` (next sequential ID, determine `type:` and `phase:`, identify dependencies, insert at end of appropriate phase). If no task is `[-]` and dependencies are met, start it. If a task is already `[-]`, ask the user: finish current first, or abandon and switch?
   - **(c) Conflict** — contradicts SPEC.md, NON_GOALS.md, ADRs, extension boundary, plans, scope, or architecture → **stop and report** the conflict with document references. Do not proceed.

## Outputs

- Active task identified (TASK-NNN)
- TASKS.md updated with `[-]` status and `progress: started`

## Stop Conditions

- More than one `[-]` task exists → **stop and report**.
- `/next <request>` classified as conflict → **stop and report**.
- No eligible task found → **report** and wait for user direction.
