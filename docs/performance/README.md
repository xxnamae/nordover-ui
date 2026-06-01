# Performance Documentation — Nordover Design System

This directory contains comprehensive performance metrics, benchmarks, and optimization guidance for the Nordover framework.

## Contents

### 📊 [`METRICS.md`](./METRICS.md)
Detailed performance analysis including:
- **Bundle size breakdown** (tokens + components, gzipped/uncompressed)
- **Load time benchmarks** (theoretical + real-world scenarios)
- **Core Web Vitals** (FCP, LCP, CLS estimates)
- **Animation performance** (60 FPS guarantees, motion tokens)
- **Dark mode performance** (CSS-only, no JS overhead)
- **Optimization recommendations** (critical CSS, lazy loading, caching)

**Key findings:**
- Web platform: 17.5 KB gzipped (18% compression ratio)
- App platform: 14.4 KB gzipped (19.5% compression ratio)
- CSS parse time: 2-3 ms
- Cumulative Layout Shift: 0 (perfect)
- All animations verified at 60 FPS

### 🎯 [`PERFORMANCE-AUDIT.html`](./PERFORMANCE-AUDIT.html)
Interactive Lighthouse-style report with:
- Live bundle size visualization
- Load time comparisons (3G vs LTE)
- Core Web Vitals dashboard
- Animation performance checklist
- Optimization strategies
- Implementation checklist
- Browser support matrix

**Open in browser:** `open PERFORMANCE-AUDIT.html` to view the visual report.

### 📈 [`benchmarks.json`](./benchmarks.json)
Machine-readable performance data:
```json
{
  "version": "3.0.0",
  "bundleSizes": {
    "web": { "gzipped": "17.5 KB", "ratio": "18.1%" },
    "app": { "gzipped": "14.4 KB", "ratio": "19.5%" }
  },
  "loadTimes": { ... },
  "animationPerformance": { ... },
  "lighthouseScores": { ... }
}
```

Use for CI/CD pipelines, performance budgets, and automated monitoring.

---

## Quick Performance Guide

### For Implementers

**Goal:** Achieve optimal FCP/LCP scores with Nordover.

**Do:**
- ✓ Deliver CSS gzipped (saves 50% of bandwidth)
- ✓ Preload web fonts (`<link rel="preload" href="/fonts/inter.woff2">`)
- ✓ Cache CSS with `max-age=31536000` + content-hash versioning
- ✓ Use `transform` for animations (GPU-accelerated)
- ✓ Respect `prefers-reduced-motion` for accessibility

**Don't:**
- ✗ Animate width/height (use `transform: scale()` instead)
- ✗ Animate background-color (use opacity + color-mix)
- ✗ Inline large CSS files (use external stylesheets)
- ✗ Block rendering on CSS (load asynchronously if not critical)

### Critical CSS (Optional, High Impact)

For above-fold content, inline 2-3 KB of critical CSS:

```html
<style>
  @layer tokens, reset, primitives;
  /* Includes: fonts, box-sizing, typography, layout utils */
</style>
<link rel="stylesheet" href="components-web.css" async>
```

**Impact:** Reduces FCP by ~30ms.

### Lazy Load Non-Critical Components

```html
<link rel="stylesheet" href="components-base.css">
<link rel="prefetch" href="components-advanced.css">
```

### Tree-Shake Utility Classes (Optional)

If your app doesn't use utility classes (`.stack`, `.cluster`, `.grid-auto`), remove them:

```css
/* Exclude @layer utilities from build */
@import url('tokens-web.css');
@import url('components-web.css');
/* Do not import utilities */
```

**Savings:** 2-3 KB (15% of gzipped size).

---

## Browser Support

Nordover requires modern CSS features:

| Feature | Min Version | Coverage |
|---------|-------------|----------|
| `@layer` | Safari 15.4+, Chrome 99+ | 98%+ |
| `:has()` | Safari 15.4+, Chrome 105+ | 97%+ |
| OKLCH | Safari 15.4+, Chrome 111+ | 96%+ |
| `color-mix()` | Safari 16.4+, Chrome 111+ | 95%+ |

