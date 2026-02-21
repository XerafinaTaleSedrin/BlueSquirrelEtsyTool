# CLAUDE.md - RandomIdeaResearch Market Research Infrastructure

This file provides guidance to Claude Code when working with this repository.

## Project Type: Market Research & Idea Feasibility Assessment

This is **not a traditional software development codebase**. It's a systematic workspace for researching random business/startup ideas, evaluating feasibility, and making informed go/no-go decisions.

### Purpose
- Research random business ideas to explore viability
- Determine if ideas already exist in the market
- Assess technical, financial, and operational feasibility
- Make data-driven decisions about which ideas to pursue
- Build personal pattern recognition for viable opportunities

---

## System Architecture: Hub-and-Spokes

The repository uses a **hub-and-spokes architecture**:
- **Central hub**: Shared evaluation frameworks, research methodologies, decision templates
- **Individual spokes**: One subfolder per idea, each containing progressive research documentation

### HUB: Shared Resources (Root Level)

#### **`frameworks/` Directory**
Evaluation methodologies that apply to all ideas:
- `market-research-methodology.md` - How to research markets systematically
- `feasibility-evaluation-criteria.md` - Technical/financial/operational assessment framework
- `decision-framework-template.md` - Structured decision-making process
- `competitive-analysis-framework.md` - How to analyze existing solutions

#### **`templates/` Directory**
Document templates for consistent research outputs:
- `01_brainstorm-template.md` - Initial idea capture structure
- `02_market-research-template.md` - Competitive landscape format
- `03_feasibility-analysis-template.md` - Viability assessment structure
- `04_decision-framework-template.md` - Go/no-go decision format

#### **`.claude/agents/` Directory**
Specialized AI agents for research tasks:
- `market-validator.md` - Competitive landscape analysis and market opportunity assessment
- `feasibility-analyzer.md` - Technical/financial/operational viability evaluation
- `decision-framework-builder.md` - Structured decision support and recommendations

#### **`ideas/` Directory**
Portfolio tracking and quick capture:
- `00_IDEA_PORTFOLIO.md` - Master index of all ideas (like TABLE_OF_CONTENTS)
- `idea-backlog.md` - Quick capture for future exploration

#### **`playbook/` Directory**
Personal knowledge base (grows over time):
- `patterns-that-work.md` - Market characteristics of viable ideas
- `red-flags.md` - Warning signs and patterns to avoid
- `evaluation-insights.md` - Lessons from go/no-go decisions

### SPOKES: Individual Ideas

Each idea gets its own subfolder with progressive documentation:

```
[idea-name]/
├── 01_brainstorm.md           # Initial thinking, problem definition
├── 02_market-research.md      # Competitive landscape, market size
├── 03_feasibility-analysis.md # Technical/financial/operational viability
├── 04_decision-framework.md   # SWOT, scoring, go/no-go recommendation
├── supporting-research/       # Deep dives on specific aspects
│   ├── competitor-XX_[name].md
│   ├── market-XX_[segment].md
│   └── technology-XX_[aspect].md
└── assets/                    # Screenshots, diagrams, mockups
```

---

## Research Request System

### Pattern: **"Research idea: [IDEA NAME]"**

When you write: **"Research idea: AI meal planning for dietary restrictions"**

The system automatically:
1. Creates idea subfolder with slugified name (`ai-meal-planning-dietary-restrictions/`)
2. Generates initial brainstorm document (`01_brainstorm.md`)
3. Launches market-validator agent for competitive research
4. Creates entry in `ideas/00_IDEA_PORTFOLIO.md`
5. Sets status to [Researching]

**Additional Commands:**
- `"Look up competitors for [IDEA]"` → Generate market research
- `"Analyze feasibility of [IDEA]"` → Generate feasibility analysis
- `"Create decision framework for [IDEA]"` → Generate decision document

### Example Workflow

```
User: "Research idea: AI-powered meal planning for dietary restrictions"
→ System creates folder, brainstorm doc, launches market research

User: "Analyze feasibility of AI meal planner"
→ System generates feasibility analysis (technical/financial/operational)

User: "Create decision framework for AI meal planner"
→ System synthesizes research into scored evaluation with recommendation
```

---

## Workflow States

Ideas progress through these stages:

