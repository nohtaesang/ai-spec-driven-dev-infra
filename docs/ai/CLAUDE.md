# Claude Behavioral Rules — AI Spec-Driven Development

These rules govern how Claude Code must operate within any project using this infrastructure. They apply to every session.

---

## Document Hierarchy

The project enforces a strict constraint hierarchy. Higher documents constrain all lower documents. No lower document may contradict a higher one.

```
SPEC.md                 ← highest constraint, non-negotiable
NON_GOALS.md            ← scope boundary, features must not conflict
ASSUMPTIONS.md          ← design context, changes require ADR file
  ↓ constrains
DEFINITIONS.md          ← terms must match SPEC
  ↓ constrains
Model documents         ← models must implement SPEC entities
  ↓ constrains
UX / Architecture docs  ← must conform to the models
  ↓ constrains
Implementation          ← code must conform to all above
```

**SPEC.md is the highest-level constraint.** If any document or implementation contradicts SPEC.md, Claude must **stop and report the conflict**. Changes to SPEC.md require an explicit ADR.

**NON_GOALS.md is the scope boundary.** If a proposed feature conflicts with a non-goal, Claude must **stop and flag the conflict**. Changing a non-goal requires an ADR file before updating the document.

**ASSUMPTIONS.md provides design context.** If a design depends on changing an assumption, Claude must **propose the assumption change** before proceeding.

---

## `/next` — The Only Command Humans Need

`/next` is the single entrypoint for all normal project work. It runs a full pipeline automatically.

The pipeline is defined as 9 sequential steps (0–8) in `docs/ai/runtime/`. Each step has explicit inputs, outputs, procedures, and stop conditions.

**Authoritative step definitions**: `docs/ai/runtime/STEP_*.md`
**Pipeline overview**: `docs/ai/runtime/README.md`
**Output templates**: `docs/ai/templates/`

### Pipeline Summary

```
/next
  ├─ 0. Bootstrap detection        → docs/ai/runtime/STEP_0_BOOTSTRAP.md
  ├─ 1. Restore context            → docs/ai/runtime/STEP_1_RESTORE_CONTEXT.md
  ├─ 2. Report state               → docs/ai/runtime/STEP_2_REPORT_STATE.md
  ├─ 3. Pick or resume task        → docs/ai/runtime/STEP_3_PICK_TASK.md
  ├─ 4. Load task context          → docs/ai/runtime/STEP_4_LOAD_TASK_CONTEXT.md
  ├─ 5. Execute task               → docs/ai/runtime/STEP_5_EXECUTE.md
  ├─ 6. Automatic analysis         → docs/ai/runtime/STEP_6_ANALYZE.md
  ├─ 7. Automatic audit            → docs/ai/runtime/STEP_7_AUDIT.md
  └─ 8. Close task                 → docs/ai/runtime/STEP_8_CLOSE_TASK.md
```

Execute steps in strict order. Do not skip or merge steps. If a step triggers a stop condition, halt and report.

---

## Governance

Explicit fail conditions for all governance checks are in `docs/ai/GOVERNANCE_CHECKS.md`. That file is authoritative for determining pass/fail verdicts.

### Stop Principles

Claude must **stop and report** (not proceed) when:

- SPEC.md would be contradicted
- NON_GOALS.md would be violated
- More than one `[-]` task exists
- Target document is not registered in DOCUMENT_SYSTEM.md
- Implementation is requested but governing design docs are still placeholders
- Architecture change is implied but no ADR exists or is proposed
- Required related documents were not read before executing
- Accepted ADR would be contradicted without a superseding ADR

---

## Task Types

| Type | Purpose | What it produces |
|---|---|---|
| `design` | Create or update domain/architecture/UX design documents | Updated design doc, possible ADR, possible new definitions |
| `implement` | Write application code | Working code, updated docs if needed |
| `document` | Update workflow, process, or system documentation | Updated documentation |

`analyze` and `audit` are **not task types**. They are automatic pipeline steps (Steps 6–7).

---

## Architecture Decision Records (ADRs)

### Storage

