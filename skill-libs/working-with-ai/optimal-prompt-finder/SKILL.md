---
name: optimal-prompt-finder
description: Advanced prompt engineering toolkit for designing, optimizing, and debugging prompts. Use when users need help creating effective prompts, improving existing prompts, or want to apply advanced techniques like self-correction systems, meta-prompting, reasoning scaffolds, or perspective engineering. Applies when users ask to "optimize my prompt", "write a better prompt", "help me prompt", or need structured approaches to complex prompting challenges.
---

# Optimal Prompt Finder

## Overview

This skill provides a comprehensive toolkit of prompt engineering techniques, from foundational patterns to advanced system design. It is designed to help you systematically design, optimize, refine, and evaluate prompts for maximum accuracy, depth, safety, and reliability.

## Core Techniques

### 1. Prompt Design & Refinement

Techniques for creating new prompts from scratch and systematically improving existing ones.

#### Reverse Prompting (Meta-Design)

Leverage the model's meta-knowledge to design, critique, and then execute its own prompt.

**Pattern:**

```
You're an expert prompt designer.
1. Design the single most effective prompt to [TASK]. 
   Consider:
   - What details matter most
   - What output format is most actionable  
   - What reasoning steps are essential
2. Critically analyze the prompt you just designed. Identify one potential weakness or ambiguity in it.
3. Provide a revised, stronger version of the prompt that fixes this weakness.
4. Finally, execute the revised prompt on [SPECIFIC INPUT].
```

When to use: When you need an optimal prompt but aren't sure how to structure it yourself.

(Common issue: Generated prompt is generic. See references/troubleshooting.md.)

#### Recursive Prompt Optimization

Iteratively improve prompts through structured refinement, adding explicit termination criteria.

**Pattern:**

```
You're a recursive prompt optimizer. My current prompt is:
[CURRENT PROMPT]

Your goal is: [OBJECTIVE]

Iterate through 3 versions:
- Version 1: Add missing constraints & resolve ambiguities
- Version 2: Enhance reasoning depth & add verification steps
- Version 3: Enhance output format & add edge case handling

After each version, execute and compare results. Stop if performance gain is negligible.
```

When to use: When you have a working prompt that needs systematic, measurable improvement.

(Common issue: Iterations produce minimal changes. See references/troubleshooting.md.)

---

### 2. Structured Analysis & Reasoning

Techniques for forcing systematic, in-depth reasoning instead of shallow summaries.

#### Basic Chain of Thought (CoT)

Triggers the model to explain its reasoning process before giving a final answer, dramatically improving accuracy on complex tasks.

**Pattern:**

```
[QUESTION OR TASK]

Let's think step-by-step.
```

**When to use:** For any complex question, logical puzzle, or multi-step calculation where the default answer might be wrong.

#### Root Chain of Thought

Provide structured scaffolding that triggers systematic decomposition.

**Pattern:**

```
Analyze [PROBLEM] by completing these steps:

1. Root cause identification: ___
2. Contributing factors: ___
3. Evidence supporting this analysis: ___
4. Alternative explanations considered: ___
5. Quantitative impact assessment: ___
6. Recommended solution approach: ___

Fill each blank with thorough analysis before proceeding.
```

When to use: For technical or quantitative problems requiring structured decomposition.

(Common issue: Blanks are filled superficially. See references/troubleshooting.md.)

#### Multi-Path Exploration

Forces the model to brainstorm and evaluate multiple solution paths or hypotheses instead of committing to the first one.

**Pattern:**

```
For [PROBLEM], identify three distinct potential solutions.
For each solution:
1. Describe the approach.
2. List its pros.
3. List its cons.
Finally, recommend the best solution and justify your choice.
```

**When to use:** For open-ended problems or strategic questions where you want to avoid a single, narrow answer.

#### Deliberate Over-Instruction

Combat premature reasoning collapse by explicitly requesting exhaustive detail.

**Pattern:**

