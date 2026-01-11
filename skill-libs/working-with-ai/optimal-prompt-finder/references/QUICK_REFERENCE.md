# Quick Reference

Fast lookup for all prompt engineering techniques. For detailed examples, see references/examples.md.

## Technique Selection Matrix

| Your Need | Use This Technique | Complexity |
|-----------|-------------------|------------|
| Don't know how to start | Reverse Prompting | Low |
| Have prompt, need better | Recursive Optimization | Medium |
| Need deep reasoning | Deliberate Over-Instruction | Low |
| Need accuracy checks | Chain of Verification | Medium |
| Need stress-testing | Adversarial Prompting | Medium |
| Need structured thinking | Root Chain of Thought | Medium |
| Need specific format | Structured Output Forcing | Medium |
| Need consistency | Reference Class Priming | Medium |
| Learn edge cases | Failure-Mode Priming | High |
| Need multiple views | Multi-Persona Debate | High |
| Need uncertainty + confidence | Confidence Persona Simulation | Medium |
| Prevent hallucination | Contextual Grounding | Low |
| Set behavior rules | Constraint & Value Bounding | Low |

## Quick Patterns

### Basic Chain of Thought
```
[QUESTION]
Let's think step-by-step.
```

### Reverse Prompting
```
You're an expert prompt designer.
Design the optimal prompt for [TASK].
Execute it on [INPUT].
```

### Recursive Optimization
```
My current prompt: [PROMPT]
Goal: [OBJECTIVE]
Create 3 versions, each improving [ASPECT].
```

### Chain of Verification
```
[TASK]
After completion:
1. Identify 3 ways this might be incomplete
2. Cite evidence that confirms/refutes each
3. Revise based on verification
```

### Adversarial Prompting
```
[TASK]
Now attack your output.
Find 5 vulnerabilities with:
- Attack vector
- Likelihood
- Impact
- Mitigation
```

### Deliberate Over-Instruction
```
[TASK]
CRITICAL: Do not summarize. Include:
- Implementation details
- Edge cases
- Failure modes
- Quantitative analysis
```

### Root Chain of Thought
```
Analyze [PROBLEM] by completing:
1. Root cause: ___
2. Contributing factors: ___
3. Evidence: ___
4. Alternatives considered: ___
5. Impact assessment: ___
6. Solution: ___
```

### Few-Shot Learning
```
[TASK]
Example 1: Input → Output
Example 2: Input → Output
Now for: [NEW INPUT]
```

### Failure-Mode Priming
```
Learn from failures:
Example 1 (Failure): [INPUT]
Why it fails: [REASON]
Key learning: [PRINCIPLE]
Now apply to: [NEW CASE]
```

### Reference Class Priming
```
Example of quality expected:
[HIGH-QUALITY EXAMPLE]
Match this quality for: [NEW TASK]
```

### Multi-Persona Debate
```
Persona 1 (priority X): Argues [POSITION A]
Persona 2 (priority Y): Argues [POSITION B]
Each critiques the other.
Referee: Synthesize recommendation.
```

### Confidence Persona Simulation
```
Pass 1 (uncertain analyst): [OVEREXPLAIN]
Pass 2 (confident expert): [CONCISE]
Synthesis: Where is uncertainty warranted?
```

### Multi-Path Exploration
```
For [PROBLEM], identify 3 solutions.
For each:
- Approach
- Pros
- Cons
Recommend best with justification.
```

### Contextual Grounding (RAG)
```
Use ONLY these documents:
[DOCUMENTS]
- Cite sources
- If not in docs, say so clearly
Question: [QUESTION]
```

### Structured Output Forcing
```
Provide answer as valid JSON:
{
  "field": "type",
  "nested": { }
}
No text before or after JSON.
```

### Constraint & Value Bounding
```
[TASK]
CRITICAL CONSTRAINTS:
- MUST NOT [ACTION]
- MUST avoid [BEHAVIOR]
- MUST ground in [SOURCE]
```

### Self-Critique Phase
```
[TASK]
Before final answer:
1. List 3 strongest parts
2. List 3 weakest parts
3. Revise to fix weaknesses
```

## Common Combinations

| Use Case | Technique Stack |
|----------|----------------|
| High-accuracy analysis | Grounding + Root CoT + Verification + Self-Critique |
| Tool-using agent | System Prompt + Multi-Path + Tool Integration + Structured Output |
| Creative ideation | Reverse Prompting + Confidence Simulation + Debate + Priming |
| Document QA | Contextual Grounding + Verification + Structured Output |
| Decision-making | Multi-Persona Debate + Adversarial + Self-Critique |
| Technical debugging | Root CoT + Failure-Mode Priming + Verification |
| Security review | Adversarial + Chain of Verification + Deliberate Over-Instruction |

## Critical Don'ts

❌ "Be thorough yet concise" (contradictory)
❌ "Consider if..." (too weak, use "MUST")
❌ "Analyze thoroughly" (vague, specify criteria)
❌ Combining 5+ techniques at once
❌ Using generic examples in Few-Shot
❌ Skipping verification on critical tasks
❌ Forgetting to test on real inputs

## Critical Do's

✅ Make instructions mandatory ("MUST", "You MUST")
✅ Specify exact criteria (numbers, lengths, formats)
✅ Provide concrete examples
✅ Test on actual inputs before production
✅ Start simple, add complexity only when needed
✅ Check for instruction contradictions
✅ Document successful patterns for reuse

## Emergency Fixes

**Output too shallow?**
→ Add Deliberate Over-Instruction + Reference Class Priming

**Factual errors?**
→ Add Chain of Verification + Contextual Grounding

**Missing edge cases?**
→ Add Failure-Mode Priming + Adversarial Prompting

**Inconsistent quality?**
→ Add Reference Class Priming + Structured Output

**Need multiple perspectives?**
→ Add Multi-Persona Debate + Confidence Simulation

**Generic output?**
→ Add specific constraints + examples + format requirements

## File References

- Full examples: `references/examples.md`
- Problem solving: `references/troubleshooting.md`
- Workflow blueprints: `references/workflows.md`
- Detailed usage: `references/USAGE_GUIDE.md`
- Beginner intro: `references/BRIEFING.md`

## Version Notes

- Start with Basic Chain of Thought for any complex task
- Use Reverse Prompting when you don't know how to structure prompt
- Add verification for accuracy-critical tasks
- Combine 2-3 techniques max until comfortable
- Always test before production use
