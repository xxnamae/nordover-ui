# Typography System — Nordover

**Status:** Complete  
**Package:** `tokens-web.css` and `tokens-app.css`

## Overview

Nordover typography uses Inter Variable font with a fluid, responsive type scale. Web and app packages use the same font families but different base sizes and weight strategies.

---

## Font Families

### Web Package (Editorial)

```css
--font-sans: "Inter Variable", "Inter Fallback", system-ui, sans-serif;
--font-display: "Inter Tight Variable", "Inter Tight Fallback", "Inter Variable", system-ui, sans-serif;
--font-mono: ui-monospace, "SF Mono", "Menlo", "Cascadia Code", monospace;
```

- **Display font**: Inter Tight (tighter default spacing, better for headlines)
- **Body font**: Inter Variable (generous x-height, better for reading)
- **Mono font**: System monospace stack (code blocks, data display)

### Loading Inter Fonts

```html
<link rel="preconnect" href="https://rsms.me">
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
```

If offline or restricted: browsers fall back to system fonts (Arial, San Francisco) with `size-adjust` (zero layout shift).

---

## Type Scale

### Web Package (16px Base, 1.2–1.333 Ratio)

Fluid scaling with `clamp()` allows responsive sizing without media queries.

```css
:root {
  --text-xs: 0.75rem;     /* 12px, static */
  --text-sm: 0.875rem;    /* 14px, static */
  --text-base: 1rem;      /* 16px base */
  
  /* Fluid scaling: min + (preferred - min) * (vw / available-range) */
  --text-lg: clamp(1.125rem, 1.089rem + 0.18vw, 1.25rem);       /* 18–20px */
  --text-xl: clamp(1.25rem, 1.18rem + 0.36vw, 1.5rem);          /* 20–24px */
  --text-2xl: clamp(1.5rem, 1.36rem + 0.71vw, 2rem);            /* 24–32px */
  --text-3xl: clamp(1.875rem, 1.66rem + 1.07vw, 2.625rem);      /* 30–42px */
  --text-4xl: clamp(2.25rem, 1.89rem + 1.79vw, 3.5rem);         /* 36–56px */
  --text-5xl: clamp(2.75rem, 2.25rem + 2.5vw, 4.5rem);          /* 44–72px */
  --text-6xl: clamp(3.25rem, 2.54rem + 3.57vw, 5.75rem);        /* 52–92px */
  --text-7xl: clamp(3.75rem, 2.68rem + 5.36vw, 7.5rem);         /* 60–120px */
  --text-8xl: clamp(4.5rem, 2.93rem + 7.86vw, 10rem);           /* 72–160px */
}
```

**Mobile (320px) → Desktop (1920px)** = smooth responsive scaling

### App Package (14px Base, Static Scale)

For data-dense interfaces, app uses fixed sizes:

```css
:root {
  --text-2xs: 0.625rem;   /* 10px, ultra-small labels */
  --text-xs: 0.75rem;     /* 12px */
  --text-sm: 0.875rem;    /* 14px */
  --text-base: 0.875rem;  /* 14px base (more compact) */
  --text-lg: 1rem;        /* 16px */
  --text-xl: 1.125rem;    /* 18px */
  --text-2xl: 1.25rem;    /* 20px */
  --text-3xl: 1.5rem;     /* 24px */
  --text-4xl: 1.875rem;   /* 30px */
  --text-5xl: 2.25rem;    /* 36px */
}
```

---

## Font Weight System

### Web Package (Variable Font)

Weights are tuned for Inter Variable font at specific sizes:

```css
--fw-display-xl: 380;   /* Mega headline: 72px+, very thin */
--fw-display-lg: 400;   /* Large headline: 52px+, thin */
--fw-display-md: 420;   /* Medium headline: 30–36px, light */
--fw-heading-lg: 440;   /* Section heading: 24–30px, light-medium */
--fw-heading-md: 480;   /* Subsection: 20–24px, medium */
--fw-heading-sm: 500;   /* Label: 16–20px, medium */
--fw-body: 400;         /* Body text: default, readable */
--fw-body-sm: 520;      /* Small body: 12–14px, slightly heavier */
--fw-eyebrow: 600;      /* Label, tag, badge: uppercase, bold */
--fw-caption: 520;      /* Caption: 12px, slightly heavier */

/* Standard weights for reference */
--fw-normal: 400;
--fw-medium: 500;
--fw-semibold: 600;
--fw-bold: 700;
```

