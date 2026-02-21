# Donor & Endorsement Research Tool

A structured, multi-client research system for political campaign donor prospecting and endorsement cultivation.

## Getting Started

1. **Read the main instructions:** Start with `CLAUDE.md` for the complete workflow guide
2. **Create a campaign:** Copy `campaigns/_CAMPAIGN_TEMPLATE/` and rename it
3. **Understand the frameworks:** Review files in `frameworks/` for scoring criteria and validation rules
4. **Use the templates:** Copy templates from `templates/` when starting new research

## Multi-Client Structure

This system supports multiple campaign clients. Each client gets their own folder:

```
campaigns/
├── _CAMPAIGN_TEMPLATE/           # Template for new campaigns
├── 2026 - Smith - MD-14/         # Example client folder
├── 2026 - Johnson - VA-07/       # Example client folder
└── 2028 - Williams - PA-Senate/  # Example client folder
```

### Naming Convention

Campaign folders use the format: `YYYY - CandidateName - Location`
- `YYYY` - Election year
- `CandidateName` - Candidate's last name (or short identifier)
- `Location` - District/seat (e.g., MD-14, VA-Senate, Chicago-Mayor)

## Directory Structure

```
donorresearch/
├── CLAUDE.md                    # Main workflow instructions
├── .claude/agents/              # Agent definitions for multi-agent workflow
├── frameworks/                  # Scoring and evaluation frameworks (shared)
├── templates/                   # Reusable templates for research (shared)
├── compliance/                  # FEC rules reference (shared)
└── campaigns/                   # Client-specific research
    ├── _CAMPAIGN_TEMPLATE/      # Copy this for new clients
    └── YYYY - Name - Location/  # Each client's folder
        ├── campaign-profile.md  # Client info and candidate positions
        ├── prospects/           # Donor research for this client
        ├── endorsements/        # Endorsement research for this client
        ├── network-maps/        # Relationship mapping for this client
        ├── compliance/          # Client-specific compliance notes
        └── knowledge-base/      # District info and prior donors
```

## Creating a New Campaign

1. Copy the `campaigns/_CAMPAIGN_TEMPLATE/` folder
2. Rename it using the format: `YYYY - CandidateName - Location`
3. Update `campaign-profile.md` with the candidate and campaign details
4. Customize the knowledge-base files for the specific district
5. Begin prospect and endorsement research

## Workflow Overview

### 3-Phase Process

1. **Intake & Validation** - Verify prospect is worth researching
2. **Research Execution** - Gather comprehensive intelligence
3. **Scoring & Strategy** - Calculate priority and develop approach

### Checkpoints

- **Checkpoint 1:** Research plan approval
- **Checkpoint 2:** Research findings review
- **Checkpoint 3:** Priority scoring approval

## Key Concepts

### Donor Tiers
- **Major Donors:** $1,000+ capacity
- **Mid-Level:** $200-$999 capacity
- **Bundlers:** Can raise from networks
- **Small-Dollar:** <$200 (batch research)

### Priority Ratings
- **Priority A (4.0+):** Cultivate immediately
- **Priority B (3.0-3.9):** Cultivate this cycle
- **Priority C (2.5-2.9):** Maintain awareness
- **Below 2.5:** Deprioritize

## Shared Resources

These resources are shared across all campaigns:

| Resource | Purpose |
|----------|---------|
| `frameworks/` | Scoring and evaluation frameworks |
| `templates/` | Research templates to copy into campaigns |
| `compliance/` | FEC contribution limits and rules |
| `.claude/agents/` | Agent definitions for the workflow |

## Files Reference

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Main workflow instructions |
| `campaigns/_CAMPAIGN_TEMPLATE/` | Template for new campaign clients |
| `frameworks/donor-scoring-framework.md` | How donors are evaluated |
| `frameworks/endorsement-scoring-framework.md` | How endorsements are evaluated |
| `frameworks/t0-validation-framework.md` | Pre-research blocker checks |
| `compliance/fec-contribution-limits.md` | Federal contribution limits |
