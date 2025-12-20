# Detailed Prompt Examples

This document provides complete, ready-to-use examples for each advanced prompting technique.

## 1. Reverse Prompting Examples

### Example: Legal Document Analysis

```
You're an expert prompt designer.
1. Design the single most effective prompt to analyze acquisition agreements for early warning signs of deal risk. 
   Consider:
   - What specific contractual terms matter most for risk assessment
   - What output format would be most actionable for executives
   - What reasoning steps are essential for thorough analysis
2. Critically analyze the prompt you just designed. Identify one potential weakness or ambiguity in it.
3. Provide a revised, stronger version of the prompt that fixes this weakness.
4. Finally, execute the revised prompt on the attached acquisition agreement.
```

### Example: Technical Code Review

```
You're an expert prompt designer.
1. Design the optimal prompt to review this Python codebase for security vulnerabilities and performance issues.
   Consider:
   - What specific vulnerability patterns to check
   - How to prioritize findings by severity
   - What format would be most useful for developers
2. Critically analyze your prompt. Identify one way it could be misinterpreted.
3. Provide a revised, stronger version of the prompt.
4. Execute the revised prompt on the attached code.
```

## 2. Recursive Optimization Examples

### Example: Customer Support Response

```
You're a recursive prompt optimizer. My current prompt is:
"Write a response to this customer complaint about delayed shipping."

Your goal is: Create empathetic, solution-oriented responses that reduce escalations.

Iterate through 3 versions:
- Version 1: Add specific tone guidelines (empathetic, apologetic, solution-oriented) and a clear response structure (Acknowledge, Empathize, Solve, Close).
- Version 2: Include examples of empathy phrases and solution templates (e.g., "I understand how frustrating that is...", "As a solution, I can offer...").
- Version 3: Add constraints for response length (under 150 words) and escalation triggers to avoid (e.g., "do not use the word 'policy'").

Execute the final version on this customer message: [INSERT MESSAGE]
```

### Example: Data Analysis Query

```
You're a recursive prompt optimizer. My current prompt is:
"Analyze the sales data and find trends."

Your goal is: Generate insights with statistical rigor and actionable recommendations.

Iterate through 3 versions:
- Version 1: Specify exact metrics (e.g., MoM growth, avg. order value) and time periods (e.g., last 6 months).
- Version 2: Add statistical significance requirements and request identification of confounding variables.
- Version 3: Define output format (e.g., "JSON with keys 'key_finding', 'supporting_data', 'recommendation'") and add competitive context.

Execute the final version on: [DATA]
```

## 3. Chain of Verification (Internal & External) Examples

### Example: Financial Report Analysis

```
Analyze this quarterly earnings report and list your three most important findings about the company's financial health.

After completing your analysis, you MUST perform a verification:
1. (Internal Check) Identify three ways your analysis might be incomplete (e.g., missing context about industry trends, overlooked footnote disclosures, or unexamined segment performance).
2. (External Check) Cross-reference your finding about 'revenue growth' with the provided 'Investor Relations Transcript'. Cite the specific quote that confirms or refutes it.
3. Revise your three findings based on this verification process.
```

### Example: Technical Architecture Review

```
Review this system architecture diagram and identify the top 3 scalability concerns.

After your initial assessment, you MUST perform a verification:
1. (Internal Check) Identify three ways your analysis might be incomplete (e.g., overlooked single points of failure, missing failure scenarios, or unconsidered load patterns).
2. (External Check) Cross-reference your concern about the 'database bottleneck' with the attached 'Performance Test Results'. Does the data support or contradict your concern?
3. Update your scalability concerns based on this verification.
```

## 4. Adversarial Prompting (Content & Behavior) Examples

### Example: Security Architecture

```
Review this cloud security architecture and provide your assessment.

Now, attack your previous assessment:
1. (Content Attack) Identify five specific ways this architecture could be compromised:
   - For each, describe the attack vector in detail.
   - Assess likelihood (High/Medium/Low) and impact (Critical/High/Medium/Low).
   - Provide specific mitigation steps.
2. (Behavior Attack) Now assume my original request was sarcastic and I'm actually a junior developer who misunderstood the task. How would your original assessment be unhelpful or dangerous?

Provide a revised, more robust assessment.
```

