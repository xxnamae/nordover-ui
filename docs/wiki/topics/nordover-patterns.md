# Pattern Specifications — Nordover

**Status:** Complete  
**Package:** `components-web.css` and `components-app.css`

## Overview

Patterns are reusable layouts for common sections and page structures. Nordover provides section patterns for editorial content and layout patterns for application shells.

---

## Section Patterns

### Hero Section

Centered headline with optional background gradient and CTA.

```html
<section class="hero-centered">
  <h1 class="t-display-lg">Build Without Limits</h1>
  <p class="t-body-lg">A design system built for scale</p>
  <button class="btn btn-primary btn-lg">Get Started</button>
</section>
```

**CSS:**
```css
.hero-centered {
  padding: var(--space-10) var(--space-6);  /* 64px vert, 32px horiz */
  text-align: center;
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-lg);
  border: var(--border-card);
}

.hero-centered::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--gradient-radial-accent);
  pointer-events: none;
  opacity: 0.03;
}

.hero-centered > * {
  position: relative;
  z-index: 1;
}
```

**Customization:**
- `.hero-centered` — default centered layout
- Add background gradient with `::before` pseudo-element
- Adjust padding via `--space-*` tokens
- Dark mode: gradient automatically adjusts via CSS variables

---

### Feature Grid

Grid of feature cards with icon, heading, and description.

```html
<section class="page-section">
  <h2 class="t-heading-lg">Features</h2>
  <div class="feature-grid">
    <article class="feature-card">
      <svg class="icon icon-lg icon-primary" viewBox="0 0 24 24"><!-- icon --></svg>
      <h3 class="t-heading-sm">Design Tokens</h3>
      <p class="t-body-sm">Semantic variables for colors, spacing, typography</p>
    </article>
    <article class="feature-card">
      <svg class="icon icon-lg icon-primary" viewBox="0 0 24 24"><!-- icon --></svg>
      <h3 class="t-heading-sm">Components</h3>
      <p class="t-body-sm">40+ production-ready, accessible components</p>
    </article>
  </div>
</section>
```

**CSS:**
```css
.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(15rem, 100%), 1fr));
  gap: var(--space-5);  /* 24px grid gap */
}

.feature-card {
  padding: var(--space-5);  /* 24px */
  border: var(--border-card);
  border-radius: var(--radius-lg);
  transition: border-color var(--duration-fast) var(--ease-out),
              background var(--duration-fast) var(--ease-out);
}

.feature-card:hover {
  border-color: var(--color-fg);
  background: var(--color-subtle);
}

.feature-card-icon {
  width: 2rem;
  height: 2rem;
  color: var(--color-accent);
  margin-bottom: var(--space-3);
}
```

**Responsive:** `auto-fit` creates 1–3 column layout based on viewport.

---

### Pricing Cards

Cards displaying pricing tiers with features list.

```html
<section class="page-section">
  <h2 class="t-heading-lg">Pricing</h2>
  <div class="pricing-grid">
    <article class="price-card">
      <h3 class="t-heading-sm">Starter</h3>
      <div class="price-val">$29</div>
      <p class="t-body-sm">/month</p>
      <ul class="price-features">
        <li>10 projects</li>
        <li>Basic components</li>
        <li>Community support</li>
      </ul>
      <button class="btn btn-secondary btn-lg">Get Started</button>
    </article>
    
    <article class="price-card price-card-highlight">
      <h3 class="t-heading-sm">Pro</h3>
      <div class="price-val">$99</div>
      <p class="t-body-sm">/month</p>
      <ul class="price-features">
        <li>Unlimited projects</li>
        <li>All components</li>
        <li>Priority support</li>
      </ul>
      <button class="btn btn-primary btn-lg">Choose Plan</button>
    </article>
  </div>
</section>
```

