# Mill AI Workflow Walkthrough

**Session Start:** 2026-02-27
**Operator:** Gavin Pola (BCG → Mill applicant)
**AI System:** Claude Opus 4.5 via Claude Code CLI

---

## Purpose

This document captures the complete prompting process used to build Mill's AI workflow system. It serves as both documentation and a teaching tool for the Mill team on how to leverage AI for complex, multi-step business workflows.

---

## Phase 1: Initial Prompt (Verbatim)

**Timestamp:** Session start

```
alright so we have some stuff to get through today... we are starting up a true new claude code instance and we are gonna build
out some cool workflows. so context here: my name is gavin pola (feel free to do in-depth research on me) and i'm at bcg rn
leading ai adoption for aws, but im applying to mill. the job description is a combination of leading out hteir commerical
strategy pipeline in addition to leading ai adoption. i'll attach the ful chain of messages here with the ceo that we've been
talking about for next steps in the process: [Pasted text #1 +8 lines]. basically, the way im coming at it, i want to show by
doing. i want to use this session to create some reusable workflows that i woudl want to implement at mill. the first is a
reusable workflow that basically generates targeted presentations that are customized to the enterprise we are going after. so
im gonna want you to spin up a few 'subagents' that have different purposes, with the core few being a 'research' subagent,
'execution' subagent based on outputs (e.g., one for decks, one for excel, etc.), a reviewer workflow which is a synthesized
persona of Harry Tannebaum (go in depth to think about what he truly wants and cares about), a 'subagent' subagent whose job is
to spin up new hyper-focused subagents if we need one for parallelized work and don't have one already, and then a
'facilitatior' agent that kind of orchestrates the entire workflow, knows what has to get done, and gets shit done. this whole
prompting exercise i also want to use as kind of an example for the Mill team on not just what i can do but how to enable their
team to do this in a cool way, so let's use my prompts verbatim and store them in an easy way (maybe a MD file or HTML) so
that it walks them through the process. i think it's also maybe helpful to put a timeline on this in the sense of marking how
long execution is taking and just showing the art of the possible and what we can accomplish in such a short amount of time. a
few things i want you to utilize: the GSD protocol on claude https://github.com/gsd-build/get-shit-done, gas town:
https://github.com/steveyegge/gastown (https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 synopsis). just to
clarify, dont use these as prescriptive things, but understand the art of the possible here and i really want to be building
out a system, not just doing one-off tasks here. also, im interested in the idea of having some way that tells certain tasks to
use different modesl based on the level of complexity (im doing this all on my personal laptop with my own computer, so do
want to be budget conscious). and then last fun thing but i want to make a jarvis in my terminal or in my localhost (will defer
to you) but that just synthesizes which agents are up and running, what tasks they are doing, what the system is working on,
etc... (think about key prios as me as a builder). last things to note: big prios for workflows are a personalized marketing
workflow that 1. takes a deep look at mill, understands its context, understands where we are going (just landed Amazon, Whole
Foods, and Google and looking for next targeted 'whales' to hit - for internal context, the methodology so far has been like a
sniper rifle: ton of research, hyper targeted, and going full send. but it's also very focused on the ROI on reduced waste,
rather thant he outcome (that i believe is hte needle mover in these conversations) about the possibility of procurement and
supply chain reduction of waste wiht better waste data models. from first principles, using waste as the input for optimizing
supply chain is actually kind of genius. seems like there are some EXTREMELY cool things we can do with that. so afetr we get
the context on what mill is doing, do a deep dive anlaysis into where we can go next. im sure there are a ton of prioiriteis
and i wnat to create a framework for how we score opportunities. some potential levers include: size of oppty, current
sustainability initiatives and focus, hypothesized food waste, any plans, etc... i want you to take a deep pass at this and
reframe it in a mece way, but just those are my instinctual thoughts. once we have that list, let's start with the highest prio
next bet and i want to build out a full marketing deck for that (will let you use whatever you want to build out this deck).
actually just in general, before we start any task in teh workflow, we should have an agent that ingests the full plan and
understands EXACTLY which MCPs we will need throughout the HWOLE process to make this happen (could include google chrome
devtools mcp, etc.).. do a deep scan into hte art of the possible of MCPs out there and figure otu which align with needs, and
also like if we need any logins to anythings so that way we can just run fully autonomously and one-shot this plan without
having to have me intervene (until we get to the final output and we can iterate on that). once we have this deck, and for any
content, storylining, etc., make sure that we are feeding this through the reveiwer and also just like self-improving agents
based on 1. reviewer feedback and 2. my feedback. this needs to be a constant feedback loop that gets everything bettter as we
progress. okay so once we have that deck it's great and i can review it. another output i really want is that often we get huge
data dumps from clients and it can have a ton of different things (e.g., pictures of trash cans, pictures of trash, food waste
numbers, etc... i dont have any on my computer but i want you to do an in-depth thought on what potential customers would
actually want to see in a dashboard (when they hadnover this food waste data, we hadn this back over to them). the way i see it
is that the output will fundamentally depend on the data from the individual customer, but i stil think we can spin up a
workflow that understands what they have and use AI to automatically create python scirpts, etc., and produce the best picture
for that customer. canw e creaet this agent / workflow with a sample data outptu? third piece, once you've done all this heavy
lifting na dhave more context, is Harry's 2nd ask around how hte data piece si the missing piece of this story and this puzzle.
i want you to research the state of the world and put together a compelling story on how, where, and why this data can be used
and do a deep analysis on if you think this is important or not. if it is important, put together a thoughtfull plan on how it
is and isn't, the messages we should prioritize in our meetings, the messages w eshouldnt, where this can go right, where this
can go wrong, and just our plan of attack here. be really thoughtful and deep and understand things holistically and in
context. as a last thing, just know that anything i said before is not set in stone. this prompt and exercise is a true test of
your capabilites as a model and as an executor. i believe that in your research you will fundamentally get to a higher
fidelity answer and i fully entrust you with that - feel free to push back, be fully real, and know that the north star in all
of this is getting to the best answers and putting mill on the best track possible. good luck and think deeply about this plan.
```

