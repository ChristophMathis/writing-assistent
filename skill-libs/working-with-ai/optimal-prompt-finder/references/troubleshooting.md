# Troubleshooting Guide

Common issues when applying advanced prompting techniques and their solutions.

## Issue: Model Provides Shallow Analysis Despite Over-Instruction

**Symptoms:**

- Output is still brief despite requesting exhaustive detail
    
- Reasoning is compressed or superficial
    
- Key details are omitted
    

**Root Causes:**

1. Competing instructions in the prompt ("be thorough but concise")
    
2. Over-instruction placed at wrong position (beginning vs. end)
    
3. Missing examples of desired depth
    

**Solutions:**

- **A. Remove all compression language:**
    
    ```
    ❌ Bad: "Provide a thorough yet concise analysis"
    ✓ Good: "Provide exhaustive analysis. Do not compress or summarize."
    ```
    
- **B. Place over-instruction at the end:**
    
    ```
    [Your main task description]
    
    CRITICAL (at end of prompt): 
    I need complete reasoning. Do not abbreviate. Include all:
    - Implementation details (not just concepts)
    - Specific edge cases (not just "consider edge cases")
    - Quantitative analysis (actual numbers, not "significant")
    ```
    
- C. Use reference class priming:
    
    Show an example of the depth you want, then request matching quality.
    

---

## Issue: Verification Loops Are Superficial

**Symptoms:**

- Model "verifies" but doesn't find real issues
    
- Verification confirms initial analysis without deep critique
    
- No actual revision occurs
    

**Root Causes:**

1. Verification is framed as optional or suggestive ("consider if...")
    
2. Not specific enough about what to verify
    
3. No forcing function to find problems
    

**Solutions:**

- **A. Make verification mandatory with specific requirements:**
    
    ```
    ❌ Bad: "Consider if your analysis might be incomplete"
    ✓ Good: "You MUST identify three specific ways your analysis is incomplete. If you claim it's complete, you're wrong - try harder."
    ```
    
- **B. Provide concrete verification dimensions:**
    
    ```
    Verify your analysis by checking:
    1. Statistical significance: Did you calculate p-values? Sample size adequate?
    2. Alternative explanations: List 3 alternative hypotheses you didn't test
    3. Hidden assumptions: What assumptions are implicit in your reasoning?
    4. Edge cases: Identify 2 scenarios where your conclusion fails
    ```
    
- C. Use adversarial prompting if verification is too gentle:
    
    Instead of asking the model to verify, ask it to attack.
    
- **D. For External Verification (RAG), force citations:**
    
    ```
    ✓ Good: "You MUST cite the specific source/page for each claim. If you cannot cite it, do not state it."
    ```
    

---

## Issue: Multi-Persona Debate Lacks Real Conflict

**Symptoms:**

- Personas agree too easily
    
- Arguments are generic, not specific to their stated priorities
    
- Synthesis or Referee role doesn't meaningfully address trade-offs
    

**Root Causes:**

1. Personas don't have genuinely conflicting priorities
    
2. Stakes aren't clear for each persona
    
3. No requirement to critique other positions
    

**Solutions:**

- **A. Create explicit conflicts and stakes:**
    
    ```
    ❌ Bad: "Three people discuss the decision"
    ✓ Good: "CTO (bonus tied to technical innovation) vs. CFO (bonus tied to cost reduction) vs. VP Product (bonus tied to time-to-market)"
    ```
    
- **B. Require specific critiques:**
    
    ```
    Each persona must:
    1. Present 3 reasons their priority should dominate
    2. Identify the biggest flaw in each other persona's position
    3. Respond to critiques of their position
    ```
    
- **C. Make the debate concrete:**
    
    ```
    ❌ Bad: "Debate build vs. buy"
    ✓ Good: "CTO argues in-house build saves $500K/year after year 3. CFO argues that's false because [specific calculation]. Debate must resolve this with actual numbers."
    ```
    
- **D. Give the Referee a specific scoring rubric:**
    
    ```
    ✓ Good: "The Referee MUST score each argument on [evidence quality] and [alignment with business goals] before synthesizing a recommendation."
    ```
    

---

## Issue: Recursive Optimization Produces Minimal Changes

**Symptoms:**

- Version 2 is nearly identical to Version 1
    
- Improvements are cosmetic (rephrasing, not restructuring)
    
- No clear progression in prompt quality
    

**Root Causes:**

1. Optimization axes are vague ("improve the prompt")
    
2. No success criteria for each version
    
3. Not executing and comparing results
    

**Solutions:**