1. **[Brainstorm]** - Initial capture, problem exploration
2. **[Researching]** - Active market/competitive research
3. **[Feasibility Analysis]** - Technical/financial/operational assessment
4. **[Decision Pending]** - Evaluation complete, ready to decide
5. **[Go]** - Pursuing (moved to external project, link maintained)
6. **[No-Go]** - Not pursuing (archived with reasons documented)
7. **[On Hold]** - Interesting but not now (conditions for reconsideration noted)

---

## File Naming Conventions

### Idea Folders
Format: `[lowercase-hyphen-separated-description]`

Examples:
- `ai-meal-planner-dietary-restrictions`
- `elderly-care-service-marketplace`
- `restaurant-inventory-automation`

### Core Research Files (within idea folders)
Always numbered sequentially:
- `01_brainstorm.md`
- `02_market-research.md`
- `03_feasibility-analysis.md`
- `04_decision-framework.md`

### Supporting Research Files (in `supporting-research/`)
Format: `[type]-[##]_[topic].md`

Types:
- `competitor-` : Detailed competitor analysis
- `market-` : Market segment or trend research
- `technology-` : Technical investigation
- `customer-` : Customer research or interviews
- `financial-` : Financial modeling or analysis

Examples:
- `competitor-01_blue-apron.md`
- `market-01_meal-kit-industry.md`
- `technology-01_dietary-restriction-apis.md`

---

## Using Custom Agents

### Market Validator
**Consult when:**
- Starting research on new idea
- Looking for competitors and existing solutions
- Assessing market size and opportunity
- Identifying differentiation opportunities
- Need to answer "does this already exist?"

**What it does:**
- Searches for direct and indirect competitors
- Analyzes market size and trends
- Identifies customer segments
- Surfaces "why hasn't this been done?" insights
- Documents red flags and opportunity signals

### Feasibility Analyzer
**Consult when:**
- Evaluating technical requirements
- Assessing financial viability (costs, revenue model)
- Understanding operational complexity
- Identifying risks and constraints
- Need to know if this is actually buildable

**What it does:**
- Rates technical complexity (1-5 scale)
- Estimates startup and ongoing costs
- Analyzes revenue model viability
- Assesses operational requirements
- Identifies and rates risks

### Decision Framework Builder
**Consult when:**
- Need structured evaluation of an idea
- Creating go/no-go recommendation
- Comparing multiple ideas
- Defining next steps after research
- Ready to make a decision

**What it does:**
- Scores idea across 5 dimensions (1-5 scale each)
- Creates SWOT analysis
- Identifies critical assumptions
- Makes recommendation (go/no-go/on-hold)
- Defines specific next steps
- Extracts lessons for playbook

---

## Progressive Documentation Workflow

Each idea follows this progression:

### Stage 1: Brainstorm
**File**: `01_brainstorm.md`
- What's the idea?
- What problem does it solve?
- Who experiences this problem?
- Initial viability thoughts
- Questions to answer

**Trigger**: "Research idea: [NAME]"

### Stage 2: Market Research
**File**: `02_market-research.md`
- Who's already doing this?
- What exists in the market?
- How big is the market?
- Who are the customers?
- What are the gaps/opportunities?

**Trigger**: "Look up competitors for [IDEA]"

**Agent**: market-validator

### Stage 3: Feasibility Analysis
**File**: `03_feasibility-analysis.md`
- Technical feasibility (complexity, requirements, timeline)
- Financial feasibility (costs, revenue, break-even)
- Operational feasibility (what it takes to run this)
- Scalability assessment
- Risk identification

**Trigger**: "Analyze feasibility of [IDEA]"

**Agent**: feasibility-analyzer

### Stage 4: Decision Framework
**File**: `04_decision-framework.md`
- Evaluation scores (5 dimensions)
- SWOT analysis
- Critical assumptions
- Key uncertainties
- Go/No-Go/On-Hold recommendation
- Next steps
- Lessons learned

**Trigger**: "Create decision framework for [IDEA]"

**Agent**: decision-framework-builder

---

## Evaluation Framework Overview

Every idea is evaluated across **5 dimensions** (scored 1-5):

1. **Technical Feasibility** - Can this be built? What's the complexity?
2. **Financial Feasibility** - What does it cost? Can it make money?
3. **Operational Feasibility** - Can this be run? What's required?
4. **Market Timing** - Is the market ready? Are trends favorable?
5. **Personal Fit** - Do I have skills/interest? Will I commit?

