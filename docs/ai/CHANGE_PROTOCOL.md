# Change Protocol

This document defines how documentation and task state are updated. All changes must follow this protocol.

---

## Document Hierarchy

Changes must respect the constraint hierarchy. A lower document may never contradict a higher one.

```
SPEC.md                 ← highest, changes require ADR
NON_GOALS.md            ← scope boundary, features must not conflict
ASSUMPTIONS.md          ← design context, changes require ADR file
  ↓
DEFINITIONS.md          ← terms must match SPEC
  ↓
Model documents
  ↓
UX / Architecture documents
  ↓
Implementation
```

### SPEC Violation Rule

If a proposed change would contradict `docs/core/SPEC.md`:
1. **Stop.** Do not apply the change.
2. Report the specific SPEC section that would be violated.
3. If the user wants to proceed, create an ADR in `docs/project/decisions/` **before** modifying SPEC.md or any downstream documents.

### Extension Boundary Rule

If a proposed change would introduce domain-specific concepts into core entities:
1. **Stop.** Report the violation.
2. Redirect the feature to an extension.
3. If the core genuinely needs to change, create an ADR and propose a SPEC amendment.

### Performance Constraint Rule

If a proposed design violates performance constraints defined in SPEC.md:
1. **Flag** the violation.
2. Propose an alternative that respects the constraints.

### Non-Goal Violation Rule

If a proposed feature conflicts with `docs/core/NON_GOALS.md`:
1. **Stop.** Report the specific non-goal that would be violated.
2. If the user wants to proceed, create an ADR file in `docs/project/decisions/` and update `DECISIONS.md` index **before** modifying `NON_GOALS.md`.

### Assumption Change Rule

If a proposed change depends on modifying an assumption in `docs/core/ASSUMPTIONS.md`:
1. **Flag** the assumption that would need to change.
2. Propose the assumption update.
3. Create an ADR file in `docs/project/decisions/` documenting the change and update `DECISIONS.md` index **before** modifying `ASSUMPTIONS.md`.

---

## Task State Transitions

| Notation | State | Meaning |
|---|---|---|
| `[ ]` | TODO | Not started. Eligible if dependencies met. |
| `[-]` | IN_PROGRESS | Being worked on. Max one at a time. |
| `[x]` | DONE | Complete. Must also appear in DONE.md. |
| `[!]` | BLOCKED | Cannot proceed. Reason stated inline. |

### `[ ]` → `[-]` Starting

- **Trigger**: `/next` selects the task.
- **Action**: Change `[ ]` to `[-]` in `TASKS.md`. Write `progress: started` immediately. Save before any other work.
- **Constraint**: No other task may be `[-]`.

### `[-]` → `[x]` Completing

- **Trigger**: Acceptance criteria met AND analysis passed AND audit green/yellow AND no violations or ADR conflicts.
- **Actions** (in order):
  1. Change `[-]` to `[x]` in `TASKS.md`. Remove `progress:` field.
  2. Append to `DONE.md`: `- [x] TASK-NNN: Name (YYYY-MM-DD)`
  3. If the task produced a decision → create ADR file in `docs/project/decisions/` and update `DECISIONS.md` index.
  4. Check all `[!]` tasks — if blocker resolved, change to `[ ]`.

### `[-]` progress update

- **Trigger**: Natural milestone reached during task execution.
- **Action**: Update `progress:` field on the `[-]` task in `TASKS.md`. This enables the next session to resume without repeating work.

### `[-]` → `[ ]` Abandoning

- **Trigger**: User redirects, or a violation is discovered.
- **Action**: Change `[-]` back to `[ ]`. Remove `progress:` field. Add note if partial work should be preserved.

### Task Decomposition

If a `[-]` task proves too large for a single session:

1. Split into ordered subtasks: `TASK-NNNa`, `TASK-NNNb`, etc.
2. Subtasks are listed inline under the parent task in `TASKS.md`, indented with two extra spaces.
3. Each subtask gets its own `acceptance:` criterion.
4. Parent task stays `[-]`. Subtasks are worked in order.
5. Subtask completion is noted in the parent's `progress:` field.
6. Only the parent appears in `DONE.md` when all subtasks are `[x]`.

### `[ ]` → `[!]` Blocking

- **Action**: Change to `[!]`. Add inline: `blocked: <reason>`.

### `[!]` → `[ ]` Unblocking

- **Action**: Change to `[ ]`. Remove `blocked:` line.

---

## When Files Must Be Updated

### TASKS.md Mutation Rules

- On task start: change `[ ]` → `[-]` and write `progress: started` **before any other work**.
- During execution: update `progress:` at each natural milestone.
- On completion: change `[-]` → `[x]`, remove `progress:`, and update DONE.md **in the same step**.
- On completion: write a final summary in DONE.md entry (not just the task title).
- Never modify `[x]` tasks (append-only history).