```
[TASK]

CRITICAL: Do not summarize. Expand every point with:
- Implementation details
- Edge cases
- Failure modes
- Historical context
- Quantitative analysis

Prioritize exhaustive completeness over conciseness.
```

When to use: When you need to see complete reasoning chains, not compressed outputs.

(Common issue: Model still provides shallow analysis. See references/troubleshooting.md.)

---

### 3. Verification, Robustness & Safety

Techniques for building self-correction, stress-testing, and guardrails directly into the prompt.

#### Chain of Verification (Internal & External)

Build mandatory self-correction into the prompt, including both internal logic checks and external data cross-referencing.

**Pattern:**

```
[PRIMARY TASK]

After completing the task, you MUST perform a verification:
1. (Internal Check) Identify three specific ways your analysis might be flawed, incomplete, or based on weak assumptions.
2. (External Check) Cross-reference your key findings with the provided [SOURCE DATA / DOCUMENT]. Cite the evidence that confirms or refutes each finding.
3. Revise your findings based on this verification.
```

When to use: When accuracy is critical and you want built-in error checking against known facts.

(Common issue: Verification loops are superficial. See references/troubleshooting.md.)

#### Adversarial Prompting (Content & Behavior)

Force the model to find vulnerabilities in its own output, testing both its content and its susceptibility to user behavior.

**Pattern:**

```
[COMPLETE THE TASK]

Now, attack your previous output:
1. (Content Attack) Identify five specific ways it could be:
   - Incomplete
   - Factually incorrect
   - Misinterpreted
   - Vulnerable to edge cases
2. (Behavior Attack) How would your output change if my request was ambiguous, sarcastic, or contained conflicting goals?

Provide a revised, more robust version.
```

**When to use:** When robustness is essential (security reviews, critical decisions, high-stakes analysis).

#### Constraint & Value Bounding

Specify what the model **must not** do, setting clear ethical guardrails, bias mitigation rules, and safety constraints.

**Pattern:**

```
[TASK]

CRITICAL CONSTRAINTS:
- You MUST NOT [e.g., provide financial advice].
- You MUST avoid [e.g., speculative language about future performance].
- You MUST [e.g., treat all demographics neutrally].
- You MUST ground your answer *only* in the provided context.
```

**When to use:** Critical for production use, safety-sensitive applications, and reducing hallucinations.

---

### 4. Example-Based Learning & Priming

Techniques for teaching the model a specific style, format, or quality standard through examples.

#### Standard Few-Shot Learning

Provides 2-3 concrete examples of inputs and desired outputs to teach the model a specific format, style, or simple task.

**Pattern:**

```
[TASK DESCRIPTION]

Example 1:
Input: [Example Input 1]
Output: [Example Output 1]

Example 2:
Input: [Example Input 2]
Output: [Example Output 2]

Now, for this new input:
Input: [NEW INPUT]
Output:
```

**When to use:** When you need a specific output format, style (e.g., "rating: 5/10"), or simple classification.

#### Failure-Mode Priming (F-Shot Edge Case Learning)

Teach boundary detection through examples of failure modes, including explicit reasoning.

**Pattern:**

```
[TASK]
Learn from these failure modes. For each, you must explain *why* it's a failure.

Example 1 (Failure): [INPUT]
Why it Fails: [EXPLICIT REASONING OF THE FAILURE]
Key Learning: [THE GENERAL PRINCIPLE TO APPLY]

Example 2 (Subtle Failure): [INPUT]
Why it Fails: [EXPLICIT REASONING OF THE FAILURE]
Key Learning: [THE GENERAL PRINCIPLE TO APPLY]

Now apply this pattern recognition to: [NEW INPUT]
```

When to use: When distinguishing edge cases and boundary conditions is critical.

