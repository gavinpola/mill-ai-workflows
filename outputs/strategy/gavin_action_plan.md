# Mill Strategic Roadmap
## From Hardware to $10B Data Intelligence Platform

**Status:** Living Document | **Last Updated:** 2026-03-06 | **Prepared for:** Harry & Leadership Team

---

## Executive Summary

Mill is transforming from a hardware company into an autonomous data intelligence platform. This roadmap outlines the strategic path from our current state—**in active targeting with 0 deployed customers**—to a $10B food intelligence platform.

### Current State (Honest Assessment)

| Dimension | Where We Are |
|-----------|--------------|
| **Customers** | Targeting phase. Costco is #1 priority (scored 4.15/5.0). Whole Foods is a partnership/proof point opportunity, not a paying customer yet. |
| **Sales Infrastructure** | Pipeline exists with 500+ targets identified. MECE scoring framework operational (5 dimensions, 10-company analysis complete). |
| **Pitch Materials** | Costco deck suite complete (5 versions + 3 audience variants for CFO, Procurement, Sustainability). |
| **Hardware** | Core components selected (Basler ace2, RealSense D455, Jetson Orin NX). BOM estimated at $2,000-3,500/unit. Prototype not yet built. |
| **ML Model** | 30 food categories defined. No trained model yet. Path to 92% accuracy documented. |
| **AI Operations** | 6-agent system built (Facilitator, Researcher, DeckBuilder, DashboardGen, Reviewer, Spawner). Team adoption in early stages. |
| **Completed Tasks** | 7 of 220 tasks (3%). We're at the starting line. |

### The Core Thesis

**Turn food waste data into autonomous procurement decisions.**

This isn't about selling bins. It's about owning the most valuable food waste dataset on Earth and using it to fundamentally change how the food industry manages inventory, procurement, and sustainability.

### The Five Strategic Pillars

| Pillar | Mission | Why It Matters |
|--------|---------|----------------|
| **Commercial Autonomy** | Harry doesn't need to be on every call | Founders shouldn't scale through heroics. Repeatable systems = $10M to $10B. |
| **AI Leverage** | Every person becomes 10x | 10 people at 10x > 100 people at 1x. AI is the multiplier. |
| **Data Precision** | The best food waste data on Earth | 92% accuracy with 500K images = the most valuable food dataset on Earth. |
| **Outcome Delivery** | Prove ROI or don't charge | Outcome-based pricing flips risk. CFOs love verified ROI. |
| **Scale Effects** | Data that changes the food system | Network effects create winner-take-all. Every customer makes data more valuable. |

### Critical Dependencies (What Blocks What)

```
Commercial success depends on → Data Precision (need 85%+ accuracy for credible ROI)
Outcome Delivery depends on → Data Precision (accurate data for cost calculations)
Scale Effects depends on → Outcome Delivery (need ROI proof to attract customers)
All pillars accelerated by → AI Leverage (workflows multiply team capacity)
```

---

## Realistic Timeline Expectations

Based on industry research, here's what these major milestones actually take:

| Milestone | Optimistic Estimate | Realistic Range | Why |
|-----------|---------------------|-----------------|-----|
| Hardware prototype → 10 beta units | 3 months | **9-14 months** | Manufacturing sourcing, iteration cycles, supply chain delays |
| ML model 80% → 92% accuracy | 2 months | **6-8 months** | Training data acquisition, labeling, iterative improvement |
| 500K labeled images | 3 months | **4-5 months + $50-250K** | Human labeling at scale is expensive and slow |
| First enterprise sale (Costco tier) | 3 months | **10-14 months** | Enterprise sales cycles with pilots, legal, procurement |
| 50% team AI tool adoption | 2 weeks | **4-6 months** | Behavior change is hard; requires sustained effort |
| Industry report ("State of Food Waste") | 2 months | **5-8 months** | Data collection, analysis, design, distribution |

**Bottom line:** We're playing a 12-24 month game, not a 3-month sprint.

---

## Priority Framework

We've recalibrated priorities to be realistic about what truly blocks progress:

| Priority | Meaning | Target Count |
|----------|---------|--------------|
| **P0** | Blocks other critical work or is revenue-critical | ~25 tasks |
| **P1** | Important for this quarter but not blocking | ~60 tasks |
| **P2** | Nice to have this quarter | ~80 tasks |
| **P3** | Future consideration | ~55 tasks |

**Previous state:** 76 P0 tasks (34% of all tasks). That's not prioritization—that's panic.
**New state:** ~25 P0 tasks focused on genuine blockers.

---

## Commercial Autonomy

### Why This Pillar Matters

Harry cannot be on every sales call if Mill is going to be a $10B company. The goal isn't to make Harry redundant—it's to build systems that allow others to carry the Mill story with the same conviction and effectiveness. Every successful enterprise company has figured this out. It's time for Mill to do the same.

### What Already Exists

- **Costco deck suite**: 5 versions + 3 audience-specific variants (CFO, Procurement, Sustainability)
- **MECE scoring framework**: 5 dimensions, 10-company detailed analysis complete
- **Target pipeline**: 500+ companies identified in database
- **Outcome-based pricing model**: Core model defined and documented

### Subgoal: Repeatable Pitch System

#### c-p-1: Create base pitch deck template ✓ COMPLETED
Already done. Costco deck suite serves as the foundation.

#### c-p-2: Build audience variant decks ✓ COMPLETED
Already done. We have CFO, Procurement, and Sustainability variants.

#### c-p-3: Document Mill Story in 3/30/180 formats

**What:** Create three versions of the Mill story—a 3-second tagline, a 30-second elevator pitch, and a 180-second full narrative. These become the canonical versions that everyone uses.

**Why:** Consistent messaging matters. When different team members tell different stories, it signals chaos. When everyone tells the same story with conviction, it signals a company that knows what it's doing.

**Builds On:** Costco deck narrative work

**Timeline:** 1 week to draft, 1 week to refine with feedback

**Success Metric:** All customer-facing team members can deliver all three versions without notes

**Priority:** P0 | **Effort:** Low | **Impact:** High

#### c-p-4: Create objection handling playbook (living system)

**What:** Not a static 20-objection document, but a living CRM field that tracks:
- Actual objections heard on calls (logged by rep)
- Response variants attempted
- Outcome of each response (objection overcome Y/N)
- Quarterly refresh based on what's actually working

**Why:** Objections evolve. "We're already using Leanpath" is different from "We don't have budget." A static playbook gets stale; a living system gets smarter.

**Builds On:** Call recordings, CRM infrastructure

**Timeline:** 2 weeks for initial playbook, then ongoing refinement

**Success Metric:** 80%+ of common objections have documented responses with >50% success rate

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-p-5: Build competitive battlecards (Leanpath, Winnow)

**What:** One-page comparison docs for each major competitor showing: their positioning, their weaknesses, Mill's differentiation, specific proof points to cite, and responses to "why not them?"

**Why:** Reps need quick reference material when competitors come up. This isn't about bashing competitors—it's about confidently articulating why Mill is different.

**Builds On:** Competitive research already conducted

**Timeline:** 1 week per competitor

**Success Metric:** Used in 3+ competitive deals

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### c-p-6: Record practice pitch videos

**What:** Record Harry delivering the full pitch, then have team members record their own versions for feedback. Build a library of "what good looks like."

**Why:** Watching yourself pitch is uncomfortable and incredibly effective. Comparing your pitch to Harry's highlights the gaps.

**Builds On:** Mill Story documentation

**Timeline:** 2 weeks

**Success Metric:** Each sales team member has recorded at least one practice pitch

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### c-p-7: Set up live demo environment

**What:** A working demo environment that shows: live bin camera feed (simulated or real), classification in action, dashboard with waste data, and ROI calculations.

**Why:** "Show don't tell" is 10x more effective than slides. A working demo turns skeptics into believers.

**Builds On:** Prototype hardware, dashboard MVP

**Timeline:** Depends on hardware prototype (parallel track)

**Success Metric:** Demo used in 5+ customer meetings

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-p-8: Create pricing presentation

**What:** A clear presentation explaining Mill's pricing model—especially the outcome-based component. Includes comparison to traditional software pricing and worked examples.

**Why:** Outcome-based pricing is novel. Customers need to understand how it works to say yes to it.

**Builds On:** Outcome-based pricing model (completed)

**Timeline:** 1 week

**Success Metric:** Customers understand pricing on first explanation

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### c-p-9: Create pitch pattern analysis system

**What:** Track all customer interactions (calls, emails, meetings) and tag them with: pitch approach used, customer segment, objections raised, outcome. Use this data to identify which patterns lead to wins.

**Why:** "Document successful pitch patterns" is vague. What we need is a system that continuously learns what works. This is how you go from tribal knowledge to scalable playbooks.

**Builds On:** CRM, call recording tools

**Timeline:** 2 weeks to set up tracking, then ongoing

**Success Metric:** Can answer "what's our best-performing pitch approach for grocery?" with data

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### c-p-10: Train team member #1 to pitch independently

**What:** Structured training program: watch Harry pitch 3x, shadow 3 calls, co-pitch 3 calls, solo pitch with Harry on mute, then fully independent. Document what was learned at each stage.

**Why:** You can't scale what lives only in the founder's head. Training the first person proves the model works.

**Builds On:** Mill Story documentation, practice pitch videos

**Timeline:** 4-6 weeks of dedicated focus

**Success Metric:** Team member closes (or advances) a deal without Harry present

**Priority:** P1 | **Effort:** High | **Impact:** High

#### c-p-11: Train team member #2 to pitch independently

**What:** Same program as #1, but now the first trained person helps train the second. Tests whether the training process itself is repeatable.

**Why:** If only Harry can train people, it still doesn't scale. The training program needs to be teachable.

**Builds On:** Team member #1 training

**Timeline:** 4-6 weeks

**Success Metric:** Second team member can pitch independently AND helped train

**Priority:** P2 | **Effort:** High | **Impact:** High

#### c-p-12: WIN: First solo pitch (no Harry)

**What:** A team member conducts a full customer pitch—from intro to close—without Harry present. Harry reviews the recording afterward.

**Why:** This is the proof point that Commercial Autonomy is working. It's not about the outcome; it's about proving the capability exists.

**Builds On:** All pitch system work

**Timeline:** 8-12 weeks from training start

**Success Metric:** Pitch completed; customer advances in pipeline OR provides constructive feedback

**Priority:** P0 (milestone) | **Effort:** Low | **Impact:** High

---

### Subgoal: Pipeline Intelligence

#### c-pi-1: Refine and document ICP

**What:** Formalize the Ideal Customer Profile based on data from MECE scoring. Document: company size, industry vertical, sustainability commitments, procurement tech stack, decision-making process, and "ready to buy" signals.

**Why:** Focused outbound requires knowing exactly who you're targeting. This keeps the team from chasing bad-fit opportunities.

**Builds On:** MECE scoring framework (exists), 500+ target database

**Timeline:** 1 week

**Success Metric:** Team can filter pipeline to "ICP matches" and prioritize accordingly

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### c-pi-2: Add AI-powered scoring to existing pipeline

**What:** Our MECE scoring framework has identified 500+ targets. Layer on an AI system that:
- Dynamically re-ranks opportunities based on engagement signals (opened email, visited website, etc.)
- Allows natural language queries ("What's our best cruise line target?" or "Which companies have sustainability deadlines in 2025?")
- Learns from win/loss outcomes to refine scoring weights

**Why:** Removes guesswork from prioritization. Anyone on the team can make strategic targeting decisions without needing deep pipeline context. Transforms static list into living intelligence.

**Builds On:** MECE scoring framework, existing pipeline database

**Timeline:** 2-3 weeks for MVP, then ongoing refinement

**Success Metric:** Team uses AI query interface 3+ times/week; scoring accuracy improves measurably quarter-over-quarter

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-pi-3: Apply MECE scoring to all targets

**What:** Extend the detailed 10-company MECE analysis to all 500+ companies in the pipeline. Automate where possible; manual deep-dives for top 50.

**Why:** Scoring creates prioritization. Without it, we're guessing which opportunities to pursue.

**Builds On:** MECE framework (5 dimensions defined)

**Timeline:** 2 weeks with automation assistance

**Success Metric:** All pipeline companies have scores; top 50 have detailed analysis

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-pi-4: Deep research on top 50 targets

