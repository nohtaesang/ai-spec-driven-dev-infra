# AI Spec-Driven Development Infrastructure — Claude Code Project Rules

This is the root-level instruction file for Claude Code sessions using AI Spec-Driven Development.

## First Action in Every Session

Run `/next`. That's it.

`/next` runs the full pipeline automatically:
0. Detect template state → if still a template, run bootstrap (structured intake → generate foundation docs → select Level-2 docs → initialize Phase 1 tasks)
1. Restore project context (SPEC.md first — it constrains everything)
2. Report current state, SPEC conflicts, and ADR status
3. Detect or select the next task
4. Execute the task (verify SPEC, ADRs, extension boundary, performance constraints)
5. Run automatic analysis
6. Run automatic audit
7. Mark task complete, create ADRs if needed, update tracking

If you have a specific request: `/next <your request>`.

## Document Hierarchy

```
SPEC.md  →  DEFINITIONS.md  →  Models  →  UX / Architecture / Extensions  →  Code
```

Higher constrains lower. SPEC.md is non-negotiable. ADRs constrain downstream design.

## Core Rules

1. **`/next` is the primary workflow command.** All task work flows through it.
2. **SPEC.md is supreme.** No document or code may contradict it. Violations halt work.
3. **Check ADRs before changing architecture.** ADRs in `docs/project/decisions/` record binding decisions.
4. **Respect the extension boundary.** Domain-specific features go in extensions, not core. See `docs/architecture/EXTENSIONS.md` (when created).
5. **Respect performance constraints.** See SPEC.md performance section.
6. **Documentation before code.** Read docs first. Update docs before implementing.
7. **Single source of truth.** Each concept defined in one place.
8. **Track everything.** `TASKS.md` = progress. `DECISIONS.md` = ADR index. `DONE.md` = log.
9. **One task at a time.** Max one `[-]`. Never skip dependencies.
10. **Analyze and audit automatically.** After every task. Never skip.

## Commands

### Primary

| Command | Purpose |
|---|---|
| `/next` | **Run the full pipeline** for the next task. The default for all work. |
| `/next <request>` | Run the pipeline with a specific request or direction. |
| `/pick` | Evaluate a proposal and decide whether to adopt it. |
| `/idea` | Evaluate a new idea before it enters the task system. |
| `/check` | Validate recent changes against infrastructure rules. |
| `/critic` | Challenge a design or proposal with strong skepticism. |

### Milestone

| Command | Purpose |
|---|---|
| `/audit` | Full project-level system audit. Use at phase boundaries. |

### Internal Modes

| Command | Purpose |
|---|---|
| `/analyze` | Analysis mode. Normally invoked internally by `/next`. |
| `/design` | Design mode. Normally invoked internally by `/next`. |
| `/implement` | Implementation mode. Normally invoked internally by `/next`. |

## Domain Term Registration

All domain terminology must be registered in `docs/core/DEFINITIONS.md`. This applies to every design document (SPEC, models, architecture, UX, extensions).

1. **Register new terms immediately.** When a new domain term appears in any document, add it to DEFINITIONS.md before closing the task.
2. **No undefined terminology.** Documents must not use domain terms absent from DEFINITIONS.md. Define first, then use.
3. **Detect term drift.** During `/analyze` and `/audit`, scan for terms that appear to be domain concepts but are missing from DEFINITIONS.md. Flag as **"term drift"**.
4. **Gate task completion.** Before closing any design task, verify all newly introduced terms are registered. Missing registrations block completion.

## Process Documents

Reusable process guardrails are in `docs/process/`:

| Document | Purpose |
|---|---|
| `DEFINITION_OF_DONE.md` | Task completion checklist |
| `CHANGE_IMPACT_CHECKLIST.md` | What a change might affect |
| `REPOSITORY_CONVENTIONS.md` | File and module placement rules |
| `CONFIG_CONSTANTS_POLICY.md` | Magic numbers and config policy |
| `AI_SESSION_BOOTSTRAP.md` | New AI session startup context |
| `ARCHITECTURE_GUARDRAILS.md` | Framework for defining forbidden dependencies |
| `SPEC_CODE_CONSISTENCY.md` | Framework for spec ↔ code validation |
| `FEATURE_REGISTRY.md` | Framework for feature/test/flag drift prevention (optional — see adoption criteria) |
| `PROJECT_EXTENSIONS.md` | What belongs in project repos, not this template |

## Project Phase

See `docs/project/TASKS.md` for current phase and active work.
