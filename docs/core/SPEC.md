<!-- BOOTSTRAP:PENDING -->
# SPEC.md

## Purpose

This document defines the **non-negotiable architectural assumptions** of the project.

All design, documentation, and implementation must remain consistent with this specification.

If a change would violate this document, the change must be reviewed and explicitly approved through an ADR in `docs/project/decisions/`.

This document should remain **short and stable**.

---

<!--
PROJECT SETUP INSTRUCTIONS:

Replace the sections below with your project's actual architectural constraints.
Each section should define a non-negotiable rule that all design and code must follow.

SPEC Clause IDs:
- Number each constraint clause as SPEC-NNN (e.g., SPEC-001, SPEC-002).
- Other documents reference SPEC clauses by ID (e.g., "per SPEC-003").
- IDs are stable — do not renumber. Deprecated clauses are marked, not removed.

Example sections you might include:
- System Scope (what the system is)
- Data Model (core entities and relationships)
- Performance Constraints (scalability requirements)
- Core vs Extension boundary
- Architectural Principles

Keep it short. SPEC.md defines constraints, not designs.
Design details belong in model and architecture documents.
-->

# 1. System Scope

*Define what your system is and what it must support.*

---

# 2. Specification Enforcement

This document is the **highest-level constraint** in the system.

Rules:

* No document or implementation may contradict this specification.
* If a change requires modifying this specification, it must be recorded as an ADR in `docs/project/decisions/`.
* Claude must stop and report any conflict with this specification.
