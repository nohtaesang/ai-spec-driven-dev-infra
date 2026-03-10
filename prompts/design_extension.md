# Prompt Template: Design Extension

## Extension Identity

- **Name**: [Extension name]
- **Purpose**: [One-line description]
- **Target location**: [Where it will live in the project]

## Context

- **Motivation**: [Why this extension is needed]
- **Related components**: [What it integrates with]
- **User-facing behavior**: [What users will see/do differently]

## Constraints

1. [ ] Must not modify core interfaces without an ADR
2. [ ] Must respect the extension boundary (domain-specific → extensions, not core)
3. [ ] Must not introduce forbidden dependency patterns
4. [ ] Must not violate performance guardrails
5. [ ] Must register all new domain terms in DEFINITIONS.md

## Deliverables

1. Design document describing the extension's architecture
2. Interface specification — how it connects to existing modules
3. New type definitions (must be registered in DEFINITIONS.md)
4. ADR if architectural decisions are made

## Questions to Address

1. What existing types/interfaces does this extension consume?
2. What new types does it introduce?
3. How does it affect hot paths (if at all)?
4. What test fixtures are needed?
5. What is the minimum viable scope?