**What:** For the 50 highest-scoring opportunities, compile: decision-maker profiles, organizational structure, known initiatives, warm intro paths, recent news, and specific pain points we can address.

**Why:** Enterprise sales is relationship-driven. Deep knowledge of your targets converts cold outreach to warm conversations.

**Builds On:** MECE scoring results

**Timeline:** 2-3 weeks (1-2 hours per company with AI assistance)

**Success Metric:** Dossier created for each top 50 company

**Priority:** P1 | **Effort:** High | **Impact:** High

#### c-pi-5: Map warm intro paths for top 20

**What:** For top 20 targets, identify every possible warm introduction: investor connections, advisor networks, existing customer referrals, conference contacts, LinkedIn second-degree connections.

**Why:** Warm intros have 3-5x response rates vs. cold outreach. This is the highest-leverage prospecting activity.

**Builds On:** Top 50 deep research, network mapping

**Timeline:** 1 week focused effort

**Success Metric:** At least one warm path identified for 15+ of top 20

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-pi-6: Create segment-specific outreach sequences

**What:** Develop tailored email/call sequences for each vertical: grocery, hospitality, cruise lines, universities, healthcare. Each sequence addresses segment-specific pain points and uses segment-relevant case studies.

**Why:** Generic outreach performs worse than tailored messaging. "We help grocery stores reduce waste" beats "We help companies reduce waste."

**Builds On:** ICP documentation, vertical research

**Timeline:** 1 week per vertical

**Success Metric:** Each vertical has 5+ touch sequence with >20% response rate

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### c-pi-7: Implement CRM pipeline automation

**What:** Our CRM likely exists—what we need is automation: auto-tagging based on engagement, stage advancement triggers, task reminders, activity logging from email/calendar. Remove manual data entry.

**Why:** Reps should sell, not do data entry. Automation ensures nothing falls through cracks while reducing friction.

**Builds On:** Existing CRM infrastructure

**Timeline:** 2 weeks

**Success Metric:** Zero manual pipeline stage updates; all activity auto-logged

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### c-pi-8: Build real-time pipeline dashboard

**What:** Dashboard showing: pipeline by stage, velocity metrics, conversion rates by source, team activity, and forecasted close dates. Updated in real-time from CRM data.

**Why:** You can't improve what you can't see. Harry needs a single view of commercial progress.

**Builds On:** CRM data, dashboard generation workflow

**Timeline:** 1 week

**Success Metric:** Dashboard used in weekly pipeline reviews

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### c-pi-9: Establish weekly pipeline review cadence

**What:** Standing weekly meeting (30-60 min): review pipeline changes, discuss stuck deals, assign actions, forecast next week. Clear agenda, documented outcomes.

**Why:** Consistent rhythm drives accountability. Sales teams that review weekly outperform those that don't.

**Builds On:** Pipeline dashboard, CRM data

**Timeline:** This week (just schedule it)

**Success Metric:** 4 consecutive weeks held without cancellation

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### c-pi-10: Create inbound qualification checklist

**What:** Scoring criteria for inbound leads: company fit (ICP match), timing fit (budget cycle, active project), contact fit (decision-making authority). Automated where possible.

**Why:** Not all inbound leads deserve time. Quick qualification prevents reps from wasting effort on bad fits.

**Builds On:** ICP documentation

**Timeline:** 3 days

**Success Metric:** All inbound leads scored within 24 hours of receipt

**Priority:** P2 | **Effort:** Low | **Impact:** Low

---

### Subgoal: Proof Arsenal

#### c-pr-1: Document Whole Foods engagement timeline

**What:** Create comprehensive timeline of Whole Foods engagement: initial contact, meetings, pilot scope, what was deployed, what was measured, outcomes observed. This becomes the foundation for case study materials.

**Why:** Whole Foods is our proof point. We need to be able to tell this story precisely and consistently.

**Builds On:** Existing Whole Foods relationship

**Timeline:** 1 week

**Success Metric:** Complete timeline with dates, contacts, and key milestones documented

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### c-pr-2: Calculate and verify Whole Foods ROI

**What:** Work with Whole Foods contacts to calculate verified ROI: baseline waste cost, waste reduction observed, dollar savings, payback period. Get their sign-off on the numbers.

**Why:** Customer-verified ROI is 10x more credible than our own projections. This is the proof that unlocks Costco and similar accounts.

**Builds On:** Whole Foods data, baseline methodology

**Timeline:** 2-3 weeks (requires customer collaboration)

**Success Metric:** ROI statement that Whole Foods agrees can be shared publicly

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### c-pr-3: Secure testimonial quote from Whole Foods

**What:** Get a quotable testimonial from a Whole Foods decision-maker. Ideally someone with title credibility (Director+). Document approval for use in sales materials.

**Why:** Third-party validation beats self-promotion. A quote from Whole Foods opens doors.

**Builds On:** Whole Foods relationship, ROI calculation

**Timeline:** 1-2 weeks

**Success Metric:** Written quote with attribution approval

**Priority:** P0 | **Effort:** Low | **Impact:** High

#### c-pr-4: Create PDF case study (2-pager)

**What:** Designed 2-page PDF: company background, challenge, solution (Mill), results, testimonial quote. Professional design, scannable format, sharable via email.

**Why:** Sales reps need leave-behinds. A polished case study does selling when you're not in the room.

**Builds On:** Whole Foods timeline, ROI, testimonial

**Timeline:** 1 week after inputs ready

**Success Metric:** Used in 10+ prospect interactions

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-pr-5: Create video case study (90 seconds)

**What:** Short video with b-roll of bin in action, talking head from Whole Foods contact (or voiceover with their approval), key stats animated on screen.

**Why:** Video is higher engagement than PDF. Useful for website, social, and email marketing.

**Builds On:** PDF case study content

**Timeline:** 2-3 weeks (production time)

**Success Metric:** 1000+ views across channels

**Priority:** P2 | **Effort:** High | **Impact:** Medium

#### c-pr-6: Document second enterprise case study

**What:** Replicate Whole Foods process with second customer: timeline, ROI, testimonial, PDF, video.

**Why:** One case study is an anecdote. Two case studies start to show a pattern. Three is a trend.

**Builds On:** Whole Foods case study process

**Timeline:** Depends on second customer deployment

**Success Metric:** Complete case study package for customer #2

**Priority:** P1 | **Effort:** High | **Impact:** High

#### c-pr-7: Document third enterprise case study

**What:** Third case study, ideally in a different vertical (if WF is grocery, make this hospitality or cruise).

**Why:** Vertical diversity shows Mill works across industries, not just one niche.

**Builds On:** Case study process

**Timeline:** Depends on customer #3 deployment

**Success Metric:** Complete case study in different vertical

**Priority:** P2 | **Effort:** High | **Impact:** Medium

#### c-pr-8: Build interactive ROI calculator

**What:** Web-based tool where prospects input: waste volume, food cost, labor cost. Calculator outputs: projected savings with Mill, payback period, sustainability metrics.

**Why:** Self-service ROI is powerful. Prospects convince themselves when they see their own numbers.

**Builds On:** ROI methodology from Whole Foods

**Timeline:** 2 weeks to build

**Success Metric:** 50+ prospects use calculator; leads from calculator convert at higher rate

**Priority:** P1 | **Effort:** High | **Impact:** High

#### c-pr-9: Create CFO-specific proof deck

**What:** A version of the pitch deck optimized for CFOs: less vision, more numbers. Unit economics, ROI calculations, payback periods, risk mitigation, contract structure.

**Why:** CFOs are the ultimate decision-makers on spend. They care about different things than operators.

**Builds On:** Costco deck suite, CFO audience variant

**Timeline:** Already partially done with CFO variant. Enhance with ROI calculator outputs.

**Success Metric:** CFO-approved budget allocation in 3+ deals

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-pr-10: Pursue third-party validation

**What:** Submit Mill for industry awards, seek analyst coverage (Gartner, Forrester), pursue sustainability certifications. Create external validation beyond customer testimonials.

**Why:** Third-party validation reduces perceived risk. "Gartner recognized" or "GreenBiz award winner" adds credibility.

**Builds On:** Case studies, ROI proof

**Timeline:** 3-6 months (award cycles vary)

**Success Metric:** At least one meaningful third-party recognition

**Priority:** P2 | **Effort:** Medium | **Impact:** High

---

### Subgoal: Outcome-Based Pricing

#### c-o-1: Define outcome-based pricing model ✓ COMPLETED
Core model defined. Pricing tied to verified waste reduction and cost savings.

#### c-o-2: Create baseline methodology documentation

**What:** Document exactly how we establish baseline: what data we collect, over what period, how we handle seasonality, what counts as "Mill-attributed" savings vs. other factors.

**Why:** Outcome pricing requires bulletproof methodology. If customers or their CFOs question the numbers, we need a defensible process.

**Builds On:** Outcome-based pricing model

**Timeline:** 2 weeks

**Success Metric:** Methodology reviewed and approved by finance/legal advisor

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### c-o-3: Draft outcome-based contract template

**What:** Legal contract template for outcome-based pricing: baseline period, measurement methodology, verification process, fee structure, audit rights, dispute resolution.

**Why:** Novel pricing models need novel contracts. Get this right once, then reuse.

**Builds On:** Pricing model, baseline methodology

**Timeline:** 2-3 weeks (legal review)

**Success Metric:** Contract signed by first outcome-based customer

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### c-o-4: Identify 3 pilot customers for outcome pricing

**What:** Find 3 customers willing to pilot outcome-based pricing. Ideal: different sizes, different verticals, willing to share learnings.

**Why:** Pilots test the model before broad rollout. Three gives enough data to refine.

**Builds On:** Pipeline prioritization

**Timeline:** Depends on sales cycle (3-6 months realistic)

**Success Metric:** 3 signed pilot agreements

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-o-5: Deploy 60-day baseline measurement at pilots

**What:** Install bins at pilot sites and collect 60 days of baseline data before "turning on" Mill recommendations. This establishes pre-Mill waste levels.

**Why:** You can't prove savings without a baseline. 60 days accounts for variability.

**Builds On:** Pilot customer agreements, hardware deployment

**Timeline:** 60 days after deployment (non-compressible)

**Success Metric:** Complete baseline data for all pilot sites

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### c-o-6: Build attribution dashboard

**What:** Dashboard showing: baseline waste, current waste, calculated savings, attribution breakdown (what Mill vs. other factors), running savings total, projected annual savings.

**Why:** Transparency builds trust. Customers should see exactly how savings are calculated.

**Builds On:** Measurement infrastructure, dashboard MVP

**Timeline:** 2-3 weeks

**Success Metric:** Dashboard reviewed and trusted by customer finance team

**Priority:** P1 | **Effort:** High | **Impact:** High

#### c-o-7: Calculate and verify savings at Pilot #1

**What:** After 90+ days (60 baseline + 30 measured), calculate savings at first pilot. Walk through methodology with customer. Get their agreement on the numbers.

**Why:** First verified savings becomes proof point for selling outcome pricing to others.

**Builds On:** Baseline data, measurement infrastructure

**Timeline:** 90+ days from deployment

**Success Metric:** Customer-verified savings statement

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-o-8: Calculate and verify savings at Pilot #2

**What:** Same process at second pilot site.

**Why:** Second data point confirms the model works across customers.

**Builds On:** Pilot #1 process

**Timeline:** Parallel with or after Pilot #1

**Success Metric:** Second customer-verified savings statement

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### c-o-9: Document learnings, refine pricing model

**What:** After pilots, document: what worked, what didn't, contract clauses that need revision, methodology refinements, pricing adjustments.

**Why:** Pilots are for learning. Capture those learnings before scaling.

**Builds On:** Pilot outcomes

**Timeline:** 2 weeks post-pilots

**Success Metric:** Updated pricing model and contracts based on real data

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### c-o-10: WIN: Roll out outcome pricing as default

**What:** Make outcome-based pricing the standard contract model for all new customers, not an experiment.

**Why:** This is the moment Mill's business model truly differentiates. Outcome pricing is the moat.

**Builds On:** Successful pilots, refined model

**Timeline:** 6-12 months from pilot start

**Success Metric:** 3+ new customers on outcome-based contracts

**Priority:** P2 | **Effort:** Medium | **Impact:** High

---

## AI Leverage

### Why This Pillar Matters

