# Document System

This file describes the purpose, scope, and governance of every documentation category in a spec-driven development project.

## Principles

- **Single source of truth**: each concept is defined in exactly one document.
- **Reference, don't duplicate**: other documents link to the authoritative definition.
- **Documentation leads implementation**: docs are updated *before* code changes.
- **Minimal but complete**: write only what is needed, but cover every decision.
- **Hierarchy enforcement**: higher documents constrain lower documents. SPEC.md is supreme.

---

## Document Constraint Hierarchy

Higher documents constrain all lower documents. No lower document may contradict a higher one.

```
docs/core/SPEC.md               ← non-negotiable, changes require ADR
docs/core/NON_GOALS.md          ← scope boundary, features must not conflict
docs/core/ASSUMPTIONS.md        ← design context, changes require ADR file
  ↓
docs/core/DEFINITIONS.md        ← terms must match SPEC
  ↓
docs/model/*                    ← models must implement SPEC entities
  ↓
docs/ux/* + docs/architecture/* ← must conform to the models
  ↓
Implementation (code)           ← must conform to all above
```

Conflict resolution always defers to the higher document. Accepted ADRs constrain downstream design.

---

## Documentation Categories

### `docs/core/` — Foundation

Stable, rarely-changing documents that define what the project *is*.

| File | Purpose |
|---|---|
| `SPEC.md` | **Highest-level constraint.** Non-negotiable architectural assumptions. Changes require an ADR. |
| `ASSUMPTIONS.md` | Design assumptions. Guides decisions but softer than SPEC. Changes require an ADR file. |
| `NON_GOALS.md` | **Scope boundary.** What the project is NOT building. Feature proposals conflicting with this must be stopped and flagged. |
| `VISION.md` | Why the project exists. Long-term goals and target users. |
| `PRINCIPLES.md` | Design and engineering principles that guide all decisions. |
| `DEFINITIONS.md` | Canonical glossary. Every domain term is defined here once. Must be consistent with SPEC.md. |

### `docs/model/` — Domain Models

*Created by the project, not part of core infrastructure.*

Formal descriptions of the domain data, sources, and systems. Must implement SPEC.md. Projects add model documents here as design tasks are completed.

### `docs/ux/` — User Experience

*Created by the project, not part of core infrastructure.*

Interaction design and UX architecture. Must conform to domain models.

### `docs/architecture/` — Technical Architecture

*Created by the project, not part of core infrastructure.*

System-level design decisions. Must conform to SPEC.md. Projects add architecture documents (e.g., ARCHITECTURE.md, EXTENSIONS.md, TESTING.md, ERROR_MODEL.md, VERSIONING.md) as design tasks are completed.

### `docs/planning/` — Scope and Roadmap

*Created by the project, not part of core infrastructure.*

Projects add planning documents (e.g., MVP_SCOPE.md, ROADMAP.md) as needed.

### `docs/project/` — Project State

Living documents that track progress and decisions.

| File | Purpose |
|---|---|
| `TASKS.md` | **Source of truth for project progress.** Phase-based task list with states, dependencies, types, and selection rules. |
| `DONE.md` | Append-only log of completed tasks. |
| `DECISIONS.md` | **Index** of all Architecture Decision Records. Points to individual ADR files. |

### `docs/project/decisions/` — ADR Files

Individual Architecture Decision Record files. Each captures one architectural decision.

