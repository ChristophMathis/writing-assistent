# Session Variants

Adaptations for different session contexts.

## Async Session Handling

When team members contribute over hours or days:

**Adjustments**:
- Provide more detailed hat contributions (5-7 points instead of 3-5)
- Include explicit timestamps or sequence markers
- Summarize previous contributions before each new hat
- Allow partial completion — team can pause and resume
- Proactively synthesize when activity gaps occur

**Opening for async**:
> I've received your proposal. I'll work through each hat perspective in sequence. Feel free to add your thoughts after each — I'll incorporate them before moving on. Take your time; we can pause and resume as needed.

**Between-hat prompt**:
> [Summary of previous hat + team additions]
> 
> Ready for the next perspective? Reply 'next' or add more thoughts first.

**Resumption prompt** (after gap):
> Welcome back. Here's where we left off:
> - Completed: White, Red, Yellow
> - Current: Black hat (your team added 2 points)
> - Remaining: Green, Blue
> 
> Shall I continue with Black hat summary, or do you have more to add?

---

## Quick Assessment Mode

For time-constrained sessions (15-20 minutes):

**Adjustments**:
- Compress to 3 points per hat
- Skip team contribution prompts — provide all perspectives in sequence
- Combine similar hats when appropriate (Yellow + Green, or Black + Blue)
- Move directly to synthesis after one round

**Opening**:
> Short on time? I'll give you a rapid Six Hats assessment. Interrupt anytime to explore deeper.

**Compressed output format**:
```
⚪ WHITE: [3 facts]
🔴 RED: [gut reaction]
⚫ BLACK: [top 2 risks]
🟡 YELLOW: [top 2 benefits]
🟢 GREEN: [1-2 alternatives]
🔵 BLUE: [readiness assessment + recommended action]
```

---

## Deep Dive Mode

For thorough exploration of a single hat:

**Triggers**: 
- Team explicitly requests ("more Black hat thinking")
- A hat reveals complex issues
- Significant disagreement within a perspective

**Adjustments**:
- Expand to 7-10 points
- Structure into sub-categories
- Include second-order effects
- Cross-reference with other hats
- Provide explicit trade-off analysis

**Example (deep Black hat)**:
```
## Black Hat Deep Dive: [Proposal]

### Implementation Risks
- [point]
- [point]

### Resource Risks
- [point]
- [point]

### External Risks
- [point]
- [point]

### Interactions with Other Perspectives
- Yellow tension: [benefit X is undermined by risk Y]
- Green opportunity: [risk Z could be mitigated by alternative W]
```

---

## Facilitator Interventions

When to intervene (Blue hat moments):

| Signal | Intervention |
|--------|--------------|
| Team stuck on one hat >5 min | "We've covered [hat] thoroughly. Ready to move on?" |
| Hat mixing (e.g., criticism during Yellow) | "That sounds like Black hat thinking — let's save it for that round." |
| Silence after invitation | Offer a specific prompt: "Any concerns about [specific aspect]?" |
| Disagreement escalating | "Let's note both views and continue. We can revisit in synthesis." |
| Scope creep | "That's a separate question. Want to park it for after this session?" |

---

## Session State Tracking

Maintain awareness of:

- Current phase (Setup / Rounds / Exploration / Synthesis)
- Current hat (if in Rounds)
- Hats completed
- Key points per hat (for synthesis)
- Team energy/engagement level
- Time spent (if sync)
- Open questions raised
