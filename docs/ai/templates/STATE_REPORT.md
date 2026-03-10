# State Report Template

Used by Step 2 (Report State). Output exactly in this format.

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

## Field Definitions

| Field | Value |
|---|---|
| Phase | The currently active phase from TASKS.md |
| Last completed | Most recent `[x]` task, or `none` |
| In progress | Current `[-]` task, or `none` |
| progress | The `progress:` field from the `[-]` task, or `fresh start` if just selected |
| Next eligible | First `[ ]` task with all dependencies met, or `none` |
| Governance | `active` if SPEC.md has real constraints; `inactive` if still placeholder |
| Conflicts | Any conflicts detected during context restore, or `none found` |

## Session Continuity

If `docs/project/PROJECT_STATE.md` exists, include its key fields after the state report:

```
Session context (from PROJECT_STATE.md):
  Focus: <current focus>
  Recent: <most recent change>
  Risks: <active risks> | none
  Next session: <start instructions>
```

If PROJECT_STATE.md does not exist, omit this section.
