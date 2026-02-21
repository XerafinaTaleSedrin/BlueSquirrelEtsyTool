# Donor & Endorsement Research System

## System Overview

This is a structured, multi-client research system for political campaign donor prospecting and endorsement cultivation. It uses a multi-agent workflow with defined checkpoints to ensure quality research and actionable recommendations.

## Purpose

- Research and evaluate potential campaign donors
- Identify and pursue organizational endorsements
- Map relationship networks for warm introductions
- Ensure FEC and state campaign finance compliance
- Prioritize prospects by likelihood and impact
- Support multiple campaign clients simultaneously

---

## Multi-Client Structure

### Campaign Organization

Each client has their own folder in `campaigns/`:

```
campaigns/
├── _CAMPAIGN_TEMPLATE/              # Copy this for new clients
├── 2026 - Smith - MD-14/            # Client 1
├── 2026 - Johnson - VA-07/          # Client 2
└── 2028 - Williams - PA-Senate/     # Client 3
```

### Naming Convention

**Format:** `YYYY - CandidateName - Location`

Examples:
- `2026 - Rodriguez - MD-14`
- `2026 - Chen - CA-45`
- `2028 - Williams - PA-Senate`

### Creating a New Campaign

1. Copy `campaigns/_CAMPAIGN_TEMPLATE/` to a new folder
2. Rename using the naming convention above
3. Update `campaign-profile.md` with candidate and campaign details
4. Customize knowledge-base files for the specific district
5. Begin prospect and endorsement research

### Campaign Folder Structure

Each campaign folder contains:

```
YYYY - Name - Location/
├── campaign-profile.md          # Candidate info, positions, goals
├── prospects/                   # Donor research
│   ├── _PROSPECT_TRACKER.md
│   ├── major-donors/
│   ├── mid-level/
│   ├── bundlers/
│   └── small-dollar/
├── endorsements/                # Endorsement research
│   ├── _ENDORSEMENT_TRACKER.md
│   ├── unions/
│   ├── advocacy-organizations/
│   ├── civic-groups/
│   ├── elected-officials/
│   └── media-newspapers/
├── network-maps/                # Relationship mapping
│   └── _NETWORK_OVERVIEW.md
├── compliance/                  # Campaign-specific compliance notes
└── knowledge-base/              # Campaign-specific knowledge
    ├── district-profile.md
    ├── candidate-positions.md
    ├── prior-campaign-donors.md
    └── endorsement-patterns.md
```

---

## 3-Phase Workflow

### Phase 1: Intake & Validation

**Goal:** Ensure the prospect is worth researching before investing time.

1. Create prospect/endorsement folder using appropriate template
2. Complete intake form with initial hypothesis
3. Run T0 validation checklist (see `frameworks/t0-validation-framework.md`)
4. If blockers found → document reason and deprioritize
5. If clear → create research plan with specific questions to answer

**Checkpoint 1:** Research plan approval before proceeding

### Phase 2: Research Execution

**Goal:** Gather comprehensive intelligence on the prospect.

Launch research agents in parallel:
- **prospect-researcher** (or org-researcher for endorsements)
- **giving-history-analyst**
- **alignment-analyst**
- **relationship-mapper**

Each agent completes their designated template sections.

**Checkpoint 2:** Review findings, identify gaps, approve to proceed to scoring

### Phase 3: Scoring & Strategy

**Goal:** Calculate priority score and develop cultivation approach.

1. **priority-scorer** calculates weighted dimension scores
2. Generate overall priority rating (A/B/C)
3. Develop cultivation/outreach strategy
4. Flag any escalation triggers

**Checkpoint 3:** Approve priority rating and recommended strategy

---

## Agent Coordination

### Starting a New Prospect Research

```
@research-coordinator Create a new prospect research for [NAME] in [CAMPAIGN FOLDER]
```

The coordinator will:
1. Create the folder structure
2. Guide you through intake
3. Run T0 validation
4. Orchestrate the research agents
5. Generate checkpoint reviews

### Running Individual Agents

