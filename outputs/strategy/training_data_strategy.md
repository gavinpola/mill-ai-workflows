# Mill Training Data Strategy: Deep Dive

## Executive Summary

Mill's CV system doesn't need to solve general food recognition. It needs to solve **food waste recognition in a constrained commercial kitchen environment with multi-modal data**. This is fundamentally easier than the academic problem - but requires a deliberate training data strategy.

**Key Insight:** Mill has three unique advantages that dramatically simplify training:
1. **6-angle Kaleidoscope views** - Humans can label with 85% less ambiguity than single-view
2. **Weight signatures** - Ground truth for density-based validation (chicken weighs like chicken)
3. **Menu context** - Commercial kitchens have predictable, finite menus (50-200 items)

The strategy: Bootstrap fast with synthetic + crowdsource, then build a data flywheel where every deployed bin improves the model.

---

## Part 1: The Problem We're Actually Solving

### What Makes Food Waste Classification Hard

| Challenge | General Food Recognition | Mill's Constrained Problem |
|-----------|-------------------------|---------------------------|
| Partial foods | Extremely hard (half-eaten, sauce-covered) | Hard, but 6-angle views help significantly |
| Dataset bias | Datasets show whole, plated foods | Mill collects actual waste from day 1 |
| Intra-class variation | Unlimited (global cuisines) | Bounded by customer's menu |
| Lighting conditions | Highly variable | Controlled (same LED ring on every bin) |
| Camera angles | Single view typical | 6 simultaneous views standard |
| Ground truth | Visual only | Visual + weight + menu context |

### The Partial Food Problem (Core Challenge)

Academic datasets (Food-101, ISIA Food-500) are heavily biased toward:
- Whole, intact foods
- Professionally plated dishes
- Good lighting and framing

Mill needs to classify:
- Half-eaten chicken breasts with bite marks
- Pasta mixed with sauce and vegetables
- Crushed/scraped food from plates
- Items occluded by other items

**Why this matters:** A model trained on Food-101 achieves 90%+ accuracy on whole foods but drops to 60-70% on partial foods. This is the gap Mill must close.

### Mill's Unfair Advantages

**1. Multi-Angle Views (Kaleidoscope)**
- Human labelers see 6 angles simultaneously
- Reduces labeling ambiguity by ~85% vs. single-view
- Same partial chicken breast might be unrecognizable from above but obvious from the side
- Labeling cost: effectively 6x more information per labeling task

**2. Weight Signatures (Weighmaster)**
- Provides density ground truth independent of appearance
- "This looks uncertain but weighs like chicken" → probably chicken
- Enables automatic validation of visual predictions
- Creates sensor fusion training signal (vision + weight must agree)

**3. Constrained Menu Space**
- A Costco food court has ~50 items
- A corporate cafeteria has ~100-200 items per week
- This is NOT open-domain food recognition
- Model only needs to recognize what's on that customer's menu

**4. Controlled Environment**
- Same bin design everywhere (consistent camera geometry)
- Same LED illumination ring (consistent lighting)
- Same weight-triggered capture timing (consistent image quality)
- Dramatically reduces domain shift vs. consumer photos

**5. Before/After Capture**
- Weight-triggered burst captures state before AND after dump
- Enables diff-based analysis (what changed?)
- Volume estimation from before/after comparison
- Training signal: the "new stuff" is what we need to classify

---

## Part 2: The Training Data Flywheel

### Phase 0: Pre-Launch Bootstrap (Weeks 1-8)

**Goal:** Build initial model capable of ~80% accuracy on common foods before first deployment.

#### Step 1: Seed Dataset (Week 1-2)
- Collect 500 high-quality labeled images per category
- 30 categories initially (most common commercial kitchen waste)
- Total: 15,000 labeled images
- Source: Combination of:
  - Internal collection (photograph actual food waste)
  - Crowdsource (Appen, Scale Remotasks) - $5-10/image
  - Academic datasets (UNIMIB 2015 has actual tray waste)
