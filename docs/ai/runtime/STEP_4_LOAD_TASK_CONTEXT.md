# STEP 4: Load Task Context

## Purpose

Read additional documents specific to the task's type and target, building the full context needed for execution.

## Required Reads

Depends on the task's `type:` field:

| Type | Additional Reads |
|---|---|
| `design` | `docs/core/PRINCIPLES.md`, target document, all docs it references, architecture docs, relevant ADRs from `docs/project/decisions/`. Also read any architecture constraint docs relevant to the task. |
| `implement` | Architecture docs, scope docs, relevant model/UX docs, relevant ADRs. Also read testing, error handling, and versioning docs if they exist. |
| `document` | Target document, `docs/ai/CHANGE_PROTOCOL.md` |

## Procedure

1. Identify the task's `type:` and `target:` fields from TASKS.md.
2. Read the documents listed above for that type.
3. If the task's target document is constrained by SPEC.md (see document hierarchy), re-read the relevant SPEC sections.
4. If the task has a `relates:` field, read the referenced SPEC clauses or ADRs.

## Outputs

- All task-relevant documents loaded
- Governing constraints identified
- Related ADRs noted

## Stop Conditions

None. This step always completes. Proceed to Step 5.