You can also invoke agents directly:

```
@prospect-researcher Research background for [NAME] in [CAMPAIGN]/prospects/[tier]/[name]/
@giving-history-analyst Analyze giving history for [NAME]
@alignment-analyst Assess political alignment for [NAME]
@relationship-mapper Map network connections for [NAME]
@priority-scorer Calculate final score for [NAME]
```

---

## File Naming Conventions

### Prospect Folders
```
campaigns/[campaign-name]/prospects/[tier]/[lastname-firstname]/
  00_intake.md
  01_research-plan.md
  02_background.md
  03_giving-history.md
  04_alignment.md
  05_relationship-map.md
  06_scoring.md
  07_cultivation-strategy.md
```

### Endorsement Folders
```
campaigns/[campaign-name]/endorsements/[category]/[org-name-slug]/
  00_intake.md
  01_org-research.md
  02_endorsement-history.md
  03_alignment.md
  04_decision-process.md
  05_outreach-strategy.md
```

### Tier Classification
- **major-donors/**: $1,000+ capacity
- **mid-level/**: $200-$999 capacity
- **bundlers/**: Can raise from others regardless of personal capacity
- **small-dollar/**: <$200 (batch research only)

---

## Quality Standards

### Research Completeness
- All template sections must be completed
- "Unknown" is acceptable but must note why (no data available vs. not researched)
- Sources must be cited for all factual claims
- Confidence levels (High/Medium/Low) required for assessments

### Scoring Rigor
- Each dimension score must include justification
- Confidence level affects how scores are weighted
- Red flags must be explicitly addressed
- Recommendations must follow logically from scores

### Checkpoint Reviews
- Cannot proceed without checkpoint approval
- Gaps or concerns must be resolved before advancing
- User can request additional research at any checkpoint

---

## Escalation Triggers

### Immediate Escalation (Stop & Consult)
- Potential legal/compliance issue discovered
- Significant reputational risk identified
- Conflicting information that changes assessment
- Connection to opponent campaign discovered

### Flag for Review
- Borderline T0 validation results
- Mixed signals on alignment
- Complex relationship dynamics
- Unusual giving patterns

---

## Key Frameworks (Shared)

| Framework | Purpose |
|-----------|---------|
| `frameworks/t0-validation-framework.md` | Pre-research blocker checks |
| `frameworks/donor-scoring-framework.md` | 8-dimension donor evaluation |
| `frameworks/endorsement-scoring-framework.md` | 7-dimension endorsement evaluation |
| `frameworks/compliance-framework.md` | FEC rules reference |
| `frameworks/risk-assessment-framework.md` | Red flags and mitigation |
| `frameworks/relationship-mapping-framework.md` | Network analysis methodology |

---

## Quick Start

### Set Up a New Client

1. Copy `campaigns/_CAMPAIGN_TEMPLATE/`
2. Rename to `YYYY - CandidateName - Location`
3. Fill out `campaign-profile.md`
4. Update knowledge-base files

### Research a New Donor Prospect

1. Navigate to the appropriate campaign folder
2. Copy `templates/prospects/00_prospect-intake-template.md` to new prospect folder
3. Fill out intake form
4. Run through T0 validation
5. If approved, proceed through phases

### Research a New Endorsement Target

1. Navigate to the appropriate campaign folder
2. Copy `templates/endorsements/00_endorsement-intake-template.md` to new folder
3. Fill out intake form
4. Run through T0 validation
5. If approved, proceed through phases

### Review Current Prospects

- See `[campaign]/prospects/_PROSPECT_TRACKER.md` for donor prospects
- See `[campaign]/endorsements/_ENDORSEMENT_TRACKER.md` for endorsement targets

---

## Compliance Reminders

- Always verify contribution limits before recommending ask amounts
- Check FEC rules and state-specific rules for each campaign
- Document employer/occupation for contributions $200+
- Flag LLC contributions for additional verification
- Never research minors or non-citizens for contribution purposes
- Each campaign may have different applicable rules (federal vs. state races)
