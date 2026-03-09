# /pick — Evaluate and Decide on a Proposal

Evaluate the answer or proposal that Claude just produced and decide whether it should be adopted.

---

## Instructions for Claude

1. **Summarize the proposal** — what is being proposed and what it would change.

2. **List alternatives** — if other options exist, enumerate them briefly.

3. **Evaluate against governance constraints**:
   - **SPEC conformance** — does the proposal respect SPEC.md?
   - **Non-goal boundary** — does it conflict with NON_GOALS.md?
   - **Assumption alignment** — does it depend on or contradict ASSUMPTIONS.md?
   - **ADR consistency** — does it align with accepted ADRs in `docs/project/decisions/`?
   - **Workflow constraints** — does it fit within the current task, phase, and dependency structure?

4. **Recommend the best option** — select the strongest choice and explain why.

5. **Output structure**:

```
Evaluation:
- <summary of proposal>

Options:
1. <option> — <brief assessment>
2. <option> — <brief assessment>

Recommended choice: <option number>

Reasoning:
- <why this option is best>

Workflow compliance:
- SPEC: ok | issue
- Non-goals: ok | issue
- Assumptions: ok | issue
- ADRs: ok | issue
- Task fit: ok | issue
```

6. Do NOT apply changes. This command evaluates only. Use `/next` to proceed with execution.
