# Spacing System — Nordover

**Status:** Complete  
**Package:** `tokens-web.css` and `tokens-app.css`

## Overview

Nordover's spacing system uses a consistent 4px base (rem-based) for precise, scalable layouts. Spacing tokens are used for:
- **Component padding** (inside buttons, inputs)
- **Component gaps** (between list items, flex gaps)
- **Section spacing** (between major sections)
- **Page padding** (margin around page edges)

---

## Spacing Scale

### Base Units

```css
--space-0: 0;
--space-px: 1px;           /* For hairline borders/gaps */

--space-1: 0.25rem;        /* 4px — micro-spacing */
--space-2: 0.5rem;         /* 8px — tight component gap */
--space-3: 0.75rem;        /* 12px — standard padding */
--space-4: 1rem;           /* 16px — component padding */
--space-5: 1.5rem;         /* 24px — standard gap between components */
--space-6: 2rem;           /* 32px — generous padding */
--space-7: 2.5rem;         /* 40px — large gap */
--space-8: 3rem;           /* 48px — section gap */
--space-10: 4rem;          /* 64px — large section gap */
--space-12: 6rem;          /* 96px — hero section gap */
--space-16: 8rem;          /* 128px — mega spacing */
--space-20: 10rem;         /* 160px — page-level gap */
--space-24: 12rem;         /* 192px — extreme spacing */
--space-32: 16rem;         /* 256px — layout spacing */
--space-40: 20rem;         /* 320px — rare use */
--space-48: 24rem;         /* 384px — rare use */
```

**Ratio:** 1.5× scaling (0.25 → 0.375 → 0.5 → 0.75 → 1 → 1.5 → 2 → ...)

---

## Semantic Spacing Tokens

For common use cases, semantic tokens reduce cognitive load:

```css
/* Component internals */
--gap-tight: var(--space-2);           /* 8px — inside form row, tag list */
--gap-component: var(--space-5);       /* 24px — between list items, flex items */
--gap-section: var(--space-8);         /* 48px — between major sections */

/* Page layout */
--spacing-section: clamp(var(--space-12), 12vw, var(--space-20));
  /* Mobile: 96px, desktop: 160px (responsive) */

--page-padding: clamp(var(--space-5), 4vw, var(--space-8));
  /* Mobile: 24px, desktop: 48px (responsive) */
```

---

## Component-Level Spacing

### Buttons

```css
.btn {
  padding: var(--space-3) var(--space-5);  /* 12px vert, 24px horiz */
}

.btn-sm {
  padding: var(--space-2) var(--space-4);  /* 8px vert, 16px horiz */
}

.btn-lg {
  padding: var(--space-4) var(--space-7);  /* 16px vert, 40px horiz */
}
```

**Rationale:** Size 3 vertical padding (12px) provides comfortable vertical touch target; horizontal padding scales with size.

### Form Inputs

```css
.form-input {
  padding: var(--space-3) var(--space-4);  /* 12px vert, 16px horiz */
  font-size: var(--text-base);
}
```

**Rationale:** Consistent vertical padding (44px minimum height on mobile when including font size).

### Card Padding

```css
.price-card {
  padding: var(--space-6);  /* 32px all sides */
}

.feature-card {
  padding: var(--space-5);  /* 24px all sides */
}

.modal-body {
  padding: var(--space-6);  /* 32px all sides */
}
```

**Rationale:** Larger cards use larger padding for visual hierarchy.

---

## Gap System (Flexbox/Grid)

### Component Gaps

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);  /* 24px between list items */
}

.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--gap-component);  /* 24px between items (both axes) */
  align-items: center;
}

.form-group {
  display: flex;
  gap: var(--space-4);        /* 16px between form items */
  flex-wrap: wrap;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: var(--space-5);        /* 24px grid gap */
}
```

### Tight Gaps (Form Rows, Tag Lists)

```css
.form-group {
  display: flex;
  gap: var(--gap-tight);      /* 8px tight */
  flex-wrap: wrap;
}

.tag-list {
  display: flex;
  gap: var(--gap-tight);      /* 8px between tags */
  flex-wrap: wrap;
}
```

---

## Section-Level Spacing

### Page Layout

```css
.page {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-section);        /* Responsive: 96px → 160px */
  padding-inline: var(--page-padding); /* Responsive: 24px → 48px */
}

.page-section {
  padding-block: var(--spacing-section);
}

.page-content {
  max-width: 64rem;           /* Content width limit */
  margin-inline: auto;        /* Center content */
}
```

### Hero & CTA Sections

```css
.hero-centered {
  padding: var(--space-10) var(--space-6);  /* 64px vert, 32px horiz */
}