The best companies don't just hire more people—they multiply the people they have. Mill has roughly 10 people. With AI leverage, those 10 people can output what 100 people would produce traditionally. But this only works if the team actually adopts AI tools and workflows. Adoption is the hard part.

### What Already Exists

- **6-agent system**: Facilitator, Researcher, DeckBuilder, DashboardGen, Reviewer, Spawner
- **Deck generation workflow**: Used to create Costco deck variants
- **Prompt library foundation**: Key prompts documented in workflow guides

### Subgoal: Tool Access (Claude Code for All)

#### a-t-1: Research Anthropic enterprise pricing

**What:** Get pricing quotes for Claude enterprise (API access, team seats, Claude Code licenses). Understand tier options, volume discounts, and support levels.

**Why:** Can't budget without pricing. Need to know what we're committing to.

**Builds On:** Current individual usage patterns

**Timeline:** 1 week (reach out to Anthropic sales)

**Success Metric:** Written pricing proposal in hand

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-t-2: Build business case for enterprise license

**What:** Document ROI case for AI tool investment: current time spent on tasks AI could automate, projected time savings, value of those hours, payback period. Compare to license cost.

**Why:** Harry and Matt need numbers to approve budget. Make it easy to say yes.

**Builds On:** Anthropic pricing, usage research

**Timeline:** 1 week

**Success Metric:** Approved budget for AI tools

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-t-3: Get executive budget approval

**What:** Present business case to Harry and Matt. Get explicit budget approval for Anthropic contract and any supporting tools.

**Why:** No approval = no tools. This is a gate.

**Builds On:** Business case document

**Timeline:** 1 meeting

**Success Metric:** Written approval for AI tool budget

**Priority:** P0 | **Effort:** Low | **Impact:** High

#### a-t-4: Negotiate and sign Anthropic contract

**What:** Work with Anthropic to finalize contract terms: pricing, seat count, usage limits, support SLA, data handling terms.

**Why:** Get the contract done. This has been blocking broader rollout.

**Builds On:** Budget approval

**Timeline:** 2-4 weeks (legal review)

**Success Metric:** Signed contract with Anthropic

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-t-5: Set up team organization and seat allocation

**What:** Create Mill organization in Claude/API, allocate seats by team, set up billing, establish admin controls.

**Why:** Administrative setup before rollout ensures smooth onboarding.

**Builds On:** Signed contract

**Timeline:** 1-2 days after contract

**Success Metric:** All team members have access credentials

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-t-6: Create Getting Started onboarding guide

**What:** Step-by-step guide for new AI tool users: installation, first prompts, best practices, common use cases by role, links to workflow library.

**Why:** Reduces friction for adoption. People won't use tools they can't figure out.

**Builds On:** Existing workflow documentation

**Timeline:** 1 week

**Success Metric:** New users can get productive in <30 minutes using guide

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### a-t-7: Roll out to 5 power users first

**What:** Select 5 team members who are most likely to adopt and succeed with AI tools. Give them early access, collect detailed feedback, refine approach.

**Why:** Champions create culture change. Start with people who will evangelize to others.

**Builds On:** Tool access, onboarding guide

**Timeline:** 2 weeks of active use

**Success Metric:** 5 users actively using tools daily; qualitative feedback collected

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-t-8: Collect feedback and iterate onboarding

**What:** Interview power users: what's working, what's confusing, what workflows are most valuable, what documentation is missing. Update onboarding based on feedback.

**Why:** First version is never right. Iterate before broader rollout.

**Builds On:** Power user experience

**Timeline:** 1 week

**Success Metric:** Onboarding updated with at least 5 improvements from feedback

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-t-9: Roll out to full team

**What:** Extend AI tool access to all team members. Host onboarding session, distribute guide, set expectations for adoption.

**Why:** Power user success proves the model. Now scale it.

**Builds On:** Refined onboarding, power user champions

**Timeline:** 1 week for logistics, 4-6 weeks for adoption

**Success Metric:** 100% of team has access; 50%+ actively using within 6 weeks

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### a-t-10: Set up usage tracking and ROI measurement

**What:** Track AI tool usage: sessions per user, tasks completed, time saved (estimated), workflows used. Calculate ROI quarterly.

**Why:** What gets measured gets managed. Need to prove ongoing value.

**Builds On:** Full team rollout

**Timeline:** 1 week to set up, then ongoing

**Success Metric:** Quarterly ROI report showing positive return

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

---

### Subgoal: AI Day (Gavin Leads)

#### a-d-1: Set date and get leadership buy-in

**What:** Pick a date for AI Day (ideally 4-6 weeks out). Get Harry's commitment to attend and to mandate team attendance. Block calendars.

**Why:** If leadership doesn't show up and participate, the team won't take it seriously.

**Builds On:** AI tool budget approval

**Timeline:** This week

**Success Metric:** Date set, calendars blocked, Harry confirmed

**Priority:** P0 | **Effort:** Low | **Impact:** High

#### a-d-2: Define learning objectives

**What:** Specific, measurable objectives for AI Day: "By end of day, every participant will have: completed one AI-assisted task relevant to their role, saved one prompt to the shared library, identified one workflow to adopt weekly."

**Why:** Without objectives, it's just a workshop. With objectives, it's behavior change.

**Builds On:** Workflow library research

**Timeline:** 1 week

**Success Metric:** Written objectives approved by Harry

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-d-3: Create agenda (AM theory, PM hands-on)

**What:** Morning: why AI matters for Mill (Harry), how AI tools work (Gavin), live demos. Afternoon: hands-on exercises by team, build your first workflow, share results.

**Why:** Balance inspiration with practical skill-building. People learn by doing.

**Builds On:** Learning objectives

**Timeline:** 1 week

**Success Metric:** Agenda reviewed and approved

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-d-4: Design hands-on exercises for each team

**What:** Create role-specific exercises: Sales gets prospecting exercises, Ops gets process automation, Eng gets code review. Each exercise takes 30-45 minutes and produces a real output.

**Why:** Generic training doesn't stick. Role-specific training shows immediate relevance.

**Builds On:** Workflow library, team role analysis

**Timeline:** 2 weeks

**Success Metric:** Exercises tested with 1 person per role before AI Day

**Priority:** P0 | **Effort:** High | **Impact:** High

#### a-d-5: Prepare demo environments

**What:** Set up test accounts, sample data, and sandbox environments so exercises work smoothly. Test everything twice.

**Why:** Technical failures kill training momentum. Don't let setup problems derail the day.

**Builds On:** Tool access setup

**Timeline:** 1 week before AI Day

**Success Metric:** All exercises tested end-to-end; backup plans documented

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-d-6: Create pre-work materials

**What:** 10-minute video explaining what AI Day is, why it matters, what to expect. Short reading on AI basics. Survey asking what problems people want to solve with AI.

**Why:** Pre-work gets people thinking ahead, increases engagement, surfaces specific needs.

**Builds On:** Learning objectives

**Timeline:** Send 1 week before AI Day

**Success Metric:** 80%+ completion rate on pre-work

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-d-7: Send invites with hype communication

**What:** Calendar invites to all team members. Accompanying email from Harry explaining why this matters for Mill's future. Build anticipation.

**Why:** Buy-in starts before the day begins. Leadership communication signals importance.

**Builds On:** Date confirmation

**Timeline:** 2 weeks before AI Day

**Success Metric:** 100% acceptance rate on invites

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-d-8: RUN AI DAY

**What:** Execute the full-day training. Capture photos/videos. Document questions asked. Note what resonated and what fell flat. Celebrate wins.

**Why:** This is the moment. Make it count.

**Builds On:** All AI Day prep

**Timeline:** 1 day

**Success Metric:** 80%+ attendance; positive post-event feedback

**Priority:** P0 (milestone) | **Effort:** High | **Impact:** High

#### a-d-9: Collect feedback via survey

**What:** Same-day survey: what was valuable, what was confusing, what do you want more of, Net Promoter Score for the event.

**Why:** Real-time feedback is more honest than feedback collected later.

**Builds On:** AI Day execution

**Timeline:** Day of event

**Success Metric:** 80%+ response rate; NPS > 50

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-d-10: Create follow-up resources

**What:** Package AI Day materials into a resource hub: recorded demos, exercise templates, FAQ from questions asked, links to workflow library.

**Why:** Learning doesn't end at 5pm. Give people references for continued growth.

**Builds On:** AI Day content

**Timeline:** 1 week after AI Day

**Success Metric:** Resource hub published and linked from team wiki

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-d-11: Measure behavior change at 2 weeks

**What:** Survey team 2 weeks after AI Day: Are you using AI tools? Which workflows? How often? What's helped? What's blocking you?

**Why:** Training that doesn't change behavior is worthless. Measure the behavior, not just the reaction.

**Builds On:** AI Day training

**Timeline:** 2 weeks post-event

**Success Metric:** 50%+ of team reports using AI tools at least once per week

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### a-d-12: Plan quarterly AI refresher cadence

**What:** Schedule quarterly "AI Refresh" sessions: new features, advanced techniques, share success stories, address adoption challenges.

**Why:** Skills decay without reinforcement. Quarterly touchpoints maintain momentum.

**Builds On:** AI Day feedback

**Timeline:** After AI Day

**Success Metric:** First refresh scheduled; 80%+ attendance maintained

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

---

### Subgoal: AI Office Hours

#### a-o-1: Choose recurring time slot

**What:** Pick a weekly time for AI Office Hours. Ideally when most people are available, not competing with other standing meetings.

**Why:** Consistency beats sporadic availability. Same time every week creates habit.

**Builds On:** Team calendar review

**Timeline:** This week

**Success Metric:** Time slot selected and announced

**Priority:** P0 | **Effort:** Low | **Impact:** Medium

#### a-o-2: Create #ai-office-hours Slack channel

**What:** Dedicated Slack channel for AI questions, sharing wins, posting prompts. Gavin monitors and responds. Thread for each Office Hours session.

**Why:** Creates async support layer. Questions get answered even outside Office Hours.

**Builds On:** Slack workspace

**Timeline:** 10 minutes

**Success Metric:** Channel created, purpose pinned, team invited

**Priority:** P0 | **Effort:** Low | **Impact:** Medium

#### a-o-3: Send launch announcement

**What:** All-hands announcement about AI Office Hours: what it is, when it is, what kinds of questions to bring, first session date.

**Why:** People won't attend what they don't know about.

**Builds On:** Time slot, Slack channel

**Timeline:** 1 week before first session

**Success Metric:** 80%+ of team reads announcement

**Priority:** P0 | **Effort:** Low | **Impact:** Medium

#### a-o-4: Prepare 5 demo use cases

**What:** Five ready-to-go demos for first Office Hours: email drafting, research summarization, data analysis, content creation, code explanation. Each takes 5 minutes.

**Why:** First session sets expectations. Strong demos create "I want to try that" reactions.

**Builds On:** Workflow documentation

**Timeline:** 1 week

**Success Metric:** Demos tested and timed

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-o-5: Run first AI Office Hours session

**What:** Host first session: welcome, explain format, run demos, take live questions, solve real problems, celebrate wins.

**Why:** First session establishes the vibe. Make it welcoming and useful.

**Builds On:** All Office Hours prep

**Timeline:** Scheduled date

**Success Metric:** At least 5 attendees; at least 3 questions answered

**Priority:** P0 | **Effort:** Low | **Impact:** High

#### a-o-6: Document questions and build FAQ

**What:** After each Office Hours, document questions asked and answers given. Build growing FAQ for the team.

**Why:** Same questions get asked repeatedly. Documentation prevents repetition.

**Builds On:** Office Hours sessions

**Timeline:** Ongoing after each session

**Success Metric:** FAQ grows by 3+ entries per month

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-o-7: Maintain weekly cadence for 4 weeks

**What:** Run Office Hours every week for 4 consecutive weeks. Don't skip. Show up even if only 2 people attend.

**Why:** Consistency builds trust. If you skip weeks, people stop coming.

**Builds On:** First session success

**Timeline:** 4 weeks

**Success Metric:** 4 consecutive sessions held; average attendance increases

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### a-o-8: Identify and empower AI champions

**What:** Identify 2-3 team members who are becoming AI power users. Give them title ("AI Champion"), ask them to help onboard others, include them in planning.

**Why:** Peer influence > top-down mandates. Champions create grassroots adoption.

**Builds On:** Usage observation

