# Mill Deck Visual Design System

## Brand Identity Merger: Mill + Partner

### Philosophy
Every partner deck should feel like a natural collaboration - Mill's minimalist sophistication meets the partner's brand energy. BCG-style substance over decoration.

---

## Color System

### Mill Core Palette
```css
--mill-black: #000000;           /* Primary text */
--mill-charcoal: #1a1a1a;        /* Headlines */
--mill-gray: #4a4a4a;            /* Body text */
--mill-light-gray: #888888;      /* Secondary text */
--mill-green: #303803;           /* Earthy green - primary accent */
--mill-sage: #525856;            /* Neutral sage */
--mill-cream: #FAFAF8;           /* Background accent */
--mill-white: #FFFFFF;           /* Clean white */
```

### Partner Integration (Example: Costco)
```css
--partner-primary: #E31837;      /* Costco Red - for emphasis */
--partner-secondary: #005DAA;    /* Costco Blue - for callouts */
```

### Semantic Colors
```css
--highlight-bg: rgba(48, 56, 3, 0.08);   /* Mill green at 8% */
--callout-bg: rgba(227, 24, 55, 0.06);   /* Partner red at 6% */
--success: #27ae60;                       /* Green for positive metrics */
--caution: #f39c12;                       /* Amber for warnings */
```

---

## Typography

### Font Stack
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Scale (BCG Two-Size Rule)
- **Headlines (H1):** 56px / 700 weight / -0.02em tracking
- **Section Titles (H2):** 44px / 600 weight / -0.01em tracking
- **Subtitles (H3):** 28px / 600 weight / normal
- **Body Large:** 24px / 400 weight / 0.01em tracking
- **Body:** 20px / 400 weight / normal
- **Caption/Source:** 14px / 400 weight / 0.02em tracking

### Title Writing Rules
BCG Pyramid Principle:
- Slide titles should be **complete sentences** that convey the key insight
- If you read only the titles, the story should be clear
- Example: Instead of "ROI Analysis", use "Mill delivers 8-12 month payback with 3-5x Year 1 ROI"

---

## Layout System

### Slide Dimensions
```css
width: 1920px;
height: 1080px;  /* 16:9 */
```

### Margins & Safe Zones
```css
--margin-outer: 80px;        /* Outer margin */
--margin-content: 120px;     /* Content start from edges */
--margin-bottom: 100px;      /* Bottom for footnotes */
```

### Grid System
- 12-column grid
- 24px gutters
- Content typically spans 10 columns (centered)

---

## Component Library

### 1. Headline Statement Box
```css
.headline-statement {
  background: var(--mill-cream);
  border-left: 4px solid var(--mill-green);
  padding: 32px 40px;
  font-size: 28px;
  font-weight: 500;
  color: var(--mill-charcoal);
}
```

### 2. Stat Block
```css
.stat-block {
  text-align: center;
  padding: 40px;
}
.stat-number {
  font-size: 80px;
  font-weight: 800;
  color: var(--mill-green);
  line-height: 1;
  letter-spacing: -0.03em;
}
.stat-label {
  font-size: 16px;
  font-weight: 500;
  color: var(--mill-gray);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-top: 12px;
}
```

### 3. Comparison Table
```css
.comparison-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}
.comparison-table th {
  background: var(--mill-charcoal);
  color: white;
  padding: 16px 24px;
  font-weight: 600;
  text-align: left;
}
.comparison-table td {
  padding: 20px 24px;
  border-bottom: 1px solid rgba(0,0,0,0.08);
}
.comparison-table tr:hover {
  background: var(--highlight-bg);
}
```

### 4. Callout Box (Partner Accent)
```css
.callout-box {
  background: var(--callout-bg);
  border-radius: 8px;
  padding: 24px 32px;
  border-left: 3px solid var(--partner-primary);
}
.callout-box .callout-label {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--partner-primary);
  margin-bottom: 8px;
}
```

### 5. Timeline
```css
.timeline {
  display: flex;
  position: relative;
  padding: 60px 0;
}
.timeline::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 80px;
  right: 80px;
  height: 2px;
  background: linear-gradient(90deg, var(--mill-green), var(--partner-secondary));
}
.timeline-node {
  flex: 1;
  text-align: center;
}
.timeline-marker {
  width: 48px;
  height: 48px;
  background: white;
  border: 3px solid var(--mill-green);
  border-radius: 50%;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  color: var(--mill-green);
}
```

### 6. Source Footnote
```css
.source-footnote {
  position: absolute;
  bottom: 40px;
  left: 80px;
  right: 80px;
  font-size: 12px;
  color: var(--mill-light-gray);
  border-top: 1px solid rgba(0,0,0,0.1);
  padding-top: 12px;
}
```

### 7. Circular Flow Diagram
```css
.circular-flow {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
}
.flow-node {
  width: 160px;
  height: 160px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: var(--mill-cream);
  border: 2px solid var(--mill-green);
  transition: all 0.3s ease;
}
.flow-node.active {
  background: var(--mill-green);
  color: white;
}
.flow-arrow {
  font-size: 32px;
  color: var(--mill-green);
}
```

---

## BCG-Style Best Practices

### 1. Squint Test
Every slide should pass the squint test - key message visible when squinting.

### 2. One Idea Per Slide
Each slide conveys exactly one message. The title IS the message.

### 3. Strategic Color
- Use color sparingly to highlight key insights
- Maximum 2 accent colors per slide
- Numbers that matter get color treatment

### 4. Data Labeling
- Labels directly on/near chart elements
- No legends requiring back-and-forth reading
- Round numbers for readability (say "~$135M" not "$134,872,500")

### 5. Footnotes Build Trust
- Every stat needs a source
- Format: "Source: [Publisher], [Year]. [Methodology note if relevant]"

### 6. White Space is Information
- Let content breathe
- Crowded slides = unclear thinking
- If it doesn't fit, it's two slides

---

## Animation Guidelines

### Allowed Transitions
- `fade` - for all slide transitions
- `fadeIn` - for fragment reveals
- No slide, zoom, or convex

### Fragment Timing
- 300ms duration
- 50ms stagger for lists
- Never autoplay - presenter controls pace

---

## Cover Slide Template

```
+----------------------------------------------------------+
|                                                          |
|                                                          |
|        [PARTNER LOGO]  +  [MILL LOGO]                   |
|                                                          |
|        Title of Presentation                             |
|        Subtitle explaining the value proposition         |
|                                                          |
|                                                          |
|                                                          |
|        Month Year                                        |
|                                                          |
+----------------------------------------------------------+
```

---

## Section Divider Template

```
+----------------------------------------------------------+
|                                                          |
|                                                          |
|                                                          |
|        01                                                |
|        SECTION TITLE                                     |
|        Brief description of what this section covers     |
|                                                          |
|                                                          |
|                                                          |
+----------------------------------------------------------+
```

---

## Quality Checklist

Before finalizing any deck:

- [ ] All titles are complete sentences with insights
- [ ] Color used strategically (not decoratively)
- [ ] Every stat has a source footnote
- [ ] Squint test passed on all slides
- [ ] Maximum 2 font sizes in body content
- [ ] Sufficient white space
- [ ] Partner brand colors correctly applied
- [ ] No orphaned words in titles
- [ ] Consistent capitalization
- [ ] Transitions set to fade only