**Philosophy:** Larger text uses lighter weights (380–420) for elegance; smaller text uses heavier weights (520–700) for clarity.

### App Package

Similar strategy but optimized for compact data:

```css
--fw-display-lg: 420;   /* Smaller max than web */
--fw-heading-lg: 480;   /* Medium-heavy for emphasis */
--fw-body: 400;
--fw-body-sm: 500;      /* Slightly heavier for small text */
```

---

## Line Height System

```css
--leading-none: 0.9;      /* Ultra-tight (display only) */
--leading-tight: 1.1;     /* Headlines: 18–24px text */
--leading-snug: 1.25;     /* Subheading: 20–30px text */
--leading-normal: 1.6;    /* Body text: optimal readability */
--leading-relaxed: 1.75;  /* Long-form: 14–16px text */
```

**WCAG AA Requirement:** Minimum 1.5× line-height for body text. Nordover uses 1.6 (120–130% gap above text).

---

## Letter Spacing

```css
--tracking-tighter: -0.04em;  /* Display: tighten large text */
--tracking-tight: -0.02em;    /* Heading: subtle tightening */
--tracking-normal: 0;         /* Body: no adjustment */
--tracking-wide: 0.01em;      /* Labels: subtle spacing */
--tracking-widest: 0.08em;    /* All-caps: strong spacing */
```

---

## Semantic Typography Classes

### Display & Heading Classes

```html
<h1 class="t-display-xl">Main Headline</h1>
<h2 class="t-display-lg">Page Title</h2>
<h3 class="t-display-md">Section Hero</h3>
<h4 class="t-heading-lg">Section Title</h4>
<h5 class="t-heading-md">Subsection</h5>
<h6 class="t-heading-sm">Label</h6>
```

**CSS:**
```css
.t-display-xl {
  font-family: var(--font-display);
  font-size: var(--text-8xl);
  font-weight: var(--fw-display-xl);  /* 380 */
  line-height: var(--leading-none);   /* 0.9 */
  letter-spacing: -0.04em;
}

.t-display-lg {
  font-family: var(--font-display);
  font-size: var(--text-6xl);
  font-weight: var(--fw-display-lg);  /* 400 */
  line-height: 1.0;
  letter-spacing: -0.03em;
}

.t-heading-lg {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: var(--fw-heading-lg);  /* 440 */
  line-height: 1.2;
  letter-spacing: -0.02em;
}
```

### Body & Label Classes

```html
<p class="t-body-lg">Large paragraph</p>
<p class="t-body">Normal paragraph</p>
<p class="t-body-sm">Small detail</p>
<p class="t-eyebrow">UPPERCASE LABEL</p>
<p class="t-caption">Fine print</p>
```

**CSS:**
```css
.t-body-lg { font-size: var(--text-lg); line-height: var(--leading-normal); }
.t-body { font-size: var(--text-base); line-height: var(--leading-normal); }
.t-body-sm { font-size: var(--text-sm); font-weight: var(--fw-body-sm); }
.t-eyebrow {
  font-size: var(--text-xs);
  font-weight: var(--fw-eyebrow);  /* 600 */
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
}
.t-caption { font-size: var(--text-xs); font-weight: var(--fw-caption); }
```

---

## Weight Strategy for Different Sizes

### Display (60px+)

```css
font-size: var(--text-6xl);      /* 52–92px (web) or 52px (app) */
font-weight: var(--fw-display-lg); /* 400 — thin for elegance */
letter-spacing: -0.03em;         /* tighten */
```

**Rationale:** Large text is visually heavy; lighter weight prevents bulk.

### Heading (24–30px)

```css
font-size: var(--text-2xl);
font-weight: var(--fw-heading-md); /* 480 — medium */
letter-spacing: -0.02em;
```

**Rationale:** Medium weight provides visual hierarchy without excess weight.

### Body (14–16px)

```css
font-size: var(--text-base);
font-weight: var(--fw-body); /* 400 — normal */
line-height: var(--leading-normal); /* 1.6 */
```

**Rationale:** Standard weight for readability; increased line-height helps scanning.

### Label (10–12px)

```css
font-size: var(--text-xs);
font-weight: var(--fw-eyebrow); /* 600 — bold */
text-transform: uppercase;
letter-spacing: var(--tracking-widest);
```

