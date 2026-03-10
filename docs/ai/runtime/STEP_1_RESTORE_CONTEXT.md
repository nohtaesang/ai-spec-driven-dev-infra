# STEP 1: Restore Context

## Purpose

Load all governance and project state documents to establish the working context for this session.

## Required Reads

Read these files in order:

1. `docs/core/SPEC.md` — non-negotiable architectural constraints
2. `docs/core/NON_GOALS.md` — scope boundary
3. `docs/core/ASSUMPTIONS.md` — design context
4. `docs/ai/DOCUMENT_SYSTEM.md` — documentation structure and registry
5. `docs/ai/CLAUDE.md` — behavioral rules
6. `docs/ai/GOVERNANCE_CHECKS.md` — explicit fail conditions
7. `docs/core/DEFINITIONS.md` — project vocabulary
8. `docs/project/TASKS.md` — current project state
9. `docs/project/PROJECT_STATE.md` — session continuity anchor (if it exists)

## Procedure

1. Read each file in order.
2. For each file, note whether it is a placeholder or contains real content.
3. Determine governance status:
   - **inactive**: SPEC.md is still a placeholder (contains only setup instructions, no project-specific constraints), OR core governance documents have not been filled in yet.
   - **active**: SPEC.md contains real project constraints and governance checks are meaningful.

## Placeholder Handling

Some registered documents may still be placeholders (contain only section headings or TODO markers). Verify existence but do **not** treat placeholder content as authoritative state. Placeholder documents become meaningful only after their design task completes.

## Outputs

- All governance documents loaded
- Governance status determined (active / inactive)
- Current phase and task state identified
- Session continuity context from PROJECT_STATE.md (if available)
- Missing or placeholder documents noted

## Stop Conditions

None. This step always completes. Proceed to Step 2.
