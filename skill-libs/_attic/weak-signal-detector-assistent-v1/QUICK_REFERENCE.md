# Weak Signal Detection Skill - Quick Reference

## What It Does
Supports organizational designers in establishing weak signal detection capabilities by assessing readiness, implementing detection methods, and building cultural/structural enablers.

## Core Components

### 📋 Assessment Tools
- **assess_readiness.py** - Automated readiness evaluation across 4 dimensions
- **assessment_questionnaire.md** - 80-question detailed assessment survey

### 🔍 Detection & Classification
- **classify_signals.py** - Signal classification, prioritization, and response options
- **detection_methods.md** - 8 comprehensive detection methods with procedures

### 🏛️ Cultural & Structural Foundations
- **cultural_enablers.md** - Deep dive into 5 cultural + 5 structural prerequisites
- Implementation roadmap (3 phases, 24 months)

## The 6-Step Workflow

1. **Assess Readiness** → Evaluate cultural and organizational conditions
2. **Identify Gaps** → Determine what needs strengthening  
3. **Design Interventions** → Develop targeted improvement initiatives
4. **Implement Methods** → Establish detection processes and tools
5. **Build Capacity** → Train people and create support systems
6. **Monitor & Refine** → Track effectiveness and improve

## Quick Start Guide

### If You're Starting from Scratch:
```bash
1. Run: python scripts/assess_readiness.py
2. Read: references/cultural_enablers.md (focus on your weak dimensions)
3. Use SKILL.md Step 2 to design interventions
4. Start with 1-2 simple detection methods
5. Focus on building psychological safety first
```

### If You Need to Classify Signals:
```bash
1. Run: python scripts/classify_signals.py
2. Use the framework in SKILL.md Step 4
3. Assess impact across 5 criteria (1-5 score each)
4. Calculate priority score = impact × urgency / 5
5. Match response to priority level
```

### If Culture Is the Blocker:
```bash
1. Deep dive: references/cultural_enablers.md
2. Focus on these indicators:
   - Can people share observations that contradict leadership?
   - Are mistakes discussed without blame?
   - Is curiosity rewarded?
   - Can assumptions be challenged?
   - Is "I don't know" acceptable?
3. Design cultural interventions from SKILL.md Step 2
```

## The 4 Readiness Dimensions

### Cultural (30% weight)
- Psychological Safety
- Curiosity Orientation  
- Openness to Challenge
- Tolerance for Ambiguity
- Learning Culture

### Structural (25% weight)
- Cross-Functional Communication
- Information Flow
- Decision-Making Autonomy
- Peripheral Vision Mechanisms
- Boundary-Spanning Roles

### Cognitive (25% weight)
- Diverse Perspectives
- Systems Thinking
- Scenario Planning Capability
- Pattern Recognition Skills
- Sense-Making Processes

### Resource (20% weight)
- Time Allocation
- Dedicated Roles
- Technology Infrastructure
- Analytical Capabilities
- External Network Access

## Maturity Levels

| Level | Label | Description | Focus |
|-------|-------|-------------|-------|
| 1 | Initial | Ad-hoc, reactive | Build awareness |
| 2 | Developing | Informal practices | Formalize processes |
| 3 | Defined | Inconsistent application | Standardize methods |
| 4 | Managed | Regular practice | Optimize linkages |
| 5 | Optimizing | Integrated culture | Lead innovation |

## 8 Detection Methods

1. **Horizon Scanning** - Systematic examination across domains (STEEP-V)
2. **Pattern Recognition** - Clustering trends, detecting anomalies
3. **Peripheral Vision** - Boundary spanning, cognitive diversity
4. **Scenario Planning** - Exploring multiple futures, identifying indicators
5. **Delphi Method** - Expert panels, anonymous rounds, convergence
6. **Bibliometric Analysis** - Research trends, citation networks
7. **Social Listening** - Digital conversations, hashtag tracking
8. **Stakeholder Ethnography** - Customer observation, lead users

## Signal Classification

### Types
Technological • Social • Economic • Environmental • Political • Competitive • Regulatory • Consumer

### Strength Levels
Very Weak → Weak → Emerging → Moderate → Strong

### Time Horizons
Immediate (0-1y) • Short (1-3y) • Medium (3-5y) • Long (5-10y) • Very Long (10+y)

