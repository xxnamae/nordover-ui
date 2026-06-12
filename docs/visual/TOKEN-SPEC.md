# Token Specification — Nordover Design System

**Version:** 3.0.0  
**Updated:** 2026-06-12  
**Audience:** Framework consumers (Token Studio, theme generators, platform integrations)

## Overview

Nordover tokens are designed for **machine generation of themes** (high-contrast, dark mode variants, platform-specific overrides) while maintaining semantic consistency. This document specifies the contract that generators can rely on.

## Grayscale Scale as Contrast Anchor

The grayscale scale is the **sanctioned adjustment point for contrast**. Consumers (Token Studio, automated theme generators) can modify contrast by adjusting grayscale endpoints and propagating changes through semantic tokens.

### Light Mode Grayscale (app package)

```
--gray-50:  oklch(0.985 …)  ← lightest (near-white, used as fallback light)
--gray-100: oklch(0.96 …)   ← very light (surface, subtle backgrounds)
--gray-200: oklch(0.92 …)   ← light gray (borders, disabled)
--gray-300: oklch(0.865 …)  ← light-mid
--gray-400: oklch(0.70 …)   ← medium (muted text, secondary content)
--gray-500: oklch(0.52 …)   ← mid-dark (contrast ceiling for --color-muted)
--gray-600: oklch(0.435 …)  ← dark
--gray-900: oklch(0.13 …)   ← darkest (used as dark-mode surface base)
```

**Contrast-High Variant Rule:**  
To generate a high-contrast theme, increase ΔL between `--color-bg` and `--color-fg`:
- **Standard:** bg=0.98 (gray-50), fg=0.13 (gray-900) — ΔL=0.85 (ratio ~9:1)
- **High-contrast:** bg=0.995 (white), fg=0 (pure black) — ΔL=0.995 (ratio ~20:1)

Both are **valid expressions** of the token system. Consumers can:
1. Adjust gray-50 and gray-900 L-values
2. Cascade changes through derived tokens (`--color-bg`, `--color-fg`, `--color-subtle`, etc.)
3. Regenerate theme CSS

### Dark Mode Grayscale (inverse)

Same scale, inverted usage:
- `--color-bg`: uses `--gray-950` (darkest, L=0.06 or lower)
- `--color-fg`: uses `--gray-50` (brightest)
- ΔL maintained for contrast

## Surface Elevation as L-Axis Offsets

`--surface-1` through `--surface-5` are defined as **L-axis offsets from `--color-bg`**, not absolute L-values. This enables:
- **Automatic depth scaling:** If a theme lowers `--color-bg`, surfaces scale proportionally
- **Consistent hierarchy:** Ratios between surfaces remain perceptually even across themes

### Example: Light Mode
```
--color-bg: oklch(0.98 …)
--surface-1: 0.98 L  (= bg, base level)
--surface-2: 0.99 L  (= bg + 0.01, subtle lift)
--surface-3: 1.0 L   (= bg + 0.02, elevated panel)
```

### Example: Dark Mode
```
--color-bg: oklch(0.13 …)
--surface-1: 0.13 L  (= bg)
--surface-2: 0.17 L  (= bg + 0.04, subtle lift)
--surface-3: 0.21 L  (= bg + 0.08, elevated panel)
```

**Machine Implication:** Generators can compute surfaces dynamically:
```
surface-N = color-mix(white, color-bg, percentage)
// or
surface-N = oklch(color-bg-lightness + offset, …)
```

## Semantic Token Mapping

### Text / Display Hierarchy
- Semantic: `.t-display-*`, `.t-heading-*`, `.t-body-*` (class contracts)
- Mapped to: `--text-*` tokens (size scale)
- **Invariant:** Class→token mappings identical across app/web packages
- **Values differ:** App uses fixed rem, Web uses fluid clamp()

### Color Semantic Triples
All colored surfaces follow the pattern:
```
--{semantic}: base color (e.g., oklch(0.62 0.22 25) for error)
--{semantic}-subtle: color-mix(--{semantic} 20%, --color-bg)  ← background
--{semantic}-strong: color-mix(--{semantic} 70%, white|black)  ← emphasis/text
```

**Contrast Obligation:** `-strong` variants **must** meet WCAG AA (4.5:1) on `--color-bg` and `--color-surface`.

## Type Precision Weights (App Package)

Linear-inspired mid-range weights for UI density:
- `--fw-ui: 510` — standard UI (nav, labels, buttons)
- `--fw-ui-strong: 590` — emphasized UI (active, headers)

These are **app-specific** (not in web). Used to achieve tighter, clearer UI without changing font.

## Theme Variant Expression

Valid theme expressions (consumers may generate):

### high-contrast variant
- Increase `--gray-50` L (whiter)
- Decrease `--gray-900` L (blacker)
- Regenerate all dependent tokens
- Result: WCAG AAA compliance guaranteed if ΔL ≥ 0.99

### high-saturation variant (future)
- Increase chroma (C-axis) in semantic colors
- Useful for accessibility markers, brand emphasis
- Does not affect grayscale

### reduced-motion variant
Already in CSS via `@media (prefers-reduced-motion: reduce)`. Generators should preserve.

## Deprecation Schedule

Tokens/classes marked `@deprecated` are guaranteed to exist for **one minor release** (8 weeks) before removal.

Example:
```css
--text-8xl: /* @deprecated since v3.2.0 — use --text-7xl instead. Removing in v3.3.0. */
```

Consumers must update before the removal release. Non-compliance breaks downstream CI.

## Accessibility Constraints (Non-Negotiable)

- `--color-muted` must maintain ≥4.5:1 contrast on `--color-bg` (WCAG AA for secondary text)
- All `-strong` variants must meet ≥4.5:1 contrast on `--color-surface`
- `@media (prefers-reduced-motion: reduce)` must suppress all animations/transitions

These are **invariants**. Consumers may increase contrast but not decrease below these floors.

## Tooling Implications

### Token Studio
- Can regenerate `gray-*` scale as input (theme configurator)
- Should compute `--surface-*` as L-offsets from computed `--color-bg`
- May generate high-contrast variant by adjusting gray-50/gray-900

### Design Tools
- Import `tokens-app.json` / `tokens-web.json` for local use
- Semantic tokens (`--color-accent`, `--fw-ui`) are guaranteed stable
- Generated artefacts (Elementor-JSON) are regenerated with each CSS commit

### CI / Automation
- `npm run build:tokens` regenerates JSON from CSS (single source of truth)
- JSON must stay in sync; CI enforces this
- Breaking changes (grayscale adjustments) warrant minor version bump

## Changelog

- **v3.0.0 (2026-06-12)** — Specification published. L-axis stepping surfaces + UI weights introduced. Contrast variants documented as valid theme expressions.
