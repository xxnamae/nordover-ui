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

> **Shortcut:** the [styleguide](https://xxnamae.github.io/nordover-ui/docs/visual/styleguide.html)
> has a one-click **"Copy tokens for Elementor / WordPress"** block in its
> *Documentation* section. It serves the selected package (Web/App) already
> flattened — no `@layer` wrapper, no reset — which is exactly option B,
> paste-ready.

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

## Native Variables for Editor V4 (Elementor 3.33+/4.x)

If you run **Editor V4**, you don't have to map tokens by hand — Nordover ships
a ready-made **Variables Manager** import that recreates the whole token set as
native v4 variables (so they appear in every colour/typography/size picker).

**Files** (generated from the canonical CSS, never hand-edited):

| Package | File |
|---|---|
| Web (editorial) | `docs/handoff/nordover-elementor-v4-web.json` |
| App (dense UI) | `docs/handoff/nordover-elementor-v4-app.json` |

**Import:** Elementor → *Variables Manager* → import the JSON (or drop it into a
kit and use **Tools → Import**), then **Tools → Regenerate CSS & Data**.

**What you get** — four native variable types, mapped from the tokens:

| Elementor type | From | Example |
|---|---|---|
| `global-color-variable` | colours (OKLCH/`color-mix` **resolved to hex**) | `color-accent → #060709` |
| `global-font-variable` | font stacks (first family) | `font-display → Inter Tight` |
| `global-size-variable` | simple dimensions | `space-4 → 1rem` |
| `global-custom-size-variable` | fluid values (**`clamp()` kept intact**) | `text-4xl → clamp(2.25rem, …, 3.5rem)` |

**Regenerate** after any token change: `npm run build:elementor` (CI enforces
the JSON stays in sync with the CSS, exactly like the DTCG token JSON).

### Honest limitations of the native route

- **Colours are concrete hex.** Elementor v4 colour variables can't hold OKLCH
  or `color-mix()`, so they're pre-resolved. You lose the runtime-derived
  relationship (e.g. changing `--color-accent` no longer recomputes
  `accent-hover`); you get a faithful **snapshot** instead.
- **No light/dark per variable.** Each variable holds one value, so the export
  is the **light/base** set. Dark mode still needs the Custom-CSS route (with the
  `:has(#dark:checked)` block) or a duplicate variable set.
- **Excluded by design:** weights, line-height/letter-spacing, motion (durations/
  easings), shadows, gradients and glass — none map to a v4 variable *type*. Use
  the Custom-CSS paste for those.
- **`watermark` is best-effort.** Elementor recomputes its internal sync counter
  on import; the generated value is a placeholder.

> **Which route?** Native variables give the best **editing UX** (real pickers,
> on-brand by default). The Custom-CSS paste (top of this doc) is the most
> **faithful** (keeps fluid type, derived colours and dark mode). They're not
> exclusive — many teams import the variables *and* paste the CSS for the parts
> variables can't express.

---

## Summary

1. Load `tokens-web.css` once in Site Settings → Custom CSS (most faithful), **or**
   import `nordover-elementor-v4-web.json` into the Variables Manager (best UX).
2. Recreate Nordover's semantic colours/fonts as Elementor Global Colors/Fonts
   (only needed for the Custom-CSS route).
3. Build with native Elementor widgets; reference `var(--…)` where you need
   custom styling.

You get Nordover's visual foundation across your WordPress site without
fighting Elementor's markup — the same tokens your apps and sites use.
