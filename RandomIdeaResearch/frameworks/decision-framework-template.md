# Decision Framework Template

**Purpose**: Structured decision-making process for go/no-go on business ideas.

This framework defines how to synthesize research into clear, data-driven decisions about which ideas to pursue.

---

## Decision Document Structure

Every decision framework should include these sections:

### 1. Executive Summary

**Format**:
```markdown
# Decision Framework: [Idea Name]

**Date**: YYYY-MM-DD
**Research Time Invested**: [X hours]
**Decision**: [Go / No-Go / On Hold]
**Confidence**: [High / Medium / Low]

## Executive Summary
[One paragraph: What's the idea, what did we learn, what's the recommendation]
```

**Content**:
- One-paragraph summary of the idea
- Key findings from research
- Overall recommendation (go/no-go/on-hold)
- Confidence level in the decision
- Primary reason for the decision

**Example**:
> AI-powered meal planning for dietary restrictions would enter a saturated market dominated by well-funded incumbents (Blue Apron, HelloFresh, Factor). While the market is large ($5B+), our feasibility analysis reveals high technical complexity (4/5), significant startup costs ($50K+), and low personal fit (limited ML expertise). Overall score: 2.4/5. **Recommendation: No-Go**. The combination of market saturation and high technical barriers without unique differentiation makes this unviable.

---

### 2. Evaluation Scores

**Format**:
```markdown
## Evaluation Scores

| Dimension | Score | Summary |
|-----------|-------|---------|
| Technical Feasibility | X/5 | [One sentence] |
| Financial Feasibility | X/5 | [One sentence] |
| Operational Feasibility | X/5 | [One sentence] |
| Market Timing | X/5 | [One sentence] |
| Personal Fit | X/5 | [One sentence] |
| **Overall** | **X.X/5** | [Weighted average or simple average] |
```

**Requirements**:
- All 5 dimensions must be scored
- Each score must have a one-sentence justification
- Overall score must be calculated (average or weighted)
- Use the scoring rubric from `feasibility-evaluation-criteria.md`

**Scoring Reference**:
- **5**: Exceptional - Major advantage
- **4**: Strong - Clear viability
- **3**: Adequate - Acceptable but not standout
- **2**: Weak - Concerning limitations
- **1**: Critical - Likely fatal flaw

---

### 3. SWOT Analysis

**Format**:
```markdown
## SWOT Analysis

**Strengths**:
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]

**Weaknesses**:
- [Concern 1]
- [Concern 2]
- [Concern 3]

**Opportunities**:
- [Upside 1]
- [Upside 2]
- [Upside 3]

**Threats**:
- [Risk 1]
- [Risk 2]
- [Risk 3]
```

**Guidelines**:

**Strengths** (Internal positive factors):
- What advantages does this idea have?
- What unique capabilities or insights?
- What market gaps does it fill?
- What competitive advantages?

**Weaknesses** (Internal negative factors):
- What limitations or disadvantages?
- What skills or resources are lacking?
- What's difficult or challenging?
- What competitive disadvantages?

**Opportunities** (External positive factors):
- What favorable trends or conditions?
- What could go exceptionally well?
- What positive surprises are possible?
- What market shifts could help?

**Threats** (External negative factors):
- What unfavorable trends or conditions?
- What could derail this?
- What competitive responses?
- What market shifts could hurt?

---

### 4. Critical Assumptions

**Format**:
```markdown
## Critical Assumptions

Assumptions that must hold true for this idea to succeed:

1. [Market assumption]
   - **Impact if wrong**: [What happens]
   - **How to validate**: [What to test]

2. [Customer assumption]
   - **Impact if wrong**: [What happens]
   - **How to validate**: [What to test]

3. [Technical assumption]
   - **Impact if wrong**: [What happens]
   - **How to validate**: [What to test]

4. [Financial assumption]
   - **Impact if wrong**: [What happens]
   - **How to validate**: [What to test]

5. [Operational assumption]
   - **Impact if wrong**: [What happens]
   - **How to validate**: [What to test]
```