- **Cost estimate:** $50,000-75,000

**Category Selection (30 initial):**
```
Proteins: Chicken, Beef, Pork, Fish, Eggs, Tofu
Starches: Rice, Pasta, Bread, Potatoes, Fries
Vegetables: Lettuce, Tomatoes, Carrots, Broccoli, Mixed Salad
Fruits: Apples, Oranges, Bananas, Mixed Fruit
Dairy: Cheese, Milk/Cream, Yogurt
Prepared: Pizza, Sandwiches, Burgers, Soup
Other: Coffee Grounds, Condiments/Sauces, Baked Goods
```

#### Step 2: Synthetic Data Augmentation (Week 2-4)
- 3D model 30 food items in Blender
- Generate 1,000 variations each (angle, lighting, plate background)
- Apply domain randomization (simulates Kaleidoscope views)
- **Total: 30,000 synthetic images**
- Mix ratio: 50% real, 50% synthetic for initial training
- **Cost estimate:** $15,000-20,000 (contractor for 3D modeling)

#### Step 3: Aggressive Data Augmentation (Week 3-4)
- Geometric: Rotation ±30°, scaling 0.8-1.2x, perspective transforms
- Photometric: Brightness ±20%, contrast ±15%, saturation ±20%
- Food-specific: Simulate partial occlusion, sauce overlay, crushing
- **Expand 15,000 real → 75,000 augmented**
- Apply more aggressive augmentation to rare categories

#### Step 4: Baseline Model Training (Week 5-6)
- Architecture: EfficientNetB4 or ResNet50 (proven on food)
- Transfer learning: ImageNet → Food-101 → Mill waste dataset
- Train on: 75,000 augmented real + 30,000 synthetic = 105,000 images
- **Expected accuracy: 75-80%** on common foods
- Identify failure modes (which foods does the model get wrong?)

#### Step 5: Failure Mode Analysis (Week 7-8)
- Run model on held-out test set (2,000 images)
- Identify:
  - Low-accuracy categories (need more data)
  - High-confusion pairs (chicken vs. pork, pasta vs. rice)
  - Systematic failures (partial foods, sauce-covered items)
- Use this to prioritize active learning in Phase 1

---

### Phase 1: Launch with Human-in-the-Loop (Months 1-3)

**Goal:** Deploy to first 10-50 bins with active learning loop. Reach 88% accuracy.

#### Confidence-Based Routing

```
Prediction Flow:
┌─────────────────────────────────────────────────────────────┐
│ Food dropped into bin                                       │
│         ↓                                                   │
│ Weight trigger → 0.5s burst capture (6-angle + before/after)│
│         ↓                                                   │
│ Model prediction + confidence score                         │
│         ↓                                                   │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ Confidence > 0.90 → AUTO-ACCEPT (log for spot-check)    │ │
│ │ Confidence 0.70-0.90 → 10% SAMPLE REVIEW                │ │
│ │ Confidence < 0.70 → FULL HUMAN REVIEW                   │ │
│ └─────────────────────────────────────────────────────────┘ │
│         ↓                                                   │
│ Human-reviewed labels → Weekly model retraining             │
└─────────────────────────────────────────────────────────────┘
```

**Why this works:**
- High-confidence predictions (60-70% of volume) require no human effort
- Low-confidence predictions are exactly the training examples we need
- System automatically surfaces the hardest cases for labeling
- Each week, model improves on exactly its failure modes

#### Active Learning Strategy

**Uncertainty Sampling (Primary):**
- Score all predictions by entropy (model uncertainty)
- Top 20% uncertain predictions → human review queue
- This targets exactly where the model is weakest

**Category-Aware Sampling:**
- Track accuracy per food category
- Oversample from low-accuracy categories
- Prevents model from ignoring rare foods