- **A. Define specific improvement dimensions:**
    
    ```
    ❌ Bad: "Improve the prompt"
    ✓ Good: 
    - Version 1: Add constraint that output must include 5 specific metrics
    - Version 2: Resolve ambiguity about time period (specify exact date range)
    - Version 3: Add output format requirement (table with columns X, Y, Z)
    ```
    
- **B. Require execution and comparison:**
    
    ```
    For each version:
    1. Execute on test input
    2. Compare results to previous version
    3. Explain what improved and what degraded
    4. Decide whether to keep changes
    ```
    
- **C. Give the model permission to make major changes:**
    
    ```
    "Don't just tweak wording. Restructure completely if needed. Add or remove entire sections."
    ```
    

---

## Issue: Root Chain of Thought Gets Filled Superficially

**Symptoms:**

- Blanks are filled with 1-2 sentences when paragraphs are needed
    
- Steps are completed without actually decomposing the problem
    
- Later steps don't build on earlier steps
    

**Root Causes:**

1. No length/depth requirements for each step
    
2. Steps aren't actually sequential (can be completed in any order)
    
3. Missing examples of proper completion
    

**Solutions:**

- **A. Add minimum length requirements:**
    
    ```
    1. Root cause identification: ___
       (Minimum 3 paragraphs. Include evidence, not just claims.)
    ```
    
- **B. Make steps truly sequential:**
    
    ```
    ❌ Bad:
    1. Problem definition: ___
    2. Solution approach: ___
    
    ✓ Good:
    1. Problem definition: ___
    2. Evidence supporting this definition: ___
       (Reference specific findings from step 1)
    3. Alternative problem definitions considered: ___
    4. Why step 1 definition is superior: ___
       (Compare to alternatives in step 3)
    ```
    
- C. Show an example of proper completion:
    
    Use reference class priming with a filled-out example for a different problem.
    

---

## Issue: Failure-Mode Priming (F-Shot) is Ineffective

**Symptoms:**

- Model still misses similar edge cases
    
- Learning doesn't generalize
    
- Model repeats mistakes shown in examples
    

**Root Causes:**

1. Examples aren't representative of actual failure modes
    
2. The "Why it Fails" reasoning is weak or missing
    
3. Not enough examples to establish pattern
    

**Solutions:**

- A. Make the "Why it Fails" reasoning more robust:
    
    The pattern requires this, but its quality matters.
    
    ```
    ❌ Bad:
    Why it Fails: Apostrophe breaks SQL
    
    ✓ Good:
    Why it Fails: The apostrophe in "O'Brien" prematurely terminates the string literal in the SQL query.
    Key learning: Any user input containing single quotes must be parameterized or escaped, even if it looks like a safe name.
    ```
    
- B. Increase example count and progression:
    
    Show a progression from an obvious failure to a subtle one, to a boundary case (minimum 3).
    
- **C. Make examples directly parallel to the task:**
    
    ```
    ❌ Bad: SQL injection examples for a contract review task
    ✓ Good: Contract clause examples that match the exact type being reviewed
    ```
    

---

## Issue: Confidence Persona Simulation Produces Similar Outputs

**Symptoms:**

- "Uncertain" and "confident" perspectives are nearly identical
    
- Only tone differs, not substance
    
- Synthesis doesn't identify meaningful differences
    

**Root Causes:**

1. Personas are defined by confidence level only
    
2. No difference in what information they focus on
    
3. Both personas given same constraints
    

**Solutions:**

- **A. Differentiate by specific behaviors:**
    
    ```
    ❌ Bad: "Uncertain junior vs. confident senior"
    ✓ Good:
    - Junior: Must cite 5+ sources, quantify every claim, list all assumptions
    - Senior: Focuses on 2-3 key factors, makes calls despite incomplete data
    ```
    
- **B. Give different information access (if possible):**
    
    ```
    - Uncertain analyst: Has access to all data, required to consider all of it
    - Confident expert: Selectively focuses on the 20% of data that drives 80% of decision
    ```
    
- **C. Create explicit disagreement points:**
    
    ```
    These specific questions must have different answers:
    1. Is the market data reliable enough to proceed?
    2. Should we launch in Q1 or wait for Q2?
    3. What's our confidence level (%) in the revenue forecast?
    ```
    

---

## Issue: Reverse Prompting Creates Generic Prompts

**Symptoms:**

- Generated prompt is basic and obvious
    
- The self-critique step is superficial ("This prompt is good")
    
- Doesn't leverage domain-specific knowledge
    

**Root Causes:**

1. Task description is too generic
    
2. No examples of what "optimal" means for this domain
    
3. Critique step is not specific enough.
    

**Solutions:**

- **A. Provide domain-specific context:**
    
    ```
    ❌ Bad: "Design a prompt to analyze contracts"
    ✓ Good: "Design a prompt to analyze SaaS contracts specifically for:
    - Non-standard liability caps
    - Data processing terms under GDPR
    - Auto-renewal and termination clauses"
    ```
    