.cta-card {
  padding: clamp(var(--space-8), 7vw, var(--space-12)) var(--space-6);
  /* Mobile: 48px, desktop: 96px (responsive) */
}
```

---

## Responsive Spacing with `clamp()`

### Why `clamp()`?

Traditional responsive spacing requires media queries:

```css
/* Old approach (media queries) */
.section { padding: 48px 24px; }
@media (max-width: 768px) { .section { padding: 32px 16px; } }
```

**Problem:** Jumps at breakpoint. Better to scale smoothly:

```css
/* New approach (clamp) */
.section {
  padding: clamp(var(--space-6), 5vw, var(--space-8));
}
/* Mobile (320px): 32px, Desktop (1920px): 48px, smooth transition */
```

### Common `clamp()` Patterns

#### Responsive Page Padding

```css
--page-padding: clamp(
  var(--space-5),    /* min: 24px (mobile) */
  4vw,               /* preferred: 4% of viewport width */
  var(--space-8)     /* max: 48px (desktop) */
);
```

#### Responsive Section Gap

```css
--spacing-section: clamp(
  var(--space-12),   /* min: 96px */
  12vw,              /* preferred: 12% of viewport width */
  var(--space-20)    /* max: 160px */
);
```

#### Responsive Component Gap

```css
.feature-grid {
  gap: clamp(var(--space-3), 3vw, var(--space-6));
  /* 12px → 48px based on viewport */
}
```

### Calculation Formula

```
clamp(MIN, PREFERRED, MAX) = max(MIN, min(PREFERRED, MAX))
```

**Example:** `clamp(24px, 4vw, 48px)`
- At 320px: 4% = 12.8px → clamped to 24px (MIN)
- At 768px: 4% = 30.7px → use 30.7px (between MIN and MAX)
- At 1920px: 4% = 76.8px → clamped to 48px (MAX)

---

## Web vs App Spacing

### Web Package (Editorial, Generous)

Optimized for reading and exploration:

```css
--gap-component: var(--space-5);       /* 24px — roomy */
--spacing-section: clamp(var(--space-12), 12vw, var(--space-20));
  /* 96px → 160px (expansive) */
```

**Use case:** Article, landing page, content-rich site

### App Package (Compact, Data-Dense)

Optimized for productivity and data scanning:

```css
--gap-component: var(--space-4);       /* 16px — compact */
--gap-tight: var(--space-1);           /* 4px — ultra-tight */
--spacing-section: clamp(var(--space-8), 8vw, var(--space-12));
  /* 48px → 96px (compact) */
```

**Use case:** Dashboard, SaaS, admin panel

---

## Touch-Friendly Spacing

Mobile users need larger touch targets (44px minimum).

### Button Touch Area

```css
.btn-touch {
  padding: var(--space-3) var(--space-5);  /* Ensures 44px+ height */
  min-height: 2.75rem;                      /* 44px explicit */
}
```

### Form Input Touch Area

```css
.form-input {
  padding: var(--space-3) var(--space-4);  /* 12px + 16px = good */
  min-height: 2.75rem;                      /* 44px guarantee */
  font-size: var(--text-base);              /* 16px (prevents zoom on iOS) */
}
```

### Checkbox/Radio Touch Area

```css
.form-checkbox, .form-radio {
  width: 1.125em;      /* ~18px at 16px font size */
  height: 1.125em;
  margin: var(--space-2); /* Add margin for 44px total area */
}
```

---

## Negative Space Strategies

### Content Breathing Room

Large text needs large spacing:

```html
<h2 class="t-display-lg">Headline</h2>
<!-- Large space below heading -->
<p class="t-body">Body text starts here...</p>
```

**Spacing:** `margin-bottom: var(--space-8)` (48px) for display text

### Visual Hierarchy

Varying spacing creates grouping:

```html
<div class="stack">
  <article>
    <h3>Article 1</h3>
    <p>Content</p>
  </article>
  <!-- gap: var(--gap-component) = 24px between articles -->
  <article>
    <h3>Article 2</h3>
    <p>Content</p>
  </article>
</div>
```

### Compact Lists

Tight spacing for data lists:

```html
<ul class="stack stack-tight">
  <li>Item 1</li> <!-- gap: var(--gap-tight) = 8px -->
  <li>Item 2</li>
</ul>
```

---

## Token Dependencies

| Token | Typical Use | Value |
|-------|-------------|-------|
| `--space-1` | Icon gaps, micro-spacing | 4px |
| `--space-2` | Form row gaps, tight lists | 8px |
| `--space-3` | Button/input padding | 12px |
| `--space-4` | Form input horiz padding, gaps | 16px |
| `--space-5` | Component gap (flex items) | 24px |
| `--space-6` | Card padding, large gaps | 32px |
| `--space-8` | Section gaps, hero padding vert | 48px |
| `--gap-tight` | Form rows, tag lists | 8px |
| `--gap-component` | Between components | 24px (web) or 16px (app) |
| `--spacing-section` | Between major sections | 96–160px (web) or 48–96px (app) |
| `--page-padding` | Page left/right padding | 24–48px |

---

## Best Practices

1. **Use tokens, not magic numbers**: Always use `var(--space-*)` instead of hardcoding `32px`
2. **Prefer gaps to margins**: Use `gap` in flex/grid instead of margins
3. **Responsive scaling**: Use `clamp()` for section-level spacing
4. **Visual grouping**: Larger spacing = new group; tighter spacing = related items
5. **Touch targets**: Ensure interactive elements are 44px+ on mobile
6. **Breathing room**: Large text needs large padding; small text can be tighter
7. **Consistency**: Pick web or app package based on use case; don't mix defaults

---

## References

- `tokens-web.css` line 180+: complete spacing scale
- `tokens-app.css` line 180+: app-specific spacing defaults
- `components-web.css` line 10+: primitives (stack, cluster, grid-auto)
- [MDN: clamp()](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp())
- [Spacing in Design Systems](https://www.designsystems.com/spacing/) — industry best practices