**Guidelines**:
- List 3-7 critical assumptions
- Focus on assumptions that could be wrong and would matter
- For each, describe impact if wrong
- For each, note how to validate
- Be honest about what you're assuming vs. what you know

**Examples**:
- "Customers will pay $X/month" (financial)
- "We can build this in 3 months" (technical)
- "Market is growing at Y% per year" (market)
- "Competitors won't respond aggressively" (competitive)
- "Regulatory environment stays stable" (operational)

---

### 5. Key Uncertainties

**Format**:
```markdown
## Key Uncertainties

What we still don't know:

- **[Uncertainty 1]**
  - Why it matters: [Impact]
  - To resolve: [What to do]
  - Cost to validate: [Time/money]

- **[Uncertainty 2]**
  - Why it matters: [Impact]
  - To resolve: [What to do]
  - Cost to validate: [Time/money]

- **[Uncertainty 3]**
  - Why it matters: [Impact]
  - To resolve: [What to do]
  - Cost to validate: [Time/money]
```

**Guidelines**:
- Be honest about what you don't know
- Distinguish between "unknown but knowable" vs. "fundamentally uncertain"
- Prioritize uncertainties by potential impact
- Note cost/effort to resolve each uncertainty
- Don't let uncertainty paralyze - decide with available information

**Examples**:
- "Actual customer acquisition cost" - matters for profitability, resolve with test campaign ($500 budget)
- "Time to build MVP" - matters for runway, resolve with technical prototype (2 weeks)
- "Willingness to pay at $X price point" - matters for revenue model, resolve with landing page test ($200 + 1 week)

---

### 6. Decision Reasoning

**Format**:
```markdown
## Decision Reasoning

[2-4 paragraphs explaining the decision logic]

**Key Factors**:
- [Factor that drove decision 1]
- [Factor that drove decision 2]
- [Factor that drove decision 3]

**Decision Criteria Applied**:
- Minimum score threshold: [e.g., 3.0 average, no dimension below 2]
- Deal-breakers: [What made this definite no, if applicable]
- Must-haves: [What was required to say yes, if applicable]

**Tradeoff Analysis**:
- What we're trading off: [If pursuing]
- Opportunity cost: [What else could we do with time/resources]
- Risk tolerance: [What risks we're accepting or avoiding]
```

**Guidelines**:
- Explain the logic, not just the conclusion
- Reference specific data from research
- Acknowledge tradeoffs and alternatives
- Be honest about uncertainty and risk
- Connect to personal priorities and constraints

**For Go Decisions**:
- What makes this compelling despite risks?
- What unique advantages or timing factors?
- What risks are acceptable and why?
- What's the upside case?

**For No-Go Decisions**:
- What were the deal-breakers?
- What would need to change for reconsideration?
- What did we learn?
- Are there pivots or related ideas to explore?

**For On-Hold Decisions**:
- Why not now?
- What conditions would change this to go?
- When to revisit?
- What to monitor in the meantime?

---

### 7. Recommendation & Next Steps

**For Go Decisions**:
```markdown
## Recommendation: GO

**Confidence Level**: [High / Medium / Low]

**Why**: [1-2 sentences on primary rationale]

**Next Steps**:
1. **Immediate action** (this week):
   - [Specific action]
   - [Specific action]

2. **Validation experiments** (2-4 weeks):
   - [What to test]
   - [Success criteria]
   - [Budget: $X, Time: Y hours]

3. **MVP scope** (if validation succeeds):
   - [Core features only]
   - [Timeline estimate]
   - [Resource requirements]

4. **Decision checkpoints**:
   - [Milestone 1]: Reassess if [condition]
   - [Milestone 2]: Reassess if [condition]
   - Stop if: [Clear stop criteria]

**Resources Required**:
- Time: [X hours/week]
- Money: $[Y startup + $Z/month]
- Skills to acquire: [List]
- Help needed: [What to outsource or get help with]

**Success Metrics** (for first 3 months):
- [Metric 1]: [Target]
- [Metric 2]: [Target]
- [Metric 3]: [Target]
```