### Example: Business Strategy

```
Analyze this market entry strategy for Southeast Asia.

Now, attack your analysis:
1. (Content Attack) Identify five specific ways this strategy could fail:
   - For each, explain the underlying assumptions that could be wrong.
   - Rate the probability of occurrence and estimated financial impact.
   - Suggest specific contingency plans.
2. (Behavior Attack) How would your analysis change if my request had a hidden, conflicting goal (e.g., "I want to enter the market *and* spend as little as possible")?

Revise your analysis to account for these risks.
```

## 5. Deliberate Over-Instruction Examples

### Example: Product Requirements Analysis

```
Analyze this product requirements document for completeness and feasibility.

CRITICAL: Do not summarize. Expand every point with:
- Specific implementation challenges and dependencies
- Edge cases that aren't explicitly addressed
- Failure modes and error handling requirements
- Historical context from similar features in other products
- Quantitative estimates for development time and complexity
- Specific acceptance criteria that would be needed

Prioritize exhaustive completeness over conciseness. I need to examine your full reasoning.
```

### Example: Research Paper Review

```
Review this machine learning research paper for methodological soundness.

CRITICAL: Do not compress your analysis. For each section (Abstract, Intro, Methods, Results), provide:
- Detailed explanation of the methodology and why it was chosen
- Edge cases and boundary conditions that weren't tested
- Potential failure modes of the proposed approach
- Historical context of similar approaches and their outcomes
- Statistical power analysis and sample size considerations
- Specific follow-up experiments that would strengthen claims

I need exhaustive depth to evaluate reproducibility.
```

## 6. Root Chain of Thought Examples

### Example: Database Performance Issue

```
Diagnose this database performance degradation by completing these steps:

1. Symptom characterization: ___
   (Describe exact behavior, affected queries, timing patterns)
2. Timeline analysis: ___
   (When did it start? What changed? Deploy history?)
3. Resource metrics: ___
   (CPU, memory, disk I/O, network - specific numbers)
4. Query execution plans: ___
   (Identify which queries changed behavior and why)
5. Root cause hypothesis: ___
   (Most likely cause with supporting evidence)
6. Resolution approach: ___
   (Specific remediation steps in order)

Fill each blank with thorough analysis before proceeding.
```

### Example: Sales Pipeline Analysis

```
Analyze why our Q3 sales pipeline is underperforming by completing these steps:

1. Metric comparison: ___
   (Current vs. target vs. historical - specific numbers)
2. Funnel stage breakdown: ___
   (Where is the drop-off occurring? Lead gen? Demo? Close?)
3. Segment analysis: ___
   (Which customer segments, regions, or products are affected?)
4. Root cause identification: ___
   (Primary driver with quantitative evidence)
5. Action plan: ___
   (Prioritized interventions with expected outcomes)

Fill each step completely before moving to the next.
```

## 7. Failure-Mode Priming (F-Shot) Examples

### Example: Input Validation

```
Classify whether each user input is safe or represents a potential security risk.
Learn from these failure modes. For each, explain *why* it's a failure.

Example 1 (Failure): "admin' OR '1'='1"
Why it Fails: This is a classic SQL injection attack that attempts to bypass authentication.
Key Learning: Always sanitize inputs that contain SQL keywords like OR.

Example 2 (Subtle Failure): "John O'Brien"
Why it Fails: The single quote (') can break an SQL query if it's not parameterized or properly escaped, leading to an injection vulnerability.
Key Learning: Single quotes in user input require parameterization, even in "safe" contexts.

Now classify these inputs:
- "Robert'); DROP TABLE users;--"
- "O'Reilly Media"
```

### Example: Contract Clause Interpretation