**Disagreement Sampling:**
- When vision says "chicken" but weight signature says "bread" → flag for review
- Multi-modal disagreement is a strong signal of difficult cases

#### Human Labeling Workflow

**Interface Requirements:**
- Show 6-angle Kaleidoscope views side-by-side
- Show weight signature graph (impact curve)
- Show before/after images
- Pre-fill model's best guess (humans confirm or correct)
- Allow "uncertain" option (routes to expert)

**Labeler Capacity Planning:**
- ~500 reviews/day needed for 50 bins
- 2-3 full-time labelers OR distributed across kitchen staff
- Consider gamification: staff compete on labeling accuracy

**Quality Assurance:**
- 10% of labels get double-reviewed
- Track inter-annotator agreement (target: >95%)
- Flag inconsistent labelers for retraining

#### Weekly Retraining Cycle

```
Every Sunday Night:
1. Pull all human-reviewed labels from past week
2. Combine with existing training set
3. Retrain model (fine-tune, not from scratch)
4. Evaluate on held-out test set
5. If accuracy improved → deploy new model Monday AM
6. If accuracy regressed → investigate, manual review
```

**Expected Volume (50 bins):**
- ~100 waste events per bin per day
- ~5,000 events/day total
- ~25% flagged for review = 1,250 reviews/day
- ~35,000 new labeled examples per month

---

### Phase 2: Scaling the Flywheel (Months 4-12)

**Goal:** Scale to 500+ bins. Reach 92% accuracy. Reduce human review to <10%.

#### The Data Flywheel Effect

```
More Bins Deployed
       ↓
More Waste Events Captured
       ↓
More Edge Cases Surface (via uncertainty sampling)
       ↓
More Training Data (from human reviews)
       ↓
Better Model Accuracy
       ↓
Higher Customer Satisfaction
       ↓
More Bins Sold
       ↓
[Cycle Repeats]
```

**By month 12 (500 bins):**
- 50,000 waste events/day
- ~5,000 human reviews/day (10% rate)
- ~1.5M new labeled examples accumulated
- Model accuracy: 92%+ on common foods

#### Menu-Aware Classification

**Key Optimization:** Mill knows each customer's menu.

```
Instead of: "Classify this into 1,000 possible foods"
Do this:    "Classify this into the 75 foods on Costco's menu"
```

**Implementation:**
- Each bin has a menu configuration
- Model outputs constrained to that customer's items
- Dramatically reduces confusion between similar foods
- Enables customer-specific fine-tuning

#### Per-Customer Fine-Tuning

After 30 days of deployment at a site:
1. Collect 1,000+ labeled examples specific to that kitchen
2. Fine-tune base model on site-specific data
3. Deploy site-specific model to those bins
4. Track per-site accuracy (should exceed base model)

**Why this works:**
- A Costco food court chicken looks different from a Marriott cafeteria chicken
- Site-specific models capture local presentation/preparation patterns
- Still benefits from shared base model (transfer learning)

#### Reducing Human Review Load

**Month 1-3:** 25% of predictions reviewed
**Month 4-6:** 15% of predictions reviewed
**Month 7-12:** <10% of predictions reviewed

How we get there:
- Model improves → confidence scores increase → fewer low-confidence predictions
- Implement "auto-confirm" for highly-confident repeat patterns
- Kitchen staff quick-confirm obvious items (1-tap interface)

---

### Phase 3: Advanced Optimizations (Year 2+)

**Goal:** 95%+ accuracy. Human review only for novel items.

#### Federated Learning (Privacy-Preserving)

For customers who won't share raw images:
1. Model runs on-bin (Jetson Orin NX)
2. Human corrections update local model only
3. Model deltas (not images) sent to Mill central
4. Central aggregates updates from all bins
5. Improved global model pushed back to bins

**Benefits:**
- Images never leave customer premises
- Still benefits from fleet-wide learning
- Addresses enterprise privacy concerns

#### Synthetic Data for Edge Cases

