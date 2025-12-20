# Briefing: Introduction to Systematic Prompt Engineering

This document introduces the core concepts of systematic prompt engineering for those new to the field.

## What is Prompt Engineering?

Prompt engineering is the practice of designing instructions (prompts) that guide AI language models to produce desired outputs. While anyone can ask questions, systematic prompt engineering applies structured techniques to reliably achieve high-quality, accurate, and useful results.

## Why Systematic Approaches Matter

### The Problem with Ad-Hoc Prompting

Most people interact with AI using natural, conversational questions:
- "Summarize this document"
- "What do you think about X?"
- "Help me with this code"

This works for simple tasks, but fails for:
- **Complex analysis** requiring deep reasoning
- **Accuracy-critical work** where errors have consequences
- **Production systems** requiring consistent behavior
- **Specialized domains** with specific requirements

### The Value of Structure

Systematic prompt engineering provides:
1. **Reliability:** Consistent quality across multiple uses
2. **Accuracy:** Built-in verification and error checking
3. **Depth:** Forces comprehensive rather than superficial analysis
4. **Transparency:** Makes AI reasoning visible and auditable
5. **Efficiency:** Reusable patterns save time

## Core Concepts

### 1. Prompt Structure

**Basic prompt:**
```
Analyze this contract for risks.
```

**Structured prompt:**
```
Analyze this contract for risks by completing these steps:
1. Identify liability clauses: ___
2. Assess termination conditions: ___
3. Evaluate payment terms: ___

After analysis, verify by:
- Checking if all sections were reviewed
- Citing specific contract language
- Revising findings if needed
```

The structured version:
- Defines explicit steps
- Creates scaffolding for thinking
- Includes verification
- Produces more thorough, reliable results

### 2. Explicit vs. Implicit Instructions

**Implicit (weak):**
```
Consider whether your analysis might be incomplete.
```

**Explicit (strong):**
```
You MUST identify three specific ways your analysis is incomplete.
If you cannot find three, you're not trying hard enough.
```

Language models respond better to clear, mandatory instructions than suggestions.

### 3. Verification and Self-Correction

AI models can make mistakes. Building verification into prompts catches errors:

**Without verification:**
```
Analyze the quarterly report.
```

**With verification:**
```
Analyze the quarterly report.

After your analysis:
1. Identify three assumptions you made
2. Cross-reference your findings with the provided data
3. Revise if discrepancies exist
```

This turns single-pass generation into a multi-step process with built-in quality control.

### 4. Examples Teach Behavior

Models learn patterns from examples. Two types matter:

**Input-Output Examples (Few-Shot):**
```
Task: Classify sentiment

Example 1: "This is amazing!" → Positive
Example 2: "Disappointed with quality" → Negative
Example 3: "It works" → Neutral

Now classify: "Exceeded expectations"
```

**Quality Examples (Reference Class Priming):**
```
Here's the level of detail I expect:
[DETAILED EXAMPLE OUTPUT]

Match this quality when analyzing:
[NEW INPUT]
```

### 5. Perspective Engineering

Single perspectives miss important considerations. Systematic prompts can simulate multiple viewpoints:

```
Three experts debate this decision:
- CFO (priority: cost control)
- CTO (priority: technical excellence)
- CPO (priority: customer value)

Each argues their position and critiques others.
```

This surfaces trade-offs and considerations a single analysis might miss.

## The Progression of Skill

### Beginner Level
- Ask clear questions
- Use "Let's think step-by-step" for complex tasks
- Provide relevant context
- Specify desired output format

### Intermediate Level
- Structure prompts with explicit steps
- Add verification loops
- Use examples to guide behavior
- Specify constraints and requirements clearly

### Advanced Level
- Design custom workflows combining multiple techniques
- Anticipate failure modes
- Build self-correcting systems
- Create reusable prompt patterns for production

## Common Beginner Mistakes

### Mistake 1: Vague Instructions
```
❌ "Analyze this thoroughly"
✅ "Provide 3 paragraphs analyzing: cost, risk, timeline"
```

### Mistake 2: Contradictory Requirements
```
❌ "Be thorough yet concise"
✅ "Provide comprehensive analysis. Minimum 500 words."
```

### Mistake 3: Assuming the Model Knows Your Context
```
❌ "Check if this is compliant"
✅ "Check if this contract complies with GDPR Article 6(1)(a) requirements for consent"
```

### Mistake 4: Optional Language for Mandatory Requirements
```
❌ "Consider checking for edge cases"
✅ "You MUST identify 5 specific edge cases"
```

### Mistake 5: No Verification on Critical Tasks
```
❌ [Just asking for analysis]
✅ [Analysis + verification step + revision based on verification]
```

## Key Principles for Beginners

### 1. Start Simple
Begin with basic structured prompts before advanced techniques:
```
Step 1: [Clear instruction]
Step 2: [Clear instruction]
Step 3: [Clear instruction]
```