```
Classify whether each contract clause represents a favorable, neutral, or unfavorable term for the Client.
Learn from these failure modes. For each, explain *why* it's a failure.

Example 1 (Failure): "Client shall indemnify Provider against all claims, including Provider's own negligence."
Why it Fails: This is an unlimited indemnification clause that makes the Client responsible even for the Provider's mistakes.
Key Learning: Indemnification should be mutual and exclude the indemnified party's gross negligence.

Example 2 (Subtle Failure): "Either party may terminate with 90 days notice, provided Client completes all outstanding deliverables."
Why it Fails: This looks mutual, but the "provided" clause makes it asymmetric. The Client's right to terminate is conditional, while the Provider's is not.
Key Learning: Termination clauses must be reviewed for conditional language that creates asymmetry.

Now classify these clauses:
[INSERT ACTUAL CLAUSES TO ANALYZE]
```

## 8. Reference Class Priming Examples

### Example: Technical Documentation

```
Here's an example of the documentation quality I expect:

'''
API Endpoint: POST /api/v2/users

Purpose: Creates a new user account with role-based permissions.

Request Body:
{
  "email": "string (required, must be valid email format)",
  "name": "string (required, 2-100 characters)",
  "role": "enum (required, one of: 'admin', 'user', 'viewer')"
}

Response Codes:
- 201: User created successfully
- 400: Invalid request (missing required fields)
- 409: Email already exists
'''

Now document the following API endpoints with this same level of detail:
[LIST OF ENDPOINTS]
```

### Example: Strategic Analysis

```
Here's an example of the analytical quality I expect:

'''
Market Entry Assessment: Vietnam E-commerce Market

1. Market Size & Growth: Vietnam's e-commerce market reached $13.2B in 2023 (source: Google-Temasek report), growing at 18% CAGR.
2. Competitive Landscape: Dominated by Shopee (42% share) and Lazada (21%). Shopee's advantage is its integrated payment (ShopeePay) and logistics.
3. Regulatory Environment: Data localization laws (Decree 52/2013) require in-country data centers, adding ~$1M in infrastructure cost.
4. Recommendation: Viable but requires $10-15M for first 18 months to compete on CAC and logistics.
'''

Now provide analysis of this expansion opportunity with matching depth:
[EXPANSION SCENARIO]
```

## 9. Multi-Persona Debate (with Referee) Examples

### Example: Build vs. Buy Decision

```
Three experts with conflicting priorities debate whether to build in-house analytics infrastructure or buy a third-Party solution:

Persona 1 (CTO - priorities: technical control, customization, long-term cost):
- Must argue for building in-house
- Emphasize customization needs and vendor lock-in risks

Persona 2 (CFO - priorities: immediate ROI, predictable costs, minimal risk):
- Must argue for buying third-party solution
- Emphasize faster time-to-value and predictable pricing

Each must critique the other's position.

Persona 3 (Referee/CIO):
1. Evaluate the strength of the CTO's and CFO's arguments.
2. Identify the key trade-offs (e.g., control vs. speed, capex vs. opex).
3. Synthesize a final recommendation with a clear decision trigger (e.g., "Buy if TCO < $X, otherwise Build").
```

### Example: Pricing Strategy

```
Three team leads debate pricing strategy for a new SaaS product:

Persona 1 (Sales Leader - priorities: deal velocity, competitive positioning):
- Argues for lower entry price ($49/month) to reduce friction.

Persona 2 (Product Marketing - priorities: brand positioning, value perception):
- Argues for premium pricing ($199/month) to anchor on value.

Each must critique the other's position.

Persona 3 (Referee/Finance):
1. Evaluate both pricing models against CAC payback and LTV targets.
2. Identify the key risk (e.g., "Sales risks low LTV, Marketing risks low adoption").
3. Synthesize a recommendation (e.g., "Start with tiered pricing $99-$299 to test both segments").
```

## 10. Confidence Persona Simulation Examples

### Example: Investment Decision