Use diffusion models to generate training data for rare scenarios:
- Half-eaten versions of all menu items
- Various sauce coverage levels
- Different crushing/mixing states
- Unusual lighting conditions

**Cost:** ~$1-2 per synthetic image
**Value:** Addresses long-tail without waiting for real examples

#### Novel Food Detection

When model encounters food it's never seen:
1. Flag as "unknown" (high uncertainty, no good class match)
2. Route to expert labeler
3. Expert creates new category if warranted
4. Retrain model to include new food
5. Push update to all bins

**This prevents model from confidently misclassifying new menu items.**

---

## Part 3: The Partial Food Problem (Deep Dive)

### Why Partial Foods Are Hard

Standard food classifiers are trained on images like:
- A whole apple on a plate
- A complete pizza slice
- An intact burger

But waste classification sees:
- Half an apple with bite marks and browning
- Pizza crust with some cheese remnants
- Burger bun with a bite taken out and ketchup smeared

**The visual features that make a "chicken breast" recognizable are often destroyed by partial consumption.**

### Mill's Multi-Modal Advantage

| Modality | What It Captures | Partial Food Benefit |
|----------|------------------|---------------------|
| **Vision (6-angle)** | Color, texture, shape | Some angles preserve recognizable features |
| **Weight signature** | Density, mass, impact dynamics | Density unchanged by partial consumption |
| **Before/after diff** | What was added to the bin | Volume change helps estimate quantity |
| **Menu context** | What's possible | Constrains classification space |

**Sensor Fusion Training:**

Train the model to use ALL modalities:
```
Input: [6 images, weight signature, menu constraints]
Output: [food_class, confidence, estimated_mass]

Loss Function:
- Cross-entropy on food_class (vision-based)
- MSE on estimated_mass (weight-based)
- Consistency penalty when vision and weight disagree
```

This forces the model to learn that:
- "When uncertain visually, trust weight signature"
- "When weight suggests chicken but vision says bread, flag for review"

### Labeling Partial Foods

**Challenge:** Partial foods are ambiguous even for humans.

**Solution:** Multi-annotator consensus + rich context

For each uncertain image:
1. Show 6-angle views + weight signature + before/after
2. Have 3 labelers independently classify
3. If 3/3 agree → accept label
4. If 2/3 agree → accept with lower confidence weight
5. If all 3 disagree → expert review + create labeling guideline

**Labeling Guidelines (Examples):**
- "Chicken breast with sauce" → label as Chicken (primary protein)
- "Pizza crust only (no toppings)" → label as Bread (if >80% crust)
- "Mixed pasta and vegetables" → label as Pasta (primary starch)
- "Unidentifiable mush" → label as Mixed/Unknown

---

## Part 4: Implementation Roadmap

### Milestone 1: Bootstrap Dataset (Weeks 1-8)
- [ ] Define 30 initial food categories
- [ ] Collect 500 images per category (crowdsource + internal)
- [ ] Generate synthetic data (3D models + rendering)
- [ ] Apply augmentation pipeline
- [ ] Train baseline model
- [ ] Evaluate and document failure modes

**Deliverable:** Baseline model with 75-80% accuracy on common foods

### Milestone 2: HITL Infrastructure (Weeks 9-12)
- [ ] Build labeling interface (6-angle views, weight signature display)
- [ ] Implement confidence-based routing
- [ ] Set up weekly retraining pipeline
- [ ] Hire/train labeling team (2-3 people or contractor)
- [ ] Deploy to 10 beta bins

**Deliverable:** Working HITL loop with weekly model updates

### Milestone 3: Active Learning Loop (Months 3-6)
- [ ] Implement uncertainty sampling
- [ ] Add category-aware sampling
- [ ] Add multi-modal disagreement detection
- [ ] Scale to 50+ bins
- [ ] Reduce human review rate to <15%

**Deliverable:** 88% accuracy, sustainable labeling workflow

