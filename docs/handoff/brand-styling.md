# Brand Styling Guide — Nordover

**For:** Implementors, new customers  
**Status:** Normativ (governs all client projects)  
**Updated:** 2026-06-01

---

## Overview

Nordover design system is **universal + customizable**. You get:

- ✅ **Out of the box:** 50+ battle-tested components, responsive on mobile/tablet/desktop, WCAG AA compliant, dark mode
- ✅ **Your brand:** Change 3–5 tokens, watch the entire system recolor. No per-component hacking.

This guide covers how to brand Nordover for your product.

---

## Quick Start (3 minutes)

1. **Copy the template:**
   ```bash
   cp docs/visual/clients/_template.css clients/<your-slug>.css
   ```

2. **Open `clients/<your-slug>.css` and customize these tokens:**
   - `--color-accent` — your primary brand color
   - `--font-display` — your display/headline font (optional)
   - `--radius-md` — personality of rounded corners (optional)

3. **Test in your app:**
   ```html
   <link rel="stylesheet" href="path/to/tokens-web.css">
   <!-- ... all other framework CSS ... -->
   <link rel="stylesheet" href="path/to/clients/your-slug.css">
   ```

That's it. Your entire brand is now live.

---

## Token Categories

### Safe to Override: BRAND-OVERSTYRBARE

These tokens control visual branding. Override them freely per customer.

| Token | Default | What it does | Example override |
|-------|---------|-------------|------------------|
| `--color-accent` | `oklch(0.55 0.30 260)` (blå) | Primary brand color (buttons, links, accents) | `oklch(0.55 0.35 15)` (red) |
| `--color-accent-hover` | Derived via color-mix | Hover state of accent elements | Automatically derives from your accent |
| `--color-accent-active` | Derived via color-mix | Active/pressed state | Automatically derives from your accent |
| `--font-display` | `"Inter Tight Variable"` | Headlines, large titles | `"Fraunces", serif` |
| `--color-focus` | `#0066FF` | Focus ring (keyboard navigation) | Match your brand color |
| `--radius-md` | `8px` | Default roundness | `2px` (sharp) or `16px` (soft) |
| `--radius-lg` | `12px` | Larger rounded elements | Adjust in sync with md |
| `--chart-1..8` | See tokens-web.css | Data visualization colors | Brand-specific palette |

### NEVER Override: LÅSTE TOKENS

These are architectural — changing them breaks the system. Here's why:

| Token | Why it's locked |
|-------|-----------------|
| `--text-xs`, `--text-sm`, `--text-base`, …, `--text-8xl` | **Fluid typography scale.** These power responsive text sizing (clamp) and line-height harmony. Changing them breaks hierarchy and readability on mobile. |
| `--space-1`, `--space-2`, `--space-3`, …, `--space-48` | **Spacing grid.** All component padding/margin are multiples of this. Breaking it destroys layout rhythm. |
| `--gap-tight`, `--gap-component`, `--gap-section` | **Component gaps.** Built into Button, Card, List, etc. Changing collapses spacing. |
| `--bp-tablet` (576px), `--bp-desktop` (768px), `--bp-wide` (960px), etc. | **Responsive breakpoints.** These are in media queries. Changing breaks layout at specific viewports. |
| `--duration-fast`, `--duration-base`, `--duration-slow` | **Motion timing.** These define transition speeds. Consistency across the system is critical for a polished feel. |
| `--shadow-xs`, `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl` | **Elevation/depth hierarchy.** Changing breaks visual hierarchy. |

**If you absolutely need to change a locked token,** contact the design system team. We'll create a variant or ADR.

---

## Examples

### Example 1: Red Brand

```css
/* clients/acme-red.css */
@layer brand {
  :root {
    --color-accent: oklch(0.55 0.25 20);  /* Vibrant red */
    --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);
    --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, white);
    --color-focus: oklch(0.55 0.25 20);
  }
}
```

Result: All buttons, links, focus rings, badges are now red. Hover/active states auto-derive. Dark mode automatically adjusts shadow colors for contrast.

### Example 2: Serif + Soft Design

```css
/* clients/editorial.css */
@layer brand {
  :root {
    --color-accent: oklch(0.50 0.15 280);  /* Subtle purple */
    --font-display: "Crimson Text", serif;
    --radius-md: 14px;
    --radius-lg: 20px;
  }
}
```

Result: Headlines are serif, corners are soft, accent is muted purple. Still fully responsive and accessible.

### Example 3: Dark + Tech

```css
/* clients/dark-tech.css */
@layer brand {
  :root {
    --color-accent: oklch(0.60 0.25 240);  /* Bright cyan */
    --font-display: "IBM Plex Mono", monospace;
    --radius-md: 0px;  /* Fully sharp */
    --chart-1: oklch(0.60 0.25 240);       /* Cyan */
    --chart-2: oklch(0.55 0.20 150);       /* Teal */
    --chart-3: oklch(0.50 0.30 15);        /* Red */
  }
}
```

