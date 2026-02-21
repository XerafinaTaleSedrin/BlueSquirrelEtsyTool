# Research Request System for RandomIdeaResearch

## Pattern Recognition: "Research Idea: [NAME]"

This document describes the automated research workflow for business idea exploration and feasibility assessment.

---

## How It Works

### **Pattern Recognition**
When you write: **"Research idea: [IDEA NAME]"**

The system automatically:
1. Creates subfolder with slugified idea name
2. Generates initial brainstorm document (`01_brainstorm.md`)
3. Launches market-validator agent for competitive research
4. Creates entry in `ideas/00_IDEA_PORTFOLIO.md`
5. Sets status to [Researching]

### **Example Usages**

```
"Research idea: AI-powered meal planning for dietary restrictions"
→ Creates: ai-powered-meal-planning-dietary-restrictions/

"Research idea: Elderly care service marketplace"
→ Creates: elderly-care-service-marketplace/

"Research idea: Automated inventory for small restaurants"
→ Creates: automated-inventory-for-small-restaurants/
```

---

## Workflow Progression

### **Stage 1: Initial Brainstorm**
**Trigger**: `"Research idea: [NAME]"`

**System Actions**:
- Creates idea subfolder with slugified name
- Generates `01_brainstorm.md` capturing initial thinking
- Creates entry in portfolio index
- Sets status: [Brainstorm]

**File Created**: `[idea-name]/01_brainstorm.md`

**Contents**:
- What's the idea?
- What problem does it solve?
- Who experiences this problem?
- Initial viability thoughts
- Questions to answer

---

### **Stage 2: Market Research**
**Trigger**: `"Look up competitors for [IDEA]"` or `"Analyze market for [IDEA]"`

**System Actions**:
- Launches market-validator agent
- Generates `02_market-research.md`
- Creates supporting files in `supporting-research/` as needed
- Updates portfolio index
- Sets status: [Researching]

**File Created**: `[idea-name]/02_market-research.md`

**Contents**:
- Executive summary
- Competitive landscape (direct/indirect competitors)
- Market size & trends
- Customer segments
- Differentiation opportunities
- Red flags
- Opportunity signals
- Sources (all URLs documented)

**Market Validator Agent** searches for:
- Existing solutions (competitors, alternatives)
- Market size estimates
- Customer characteristics
- Pricing data
- Critical question: "Why hasn't this been done already?"

**Supporting Research Files** (created as needed):
- `competitor-01_[name].md` - Detailed competitor analysis
- `market-01_[segment].md` - Specific market research
- `technology-01_[aspect].md` - Technical investigation

---

### **Stage 3: Feasibility Analysis**
**Trigger**: `"Analyze feasibility of [IDEA]"`

**System Actions**:
- Launches feasibility-analyzer agent
- Generates `03_feasibility-analysis.md`
- Assesses technical/financial/operational dimensions
- Updates portfolio index
- Sets status: [Feasibility Analysis]

**File Created**: `[idea-name]/03_feasibility-analysis.md`

**Contents**:
- Executive summary
- Technical feasibility (complexity 1-5, requirements, timeline, risks)
- Financial feasibility (startup costs, monthly costs, revenue model, break-even)
- Operational feasibility (requirements, complexity, team needs)
- Scalability analysis
- Risk summary table
- Overall viability rating

**Feasibility Analyzer Agent** evaluates:
- Technical complexity and development requirements
- Cost estimates (startup + ongoing)
- Revenue model viability
- Operational requirements
- Risk identification and rating

---

### **Stage 4: Decision Framework**
**Trigger**: `"Create decision framework for [IDEA]"`

**System Actions**:
- Launches decision-framework-builder agent
- Synthesizes all prior research
- Generates `04_decision-framework.md`
- Updates portfolio index
- Sets status: [Decision Pending]

**File Created**: `[idea-name]/04_decision-framework.md`

**Contents**:
- Executive summary
- Evaluation scores (5 dimensions, 1-5 scale each)
- SWOT analysis
- Critical assumptions
- Key uncertainties
- Decision reasoning
- Go/No-Go/On-Hold recommendation
- Confidence level
- Specific next steps
- Lessons learned

**Decision Framework Builder Agent** provides:
- Scored evaluation across 5 dimensions
- SWOT analysis
- Assumption identification
- Clear recommendation with reasoning
- Next steps based on decision

---

### **Stage 5: Decision Executed**

**If Go**:
- Status updated to: [Go]
- Idea stays in active portfolio with link to external project
- Research preserved for reference
- Next steps initiated

**If No-Go**:
- Status updated to: [No-Go]
- Folder moved to `archive/rejected/`
- Reasons documented in decision framework
- Lessons extracted to `playbook/`
- Related pivots noted

**If On Hold**:
- Status updated to: [On Hold]
- Stays in active portfolio
- Conditions for reconsideration documented
- Trigger date or event noted

---

## Additional Research Commands

Beyond the main workflow, these commands support deeper analysis:

