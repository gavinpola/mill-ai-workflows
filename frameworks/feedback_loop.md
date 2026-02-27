# Self-Improving Feedback Loop Protocol

## Purpose
A systematic approach to iteratively improve outputs through structured feedback from both the Harry Tannenbaum reviewer persona and human stakeholders. This creates a compounding quality improvement over time.

---

## Feedback Sources

### 1. Reviewer Agent (Harry Persona)
- Automatic review of all outputs before human review
- Scores on: Strategic Alignment, Quality, Effectiveness, Scalability
- Provides specific, actionable feedback
- Can approve, request revision, or request rethink

### 2. Human Feedback (Gavin/Stakeholders)
- Final approval authority
- Strategic direction adjustments
- Real-world context the AI may miss
- Preference calibration

---

## Feedback Loop Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        GENERATE OUTPUT                          │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    REVIEWER AGENT EVALUATION                     │
│  - Score on 4 dimensions                                         │
│  - Identify strengths and weaknesses                            │
│  - Generate specific improvement suggestions                     │
└───────────────────────────────┬─────────────────────────────────┘
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
              ▼                                   ▼
      ┌───────────────┐                   ┌───────────────┐
      │   APPROVED    │                   │  NEEDS WORK   │
      │   (Score ≥8)  │                   │  (Score <8)   │
      └───────┬───────┘                   └───────┬───────┘
              │                                   │
              ▼                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                     HUMAN REVIEW                                 │
└───────────────────────────────┬─────────────────────────────────┘
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
              ▼                                   ▼
      ┌───────────────┐                   ┌───────────────┐
      │    SHIP IT    │                   │   FEEDBACK    │
      │               │                   │  PROVIDED     │
      └───────────────┘                   └───────┬───────┘
                                                  │
                                                  ▼
                                    ┌─────────────────────────┐
                                    │    REVISION CYCLE       │
                                    │  (Back to Generate)     │
                                    └─────────────────────────┘
```

---

## Feedback Integration Protocol

### Step 1: Receive Feedback
```markdown
## Feedback Received

### Source: [Reviewer/Human]
### Output: [Name of deliverable]

### Feedback Items:
1. [Specific feedback point]
2. [Specific feedback point]
3. [Specific feedback point]

### Priority Classification:
- Critical: [Must fix before proceeding]
- Important: [Should address in this revision]
- Nice-to-have: [Consider for future iterations]
```

### Step 2: Analyze Feedback
- Identify root cause of each issue
- Determine if feedback conflicts with other requirements
- Assess effort vs. impact for each change
- Flag any unclear feedback for clarification

### Step 3: Plan Revision
```markdown
## Revision Plan

### Changes to Make:
1. [Change X] - Addresses feedback #1, #3
2. [Change Y] - Addresses feedback #2

### Changes NOT Making:
1. [Why not making change Z] - [Rationale]

### Questions for Clarification:
1. [Question if any]
```

### Step 4: Execute Revision
- Make changes systematically
- Document what was changed and why
- Preserve original for comparison if needed

### Step 5: Re-submit for Review
- Include summary of changes made
- Reference original feedback
- Request re-evaluation

---

## Quality Metrics Tracking

Track these metrics across iterations to measure improvement:

| Metric | Definition | Target |
|--------|------------|--------|
| First-pass approval rate | % of outputs approved by Reviewer on first try | >50% |
| Average revision cycles | Mean # of revisions before approval | <2 |
| Human override rate | % where human disagrees with Reviewer | <20% |
| Feedback incorporation rate | % of feedback items addressed | >90% |

---

## Learning Integration

### Pattern Recognition
After each feedback cycle, identify:
1. **Recurring issues**: Same feedback appearing multiple times
2. **Root causes**: Why these issues keep happening
3. **Preventive measures**: How to avoid in future

### Prompt Refinement
Use feedback to improve agent prompts:
```markdown
## Prompt Update Log

### Date: [Date]
### Agent: [Agent name]
### Feedback Pattern: [What kept coming up]
### Prompt Change: [What was added/modified]
### Result: [Did it help?]
```

### Knowledge Base Building
Accumulate learnings:
- What Harry (persona) consistently likes/dislikes
- What human stakeholders value
- Industry-specific requirements
- Effective patterns and anti-patterns

---

## Feedback Templates

### Reviewer → Generator Feedback
```markdown
## Review Feedback

**Output**: [Name]
**Score**: X/10
**Verdict**: [Approved/Revise/Rethink]

### Strengths
- [What works well]

### Required Changes (must address)
1. [ ] [Specific change needed]
2. [ ] [Specific change needed]

### Suggested Improvements (optional)
- [Nice to have]

### Context for Changes
[Why these changes matter]
```

### Human → System Feedback
```markdown
## Human Feedback

**Output**: [Name]
**Overall Reaction**: [Positive/Mixed/Negative]

### What I Liked
- [Specific praise]

### What Needs to Change
1. [Change with context]
2. [Change with context]

### Strategic Direction
[Any broader guidance]

### Questions for Me
[If the system needs clarification]
```

---

## Anti-Patterns to Avoid

1. **Feedback loops without exit**: Always have clear approval criteria
2. **Over-iteration**: Know when good enough is good enough
3. **Conflicting feedback**: Resolve conflicts before implementing
4. **Ignoring patterns**: If same feedback keeps coming, fix the root cause
5. **Subjective spiraling**: Anchor to objective criteria when possible

---

## Integration with Jarvis

Update Jarvis state on each feedback cycle:
```python
# Log feedback events
add_log(f"Reviewer scored {output_name}: {score}/10", "info")
add_log(f"Revision #{n} submitted for {output_name}", "info")
add_log(f"{output_name} approved after {n} revisions", "success")
```

Track revision counts in task status:
```json
{
  "name": "Marketing Deck",
  "status": "in_revision",
  "revision": 2,
  "reviewer_score": 7,
  "feedback_items": 3
}
```