### TASKS.md

| Event | Action |
|---|---|
| Task selected | `[ ]` → `[-]` |
| Milestone reached on [-] task | Update `progress:` field |
| Task complete + analysis + audit pass | `[-]` → `[x]`, remove `progress:` |
| Task blocked | `[ ]` → `[!]` with reason |
| Blocker resolved | `[!]` → `[ ]` |
| User abandons task | `[-]` → `[ ]`, remove `progress:` |
| Task too large | Decompose into subtasks (TASK-NNNa, NNNb, …) |
| New task from `/next <request>` | Add with next TASK-NNN |

### DONE.md

| Event | Action |
|---|---|
| Task marked `[x]` | Append: `- [x] TASK-NNN: Name (YYYY-MM-DD)` |

### DECISIONS.md (index)

| Event | Action |
|---|---|
| New ADR file created | Add entry to index |
| ADR superseded | Update status in index |

### ADR files (docs/project/decisions/)

**All new ADRs must be individual files.** No inline ADR entries in DECISIONS.md.

| Event | Action |
|---|---|
| Architectural decision made | Create new ADR file (next sequential number) |
| Technology choice made | Create new ADR file |
| SPEC.md change proposed | **Mandatory** new ADR file before change |
| Assumption in ASSUMPTIONS.md changed | Create new ADR file before modifying assumption |
| Previous decision reversed | New ADR with `supersedes ADR-NNNN`; update old ADR status |

---

## Handling `/next <new request>`

### Maps to existing task
Continue or start that task.

### New task
1. Assign next TASK-NNN ID.
2. Determine `type:` (design, implement, document).
3. Determine `phase:`.
4. Identify `depends:`.
5. **Verify** does not contradict SPEC.md, NON_GOALS.md, or accepted ADRs.
6. Insert at end of appropriate phase section.
7. If no `[-]` and deps met → start immediately.
8. If `[-]` exists → ask user: finish or switch?

### Conflicts
Stop. Report conflict with SPEC section, NON_GOALS.md item, or ADR number. Wait for resolution.

---

## Documentation Change Process

### Step 1: Check Hierarchy
Identify where the target document sits. Read all documents above it.

### Step 2: Check SPEC Conformance
Verify proposed change does not violate SPEC.md. If it does → stop.

### Step 3: Check ADRs
Read relevant ADRs in `docs/project/decisions/`. Verify no contradiction with accepted decisions.

### Step 4: Check for Conflicts
Verify no contradictions, no duplicate definitions, cross-references remain valid.

### Step 5: Draft the Change
State what is changing, why, and which documents are affected.

### Step 6: Apply the Change
Update documents. Keep definitions in `DEFINITIONS.md` only. Use relative paths. No orphans.

### Step 7: Record Decision (if applicable)
Create ADR file in `docs/project/decisions/`:
```
# ADR-NNNN: Title
- **Date**: YYYY-MM-DD
- **Status**: accepted | superseded by ADR-NNNN | deprecated
- **SPEC reference**: Section N (if applicable)

## Context
## Decision
## Consequences
```
Update `DECISIONS.md` index.

### Step 8: Update Task Tracking (mandatory)
1. Verify current task is `[-]`.
2. If complete, run analysis + audit, then set `[x]` and copy to DONE.md.
3. Check for newly unblocked tasks.

---

## Cross-Reference Rules

- Reference canonical documents, not copies.
- Use relative paths: `../core/DEFINITIONS.md`.
- Reference ADRs by number: `ADR-0001`.
- Reference SPEC clauses by ID: `SPEC-001`.
- Reference tasks by ID: `TASK-001`.
- When removing a document, find and update all references first.

### ID Conventions

| Entity | Format | Example | Scope |
|---|---|---|---|
| Task | `TASK-NNN` | TASK-014 | TASKS.md, DONE.md |
| Decision | `ADR-NNNN` | ADR-0003 | docs/project/decisions/ |
| SPEC clause | `SPEC-NNN` | SPEC-001 | docs/core/SPEC.md |

IDs are stable and sequential. Do not renumber. Deprecated items are marked, not removed.

## Conflict Resolution

1. Check `SPEC.md` first — it always wins.
2. Check `NON_GOALS.md` — features must not conflict with stated non-goals.
3. Check `ASSUMPTIONS.md` — designs should align with stated assumptions.
4. Check accepted ADRs — they constrain downstream design.
5. Then identify authoritative source per `DOCUMENT_SYSTEM.md`.
6. Update non-authoritative document to align.
7. If unclear, create an ADR to establish precedence.