### Competitive Analysis
```
"Look up [SPECIFIC COMPETITOR] for [IDEA]"
→ Creates detailed competitor analysis file

"Compare [IDEA] to [COMPETITOR]"
→ Generates side-by-side comparison
```

### Market Deep Dive
```
"Research [MARKET SEGMENT] for [IDEA]"
→ Creates market segment analysis

"Analyze pricing for [IDEA]"
→ Generates pricing analysis
```

### Technical Investigation
```
"Evaluate technical requirements for [IDEA]"
→ Deep dive on technology needs

"Research [TECHNOLOGY] for [IDEA]"
→ Technology-specific investigation
```

---

## File Naming Conventions

### Idea Folders
Format: `[lowercase-hyphen-separated-description]`

**Good Examples**:
- `ai-meal-planner-dietary-restrictions`
- `elderly-care-service-marketplace`
- `restaurant-inventory-automation`

**Rules**:
- Lowercase only
- Hyphen-separated words
- Descriptive enough to understand at a glance
- No dates (use git history for timeline tracking)

### Core Research Files
**Always numbered sequentially**:
- `01_brainstorm.md`
- `02_market-research.md`
- `03_feasibility-analysis.md`
- `04_decision-framework.md`

### Supporting Research Files
**Format**: `[type]-[##]_[topic].md`

**Types**:
- `competitor-` : Detailed competitor analysis
- `market-` : Market segment or trend research
- `technology-` : Technical investigation
- `customer-` : Customer research or interviews
- `financial-` : Financial modeling or analysis

**Examples**:
- `competitor-01_blue-apron.md`
- `competitor-02_hellofresh.md`
- `market-01_meal-kit-industry-2025.md`
- `technology-01_dietary-restriction-apis.md`
- `customer-01_parent-interviews.md`

---

## Status Workflow

Ideas progress through these states:

```
[Brainstorm]
    ↓
[Researching] (Market research in progress)
    ↓
[Feasibility Analysis] (Technical/financial assessment)
    ↓
[Decision Pending] (Evaluation complete, ready to decide)
    ↓
┌───────────┼───────────┐
↓           ↓           ↓
[Go]    [No-Go]   [On Hold]
```

### Status Definitions

**[Brainstorm]** - Initial capture, curiosity exploration
- File: `01_brainstorm.md` created
- Questions identified
- Problem defined

**[Researching]** - Active market/competitive research
- File: `02_market-research.md` in progress or complete
- Market validator agent active
- Competitors being identified

**[Feasibility Analysis]** - Technical/financial/operational assessment
- File: `03_feasibility-analysis.md` in progress or complete
- Feasibility analyzer agent active
- Viability being evaluated

**[Decision Pending]** - Evaluation complete, ready to decide
- File: `04_decision-framework.md` complete
- All research synthesized
- Recommendation made
- Awaiting final decision

**[Go]** - Pursuing this idea
- Moved to external project (link maintained in portfolio)
- Next steps initiated
- Research stays accessible

**[No-Go]** - Not pursuing
- Archived to `archive/rejected/`
- Reasons documented
- Lessons extracted to playbook

**[On Hold]** - Interesting but not now
- Stays in active portfolio
- Conditions for reconsideration documented
- Periodic review scheduled

---

## Quality Standards

Every research file must meet these standards:

### Market Research (`02_market-research.md`)
- ✓ 5-8 competitors/alternatives identified
- ✓ Market size estimate with source
- ✓ Customer segments clearly defined
- ✓ Pricing data from at least 3 existing solutions
- ✓ Honest answer to "why hasn't this been done already?"
- ✓ Trend direction indicated (growing/stable/declining)
- ✓ All sources documented with URLs

### Feasibility Analysis (`03_feasibility-analysis.md`)
- ✓ Technical complexity rated (1-5 with justification)
- ✓ Startup cost estimate (range acceptable)
- ✓ Monthly operating cost estimate
- ✓ Timeline estimate for development
- ✓ Operational requirements clearly defined
- ✓ Risks identified and rated (critical/significant/moderate/low)
- ✓ Clear viability rating for each dimension

### Decision Framework (`04_decision-framework.md`)
- ✓ All 5 dimensions scored (1-5 scale)
- ✓ Justification for each score
- ✓ SWOT analysis completed
- ✓ Critical assumptions explicitly identified
- ✓ Uncertainties honestly acknowledged
- ✓ Clear recommendation (go/no-go/on-hold) with confidence level
- ✓ Specific next steps (not vague)
- ✓ Lessons extracted for future evaluations

---

## Integration with Portfolio Index

`ideas/00_IDEA_PORTFOLIO.md` is automatically updated when:

1. **New Idea Researched**
   - Entry added to Active Ideas table
   - Status set to [Brainstorm] or [Researching]
   - Priority assigned
   - Link to idea folder created

2. **Status Changes**
   - Status column updated
   - Last Updated date refreshed
   - Notes column may be updated

