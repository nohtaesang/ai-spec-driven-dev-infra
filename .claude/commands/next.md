# /next — Primary Workflow Command

`/next` is the primary command for all project work. It runs the full workflow pipeline automatically.

**The authoritative pipeline definition is in [`docs/ai/CLAUDE.md`](../docs/ai/CLAUDE.md).** This file is a concise reference only. If there is any conflict, `CLAUDE.md` governs.

---

## Quick Reference

```
/next
  │
  ├─ 0. Bootstrap detection (if SPEC.md has BOOTSTRAP:PENDING → run bootstrap protocol)
  ├─ 1. Restore context (7 files: SPEC, NON_GOALS, ASSUMPTIONS, DOCUMENT_SYSTEM, CLAUDE, DEFINITIONS, TASKS)
  ├─ 2. Report state (phase, task, progress, governance status, 5 conflict checks)
  ├─ 3. Detect [-] or select next [ ]  →  set [-]  →  write progress: started
  ├─ 4. Load task-type context (design / implement / document)
  ├─ 5. Execute task (verify SPEC + non-goals + assumptions + ADRs + extensions + perf)
  ├─ 6. Auto-analysis (6 named checks, stop on VIOLATION)
  ├─ 7. Auto-audit (13-point consistency check, stop on red)
  └─ 8. Complete  →  [x] + DONE.md + ADR file + DECISIONS.md
```

## Step 0: Bootstrap

When the repository is in template state (SPEC.md contains `<!-- BOOTSTRAP:PENDING -->` and no tasks are in progress or completed), `/next` enters bootstrap mode automatically.

Bootstrap asks structured intake questions, generates foundation documents, selects Level-2 documents, and initializes Phase 1 tasks. See [`docs/ai/BOOTSTRAP_PROTOCOL.md`](../docs/ai/BOOTSTRAP_PROTOCOL.md) for the full protocol.

## `/next` (no arguments)

Runs all 8 steps. See `docs/ai/CLAUDE.md` → "The `/next` Pipeline" for full step definitions.

## `/next <new request>`

Steps 1–2 run the same. Then the request is classified:

- **(a) Continuation** — relates to current `[-]` task → continue from Step 4.
- **(b) New task** — no conflict → add to `TASKS.md`. If no `[-]` and deps met, start. If `[-]` exists, ask user.
- **(c) Conflict** — contradicts SPEC.md, NON_GOALS.md, ADRs, or plans → stop and report.

See `docs/ai/CLAUDE.md` → "`/next <new request>`" for full classification rules.

---

## Governance Status

`/next` reports governance status in Step 2 so users understand whether the project has entered the governed design phase.

When core governance documents are still placeholders:

```
Phase: Phase 0 — Project Setup
Last completed: none
In progress: none
Next eligible: TASK-001 Define project specification

Governance: inactive

SPEC conflicts: none found
Non-goal conflicts: none found
```

`inactive` means "no constraints defined yet" — not "no violations found." Governance becomes `active` once `SPEC.md` contains real project constraints.

---

## Related Commands

| Command | Purpose |
|---|---|
| `/next` | **Primary.** Run the full pipeline for the next task. |
| `/pick` | Evaluate a proposal and decide whether to adopt it. |
| `/idea` | Evaluate a new idea before it enters the task system. |
| `/check` | Validate recent changes against infrastructure rules. |
| `/critic` | Challenge a design or proposal with strong skepticism. |
| `/audit` | Full project-level system audit (milestone use). |