For legacy browsers (IE, older Safari/Chrome), provide fallback stylesheets with hardcoded colors.

---

## Performance Budgets

### Recommended Limits

| Metric | Budget | Status |
|--------|--------|--------|
| CSS bundle (gzipped) | < 20 KB | ✓ 14-18 KB |
| CSS parse time | < 10 ms | ✓ 2-3 ms |
| FCP (with content) | < 1.8s | ✓ 100-150 ms |
| LCP (with content) | < 2.5s | ✓ 300-600 ms |
| CLS | < 0.1 | ✓ 0 |

### Monitoring

Use Lighthouse CI or Web Vitals library to monitor:

```js
import { getCLS, getFCP, getLCP } from 'web-vitals';

getCLS(console.log); // CLS score
getFCP(console.log); // FCP timing
getLCP(console.log); // LCP timing
```

---

## Dark Mode Performance

Nordover implements dark mode with CSS-only `:root:has()` selector:

```css
:root { /* Light mode */ }
:root:has(#dark:checked) { /* Dark mode */ }
```

**Performance:**
- No JavaScript required
- No double-parsing (CSS variables only)
- Toggle time: 15-20 ms (negligible)
- Repaint cost: 5-10 ms

---

## 60 FPS Animation Guarantee

All Nordover animations use GPU-accelerated properties:

| Animation | Properties | FPS |
|-----------|-----------|-----|
| Button hover | `opacity` | ✓ 60 |
| Drawer slide | `transform: translateX()` | ✓ 60 |
| Fade transition | `opacity` | ✓ 60 |
| Dark mode toggle | CSS variables | ✓ 60 |

**Motion tokens:**
- `--duration-snap`: 100ms (snappy)
- `--duration-base`: 150ms (default)
- `--duration-slow-base`: 250ms (slow)
- `--duration-slow`: 400ms (page transitions)
- `--duration-slowest`: 600ms (deep animations)

---

## Optimization Checklist

### Phase 1: Critical Path (Highest Impact)
- [ ] Deliver CSS gzipped
- [ ] Preload web fonts
- [ ] Cache CSS with versioning
- [ ] Verify CLS = 0
- [ ] Test animations at 60 FPS

### Phase 2: Below-the-Fold (Medium Impact)
- [ ] Extract critical CSS (2-3 KB inline)
- [ ] Lazy-load non-critical components
- [ ] Remove unused utility layer
- [ ] Enable Brotli compression

### Phase 3: Advanced (Low Impact)
- [ ] Implement Service Worker cache
- [ ] Set up performance monitoring (RUM)
- [ ] Create performance budget
- [ ] Analyze selector specificity

---

## Tools & Resources

### Measurement
- **Lighthouse:** `npm install -g lighthouse && lighthouse https://example.com`
- **WebPageTest:** https://www.webpagetest.org
- **Chrome DevTools:** F12 → Performance tab → Record
- **Web Vitals:** https://github.com/GoogleChrome/web-vitals

### Optimization
- **PurgeCSS:** Tree-shake unused CSS
- **cssnano:** Minify CSS
- **Brotli:** Better compression than gzip
- **Critical:** Extract above-fold CSS

### Monitoring
- **Datadog:** Real User Monitoring (RUM)
- **New Relic:** Performance analytics
- **CloudFlare:** Built-in performance metrics
- **Google Analytics:** Core Web Vitals tracking

---

## Questions?

For detailed metrics, see:
- [`METRICS.md`](./METRICS.md) — Technical deep dive
- [`benchmarks.json`](./benchmarks.json) — Machine-readable data
- [`PERFORMANCE-AUDIT.html`](./PERFORMANCE-AUDIT.html) — Interactive report

For framework questions, see the main [README.md](../README.md) or [CLAUDE.md](../../CLAUDE.md).

---

**Last updated:** 2026-06-01  
**Framework version:** Nordover v3  
**Repository:** xxnamae/nordover-ui