**For No-Go Decisions**:
```markdown
## Recommendation: NO-GO

**Confidence Level**: [High / Medium / Low]

**Primary Reason**: [One sentence explaining main deal-breaker]

**Key Learnings**:
1. [What did we learn from this research]
2. [Pattern to remember for future ideas]
3. [Skill or knowledge gained]

**Related Ideas to Explore**:
- [Pivot 1]: [How this could be adapted]
- [Pivot 2]: [Adjacent opportunity]
- [Related concept]: [Different approach to similar problem]

**Add to Playbook**:
- Red flags: [Specific warning signs to watch for]
- Patterns: [Market or technical patterns observed]
- Insights: [Evaluation methodology improvements]

**Archive Decision**:
- Move to: `archive/rejected/`
- Document: [Reason for rejection]
- Lessons: [Extract to playbook files]
```

**For On-Hold Decisions**:
```markdown
## Recommendation: ON HOLD

**Confidence Level**: [High / Medium / Low]

**Reason for Deferral**: [Why not now]

**Conditions for Reconsideration**:
1. [Condition 1]: [What would need to change]
2. [Condition 2]: [What would need to happen]
3. [Condition 3]: [What threshold to meet]

**When to Revisit**:
- Date trigger: [Specific date or timeframe]
- Event trigger: [Market event, personal milestone, etc.]
- Periodic review: [Every X months]

**Lightweight Monitoring**:
- [What to track]: Google Alert, competitor monitoring, etc.
- [How often]: Weekly check, monthly review, etc.
- [Stop condition]: If [X happens], reconsider or archive

**Why This Could Work Later**:
- [Future scenario 1]
- [Future scenario 2]

**Why Not Now**:
- [Current constraint 1]
- [Current constraint 2]
```

---

### 8. Lessons Learned

**Format**:
```markdown
## Lessons Learned

**For Future Idea Evaluation**:
- [Pattern to remember]
- [Red flag to watch for]
- [Insight gained]
- [Methodology improvement]

**Market Insights**:
- [Industry pattern observed]
- [Customer behavior learned]
- [Competitive dynamic noted]

**Personal Insights**:
- [Self-awareness gained]
- [Skill gap identified]
- [Preference clarified]

**Research Process**:
- [What worked well in research]
- [What to do differently next time]
- [Tool or source discovered]
```

**Guidelines**:
- Extract lessons regardless of go/no-go decision
- Focus on generalizable patterns, not just this specific idea
- Note both positive and negative learnings
- Capture methodology improvements
- These feed into playbook files

---

## Decision Criteria

### Quantitative Thresholds

**For "Go" consideration**:
- ✓ No dimension scored below 2 (no critical flaws)
- ✓ Overall average score ≥ 3.0
- ✓ At least one dimension scored 4+ (has a strength)
- ✓ No "Critical" risks without mitigation plan

**For "No-Go" consideration**:
- Any dimension scored 1 (deal-breaker)
- Overall average score < 2.5
- Multiple "Critical" risks
- No path to viability identified

**For "On-Hold" consideration**:
- Score between 2.5-3.5 but timing is wrong
- Viable but dependent on external factors
- Good idea but personal constraints prevent pursuit now
- Needs more validation but not urgent

### Qualitative Factors

**Consider saying "Go" if**:
- Unique insight or unfair advantage
- Clear market gap with growing demand
- Reasonable path to first customers
- Aligned with personal goals and skills
- Acceptable risk/reward ratio

**Consider saying "No-Go" if**:
- "Why hasn't this been done?" has concerning answer
- Market saturated with well-funded incumbents
- Economics don't work (can't build, can't monetize)
- Requires skills/resources far beyond reach
- Personal misalignment or low interest

**Consider "On-Hold" if**:
- Good idea but wrong time (too early or need preparation)
- Dependent on external factor (job change, funding, skill acquisition)
- Lower priority than other opportunities
- Cyclical opportunity (revisit in X months)

---

## Confidence Levels

**High Confidence**:
- Extensive research completed
- Clear data on all dimensions
- Decision is obvious from the data
- Few remaining uncertainties
- Consensus between head and gut

