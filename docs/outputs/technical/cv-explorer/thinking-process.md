# Mill CV Infrastructure: The Thinking Process

**Internal Analysis Document | March 2026**

This document captures the full reasoning process behind our CV infrastructure recommendations. It's meant to show our work and help future decisions build on this analysis.

---

## Starting Point: What Problem Are We Actually Solving?

### The Surface Problem
"How do we identify food waste in commercial kitchens?"

### The Real Problem
**Partial foods don't look like reference images.**

A whole apple is easy to classify. A half-eaten apple with bite marks, browning, and maybe some peanut butter on it? That's what actually gets thrown away. And it looks nothing like the training data.

This is the core accuracy challenge:
- Half-eaten items (bites, tears, cuts)
- Sauce-covered items (gravy, dressing, condiments)
- Mixed items (rice with vegetables, pasta with meat)
- Crushed/compressed items (smashed in serving tray)
- Temperature-altered items (melted, congealed, dried out)

### The Constraint We Almost Missed

Early in analysis, we nearly recommended the **Photo Booth** (a vertical imaging tunnel inside the bin). It solves occlusion beautifully - items fall through and are imaged individually.

But then we caught the critical constraint:

> **Mill's core operation happens inside the bin.**

The bin heats food waste and converts it to compost. Any interior obstruction - a tube, a conveyor, a sieve - interferes with this. The Photo Booth's polycarbonate tunnel would:
- Reduce interior volume
- Block heat distribution
- Possibly melt under operating temperatures
- Require redesigning the core product

This constraint eliminates multiple high-accuracy approaches:
- Photo Booth (tunnel)
- Tumbler (rotating sieve)
- Cascade (mini conveyor)

**Lesson: The best technical solution isn't always the right solution.**

---

## What Features Are Invariant for Partial Foods?

This is the key insight that shaped our recommendation.

When a chicken breast is half-eaten, what changes and what stays the same?

### Things That Change (Unreliable for Classification)
| Feature | Why It's Unreliable |
|---------|---------------------|
| Shape | Bites remove recognizable contours |
| Color (visible) | Sauce, browning, mixing with other foods |
| Texture (visual) | Surface altered by handling, mixing |
| Size | Portions vary wildly |

### Things That Stay the Same (Invariant)
| Feature | Why It Works |
|---------|--------------|
| **Density** | Half a chicken breast still has chicken density |
| **Chemistry** | Protein is protein, carbs are carbs, fat is fat |
| Material composition | NIR spectral signature unchanged by shape |
| Impact dynamics | How it bounces/settles based on mass distribution |

**This is why we recommend sensor fusion.** Vision catches what it can. Weight/density catches what vision misses. Chemistry (NIR) is the nuclear option if needed.

---

## The Approaches: Tiered Analysis

### Tier 1: External, High Impact
These can be implemented without touching the bin interior.

| Approach | Partial Food Help | Why |
|----------|-------------------|-----|
| **Kaleidoscope** | Medium-High | 6 angles catch features invisible from one view |
| **Weighmaster** | High | Density is invariant. Weight signatures validate vision |
| **Fingerprinter (NIR)** | Highest | Chemistry doesn't care about appearance |

### Tier 2: External, Lower Impact
Useful as additional fusion layers but not primary classifiers.

| Approach | Partial Food Help | Why |
|----------|-------------------|-----|
| Listener (acoustic) | Low | Impact sounds help but kitchen is noisy |
| Heat Map (thermal) | Low | Fresh waste is warm, but cold items exist |
| Penetrator (radar) | Low | Sees through pile but can't classify well |
| Polarizer | Low | Cuts glare, niche benefit |

### Tier 3: Interior Modifications (Eliminated)
These have the highest accuracy but conflict with core operations.

| Approach | Why Eliminated |
|----------|----------------|
| Photo Booth | Tube obstructs interior |
| Tumbler | Rotating mechanism in bin |
| Cascade | Conveyor system in bin |

---

## Hybrid Designs Explored

We explored combining approaches in novel ways:

### The Oracle (Kaleidoscope + Weighmaster + NIR)
- Full sensor suite: 6-angle vision + weight + spectral
- Estimated accuracy: 95-99%
- Cost: +35% over baseline
- Verdict: **Overkill for launch.** Save NIR as upgrade path.

### The Economist (Kaleidoscope + Weighmaster)
- Multi-angle vision + weight validation
- Estimated accuracy: 92-97%
- Cost: +7% over baseline ($200)
- Verdict: **Recommended.** Best ROI.

### The Chemist (Baseline + NIR)
- Standard vision + spectral chemistry
- Estimated accuracy: 94-98%
- Cost: +25% over baseline
- Verdict: **Future upgrade.** If Economist doesn't hit targets.

### The Temporal (Weight-Triggered Burst)
- Not a sensor hybrid - a capture strategy
- Load cells trigger burst capture on weight change
- Captures before/during/after states
- Verdict: **Definitely implement.** Better than always-on.

### The Learner (Human-in-the-Loop)
- Low-confidence items flagged for human review
- Humans see 6-angle views + weight data
- Their labels improve the model
- Verdict: **Critical for Phase 1.** How we get from 85% to 95%.

---

## The Staged Deployment Strategy

### Phase 1: Launch Smart, Learn Fast
**Deploy: Kaleidoscope + Weighmaster**

