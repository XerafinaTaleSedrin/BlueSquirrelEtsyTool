# Donor Scoring Framework

8-dimension evaluation system for prioritizing donor prospects.

## Scoring Scale

All dimensions use a 1-5 scale:

| Score | Meaning |
|-------|---------|
| 5 | Exceptional - Best possible case |
| 4 | Strong - Above average, favorable |
| 3 | Moderate - Average, acceptable |
| 2 | Weak - Below average, concerning |
| 1 | Poor - Significant issues |

---

## Dimensions & Weights

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Financial Capacity | 20% | Ability to give at target level |
| Political Alignment | 20% | Issue positions match candidate |
| Geographic Connection | 15% | Lives in, works in, or cares about MD-14 |
| Giving History | 15% | Track record of political giving |
| Accessibility | 10% | How reachable via existing network |
| Engagement Potential | 10% | Likelihood of becoming active supporter |
| Risk Factors | 5% | Red flags, reputational concerns (inverted: 5=no risk) |
| Timing | 5% | Ready to give now vs. later |

---

## Dimension Definitions

### 1. Financial Capacity (20%)

Ability to contribute at target levels based on wealth indicators.

| Score | Criteria |
|-------|----------|
| 5 | Clear capacity for max contribution ($6,600+); likely major donor |
| 4 | Capacity for $2,500-$6,600; comfortable major gift |
| 3 | Capacity for $1,000-$2,500; stretch but doable |
| 2 | Capacity for $200-$1,000; mid-level donor |
| 1 | Capacity under $200; small dollar only |

**Indicators:** Real estate holdings, business ownership, executive compensation, prior large gifts, lifestyle indicators.

### 2. Political Alignment (20%)

How well the prospect's political views align with our candidate.

| Score | Criteria |
|-------|----------|
| 5 | Strong alignment on all major issues; enthusiastic supporter profile |
| 4 | Alignment on most issues; minor disagreements on secondary issues |
| 3 | Mixed alignment; agrees on some key issues, unclear on others |
| 2 | Weak alignment; different priorities, some opposing views |
| 1 | Misaligned; supports opposing positions on key issues |

**Indicators:** Past candidate support, issue advocacy, public statements, organizational memberships.

### 3. Geographic Connection (15%)

Strength of connection to Maryland's 14th Congressional District.

| Score | Criteria |
|-------|----------|
| 5 | Lives in MD-14; votes in district |
| 4 | Lives in adjacent MD district; works in MD-14 or has business there |
| 3 | Lives elsewhere in Maryland; has Maryland ties |
| 2 | Former Maryland resident; family or business connections |
| 1 | No direct Maryland connection; only ideological interest |

**Indicators:** Address, employer location, property ownership, family ties, business operations.

### 4. Giving History (15%)

Track record of political contributions and philanthropic giving.

| Score | Criteria |
|-------|----------|
| 5 | Consistent political donor; gives to similar candidates; gives early |
| 4 | Regular political donor; history of supporting Democrats/progressives |
| 3 | Occasional political donor; or strong philanthropic but limited political |
| 2 | Rare political donor; minimal contribution history |
| 1 | No giving history found; or history of supporting opponents |

**Indicators:** FEC records, state contribution databases, foundation giving, nonprofit board service.

### 5. Accessibility (10%)

How easily we can reach and engage this prospect.

| Score | Criteria |
|-------|----------|
| 5 | Direct relationship with candidate or campaign leadership |
| 4 | Strong connection through active supporter; warm intro available |
| 3 | Second-degree connection; intro possible with effort |
| 2 | Weak connection; would need intermediary we don't know well |
| 1 | No known connection; would require cold outreach |

**Indicators:** Relationship mapping, mutual connections, event attendance, network analysis.

### 6. Engagement Potential (10%)

Likelihood of becoming an active supporter beyond just writing a check.

| Score | Criteria |
|-------|----------|
| 5 | High potential: could host events, make introductions, become bundler |
| 4 | Good potential: likely to attend events, may recruit others |
| 3 | Moderate: will give but probably not highly engaged |
| 2 | Low: transaction-only; unlikely to engage further |
| 1 | Very low: prefers anonymity or minimal involvement |

**Indicators:** Past campaign involvement, community leadership, social network size, time availability.

### 7. Risk Factors (5%)

Presence of red flags or reputational concerns. **Note: This dimension is inverted - higher score means LOWER risk.**

| Score | Criteria |
|-------|----------|
| 5 | No risk factors identified; clean background |
| 4 | Minor yellow flags; manageable with awareness |
| 3 | Moderate concerns; requires careful consideration |
| 2 | Significant concerns; proceed only if high value |
| 1 | Major red flags; potential liability to campaign |

**Indicators:** See Risk Assessment Framework for detailed red flag categories.

### 8. Timing (5%)

Readiness to contribute in current cycle and optimal timing.

| Score | Criteria |
|-------|----------|
| 5 | Ready now; expressed interest or historically gives early |
| 4 | Good timing; likely receptive in current quarter |
| 3 | Moderate; may need cultivation before ask |
| 2 | Challenging timing; personal circumstances or other commitments |
| 1 | Poor timing; recently gave elsewhere, financial constraints, or bad moment |

**Indicators:** Recent giving to others, known financial events, personal circumstances, election cycle position.

---

## Calculating Weighted Score

```
Weighted Score = (FC × 0.20) + (PA × 0.20) + (GC × 0.15) + (GH × 0.15) +
                 (AC × 0.10) + (EP × 0.10) + (RF × 0.05) + (TM × 0.05)
```

Where:
- FC = Financial Capacity
- PA = Political Alignment
- GC = Geographic Connection
- GH = Giving History
- AC = Accessibility
- EP = Engagement Potential
- RF = Risk Factors
- TM = Timing

---

## Priority Classification

| Score Range | Priority | Action |
|-------------|----------|--------|
| 4.0 - 5.0 | **Priority A** | Cultivate immediately; high-touch engagement |
| 3.0 - 3.9 | **Priority B** | Cultivate this cycle; regular touchpoints |
| 2.5 - 2.9 | **Priority C** | Maintain awareness; opportunistic engagement |
| Below 2.5 | **Deprioritize** | Remove from active cultivation |

---

## Confidence Adjustment

Each dimension score should include a confidence level:

- **High Confidence:** Based on verified, multiple sources
- **Medium Confidence:** Based on reasonable inference or single source
- **Low Confidence:** Based on limited data or assumption

For overall scoring, low-confidence dimensions may be weighted less heavily or flagged for additional research.

---

## Score Interpretation Notes

- A score of 3.0 is not "bad" - it represents an average prospect worth cultivating
- Very few prospects will score 5.0 across all dimensions
- A single low score doesn't disqualify - it's the weighted total that matters
- Risk factors (Dimension 7) can override high scores if severe enough
- Revisit scores as new information emerges