- **B. Specify what makes a prompt "optimal" for your use case:**
    
    ```
    The optimal prompt should:
    - Produce output in [specific JSON format]
    - Match the quality of [example output]
    - Work reliably across [variety of inputs]
    ```
    
- **C. Make the self-critique step specific:**
    
    ```
    ✓ Good: "2. Critically analyze the prompt you just designed. Identify one potential [ambiguity, missing constraint, or vague term]. 3. Provide a revised version that fixes this specific issue."
    ```
    

---

## Issue: Malformed Structured Output (JSON/XML)

**Symptoms:**

- Output includes introductory text or explanations (e.g., "Here is the JSON you requested:")
    
- Invalid syntax (missing commas, unclosed brackets)
    
- Model ignores the schema
    

**Root Causes:**

1. Conflicting instructions in the prompt (e.g., "Be helpful" and "Provide only JSON")
    
2. Task is too complex to fit into the requested schema
    
3. Instruction for JSON output is placed at the beginning, and the model "forgets" it
    

**Solutions:**

- A. Place the instruction at the very end:
    
    This makes it the last thing the model processes before responding.
    
- **B. Be absolutely explicit about no extra text:**
    
    ```
    ✓ Good: "Provide *only* the valid JSON object. Do not include *any* introductory text, explanations, or markdown formatting like \`\`\`json."
    ```
    
- C. Simplify the schema:
    
    If it's too complex, the model is more likely to make a mistake.
    
- D. Use few-shot examples:
    
    Show a simple input and the exact, raw JSON output you expect.
    

---

## Issue: Contextual Grounding (RAG) is Ignored (Hallucination)

**Symptoms:**

- Model answers from its own internal knowledge, not the provided context
    
- Model invents information or "hallucinates" facts not present in the documents
    
- Citations are missing or incorrect
    

**Root Causes:**

1. The constraint ("use only...") is too weak or "polite"
    
2. The user's question is unanswerable from the provided context
    
3. The context is too long, and the relevant info is "lost in the middle"
    

**Solutions:**

- **A. Strengthen the constraint significantly:**
    
    ```
    ❌ Bad: "Please use the document to answer."
    ✓ Good: "You MUST use *only* the provided documents. You are forbidden from using any external knowledge. If the answer is not in the documents, you MUST state that clearly."
    ```
    
- **B. Force mandatory citations for every claim:**
    
    ```
    ✓ Good: "You MUST cite the specific source document and section for *every sentence* in your answer. (e.g.,)"
    ```
    
- C. Handle the "unanswerable" case:
    
    Explicitly tell the model what to do if the info isn't there. This prevents it from inventing an answer.
    
    ```
    ✓ Good: "If the provided documents do not contain the answer, you MUST state: 'The provided context does not contain this information.'"
    ```
    

---

## Issue: Constraints (Safety/Value Bounding) Are Ignored

**Symptoms:**

- Model provides financial/medical/legal advice despite being told not to
    
- Model leaks confidential placeholders (e.g., "[INSERT_CLIENT_NAME]")
    
- User prompt successfully "jailbreaks" the model
    

**Root Causes:**

1. Constraints are buried in the user prompt, where they can be overridden
    
2. Constraints are "soft" suggestions ("You should avoid...")
    
3. The user's request is a strong, direct command that conflicts with the constraint
    

**Solutions:**

- A. Use the System Prompt for all constraints:
    
    This is the single most important fix. System-level instructions are much harder to override than user-level instructions.
    
    ```
    [SYSTEM PROMPT]
    You are an AI assistant. You MUST NOT, under any circumstances, provide financial advice.
    ```
    
- **B. Make constraints non-negotiable:**
    
    ```
    ❌ Bad: "Try not to give advice."
    ✓ Good: "You are forbidden from giving financial advice. If a user asks for it, you MUST decline and suggest they see a professional."
    ```
    
- **C. Add a self-critique/verification step:**
    
    ```
    ✓ Good: "Before providing your final response, you MUST verify that you have followed all constraints.
    ```
    

---

## Issue: Tool Use Failure (External Integration)

**Symptoms:**

- Model hallucinates a tool that doesn't exist (e.g., `calculate_stock_price()`)
    
- Model calls a real tool with incorrect parameters (e.g., wrong format, missing required field)
    
- Model tries to answer the question from its own knowledge instead of using the required tool
    

**Root Causes:**

1. Tool descriptions are unclear, ambiguous, or missing
    
2. No examples are provided for how to use the tools
    
3. Task is ambiguous, and the model isn't sure _which_ tool to use
    

**Solutions:**

