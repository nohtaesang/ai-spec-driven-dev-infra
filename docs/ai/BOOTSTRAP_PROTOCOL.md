# Bootstrap Protocol

This document defines how `/next` bootstraps a new project from template state to Level-2 readiness.

---

## When Bootstrap Activates

`/next` enters bootstrap mode when **all** of the following are true:

1. `docs/core/SPEC.md` contains the marker `<!-- BOOTSTRAP:PENDING -->`
2. No tasks in `TASKS.md` are `[-]` or `[x]`

This means the repository is still in template state — no project work has started.

Bootstrap runs **once**. After completion, the marker is removed and `/next` follows the normal pipeline.

---

## Bootstrap Steps

### B1: Welcome

Display:

```
=== Project Bootstrap ===

This repository uses AI Spec-Driven Development.
I'll guide you through project setup in two rounds,
then generate your foundation documents.

Let's start with the project basics.
```

---

### B2: Round 1 — Project Identity

Ask these 7 questions. All are required.

```
Round 1: Project Identity

1. Project name — What is this project called?
2. One-line description — What does it do in one sentence?
3. Project type — Choose: tool/CLI, web app/SaaS, library/framework,
   mobile app, game/simulation, data pipeline, other
4. Target users — Who will use this?
5. Core problem — What problem does it solve?
6. Key capabilities — List 3–5 things it must do.
7. Non-goals — List at least 1 thing it will NOT do.
```

If any required field is missing or unclear, ask a targeted follow-up. Do not proceed until all 7 are answered.

---

### B3: Round 1 Summary + Confirmation

After all Round 1 answers are collected, produce a **concise summary block** and ask for explicit confirmation.

```
=== Round 1 Summary ===

Project: <name>
Description: <one-line>
Type: <type>
Users: <target users>
Problem: <core problem>
Must do:
  - <capability 1>
  - <capability 2>
  - ...
Will NOT do:
  - <non-goal 1>
  - ...

Is this correct? Say "yes" to continue, or tell me what to change.
```

**Do not proceed to Round 2 until the user confirms.** If the user requests changes, update the summary and re-confirm.

---

### B4: Round 2 — Technical Constraints

Only after Round 1 is confirmed, ask:

```
Round 2: Technical Constraints

These are optional. Skip any you haven't decided yet.

8. Tech stack — Language, framework, platform?
9. Performance constraints — Any hard performance requirements?
10. Integration constraints — Must it integrate with specific systems?
11. Deployment target — Where will it run?
```

Accept whatever the user provides. Missing answers default to "to be decided in Phase 1."

---

### B5: Generate and Review Foundation Documents

Using both rounds of intake, generate initial content for all 6 core documents.

**Generation mapping:**

| Document | Source fields | What to generate |
|---|---|---|
| `SPEC.md` | Capabilities, tech stack, performance, integrations | Non-negotiable architectural constraints. Each capability becomes a SPEC entry. Tech choices become constraints. |
| `VISION.md` | Name, description, problem, target users | Why the project exists, who it serves, what success looks like. |
| `PRINCIPLES.md` | Project type, constraints | Design principles appropriate to the project type. Preserve the existing Engineering Principles section from the template. |
| `ASSUMPTIONS.md` | Tech stack, deployment, integrations | Operating assumptions about platform, runtime, dependencies. Items marked "to be decided" become explicit open questions. |
| `NON_GOALS.md` | Non-goals from Round 1 | Explicit scope boundaries with explanations. |
| `DEFINITIONS.md` | Key terms from all answers | Initial glossary seeded from intake vocabulary. |

**Review flow (3 sub-steps):**

**B5a: Summary table.** Show a concise overview first — not full documents.

```
=== Foundation Documents ===

| Document        | Key content                                        |
|-----------------|----------------------------------------------------|
| SPEC.md         | <2-3 line summary of constraints generated>        |
| VISION.md       | <1 line: the vision statement core>                |
| PRINCIPLES.md   | <count> design principles + 4 engineering preserved |
| ASSUMPTIONS.md  | <count> assumptions, <count> open questions         |
| NON_GOALS.md    | <count> non-goals defined                          |
| DEFINITIONS.md  | <count> terms defined                              |

Want to review any document in detail before approving?
Name the documents to review, or say "approve" to accept all.
```

**B5b: Focused review.** If the user names specific documents, show the full content of only those documents. Accept edit requests. Revise and re-show until the user is satisfied.

**B5c: Final approval.** After focused review (or if the user said "approve" immediately):

```
All foundation documents ready. Writing files now.
```

