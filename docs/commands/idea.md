# /idea — Evaluate a New Idea

Evaluate a new idea before it enters the design or task system. This command helps decide whether an idea is worth pursuing, needs more design, or should be deferred.

---

## Instructions for Claude

1. Read governance documents:
   - `docs/core/SPEC.md`
   - `docs/core/NON_GOALS.md`
   - `docs/core/ASSUMPTIONS.md`
   - `docs/project/TASKS.md`
   - Relevant ADRs from `docs/project/decisions/`

2. Perform the following evaluation steps:

### Step 1: Idea Summary
State the idea clearly in 1–3 sentences.

### Step 2: Value Analysis
- What problem does this solve?
- Who benefits?
- How significant is the impact?

### Step 3: Consistency with Existing System
- Does it conflict with SPEC.md?
- Does it conflict with NON_GOALS.md?
- Does it depend on or contradict ASSUMPTIONS.md?
- Does it contradict any accepted ADRs?
- Does it fit within the current project phase?

### Step 4: Over-Engineering Risk
- Is this solving a real problem or a hypothetical one?
- Could a simpler approach achieve the same goal?
- Does this add unnecessary complexity?

### Step 5: Dependency or Duplication Check
- Does this duplicate existing functionality or planned tasks?
- What dependencies would this introduce?
- Does it block or conflict with current work?

### Step 6: Recommendation

Provide one of:

| Recommendation | Meaning |
|---|---|
| **Strongly recommended** | High value, low risk, fits cleanly into the system. |
| **Recommended** | Good value, manageable complexity, should be pursued. |
| **Needs deeper design** | Promising but requires more analysis before committing. |
| **Postpone** | Valid idea but not the right time. Revisit in a later phase. |
| **Reject** | Conflicts with constraints, duplicates existing work, or adds unjustified complexity. |

3. **If the recommendation is "Strongly recommended" or "Recommended"**, specify how the idea should enter the system:

| Entry path | When to use |
|---|---|
| **Task** | Can be defined as a concrete task now. Specify suggested type, phase, and dependencies. |
| **Roadmap item** | Too large or distant for a task. Should be added to planning documents. |
| **Future phase feature** | Belongs in a later project phase. Note which phase and why. |

4. **Output structure**:

```
Idea: <summary>

Value: <high | medium | low>
Consistency: <ok | conflict with ...>
Over-engineering risk: <low | medium | high>
Duplication: <none | overlaps with ...>

Recommendation: <one of the five levels>
Entry path: <task | roadmap item | future phase feature>
Reasoning: <brief explanation>
```

5. Do NOT create tasks or modify documents. This command evaluates only.
