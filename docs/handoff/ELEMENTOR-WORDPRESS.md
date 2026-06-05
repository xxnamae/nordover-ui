# Nordover in Elementor Pro / WordPress

**Approach:** use Nordover as your **design-token layer**. You map Nordover's
tokens (colours, spacing, typography, radius, shadows) into Elementor's own
systems, then build pages with Elementor's native widgets — styled by those
tokens. You are *not* loading the component CSS; you're adopting the
foundation so everything you build in Elementor stays on-brand and consistent
with apps/sites that use the full framework.

> Why token-only here: Elementor widgets generate their own markup, so the
> `.btn` / `.card` component classes rarely land on the right element. Tokens,
> on the other hand, drop straight into Elementor's Global Colors, Global
> Fonts, and any Custom CSS field via `var(--…)`.

---

## Step 1 — Load the tokens once (site-wide)

**Elementor → Site Settings → Custom CSS** (Pro) or **Appearance → Customize →
Additional CSS**. Paste the Nordover token block so every page can use
`var(--…)`. You have two options:

**A. Reference the published file (simplest):**
```css
@import url("https://YOUR-CDN/nordover/tokens-web.css");
```
Use `tokens-web.css` for marketing/editorial sites, `tokens-app.css` for
dense app-like dashboards.

**B. Paste the token values inline** (no external request). Copy the
`:root { … }` block from `docs/visual/tokens/tokens-web.css` into the Custom
CSS field. This is the most robust for WordPress hosting.

Either way you now have the full token set available globally.

---

## Step 2 — Map the core tokens into Elementor's managers

Elementor has native **Global Colors** and **Global Fonts** (and a Variables
Manager in v3.33+/Editor V4). Recreate Nordover's semantic names there and set
each value to the matching token. Use semantic names, never "Blue"/"Red".

### Global Colors

| Elementor Global Color | Set value to | Nordover token |
|------------------------|--------------|----------------|
| Primary / Accent | `var(--color-accent)` | `--color-accent` |
| On-Accent (text on accent) | `var(--color-accent-fg)` | `--color-accent-fg` |
| Text / Body | `var(--color-fg)` | `--color-fg` |
| Muted Text | `var(--color-muted)` | `--color-muted` |
| Background | `var(--color-bg)` | `--color-bg` |
| Surface (cards) | `var(--color-surface)` | `--color-surface` |
| Border | `var(--color-border)` | `--color-border` |
| Success | `var(--color-success)` | `--color-success` |
| Warning | `var(--color-warning)` | `--color-warning` |
| Error | `var(--color-error)` | `--color-error` |
| Info | `var(--color-info)` | `--color-info` |

> Tip: if Elementor's color field rejects `var(--…)`, paste the resolved
> value from the token file (e.g. the OKLCH or hex fallback) and keep the
> token name in the color's label so the mapping stays traceable.

### Global Fonts

| Elementor Global Font | Nordover token | Typical role |
|-----------------------|----------------|--------------|
| Primary | `--font-sans` | Body copy, UI |
| Secondary / Display | `--font-display` | Headlines |
| Accent / Code | `--font-mono` | Code, data |

Set the type **sizes** from the scale (`--text-sm`, `--text-base`,
`--text-lg`, `--text-2xl`, …) and headings from the semantic tier
(`--text-4xl`/`--text-6xl` for display).

### Spacing & radius (Variables Manager or Custom CSS)

Reuse the spacing scale instead of typing pixel values into widgets:

| Token | Value (web) | Use for |
|-------|-------------|---------|
| `--space-2` | 0.5rem | Tight gaps |
| `--space-4` | 1rem | Default padding/gap |
| `--space-6` | 2rem | Section inner padding |
| `--space-8` | 3rem | Between blocks |
| `--space-12` | 6rem | Section rhythm |
| `--radius-md` / `--radius-lg` | — | Buttons / cards |
| `--shadow-sm` / `--shadow-md` | — | Elevation |

---

## Step 3 — Use the tokens while building

Anywhere Elementor exposes a **Custom CSS** box (widget, container, or
site-wide) you can reference the tokens directly:

```css
/* On a Container's Custom CSS */
selector {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
}

/* A call-to-action button styled from tokens */
selector .elementor-button {
  background: var(--color-accent);
  color: var(--color-accent-fg);
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-5);
}
```

For most widgets you won't even need Custom CSS — once the Global Colors and
Fonts are mapped, picking "Primary" or "Text" in the widget's style panel
already pulls the Nordover value.

---

## Light / dark

Nordover flips theme via `:root:has(#dark:checked)` (or a `data-theme`
override in your own wrapper). In WordPress this usually isn't needed for a
marketing site — pick one mode. If you do want a dark section, wrap it and set
the surface/text tokens locally:

```css
selector {
  --color-bg: var(--color-fg);
  --color-fg: var(--color-bg);
  background: var(--color-bg);
  color: var(--color-fg);
}
```

---

## Gotchas

- **Custom CSS variables defined in the Customizer's “Additional CSS”** are
  usable in Elementor Custom CSS fields, but they won't appear inside
  Elementor's Global managers. Define them once (Step 1) and they cascade.
- **Don't paste the component CSS** (`components-*.css`) expecting `.btn`/`.card`
  to style Elementor widgets — the widget markup differs. Tokens are the
  contract that travels cleanly.
- **Keep the token names** as the single source of truth. When the design
  system updates a value, update it in one place (Step 1) and the whole site
  follows.
- Match the package to the project: `tokens-web.css` (airy, editorial) for
  marketing sites; `tokens-app.css` (compact) only for dashboard-like builds.

---

## Summary

1. Load `tokens-web.css` once in Site Settings → Custom CSS.
2. Recreate Nordover's semantic colours/fonts as Elementor Global Colors/Fonts.
3. Build with native Elementor widgets; reference `var(--…)` where you need
   custom styling.

You get Nordover's visual foundation across your WordPress site without
fighting Elementor's markup — the same tokens your apps and sites use.