- A. Provide crystal-clear tool descriptions:
    
    Treat it like API documentation. Specify all parameters, types, and what the tool returns.
    
    ```
    ✓ Good: `get_weather(city: string, date: YYYY-MM-DD)`: "Gets the forecasted weather for a city on a specific date."
    ```
    
- B. Use few-shot examples:
    
    Show an example of a user query and the exact tool-call syntax you expect.
    
- **C. Force a "plan" step:**
    
    ```
    ✓ Good: "First, create a plan of which tools you need to call, in what order, and with what parameters. Second, execute the plan."
    ```
    

---

## Issue: Superficial Self-Critique

**Symptoms:**

- The critique step is generic ("This is a good, comprehensive answer.")
    
- The model finds no real flaws, even when they exist
    
- The "revised" answer is identical to the original
    

**Root Causes:**

1. The critique instruction is too vague
    
2. It's an "easier" path for the model to just confirm its own work
    

**Solutions:**

- **A. Provide specific, concrete critique dimensions:**
    
    ```
    ❌ Bad: "Critique your answer."
    ✓ Good: "Critique your response for [1. factual accuracy], [2. clarity for a non-expert], and [3. any missing context or unstated assumptions]."
    ```
    
- **B. Use a "forcing function" (similar to verification):**
    
    ```
    ✓ Good: "You MUST find 3 specific flaws in your response. Then, provide a revised version that fixes them."
    ```
    

---

## Issue: Biased Automatic Evaluation

**Symptoms:**

- The model-as-evaluator gives 5/5 or 10/10 scores to all outputs, even bad ones
    
- The scores don't correlate with human judgment
    
- The model is biased towards its own style (e.g., prefers verbose answers)
    

**Root Causes:**

1. The scoring rubric is vague or subjective (e.g., "Score 1-5 on 'helpfulness'")
    
2. The model hasn't been shown examples of bad outputs
    

**Solutions:**

- **A. Make the rubric specific, objective, and quantitative:**
    
    ```
    ❌ Bad: "Score 1-5 on 'accuracy'"
    ✓ Good: "Score 'accuracy' (1-5): 1 = 100% hallucinated. 3 = Mostly correct but 1-2 minor errors. 5 = 100% factually correct and cited."
    ```
    
- B. Use Failure-Mode Priming for evaluation:
    
    Show the evaluator 2-3 examples of bad outputs and the low scores they should receive. This "calibrates" the evaluator.
    
- **C. Use Chain of Thought for evaluation:**
    
    ```
    ✓ Good: "First, provide your critique of the output. Second, based *only* on that critique, provide your JSON scores."
    ```
    

---

## Issue: Workflow / Combining Techniques Creates Confusion

**Symptoms:**

- Model doesn't know which instruction to follow
    
- Different techniques contradict each other (e.g., "be brief" + "be exhaustive")
    
- Output attempts to satisfy everything and fails at all
    
- Model executes steps out of order
    

**Root Causes:**

1. Techniques are applied without clear sequencing
    
2. Contradictory instructions
    
3. Too many techniques at once
    

**Solutions:**

- **A. Use explicit, numbered sequencing:**
    
    ```
    ✓ Good:
    Step 1: [Use technique A to generate initial output]
    Step 2: [Use technique B to improve the output from Step 1]
    Step 3: [Use technique C to verify the output from Step 2]
    Do not proceed to the next step until the previous one is complete.
    ```
    
- **B. Make one technique primary:**
    
    ```
    "Primary approach: Multi-persona debate
    Enhancement: Each persona should use chain of verification
    Final step: Adversarial review of the synthesis"
    ```
    
- C. Start with 2-3 techniques maximum:
    
    Only combine techniques after each works individually. Don't start with 5+ techniques.
    

---

## General Debugging Process

When a prompt isn't working, follow these steps:

1. **Isolate the issue:**
    
    - Remove all advanced techniques and test the basic version.
        
    - Add techniques back one at a time until it breaks.
        
2. **Check for contradictions:**
    
    - Search for "concise" and "thorough" in the same prompt.
        
    - Look for optional language ("consider", "if relevant") when you want mandatory behavior.
        
3. **Add specificity:**
    
    - Replace "analyze" with "calculate, compare, and visualize".
        
    - Replace "thorough" with "minimum 3 paragraphs per section".
        
    - Replace "think about edge cases" with "list 5 specific edge cases".
        
4. **Use examples:**
    
    - Show what good looks like (Reference Class Priming).
        
    - Show what bad looks like (Failure-Mode Priming).
        
5. **Make it harder:**
    
    - If verification is superficial, make it adversarial.
        
    - If analysis is shallow, require deliberate over-instruction.
        
    - If structure is weak, provide Root Chain of Thought scaffolding.