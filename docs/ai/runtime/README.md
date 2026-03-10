# Runtime Pipeline

This directory contains the step-by-step execution specification for the `/next` pipeline. Each file defines one step with explicit inputs, outputs, procedures, and stop conditions.

## Execution Order

```
/next
  │
  ├─ STEP_0_BOOTSTRAP.md         Detect template state, enter bootstrap if needed
  ├─ STEP_1_RESTORE_CONTEXT.md   Read governance and project state documents
  ├─ STEP_2_REPORT_STATE.md      Output standardized status report
  ├─ STEP_3_PICK_TASK.md         Resume [-] or select next eligible [ ] task
  ├─ STEP_4_LOAD_TASK_CONTEXT.md Read task-type-specific documents
  ├─ STEP_5_EXECUTE.md           Run the task workflow with governance checks
  ├─ STEP_6_ANALYZE.md           Automatic analysis with fixed output format
  ├─ STEP_7_AUDIT.md             Automatic audit with fixed output format
  └─ STEP_8_CLOSE_TASK.md        Mark complete, update tracking, report
```

## Rules

- Execute steps in strict order. Do not skip or merge steps.
- If a step has a stop condition that triggers, halt the pipeline and report.
- Each step's output feeds into the next step's input.
- The authoritative behavioral rules are in `docs/ai/CLAUDE.md`. These steps implement those rules.

## Output Templates

Fixed output formats are in `docs/ai/templates/`:
- `STATE_REPORT.md` — used by Step 2
- `ANALYSIS_REPORT.md` — used by Step 6
- `AUDIT_REPORT.md` — used by Step 7