**Decision Thresholds:**
- No dimension below 2 (critical flaws are deal-breakers)
- Average score of 3.0+ across all dimensions
- At least one dimension rated 4+ (needs a strength)

---

## Quality Standards

### Market Research Must Include:
- ✓ 5-8 competitors/alternatives identified
- ✓ Market size estimate with source
- ✓ Customer segments defined
- ✓ Pricing data from existing solutions
- ✓ Honest answer to "why hasn't this been done?"
- ✓ Trend direction (growing/stable/declining)
- ✓ All sources documented with URLs

### Feasibility Analysis Must Include:
- ✓ Technical complexity rated (1-5 with justification)
- ✓ Cost estimates (startup + monthly ongoing)
- ✓ Timeline estimates for development
- ✓ Operational requirements clearly defined
- ✓ Risks identified and rated (critical/significant/moderate/low)
- ✓ Clear viability rating for each dimension

### Decision Framework Must Include:
- ✓ All 5 dimensions scored (1-5)
- ✓ SWOT analysis completed
- ✓ Critical assumptions explicitly identified
- ✓ Uncertainties honestly acknowledged
- ✓ Clear recommendation with confidence level
- ✓ Specific next steps (not vague)
- ✓ Lessons extracted for future evaluations

---

## Portfolio Management

### Tracking Ideas
`ideas/00_IDEA_PORTFOLIO.md` serves as the master index:
- All active ideas with current status
- Priority levels (high/medium/low)
- Last updated dates
- Quick notes
- Links to idea folders

**Updated when:**
- New idea researched
- Status changes
- Decision made
- Priority adjusted

### Quick Capture
`ideas/idea-backlog.md` for rapid idea capture:
- Simple bulleted list
- One-line descriptions
- No research commitment yet
- Review periodically to select ideas for full research

### Archive System
**Pursued Ideas** (`archive/pursued/`):
- Ideas moved forward to external projects
- Research preserved for reference
- Links to actual projects
- Outcomes tracked

**Rejected Ideas** (`archive/rejected/`):
- Ideas not pursued with reasons documented
- Full research preserved
- Patterns extracted to playbook
- Related pivots noted

---

## Key Philosophy

This workspace is about **systematic exploration without bias**. The goal is to:

1. **Explore thoroughly before committing** - Understand what exists, what's feasible, what it really takes
2. **Make data-driven decisions** - Ground choices in research, not enthusiasm or fear
3. **Learn from every idea** - Whether go or no-go, extract lessons for future evaluations
4. **Build pattern recognition** - Over time, recognize viable opportunities faster
5. **Be ruthlessly honest** - Better to find problems during research than after commitment

### What This Is NOT:
- ❌ Not a place to validate ideas you've already decided to pursue
- ❌ Not optimistic brainstorming without critical analysis
- ❌ Not a graveyard of abandoned ideas (decisions are documented and learned from)
- ❌ Not perfectionism or analysis paralysis (decide with available data, document assumptions)

### What This IS:
- ✓ Systematic idea exploration with consistent methodology
- ✓ Honest assessment of viability (strengths AND weaknesses)
- ✓ Learning lab for understanding what makes ideas work
- ✓ Decision-forcing process (move to go/no-go/on-hold, don't linger)
- ✓ Personal knowledge base that improves evaluation over time

---

## Documentation References

For detailed guidance, see:

- **Research Methodology**: `frameworks/market-research-methodology.md`
- **Feasibility Criteria**: `frameworks/feasibility-evaluation-criteria.md`
- **Decision Templates**: `frameworks/decision-framework-template.md`
- **Competitive Analysis**: `frameworks/competitive-analysis-framework.md`
- **Research Request System**: `.claude/RESEARCH_REQUEST_SYSTEM.md`
- **Portfolio Index**: `ideas/00_IDEA_PORTFOLIO.md`

---

## Getting Started

### To Research a New Idea:
```
"Research idea: [YOUR IDEA NAME]"
```

### To Track Research Progress:
Check `ideas/00_IDEA_PORTFOLIO.md`

### To Capture Quick Ideas:
Add to `ideas/idea-backlog.md`

### To Learn from Past Decisions:
Review `playbook/` files (patterns, red flags, insights)

---

This system treats **idea evaluation as a structured, repeatable process** where AI assists in market intelligence and feasibility assessment guided by systematic frameworks—enabling faster, more confident decisions about which opportunities to pursue.
