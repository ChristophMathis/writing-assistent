# Usage Guide

This guide explains how to effectively use the Optimal Prompt Finder skill for different scenarios.

## Getting Started

### Step 1: Identify Your Need

Before selecting a technique, clarify what you need:

**Quality Issues?**
- Shallow analysis → Deliberate Over-Instruction
- Factual errors → Chain of Verification
- Missing edge cases → Failure-Mode Priming

**Structural Issues?**
- Unclear how to approach → Reverse Prompting
- Need systematic breakdown → Root Chain of Thought
- Want multiple perspectives → Multi-Persona Debate

**Optimization Needs?**
- Have working prompt → Recursive Optimization
- Inconsistent quality → Reference Class Priming
- Need stress-testing → Adversarial Prompting

### Step 2: Start Simple

Always begin with the simplest applicable technique:

1. **First try:** Basic Chain of Thought ("Let's think step-by-step")
2. **If insufficient:** Add one structured technique
3. **If still insufficient:** Combine 2-3 techniques
4. **For production:** Build a complete workflow

**Example progression:**
```
Try 1: "Analyze this contract for risks."
Try 2: "Analyze this contract for risks. Let's think step-by-step."
Try 3: "Analyze this contract for risks using Root Chain of Thought..."
Try 4: Full workflow with verification and adversarial testing
```

### Step 3: Iterate Based on Results

After testing, evaluate and adjust:

**If output is too shallow:**
- Add Deliberate Over-Instruction
- Use Reference Class Priming with a detailed example

**If output contains errors:**
- Add Chain of Verification
- Switch to Adversarial Prompting for critical tasks

**If structure is weak:**
- Replace open instructions with Root Chain of Thought scaffolding
- Add specific output format requirements

## Common Usage Patterns

### Pattern 1: Document Analysis

**Scenario:** Analyze a legal contract, financial report, or technical document.

**Recommended approach:**
1. Start with Contextual Grounding (provide document)
2. Add Root Chain of Thought for structure
3. Include Chain of Verification for accuracy
4. For critical analysis, add Adversarial Prompting

**Example:**
```
Use only the provided contract to answer.

Analyze risks by completing these steps:
1. Liability clauses: ___
2. Termination conditions: ___
3. Payment terms: ___
4. Non-standard provisions: ___

After analysis, perform verification:
1. Identify three ways your analysis might be incomplete
2. Cross-reference with contract sections
3. Revise findings
```

### Pattern 2: Creating New Prompts

**Scenario:** Need to design a prompt but unsure of the optimal structure.

**Recommended approach:**
1. Use Reverse Prompting first
2. If result is generic, add domain-specific requirements
3. Use Recursive Optimization to refine
4. Test with example inputs

**Example:**
```
You're an expert prompt designer.
1. Design the optimal prompt for [SPECIFIC TASK WITH DETAILS]
   Consider:
   - [SPECIFIC REQUIREMENT 1]
   - [SPECIFIC REQUIREMENT 2]
2. Critique your prompt for weaknesses
3. Provide improved version
4. Execute on: [TEST INPUT]
```

### Pattern 3: Complex Decision-Making

**Scenario:** Strategic decision with multiple stakeholders and trade-offs.

**Recommended approach:**
1. Start with Multi-Persona Debate
2. Add Adversarial Prompting to find weaknesses
3. Include Self-Critique Phase
4. Optional: Use Confidence Persona Simulation for risk assessment

**Example:**
```
Three executives debate: [DECISION]

CTO (priority: technical excellence): Argues for [OPTION A]
CFO (priority: cost control): Argues for [OPTION B]
CPO (priority: customer value): Argues for [OPTION C]

Each must critique others' positions.

Referee: Synthesize recommendation addressing all concerns.

Then: Attack this recommendation. Find 3 weaknesses.
```

### Pattern 4: Technical Problem-Solving

**Scenario:** Debug a system, analyze code, or diagnose technical issues.

**Recommended approach:**
1. Use Root Chain of Thought for structured debugging
2. Add Failure-Mode Priming with examples
3. Include Chain of Verification
4. For security issues, add Adversarial Prompting

**Example:**
```
Diagnose this performance issue by completing:

1. Symptom characterization: ___
2. Timeline and changes: ___
3. Resource metrics: ___
4. Root cause hypothesis: ___
5. Verification steps: ___
6. Resolution approach: ___

Learn from these failure modes:
[SIMILAR PAST ISSUES]

Verify your diagnosis by checking assumptions.
```

