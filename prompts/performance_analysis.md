# Prompt Template: Performance Analysis

## Analysis Target

- **Component/System**: [What to analyze]
- **Observed issue**: [e.g., frame drops, high memory usage, slow loading]
- **Measurement**: [Any existing data — latency, throughput, memory]

## Investigation Steps

1. [ ] Identify the hot path (what runs frequently vs. on demand)
2. [ ] Check for guardrail violations in the hot path
3. [ ] Profile memory allocation patterns
4. [ ] Measure actual vs. target latency
5. [ ] Identify the bottleneck (CPU, GPU, I/O, memory)

## Common Anti-Patterns

- I/O in a hot path (file reads, network calls in tight loops)
- Unnecessary deep copies of large data
- Unbounded growth (push without limit in per-iteration code)
- Blocking async operations on a time-sensitive thread
- Repeated allocation/deallocation in tight loops
- O(n) operations where O(1) or O(log n) is possible

## Output

- Bottleneck identification with evidence
- Guardrail violations found (if any)
- Optimization recommendations (ordered by impact)
- Updated benchmark targets if needed
