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

---

## The `/next` Pipeline

Every `/next` executes these 8 steps in order. Do not skip steps.

### Step 1: Restore Context

Read these files in order:

1. `docs/core/SPEC.md` — non-negotiable architectural constraints
2. `docs/core/NON_GOALS.md` — scope boundary
3. `docs/core/ASSUMPTIONS.md` — design context
4. `docs/ai/DOCUMENT_SYSTEM.md` — documentation structure
5. `docs/ai/CLAUDE.md` — this file (behavioral rules)
6. `docs/core/DEFINITIONS.md` — project vocabulary
7. `docs/project/TASKS.md` — current project state

**Placeholder handling**: Some registered documents may still be placeholders (contain only section headings or TODO markers). During Step 1, verify existence but do **not** treat placeholder content as authoritative state. Placeholder documents become meaningful only after their design task completes.

### Step 2: Report State

Output a brief status block:

```
Phase: <active phase name>
Last completed: TASK-NNN <name>
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

Report **`Governance: inactive`** when:
- `SPEC.md` is still a placeholder (contains only setup instructions, no project-specific constraints), OR
- core governance documents (`SPEC.md`, `NON_GOALS.md`, `ASSUMPTIONS.md`) have not been filled in yet.

This means governance checks will report "none found" because no constraints exist to violate — not because the project is violation-free.

Report **`Governance: active`** when:
- `SPEC.md` contains real project constraints, AND
- governance checks against SPEC, NON_GOALS, and ASSUMPTIONS are meaningful.

This status is informational. Analysis (Step 6) and audit (Step 7) always run regardless of governance status.

### Step 3: Detect or Select Task

- If a task is `[-]` → **continue it**. Read its `progress:` field to understand what was already done. Do not start another.
- If no task is `[-]` → select the next `[ ]` task where:
  - All `depends:` are `[x]`.
  - It appears earliest in the active phase.
- Set the selected task to `[-]` in `TASKS.md` and write `progress: started` immediately. Save **before any other work**.
- Update the `progress:` field at natural milestones during work (e.g., "Draft reviewed", "Section 2 complete"). This allows the next session to resume without repeating work.

### Step 4: Load Task Context

Read additional documents based on the task's `type:` field:

| type | Additional reads |
|---|---|
| `design` | `docs/core/PRINCIPLES.md`, target document, all docs it references, architecture docs, relevant ADRs from `docs/project/decisions/`. Also read any architecture constraint docs relevant to the task. |
| `implement` | Architecture docs, scope docs, relevant model/UX docs, relevant ADRs. Also read testing, error handling, and versioning docs if they exist. |
| `document` | Target document, `docs/ai/CHANGE_PROTOCOL.md` |

**For all types**: if the task's target document is constrained by SPEC.md (see hierarchy above), re-read the relevant SPEC sections before drafting.

### Step 5: Execute Task

Run the workflow for the task's type:

**`type: design`** — Create or update a design document.
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

**`type: implement`** — Write application code.
1. Verify feature is in scope per scope documents and `TASKS.md`.
2. **Check NON_GOALS.md** — verify feature does not conflict with a non-goal.
3. **Check ASSUMPTIONS.md** — verify implementation aligns with stated assumptions.
4. **Check existing ADRs** for relevant prior decisions.
5. **Verify conformance with SPEC.md** (all relevant sections including performance constraints).
6. **Verify extension boundary** — domain-specific code must be in extension modules, not core.
7. Update documentation first if the implementation requires doc changes.
8. Implement the code.
9. Test.

**`type: document`** — Update workflow or process documentation.
1. Read the target document.
2. Draft updated content.
3. Present for review.
4. Apply changes.

### Step 6: Automatic Analysis

Runs automatically after every task. Do not skip. Do not wait for user request.

1. Check the target document and all documents modified during the task.
2. **Verify SPEC conformance** — flag any deviation from SPEC sections.
3. **Verify non-goal boundary** — flag any feature that conflicts with `NON_GOALS.md`.
4. **Verify assumption alignment** — flag any design that silently contradicts `ASSUMPTIONS.md`.
5. **Verify extension boundary** — flag any domain-specific concepts leaking into core.
6. **Verify performance constraints** — flag designs that violate SPEC performance requirements.
7. Verify consistency with `PRINCIPLES.md` and architecture documents.
8. Verify the document hierarchy is respected.
9. **Check ADR consistency** — verify no contradiction with accepted ADRs.
10. Identify gaps, ambiguities, or open questions.
11. Output:

```
Analysis:
- <finding>
- ...
SPEC conformance: ok | VIOLATION: <detail>
Non-goal boundary: ok | VIOLATION: <detail>
Assumption alignment: ok | CHANGE NEEDED: <detail>
Extension boundary: ok | VIOLATION: <detail>
Performance constraints: ok | VIOLATION: <detail>
ADR consistency: ok | CONFLICT: <detail>
Issues: <count> | none
```

**If any VIOLATION is found → stop immediately. Do not proceed to Step 7.**

### Step 7: Automatic Audit

Runs automatically after every task. Do not skip. Do not wait for user request.

1. Re-read `docs/core/SPEC.md`, `docs/core/DEFINITIONS.md`, and `docs/project/TASKS.md`.
2. Check for:
   - **SPEC violations**: any document contradicting SPEC.md
   - **Non-goal violations**: features conflicting with NON_GOALS.md
   - **Assumption conflicts**: designs that silently contradict ASSUMPTIONS.md
   - **Hierarchy violations**: lower document contradicting a higher one
   - **Extension boundary violations**: domain-specific concepts in core
   - **Performance constraint violations**: designs incompatible with SPEC performance requirements
   - **ADR conflicts**: work contradicting accepted ADRs
   - **Term drift**: terms used in modified documents but not in `DEFINITIONS.md`
   - **Contradictions**: statements that conflict across documents
   - **Orphaned references**: links to documents or sections that don't exist
   - **Stale content**: information outdated given the work just completed
   - **Missing registrations**: documents that exist but are not listed in `DOCUMENT_SYSTEM.md`
   - **Code drift**: implementation that diverges from documented architecture
3. Output:

```
Audit:
- SPEC violations: <list> | none
- Non-goal violations: <list> | none
- Assumption conflicts: <list> | none
- Hierarchy violations: <list> | none
- Extension violations: <list> | none
- Performance violations: <list> | none
- ADR conflicts: <list> | none
- Term drift: <list> | none
- Contradictions: <list> | none
- Orphaned refs: <list> | none
- Stale content: <list> | none
- Missing registrations: <list> | none
- Code drift: <list> | none
Status: green | yellow | red
```

- **Red** (any SPEC/hierarchy/extension/performance/non-goal violation or ADR conflict) → stop. Do not complete task.
- **Yellow** (non-blocking issues) → note and proceed.
- **Green** → proceed.

### Step 8: Complete Task

1. Set the task to `[x]` in `TASKS.md`.
2. Append to `DONE.md`: `- [x] TASK-NNN: Name (YYYY-MM-DD)`
3. Record any decisions as ADR files in `docs/project/decisions/` and update `DECISIONS.md` index.
4. Check if any `[!]` BLOCKED tasks are now unblocked → set to `[ ]`.
5. Report: what was completed, analysis summary, audit status, next eligible task.

---

## `/next <new request>`

When the user provides a request alongside `/next`:

1. Execute Steps 1–2 (restore context, report state).
2. **Classify the request** as one of:
   - **(a) Continuation** — relates to the `[-]` task → incorporate the input and continue from Step 4.
   - **(b) New task** — does not conflict → create a new task in `TASKS.md` (next sequential ID, determine `type:` and `phase:`, identify dependencies, insert at end of appropriate phase). If no task is `[-]` and dependencies are met, start it. If a task is already `[-]`, ask the user: finish current first, or abandon and switch?
   - **(c) Conflict** — contradicts SPEC.md, NON_GOALS.md, ADRs, extension boundary, plans, scope, or architecture → **stop and report** the conflict with document references. Do not proceed.
3. Continue with Steps 3–8 for the determined task.

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
- **SPEC reference**: Section N (if applicable)

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

## Rules for SPEC.md

- **Highest-level constraint.** No document or code may contradict it.
- Claude must check SPEC conformance in every analysis (Step 6) and audit (Step 7).
- If a task requires changing SPEC.md, **stop and report**. The change must be approved and recorded as an ADR before proceeding.
- SPEC.md is read first during context restoration.

## Rules for Extension Boundary

- Core entities are domain-neutral.
- Domain-specific features must be implemented as extensions.
- Extensions must not modify core data models.
- Extensions attach through defined extension points.
- Analysis (Step 6) and audit (Step 7) check for extension boundary violations.

## Rules for Performance Constraints

- Designs must respect performance constraints defined in SPEC.md.
- Analysis (Step 6) checks for performance constraint violations.

## Rules for NON_GOALS.md

- Defines what the project is NOT building.
- If a proposed feature falls within a non-goal → **stop and flag the conflict**. Do not proceed.
- If a feature is adjacent to a non-goal → flag, discuss scope, decide.
- Changing a non-goal requires an ADR file in `docs/project/decisions/` (with `DECISIONS.md` index update) before updating the document.
- Check NON_GOALS.md during Step 5 (execute) for all `design` and `implement` tasks.
- Analysis (Step 6) and audit (Step 7) check for non-goal violations.

## Rules for ASSUMPTIONS.md

- Captures design assumptions that guide but do not mandate.
- If a design depends on an assumption → reference it explicitly.
- If a design requires changing an assumption → **propose the change before proceeding**. Create an ADR file in `docs/project/decisions/` documenting the change and update `DECISIONS.md` index before modifying `ASSUMPTIONS.md`.
- Assumptions are softer than SPEC.md — they can evolve, but not silently. Changes follow the same ADR governance as other architectural decisions.
- Check ASSUMPTIONS.md during Step 5 (execute) for `design` and `implement` tasks.

## Rules for TASKS.md

- Source of truth for project progress.
- Read fully before selecting work.
- Max one `[-]` at a time.
- Never skip dependencies.
- Never remove tasks — only change state.
- New tasks get next sequential ID (noted at bottom of file).
- Update immediately on state change.
- Update `progress:` field on `[-]` tasks at natural milestones.
- If a task is too large for one session, decompose it into subtasks (see Task Decomposition in TASKS.md).

## Rules for DONE.md

- Append-only log.
- Copy task on `[x]` with date.
- Never modify existing entries.

## Rules for DECISIONS.md

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
