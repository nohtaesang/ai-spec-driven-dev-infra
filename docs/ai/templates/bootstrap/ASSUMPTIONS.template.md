# Assumptions

These assumptions guide design decisions but are softer than SPEC.md. They can evolve — but not silently. Changes require an ADR.

---

## Platform & Runtime

{{#if TECH_STACK}}
- {{TECH_STACK_ASSUMPTIONS}}
{{else}}
- *To be decided in Phase 1.*
{{/if}}

## Deployment

{{#if DEPLOYMENT_TARGET}}
- {{DEPLOYMENT_ASSUMPTIONS}}
{{else}}
- *To be decided in Phase 1.*
{{/if}}

## Dependencies

{{#if INTEGRATION_CONSTRAINTS}}
- {{DEPENDENCY_ASSUMPTIONS}}
{{else}}
- *No external dependencies assumed yet.*
{{/if}}

## Open Questions

{{#each OPEN_QUESTIONS}}
- {{QUESTION}}
{{/each}}