**Rationale:** Small text needs weight to remain readable; spacing aids distinction.

---

## Readable Text Sizing

### Web Package Defaults

| Purpose | Class | Size (Mobile) | Size (Desktop) | Weight | Line-height |
|---------|-------|---------------|----------------|--------|-------------|
| Page title | `.t-display-lg` | 52px | 92px | 400 | 1.0 |
| Section | `.t-heading-lg` | 24px | 42px | 440 | 1.2 |
| Paragraph | `.t-body` | 16px | 16px | 400 | 1.6 |
| Label | `.t-eyebrow` | 12px | 12px | 600 | 1.0 |

### App Package Defaults

| Purpose | Class | Size | Weight | Line-height |
|---------|-------|------|--------|-------------|
| Heading | `.t-heading-lg` | 24px | 480 | 1.3 |
| Body | `.t-body` | 14px | 400 | 1.6 |
| Small | `.t-body-sm` | 12px | 500 | 1.5 |

---

## Font-Variant Numeric

For tabular data (numbers should align):

```css
font-variant-numeric: tabular-nums;
```

Applied to:
- `.data-table` (price, date columns)
- `.price-card .price-val` (pricing display)
- Code blocks

---

## Fluidity Explained

### How `clamp()` Works

```
clamp(MIN, PREFERRED, MAX)
```

**Example:**
```css
--text-2xl: clamp(1.5rem, 1.36rem + 0.71vw, 2rem);
```

- At 320px viewport: `1.5rem` (24px) — never smaller
- At 1920px viewport: `2rem` (32px) — never larger
- In between: smoothly interpolates based on `0.71vw`

**Result:** No media queries needed; type scales responsively.

---

## Accessibility Requirements

1. **Line-height minimum**: 1.5× for body text (WCAG SC 1.4.8)
   - Nordover uses 1.6× (exceeds requirement)

2. **Letter-spacing**: No compression below -0.05em
   - Ensures readability at all sizes

3. **Text contrast**: All text meets WCAG AA minimum (4.5:1)
   - Verified in `nordover-colors.md`

4. **Large text**: 18px+ (bold) or 24px+ (normal) = 3:1 minimum
   - Nordover maintains 4.5:1 for all text

---

## Real-World Examples

### Blog Article

```html
<article>
  <h1 class="t-display-lg">The Future of Design Systems</h1>
  <p class="t-eyebrow">Published May 30, 2026</p>
  <p class="t-body-lg">Design systems have evolved...</p>
  <p class="t-body">The standardization of components...</p>
</article>
```

### Data Dashboard

```html
<h2 class="t-heading-lg">Q2 Revenue</h2>
<p class="t-body-sm" style="font-variant-numeric: tabular-nums;">
  $2,450,000 (+12% YoY)
</p>
<table class="data-table">
  <tr>
    <td class="t-body-sm">January</td>
    <td class="t-body-sm" style="font-variant-numeric: tabular-nums;">$425,000</td>
  </tr>
</table>
```

### Form Labels

```html
<label for="email" class="t-body-sm">Email Address</label>
<input id="email" type="email" class="form-input" />
<p class="t-caption">We'll never share your email.</p>
```

---

## Migrating from Non-Variable Fonts

If you need to use static font weights instead of Inter Variable:

```css
/* For static Inter fonts */
@font-face {
  font-family: "Inter Static";
  src: url("/fonts/inter-regular.woff2") format("woff2");
  font-weight: 400;
}

@font-face {
  font-family: "Inter Static";
  src: url("/fonts/inter-semibold.woff2") format("woff2");
  font-weight: 600;
}

--font-sans: "Inter Static", system-ui, sans-serif;

/* Adjust weights to nearest static option */
--fw-display-xl: 400; /* was 380 → round up */
--fw-heading-md: 600; /* was 480 → round to 600 */
```

---

## References

- `tokens-web.css`: Complete type scale definitions
- `tokens-app.css`: App-optimized type scale
- `components-web.css`: Semantic class definitions (`.t-display-*`, `.t-heading-*`, etc.)
- [Inter Font](https://rsms.me/inter/) — variable font download
- [WCAG 2.1 SC 1.4.8 Line Spacing](https://www.w3.org/WAI/WCAG21/Understanding/line-spacing.html)