**Timeline:** 4-6 weeks after rollout

**Success Metric:** 2+ AI Champions formally recognized and actively helping peers

**Priority:** P1 | **Effort:** Low | **Impact:** High

#### a-o-9: Transition to bi-weekly cadence

**What:** Once weekly attendance stabilizes and Slack support is handling simpler questions, reduce Office Hours to bi-weekly.

**Why:** Weekly was for building momentum. Bi-weekly is sustainable long-term.

**Builds On:** Established Office Hours culture

**Timeline:** After 8+ weekly sessions

**Success Metric:** Attendance per session maintained despite reduced frequency

**Priority:** P2 | **Effort:** Low | **Impact:** Low

---

### Subgoal: Workflow Library

#### a-w-1: Document deck generation workflow

**What:** Step-by-step guide for using AI to generate pitch decks: prompts, iteration techniques, customization for audience, quality checks. Include the workflow that created Costco variants.

**Why:** This workflow has proven ROI. Document it so anyone can replicate.

**Builds On:** Costco deck creation experience

**Timeline:** 1 week

**Success Metric:** Team member who wasn't involved can create deck variant using guide

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-w-2: Document prospect research workflow

**What:** How to use AI for deep prospect research: company analysis, decision-maker profiling, pain point identification, competitive context. Include prompt templates and quality checks.

**Why:** Research is high-value, time-intensive work. AI can cut research time by 70%+ when done right.

**Builds On:** Top 50 research experience

**Timeline:** 1 week

**Success Metric:** Research quality equivalent to manual at 30% of the time

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-w-3: Document dashboard generation workflow

**What:** How to use AI to generate dashboards: requirement gathering prompts, visualization suggestions, code generation, iteration patterns.

**Why:** Extends DashboardGen agent capabilities to more team members.

**Builds On:** DashboardGen agent experience

**Timeline:** 1 week

**Success Metric:** Non-technical team member can generate basic dashboard using guide

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-w-4: Document meeting notes workflow

**What:** How to use AI for meeting notes: recording transcription, summary generation, action item extraction, follow-up email drafting.

**Why:** Meetings happen constantly. AI-assisted notes save hours per week and improve follow-through.

**Builds On:** Common use case documentation

**Timeline:** 3 days

**Success Metric:** Meeting notes quality improves; time spent on notes decreases

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-w-5: Document email drafting workflow

**What:** Templates and techniques for AI-assisted emails: cold outreach, follow-ups, proposal responses, difficult conversations. Include tone adjustment techniques.

**Why:** Email is universal. Everyone writes emails. AI assistance saves time on every single one.

**Builds On:** Common use case documentation

**Timeline:** 3 days

**Success Metric:** Team reports faster email turnaround

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-w-6: Document competitive analysis workflow

**What:** How to use AI for competitive intelligence: company research, product comparison, positioning analysis, battlecard generation.

**Why:** Competitive info changes constantly. AI-assisted research keeps battlecards current.

**Builds On:** Battlecard creation, research workflow

**Timeline:** 1 week

**Success Metric:** Battlecards updated more frequently with less effort

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-w-7: Document code review workflow (engineering)

**What:** How to use AI for code review: context setting, review prompts, security scanning, refactoring suggestions. Engineering-specific.

**Why:** Engineering team can 10x review capacity with AI assistance.

**Builds On:** Engineering team input

**Timeline:** 1 week

**Success Metric:** Engineers report faster, more thorough code reviews

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### a-w-8: Create shared prompt library

**What:** Central repository of proven prompts: categorized by use case, tagged by role, with example outputs. Searchable. Anyone can contribute; quality controlled.

**Why:** Don't make people reinvent prompts. Share what works.

**Builds On:** All workflow documentation

**Timeline:** 1 week for initial library, then ongoing

**Success Metric:** 50+ prompts in library; used 10+ times per week across team

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### a-w-9: Build internal AI wiki/playbook

**What:** Comprehensive internal resource: all workflows, all prompts, best practices, FAQ, success stories, learning resources. One place for everything AI at Mill.

**Why:** Scattered documentation = no documentation. Centralize it.

**Builds On:** All workflow and prompt documentation

**Timeline:** 2 weeks for initial version

**Success Metric:** Wiki is first place team goes for AI questions

**Priority:** P1 | **Effort:** High | **Impact:** High

#### a-w-10: WIN: 50%+ team using AI tools weekly

**What:** Achieve sustained adoption where more than half the team uses AI tools at least once per week, measured over 4 consecutive weeks.

**Why:** This is the proof that AI Leverage is working. Culture has changed.

**Builds On:** All AI Leverage work

**Timeline:** 4-6 months from rollout start (be realistic—behavior change takes time)

**Success Metric:** Usage tracking shows 50%+ weekly active users for 4+ weeks

**Priority:** P1 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

#### a-w-11: Track time savings by workflow

**What:** Quantify time saved: for each workflow, estimate time-before-AI vs. time-with-AI. Calculate total hours saved per week/month across team.

**Why:** ROI proof for continued investment. Also identifies which workflows are most valuable.

**Builds On:** Usage tracking, workflow adoption

**Timeline:** Ongoing after adoption

**Success Metric:** Documented time savings of X hours per week (target TBD)

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### a-w-12: Publish Mill AI Playbook externally

**What:** Turn internal AI wiki into public thought leadership content: blog posts, LinkedIn articles, downloadable playbook. Positions Mill as AI-forward company.

**Why:** Recruiting leverage (attracts AI-curious talent), brand building (positions Mill as innovative), potential lead generation (companies interested in AI might be Mill customers).

**Builds On:** Internal AI wiki, proven workflows

**Timeline:** 3-6 months after internal playbook is mature

**Success Metric:** 5000+ views/downloads; 3+ recruiting mentions ("I saw your AI playbook")

**Priority:** P3 | **Effort:** High | **Impact:** Medium

---

### Subgoal: AI Steering Committee

#### a-s-1: Define committee members

**What:** Select 4-5 people for AI Steering Committee: cross-functional (sales, ops, eng, leadership), includes executive sponsor (Harry or Matt), includes Gavin as AI lead.

**Why:** Cross-functional committee ensures AI strategy serves whole company, not just one team.

**Builds On:** Organizational understanding

**Timeline:** 1 week

**Success Metric:** Committee roster confirmed with all members accepting

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-s-2: Create committee charter

**What:** Document purpose, scope, decision rights, meeting cadence, success metrics for the committee. What does the committee own? What does it NOT own?

**Why:** Clarity prevents scope creep and confusion about authority.

**Builds On:** Committee membership

**Timeline:** 1 week

**Success Metric:** Charter approved by executive sponsor

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### a-s-3: Schedule bi-weekly meetings

**What:** Standing bi-weekly meeting for committee: review AI initiatives, approve new projects, address blockers, allocate resources.

**Why:** Regular cadence prevents AI projects from languishing.

**Builds On:** Committee formation

**Timeline:** 1 day

**Success Metric:** First 4 meetings scheduled

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-s-4: Create prioritization framework

**What:** Framework for evaluating AI initiatives: impact (time saved), effort (development time), risk (data privacy, accuracy), alignment (strategic fit). Score and rank proposals.

**Why:** Can't do everything. Need principled way to say "yes" and "not now."

**Builds On:** Committee charter

**Timeline:** 1 meeting to develop

**Success Metric:** Framework used to prioritize first 5 proposals

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### a-s-5: Establish data privacy guidelines

**What:** Clear guidelines on what data can/cannot be used with AI tools: customer data handling, PII rules, third-party data, export controls. Get legal review.

**Why:** AI without privacy guidelines is a liability. Protect the company and customers.

**Builds On:** Legal/compliance input

**Timeline:** 2-3 weeks with legal review

**Success Metric:** Guidelines published and team trained

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### a-s-6: Run first committee meeting

**What:** First formal committee meeting: adopt charter, review prioritization framework, discuss initial AI initiatives, set expectations for cadence.

**Why:** First meeting sets the tone. Make it productive and action-oriented.

**Builds On:** Charter, framework, meeting schedule

**Timeline:** Within 2 weeks of committee formation

**Success Metric:** Meeting held, actions documented, next meeting confirmed

**Priority:** P1 | **Effort:** Low | **Impact:** Medium

#### a-s-7: Approve first 3 AI initiatives

**What:** Use committee process to formally evaluate and approve 3 AI initiatives. Document rationale for each approval.

**Why:** Proves the committee process works. Creates precedent for future decisions.

**Builds On:** Prioritization framework

**Timeline:** Within first 2 meetings

**Success Metric:** 3 initiatives approved with documented decisions

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### a-s-8: Create AI project tracking board

**What:** Visual board (Notion, Asana, etc.) tracking all AI initiatives: status, owner, timeline, blockers, outcomes. Reviewed in committee meetings.

**Why:** Visibility creates accountability. Board shows what's progressing and what's stuck.

**Builds On:** Approved initiatives

**Timeline:** 1 week

**Success Metric:** Board used in 4+ consecutive committee meetings

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

---

## Data Precision

### Why This Pillar Matters

Mill's moat is data. More specifically, it's **the ability to accurately classify food waste better than anyone else**. At 92% accuracy with 500K labeled images, Mill will have the most valuable food waste dataset on Earth. But we're currently at 0% accuracy with 0 labeled images. This pillar is about building that moat.

### What Already Exists

- **Core hardware selected**: Basler ace2 camera, Intel RealSense D455 depth sensor, NVIDIA Jetson Orin NX compute
- **30 food categories defined**: Initial taxonomy complete
- **BOM estimated**: $2,000-3,500 per unit
- **Training data strategy documented**: Path from 80% to 92% accuracy outlined

### Reality Check on Timelines

Hardware development takes longer than software. Here's what industry experience tells us:

| Milestone | Optimistic | Realistic | Why |
|-----------|------------|-----------|-----|
| First prototype built | 4 weeks | 8-12 weeks | Component sourcing, integration issues |
| Prototype tested and refined | 2 weeks | 4-8 weeks | Unknown unknowns emerge in testing |
| 10 beta units produced | 4 weeks | 8-16 weeks | Manufacturing partner onboarding, QA |
| Total: prototype to 10 units | 10 weeks | **24-36 weeks** | Hardware is hard |

For ML:

| Milestone | Optimistic | Realistic | Why |
|-----------|------------|-----------|-----|
| 80% accuracy | 8 weeks | 12-16 weeks | Data collection is the bottleneck |
| 85% accuracy | 4 weeks after 80% | 8-12 weeks | Diminishing returns kick in |
| 92% accuracy | 4 weeks after 85% | 12-20 weeks | Hard edge cases require lots of data |
| Total: 0% to 92% | 16 weeks | **32-48 weeks** | ML iteration is slow |

---

### Subgoal: Hardware Excellence

#### d-h-1: Finalize camera (Basler ace2) ✓ COMPLETED
Selected and documented.

#### d-h-2: Finalize depth sensor (RealSense D455) ✓ COMPLETED
Selected and documented.

#### d-h-3: Finalize edge compute (Jetson Orin NX) ✓ COMPLETED
Selected and documented.

#### d-h-4: Select carrier board

**What:** Evaluate and select carrier board for Jetson Orin NX. Connect Tech is the leading candidate. Document selection criteria and decision.

**Why:** Carrier board affects integration complexity, form factor, and reliability.

**Builds On:** Jetson Orin NX selection

**Timeline:** 2 weeks for evaluation

**Success Metric:** Carrier board selected, ordered, and integration tested with Jetson

**Priority:** P0 | **Effort:** Medium | **Impact:** Medium

#### d-h-5: Select LED lighting system

**What:** Evaluate lighting options for consistent image quality across different ambient conditions. Test with camera system.

**Why:** Lighting is critical for classification accuracy. Inconsistent lighting = inconsistent results.

**Builds On:** Camera selection

**Timeline:** 2 weeks

**Success Metric:** Lighting system achieves consistent image quality in varying ambient light

**Priority:** P0 | **Effort:** Medium | **Impact:** Medium

#### d-h-6: Integrate weight sensor

**What:** Select and integrate weight sensor for volume estimation. Calibration methodology documented.

**Why:** Weight data combined with visual classification enables accurate waste quantification.

**Builds On:** Enclosure design (needs mounting)

**Timeline:** 3-4 weeks

**Success Metric:** Weight readings accurate to +/- 5%

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### d-h-7: Design commercial-grade enclosure

