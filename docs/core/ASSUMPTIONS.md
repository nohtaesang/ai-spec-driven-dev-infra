<!-- BOOTSTRAP:PENDING -->
# Assumptions

This document captures the important assumptions that guide system design. These are not hard constraints like SPEC.md — they represent the expected operating conditions and usage patterns that inform architectural and design choices.

---

## How to Use This Document

- Assumptions guide design decisions but do not override SPEC.md.
- If a design choice depends on an assumption listed here, reference it explicitly.
- If an assumption changes significantly, create an ADR file in `docs/project/decisions/` and update `DECISIONS.md` index before modifying this document.
- Assumptions may evolve as the project matures. They are not immutable.

---

<!--
PROJECT SETUP INSTRUCTIONS:

Add your project's design assumptions, organized by category.

Example categories:
- Data Assumptions (data sizes, formats, quality expectations)
- Workflow Assumptions (how users interact with the system)
- Deployment Assumptions (where and how the system runs)

Each assumption should be numbered for easy reference.
-->

---

## Relationship to Other Documents

| Document | Relationship |
|---|---|
| `SPEC.md` | SPEC defines hard constraints. Assumptions provide softer context. SPEC always wins on conflict. |
| `NON_GOALS.md` | Non-goals define what we are NOT building. Assumptions describe what we expect to be true. |

---

*If an assumption no longer holds, propose the change explicitly. Do not silently design against a listed assumption.*