### Impact Criteria (score 1-5)
1. Strategic Relevance (25%)
2. Disruptive Potential (25%)
3. Opportunity Value (20%)
4. Threat Severity (20%)
5. Scope of Impact (10%)

### Priority Levels & Responses

**Immediate Action** (≥4.0)
→ Fast-track review, form team, allocate resources

**High Priority** (3.0-3.9)
→ Deep analysis, stakeholder engagement, pilot

**Monitor Actively** (2.0-2.9)
→ Regular monitoring, expand sources, build capabilities

**Track & Review** (<2.0)
→ Radar reports, set triggers, annual review

## Common Challenges → Solutions

| Challenge | Solution |
|-----------|----------|
| No time | Start small (15 min/week), embed in existing processes |
| Signal noise | Prioritization frameworks, focus on strategic relevance |
| No action | Clear escalation paths, link to decision-making |
| No sharing | Build psychological safety, reward sharing |
| Miss signals | Diversify sources, challenge assumptions, reduce filtering |
| Analysis paralysis | Set deadlines, start with experiments, accept uncertainty |

## Critical Success Factors

✓ **Psychological safety first** - Nothing works without it
✓ **Start small** - Build momentum with early wins  
✓ **Focus on strategic relevance** - Not all signals matter equally
✓ **Integrate, don't separate** - Connect to existing processes
✓ **Culture before structure** - Mindsets enable methods
✓ **Celebrate learning** - Including from "wrong" signals
✓ **Leadership commitment** - Sustained attention and resources
✓ **Regular cadences** - Weekly/monthly/quarterly rhythms

## Key Documents in Skill

| Document | Size | Purpose |
|----------|------|---------|
| SKILL.md | Core | Complete workflow and guidance |
| assess_readiness.py | Script | Automated readiness assessment |
| classify_signals.py | Script | Signal classification framework |
| detection_methods.md | 5k words | 8 methods with procedures |
| cultural_enablers.md | 7k words | Cultural/structural prerequisites |
| assessment_questionnaire.md | 3k words | 80-question detailed survey |

## Resource Requirements

### Minimal Start (Level 1→2)
- 15-30 min/week per person
- Cross-functional forum (monthly)
- Basic collaboration tool
- Leadership sponsorship

### Building Capability (Level 2→3)
- 10-20% time for selected roles
- Dedicated coordinator (0.5-1.0 FTE)
- Signal repository system
- Training investment

### Mature Capability (Level 3→4)
- Scanning team (2-4 FTE)
- Technology platform
- External information sources
- Integration with strategy processes

## Quick Wins to Build Momentum

1. **Week 1**: Conduct readiness assessment
2. **Week 2**: Share assessment results with leadership
3. **Week 3**: Select 2-3 priority improvement areas
4. **Week 4**: Launch pilot scanning in receptive unit
5. **Month 2**: First signal sharing session
6. **Month 3**: First signal leads to strategic discussion
7. **Quarter 2**: Formalize processes and expand participation

## When to Use Each Resource

**Need overall guidance?** → Read SKILL.md

**Want to assess readiness?** → Run assess_readiness.py or use assessment_questionnaire.md

**Need to understand cultural factors?** → Read cultural_enablers.md

**Ready to implement detection?** → Read detection_methods.md

**Have signals to classify?** → Run classify_signals.py

**Designing interventions?** → Use SKILL.md Step 2 + cultural_enablers.md

**Building processes?** → Use SKILL.md Step 5

## Expected Timeline

**Phase 1: Foundation** (Months 1-6)
- Assess readiness
- Build psychological safety
- Launch pilot scanning
- Early wins and learning

**Phase 2: Expansion** (Months 7-12)
- Formalize processes
- Expand participation
- Enhance technology
- Refine methods

**Phase 3: Integration** (Months 13-24)
- Full strategic integration
- Sophisticated analysis
- Mature governance
- Continuous improvement

## Remember

- Weak signals are **early, ambiguous indicators** - not predictions
- Success = **noticing, interpreting, and acting** on emerging change
- Culture > Structure > Methods - build foundations first
- Perfect is the enemy of good - start imperfect, improve over time
- The goal is **organizational adaptability**, not perfect foresight

---

**For Complete Details**: See SKILL.md and reference documents in the skill package.

**Get Started**: `python scripts/assess_readiness.py`