**What:** Design enclosure suitable for commercial kitchen environments: heat resistant, easy to clean, IP-rated, tamper-resistant, service-accessible.

**Why:** Consumer prototype ≠ commercial product. Environment requirements are different.

**Builds On:** Component selections

**Timeline:** 4-6 weeks (CAD + review cycles)

**Success Metric:** Enclosure design approved by operations team, ready for manufacturing

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-h-8: Build first prototype unit

**What:** Assemble first complete prototype: all components integrated, software running, capable of capturing and classifying images.

**Why:** This is the moment of truth for hardware. Proves the design works.

**Builds On:** All component selections, enclosure design

**Timeline:** 4-6 weeks for assembly and basic integration

**Success Metric:** Prototype captures images and runs classification (accuracy TBD)

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-h-9: Test prototype in controlled environment (2+ weeks)

**What:** Deploy prototype in office or lab setting. Capture diverse samples. Measure classification accuracy. Document failures and issues.

**Why:** Controlled testing reveals problems before field deployment.

**Builds On:** First prototype

**Timeline:** 2-4 weeks minimum

**Success Metric:** 100+ samples captured; accuracy baseline established; issues documented

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-h-10: Iterate based on testing learnings

**What:** Address issues found in testing: hardware modifications, software fixes, calibration adjustments. May require multiple iteration cycles.

**Why:** First prototype is never production-ready. Iteration is expected.

**Builds On:** Prototype testing results

**Timeline:** 4-8 weeks (depends on issue severity)

**Success Metric:** Issues from testing resolved; ready for field pilot

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-h-11: Finalize production BOM

**What:** Document complete Bill of Materials for production: all components, suppliers, pricing, lead times. Calculate landed cost per unit.

**Why:** BOM is required for manufacturing partner discussions and pricing decisions.

**Builds On:** Prototype iteration complete

**Timeline:** 2 weeks

**Success Metric:** BOM complete with cost <$3,500/unit (or revised target)

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### d-h-12: Identify and engage manufacturing partner

**What:** Evaluate contract manufacturers for small-batch production. Consider: capabilities, quality, cost, location, lead times. Visit top candidates if possible.

**Why:** Mill isn't a manufacturing company. Partner selection affects quality and timeline.

**Builds On:** BOM finalization

**Timeline:** 6-8 weeks (evaluation + negotiation)

**Success Metric:** Manufacturing partner selected; contract signed

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-h-13: Order components for 10 beta units

**What:** Place component orders for 10 beta units. Manage lead times (some components have 8-12 week lead times).

**Why:** Component lead times determine deployment timeline. Order early.

**Builds On:** BOM, manufacturing partner

**Timeline:** Order 8-12 weeks before needed

**Success Metric:** All components received and QC'd

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### d-h-14: Assemble and test 10 beta units

**What:** Assemble 10 complete units. Test each unit against quality checklist. Document any assembly issues for manufacturing partner.

**Why:** Beta units are for customer pilots. They need to work reliably.

**Builds On:** Components received, manufacturing partner (or in-house assembly)

**Timeline:** 4-6 weeks

**Success Metric:** 10 units pass QC; ready for deployment

**Priority:** P1 | **Effort:** High | **Impact:** High

---

### Subgoal: Baseline Model (80%+ Accuracy)

#### d-m-1: Define initial food categories ✓ COMPLETED
30 categories defined and documented.

#### d-m-2: Source seed dataset (Food-101 etc.)

**What:** Download and prepare public food image datasets: Food-101, ETHZ Food-101, recipes5k. Evaluate quality and relevance to Mill categories.

**Why:** Public datasets bootstrap training. We don't start from zero.

**Builds On:** Category definitions

**Timeline:** 2 weeks

**Success Metric:** 100K+ relevant images from public sources

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-m-3: Collect 500 internal images per category

**What:** Capture Mill-specific images: different angles, lighting conditions, waste states. At least 500 images per category = 15K minimum.

**Why:** Public datasets aren't Mill-specific. Our own data represents our actual use case.

**Builds On:** Prototype hardware for capture

**Timeline:** 4-6 weeks of focused collection

**Success Metric:** 15K+ internal images captured with quality validation

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-m-4: Clean and validate dataset

**What:** Review all images: remove duplicates, fix label errors, ensure category balance, identify quality issues. Data quality > data quantity.

**Why:** Garbage in, garbage out. Bad data trains bad models.

**Builds On:** Collected dataset

**Timeline:** 2-3 weeks (can parallelize with collection)

**Success Metric:** Dataset passes quality audit; error rate <2%

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-m-5: Set up labeling interface

**What:** Deploy labeling tool (Label Studio or similar): category selection UI, quality flags, multi-labeler support, review workflow.

**Why:** Scalable labeling requires proper tooling. Manual labeling doesn't scale.

**Builds On:** Infrastructure setup

**Timeline:** 1-2 weeks

**Success Metric:** Labeling interface deployed; 100+ images labeled in first day

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-m-6: Label seed dataset (15K images)

**What:** Label all seed images using labeling interface. Use multiple labelers for validation. Track inter-labeler agreement.

**Why:** Labeled data is the fuel for ML. More labels = better model (up to a point).

**Builds On:** Labeling interface, collected data

**Timeline:** 4-6 weeks at scale (15K images / ~10 images per minute = ~25 hours of labeling time, but quality checks add overhead)

**Success Metric:** 15K images labeled with >95% agreement rate

**Priority:** P0 | **Effort:** Very High | **Impact:** High

#### d-m-7: Generate synthetic training data

**What:** Use 3D rendering to generate synthetic food waste images. Augment real data with realistic synthetic samples.

**Why:** Synthetic data is cheap and can fill gaps in real data (rare categories, unusual conditions).

**Builds On:** Category definitions, image analysis

**Timeline:** 4-6 weeks (requires 3D asset creation)

**Success Metric:** 10K+ synthetic images that improve model accuracy

**Priority:** P1 | **Effort:** High | **Impact:** Medium

#### d-m-8: Implement data augmentation pipeline

**What:** Build automated augmentation: rotation, scaling, color jitter, cropping, noise injection. Apply to training data to increase effective dataset size.

**Why:** Augmentation multiplies training data without additional labeling cost.

**Builds On:** Training data

**Timeline:** 2 weeks

**Success Metric:** Augmentation improves model accuracy by measurable amount

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-m-9: Set up training infrastructure

**What:** Configure GPU training environment: cloud (AWS/GCP) or local. Set up MLflow for experiment tracking. Version control for datasets and models.

**Why:** Can't train models without infrastructure. Experiment tracking prevents wasted work.

**Builds On:** Cloud/infrastructure accounts

**Timeline:** 1-2 weeks

**Success Metric:** Can train model and track experiment in under 30 minutes from start

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-m-10: Train baseline model (EfficientNet)

**What:** Train EfficientNet-B4 (or similar) on seed dataset. Start with transfer learning from ImageNet. Track accuracy across categories.

**Why:** First real model training. Establishes baseline for improvement.

**Builds On:** Training infrastructure, labeled data

**Timeline:** 2-3 weeks of training and tuning

**Success Metric:** Baseline model trained; accuracy measured on held-out test set

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-m-11: Evaluate on held-out test set

**What:** Reserve 20% of data for testing (never used in training). Evaluate model accuracy by category. Identify best and worst categories.

**Why:** Test set measures real-world performance. Training accuracy is misleading.

**Builds On:** Trained model

**Timeline:** 1 week

**Success Metric:** Per-category accuracy documented; overall accuracy established

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### d-m-12: Identify failure modes

**What:** Analyze model errors: confusion matrix, example failures, systematic patterns. Categorize: data issues vs. model issues vs. inherent difficulty.

**Why:** Understanding failures tells you what to fix. Random iteration is slow.

**Builds On:** Model evaluation

**Timeline:** 1-2 weeks

**Success Metric:** Top 10 failure modes documented with hypothesized causes

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### d-m-13: Iterate to 80% accuracy

**What:** Address failure modes through: more data for weak categories, architecture changes, training hyperparameter tuning. Continue until 80% overall accuracy achieved.

**Why:** 80% is minimum viable accuracy for pilot deployments.

**Builds On:** Failure mode analysis

**Timeline:** 8-16 weeks (realistically)

**Success Metric:** 80%+ overall accuracy on held-out test set

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-m-14: Document model card

**What:** Create model card: training data description, accuracy metrics, known limitations, recommended use cases, failure modes, update history.

**Why:** Model documentation enables responsible deployment and future improvement.

**Builds On:** Trained model, evaluation results

**Timeline:** 1 week

**Success Metric:** Model card reviewed and published internally

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

---

### Subgoal: Beta Deployment (10-50 Bins)

#### d-b-1: Identify 3-5 beta site partners

**What:** Find 3-5 companies willing to host beta bins: diverse verticals, willing to provide feedback, realistic expectations about accuracy.

**Why:** Beta sites provide real-world data and validation. Diversity reveals category gaps.

**Builds On:** Pipeline prioritization, Commercial relationships

**Timeline:** 4-8 weeks (sales cycle for no-cost pilot)

**Success Metric:** 3-5 signed beta agreements

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-b-2: Sign beta agreements

**What:** Legal agreements covering: equipment ownership, data rights, liability, timeline, feedback requirements, path to commercial.

**Why:** Protect Mill and set expectations. Don't deploy without agreements.

**Builds On:** Beta site conversations

**Timeline:** 2-4 weeks per site

**Success Metric:** All beta sites have signed agreements

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### d-b-3: Install first bin at Site #1

**What:** Physical installation, network connectivity, software configuration, staff training, go-live checklist. Document everything.

**Why:** First deployment is the template. Document thoroughly for repeatability.

**Builds On:** Hardware ready, beta agreement signed

**Timeline:** 1-2 weeks for installation

**Success Metric:** Bin operational and capturing data

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-b-4: Install bins at Sites #2-5

**What:** Repeat installation at remaining beta sites. Use documentation from Site #1. Refine process.

**Why:** Multiple sites = diverse data = better model.

**Builds On:** Site #1 experience

**Timeline:** 2-4 weeks (can parallelize)

**Success Metric:** All beta bins operational

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-b-5: Set up Human-in-the-Loop (HITL) review queue

**What:** System for human review of low-confidence classifications: queue interface, review workflow, feedback loop to training data.

**Why:** HITL maintains quality when model is uncertain. Also generates training data.

**Builds On:** Classification system, labeling interface

**Timeline:** 2-3 weeks

**Success Metric:** HITL queue operational; reviews happening within 24 hours

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-b-6: Hire and train 2 labelers

**What:** Hire 2 part-time or contract labelers for HITL review. Train on food categories, quality standards, escalation procedures.

**Why:** Labeling volume exceeds what existing team can handle.

**Builds On:** HITL queue setup

**Timeline:** 4-6 weeks (hiring + training)

**Success Metric:** Labelers processing queue with >95% quality

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-b-7: Analyze first week of live data

**What:** After first week of beta operation: analyze classification accuracy, identify new failure modes, compare to test set performance, document real-world challenges.

**Why:** Lab testing ≠ field performance. First week reveals reality.

**Builds On:** Beta deployment

**Timeline:** 1 week after deployment

**Success Metric:** Accuracy baseline established for live data

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-b-8: Review and assess first week accuracy

**What:** Compare expected accuracy to actual. Identify gaps. Prioritize fixes.

**Why:** Data-driven improvement requires measurement.

**Builds On:** First week data

**Timeline:** 2-3 days of analysis

**Success Metric:** Accuracy assessment documented with action plan

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### d-b-9: Implement weekly retrain cycle

**What:** Set up automated weekly process: collect labeled data from HITL, retrain model, evaluate improvement, deploy updated model.

**Why:** Continuous improvement requires continuous retraining. Models get better with more data.

**Builds On:** Training infrastructure, HITL data

**Timeline:** 2-3 weeks to automate

**Success Metric:** Weekly retrains happening automatically; accuracy trending upward

**Priority:** P0 | **Effort:** High | **Impact:** High

#### d-b-10: Scale to 10 bins

**What:** Deploy bins 6-10 at existing or new beta sites. Same process as initial deployment.

**Why:** More bins = more data = better model. Scale proves operational capability.

**Builds On:** Beta deployment process

**Timeline:** 4-6 weeks after initial deployment

