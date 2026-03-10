# Definition of Done — Task Completion Checklist

Every implementation task must satisfy this checklist before being marked `[x]`.

## Build & Check

- [ ] Code compiles without errors
- [ ] No new compiler warnings introduced
- [ ] Linter passes (project-defined lint rules)

## Tests

- [ ] Existing tests pass
- [ ] New tests added for new behavior
- [ ] Edge cases covered where applicable

## Architecture Compliance

- [ ] No forbidden dependency patterns introduced (see `ARCHITECTURE_GUARDRAILS.md`)
- [ ] Module/crate boundaries respected
- [ ] Performance guardrails not violated (project-defined)

## Term Drift Review

- [ ] All new domain terms registered in `docs/core/DEFINITIONS.md`
- [ ] No undefined domain terminology introduced in documents or public APIs
- [ ] Existing term definitions not contradicted

## Documentation Update Review

- [ ] Relevant design documents updated to reflect changes
- [ ] TASKS.md updated with progress
- [ ] ADR created if an architectural decision was made
- [ ] DONE.md entry added upon completion

## Change Impact Review

- [ ] Change impact checklist reviewed (see `CHANGE_IMPACT_CHECKLIST.md`)
- [ ] No SPEC.md violations
- [ ] No non-goal conflicts

## Final Gate

- [ ] `/analyze` passes
- [ ] `/audit` passes (or issues explicitly acknowledged)
- [ ] Task marked `[x]` in TASKS.md
