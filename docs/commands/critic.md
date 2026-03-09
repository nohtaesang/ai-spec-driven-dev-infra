# /critic — Challenge a Design or Proposal

Challenge the current design or proposal at a fundamental level. This command deliberately applies **strong skepticism** to expose risks, hidden assumptions, and unnecessary complexity.

---

## Instructions for Claude

1. Read the design or proposal under review, plus relevant governance documents:
   - `docs/core/SPEC.md`
   - `docs/core/ASSUMPTIONS.md`
   - `docs/core/NON_GOALS.md`
   - Relevant ADRs from `docs/project/decisions/`
   - Any architecture or model documents the design depends on

2. Apply strong skepticism across four dimensions:

### Structural Risks
- What could go wrong architecturally?
- Are there single points of failure?
- What happens under unexpected conditions?
- Are there implicit ordering or timing dependencies?

### Hidden Assumptions
- What is the design assuming that is not stated in ASSUMPTIONS.md?
- Are there assumptions about scale, usage patterns, or environment?
- What happens if those assumptions are wrong?

### Simpler Alternatives
- Could the same goal be achieved with less complexity?
- Is this over-engineered for the current phase?
- Would a simpler approach be sufficient for now, with room to evolve?

### Final Assessment
- Overall risk level: low / medium / high
- Most critical concern
- Whether to proceed, revise, or reconsider

3. **Output structure**:

```
Target: <what is being critiqued>

Structural risks:
- <risk>

Hidden assumptions:
- <assumption not in ASSUMPTIONS.md>

Simpler alternatives:
- <alternative approach>

Final assessment:
- Risk level: <low | medium | high>
- Critical concern: <most important issue>
- Recommendation: <proceed | revise | reconsider>
```

4. Do NOT make changes. This command is adversarial review only.