**Success Metric:** 10 bins operational and generating data

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-b-11: WIN: Achieve 85% accuracy

**What:** Through data collection, labeling, and retraining, reach 85% overall classification accuracy on live data.

**Why:** 85% is commercially viable accuracy. Customers can trust the data.

**Builds On:** Weekly retrain cycle, HITL data

**Timeline:** 12-20 weeks from initial deployment (realistically)

**Success Metric:** 85%+ accuracy sustained over 2+ weeks on live data

**Priority:** P0 (milestone) | **Effort:** High | **Impact:** High

#### d-b-12: Scale to 25 bins

**What:** Expand deployment to 25 total bins across beta sites.

**Why:** Scale increases data volume and tests operational capacity.

**Builds On:** 10-bin deployment

**Timeline:** 6-10 weeks

**Success Metric:** 25 bins operational

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-b-13: Scale to 50 bins

**What:** Expand to 50 total bins. May require new beta partners.

**Why:** 50 bins generates serious training data volume.

**Builds On:** 25-bin deployment

**Timeline:** 8-12 weeks

**Success Metric:** 50 bins operational

**Priority:** P2 | **Effort:** High | **Impact:** High

#### d-b-14: WIN: Achieve 88% accuracy

**What:** Continue improvement to reach 88% accuracy.

**Why:** 88% is competitive with best-in-class solutions.

**Builds On:** Scaled deployment, retraining

**Timeline:** 8-16 weeks after 85%

**Success Metric:** 88%+ accuracy sustained

**Priority:** P1 (milestone) | **Effort:** High | **Impact:** High

#### d-b-15: Reduce human review to <15%

**What:** Improve model confidence to reduce HITL review volume from initial high percentage to <15% of classifications.

**Why:** Human review is expensive. Automation improves unit economics.

**Builds On:** Model improvement

**Timeline:** Concurrent with accuracy improvement

**Success Metric:** <15% of classifications require human review

**Priority:** P2 | **Effort:** High | **Impact:** High

---

### Subgoal: Training Data Flywheel

#### d-f-1: Implement auto-labeling for high-confidence predictions

**What:** Automatically accept classifications above a confidence threshold (e.g., 95%) and add them to training data without human review.

**Why:** Reduces labeling cost for easy cases. Humans focus on hard cases.

**Builds On:** Classification system, confidence calibration

**Timeline:** 2-3 weeks

**Success Metric:** 30%+ of classifications auto-labeled with >99% accuracy

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-f-2: Implement active learning

**What:** Prioritize human review for images where model is most uncertain or where review would most improve the model.

**Why:** Active learning gets more improvement per labeled image than random sampling.

**Builds On:** HITL system, model uncertainty estimates

**Timeline:** 3-4 weeks

**Success Metric:** Active learning improves accuracy faster than random labeling

**Priority:** P1 | **Effort:** High | **Impact:** High

#### d-f-3: Build model monitoring dashboard

**What:** Real-time dashboard: accuracy trends, confidence distributions, category performance, data drift detection, retraining triggers.

**Why:** Monitoring catches problems before they affect customers.

**Builds On:** Classification system, data warehouse

**Timeline:** 3-4 weeks

**Success Metric:** Dashboard used in weekly reviews; issues caught proactively

**Priority:** P1 | **Effort:** High | **Impact:** Medium

#### d-f-4: Implement menu-aware classification

**What:** Use customer menu data to narrow classification options. If customer serves pizza, model knows to look for pizza.

**Why:** Context improves accuracy. Menu data is easy to get from customers.

**Builds On:** Customer integration, model architecture

**Timeline:** 4-6 weeks

**Success Metric:** Menu-aware mode improves accuracy by measurable percentage

**Priority:** P2 | **Effort:** High | **Impact:** High

#### d-f-5: Implement per-customer model fine-tuning

**What:** Fine-tune base model on each customer's specific data to improve accuracy for their particular food items and conditions.

**Why:** Every customer's waste is slightly different. Customization improves accuracy.

**Builds On:** Customer data accumulation

**Timeline:** 4-6 weeks

**Success Metric:** Fine-tuning improves customer-specific accuracy

**Priority:** P2 | **Effort:** High | **Impact:** High

#### d-f-6: Design novel food detection

**What:** System to detect when the model sees food it wasn't trained on. Flag for human review and potential category addition.

**Why:** The world has more than 30 food categories. System needs to handle novelty.

**Builds On:** Model architecture, HITL system

**Timeline:** 4-6 weeks

**Success Metric:** Novel foods detected with >80% recall

**Priority:** P2 | **Effort:** High | **Impact:** Medium

#### d-f-7: R&D: Explore federated learning

**What:** Research whether federated learning could allow model training across customers without centralizing data. Proof of concept if promising.

**Why:** Privacy-preserving ML may be required for some enterprise customers.

**Builds On:** ML research

**Timeline:** 8-12 weeks for exploration

**Success Metric:** Decision documented: pursue or deprioritize

**Priority:** P3 | **Effort:** High | **Impact:** Medium

#### d-f-8: Reach 500K labeled images

**What:** Through combination of human labeling, auto-labeling, and synthetic data, accumulate 500K labeled images.

**Why:** 500K images is the dataset size that enables 92%+ accuracy.

**Builds On:** All training data collection

**Timeline:** 4-6 months of accumulation

**Success Metric:** 500K labeled images in dataset

**Priority:** P2 | **Effort:** Very High | **Impact:** High

#### d-f-9: WIN: Achieve 92% accuracy

**What:** Reach 92% classification accuracy—best-in-class performance.

**Why:** 92% is the accuracy where human review becomes minimal and data is fully trusted.

**Builds On:** 500K images, model iteration

**Timeline:** 6-10 months from project start (realistically)

**Success Metric:** 92%+ accuracy sustained on live data

**Priority:** P2 (milestone) | **Effort:** Very High | **Impact:** High

#### d-f-10: Reduce human review to <10%

**What:** Continue model improvement until fewer than 10% of classifications require human review.

**Why:** <10% human review makes unit economics compelling at scale.

**Builds On:** 92% accuracy

**Timeline:** Concurrent with accuracy improvement

**Success Metric:** <10% human review rate sustained

**Priority:** P3 | **Effort:** High | **Impact:** High

---

## Outcome Delivery

### Why This Pillar Matters

Mill's pricing model depends on proving outcomes. If we can't credibly measure and attribute cost savings to Mill, outcome-based pricing falls apart. This pillar builds the infrastructure to measure, verify, and communicate ROI with CFO-level credibility.

### What Already Exists

- **Outcome-based pricing model defined**: Core structure documented
- **Whole Foods relationship**: Potential first proof point

---

### Subgoal: Measurement Infrastructure

#### o-m-1: Define baseline methodology

**What:** Document exactly how baselines are established: data collection period (60 days), data types (weight, cost, category), normalization factors (seasonality, volume), what counts as "Mill-attributed."

**Why:** Methodology must be bulletproof. CFOs will scrutinize the numbers.

**Builds On:** Pricing model

**Timeline:** 2-3 weeks

**Success Metric:** Methodology reviewed by finance expert and approved

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### o-m-2: Create baseline data collection UX

**What:** Interface for baseline data capture: manual entry, POS integration, receipt upload. Make it easy for customers to provide baseline data.

**Why:** Baseline data from customers requires their participation. UX matters.

**Builds On:** Baseline methodology

**Timeline:** 3-4 weeks

**Success Metric:** Baseline data collected from pilot customer without friction complaints

**Priority:** P0 | **Effort:** High | **Impact:** High

#### o-m-3: Build waste-to-cost conversion engine

**What:** System that converts waste data (kg of food type) to cost ($): price per kg by category, regional adjustments, labor cost inclusion, disposal cost inclusion.

**Why:** Customers care about money, not kilograms. Conversion enables ROI communication.

**Builds On:** Classification system, pricing data

**Timeline:** 3-4 weeks

**Success Metric:** Cost calculations validated against customer's own financial data

**Priority:** P0 | **Effort:** High | **Impact:** High

#### o-m-4: Implement savings calculation pipeline

**What:** Automated calculation: baseline cost - current cost = savings. Apply attribution methodology. Generate savings reports.

**Why:** Manual calculation doesn't scale. Automation ensures consistency.

**Builds On:** Cost conversion, baseline data

**Timeline:** 3-4 weeks

**Success Metric:** Automated reports match manual calculations within 2%

**Priority:** P0 | **Effort:** High | **Impact:** High

#### o-m-5: Create full audit trail

**What:** Complete logging: every data point, every calculation, every methodology assumption. Exportable for customer review or third-party audit.

**Why:** Trust requires transparency. Customers (and their auditors) should be able to verify everything.

**Builds On:** Savings calculation

**Timeline:** 2-3 weeks

**Success Metric:** Audit trail passes review by customer finance team

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-m-6: Build attribution model

**What:** Methodology for attributing savings to Mill vs. other factors: behavior change, seasonality, menu changes, staffing. Conservative attribution builds trust.

**Why:** Not all savings are Mill savings. Honest attribution maintains credibility.

**Builds On:** Savings calculation

**Timeline:** 3-4 weeks

**Success Metric:** Attribution model reviewed and accepted by pilot customer

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-m-7: Validate methodology with finance expert

**What:** Have methodology reviewed by an external finance/accounting expert (CPA, CFO advisor). Get written feedback and make adjustments.

**Why:** External validation adds credibility and catches blind spots.

**Builds On:** Complete methodology

**Timeline:** 2-3 weeks

**Success Metric:** Expert review completed; major issues addressed

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### o-m-8: Document methodology for customer trust

**What:** Customer-facing document explaining methodology: how baseline is measured, how savings are calculated, how attribution works, what's included/excluded.

**Why:** Customers need to understand and trust the methodology before signing outcome contracts.

**Builds On:** Complete methodology

**Timeline:** 1-2 weeks

**Success Metric:** Document used in 3+ customer conversations without confusion

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### o-m-9: Get CFO methodology approval (pilot customer)

**What:** Present methodology to pilot customer's CFO or finance team. Get explicit approval that they will accept these calculations for outcome-based billing.

**Why:** Finance team sign-off prevents billing disputes later.

**Builds On:** Methodology documentation

**Timeline:** 2-4 weeks (meeting scheduling)

**Success Metric:** Written approval from customer finance

**Priority:** P1 | **Effort:** Medium | **Impact:** High

---

### Subgoal: Customer Dashboards

#### o-d-1: Design dashboard mockups (Figma)

**What:** Create interactive mockups: main dashboard view, cost savings view, sustainability view, trend view, export options. Get feedback before building.

**Why:** Design before development prevents wasted engineering effort.

**Builds On:** Customer requirements research

**Timeline:** 2-3 weeks

**Success Metric:** Mockups approved by 2+ prospective customers

**Priority:** P0 | **Effort:** High | **Impact:** High

#### o-d-2: Get customer feedback on mockups

**What:** Show mockups to 3-5 prospective customers. Collect feedback: what's valuable, what's confusing, what's missing.

**Why:** Build what customers want, not what we assume they want.

**Builds On:** Initial mockups

**Timeline:** 2 weeks

**Success Metric:** Feedback collected; mockups revised

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### o-d-3: Build dashboard MVP

**What:** Functional dashboard with core views: real-time waste data, basic cost calculations, simple visualizations. Ship fast, iterate later.

**Why:** MVP gets feedback. Perfect delays feedback.

**Builds On:** Approved mockups

**Timeline:** 4-6 weeks

**Success Metric:** MVP deployed to first customer

**Priority:** P0 | **Effort:** High | **Impact:** High

#### o-d-4: Add cost savings view

**What:** Dashboard view showing: baseline vs. current, total savings to date, projected annual savings, savings by category.

**Why:** Cost savings is the primary value proposition. Needs prominent display.

**Builds On:** Dashboard MVP, savings calculation

**Timeline:** 2-3 weeks

**Success Metric:** Cost view live; customer uses it in internal reports

**Priority:** P0 | **Effort:** High | **Impact:** High

#### o-d-5: Add sustainability/ESG view

**What:** Dashboard view showing: CO2 avoided, water saved, landfill diversion. Mapped to ESG reporting frameworks.

**Why:** Sustainability teams are often buyers. They need data for their reports.

**Builds On:** Dashboard MVP

**Timeline:** 2-3 weeks

