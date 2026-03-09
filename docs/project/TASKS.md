# Tasks

**Source of truth for all project progress.**

Claude must read this file on every `/next` before doing any work.

---

## Usage Rules

### Task States

| Notation | State | Meaning |
|---|---|---|
| `[ ]` | TODO | Not started. Eligible if dependencies are met. |
| `[-]` | IN_PROGRESS | Being worked on. **Max one at a time.** |
| `[x]` | DONE | Complete. Must also be in `DONE.md`. |
| `[!]` | BLOCKED | Cannot proceed. Reason stated inline. |

### Task Format

```
- [STATE] TASK-NNN type:<type> phase:<phase> name: <short title>
  target: <file path>
  depends: TASK-NNN, TASK-NNN | none
  acceptance: <what "done" means>
  progress: <what has been completed so far>     ← only on [-] tasks
```

The `progress:` field is present on all `[-]` (in-progress) tasks. It is initialized to `started` when a task moves to `[-]`, then updated with meaningful content at natural milestones so the next session can resume without repeating work. It is cleared when a task moves to `[x]` or back to `[ ]`.

### Task Types

| Type | What Claude does |
|---|---|
| `design` | Create or update domain/architecture/UX design documents |
| `implement` | Write application code consistent with documentation |
| `document` | Update workflow, process, or system documentation |

`analyze` and `audit` are automatic pipeline steps, not task types.

### Constraint Hierarchy

All design and implementation tasks must conform to:

```
SPEC.md + NON_GOALS.md + ASSUMPTIONS.md → DEFINITIONS.md → Models → UX/Architecture → Code
```

Additionally: check ADRs and any extension or performance constraints defined in SPEC.md.

### How Claude Selects the Next Task

1. Read this file completely.
2. If a task is `[-]` → continue it.
3. If no `[-]` → select the first `[ ]` in the active phase where all `depends:` are `[x]`.
4. Set to `[-]` and save before doing any other work.

### Completion (after automatic analysis + audit)

1. Set to `[x]` in this file.
2. Append to `DONE.md`: `- [x] TASK-NNN: Name (YYYY-MM-DD)`
3. Create ADR in `docs/project/decisions/` if applicable. Update `DECISIONS.md` index.
4. Unblock any `[!]` tasks whose blockers are resolved.
5. Report completion and next eligible task.

### Rules

- Max one `[-]` at a time.
- Never skip dependencies.
- Never remove a task — only change its state.
- New tasks get the next sequential ID (see bottom of file).
- If a task is unclear, ask the user before starting.
- Update `progress:` on `[-]` tasks at natural milestones.

### Task Decomposition

If a task proves too large for a single session:

1. Split into ordered subtasks using a letter suffix: `TASK-NNNa`, `TASK-NNNb`, etc.
2. Subtasks are listed inline under the parent task in `TASKS.md`, indented with two extra spaces.
3. Each subtask gets its own `acceptance:` criterion.
4. The parent task remains `[-]` while subtasks are worked.
5. Subtasks are completed in order. Each subtask's completion is noted in the parent's `progress:` field.
6. Only the parent task appears in `DONE.md` when all subtasks are `[x]`.
7. Record the decomposition in the parent's `progress:` field before starting subtask work.

Example:
```
- [-] TASK-003 type:design phase:core-design name: Design data model
  progress: Decomposed into 003a, 003b. 003a complete, starting 003b.
    - [x] TASK-003a name: Core entity design
      acceptance: Core entities defined with relationships.
    - [ ] TASK-003b name: Extension point design
      acceptance: Extension attachment points identified.
```

---

## Phase 0: Project Setup

*Goal: Define the project's foundational constraints, vocabulary, and scope.*

- [ ] TASK-001 type:design phase:setup name: Define project specification
  target: docs/core/SPEC.md
  depends: none
  acceptance: SPEC.md contains all non-negotiable architectural constraints for the project. Short and stable. If a technology stack or framework is chosen, that choice must be recorded as an ADR.

- [ ] TASK-002 type:design phase:setup name: Define project vocabulary
  target: docs/core/DEFINITIONS.md
  depends: TASK-001
  acceptance: All domain terms from SPEC.md are defined. No placeholder entries. Every definition is consistent with SPEC.md.

- [ ] TASK-003 type:design phase:setup name: Define project vision and principles
  target: docs/core/VISION.md, docs/core/PRINCIPLES.md
  depends: TASK-001
  acceptance: VISION.md describes why the project exists and who it serves. PRINCIPLES.md lists design and engineering principles.

- [ ] TASK-004 type:design phase:setup name: Define assumptions and non-goals
  target: docs/core/ASSUMPTIONS.md, docs/core/NON_GOALS.md
  depends: TASK-001
  acceptance: ASSUMPTIONS.md lists design assumptions. NON_GOALS.md lists what the project is NOT building. Both are consistent with SPEC.md.

---

## Phase 1: Core Design Documents

*Goal: Define domain models and architecture. Tasks will be added after Phase 0.*

---

*Completed items: [DONE.md](./DONE.md) · Decisions: [DECISIONS.md](./DECISIONS.md) · ADRs: [decisions/](./decisions/)*
*Next task ID: TASK-005*
