# AI Spec-Driven Development Infrastructure

A reusable governance and workflow infrastructure for building software projects with AI collaboration (Claude Code).

## What is this?

This repository provides a **spec-driven development workflow** — a structured system where:

- A **SPEC.md** defines non-negotiable architectural constraints
- A **document hierarchy** enforces that higher-level decisions constrain lower-level ones
- An **8-step `/next` pipeline** automates context restoration, task selection, execution, analysis, and audit
- **Architecture Decision Records (ADRs)** capture binding decisions
- **Automatic governance checks** prevent specification violations, scope creep, and architectural drift

The system is designed so that a human only needs to type `/next` to drive all project work. All governance enforcement is automatic.

## How to start a project using this infrastructure

1. **Clone or copy** this repository as your project's starting point.

2. **Fill in the foundation documents**:
   - `docs/core/SPEC.md` — Define your project's non-negotiable architectural constraints
   - `docs/core/VISION.md` — Define why the project exists
   - `docs/core/PRINCIPLES.md` — Add your design principles
   - `docs/core/ASSUMPTIONS.md` — List your design assumptions
   - `docs/core/NON_GOALS.md` — Define what you are NOT building
   - `docs/core/DEFINITIONS.md` — Add domain terms as they emerge

3. **Start working** by typing `/next` in a Claude Code session. The pipeline will:
   - Read all governance documents
   - Report the current project state
   - Select the next task from `TASKS.md`
   - Execute it with full governance checks
   - Run automatic analysis and audit
   - Track completion

4. **Add project-specific documents** as tasks are completed:
   - Model documents in `docs/model/`
   - Architecture documents in `docs/architecture/`
   - UX documents in `docs/ux/`
   - Planning documents in `docs/planning/`
   - Register new documents in `docs/ai/DOCUMENT_SYSTEM.md`

## Repository structure

```
CLAUDE.md                          ← Claude Code entrypoint (auto-loaded)
README.md                          ← This file
docs/
  ai/
    CLAUDE.md                      ← Authoritative workflow and behavioral rules
    DOCUMENT_SYSTEM.md             ← Document registry and hierarchy
    CHANGE_PROTOCOL.md             ← State transitions and change process
  commands/
    next.md                        ← /next primary workflow command
    pick.md                        ← /pick evaluate a proposal
    idea.md                        ← /idea evaluate a new idea
    check.md                       ← /check validate recent changes
    critic.md                      ← /critic challenge a design
    audit.md                       ← /audit full project system audit
    analyze.md                     ← /analyze internal mode
    design.md                      ← /design internal mode
    implement.md                   ← /implement internal mode
  core/
    SPEC.md                        ← Non-negotiable constraints (fill in)
    VISION.md                      ← Project vision (fill in)
    PRINCIPLES.md                  ← Design principles (fill in)
    ASSUMPTIONS.md                 ← Design assumptions (fill in)
    NON_GOALS.md                   ← Scope boundaries (fill in)
    DEFINITIONS.md                 ← Glossary (grows over time)
  project/
    TASKS.md                       ← Task tracking (source of truth)
    DONE.md                        ← Completion log
    DECISIONS.md                   ← ADR index
    decisions/                     ← Individual ADR files
```

## Commands

### Primary

| Command | Purpose |
|---|---|
| `/next` | **Run the full pipeline** for the next task. The default for all work. |
| `/pick` | Evaluate a proposal and decide whether to adopt it. |
| `/idea` | Evaluate a new idea before it enters the task system. |
| `/check` | Validate recent changes against infrastructure rules. |
| `/critic` | Challenge a design or proposal with strong skepticism. |

### Milestone

| Command | Purpose |
|---|---|
| `/audit` | Full project-level system audit. Use at phase boundaries. |

### Internal Modes

These are invoked internally by `/next` based on task type. Available for standalone use when needed.

| Command | Purpose |
|---|---|
| `/analyze` | Review and reason about design or architecture. |
| `/design` | Create or modify system design. |
| `/implement` | Write application code. |

## Key concepts

- **`/next`** is the primary workflow command. It runs the full 8-step pipeline.
- **SPEC.md** is the highest-level constraint. Nothing may contradict it.
- **Document hierarchy**: `SPEC → DEFINITIONS → Models → Architecture → Code`. Higher constrains lower.
- **ADRs** capture architectural decisions as immutable records.
- **Automatic analysis and audit** run after every task to catch drift.
- **One task at a time.** Dependencies are enforced. Progress is tracked across sessions.

## Governance at a glance

| Change to... | Requires... |
|---|---|
| SPEC.md | ADR file before modification |
| NON_GOALS.md | ADR file before modification |
| ASSUMPTIONS.md | ADR file before modification |
| Architecture | ADR file + SPEC conformance check |
| Any document | Hierarchy check + conflict check |