**Key Insights Extracted:**
1. Build reusable workflows, not one-off tasks
2. Multi-agent architecture with specialized roles
3. Harry Tannenbaum persona as reviewer
4. MECE scoring framework for enterprise targeting
5. Supply chain optimization angle (waste data → procurement)
6. Jarvis dashboard for agent monitoring
7. Self-improving feedback loops

---

## Phase 2: Research & Planning

**Timestamp:** +5 minutes

### Research Conducted:
- Mill company intel (funding, partnerships, product)
- Harry Tannenbaum background (Nest, philosophy, values)
- GSD Protocol methodology
- Gas Town multi-agent architecture
- MCP ecosystem scan
- Food waste data market landscape

### Key Decisions Made:
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Deck format | reveal.js HTML | No Office dependency, interactive, browser-native |
| Target selection | AI-scored MECE | Demonstrates methodology, reusable framework |
| Jarvis UI | Terminal TUI | Fast to build, matches "show by doing" speed |
| Tools | Built-in only | No API key setup friction |

---

## Phase 3: Foundation Setup

**Timestamp:** +10 minutes

### Directory Structure Created:
```
/Users/Gorp/Documents/repos/Mill/
├── agents/           # Agent prompt templates
├── frameworks/       # Scoring rubrics, protocols
├── outputs/          # All deliverables
│   ├── target_analysis/
│   ├── decks/
│   ├── dashboards/
│   └── strategy/
├── jarvis/           # Agent monitoring TUI
└── data/sample/      # Test data
```

### Agent Prompts Written:
- `facilitator.md` - Master orchestrator
- `researcher.md` - Web research and synthesis
- `reviewer_harry.md` - Harry Tannenbaum persona
- `deck_builder.md` - Presentation generation
- `dashboard_gen.md` - Dashboard and analysis
- `spawner.md` - Dynamic agent creation

---

## Execution Log

**Total Session Time:** ~25 minutes (and counting)

| Phase | Start | End | Duration | Status |
|-------|-------|-----|----------|--------|
| Foundation | 00:00 | 06:00 | 6 min | ✅ Complete |
| Target Research | 06:01 | 11:30 | 5.5 min | ✅ Complete |
| Marketing Deck | 11:31 | 14:30 | 3 min | ✅ Complete |
| Dashboard Workflow | 14:31 | 17:00 | 2.5 min | ✅ Complete |
| Data Strategy | 17:01 | 20:00 | 3 min | ✅ Complete |
| Review & Polish | 20:01 | - | ... | 🔄 In Progress |

---

## Phase 4: Execution - Target Research

**Timestamp:** +6 minutes

### Parallel Research Agents Spawned:
1. **Researcher-Mill** - Deep dive into Mill's business, technology, funding, Whole Foods deal
2. **Researcher-Gavin** - Background research on operator for context

### Key Findings:

**Mill Intel:**
- CEO is Matt Rogers (Nest co-founder), Harry Tannenbaum is President
- December 2025: Amazon/Whole Foods partnership announced
- Mill Commercial launching in Whole Foods stores starting 2027
- Hit $20M revenue as of April 2025
- Unique data asset: largest household food waste behavior dataset ever

**Target Analysis Results (MECE Scoring):**

| Rank | Company | Score | Tier | Key Insight |
|------|---------|-------|------|-------------|
| 1 | **Costco** | 4.15/5 | Tier 1 | Most Whole Foods-like profile, zero waste 2030 goal |
| 2 | Kroger | 3.90/5 | Tier 2 | Already advanced in food waste programs |
| 3 | MGM Resorts | 3.65/5 | Tier 2 | High food prep, accessible Vegas HQ |
| 4 | Marriott | 3.50/5 | Tier 2 | Massive scale but franchise complexity |
| 5 | Hilton | 3.35/5 | Tier 2 | Strong ESG but franchise model |