```
Analyze whether we should invest $2M in this early-stage AI startup.

Pass 1 (Uncertain analyst perspective):
Approach this as if you're a junior analyst. Overexplain your reasoning. Highlight all uncertainties: market size assumptions, competitive dynamics, team execution risk, technology feasibility. Call out what you don't know.

Pass 2 (Confident expert perspective):
Now analyze as a seasoned venture partner. Be concise. Focus on the 3-4 factors that actually matter. Make clear calls on risk vs. return without hedging.

Synthesis:
Compare both perspectives. Identify:
- Where genuine uncertainty exists (e.g., "market size is unknown")
- Where the junior analyst was overthinking (e.g., "team risk is low, expert is right")
- A clear investment recommendation with conditions.
```

### Example: Technical Architecture Decision

```
Evaluate whether to migrate our monolith to microservices.

Pass 1 (Uncertain engineer perspective):
Analyze as a mid-level engineer. Explain all considerations. Highlight risks: operational complexity, distributed system challenges, team skillset gaps, debugging difficulties.

Pass 2 (Confident architect perspective):
Now evaluate as a principal architect who has led 5+ migrations. Cut to what matters: domain boundaries, current pain points, and deployment frequency needs. Make a direct recommendation.

Synthesis:
Reconcile both views:
- Which concerns are valid vs. theoretical
- A phased approach that mitigates risks
- A final go/no-go decision with clear criteria.
```

---

## 11. Basic Chain of Thought (CoT) Examples

### Example: Logic Puzzle

```
There are three boxes. One contains apples, one contains oranges, and one contains both apples and oranges. All three boxes are labeled incorrectly. You can pick only one fruit from one box to determine the correct labels for all three boxes. Which box do you pick from?

Let's think step-by-step.
```

### Example: Multi-Step Calculation

```
A car rental company charges $50 per day, plus $0.20 per mile. If a customer rents a car for 3 days and drives 210 miles, what is the total charge?

Let's think step-by-step.
```

## 12. Multi-Path Exploration Examples

### Example: Marketing Strategy

```
For our new SaaS product launch, identify three distinct potential marketing strategies.
For each strategy:
1. Describe the approach (e.g., "Content Marketing", "Paid Acquisition", "Community Building").
2. List its pros (e.g., "low cost", "fast results", "high LTV").
3. List its cons (e.g., "slow to build", "high cash burn", "hard to scale").
Finally, recommend the best strategy for an early-stage, bootstrapped startup and justify your choice.
```

### Example: Technical Refactoring

```
We need to refactor our legacy user authentication service. Identify three distinct potential solutions.
For each solution:
1. Describe the approach (e.g., "Strangler Fig Pattern", "Big Bang Rewrite", "Incremental Refactor").
2. List its pros (e.g., "low risk", "modern stack", "fastest implementation").
3. List its cons (e.g., "high complexity", "long downtime", "technical debt remains").
Finally, recommend the best solution for a system with high uptime requirements.
```

## 13. Constraint & Value Bounding Examples

### Example: Financial Advice Guardrail

```
A user is asking if they should invest their savings in a specific stock.

TASK: Explain the difference between saving and investing.

CRITICAL CONSTRAINTS:
- You MUST NOT provide financial advice.
- You MUST NOT analyze or give an opinion on any specific stock.
- You MUST state clearly that you are an AI and not a financial advisor.
- You MUST suggest they speak to a qualified professional.
```

### Example: Medical Information Guardrail

```
A user describes symptoms and asks for a diagnosis.

TASK: Provide general information about the described symptoms.

CRITICAL CONSTRAINTS:
- You MUST NOT provide a diagnosis or medical advice.
- You MUST NOT suggest or recommend any specific treatments or medications.
- You MUST state clearly that you are an AI and not a medical professional.
- You MUST strongly suggest they consult a healthcare provider.
```

## 14. Standard Few-Shot Learning Examples

### Example: Sentiment Classification

```
Classify the sentiment of each customer review as Positive, Negative, or Neutral.

Example 1:
Input: "The setup was a nightmare, but the customer support was fantastic."
Output: Neutral

Example 2:
Input: "I'll be recommending this to all my friends!"
Output: Positive

Example 3:
Input: "It works, but the battery life is pretty disappointing."
Output: Negative

Now, for this new input:
Input: "The app crashes every time I try to open it."
Output:
```