### Pattern 5: Creative Work with Quality Standards

**Scenario:** Generate ideas, content, or designs that must meet specific quality bars.

**Recommended approach:**
1. Use Confidence Persona Simulation (wild + safe ideas)
2. Add Reference Class Priming with quality example
3. Include Multi-Persona Debate for critique
4. Use Self-Critique Phase for refinement

**Example:**
```
Generate product naming ideas from two perspectives:

Creative (wild): 5 unconventional names
Practical (safe): 5 market-tested names

Here's an example of quality naming: [EXAMPLE]
Match this quality in your suggestions.

Three marketing personas debate top 3 names.
Finally: Self-critique and provide refined recommendation.
```

## Troubleshooting Your Usage

### Problem: "I applied the technique but results are still poor"

**Checklist:**
- [ ] Did you make instructions mandatory? (Use "MUST" not "consider")
- [ ] Did you provide specific criteria? (Not "analyze thoroughly" but "provide 3 paragraphs per section")
- [ ] Did you include an example? (Reference Class Priming)
- [ ] Did you check for contradictions? (No "be thorough yet concise")
- [ ] Did you test on actual inputs? (Not just theory)

### Problem: "Output is too long/verbose"

**Solutions:**
- Remove Deliberate Over-Instruction
- Add length constraints ("Maximum 200 words")
- Use Structured Output Forcing with word limits
- Specify format ("3 bullet points, each 1-2 sentences")

### Problem: "Technique feels too complex"

**Solutions:**
- Start with Basic Chain of Thought only
- Add techniques incrementally
- Use examples from references/examples.md
- Focus on one technique until comfortable

### Problem: "Don't know which technique to use"

**Decision tree:**
1. Need a prompt? → Reverse Prompting
2. Have prompt, need improvement? → Recursive Optimization
3. Need accuracy? → Chain of Verification
4. Need depth? → Deliberate Over-Instruction + Root Chain of Thought
5. Need robustness? → Adversarial Prompting
6. Need perspectives? → Multi-Persona Debate
7. Need consistency? → Reference Class Priming

## Advanced Usage

### Combining with External Tools

When the model needs real-time data or calculations:

```
You can use these tools:
- [LIST TOOLS WITH DESCRIPTIONS]

Task: [USER REQUEST]

Use Multi-Path Exploration to decide which tools to call.
Then execute tool calls.
Format output as JSON using Structured Output Forcing.
```

### Building Production Workflows

For repeated tasks, create reusable workflow patterns:

1. **Define the workflow steps** (see references/workflows.md)
2. **Test on 5+ real examples**
3. **Document edge cases found**
4. **Add those edge cases as Failure-Mode Priming examples**
5. **Iterate based on production use**

### Creating Custom Techniques

You can adapt existing techniques:

**Example - Modified Chain of Verification:**
```
Standard: Identify 3 ways analysis might be incomplete
Custom for finance: 
- Check if all regulatory disclosures were considered
- Verify calculations against source data
- Confirm industry benchmarks are current
```

## Best Practices

### Do's
✅ Start simple, add complexity only when needed
✅ Test techniques on real examples before production
✅ Make instructions explicit and mandatory
✅ Provide specific criteria and examples
✅ Document what works for future reuse
✅ Combine techniques strategically, not randomly
✅ Check for contradictions in instructions

### Don'ts
❌ Don't use all techniques at once
❌ Don't use vague language ("consider", "might", "if relevant")
❌ Don't skip testing on actual inputs
❌ Don't combine contradictory instructions
❌ Don't assume one technique fits all scenarios
❌ Don't forget to iterate based on results

## Measuring Success

Track effectiveness by:

**Quality metrics:**
- Factual accuracy (errors found in verification)
- Completeness (edge cases covered)
- Depth (detail level vs. requirement)
- Consistency (output quality variance)

**Efficiency metrics:**
- First-pass success rate
- Iterations needed
- Time to acceptable output
- Reusability of prompt pattern

## Getting Help

If stuck:
1. Check references/troubleshooting.md for your specific issue
2. Review references/examples.md for similar use cases
3. Consult references/workflows.md for workflow patterns
4. Try simpler technique first
5. Test on smaller example to isolate problem

## Next Steps

After mastering basic usage:
1. Study references/workflows.md for advanced patterns
2. Create custom workflows for your common tasks
3. Build a library of reusable prompts
4. Experiment with technique combinations
5. Document your own best practices