**Success Metric:** Sustainability view used in customer ESG reporting

**Priority:** P1 | **Effort:** High | **Impact:** Medium

#### o-d-6: Add trend analysis and forecasting

**What:** Historical trends (week over week, month over month), predictive analytics (where is waste headed), anomaly detection (unusual spikes).

**Why:** Trends enable proactive waste reduction, not just measurement.

**Builds On:** Accumulated data

**Timeline:** 3-4 weeks

**Success Metric:** Forecasts within 15% of actual outcomes

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-d-7: Add export capabilities (PDF, CSV)

**What:** One-click export of dashboard data: PDF reports for management, CSV for analysis, scheduled email reports.

**Why:** Customers need to share data internally. Export enables that.

**Builds On:** Dashboard views

**Timeline:** 1-2 weeks

**Success Metric:** Exports used in 3+ customer internal presentations

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

#### o-d-8: Add benchmark comparison

**What:** Compare customer's performance to anonymized industry benchmarks: "You're in the top 20% for waste reduction."

**Why:** Benchmarks add context and motivation. "Am I doing well?" is a common question.

**Builds On:** Multi-customer data

**Timeline:** 3-4 weeks

**Success Metric:** Customers cite benchmark data in conversations

**Priority:** P2 | **Effort:** High | **Impact:** High

#### o-d-9: Deploy dashboard to first customer

**What:** Full deployment: data pipeline connected, dashboard live, customer trained, feedback loop established.

**Why:** First deployment proves the dashboard works in production.

**Builds On:** Dashboard MVP

**Timeline:** 1-2 weeks after MVP

**Success Metric:** Customer actively using dashboard weekly

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### o-d-10: Collect feedback and iterate

**What:** Structured feedback from first customer: weekly check-ins for first month, documented issues, prioritized improvements.

**Why:** First customer shapes the product. Listen carefully.

**Builds On:** First deployment

**Timeline:** 4 weeks of active feedback

**Success Metric:** Top 5 feedback items addressed in product

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-d-11: Deploy dashboard to 5 customers

**What:** Scale dashboard deployment to next 4 customers. Refine onboarding process.

**Why:** Scale validates that dashboard works beyond one customer.

**Builds On:** First customer deployment

**Timeline:** 4-8 weeks (depends on sales cycle)

**Success Metric:** 5 customers on dashboard with >80% weekly active use

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-d-12: Build automated report generation

**What:** System that automatically generates weekly/monthly reports: highlight key metrics, compare to goals, recommend actions. Sent via email.

**Why:** Reduce burden on customers to log in and check. Push value to them.

**Builds On:** Dashboard, export capabilities

**Timeline:** 3-4 weeks

**Success Metric:** Automated reports sent to 5+ customers weekly

**Priority:** P2 | **Effort:** High | **Impact:** Medium

---

### Subgoal: Procurement Recommendations

#### o-p-1: Analyze waste-to-procurement correlation

**What:** Research: which waste patterns predict which procurement adjustments? Map waste categories to actionable recommendations.

**Why:** Recommendations are where Mill goes from measurement to action.

**Builds On:** Accumulated waste data, procurement domain research

**Timeline:** 4-6 weeks of analysis

**Success Metric:** Documented correlation between waste patterns and procurement actions

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-p-2: Design recommendation engine

**What:** Architecture for recommendation system: inputs (waste data, menu, inventory), processing (rules + ML), outputs (specific recommendations with confidence).

**Why:** Design before build prevents architectural mistakes.

**Builds On:** Correlation analysis

**Timeline:** 2-3 weeks

**Success Metric:** Architecture reviewed and approved

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-p-3: Build recommendation MVP

**What:** Basic recommendation system: rule-based initially, generating top 5 recommendations per week per customer.

**Why:** Simple rules can provide value while ML matures.

**Builds On:** Engine design

**Timeline:** 4-6 weeks

**Success Metric:** MVP generating relevant recommendations

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-p-4: Test recommendations with pilot customer

**What:** Deploy recommendations to willing pilot customer. Track: which recommendations are accepted, which are ignored, which lead to savings.

**Why:** Real-world testing validates recommendation quality.

**Builds On:** Recommendation MVP

**Timeline:** 4-8 weeks of testing

**Success Metric:** 30%+ recommendations accepted; measurable savings from accepted

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-p-5: Measure recommendation adoption rate

**What:** Track adoption: recommendations generated vs. viewed vs. accepted vs. implemented. Identify blockers to adoption.

**Why:** Recommendations not adopted don't create value. Understand why.

**Builds On:** Pilot testing

**Timeline:** Ongoing

**Success Metric:** 40%+ adoption rate sustained

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

#### o-p-6: Calculate savings from recommendations

**What:** Quantify: for recommendations that were implemented, what savings resulted? Create ROI case for recommendation feature.

**Why:** Prove that recommendations drive incremental value beyond measurement.

**Builds On:** Adoption tracking, savings measurement

**Timeline:** 3-6 months of data accumulation

**Success Metric:** $X savings documented from recommendations (target TBD)

**Priority:** P2 | **Effort:** High | **Impact:** High

#### o-p-7: Integrate with procurement systems (SAP, Oracle, etc.)

**What:** Build integrations to push recommendations directly into customer procurement workflows. Reduce friction to act.

**Why:** Integration makes recommendations actionable without manual steps.

**Builds On:** Recommendation system, customer IT relationships

**Timeline:** 6-12 weeks per integration

**Success Metric:** First integration live with customer using it

**Priority:** P2 | **Effort:** High | **Impact:** High

#### o-p-8: WIN: Prove 2-5% procurement cost reduction

**What:** Document verified case where Mill recommendations led to 2-5% reduction in food procurement costs.

**Why:** This is Mill's ultimate value proposition: not just measuring waste but reducing food costs.

**Builds On:** Recommendation adoption, savings measurement

**Timeline:** 6-12 months (requires sustained usage)

**Success Metric:** Customer-verified 2-5% cost reduction

**Priority:** P1 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

---

### Subgoal: Proof Points

#### o-pr-1: WIN: Publish first verified ROI

**What:** Create and publish case study with verified ROI numbers: customer name (with permission), baseline, savings, methodology, testimonial.

**Why:** First verified ROI unlocks enterprise sales. This is the most important proof point.

**Builds On:** Whole Foods or first paying customer

**Timeline:** 3-6 months after deployment

**Success Metric:** Case study published on website and used in sales

**Priority:** P0 (milestone) | **Effort:** High | **Impact:** High

#### o-pr-2: Get customer sign-off on case study

**What:** Work with customer to review and approve case study content. Get formal permission for public use.

**Why:** Unauthorized case studies create legal risk and damage trust.

**Builds On:** ROI verification

**Timeline:** 2-4 weeks

**Success Metric:** Written approval for case study publication

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### o-pr-3: Get testimonial from decision-maker

**What:** Video or written quote from customer executive who approved Mill purchase. Ideally VP+ level with recognizable title.

**Why:** Executive testimonials carry weight with other executives.

**Builds On:** Customer relationship

**Timeline:** 1-2 weeks

**Success Metric:** Usable testimonial with attribution

**Priority:** P0 | **Effort:** Low | **Impact:** High

#### o-pr-4: Publish second verified ROI

**What:** Second customer case study with verified ROI. Ideally different vertical than first.

**Why:** Two case studies = pattern. One = anecdote.

**Builds On:** Second customer deployment

**Timeline:** Depends on customer pipeline

**Success Metric:** Second case study published

**Priority:** P1 | **Effort:** High | **Impact:** High

#### o-pr-5: Publish third verified ROI

**What:** Third case study. Now it's a trend.

**Why:** Three case studies in different verticals shows broad applicability.

**Builds On:** Third customer deployment

**Timeline:** Depends on customer pipeline

**Success Metric:** Third case study published

**Priority:** P2 | **Effort:** High | **Impact:** Medium

#### o-pr-6: Secure Whole Foods public reference

**What:** Get Whole Foods to agree to be publicly named as a Mill customer/partner.

**Why:** Whole Foods name recognition opens doors across grocery and food retail.

**Builds On:** Whole Foods relationship and results

**Timeline:** Depends on relationship development

**Success Metric:** Whole Foods logo usable on website

**Priority:** P0 | **Effort:** Medium | **Impact:** High

#### o-pr-7: Secure analyst or press coverage

**What:** Get coverage from relevant analysts (Gartner, Forrester) or press (GreenBiz, Food Tech publications).

**Why:** Third-party coverage adds credibility beyond self-promotion.

**Builds On:** Case studies, PR outreach

**Timeline:** 3-6 months (pitch cycles)

**Success Metric:** At least one substantive article or analyst mention

**Priority:** P2 | **Effort:** High | **Impact:** High

#### o-pr-8: Create shareable proof library

**What:** Central repository of all proof materials: case studies, testimonials, ROI data, analyst quotes. Easy to find and share for sales team.

**Why:** Proof materials lose impact when they're scattered and hard to find.

**Builds On:** All proof point creation

**Timeline:** 2 weeks to organize

**Success Metric:** Sales team finds and uses proof materials without asking for help

**Priority:** P1 | **Effort:** Medium | **Impact:** Medium

---

## Scale Effects

### Why This Pillar Matters

Mill's long-term defensibility comes from network effects: every new customer makes the data more valuable for everyone, every data point improves the model, and the aggregate dataset becomes impossible to replicate. But network effects don't happen automatically—they require deliberate design and investment.

### What Already Exists

- **Early data accumulation strategy**: Planned approach to building dataset
- **Partnership conversations**: Initial outreach to potential data partners

### Reality Check

Scale Effects is largely a Year 2+ pillar. Most tasks here are P2/P3 because they depend on having customers and data first. Don't let these distract from the blocking work in other pillars.

---

### Subgoal: Network Effects

#### s-n-1: Define data anonymization approach

**What:** Technical and legal framework for anonymizing customer data to enable cross-customer analysis without exposing individual customer information.

**Why:** Network effects require data sharing. Data sharing requires privacy protection.

**Builds On:** Data accumulation

**Timeline:** 4-6 weeks (legal review required)

**Success Metric:** Anonymization approach approved by legal; customers comfortable

**Priority:** P1 | **Effort:** High | **Impact:** High

#### s-n-2: Design cross-customer benchmarking

**What:** System for comparing customer performance to anonymized peer group: "Your waste is 20% below industry average."

**Why:** Benchmarking is value that individual customers can't get on their own. Network effect in action.

**Builds On:** Anonymization approach, multi-customer data

**Timeline:** 3-4 weeks design

**Success Metric:** Design approved; customers express interest

**Priority:** P1 | **Effort:** High | **Impact:** High

#### s-n-3: Build benchmark comparison tool

**What:** Functional benchmarking tool: customer inputs their data, sees comparison to relevant peer group. Integrated into dashboard.

**Why:** Design without implementation is just a slide deck.

**Builds On:** Benchmarking design

**Timeline:** 4-6 weeks

**Success Metric:** Tool used by 10+ customers

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-n-4: Create industry insights reports

**What:** Quarterly reports synthesizing data across customers: trends, best practices, benchmarks. Anonymized and aggregated.

**Why:** Insights reports demonstrate the value of Mill's unique dataset.

**Builds On:** Multi-customer data, benchmarking

**Timeline:** Ongoing quarterly

**Success Metric:** Insights reports downloaded/viewed 1000+ times

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-n-5: WIN: 20 enterprise deployments

**What:** Reach 20 paying enterprise customers with Mill deployed.

**Why:** 20 customers creates meaningful network effects and proves repeatable sales.

**Builds On:** Sales, deployment, retention

**Timeline:** 12-18 months

**Success Metric:** 20 enterprise deployments live

**Priority:** P0 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

#### s-n-6: WIN: 50 enterprise deployments

**What:** Scale to 50 enterprise customers.

**Why:** 50 customers creates significant data moat.

**Builds On:** 20 customers

**Timeline:** 18-24 months

**Success Metric:** 50 enterprise deployments live

**Priority:** P1 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

#### s-n-7: WIN: 100 enterprise deployments

**What:** Scale to 100 enterprise customers.

**Why:** 100 customers = clear market leader position.

**Builds On:** 50 customers

**Timeline:** 24-36 months

**Success Metric:** 100 enterprise deployments live

**Priority:** P2 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

#### s-n-8: Document network effect metrics