**Medium Confidence**:
- Good research but some gaps
- Mixed signals or tradeoffs
- Decision seems right but not certain
- Notable uncertainties remain
- Head and gut mostly aligned

**Low Confidence**:
- Limited research or major gaps
- Conflicting data or unclear signals
- Decision feels uncertain
- Many critical uncertainties
- Head and gut diverge

**What to do with low confidence**:
- If No-Go: Confidence level matters less (when in doubt, say no)
- If Go: Do more research or start with small validation experiments
- If On-Hold: Set specific conditions for reconsideration

---

## Quality Checklist

Before finalizing decision framework, verify:

- [ ] All 5 dimensions scored with justification
- [ ] SWOT analysis completed (3+ items in each quadrant)
- [ ] Critical assumptions identified (3-7 items)
- [ ] Key uncertainties acknowledged
- [ ] Decision reasoning explained (not just stated)
- [ ] Clear recommendation (go/no-go/on-hold)
- [ ] Confidence level specified
- [ ] Specific next steps defined (not vague)
- [ ] Lessons extracted for playbook
- [ ] Decision aligns with quantitative thresholds

---

## Decision-Making Principles

1. **Decide, don't linger**: Perfect information doesn't exist. Make the best decision with available data, document assumptions, and move forward.

2. **Default to no**: When uncertain, say no. There will always be more ideas. Protect time and resources for high-conviction opportunities.

3. **Be honest about why**: Don't rationalize. If it's gut feel, acknowledge it. If it's data-driven, show the data.

4. **Extract lessons always**: Every decision is a learning opportunity. Capture insights for future evaluations.

5. **Update as you learn**: It's okay to change your mind if new information emerges. Revisit decisions periodically.

6. **Small steps for uncertainty**: If excited but uncertain, start with small validation experiments rather than full commitment.

7. **Kill your darlings**: Don't get emotionally attached. If data says no-go, have discipline to walk away.

8. **Document thoroughly**: Future you will want to know why you decided what you decided. Be clear and specific.

---

## Common Decision Mistakes

**Confirmation Bias**:
- ❌ Researching only to validate, not to understand
- ✓ Actively look for reasons why idea won't work

**Sunk Cost Fallacy**:
- ❌ "I've already spent X hours researching, I should pursue it"
- ✓ Make decision based on future prospects, not past investment

**Optimism Bias**:
- ❌ Assuming everything will go according to plan
- ✓ Use pessimistic estimates, plan for delays and setbacks

**Analysis Paralysis**:
- ❌ Researching forever, never deciding
- ✓ Set research timeboxes, decide with available data

**Emotional Attachment**:
- ❌ "I love this idea so much, I'll make it work"
- ✓ Let data inform decision, not just passion

**Ignoring Red Flags**:
- ❌ "Yes, but..." responses to every concern
- ✓ Take warning signs seriously, don't rationalize away

**Comparing to Outliers**:
- ❌ "But look at [unicorn success story]"
- ✓ Compare to median outcomes, not exceptional cases

---

## After the Decision

### If Go:
1. Update `ideas/00_IDEA_PORTFOLIO.md` status to [Go]
2. Create project repository or workspace
3. Link from portfolio to new project
4. Start with validation experiments
5. Set decision checkpoints
6. Track against success metrics

### If No-Go:
1. Move folder to `archive/rejected/`
2. Update portfolio with decision date and reason
3. Extract lessons to playbook:
   - Add red flags to `playbook/red-flags.md`
   - Note patterns to `playbook/patterns-that-work.md` (what to avoid)
   - Update `playbook/evaluation-insights.md`
4. Note any related ideas or pivots for future exploration

### If On-Hold:
1. Update status in portfolio to [On Hold]
2. Document reconsideration conditions
3. Set calendar reminder for review date
4. Create lightweight monitoring (Google Alerts, etc.)
5. Keep in active ideas folder for periodic review

---

## Example: Complete Decision Framework

See actual idea folders for complete examples. Every decision framework should be thorough enough that you can look back 6 months later and understand exactly why you decided what you decided.

The decision framework is the culmination of all research - make it count.
