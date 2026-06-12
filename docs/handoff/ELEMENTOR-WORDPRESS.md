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

## Quick start — Which version are you using?

| You're using | Path | Effort |
|---|---|---|
| **Elementor v3** (older, Classic Editor) | Token paste + manual Global Color/Font mapping | ~30 min setup |
| **Elementor v4** (new, with Editor V4) | JSON import (automatic) or token paste | ~5 min setup (JSON) or ~30 min (manual) |

**Check your version:** Elementor → Dashboard → About → Version number. Or open
the editor; if you see a "Variables Manager" or "Global" menu, it's v4.

---

## Elementor v3 — Token paste + manual mapping

### Step 1 — Load the tokens once (site-wide)

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

> **Shortcut:** the [styleguide](https://xxnamae.github.io/nordover-ui/docs/visual/styleguide.html)
> has a one-click **"Copy tokens for Elementor / WordPress"** block in its
> *Documentation* section. It serves the selected package (Web/App) already
> flattened — no `@layer` wrapper, no reset — which is exactly option B,
> paste-ready.

Either way you now have the full token set available globally.

### Step 2 — Map the core tokens into Elementor's managers (v3 only)

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

### Step 3 — Use the tokens while building (v3 & v4)

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

## Elementor v4 — JSON import (recommended)

If you're using **Elementor 3.33+ with Editor V4**, the fastest path is to
**import a pre-made Variables Manager JSON** that gives you all Nordover tokens
as native variables. No manual mapping needed.

### Step 1 — Import the variables JSON

1. Go to **Elementor → Dashboard → Kits**
2. Open your site kit (or create one)
3. **Tools → Import** (or use WordPress admin **Tools → Import**)
4. Upload `nordover-elementor-v4-web.json` or `nordover-elementor-v4-app.json`
   - **v4-web.json** for marketing/editorial sites (airy spacing, large type)
   - **v4-app.json** for dense app-like dashboards (compact spacing)
5. After import, **Tools → Regenerate CSS & Data** (Elementor rebuilds the CSS)

All 254 Nordover tokens are now available in every color/typography/size picker.

### Step 2 — Use the variables while building

When you open the editor:
- **Color picker** → you see *Nordover colors* (color-accent, color-success, etc.)
- **Typography panel** → you see *Nordover fonts and sizes* (text-base, text-2xl, etc.)
- **Spacing fields** → you see *Nordover spacing scale* (space-4, space-8, etc.)

Pick from the list instead of typing pixel values.

### What the JSON contains

| Variable type | Examples | Notes |
|---|---|---|
| `global-color-variable` | color-accent, color-fg, color-success | Colours resolved to hex (no OKLCH runtime) |
| `global-font-variable` | font-sans, font-display | Font family names (first in stack) |
| `global-size-variable` | space-4, space-8, radius-md | Simple pixel/rem values |
| `global-custom-size-variable` | text-4xl, text-lg | Fluid sizes (keep `clamp()`) |

**Not included in JSON** (use Custom CSS instead):
- Font weights, line-height, letter-spacing
- Motion (durations, easings)
- Shadows, gradients, glass
- Dark mode overrides

### Regenerate when tokens change

Whenever Nordover's tokens update, regenerate the JSON:
```bash
npm run build:elementor  # in the nordover-ui repo
```

Upload the new JSON to your Elementor kit (re-import replaces old variables).
CI ensures the JSON stays in sync with the CSS.

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

## Gotchas (both v3 & v4)

- **Don't paste the component CSS** (`components-*.css`) expecting `.btn`/`.card`
  to style Elementor widgets — the widget markup differs. Tokens are the
  contract that travels cleanly.
- **Keep the token names** as the single source of truth. When the design
  system updates a value, update it in one place and the whole site follows.
- Match the package to the project: `tokens-web.css` or `v4-web.json` (airy,
  editorial) for marketing sites; `tokens-app.css` or `v4-app.json` (compact)
  only for dashboard-like builds.
- **v4 JSON limitations:** colours are pre-resolved hex (no OKLCH runtime), no
  dark-mode variants per variable, and shadows/motion/glass aren't included.
  Use Custom CSS paste for those.

---

## Summary

| Scenario | Steps | Files |
|---|---|---|
| **v3 (Classic Editor)** | 1. Paste tokens CSS<br>2. Map colors/fonts manually<br>3. Build with Elementor widgets | `tokens-web.css` or `tokens-app.css` |
| **v4 (Editor V4)** | 1. Import JSON into Variables Manager<br>2. Build with Elementor widgets | `nordover-elementor-v4-web.json` or `nordover-elementor-v4-app.json` |

You get Nordover's visual foundation across your WordPress site without
fighting Elementor's markup — the same tokens your apps and sites use.
