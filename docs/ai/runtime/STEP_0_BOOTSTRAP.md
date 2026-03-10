# STEP 0: Bootstrap Detection

## Purpose

Detect whether the repository is in template state. If so, enter bootstrap mode and halt the normal pipeline.

## Required Reads

- `docs/core/SPEC.md`
- `docs/project/TASKS.md`

## Procedure

1. Read `docs/core/SPEC.md`.
2. Check for `<!-- BOOTSTRAP:PENDING -->` marker.
3. Read `docs/project/TASKS.md`.
4. Check whether any tasks are `[-]` or `[x]`.
5. If marker is present AND no tasks are in-progress or completed → **enter bootstrap mode**.
6. Execute `docs/ai/BOOTSTRAP_PROTOCOL.md` for the full bootstrap procedure.
7. After bootstrap completes, **stop**. The user will run `/next` again.

If not in template state → proceed to Step 1.

## Outputs

- Bootstrap mode entered (pipeline halts), OR
- Confirmation that project is not in template state (pipeline continues)

## Stop Conditions

- Bootstrap entered successfully → **stop the normal `/next` pipeline**. Do not proceed to Step 1.