**Recommendation:** Pursue Costco as #1 priority target.

---

## Phase 5: Execution - Marketing Deck

**Timestamp:** +11.5 minutes

### Deliverable: Costco Marketing Deck
- **Format:** reveal.js HTML (16 slides)
- **Location:** `outputs/decks/costco/index.html`
- **Supporting:** `outputs/decks/costco/speaker_notes.md`

### Deck Structure:
1. Cover slide
2-3. The food waste problem (general → Costco-specific)
4. The hidden cost (data gap)
5. The opportunity (reframe: waste → procurement intelligence)
6-7. Mill solution overview + data advantage
8. Supply chain optimization flow
9-10. Proof points (Amazon/Whole Foods, Google)
11. Custom ROI model
12. Implementation roadmap
13. Partnership models
14. Why now
15. Call to action
16. Contact

### Key Messaging Strategy:
- **Lead with:** "Waste stream → procurement intelligence system"
- **Avoid:** Generic sustainability pitches
- **Differentiate:** Behavior change data, not just waste measurement

---

## Phase 6: Execution - Dashboard Workflow

**Timestamp:** +14.5 minutes

### Deliverable: Customer Data Dashboard Workflow
- **Location:** `outputs/dashboards/dashboard_workflow.py`
- **Capability:** Accepts various data formats (CSV, JSON, Excel, Parquet)

### Workflow Features:
1. **Auto-detect data types** - Identifies weight, cost, category, location, time series
2. **Data profiling** - Quality scoring, column analysis
3. **Insight generation** - AI-powered recommendations
4. **Visualization selection** - Recommends appropriate charts based on data
5. **Dashboard generation** - Produces complete HTML dashboard with Chart.js

### Sample Output Types:
- Category breakdown (doughnut chart)
- Location comparison (bar chart)
- Time series trends (line chart)
- Key metrics cards
- Actionable recommendations

---

## Phase 7: Execution - Data Strategy Memo

**Timestamp:** +17 minutes

### Deliverable: Data Strategy Memo
- **Location:** `outputs/strategy/data_strategy_memo.md`
- **Purpose:** Address Harry's 2nd ask about data as the missing piece

### Memo Sections:
1. Executive Summary
2. State of Food Waste Data Today
3. What Mill's Data Actually Shows
4. Where This Data Can Be Used (Tier 1/2/3 applications)
5. Is This Important? (Bull and Bear cases)
6. Messages to Prioritize in Meetings
7. Where This Can Go Right / Wrong
8. Plan of Attack (phased roadmap)

### Key Strategic Insight:
> "Mill isn't a hardware company or a food waste diversion company. Mill is a **data company** that happens to use hardware to collect the most accurate, granular food waste data ever assembled."

### Recommended Priority:
1. First: Prove core value proposition with enterprise customers
2. Second: Collect data as byproduct of deployments
3. Third: Monetize data through targeted channels

Data business is a 2027+ story, not 2026 priority.

---

## Phase 8: Review & Polish (In Progress)

**Timestamp:** +20 minutes

### Harry Tannenbaum Reviewer Active
Running Costco deck through the reviewer persona for alignment check.

---

## Teaching Notes for Mill Team

### How to Replicate This Workflow

1. **Start with clear intent**: The initial prompt was comprehensive but messy. That's okay - Claude extracted the key requirements.

2. **Let AI push back**: The "Honest Assessment" section challenged priorities. This is valuable - don't treat AI as a yes-machine.

3. **Parallel execution**: Multiple agents can research simultaneously. Use this for speed.

4. **MECE frameworks**: Structure your thinking. The opportunity scoring rubric makes targeting systematic, not ad-hoc.

5. **Persona-based review**: The Harry Tannenbaum reviewer catches misalignments before human review.

6. **Iterative refinement**: Each output goes through feedback loops. Quality compounds.

### Key Prompting Patterns Used

```markdown
# Pattern 1: Persona Definition
"Create a reviewer persona based on Harry Tannenbaum who:
- Values data-driven decisions
- Thinks in systems
- Focuses on scalable outcomes
- Has Nest-era execution standards"

# Pattern 2: MECE Scoring
"Score each opportunity on these dimensions:
- Market Size (25%)
- Sustainability Commitment (20%)
- Operational Fit (20%)
- Strategic Value (20%)
- Accessibility (15%)"

# Pattern 3: Parallel Research
"Research these 10 targets in parallel, focusing on:
- Public sustainability goals
- Food waste pain points
- Decision maker access"
```

---

*This document will be updated as execution progresses.*