### Example: Extracting Key Information

```
Extract the product name and the main complaint from each support ticket.

Example 1:
Input: "My UltraWidget 3000 won't turn on, and I just bought it yesterday."
Output: {"product": "UltraWidget 3000", "complaint": "Won't turn on"}

Example 2:
Input: "The shipping for my PowerBook Pro was delayed by 3 weeks."
Output: {"product": "PowerBook Pro", "complaint": "Shipping delayed"}

Now, for this new input:
Input: "I can't seem to log into the new SuperApp v2."
Output:
```

## 15. System-vs-User-Prompt Layering Examples

### Example: Customer Support Bot

```
[SYSTEM PROMPT]
You are a customer support agent for "QuickShip". You are friendly, helpful, and extremely empathetic.
You MUST follow these rules:
1. Your tone is always apologetic, even if it's not our fault.
2. You MUST NOT blame the customer.
3. You MUST offer one of these two solutions for any complaint: a full refund or a 25% discount on their next order.
4. You MUST NOT use technical jargon.

[USER PROMPT]
My package (Order #12345) still says "processing" after 10 days! Where is it? This is ridiculous!
```

## 16. Contextual Grounding (RAG Pattern) Examples

### Example: Answering from a Document

```
Use *only* the provided document below to answer the question.
- You must cite the specific section of the document for each part of your answer.
- If the answer is not in the document, state that clearly.

Document:
'''
Employee Handbook
Section 1: Welcome
...
Section 2: Time Off Policy
2a. Full-time employees receive 20 days of Paid Time Off (PTO) per year.
2b. PTO accrues at a rate of 1.67 days per month.
2c. Employees must request time off at least 2 weeks in advance.
...
Section 3: Code of Conduct
...
'''

Question: How many vacation days do part-time employees get, and how far in advance must they request time off?
```

## 17. External Tool Integration (Hybrid Prompting) Examples

### Example: Travel Planning

```
You can use these tools:
- `get_weather(city, date)`: Gets the forecasted weather for a city on a specific date.
- `search_flights(origin, destination, date)`: Finds the cheapest flight.
- `Google Hotels(city, date)`: Finds available hotels.

Task: Plan a weekend trip to Paris for me for next Friday. I want to know what the weather will be like and how much the flight from London will cost.

To complete this, first identify which tools you need. Then, call the tools and use their output to formulate your final answer.
```

## 18. Structured Output Forcing Examples

### Example: JSON Output

```
Analyze the following customer feedback and provide your analysis as a valid JSON object.
The JSON must conform to this schema:
{
  "sentiment": "Positive" | "Negative" | "Neutral",
  "key_issues": ["list", "of", "strings"],
  "suggested_action": "string"
}
Do not include *any* text or explanation before or after the JSON.

Feedback: "The new dashboard is way too confusing! I liked the old one. At least the new reporting feature is fast."
```

### Example: XML Output

```
Extract the item, price, and currency from the user request and format it as XML.
Provide *only* the XML.

Request: "Please order me a 12-pack of A-1 batteries, they cost $14.99 USD."

Expected output format:
<order>
  <item>...</item>
  <cost>
    <amount>...</amount>
    <currency>...</currency>
  </cost>
</order>
```

## 19. Context Compression & Memory Management Examples

### Example: Long-running Chat Summary

```
You are a helpful assistant. Here is a summary of our conversation so far:
"User is a product manager named Sarah, working on a new e-commerce app. We have discussed user authentication and are about to discuss payment processing."

New user message:
"Okay, thanks for the info on OAuth. Now, for payments, I'm thinking about Stripe vs. Braintree. What are the main differences in terms of developer experience and international support?"

Task:
1. Answer the user's question.
2. After answering, generate an updated summary of our conversation to be used for the next turn.
```

## 20. Automatic Evaluation Metrics Examples

### Example: Scoring a Summary