### Milestone 4: Flywheel Scaling (Months 6-12)
- [ ] Scale to 500+ bins
- [ ] Implement menu-aware classification
- [ ] Per-customer fine-tuning pipeline
- [ ] Reduce human review rate to <10%

**Deliverable:** 92% accuracy, efficient at scale

### Milestone 5: Advanced Features (Year 2)
- [ ] Federated learning for privacy-sensitive customers
- [ ] Synthetic data generation for edge cases
- [ ] Novel food detection and auto-categorization
- [ ] Ingredient-level breakdown (future capability)

**Deliverable:** 95%+ accuracy, minimal human intervention

---

## Part 5: Cost Model

### Bootstrap Phase (Pre-Launch)

| Item | Cost |
|------|------|
| Seed dataset collection (15,000 images) | $50,000-75,000 |
| 3D modeling for synthetic data | $15,000-20,000 |
| ML engineering (model development) | Internal or $50,000-100,000 |
| Labeling interface development | Internal or $20,000-30,000 |
| **Total Bootstrap** | **$135,000-225,000** |

### Ongoing Operations (Per Year at Scale)

| Item | Cost (500 bins) |
|------|------|
| Human labelers (3 FTE at $50k) | $150,000 |
| Labeling platform (Labelbox/Encord) | $25,000-50,000 |
| Cloud compute (training + inference) | $50,000-100,000 |
| **Total Annual** | **$225,000-300,000** |

### Cost Per Bin Economics

At 500 bins:
- $225,000-300,000 / 500 = **$450-600 per bin per year** for ML operations
- This is ~15-20% of estimated unit cost
- Reduces as fleet scales (fixed costs spread over more units)

At 5,000 bins:
- Fixed costs ~$500,000/year
- **$100 per bin per year** for ML operations
- The data flywheel becomes extremely cost-efficient

---

## Part 6: Key Metrics to Track

### Model Performance
- **Overall accuracy** (target: 85% → 92% → 95%)
- **Per-category accuracy** (flag categories below 80%)
- **Partial food accuracy** (the hard metric - track separately)
- **Average confidence score** (should increase over time)

### Labeling Efficiency
- **Human review rate** (target: 25% → 15% → <10%)
- **Labels per hour per labeler** (benchmark: 100-200)
- **Inter-annotator agreement** (target: >95%)
- **Time from correction to model deployment** (target: <7 days)

### Data Flywheel Health
- **Cumulative labeled images** (should grow exponentially with bins)
- **Novel food detection rate** (how often do we see new items?)
- **Per-customer model lift** (does fine-tuning help?)

### Business Impact
- **Classification disputes** (customer complaints about misclassification)
- **Trust score** (do customers rely on the data for procurement?)
- **Expansion rate** (are existing customers adding bins?)

---

## Summary: The Mill Training Data Advantage

Mill isn't solving general food recognition. Mill is solving:

> "Classify food waste in a controlled environment with 6-angle views, weight signatures, and known menu constraints."

This is a **dramatically easier problem** than the academic benchmarks suggest.

**The winning strategy:**
1. **Bootstrap fast** with synthetic + crowdsourced data
2. **Deploy early** with human-in-the-loop safety net
3. **Let the flywheel spin** - every bin makes the model better
4. **Use multi-modal fusion** - weight validates vision
5. **Constrain the problem** - menu context narrows classification space

With 500 bins generating 50,000 events/day and systematic human review of edge cases, Mill will have the best food waste classification model in the world within 12 months of launch.

---

## Files to Create

| File | Purpose |
|------|---------|
| `outputs/strategy/training_data_strategy.html` | Interactive strategy document (like CV Explorer) |
| `outputs/strategy/training_data_strategy.md` | Markdown version for reference |

The document should include:
- Executive summary
- Visual flywheel diagram
- Phase-by-phase roadmap
- Cost model with sensitivity analysis
- Metrics dashboard mockup
- Comparison to competitor approaches