### 2. Be Explicit
Replace vague with specific:
- "Analyze" → "Calculate, compare, and explain"
- "Thoroughly" → "Minimum 3 paragraphs per point"
- "Important findings" → "Top 5 findings ranked by financial impact"

### 3. Test Before Trusting
Always test prompts on real examples before production use. What works in theory may fail in practice.

### 4. Iterate Based on Results
First attempt rarely perfect. Improve based on actual outputs:
- Too shallow? Add depth requirements
- Errors? Add verification
- Inconsistent? Add examples
- Missing cases? Add failure mode examples

### 5. Document Success
When a prompt works well, save it as a template for similar tasks.

## Understanding the Techniques

This skill contains 21+ techniques. As a beginner, focus on these five first:

### 1. Basic Chain of Thought
**What:** Ask model to think step-by-step
**When:** Any complex question or calculation
**Pattern:** "[Question] Let's think step-by-step."

### 2. Structured Scaffolding (Root Chain of Thought)
**What:** Provide blank steps to fill in
**When:** Multi-step problems requiring systematic approach
**Pattern:** "Complete these steps: 1.___ 2.___ 3.___"

### 3. Verification Loop
**What:** Force model to check its work
**When:** Accuracy-critical tasks
**Pattern:** "After analysis: 1) Find issues 2) Check evidence 3) Revise"

### 4. Examples (Few-Shot)
**What:** Show 2-3 examples before new task
**When:** Specific format or style needed
**Pattern:** "Example 1: Input→Output [repeat] Now: [new input]"

### 5. Clear Constraints
**What:** Explicit rules model must follow
**When:** Safety, format, or content requirements
**Pattern:** "MUST NOT [x], MUST [y], MUST ground in [z]"

Master these five before moving to advanced techniques.

## Practical Starting Points

### For Document Analysis
```
Analyze [DOCUMENT] by answering:
1. Main points: ___
2. Key risks: ___
3. Recommendations: ___

Verify by checking if you cited specific sections.
```

### For Decision Support
```
Evaluate [DECISION] by comparing:

Option A:
- Pros: ___
- Cons: ___
- Cost: ___

Option B:
- Pros: ___
- Cons: ___
- Cost: ___

Recommendation with justification: ___
```

### For Code Review
```
Review this code for:
1. Security vulnerabilities: ___
2. Performance issues: ___
3. Best practice violations: ___

For each issue:
- Severity: High/Medium/Low
- Specific line numbers
- Suggested fix
```

### For Research Questions
```
Research [QUESTION]:

1. What do we know? ___
2. What's uncertain? ___
3. What evidence exists? ___
4. What are alternative views? ___
5. What's the most likely answer given evidence? ___
```

## Common Questions

### "When should I use advanced techniques?"

Start simple. Use advanced techniques when:
- Basic prompts fail to produce desired quality
- Task is accuracy-critical (finance, legal, medical)
- Building production systems requiring consistency
- Need to handle edge cases reliably
- Require transparent reasoning for auditing

### "How do I know if my prompt is good?"

Test it on 3-5 real examples. Good prompts produce:
- Consistent quality across examples
- Appropriate depth for task complexity
- Accurate, verifiable information
- Complete coverage of requirements
- Usable format

### "Can I combine techniques?"

Yes, but start with one or two. Common beginner combinations:
- Structured steps + verification
- Examples + clear constraints
- Chain of thought + specific output format

Avoid combining 5+ techniques until comfortable with each individually.

### "What if results are still poor?"

Check:
1. Are instructions explicit and mandatory?
2. Did you provide examples?
3. Did you test on real inputs?
4. Are there contradictions in your prompt?
5. Did you specify exact criteria?

See references/troubleshooting.md for specific issues.

## Next Steps

After understanding these basics:

1. **Practice:** Try techniques on your actual work
2. **Study examples:** Read references/examples.md
3. **Use quick reference:** Keep references/QUICK_REFERENCE.md handy
4. **Learn workflows:** Study references/workflows.md
5. **Iterate:** Improve prompts based on results

## Key Takeaways

✓ Systematic prompt engineering produces reliable, high-quality results
✓ Structure and explicitness matter more than cleverness
✓ Verification catches errors that single-pass generation misses
✓ Examples teach models desired behavior effectively
✓ Start simple, add complexity only when needed
✓ Test on real inputs before trusting results
✓ Document successful patterns for reuse

## Resources Within This Skill

- **QUICK_REFERENCE.md:** Fast lookup for all techniques
- **USAGE_GUIDE.md:** Detailed usage instructions and patterns
- **examples.md:** Complete examples for every technique
- **troubleshooting.md:** Solutions to common problems
- **workflows.md:** Advanced workflow blueprints
- **SKILL.md:** Complete technique catalog

Start with this briefing, then use QUICK_REFERENCE.md as your daily guide.
