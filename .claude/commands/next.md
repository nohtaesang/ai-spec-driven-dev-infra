# /next — Primary Workflow Command

`/next` is the primary command for all project work. It runs the full workflow pipeline automatically.

## Authoritative Sources

- **Behavioral rules**: `docs/ai/CLAUDE.md`
- **Pipeline steps**: `docs/ai/runtime/STEP_*.md`
- **Governance checks**: `docs/ai/GOVERNANCE_CHECKS.md`
- **Output templates**: `docs/ai/templates/`

## Pipeline

Execute these steps in strict order. Do not skip or merge steps. If a step triggers a stop condition, halt and report.

1. Read `docs/ai/runtime/STEP_0_BOOTSTRAP.md` — if bootstrap is needed, run it and stop.
2. Read and execute `docs/ai/runtime/STEP_1_RESTORE_CONTEXT.md`
3. Read and execute `docs/ai/runtime/STEP_2_REPORT_STATE.md`
4. Read and execute `docs/ai/runtime/STEP_3_PICK_TASK.md`
5. Read and execute `docs/ai/runtime/STEP_4_LOAD_TASK_CONTEXT.md`
6. Read and execute `docs/ai/runtime/STEP_5_EXECUTE.md`
7. Read and execute `docs/ai/runtime/STEP_6_ANALYZE.md`
8. Read and execute `docs/ai/runtime/STEP_7_AUDIT.md`
9. Read and execute `docs/ai/runtime/STEP_8_CLOSE_TASK.md`

## `/next` (no arguments)

Runs all steps. Selects the next eligible task automatically.

## `/next <request>`

Steps 1–2 run normally. Then the request is classified per `docs/ai/runtime/STEP_3_PICK_TASK.md`:

- **(a) Continuation** — relates to current `[-]` task → continue from Step 4.
- **(b) New task** — no conflict → add to `TASKS.md`. If no `[-]` and deps met, start. If `[-]` exists, ask user.
- **(c) Conflict** — contradicts SPEC.md, NON_GOALS.md, ADRs, or plans → stop and report.

---

## Related Commands

| Command | Purpose |
|---|---|
| `/next` | **Primary.** Run the full pipeline for the next task. |
| `/pick` | Evaluate a proposal and decide whether to adopt it. |
| `/idea` | Evaluate a new idea before it enters the task system. |
| `/check` | Validate recent changes against infrastructure rules. |
| `/critic` | Challenge a design or proposal with strong skepticism. |
| `/audit` | Full project-level system audit (milestone use). |
