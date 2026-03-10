# STEP 2: Report State

## Purpose

Output a standardized status report so the user and future sessions can understand the current project state at a glance.

## Required Reads

All documents from Step 1 (already loaded).

## Procedure

1. Determine active phase, last completed task, in-progress task, and next eligible task.
2. Run a quick scan for conflicts (SPEC, non-goals, assumptions, ADRs, inconsistencies).
3. Output the report using the exact format from `docs/ai/templates/STATE_REPORT.md`.

## Output Format

Use the template in `docs/ai/templates/STATE_REPORT.md`:

```
## State Report
Phase: <active phase name>
Last completed: TASK-NNN <name> | none
In progress: TASK-NNN <name> | none
  progress: <summary from progress field> | fresh start
Next eligible: TASK-NNN <name> | none

Governance: active | inactive

SPEC conflicts: <list> | none found
Non-goal conflicts: <list> | none found
Assumption conflicts: <list> | none found
ADR conflicts: <list> | none found
Inconsistencies: <list> | none found
```

**Governance status rule** (reporting only — does not change enforcement behavior):
- `inactive`: no constraints exist to violate — not "no violations found."
- `active`: checks against SPEC, NON_GOALS, and ASSUMPTIONS are meaningful.

Analysis (Step 6) and audit (Step 7) always run regardless of governance status.

## Stop Conditions

None. This step always completes. Proceed to Step 3.
