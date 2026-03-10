# Principles

## Design Principles

{{#each DESIGN_PRINCIPLES}}
### {{PRINCIPLE_NAME}}

{{PRINCIPLE_DESCRIPTION}}

{{/each}}

---

## Engineering Principles

### Documentation Before Code
Read docs first. Update docs before implementing. Code follows design.

### Single Source of Truth
Each concept is defined in exactly one document. Reference, don't duplicate.

### Hierarchy Enforcement
Higher documents constrain lower documents. SPEC.md is supreme.

### Explicit Over Implicit
State assumptions. Record decisions. Reference documents by path.
