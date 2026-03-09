# Mill AI Workflow System Architecture

## Overview

This document describes the architecture of Mill's AI workflow system - a **reusable, interconnected agent network** designed for scalable enterprise targeting and content generation.

**Key principle:** This is a system, not a collection of one-off tasks. Every component is designed to be reused, composed, and improved over time.

---

## Inspiration Sources & How They're Applied

### 1. GSD Protocol (Get Shit Done)
**Source:** https://github.com/gsd-build/get-shit-done

**Key concepts adopted:**
| GSD Concept | Our Implementation |
|-------------|-------------------|
| Context engineering | Agent prompts stored in `agents/*.md` with focused scope |
| Wave-based execution | Parallel research agents, sequential content generation |
| Atomic tasks | Each deliverable is a discrete, completable unit |
| State management | `jarvis/state.json` tracks progress, enables resume |
| Human checkpoints | Review phases before major deliverables |

**What we took:**
- Structured phases (Foundation → Research → Execute → Review)
- Keeping context focused by spawning specialized agents
- State persistence for resumability

**What we adapted:**
- Simplified for single-session use (not full project lifecycle)
- More fluid phase transitions (not strict gates)

### 2. Gas Town Multi-Agent Architecture
**Source:** https://github.com/steveyegge/gastown

**Key concepts adopted:**
| Gas Town Concept | Our Implementation |
|------------------|-------------------|
| The Mayor | Facilitator agent - orchestrates all workflows |
| Polecats (workers) | Specialized agents (Researcher, DeckBuilder, etc.) |
| Convoys (work units) | Tasks tracked in Jarvis state |
| Hooks (persistence) | State.json + output files preserve work |

**What we took:**
- Central orchestrator pattern (Facilitator)
- Specialized worker agents with focused prompts
- Persistent state that survives restarts

**What we adapted:**
- Lighter weight than full Gas Town (no git worktree hooks)
- Agent spawning via Claude Code's Task tool rather than separate processes

### 3. Claude Cookbooks Patterns
**Source:** https://github.com/anthropics/claude-cookbooks

**Patterns applied:**
| Pattern | Where Used |
|---------|-----------|
| Sub-agents (Haiku under Opus) | Model selection rules in Facilitator |
| Tool use | Web research, file generation |
| Persona prompting | Harry Tannenbaum reviewer |
| Structured output | MECE frameworks, deck templates |

**What we took:**
- Persona-based review (Harry Tannenbaum character)
- Model tiering for cost optimization
- Structured output formats (reveal.js, markdown tables)

---

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        JARVIS DASHBOARD                         │
│                    (jarvis/tui.py + state.json)                │
│         Real-time visibility into agents, tasks, progress       │
└─────────────────────────────────────────────────────────────────┘
                                 ▲
                                 │ Updates state
                                 │
┌─────────────────────────────────────────────────────────────────┐
│                      FACILITATOR AGENT                          │
│                    (agents/facilitator.md)                      │
│                                                                 │
│  Responsibilities:                                              │
│  • Own the master plan                                          │
│  • Route tasks to appropriate agents                            │
│  • Track progress and dependencies                              │
│  • Enforce quality gates (reviewer before ship)                 │
│  • Select models based on task complexity                       │
└─────────────────────────────────────────────────────────────────┘
         │                    │                    │
         │ Research           │ Execute            │ Review
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   RESEARCHER    │  │  DECK BUILDER   │  │ REVIEWER-HARRY  │
│                 │  │                 │  │                 │
│ • Web search    │  │ • reveal.js gen │  │ • Harry persona │
│ • Data analysis │  │ • Speaker notes │  │ • Score 1-10    │
│ • Synthesis     │  │ • Variants      │  │ • Feedback      │
│                 │  │                 │  │ • Approve/Revise│
└─────────────────┘  └─────────────────┘  └─────────────────┘
         │                    │
         │                    ▼
         │           ┌─────────────────┐
         │           │  DASHBOARD GEN  │
         │           │                 │
         │           │ • Data ingest   │
         │           │ • Auto-visualize│
         │           │ • HTML output   │
         │           └─────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│                         SPAWNER AGENT                           │
│                      (agents/spawner.md)                        │
│                                                                 │
│  Creates new specialized agents on demand:                      │
│  • Audience-variant generator                                   │
│  • Industry-specific researcher                                 │
│  • Custom analysis agents                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## Workflow Pipelines

### Pipeline 1: Enterprise Target Generation

```
INPUT: "Find next whale target for Mill"
                │
                ▼
┌─────────────────────────────────┐
│     MECE SCORING FRAMEWORK      │
│   (frameworks/opportunity_      │
│         scoring.md)             │
│                                 │
│  Dimensions:                    │
│  • Market Size (25%)            │
│  • Sustainability (20%)         │
│  • Operational Fit (20%)        │
│  • Strategic Value (20%)        │
│  • Accessibility (15%)          │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     PARALLEL RESEARCH           │
│                                 │
│  Spawn N researcher agents:     │
│  • Researcher-Grocery           │
│  • Researcher-Hospitality       │
│  • Researcher-Tech              │
│  (parallel execution)           │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     SCORE & RANK                │
│                                 │
│  Apply framework to findings    │
│  Output: ranked_targets.md      │
└─────────────────────────────────┘
                │
                ▼
OUTPUT: Prioritized target list with scores and rationale
```

### Pipeline 2: Marketing Deck Generation

