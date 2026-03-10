# STEP 5: Execute Task

## Purpose

Perform the actual work for the task, with governance checks at every decision point.

## Required Reads

- `docs/ai/CHANGE_PROTOCOL.md`
- `docs/ai/GOVERNANCE_CHECKS.md`

## Pre-Execution Stop Conditions

Before executing, verify **all** of the following. If any fail, **stop and report** — do not proceed.

- No more than one `[-]` task exists in TASKS.md.
- The task's target document is registered in `docs/ai/DOCUMENT_SYSTEM.md` (for design tasks).
- Implementation is not requested while governing design docs are still placeholders.
- No architecture change is implied without an ADR existing or being proposed.
- All required related documents (per Step 4) have been read.

See `docs/ai/GOVERNANCE_CHECKS.md` for the complete list.

## Procedure by Task Type

### `type: design` — Create or update a design document.

1. Read the target document and all related documents.
2. **Check existing ADRs** in `docs/project/decisions/` for relevant prior decisions.
3. **Check conformance with SPEC.md** — the design must implement, not contradict, the SPEC.
4. **Check NON_GOALS.md** — the feature must not conflict with a stated non-goal.
5. **Check ASSUMPTIONS.md** — identify which assumptions the design depends on.
6. **Check extension boundary** — domain-specific features must go in extensions, not core.
7. **Check performance constraints** — design must not violate SPEC performance requirements.
8. Check for conflicts with other existing documents.
9. Draft the design content.
10. Present draft for user review.
11. Apply changes after approval.
12. Add new terms to `DEFINITIONS.md` if any were introduced.
13. **Create ADR** in `docs/project/decisions/` if the task involves an architectural decision.
14. Update `DECISIONS.md` index if a new ADR was created.

### `type: implement` — Write application code.

1. Verify feature is in scope per scope documents and `TASKS.md`.
2. **Check NON_GOALS.md** — verify feature does not conflict with a non-goal.
3. **Check ASSUMPTIONS.md** — verify implementation aligns with stated assumptions.
4. **Check existing ADRs** for relevant prior decisions.
5. **Verify conformance with SPEC.md** (all relevant sections including performance constraints).
6. **Verify extension boundary** — domain-specific code must be in extension modules, not core.
7. Update documentation first if the implementation requires doc changes.
8. Implement the code.
9. Test.

### `type: document` — Update workflow or process documentation.

1. Read the target document.
2. Draft updated content.
3. Present for review.
4. Apply changes.

## Process References

During execution, consult these process documents as applicable:

- `docs/process/CHANGE_IMPACT_CHECKLIST.md` — review what the change might affect
- `docs/process/CONFIG_CONSTANTS_POLICY.md` — no magic numbers, tunables in config
- `docs/process/REPOSITORY_CONVENTIONS.md` — file and module placement rules

These are not required reads at task start, but should be consulted when making placement or configuration decisions.

## Task Scope Guard

During execution, if the work begins to diverge from the current task's scope:

1. **Pause** — do not continue the divergent work.
2. **Check** — is the divergent work necessary to complete the current task, or is it a separate concern?
3. **If necessary prerequisite** — note it in the `progress:` field and continue, but keep it minimal.
4. **If separate concern** — stop the divergent work. Add a new task to TASKS.md (next sequential ID) and return to the current task.

Examples of task drift:
- Implementing feature A but starting to refactor module B
- Fixing a bug but redesigning the surrounding architecture
- Writing documentation but proposing new features

The rule: **finish or formally abandon the current task before doing unrelated work.**

## Progress Updates

Update the `progress:` field in TASKS.md at natural milestones during execution (e.g., "Draft reviewed", "Section 2 complete"). This allows the next session to resume without repeating work.

## Outputs

- Task work completed (design doc, code, or documentation)
- DEFINITIONS.md updated if new terms introduced
- ADR created if architectural decision made
- TASKS.md `progress:` field updated

## Stop Conditions

- SPEC.md would be contradicted → **stop and report**
- NON_GOALS.md would be violated → **stop and report**
- Architecture change implied but no ADR path → **stop and report**
- Assumption change needed but not proposed → **stop and report**
- Extension boundary violated → **stop and report**