| Pattern | Purpose |
|---|---|
| `NNNN-kebab-case-title.md` | One ADR per file. 4-digit sequential numbering. Immutable once accepted (supersede, don't edit). |

### Root — Entrypoint

| File | Purpose |
|---|---|
| `CLAUDE.md` (root) | Claude Code auto-loads this file. Points to `/next` as the primary workflow command. Lists 10 core rules and full command architecture. |

### `docs/ai/` — AI Collaboration

| File | Purpose |
|---|---|
| `CLAUDE.md` | Behavioral rules, document hierarchy, stop principles, ADR rules, standing rules. |
| `DOCUMENT_SYSTEM.md` | This file. Describes the doc system and constraint hierarchy. |
| `CHANGE_PROTOCOL.md` | State transitions, documentation change process, ADR creation triggers. |
| `BOOTSTRAP_PROTOCOL.md` | Level-2 bootstrap: template detection, structured intake, foundation doc generation, Level-2 document selection. |
| `GOVERNANCE_CHECKS.md` | Explicit fail conditions for all governance checks. Referenced by `/next`, `/analyze`, `/audit`, `/check`. |

### `docs/ai/runtime/` — Pipeline Step Definitions

Authoritative step-by-step execution spec for the `/next` pipeline. Each file defines one step.

| File | Purpose |
|---|---|
| `README.md` | Pipeline overview and execution order. |
| `STEP_0_BOOTSTRAP.md` | Detect template state, enter bootstrap if needed. |
| `STEP_1_RESTORE_CONTEXT.md` | Read governance and project state documents. |
| `STEP_2_REPORT_STATE.md` | Output standardized status report. |
| `STEP_3_PICK_TASK.md` | Resume `[-]` or select next eligible `[ ]` task. |
| `STEP_4_LOAD_TASK_CONTEXT.md` | Read task-type-specific documents. |
| `STEP_5_EXECUTE.md` | Run the task workflow with governance checks. |
| `STEP_6_ANALYZE.md` | Automatic analysis with fixed output format. |
| `STEP_7_AUDIT.md` | Automatic audit with fixed output format. |
| `STEP_8_CLOSE_TASK.md` | Mark complete, update tracking, report. |

### `docs/ai/templates/` — Output Format Templates

Fixed output formats referenced by runtime steps.

| File | Used By |
|---|---|
| `STATE_REPORT.md` | Step 2 (Report State) |
| `ANALYSIS_REPORT.md` | Step 6 (Analyze) |
| `AUDIT_REPORT.md` | Step 7 (Audit) |

### `docs/process/` — Reusable Process Documents

Generic process guardrails that apply to all projects using this infrastructure.

| File | Purpose |
|---|---|
| `DEFINITION_OF_DONE.md` | Task completion checklist (build, test, lint, term drift, docs, impact). |
| `CHANGE_IMPACT_CHECKLIST.md` | What a change might affect (spec, types, config, tests, docs, ADRs). |
| `REPOSITORY_CONVENTIONS.md` | File, module, docs, config, and API placement rules. |
| `CONFIG_CONSTANTS_POLICY.md` | No magic numbers, tunables in config, single-source defaults. |
| `AI_SESSION_BOOTSTRAP.md` | Template for project-specific AI session startup context. |
| `ARCHITECTURE_GUARDRAILS.md` | Framework for defining forbidden dependency patterns. |
| `SPEC_CODE_CONSISTENCY.md` | Framework for spec ↔ code validation. |
| `PROJECT_EXTENSIONS.md` | Defines what belongs in project repos vs. this template. |

### `.claude/commands/` — Command Templates

**Primary user commands:**

| File | Purpose |
|---|---|
| `next.md` | `/next` primary workflow command. References `docs/ai/runtime/STEP_*.md` for step definitions. |
| `pick.md` | `/pick` — evaluate a proposal and decide whether to adopt it. |
| `idea.md` | `/idea` — evaluate a new idea before it enters the task system. |
| `check.md` | `/check` — validate recent changes against infrastructure rules. |
| `critic.md` | `/critic` — challenge a design or proposal with strong skepticism. |

**Milestone command:**

| File | Purpose |
|---|---|
| `audit.md` | `/audit` — full project-level system audit for milestone or phase validation. |

**Internal modes** (normally invoked by `/next`):

| File | Purpose |
|---|---|
| `analyze.md` | `/analyze` — review and reason about design or architecture. |
| `design.md` | `/design` — create or modify system design. |
| `implement.md` | `/implement` — write application code. |

---

## Governance

- Any new document must be registered in this file before creation.
- Documents may only be deleted after confirming no other document references them.
- Cross-document references use relative paths.
- Changes to `SPEC.md` require an ADR in `docs/project/decisions/`.
- ADRs are immutable once accepted. To change, create a superseding ADR.
- Domain-specific features must follow extension architecture rules (when defined).