**What:** Define and track metrics that demonstrate network effects: model accuracy improvement per customer added, benchmark value per customer, cross-customer insights generated.

**Why:** Network effects need to be measured to be managed.

**Builds On:** Multi-customer data

**Timeline:** 2-3 weeks to define, ongoing to track

**Success Metric:** Network effect metrics included in board reporting

**Priority:** P2 | **Effort:** Medium | **Impact:** Medium

---

### Subgoal: Strategic Partnerships

#### s-p-1: Identify 10 potential data partners

**What:** Research organizations who would benefit from Mill's data: food distributors, CPG companies, sustainability consultancies, government agencies, academic researchers.

**Why:** Data partnerships create value beyond direct customers. Also potential revenue stream.

**Builds On:** Data accumulation

**Timeline:** 2-3 weeks

**Success Metric:** 10 potential partners identified with rationale

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### s-p-2: Create data partnership pitch

**What:** Presentation for potential data partners: what data Mill has, how it could benefit them, what Mill wants in return, privacy/legal framework.

**Why:** Partners need to understand the value proposition.

**Builds On:** Partner research

**Timeline:** 2 weeks

**Success Metric:** Pitch deck reviewed and approved

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### s-p-3: Reach out to top 5 partners

**What:** Initiate conversations with 5 highest-potential data partners. Present pitch, gauge interest, understand their needs.

**Why:** Conversations reveal whether data partnership model is viable.

**Builds On:** Partner list, pitch deck

**Timeline:** 4-8 weeks of outreach

**Success Metric:** Meetings held with 5 potential partners

**Priority:** P1 | **Effort:** High | **Impact:** High

#### s-p-4: WIN: Sign first data partnership

**What:** Close first formal data partnership agreement: data sharing terms, revenue sharing, exclusivity terms.

**Why:** First partnership validates the data monetization model.

**Builds On:** Partner conversations

**Timeline:** 6-12 months from outreach start

**Success Metric:** Signed partnership agreement

**Priority:** P1 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

#### s-p-5: Explore distributor partnerships

**What:** Evaluate partnerships with food distributors (Sysco, US Foods): integration opportunities, joint go-to-market, data sharing.

**Why:** Distributors touch thousands of restaurants. Partnership accelerates distribution.

**Builds On:** Customer traction

**Timeline:** 6-12 months of exploration

**Success Metric:** Decision: pursue actively or deprioritize

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-p-6: Explore POS/technology partnerships

**What:** Evaluate partnerships with restaurant technology providers (Toast, Square, Olo): integration opportunities, co-selling, data exchange.

**Why:** Tech integrations make Mill stickier and easier to adopt.

**Builds On:** Product maturity

**Timeline:** 6-12 months of exploration

**Success Metric:** Decision: pursue actively or deprioritize

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-p-7: Sign POS integration partnership

**What:** Formal partnership with one major POS provider: API integration, joint marketing, referral terms.

**Why:** POS integration is the highest-leverage tech partnership for distribution.

**Builds On:** POS exploration

**Timeline:** 12+ months

**Success Metric:** Signed partnership; integration live

**Priority:** P2 | **Effort:** High | **Impact:** High

---

### Subgoal: Industry Authority

#### s-a-1: Draft "State of Food Waste" report outline

**What:** Outline for industry report: sections, data sources, key findings to highlight, design approach, distribution plan.

**Why:** Planning prevents scope creep and ensures valuable output.

**Builds On:** Data accumulation

**Timeline:** 1-2 weeks

**Success Metric:** Outline approved by leadership

**Priority:** P1 | **Effort:** Medium | **Impact:** High

#### s-a-2: Compile data for industry report

**What:** Gather and analyze data for report: Mill's own data, public data sources, customer interviews, expert quotes.

**Why:** Reports without data are just opinions.

**Builds On:** Report outline, data access

**Timeline:** 4-8 weeks

**Success Metric:** All data sections populated with defensible data

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-a-3: Design and publish report

**What:** Professional design, final editing, publishing (PDF + web), launch communications.

**Why:** Presentation matters. Well-designed reports get shared more.

**Builds On:** Report content

**Timeline:** 4-6 weeks

**Success Metric:** Report published and launched

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-a-4: Pitch report to press

**What:** Proactive PR outreach: pitch report findings to 10+ relevant journalists and publications. Prepare spokesperson for interviews.

**Why:** Press coverage amplifies report reach beyond owned channels.

**Builds On:** Published report

**Timeline:** 2-4 weeks of outreach

**Success Metric:** 3+ media placements citing the report

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-a-5: Present at industry conference

**What:** Submit speaking proposals to relevant conferences: NRA Show, Waste360, sustainability conferences. Present Mill's findings and thought leadership.

**Why:** Conference presence builds credibility and generates leads.

**Builds On:** Report, customer proof

**Timeline:** 6-12 months (conference cycles)

**Success Metric:** Speaking slot secured; presentation delivered

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-a-6: Brief EPA/USDA on findings

**What:** Offer to brief relevant government agencies on Mill's food waste findings. Position Mill as trusted data source for policy discussions.

**Why:** Government relationships create long-term positioning and potential regulatory tailwinds.

**Builds On:** Report, credible data

**Timeline:** 6-12 months

**Success Metric:** Briefing delivered to at least one agency

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-a-7: WIN: Cited in policy or academic work

**What:** Mill data cited in academic paper, government report, or policy proposal.

**Why:** Academic/policy citation is the ultimate validation of data credibility.

**Builds On:** Published report, government relationships

**Timeline:** 12-24 months

**Success Metric:** At least one citation in peer-reviewed or government publication

**Priority:** P3 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

---

### Subgoal: Data Monetization

#### s-m-1: Define Mill Insights product concept

**What:** Product definition for data product: what data, who buys it, what problems it solves, pricing model, delivery format.

**Why:** Clear product definition before building prevents wasted effort.

**Builds On:** Data partner conversations, market research

**Timeline:** 2-3 weeks

**Success Metric:** Product concept approved by leadership

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-m-2: Design Mill Insights MVP

**What:** Design data product experience: what users see, how they access data, what reports/exports are available.

**Why:** Design before development, as always.

**Builds On:** Product concept

**Timeline:** 2-3 weeks

**Success Metric:** Design reviewed and approved

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-m-3: Build Mill Insights beta

**What:** Functional beta of data product. May be as simple as monthly data export or as complex as self-service analytics.

**Why:** Beta enables early customer validation.

**Builds On:** Design

**Timeline:** 4-8 weeks

**Success Metric:** Beta functional for pilot customers

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-m-4: Pilot Mill Insights with 3 customers

**What:** Deploy Mill Insights to 3 pilot customers: food distributors, CPG companies, or consultancies who want food waste data.

**Why:** Pilots validate willingness to pay and product-market fit.

**Builds On:** Beta product

**Timeline:** 4-8 weeks

**Success Metric:** 3 pilots underway; feedback collected

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-m-5: Define data product pricing model

**What:** Pricing for Mill Insights: per-report, subscription, enterprise license. Based on pilot feedback and value delivered.

**Why:** Pricing affects adoption and revenue. Get it right.

**Builds On:** Pilot learnings

**Timeline:** 2 weeks

**Success Metric:** Pricing approved and ready for sales

**Priority:** P2 | **Effort:** Medium | **Impact:** High

#### s-m-6: Launch Mill Insights publicly

**What:** Public launch of data product: website presence, sales enablement, marketing support.

**Why:** Pilots prove viability; launch captures broader market.

**Builds On:** Pricing, successful pilots

**Timeline:** 8-12 weeks after pilots

**Success Metric:** Mill Insights generating revenue

**Priority:** P3 | **Effort:** High | **Impact:** High

#### s-m-7: WIN: $100K ARR from data products

**What:** Reach $100K annual recurring revenue from Mill Insights and data partnerships.

**Why:** $100K ARR proves data monetization is viable at scale.

**Builds On:** Data product launch, partnerships

**Timeline:** 18-24 months

**Success Metric:** $100K ARR from data products

**Priority:** P3 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

#### s-m-8: WIN: $1M ARR from data products

**What:** Scale data product revenue to $1M ARR.

**Why:** $1M ARR makes data products a meaningful business line.

**Builds On:** $100K ARR

**Timeline:** 24-36 months

**Success Metric:** $1M ARR from data products

**Priority:** P3 (milestone) | **Effort:** Low (outcome measure) | **Impact:** High

---

### Subgoal: Supply Chain Integration

#### s-sc-1: Map procurement system landscape

**What:** Research major procurement systems used by target customers: SAP, Oracle, Coupa, etc. Understand integration capabilities and requirements.

**Why:** Integration strategy requires understanding the landscape.

**Builds On:** Customer conversations

**Timeline:** 3-4 weeks

**Success Metric:** Landscape documented with integration feasibility assessment

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-sc-2: Build first procurement integration

**What:** Technical integration with one major procurement system (likely SAP or Oracle). Push recommendations into procurement workflows.

**Why:** Integration removes friction from acting on Mill recommendations.

**Builds On:** Landscape mapping, recommendation engine

**Timeline:** 8-12 weeks

**Success Metric:** Integration live with at least one customer

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-sc-3: Build second procurement integration

**What:** Expand integration coverage to second major system.

**Why:** Multiple integrations expand addressable market.

**Builds On:** First integration learnings

**Timeline:** 6-10 weeks

**Success Metric:** Second integration live

**Priority:** P3 | **Effort:** High | **Impact:** High

#### s-sc-4: Pilot upstream recommendations

**What:** Test recommendations that go beyond the customer to their suppliers: "Tell your distributor to reduce lettuce orders by 15%."

**Why:** Upstream impact is where Mill influences the entire supply chain.

**Builds On:** Integration, supplier data

**Timeline:** 3-6 months of piloting

**Success Metric:** At least one customer acting on upstream recommendations

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-sc-5: Prove supply chain cost reduction

**What:** Document verified case where Mill recommendations reduced costs across the supply chain, not just at the customer level.

**Why:** Supply chain impact is Mill's endgame—influencing the entire food system.

**Builds On:** Upstream pilots

**Timeline:** 6-12 months after pilots start

**Success Metric:** Customer-verified supply chain savings documented

**Priority:** P2 | **Effort:** High | **Impact:** High

#### s-sc-6: Package supply chain product

**What:** Turn supply chain capabilities into a distinct product offering: "Mill Supply Chain Intelligence" or similar.

**Why:** Product packaging enables dedicated sales motion.

**Builds On:** Proven supply chain impact

**Timeline:** 4-8 weeks after proof

**Success Metric:** Supply chain product launched; first sale

**Priority:** P3 | **Effort:** High | **Impact:** High

---

## Tracking Progress

### Mission Control

Progress against this roadmap is tracked in real-time via [Mission Control](https://gavinpola.github.io/mill-ai-workflows/mission-control.html), an interactive visualization of all 220 tasks across the five pillars.

- Zoom in to explore: from pillars to subgoals to individual tasks
- Circle size indicates task impact (bigger = higher impact)
- Progress rings show completion percentage at each level
- Completed tasks have a green checkmark

### Priority Rebalance Summary

| Priority | Old Count | New Count | Change |
|----------|-----------|-----------|--------|
| P0 | 76 | ~25 | -51 |
| P1 | 87 | ~70 | -17 |
| P2 | 57 | ~75 | +18 |
| P3 | 0 | ~50 | +50 |

The previous task list had too many P0s, which meant nothing was truly prioritized. This revision focuses P0 on genuine blockers and milestones.

---

## Appendix: Task Summary by Pillar

| Pillar | Subgoals | Tasks | P0 | P1 | P2 | P3 | Completed |
|--------|----------|-------|----|----|----|----|-----------|
| Commercial Autonomy | 4 | 42 | 5 | 22 | 12 | 3 | 3 |
| AI Leverage | 5 | 47 | 10 | 25 | 9 | 3 | 0 |
| Data Precision | 4 | 52 | 8 | 18 | 16 | 10 | 4 |
| Outcome Delivery | 4 | 37 | 5 | 16 | 12 | 4 | 0 |
| Scale Effects | 5 | 41 | 1 | 9 | 20 | 11 | 0 |
| **TOTAL** | **22** | **219** | **29** | **90** | **69** | **31** | **7** |

---

*This document is a living roadmap. It will evolve as we learn from execution.*

*Last updated: 2026-03-06*
