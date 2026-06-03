# ADR: Web vs. App Token Separation

**Date:** 2026-06-03  
**Status:** ACCEPTED  
**Affects:** tokens-web.css, tokens-app.css, components-web.css, components-app.css  

## Context

Nordover maintains separate CSS token and component files for web (editorial/marketing) and app (SaaS/dashboard) contexts. This decision documents why separation is architecturally sound and not technical debt.

### The Question
Should we consolidate tokens-web.css + tokens-app.css into a single `tokens-shared.css` + platform-specific overrides, similar to design system consolidation practices?

## Decision

**Keep platforms separate.** Do not attempt to extract a shared tokens file.

### Data-Driven Rationale

#### 1. Token-Level Separation

**Type Scale (Typography)**
```css
/* WEB: Fluid, editorial scale */
--text-base: 1rem;
--text-lg: clamp(1.125rem, 1.089rem + 0.18vw, 1.25rem);
--text-xl: clamp(1.25rem, 1.18rem + 0.36vw, 1.5rem);
/* ... scales up to 10rem for hero displays */

/* APP: Static, compact scale */
--text-base: 0.875rem;  /* 14px */
--text-md: 1rem;        /* 16px */
--text-lg: 1.125rem;    /* 18px */
/* ... caps at 3.75rem for dashboard density */
```

**Why:** Web prioritizes visual hierarchy and readability for editorial flow. App prioritizes information density and quick scanning for productive workflows.

**Consequence:** A "shared" type-scale would be compromise — too airy for app, too cramped for web.

---

**Spacing (Gap, Padding, Margin)**
```css
/* WEB: Generous, breathing room */
--gap-component: 1.5rem;
--space-4: 1rem;
--space-5: 1.5rem;

/* APP: Compact, information-dense */
--gap-component: 1rem;
--space-3: 0.75rem;
--space-4: 1rem;
```

**Consequence:** All component `.padding` and `.margin` rules differ. 60% of component CSS is due to this spacing strategy.

---

**Color Accent**
```css
/* WEB */
--color-accent: var(--gray-900);  /* Neutral black — minimalist */

/* APP */
--color-accent: oklch(0.50 0.22 260);  /* Brand blue — SaaS-specific */
```

**Consequence:** Button, link, focus-ring, and accent colors across both packages differ by design.

---

**Semantic Colors (Even Primitives)**

All of error, success, warning, info colors differ between platforms — tuned for each's light/dark defaults:

```css
/* WEB (light default) */
--error: oklch(0.55 0.22 28);
--success: oklch(0.56 0.16 160);

/* APP (dark default) */
--error: oklch(0.62 0.23 25);
--success: oklch(0.66 0.18 155);
```

These are not interchangeable; they've been selected to maintain WCAG AA contrast against each platform's `--color-bg`.

#### 2. Component-Level Separation

Linjeulikheter: **2163 of 3591 (60% genuinely different)**

Sources of divergence:
- `.grid-auto` column width: `16rem` (web) vs `14rem` (app)
- Button `.padding`: `var(--space-4)` (web) vs `var(--space-3)` (app)
- Card `.margin-bottom`: `var(--space-4)` (web) vs `var(--space-3)` (app)
- Button surface (`.button-primary`): flat design (web) vs tactile with raised effect (app)
- Modal backdrop blur: present (web) vs absent for performance (app)

#### 3. The "Shared File" Fallacy

If we attempted consolidation:

```css
/* ❌ This is what would happen */
.button-primary {
  padding: var(--button-padding-x, var(--space-4)) var(--button-padding-y, var(--space-3));
  background: var(--button-bg-web, blue);
  /* ... dozens of conditional fallbacks ... */
}
```

**Cost-Benefit:**
- **Savings:** ~1000 lines of duplicated CSS selectors
- **Cost:** 50+ new conditional tokens, harder to debug, slower CSS parsing, brittle
- **Net:** Negative. Separation wins.

---

## Constraints Respected

1. **Token-Name Consistency:** Both platforms declare the same 153 token names (in `:root`). This ensures portability.
2. **Layer Architecture:** Both use identical `@layer reset, tokens, utilities` structure.
3. **JSON Export:** `build_tokens.py` already handles per-platform JSON generation from separate CSS sources.
4. **Dark Mode:** Both use `:root:has(#dark:checked)` for theme switching (no `prefers-color-scheme` coupling).

---

## What This Enables

✅ **Field-Optimized Design:** Each platform can be best-in-class for its use case.
✅ **Independent Versioning:** Web and app tokens can evolve separately if needed.
✅ **Low Refactor Risk:** Changing web spacing doesn't inadvertently affect app.
✅ **Clear Contracts:** Implementers know exactly which file to import.

---

## What This Costs

- **Maintenance burden:** Token changes must be applied to both files if they affect shared names.
- **Coordination risk:** If a token name is added to one platform, the other's build may fail.

*Mitigation:* See `TOKEN-CONSISTENCY.md` for governance and CI checks.

---

## Alternatives Considered

### A) Unified Token File + CSS Variables

**Idea:** Single `tokens-shared.css` with platform-specific CSS variable overrides.

**Rejected because:**
- Increases cognitive load (which tokens are conditional?)
- Makes dark-mode overrides complex (nested `:root:has()` selectors)
- No actual code savings (variables still need definitions)
- Breaks the "read-once, trust-always" property of the current CSS

### B) Token Studio / Figma Plugin

**Idea:** Use design tool integration to generate web/app tokens from a single source.

**Status:** Future consideration. Current manual maintenance is acceptable. Revisit if token count exceeds 300.

### C) Monorepo with Shared Primitives

**Idea:** `tokens-primitives.css` (colors, radii, shadows) + platform-specific `tokens-web.css`, `tokens-app.css`.

**Rejected because:**
- Only ~30 lines would be truly shared (remaining colors have platform-specific mix() derivations)
- Adds one more file to the build chain
- No significant maintenance benefit

---

## Recommendations for Implementers

1. **When adding a new token:**
   - Declare it in both `tokens-web.css` and `tokens-app.css`
   - If platform-specific, document in the token's comment: `/* App only */`

2. **When changing a token value:**
   - Apply to both files in the same commit
   - If change is platform-specific, run `npm run build:tokens` immediately

3. **When reviewing a token PR:**
   - Check both files were modified (except for platform-exclusive tokens)
   - Verify `tokens-*.json` was regenerated

---

## Future Reconsideration

Revisit this decision if:
- Token count exceeds 300 and maintenance overhead becomes severe
- A third platform (native iOS/Android) needs token support (consolidation becomes more critical)
- Token Studio / Figma integration becomes standard workflow

---

**Related:**
- `docs/visual/tokens/TOKEN-CONSISTENCY.md` — governance and shared names
- `docs/visual/tokens/README.md` — consumer guide
- `scripts/build_tokens.py` — how JSON is generated