Hardware:
- 6 first-surface mirrors on camera boom (~$50)
- 4 industrial load cells under bin (~$100)
- Signal processing board (~$50)
- Total added cost: ~$200 per unit

Software:
- Multi-angle image processing
- Weight signature extraction
- Sensor fusion model
- **Uncertainty quantification** - know when you don't know

Human-in-the-loop:
- Items with <80% confidence → flagged for review
- Kitchen staff or remote reviewer confirms classification
- Confirmed labels feed back into training

Expected accuracy: **88-93%** at launch, improving to **92-97%** within months.

### Phase 2: Watch the Data

After 3-6 months of operation, analyze:
- Which food categories have lowest accuracy?
- Are failures visual (appearance) or density (weight)?
- What percentage of items need human review?

Key questions:
- If visual failures dominate → consider NIR upgrade
- If density failures dominate → recalibrate weight models
- If human review rate is <5% → system is working

### Phase 3: Data-Driven Hardware Upgrade (If Needed)

Only add NIR spectral imaging if:
- Visual+weight fusion plateaus below 90%
- Specific categories (sauces, mixed dishes) remain problematic
- ROI justifies the +25% hardware cost

**Don't over-engineer at launch.** Let the data tell you what's needed.

---

## Why Not "Always On" Camera?

The original plan was continuous video capture. Problems:

| Issue | Impact |
|-------|--------|
| Data volume | Terabytes per day per site |
| Processing load | Constant GPU utilization |
| Power consumption | Camera/processor always running |
| Missed events | Fast dumps between frames |
| No "before" state | Can't diff what changed |

### Weight-Triggered Burst Capture

Better approach:
1. Load cells detect weight increase (threshold: 50g)
2. Trigger high-speed burst capture (10 fps for 0.5 seconds)
3. Capture includes before/during/after states
4. Only process frames that matter

Benefits:
- 100x less data to process
- Precise timing - never miss a dump
- Before/after diff enables volume tracking
- Lower power consumption
- Can use higher quality captures per event

---

## Why Kaleidoscope Over Multiple Cameras?

We considered multiple discrete cameras (3-4 around the bin). Kaleidoscope wins:

| Factor | Multiple Cameras | Kaleidoscope |
|--------|------------------|--------------|
| Hardware cost | $900-1200 | $50 |
| Calibration | Complex multi-camera | Single camera |
| Synchronization | Required | Inherent (single frame) |
| Maintenance | Multiple failure points | Mirrors are robust |
| Installation | Multiple mounts | Single boom upgrade |

The mirrors are literally just optics. Light physics doesn't fail.

---

## Why Weighmaster As Validation, Not Primary?

Weight alone achieves 55-70% accuracy. Why include it?

Because it catches what vision misses:

| Vision Says | Weight Says | Likely Truth |
|-------------|-------------|--------------|
| "Bread" | Dense impact | Not bread (maybe meat) |
| "Chicken" | Light, scattered | Not chicken (maybe lettuce) |
| "Unknown" | Chicken-weight signature | Probably chicken |

The fusion model uses weight to:
- Validate high-confidence vision classifications
- Override low-confidence vision with strong weight signal
- Flag conflicting signals for human review

Weight is the "lie detector" for vision.

---

## Risk Factors and Mitigations

### Mirror Fouling (Kaleidoscope)
**Risk:** Grease/steam deposits on mirrors reduce image quality.
**Mitigation:**
- Hydrophobic coating on mirrors
- Scheduled cleaning protocol (daily wipe)
- Degradation detection in software (alert when image quality drops)

### Kitchen Vibration (Weighmaster)
**Risk:** Nearby equipment causes weight noise.
**Mitigation:**
- High-pass filtering on weight signal
- Baseline calibration per installation
- Event detection tuned to environment

### Model Drift
**Risk:** Food menu changes over time; model accuracy degrades.
**Mitigation:**
- Continuous learning from human-reviewed labels
- Quarterly model refresh
- Anomaly detection for novel food types

### Human Review Fatigue
**Risk:** Too many items flagged → reviewers disengage.
**Mitigation:**
- Target <10% review rate
- Gamification of review interface
- Prioritize high-value corrections (expensive foods)

---

## Cost Analysis Summary

| Configuration | Added Hardware | Estimated Accuracy | Notes |
|---------------|----------------|-------------------|-------|
| Baseline only | $0 | 85-92% | Single angle, occlusion issues |
| + Kaleidoscope | +$50 | 85-92% (better partial food) | Multi-angle, same compute |
| + Weighmaster | +$150 | +5-10% fusion boost | Validates/corrects vision |
| **Recommended** | **+$200** | **92-97%** | Kaleidoscope + Weighmaster |
| + NIR (future) | +$600 | 95-99% | Only if needed |

ROI: $200 hardware investment pushes accuracy from ~87% average to ~94% average. At scale, this is trivial per-unit cost for significant capability gain.

---

## Final Recommendation

**Launch with Kaleidoscope + Weighmaster.**

- External only (no interior modifications)
- Low cost (+$200/unit)
- High accuracy (92-97% with fusion)
- Weight-triggered capture (not always-on)
- Human-in-the-loop for uncertainty
- Data-driven upgrade path (NIR if needed later)

**Don't over-engineer.** Ship, learn, iterate.

---

*Document generated as part of Mill CV Infrastructure analysis. For questions, contact the systems team.*
