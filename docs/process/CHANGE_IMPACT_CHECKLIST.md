# Change Impact Checklist

Before completing any task, review whether the change affects any of the following areas. Check all that apply and ensure each affected area has been updated.

## Spec & Design

- [ ] **SPEC.md** — Does this change affect non-negotiable constraints? (Requires ADR)
- [ ] **DEFINITIONS.md** — Does this change introduce, rename, or redefine domain terms?
- [ ] **Design documents** — Do model, architecture, or UX documents need updating?
- [ ] **NON_GOALS.md** — Does this change conflict with declared non-goals?
- [ ] **ASSUMPTIONS.md** — Does this change depend on or invalidate an assumption? (Requires ADR)

## Core Types & Interfaces

- [ ] **Core type definitions** — Are domain types added, modified, or removed?
- [ ] **Public API surface** — Are any public interfaces changed?
- [ ] **Cross-module contracts** — Do module boundaries or dependencies shift?

## Configuration & Constants

- [ ] **Config values** — Are new configurable values introduced?
- [ ] **Magic numbers** — Are there unexplained literal values? (See `CONFIG_CONSTANTS_POLICY.md`)
- [ ] **Defaults** — Are default values added or changed?

## Tests & Validation

- [ ] **Existing tests** — Do any existing tests need updating?
- [ ] **New test coverage** — Does new behavior need tests?
- [ ] **Test fixtures** — Do test data fixtures need updating? (Project-level)

## Documentation & Tracking

- [ ] **TASKS.md** — Is the task status updated?
- [ ] **DONE.md** — Is a completion entry needed?
- [ ] **DECISIONS.md** — Is a new ADR needed?
- [ ] **Process documents** — Do any process docs need updating?

## Project-Level Extensions

- [ ] **Performance guardrails** — Does this change affect hot paths? (Project-defined)
- [ ] **Benchmarks** — Do benchmarks need updating? (Project-level)
- [ ] **Fixtures** — Do test data fixtures need updating? (Project-level)

## Usage

This checklist is referenced during task completion (see `DEFINITION_OF_DONE.md`) and by `/analyze` and `/audit` commands. Not every item applies to every task — check only what is relevant.