**CSS:**
```css
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: var(--space-5);
}

.price-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding: var(--space-6);
  border: var(--border-card);
  border-radius: var(--radius-lg);
  position: relative;
  transition: border-color var(--duration-fast) var(--ease-out),
              box-shadow var(--duration-fast) var(--ease-out));
}

.price-card:hover {
  border-color: var(--color-fg);
  box-shadow: var(--shadow-md);
}

.price-card-highlight {
  border-color: var(--color-fg);
  background: var(--color-subtle);
}

.price-card-highlight::before {
  content: "Popular";
  position: absolute;
  top: -0.625rem;
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-accent);
  color: var(--color-accent-fg);
  font-size: var(--text-xs);
  font-weight: var(--fw-semibold);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
  padding: 0.125rem var(--space-2);
  border-radius: var(--radius-full);
}

.price-val {
  font-family: var(--font-display);
  font-size: var(--text-4xl);
  font-weight: var(--fw-display-md);
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.price-features {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  flex: 1;
}

.price-features li {
  display: flex;
  gap: var(--space-2);
  font-size: var(--text-sm);
}

.price-features li::before {
  content: "✓";
  color: var(--color-success);
  font-weight: var(--fw-semibold);
}
```

**Highlight:** `.price-card-highlight` shows popular/recommended tier.

---

### CTA Card (Call-to-Action)

Large, centered card encouraging action.

```html
<section class="cta-card">
  <h2 class="t-heading-lg">Ready to ship?</h2>
  <p class="t-body-lg">Start with Nordover design system today</p>
  <button class="btn btn-primary btn-lg">Get Started Free</button>
</section>
```

**CSS:**
```css
.cta-card {
  position: relative;
  background: var(--color-subtle);
  border-radius: var(--radius-xl);
  padding: clamp(var(--space-8), 7vw, var(--space-12)) var(--space-6);
  text-align: center;
  overflow: hidden;
}

.cta-card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--gradient-radial-accent);
  pointer-events: none;
  opacity: 0.04;
}

.cta-card > * {
  position: relative;
  z-index: 1;
}
```

**Responsive:** Padding scales from 48px (mobile) to 96px (desktop) smoothly.

---

### FAQ Section

Collapsible details elements for frequently asked questions.

```html
<section class="page-section">
  <h2 class="t-heading-lg">Frequently Asked Questions</h2>
  <div class="faq-list">
    <details>
      <summary class="faq-summary">What browsers do you support?</summary>
      <div class="faq-answer">
        <p>Nordover supports modern browsers: Chrome 99+, Firefox 97+, Safari 15.4+, Edge 99+.</p>
      </div>
    </details>
    
    <details>
      <summary class="faq-summary">Can I customize the colors?</summary>
      <div class="faq-answer">
        <p>Yes! Override tokens in a <code>@layer brand</code> block in your CSS.</p>
      </div>
    </details>
  </div>
</section>
```

**CSS:**
```css
.faq-list { display: flex; flex-direction: column; }

.faq-item {
  border-bottom: var(--border-divider);
}

.faq-summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-4) 0;
  font-size: var(--text-lg);
  font-weight: var(--fw-medium);
  cursor: pointer;
  list-style: none;
  user-select: none;
}

.faq-summary::-webkit-details-marker {
  display: none;
}

.faq-summary::after {
  content: "▾";
  transition: transform var(--duration-base) var(--ease-out);
}

details[open] .faq-summary::after {
  transform: rotate(180deg);
}

.faq-answer {
  padding-bottom: var(--space-4);
  color: var(--color-muted);
}
```

**Accessibility:** Uses semantic `<details>` and `<summary>` elements.

---

## Layout Patterns

### Page Layout (Editorial)

Standard single-column layout for articles, landing pages.

```html
<div class="page">
  <header class="page-header">
    <h1 class="t-display-lg">Article Title</h1>
    <p class="t-eyebrow">Published May 30, 2026</p>
  </header>
  
  <article class="page-content">
    <p class="t-body-lg">Opening paragraph...</p>
    <h2 class="t-heading-lg">Section Title</h2>
    <p class="t-body">Body text...</p>
  </article>
</div>
```

**CSS:**
```css
.page {
  display: flex;
  flex-direction: column;
  gap: var(--spacing-section);           /* Responsive: 96px → 160px */
  padding-inline: var(--page-padding);   /* Responsive: 24px → 48px */
}

.page-content {
  max-width: 64rem;   /* 1024px — comfortable reading width */
  margin-inline: auto; /* Center content */
}
```

---

### Sidebar Layout (Application)