ADRs are stored as individual files in `docs/project/decisions/`:

```
docs/project/decisions/
  0001-some-decision.md
  0002-another-decision.md
  ...
```

`docs/project/DECISIONS.md` serves as the index listing all ADRs.

### When to Create an ADR

- A technology choice is made
- A design alternative is chosen over another
- A scope boundary is established
- A convention or pattern is adopted for the project
- A SPEC.md change is proposed (mandatory)
- An extension is introduced or removed
- A performance-related architectural choice is made

### ADR File Format

```
# ADR-NNNN: Title

- **Date**: YYYY-MM-DD
- **Status**: accepted | superseded by ADR-NNNN | deprecated
- **SPEC reference**: SPEC-NNN (if applicable)
- **Related tasks**: TASK-NNN (if applicable)

## Context
Why this decision was needed.

## Decision
What was decided.

## Consequences
What follows from this decision.
```

### ADR Rules

- **All new ADRs must be individual files** in `docs/project/decisions/`.
- Use 4-digit sequential numbering (0001, 0002, …).
- File name: `NNNN-kebab-case-title.md`.
- **Check existing ADRs before proposing architectural changes.** Never contradict an accepted ADR without creating a new superseding ADR.
- Never edit the Context or Decision of an accepted ADR. To change, create a new ADR that supersedes it.
- Update `DECISIONS.md` index when creating a new ADR.

---

## Rules for Core Documents

### SPEC.md
- **Highest-level constraint.** No document or code may contradict it.
- Clauses are numbered as `SPEC-NNN` for cross-referencing.
- If a task requires changing SPEC.md, **stop and report**. The change must be approved and recorded as an ADR before proceeding.
- SPEC.md is read first during context restoration.

### NON_GOALS.md
- Defines what the project is NOT building.
- If a proposed feature falls within a non-goal → **stop and flag the conflict**. Do not proceed.
- If a feature is adjacent to a non-goal → flag, discuss scope, decide.
- Changing a non-goal requires an ADR file before updating the document.

### ASSUMPTIONS.md
- Captures design assumptions that guide but do not mandate.
- If a design depends on an assumption → reference it explicitly.
- If a design requires changing an assumption → **propose the change before proceeding**. Create an ADR before modifying.
- Assumptions are softer than SPEC.md — they can evolve, but not silently.

### Extension Boundary
- Core entities are domain-neutral.
- Domain-specific features must be implemented as extensions.
- Extensions must not modify core data models.
- Extensions attach through defined extension points.

### Performance Constraints
- Designs must respect performance constraints defined in SPEC.md.

---

## Rules for Tracking Documents

### TASKS.md
- Source of truth for project progress.
- Read fully before selecting work.
- Max one `[-]` at a time.
- Never skip dependencies.
- Never remove tasks — only change state.
- New tasks get next sequential ID.
- Update `progress:` field on `[-]` tasks at natural milestones.
- See `docs/ai/CHANGE_PROTOCOL.md` for state transitions and mutation rules.

### DONE.md
- Append-only log.
- Copy task on `[x]` with date.
- Never modify existing entries.

### DECISIONS.md
- Index of all ADRs in `docs/project/decisions/`.
- Update when a new ADR file is created.
- Reference ADR files by number and title.

---

## Standing Rules

### Definitions
- Never use a domain term without it being in `DEFINITIONS.md`.
- `DEFINITIONS.md` must be consistent with SPEC.md. SPEC.md wins on conflict.
- Never redefine a term inline. Update `DEFINITIONS.md`.

### Architecture
- No new components/boundaries/flows without updating architecture documents.
- No technology changes without an ADR.
- Architecture must conform to SPEC.md.

### Scope
- No work outside scope documents and `TASKS.md`.
- Check `NON_GOALS.md` before proposing new features.
- Check `ASSUMPTIONS.md` when design choices depend on operating context.
- Flag out-of-scope requirements.

### Communication
- On `/next`: always report phase, task, SPEC conflicts, inconsistencies.
- When uncertain: ask, don't assume.
- Reference documents explicitly, don't paraphrase.