Result: Monospace headlines, no rounding, cyan accents everywhere, custom data viz colors.

---

## Dark Mode Behavior

Nordover's dark mode is **automatic**. When the user toggles dark mode:

- All `--color-*` tokens automatically adjust (defined in `tokens-web.css :root:has(#dark:checked)`)
- `--shadow-*` tokens get darker for visibility on dark backgrounds
- Your brand color (via `--color-accent`) automatically becomes lighter (the color-mix in tokens does this)

**You don't need to define dark variants in `clients/<slug>.css`.** The framework handles it.

### If you want custom dark mode behavior:

```css
@layer brand {
  :root:has(#dark:checked) {
    --color-accent: oklch(0.70 0.25 240);  /* Lighter in dark mode */
    --color-focus: oklch(0.70 0.25 240);
  }
}
```

But this is rarely needed — the defaults work well 95% of the time.

---

## Fonts: Practical Notes

### Display Font (`--font-display`)

Used in: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, `.t-display-*`, `.t-heading-*`

**Default:** `"Inter Tight Variable"` (geometric sans)

**Popular overrides:**
- **Serif:** `"Fraunces", "Crimson Text", "Playfair Display"` → Premium, editorial
- **Monospace:** `"IBM Plex Mono", "JetBrains Mono"` → Tech, code-forward
- **Humanist sans:** `"Segoe UI", "-apple-system"` → Friendly, accessible

**Important:** Make sure the font is loaded before the CSS applies. Use `@font-face` in an earlier layer or a CDN `<link>` in HTML.

```html
<!-- In your HTML head -->
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;600;700&display=swap" rel="stylesheet">
```

### Fallback Chain

```css
--font-display: "Fraunces", "Crimson Text", serif;
```

If Fraunces doesn't load, falls back to Crimson Text, then system serif. Always end with a generic (serif, sans-serif, monospace).

---

## Testing Your Brand

After applying `clients/<slug>.css`, verify:

1. **Buttons look branded:** Primary button, hover state, disabled state
2. **Links and focus rings:** Keyboard navigation shows your brand color
3. **Headings:** Display font applied if customized
4. **Dark mode:** Toggle dark mode, everything auto-adjusts (including shadows)
5. **Mobile:** Test on narrow viewport (< 480px) — spacing and colors still work
6. **Contrast:** Focus ring, buttons, text on colored backgrounds meet WCAG AA

Use a tool like [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to verify.

---

## Common Mistakes

| ❌ Wrong | ✅ Right | Why |
|---------|---------|-----|
| Override `--text-base` to 16px | Leave it alone | Font scale is locked; changing breaks hierarchy |
| Override `--space-4` to 8px | Use in your brand layer only for specific elements | Spacing grid is locked architecture |
| Define colors in hex | Use OKLCH (e.g., `oklch(0.55 0.25 20)`) | OKLCH automatically adjusts for dark mode |
| Copy entire component CSS into `clients/<slug>.css` | Only override tokens | Component CSS lives in framework, not per-client |
| Redefine `--color-accent-hover` as solid color | Use `color-mix(in oklch, var(--color-accent) 85%, white)` | Ensures hover states derive from your accent |

---

## Locked Tokens Explanation: Why They Matter

### Locked: Text Scale (`--text-xs` through `--text-8xl`)

The web version uses **fluid typography** with `clamp()`:
```css
--text-lg: clamp(1.125rem, 1.089rem + 0.18vw, 1.25rem);
```

This means:
- On mobile (320px), text-lg is ~1.125rem
- On desktop (1440px), text-lg is ~1.25rem
- Text grows smoothly in between

If you change `--text-lg` to a fixed value, you break this responsive behavior. **Don't do it.**

### Locked: Spacing Grid (`--space-*`)

All components use multiples of the spacing grid:
```css
.button { padding: var(--space-2) var(--space-3); }
.card { padding: var(--space-4); gap: var(--gap-component); }
```

The grid ensures visual rhythm. Breaking it means buttons are misaligned with cards, cards misaligned with sections, etc. **Not worth it.**

### Locked: Breakpoints (`--bp-tablet`, `--bp-desktop`, etc.)

Media queries reference these:
```css
@media (min-width: var(--bp-desktop)) { ... }
```

Changing the breakpoint value changes where responsive layout transitions happen — breaking the system.

---

## Questions?

See also:
- [Architecture Decision Record: Brand-layer kontrakt](../wiki/decisions/2026-06-01-brand-lag-kontrakt.md)
- [Tokens reference](../visual/tokens/tokens-web.css)
- [Component index](../visual/preview.html)

For custom needs or exceptions, contact the design system team.