```
INPUT: Target company + meeting context
                │
                ▼
┌─────────────────────────────────┐
│     DEEP RESEARCH               │
│                                 │
│  • Company intel                │
│  • Sustainability programs      │
│  • Decision makers              │
│  • Pain points                  │
│  • Competitive landscape        │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     DECK BUILDER                │
│  (agents/deck_builder.md)       │
│                                 │
│  • Apply template               │
│  • Generate reveal.js           │
│  • Create speaker notes         │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     AUDIENCE VARIANTS           │
│  (agents/deck_audience_         │
│         variants.md)            │
│                                 │
│  Generate versions for:         │
│  • Sustainability leader        │
│  • Procurement leader           │
│  • CFO                          │
│  • CEO                          │
│  • IT/Tech leader               │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     HARRY REVIEWER              │
│                                 │
│  • Score each variant           │
│  • Provide feedback             │
│  • Approve or revise            │
└─────────────────────────────────┘
                │
                ▼
OUTPUT: Reviewed deck variants + speaker notes
```

### Pipeline 3: Customer Data Dashboard

```
INPUT: Customer data file (CSV, JSON, Excel, Parquet)
                │
                ▼
┌─────────────────────────────────┐
│     DATA INGESTOR               │
│                                 │
│  • Auto-detect format           │
│  • Normalize columns            │
│  • Profile data quality         │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     INSIGHT GENERATOR           │
│                                 │
│  • Analyze patterns             │
│  • Generate recommendations     │
│  • Flag anomalies               │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     VISUALIZATION SELECTOR      │
│                                 │
│  Based on data profile:         │
│  • Time series → line chart     │
│  • Categories → doughnut        │
│  • Locations → bar chart        │
│  • Metrics → stat cards         │
└─────────────────────────────────┘
                │
                ▼
┌─────────────────────────────────┐
│     DASHBOARD GENERATOR         │
│                                 │
│  • Generate HTML + Chart.js     │
│  • Apply Mill branding          │
│  • Export insights JSON         │
└─────────────────────────────────┘
                │
                ▼
OUTPUT: Branded HTML dashboard + insights file
```

---

## Model Selection Strategy

Implementing cost-conscious execution per the original prompt:

| Task Type | Model | Rationale | Est. Cost |
|-----------|-------|-----------|-----------|
| Strategic planning, synthesis | Opus | Complex reasoning needed | $$$ |
| Research, content generation | Sonnet | Good quality/cost balance | $$ |
| Simple transforms, formatting | Haiku | Fast and cheap | $ |
| Code generation | Sonnet | Structured output | $$ |

**Decision rules:**
1. Start with Sonnet for most tasks
2. Escalate to Opus for strategic/synthesis work
3. Use Haiku for high-volume, simple operations
4. Track model usage in Jarvis state for cost awareness

---

## State Management

### Jarvis State Schema
```json
{
  "session_start": "ISO timestamp",
  "current_phase": "foundation|research|execution|review|complete",
  "agents": [
    {
      "name": "Agent name",
      "status": "active|running|idle|completed|error",
      "task": "Current task description",
      "model": "opus|sonnet|haiku"
    }
  ],
  "tasks": [
    {
      "name": "Task name",
      "status": "pending|in_progress|completed",
      "duration": "MM:SS or -"
    }
  ],
  "completed_phases": ["phase1", "phase2"],
  "logs": [
    {
      "time": "MM:SS",
      "message": "Log message",
      "level": "info|success|warning|error"
    }
  ]
}
```

### Resumability
If session is interrupted:
1. Jarvis state persists to disk
2. Output files are preserved
3. Next session reads state and continues from last checkpoint
4. WORKFLOW_WALKTHROUGH.md provides human-readable progress

---

## Feedback Loops

### Loop 1: Reviewer → Content
```
Content generated → Reviewer evaluates → Feedback provided → Content revised
```

### Loop 2: User → System
```
User reviews output → Provides feedback → System incorporates → Improved output
```

### Loop 3: Data → Insights → Actions
```
Customer data → Dashboard generated → Insights surfaced → Recommendations made
```

---

## Extensibility

### Adding a New Agent
1. Create `agents/{agent_name}.md` with:
   - Role definition
   - Core capabilities
   - Protocol/workflow
   - Output format
   - Model selection guidance

2. Register in Facilitator's routing logic

3. Add to Jarvis state tracking

### Adding a New Pipeline
1. Define input/output contract
2. Identify required agents
3. Document in this architecture file
4. Create reusable templates in `frameworks/`

### Adding a New Audience Variant
1. Add persona to `agents/deck_audience_variants.md`
2. Define messaging adjustments
3. System auto-generates variant when that persona is specified

---

## Quality Gates

| Gate | Trigger | Action |
|------|---------|--------|
| Research complete | All parallel agents done | Synthesize findings |
| Content ready | Deck/dashboard generated | Route to reviewer |
| Review passed | Score >= 7/10 | Approve for delivery |
| Review failed | Score < 7/10 | Iterate with feedback |
| User approval | Human review | Finalize or revise |

---

## Future Enhancements

### Planned
- [ ] MCP integrations (Google Slides, Notion, Salesforce)
- [ ] Automated competitive monitoring
- [ ] A/B testing of deck variants
- [ ] Integration with CRM for lead scoring

### Possible
- [ ] Voice-activated Jarvis interface
- [ ] Slack/Teams notifications
- [ ] Automated follow-up email generation
- [ ] Meeting prep assistant

---

## Key Takeaways

1. **System > Tasks**: Every component is reusable and composable
2. **Parallel when possible**: Research agents run simultaneously
3. **Quality gates enforced**: Reviewer before ship
4. **State preserved**: Resumable, traceable, auditable
5. **Cost-conscious**: Model selection based on task complexity
6. **Audience-aware**: Same content, different framing for different stakeholders

---

*This architecture document is part of the Mill AI Workflow System demonstration.*