Two-column layout with sidebar navigation.

```html
<div class="layout-sidebar">
  <aside class="sidebar">
    <!-- Navigation menu -->
  </aside>
  <main class="main-content">
    <!-- Page content -->
  </main>
</div>
```

**CSS:**
```css
.layout-sidebar {
  display: grid;
  grid-template-columns: 16rem 1fr;
  gap: var(--gap-section);
  min-height: 100vh;
}

.sidebar {
  background: var(--color-subtle);
  padding: var(--space-6);
  border-right: var(--border-divider);
  position: sticky;
  top: 0;
  overflow-y: auto;
}

.main-content {
  padding: var(--space-6);
}

@media (max-width: 48rem) {
  .layout-sidebar {
    grid-template-columns: 1fr;
  }
  
  .sidebar {
    display: none; /* Mobile: drawer pattern instead */
  }
}
```

---

### Grid Layout (Dashboard)

Multi-column dashboard grid for cards and widgets.

```html
<div class="dashboard-grid">
  <div class="card">
    <h3 class="t-heading-sm">Revenue</h3>
    <div class="metric-value">$24,500</div>
  </div>
  
  <div class="card">
    <h3 class="t-heading-sm">Users</h3>
    <div class="metric-value">1,240</div>
  </div>
</div>
```

**CSS:**
```css
.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr));
  gap: var(--gap-component);
}

.card {
  padding: var(--space-5);
  background: var(--color-surface);
  border: var(--border-card);
  border-radius: var(--radius-lg);
}

.metric-value {
  font-size: var(--text-3xl);
  font-weight: var(--fw-display-md);
  margin-top: var(--space-3);
}
```

---

## Footer Pattern

Standard footer with multiple columns.

```html
<footer class="footer">
  <div class="page">
    <div class="footer-grid">
      <div class="footer-col">
        <h4 class="t-heading-sm">Product</h4>
        <ul class="footer-links">
          <li><a href="#">Features</a></li>
          <li><a href="#">Pricing</a></li>
          <li><a href="#">Docs</a></li>
        </ul>
      </div>
      
      <div class="footer-col">
        <h4 class="t-heading-sm">Company</h4>
        <ul class="footer-links">
          <li><a href="#">About</a></li>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p class="t-caption">&copy; 2026 Company. All rights reserved.</p>
    </div>
  </div>
</footer>
```

**CSS:**
```css
.footer {
  background: var(--color-subtle);
  border-top: var(--border-divider);
  padding: var(--spacing-section) 0;
  margin-top: var(--spacing-section);
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  gap: var(--space-8);
  margin-bottom: var(--space-8);
}

.footer-col h4 {
  margin-bottom: var(--space-4);
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.footer-links a {
  color: var(--color-muted);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}

.footer-links a:hover {
  color: var(--color-accent);
}

.footer-bottom {
  border-top: var(--border-divider);
  padding-top: var(--space-6);
  text-align: center;
}
```

---

## Responsive Behavior

### Mobile Stacking

All multi-column patterns automatically stack on mobile:

```css
@media (max-width: 48rem) {
  .feature-grid,
  .pricing-grid,
  .dashboard-grid {
    grid-template-columns: 1fr; /* Single column */
  }
}
```

### Container Queries (Progressive Enhancement)

For advanced responsive behavior without media queries:

```css
@supports (container-type: inline-size) {
  .pricing-card {
    container-type: inline-size;
  }
  
  @container (min-width: 24rem) {
    .price-features { flex-direction: row; }
  }
}
```

---

## Best Practices

1. **Semantic HTML**: Use `<section>`, `<article>`, `<footer>`, etc.
2. **Spacing hierarchy**: Larger sections need larger gaps
3. **Readability**: Content width max 64–72rem for body text
4. **Responsive stacking**: All grids should single-column on mobile
5. **Visual hierarchy**: Use typography classes to guide focus
6. **Accessibility**: Proper heading hierarchy (h1 → h2 → h3)

---

## References

- `components-web.css` line 160+: hero, feature grid, CTA, pricing patterns
- `nordover-spacing.md`: spacing token reference
- `nordover-typography.md`: typography classes (t-heading-*, t-body-*)
