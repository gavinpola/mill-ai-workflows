# Email to Harry - Draft

**Subject:** Re: Final Steps + Some Weekend Prototyping

---

Harry,

Thanks again for the conversation yesterday—really appreciated the time with the team.

Flight back gave me some time to think, and despite terrible wifi, I couldn't help but prototype something I've been noodling on. Figured I'd share it while it's fresh.

## What I Built (in a few hours on the plane)

I spun up a multi-agent AI workflow system that demonstrates what reusable automation could look like for Mill's commercial operations:

**See it live:** https://gavinpola.github.io/mill-ai-workflows/

The system:
- Researches targets and scores them using a MECE framework
- Generates tailored marketing decks with audience-specific variants (Sustainability, Procurement, CFO)
- Self-reviews through a "Harry" persona reviewer (yes, I built a version of you)
- Creates data dashboards from customer data
- Monitors execution through a terminal dashboard I'm calling "Jarvis"

**Deliverables generated:**
- Costco partnership deck (13 slides, consistent format, story-driven with outcome-based positioning)
- 3 audience variants of the same deck
- Camera/CV architecture deep-dive (interactive explorer)
- Outcome-based pricing strategy doc (the "data piece" you asked about)
- Target ranking analysis using MECE scoring

Total build time: ~3 hours. The point isn't that these are perfect—it's that this kind of output can be generated quickly and iterated on, and the workflows are reusable.

---

## On the Data Piece

You're absolutely right that data is the massive value driver. Here's how I'd think about approaching it:

**The Core Framing Shift:**
Don't sell "food waste visibility"—sell "procurement waste eliminated."

That's the unlock. Visibility is a cost center. Savings is an investment with measurable ROI. When you walk into a CFO conversation and say "we guarantee procurement savings, and we've aligned our pricing so we only profit when you do"—that's a fundamentally different conversation than "here's a dashboard for your sustainability report."

**Pricing Model:**
I'd recommend a hybrid approach (this is what 73% of outcome-based SaaS companies use):
- **Base subscription:** Covers the platform, implementation, support
- **Outcome bonus:** Tied to verified procurement savings above an agreed baseline

This balances your revenue predictability with customer alignment. You're not carrying all the risk, but you are sharing in the upside.

**The Attribution Challenge:**
The trickiness you mentioned around "figuring out attribution" is real but solvable. The key is establishing baseline methodology *before* deployment:

1. Capture 60-90 days of waste data pre-intervention (type, volume, timing)
2. Use market benchmarks for comparable operations
3. Measure the same metrics post-Mill, adjusted for confounders (price inflation, menu changes, seasonality)
4. Joint validation process with the customer

Document the methodology upfront and 60%+ of post-hoc disputes go away.

**What to Invest in Today:**

| Area | Priority Investment |
|------|---------------------|
| **Product** | Baseline capture UX, attribution dashboard |
| **Engineering** | Savings measurement pipeline with audit trail |
| **GTM** | Sales training on "shared risk" conversations, case studies with clear baseline→result methodology |

**Go-to-Market Without Overpromising:**
- Lead with conservative estimates (2-4% food cost savings, not "up to 10%")
- Be transparent about variables: "Results depend on baseline accuracy, staff engagement, menu consistency"
- Tiered guarantees based on customer commitment level

The full analysis is here: [Outcome-Based Pricing Strategy](https://gavinpola.github.io/mill-ai-workflows/outputs/strategy/outcome_based_pricing_strategy.html)

---

This is definitely not buttoned up, but hopefully directionally interesting. Happy to go deeper on any of it when I'm back.

Looking forward to hearing the team's feedback from yesterday.

Gavin

---

**P.S.** The "Harry reviewer" persona in the system gave the Costco deck a 6.5/10 on first pass and sent it back for revisions. Apparently I built a tough critic.
