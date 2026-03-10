# Prompt Template: Architecture Review

## Review Target

- **Document/Component**: [What is being reviewed]
- **Related ADRs**: [Any relevant decision records]

## Review Checklist

### Spec Conformance
- [ ] Does not contradict SPEC.md
- [ ] Respects NON_GOALS.md boundaries
- [ ] Consistent with ASSUMPTIONS.md

### Architectural Integrity
- [ ] Respects module/layer boundaries (see `docs/process/ARCHITECTURE_GUARDRAILS.md`)
- [ ] No forbidden dependency patterns introduced
- [ ] Clear separation of concerns

### Performance
- [ ] Hot paths free of I/O and blocking operations
- [ ] No unnecessary deep copies of large data
- [ ] Scaling characteristics documented

### Domain Consistency
- [ ] All domain terms registered in DEFINITIONS.md
- [ ] Type names match spec definitions
- [ ] No terminology drift

## Questions to Answer

1. What are the main architectural trade-offs?
2. Are there hidden coupling risks?
3. Does this create future extensibility problems?
4. What would break if requirements changed?

## Output

- Assessment: APPROVED / NEEDS REVISION / BLOCKED
- Specific issues found (with guardrail references)
- Suggested improvements
