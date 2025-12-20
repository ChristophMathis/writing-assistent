# Workflow Blueprints

Instead of just sequencing techniques, combine them into reusable workflows for common use cases.

## Blueprint 1: High-Accuracy Analysis

Ideal for critical analysis where accuracy is paramount (financial reports, legal documents, research papers).

**Workflow:**
1. **System Prompt:** Set constraints & role
2. **Contextual Grounding:** Provide all source data
3. **Root Chain of Thought:** Guide the analysis steps
4. **Chain of Verification:** Force internal _and_ external checks
5. **Self-Critique Phase:** Final polish

**Use when:** Analyzing documents where errors have serious consequences.

## Blueprint 2: Robust Tool-Using Agent

Ideal for applications that integrate external tools, APIs, or real-time data.

**Workflow:**
1. **System Prompt:** Define tools and rules
2. **Multi-Path Exploration:** Brainstorm _which_ tools to use
3. **External Tool Integration:** Call tools and get data
4. **Structured Output Forcing:** Format the final answer for an application

**Use when:** Building agents that need to interact with external systems.

## Blueprint 3: Creative Ideation & Refinement

Ideal for brainstorming, product design, strategic planning, or creative writing.

**Workflow:**
1. **Reverse Prompting:** Design a good prompt for ideation
2. **Confidence Persona Simulation:** Generate both "wild" and "safe" ideas
3. **Multi-Persona Debate:** Critique the ideas from different user perspectives
4. **Reference Class Priming:** Refine the best idea to match a "gold standard" example

**Use when:** You need creative solutions that are also practical and well-vetted.

## Creating Custom Workflows

When designing your own workflows:

1. **Identify the goal:** What outcome do you need?
2. **List critical requirements:** Accuracy? Speed? Format? Safety?
3. **Select 3-5 techniques** that address those requirements
4. **Sequence logically:** Generation → Verification → Refinement
5. **Test and iterate:** Run on real examples and adjust

## Common Workflow Patterns

**For Analysis Tasks:**
- Chain of Verification + Root Chain of Thought + Deliberate Over-Instruction

**For Decision-Making:**
- Multi-Persona Debate + Adversarial Prompting + Self-Critique Phase

**For Technical Tasks:**
- Root Chain of Thought + Failure-Mode Priming + Chain of Verification

**For Creative Tasks:**
- Confidence Persona Simulation + Reference Class Priming + Multi-Path Exploration

**For Production Systems:**
- System-vs-User-Prompt Layering + Contextual Grounding + Constraint & Value Bounding + Structured Output Forcing
