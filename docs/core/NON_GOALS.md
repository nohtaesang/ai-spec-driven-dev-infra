# Non-Goals

This document explicitly defines what the project is **not** trying to build. It exists to prevent scope creep and to give Claude a clear boundary for feature proposals.

**If a proposed feature conflicts with this document, Claude must stop and flag the conflict.**

---

## How to Use This Document

- Before proposing a new feature, check that it does not fall under a non-goal.
- If a non-goal should change, create an ADR file in `docs/project/decisions/` and update `DECISIONS.md` index before updating this document.
- Non-goals are not permanent rejections — they define what is out of scope *now*. They may be revisited as the project evolves.

---

## Non-Goals

<!--
PROJECT SETUP INSTRUCTIONS:

List what your project is NOT building. Each non-goal should have:
- A clear title
- A brief explanation of what is excluded and why

Example:
### 1. Example Non-Goal Title
Brief explanation of something intentionally excluded from the system and why it is out of scope.
-->

---

## Boundary Rule

Non-goals act as a boundary for feature proposals:

- **Feature clearly within a non-goal** → reject and reference this document.
- **Feature adjacent to a non-goal** → flag, discuss scope, and decide whether it crosses the boundary.
- **Feature that would require changing a non-goal** → propose the change through an ADR first.

---

## Relationship to Other Documents

| Document | Relationship |
|---|---|
| `SPEC.md` | SPEC defines what the system IS. Non-goals define what it is NOT. |
| `ASSUMPTIONS.md` | Assumptions describe expected conditions. Non-goals describe excluded scope. |

---

*Non-goals can evolve. But they must be explicitly changed — never silently ignored.*