Write all 6 files. Remove `<!-- BOOTSTRAP:PENDING -->` and `<!-- PROJECT SETUP INSTRUCTIONS -->` blocks from each.

---

### B6: Create ADRs for Technology Choices

If the user specified technology choices in Round 2:

1. Create an ADR file in `docs/project/decisions/` for each significant choice
2. Update `docs/project/DECISIONS.md` index
3. Show the ADR(s) to the user (informational — no separate approval needed since the tech choices were already confirmed in the intake)

If no technology choices were made, skip this step.

---

### B7: Select Level-2 Documents

Based on the project type, present recommended Level-2 documents:

| Project Type | Recommended documents |
|---|---|
| tool/CLI | `docs/model/DATA_MODEL.md`, `docs/architecture/ARCHITECTURE.md`, `docs/ux/CLI_INTERFACE.md`, `docs/planning/SCOPE.md` |
| web app/SaaS | `docs/model/DOMAIN_MODEL.md`, `docs/model/API_MODEL.md`, `docs/architecture/SYSTEM_ARCHITECTURE.md`, `docs/architecture/API_DESIGN.md`, `docs/ux/SCREENS.md`, `docs/planning/SCOPE.md` |
| library/framework | `docs/model/API_MODEL.md`, `docs/architecture/MODULE_ARCHITECTURE.md`, `docs/ux/DEVELOPER_EXPERIENCE.md`, `docs/planning/SCOPE.md` |
| mobile app | `docs/model/DOMAIN_MODEL.md`, `docs/architecture/SYSTEM_ARCHITECTURE.md`, `docs/ux/SCREENS.md`, `docs/planning/SCOPE.md` |
| game/simulation | `docs/model/GAME_STATE_MODEL.md`, `docs/architecture/ENGINE_ARCHITECTURE.md`, `docs/ux/PLAYER_EXPERIENCE.md`, `docs/planning/SCOPE.md` |
| data pipeline | `docs/model/DATA_MODEL.md`, `docs/model/SCHEMA.md`, `docs/architecture/PIPELINE_ARCHITECTURE.md`, `docs/planning/SCOPE.md` |
| other | `docs/model/DOMAIN_MODEL.md`, `docs/architecture/ARCHITECTURE.md`, `docs/planning/SCOPE.md` |

```
=== Level-2 Documents ===

Based on your project type (<type>), I recommend these design documents
for Phase 1:

  - docs/planning/SCOPE.md — MVP scope and boundaries
  - docs/model/<X>.md — <purpose>
  - docs/architecture/<X>.md — <purpose>
  - docs/ux/<X>.md — <purpose>

Accept this list? You can add, remove, or modify.
```

**Wait for user approval.** After approval, for each accepted document:
1. Create a placeholder file with title and `<!-- BOOTSTRAP:PLACEHOLDER -->` marker
2. Register it in `docs/ai/DOCUMENT_SYSTEM.md`

---

### B8: Complete Phase 0 + Initialize Phase 1

After Level-2 documents are approved:

1. Mark all Phase 0 tasks (TASK-001 through TASK-004) as `[x]` in TASKS.md
2. Append completions to DONE.md
3. Create Phase 1 design tasks in TASKS.md:
   - One `type:design` task per selected Level-2 document
   - If `docs/planning/SCOPE.md` was selected, its task is first with `depends: none`
   - All other Phase 1 tasks depend on the SCOPE task (if it exists) or have `depends: none`
4. Update `*Next task ID*` at the bottom of TASKS.md

---

### B9: Report

Output:

```
=== Bootstrap Complete ===

Project: <name>
Type: <type>
Foundation: 6 documents written
ADRs: <count> created
Phase 1: <count> design tasks queued

  Next up: TASK-<NNN> <first Phase 1 task name>

Run `/next` to start Phase 1.
```

---

## Approval Checkpoints Summary

Bootstrap has **3 explicit approval points** where the user must confirm before proceeding:

| Checkpoint | What is approved | When |
|---|---|---|
| Round 1 confirmation | Project identity and scope | After B3 |
| Foundation doc approval | All 6 generated documents (summary → focused review → approve) | After B5 |
| Level-2 doc approval | Selected design documents for Phase 1 | After B7 |

No files are written and no tasks are modified until the relevant approval is given.

---

## After Bootstrap

The next `/next` call will:
1. Step 0: SPEC.md no longer has `BOOTSTRAP:PENDING` → skip bootstrap
2. Steps 1–2: Normal context restore + state report (`Governance: active`)
3. Step 3: Select the first Phase 1 task (all Phase 0 deps met)
4. Steps 4–8: Normal pipeline — load context, execute, analyze, audit, complete
