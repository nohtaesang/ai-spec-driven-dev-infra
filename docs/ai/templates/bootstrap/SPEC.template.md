# SPEC.md

## Purpose

This document defines the **non-negotiable architectural assumptions** of {{PROJECT_NAME}}.

All design, documentation, and implementation must remain consistent with this specification.

If a change would violate this document, the change must be reviewed and explicitly approved through an ADR in `docs/project/decisions/`.

This document should remain **short and stable**.

---

# 1. System Scope

{{SYSTEM_SCOPE}}

---

# 2. Core Capabilities

{{#each CAPABILITIES}}
## SPEC-{{NNN}}: {{CAPABILITY_NAME}}

{{CAPABILITY_CONSTRAINT}}

{{/each}}

---

# 3. Performance Constraints

{{#if PERFORMANCE_CONSTRAINTS}}
{{PERFORMANCE_CONSTRAINTS}}
{{else}}
*To be defined in Phase 1 design tasks.*
{{/if}}

---

# 4. Integration Constraints

{{#if INTEGRATION_CONSTRAINTS}}
{{INTEGRATION_CONSTRAINTS}}
{{else}}
*To be defined in Phase 1 design tasks.*
{{/if}}

---

# 5. Specification Enforcement

This document is the **highest-level constraint** in the system.

Rules:

* No document or implementation may contradict this specification.
* If a change requires modifying this specification, it must be recorded as an ADR in `docs/project/decisions/`.
* Claude must stop and report any conflict with this specification.