3. **Decision Made**
   - Status updated to [Go], [No-Go], or [On Hold]
   - Entry moved to appropriate section
   - Decision date recorded

4. **Priority Adjusted**
   - Priority column updated (High/Medium/Low)
   - May trigger reordering in table

The portfolio index provides:
- Quick overview of all active ideas
- Status distribution summary
- Priority-based organization
- Links to individual idea folders
- Decision history
- Pattern insights

---

## Playbook Integration

As ideas are evaluated, patterns and lessons are extracted to `playbook/`:

### `patterns-that-work.md`
Automatically updated when ideas marked [Go]:
- Market characteristics that proved viable
- Customer segment patterns
- Technology approaches that worked
- Pricing model patterns
- Common success factors

### `red-flags.md`
Automatically updated when ideas marked [No-Go]:
- Warning signs discovered during research
- Market conditions that made ideas unviable
- Technical complexities that stalled progress
- Financial model issues
- Common failure patterns

### `evaluation-insights.md`
Updated with each decision:
- What made evaluation easier/harder
- Assumptions that proved critical
- Research methodology improvements
- Decision criteria refinements

---

## Example: Full Research Workflow

### 1. Initial Trigger
```
User: "Research idea: AI-powered personal stylist using wardrobe photos"
```

**System Response**:
1. Creates `ai-powered-personal-stylist-wardrobe-photos/`
2. Generates `01_brainstorm.md` from conversation
3. Launches market-validator agent
4. Creates entry in `00_IDEA_PORTFOLIO.md`
5. Sets status: [Researching]

### 2. Market Research Phase
```
User: "Look up competitors for AI stylist"
```

**System Response**:
1. Generates `02_market-research.md`
2. Finds competitors: Stitch Fix, Wishi, Thread, Cladwell, etc.
3. Analyzes market size, pricing, gaps
4. Creates `supporting-research/competitor-01_stitch-fix.md`
5. Updates portfolio status

### 3. Feasibility Phase
```
User: "Analyze feasibility of AI stylist idea"
```

**System Response**:
1. Generates `03_feasibility-analysis.md`
2. Assesses:
   - Technical: AI/computer vision complexity (4/5)
   - Financial: Startup costs, ongoing costs, revenue model
   - Operational: App development, user acquisition, support
3. Identifies risks
4. Status: [Feasibility Analysis]

### 4. Decision Phase
```
User: "Create decision framework for AI stylist"
```

**System Response**:
1. Generates `04_decision-framework.md`
2. Synthesizes all research
3. Scores 5 dimensions:
   - Technical Feasibility: 3/5
   - Financial Feasibility: 2/5
   - Operational Feasibility: 3/5
   - Market Timing: 4/5
   - Personal Fit: 2/5
4. Overall: 2.8/5 (below 3.0 threshold)
5. SWOT analysis completed
6. Recommendation: **No-Go** - Market saturated, high technical complexity, low personal fit
7. Status: [Decision Pending]

### 5. User Decision
```
User: "I agree with the no-go recommendation. Archive this idea."
```

**System Response**:
1. Moves folder to `archive/rejected/`
2. Extracts lesson to `playbook/red-flags.md`:
   - "AI/ML projects with low personal ML expertise = high risk"
   - "Check market saturation early before deep research"
3. Updates portfolio index with decision
4. Status: [No-Go]

---

## Quick Commands Reference

### Research Trigger
```
"Research idea: [IDEA NAME]"
```

### Market Research
```
"Look up competitors for [IDEA]"
"Analyze market for [IDEA]"
"Find existing solutions for [PROBLEM]"
"Compare [IDEA] to [COMPETITOR]"
```

### Feasibility Assessment
```
"Analyze feasibility of [IDEA]"
"Evaluate technical requirements for [IDEA]"
"Estimate costs for [IDEA]"
"Research [TECHNOLOGY] for [IDEA]"
```

### Decision Framework
```
"Create decision framework for [IDEA]"
"Should I pursue [IDEA]?"
"Compare [IDEA A] vs [IDEA B]"
```

### Portfolio Management
```
"Show idea portfolio status"
"List active ideas"
"Show ideas in [STATUS]"
"What's in the backlog?"
```

---

## Best Practices

1. **Start Small** - Begin with brainstorm, don't jump to full feasibility
2. **Be Systematic** - Follow the workflow stages in order
3. **Be Honest** - Research is about finding truth, not validating enthusiasm
4. **Document Sources** - Always capture URLs and references
5. **Extract Lessons** - Every decision teaches something
6. **Use the Backlog** - Capture ideas quickly, research selectively
7. **Review Playbook** - Learn from past patterns
8. **Make Decisions** - Don't linger in research - move to go/no-go/on-hold

---

## Future Enhancements

Possible future additions to the system:
- Idea comparison framework (side-by-side evaluation)
- Validation experiment tracking
- Customer interview templates
- MVP scoping frameworks
- Financial modeling templates
- Pitch deck generation (for Go ideas)
- Post-mortem tracking (for pursued ideas)