```
Here is an original text and a summary.
Original: "The new ML model, 'Condor-7B', was trained on a 1.2T token dataset, comprising 60% code, 20% web text, and 20% academic papers. It shows a 15% improvement on the 'CodeX' benchmark, but struggles with story generation."
Summary: "The Condor-7B model is better at code than stories."

Evaluate the summary against the following metrics on a scale of 1-5:
- **Factual Accuracy (1-5):** Is the information correct? (1=very incorrect, 5=perfectly correct)
- **Conciseness (1-5):** Does it answer without unnecessary words? (1=verbose, 5=concise)
- **Specificity (1-5):** Does it include key quantitative details? (1=very vague, 5=very specific)

Provide your scores in a JSON format.
```

## 21. Self-Critique Phase Examples

### Example: Strategic Memo

```
Draft a memo to the engineering team explaining why we are migrating from a monolith to microservices.

Before you provide the final memo, perform a self-critique:
1. List the 3 strongest parts of your memo (e.g., "clear rationale").
2. List the 3 weakest parts (e.g., "too much jargon", "doesn't address risks").
3. Revise your memo to fix the weaknesses you identified.
```

### Example: Code Explanation

```
Explain this Python code snippet to a junior developer:
`comprehension = [x*x for x in range(10) if x % 2 == 0]`

Before you provide the final answer, perform a self-critique:
1. Is the explanation clear and free of jargon?
2. Did I provide a simpler, non-comprehension equivalent?
3. Did I explain *both* the `x*x` part and the `if x % 2 == 0` part?
Revise your explanation based on your critique.
```

---

## Combining Techniques: Workflow Blueprints

Instead of just sequencing, combine techniques into reusable workflows.

### Blueprint 1: High-Accuracy Analysis

(System Prompt + Contextual Grounding + Root Chain of Thought + Chain of Verification + Self-Critique)

```
[SYSTEM PROMPT]
You are a meticulous financial analyst. Your task is to analyze quarterly reports.
You MUST be objective and base all claims on the provided data.
You MUST follow all constraints.

[USER PROMPT]
Use *only* the attached 'Q3 Earnings Report' and 'Investor Transcript' to answer.

Analyze the company's Q3 performance by completing these steps:
1. Key Financial Highlights: ___ (List 3, with numbers)
2. Main Drivers of Growth: ___ (Cite transcript)
3. Emerging Risks: ___ (Cite report)
4. Outlook vs. Analyst Expectations: ___

After completing the analysis, perform a verification:
1. (Internal Check) Identify one assumption you made that is not explicitly stated.
2. (External Check) Cross-reference your 'Emerging Risks' finding with the 'Investor Transcript'. Is the risk confirmed or downplayed by the CEO?
3. Revise your analysis based on this verification.

Finally, perform a self-critique:
1. Is the analysis purely objective and free of speculative language?
2. Is every claim supported by a citation?
3. Revise to fix any gaps.
```

### Blueprint 2: Robust Tool-Using Agent

(System Prompt + Multi-Path Exploration + External Tool Integration + Structured Output Forcing)

```
[SYSTEM PROMPT]
You are a travel agent bot. You can use these tools:
- `search_flights(origin, destination, date)`
- `search_hotels(city, date, nights)`
- `get_weather(city, date)`
You MUST return your final plan in JSON format.

[USER PROMPT]
I need to go to Berlin from New York for 3 nights, starting next Monday. I need a flight, hotel, and the weather forecast.

Task:
1. (Multi-Path) First, think step-by-step about the *plan* to fulfill this request. What tools do you need to call, in what order, and with what parameters?
2. (Tool Integration) [Simulate tool calls and receive data]
3. (Structured Output) Now, provide the complete travel plan in this exact JSON format. Do not include any other text.
{
  "flight": {
    "airline": "...",
    "price": ...
  },
  "hotel": {
    "name": "...",
    "price_per_night": ...
  },
  "weather_forecast": {
    "day": "...",
    "condition": "...",
    "temp_c": ...
  }
}
```