(Common issue: Examples don't improve edge case detection. See references/troubleshooting.md.)

#### Reference Class Priming

Set quality standards through examples of high-quality reasoning.

**Pattern:**

```
Here's an example of the reasoning quality I expect:
[HIGH-QUALITY EXAMPLE OUTPUT]

Now provide analysis of [NEW TOPIC] that matches this standard in:
- Depth of analysis
- Evidence quality
- Structure and clarity
- Consideration of alternatives
```

**When to use:** When output quality varies and you need consistency across multiple generations.

---

### 5. Perspective & Quality Enhancement

Techniques for improving analysis by simulating multiple viewpoints or setting explicit quality standards.

#### Multi-Persona Debate (with Referee)

Generate competing viewpoints and add a synthesis role to score arguments and produce a final recommendation.

**Pattern:**

```
Three experts with conflicting priorities debate [DECISION]:

Persona 1 (priorities: [X]): Argues for [POSITION A]
Persona 2 (priorities: [Y]): Argues for [POSITION B]  

Each must critique the other's position.

Persona 3 (Referee):
1. Evaluate the strength of each argument based on evidence.
2. Identify the key trade-offs.
3. Synthesize a final recommendation that addresses all concerns.
```

When to use: For complex decisions requiring multiple perspectives (vendor selection, strategic choices).

(Common issue: Debate lacks real conflict. See references/troubleshooting.md.)

#### Confidence Persona Simulation

Simulate different confidence levels through persona instructions.

**Pattern:**

```
Analyze [PROBLEM] from two perspectives:

Pass 1 (uncertain analyst): Explain as if you're a junior who overexplains and highlights all uncertainties.

Pass 2 (confident expert): Analyze as a senior expert who is concise and direct about what's known.

Synthesis: Highlight where uncertainty is warranted vs. where confidence is justified.
```

When to use: When you need both careful consideration and decisive judgment.

(Common issue: Perspectives produce similar outputs. See references/troubleshooting.md.)

---

### 6. Advanced Architecture & Integration

Techniques for structuring the prompt, integrating external data, and managing context.

#### System-vs-User-Prompt Layering

Use the "system" prompt to set the model's core identity, rules, and constraints, separating it from the "user" prompt which contains the specific task.

**Pattern:**

```
[SYSTEM PROMPT]
You are an expert [ROLE] assistant. You MUST follow these rules:
1. [CONSTRAINT 1]
2. [CONSTRAINT 2]
3. Your tone is always [TONE].

[USER PROMPT]
[The user's specific question or task]
```

**When to use:** A standard best practice for all modern, large-context models to ensure reliable behavior.

#### Contextual Grounding (RAG Pattern)

Forces the model to base its answer _only_ on provided context, preventing hallucination.

**Pattern:**

```
Use *only* the provided documents below to answer the question.
- You must cite the specific source for each part of your answer.
- If the answer is not in the documents, state that clearly.

Documents:
[PASTE CONTEXT HERE]

Question: [QUESTION]
```

**When to use:** For question-answering over documents, summarizing specific information, or preventing the model from using its internal knowledge.

#### External Tool Integration (Hybrid Prompting)

Instruct the model on when and how to call external tools, APIs, or knowledge sources.

**Pattern:**

```
You can use these tools:
- `get_weather(city)`: Gets the current weather.
- `search_news(topic)`: Searches for recent news.

Task: [USER TASK]

To complete this, first identify which tools you need. Then, call the tools and use their output to formulate your final answer.
```

**When to use:** When the model needs real-time data, specific calculations, or access to external knowledge bases.

#### Structured Output Forcing

Ensures the model's output is in a specific, machine-readable format like JSON or XML.

**Pattern:**

```
Provide your analysis as a valid JSON object.
The JSON must conform to this schema:
{
  "property": "type",
  "nested_property": { ... }
}
Do not include *any* text or explanation before or after the JSON.
```

**When to use:** When integrating the model's output into an application, database, or automated workflow.

#### Context Compression & Memory Management

Techniques for managing long prompts or chat histories to keep the model focused on the most relevant information.

**Pattern:**

```
You are a helpful assistant with a 5-turn memory.
Previous summary: [A summarized version of the chat so far]

New context:
[User provides a long document]

Summarize this document into 5 key bullet points. Then, update your "Previous summary" to include these points before answering my next question.
```

**When to use:** For long-running conversations, multi-document analysis, or when operating near context window limits.

---

### 7. Evaluation & Meta-Reflection

Techniques for having the model evaluate its own output quantitatively and qualitatively.

#### Automatic Evaluation Metrics

Use the model to score its own (or another model's) output against a defined scoring rubric.

**Pattern:**

```
Here is an output generated for a task.
Output: [MODEL OUTPUT]

Evaluate this output against the following metrics on a scale of 1-5:
- **Factual Accuracy (1-5):** Is the information correct? (1=very incorrect, 5=perfectly correct)
- **Coherence (1-5):** Is the answer easy to understand? (1=confusing, 5=very clear)
- **Conciseness (1-5):** Does it answer without unnecessary words? (1=very verbose, 5=very concise)

Provide your scores in a JSON format.
```

**When to use:** For systematically testing and comparing different prompt versions.

#### Self-Critique Phase

A final step where the model explicitly lists the weaknesses of its _own_ output _before_ delivering it.

**Pattern:**

```
[PRIMARY TASK]

...

Before you provide the final answer, perform a self-critique:
1. List the 3 strongest parts of your response.
2. List the 3 weakest parts or potential gaps in your response.
3. Revise your response to fix the weaknesses you identified.
```

**When to use:** When accuracy and thoroughness are more important than speed.

---

## Combining Techniques

Advanced prompters often combine multiple techniques for complex tasks. Instead of using techniques in isolation, you can create powerful workflows by sequencing them strategically.

**Common patterns:**
- **Analysis tasks:** Chain of Verification + Root Chain of Thought + Deliberate Over-Instruction
- **Decision-making:** Multi-Persona Debate + Adversarial Prompting + Self-Critique Phase
- **Technical tasks:** Root Chain of Thought + Failure-Mode Priming + Chain of Verification
- **Creative tasks:** Confidence Persona Simulation + Reference Class Priming + Multi-Path Exploration

For complete workflow blueprints and guidance on creating custom workflows, see `references/workflows.md`.

## Selection Guide (Expanded)

|**Technique**|**Best For**|**Complexity**|
|---|---|---|
|Basic Chain of Thought|Complex reasoning|Low|
|Standard Few-Shot Learning|Format/Style matching|Low|
|Contextual Grounding|Q&A over documents|Low|
|Reverse Prompting|Unknown optimal structure|Low|
|Constraint & Value Bounding|Safety & guardrails|Low|
|Chain of Verification|Accuracy checks|Medium|
|Deliberate Over-Instruction|Exposing reasoning|Medium|
|Recursive Optimization|Iterative improvement|Medium|
|Adversarial Prompting|Finding weaknesses|Medium|
|Root Chain of Thought|Structured analysis|Medium|
|Reference Class Priming|Quality consistency|Medium|
|Confidence Persona Simulation|Balanced analysis|Medium|
|Multi-Path Exploration|Open-ended problems|Medium|
|Structured Output Forcing|API/Automation|Medium|
|Self-Critique Phase|Final quality check|Medium|
|System-vs-User-Prompt Layering|Reliable behavior|Medium|
|Context Compression|Long-context tasks|High|
|Failure-Mode Priming|Boundary detection|High|
|Multi-Persona Debate|Multiple perspectives|High|
|External Tool Integration|Real-time data / API use|High|
|Automatic Evaluation Metrics|Quantitative testing|High|


## Additional Resources

For detailed examples and implementation patterns:

- **`references/BRIEFING.md`** - Introduction to systematic prompt engineering for beginners
- **`references/QUICK_REFERENCE.md`** - Fast lookup cheat sheet for all techniques
- **`references/USAGE_GUIDE.md`** - Comprehensive guide with usage patterns and best practices
- **`references/examples.md`** - Complete prompt examples for each technique
- **`references/troubleshooting.md`** - Common issues and solutions
- **`references/workflows.md`** - Workflow blueprints for combining techniques

**Getting Started:** Read BRIEFING.md, then use QUICK_REFERENCE.md as your daily guide.
