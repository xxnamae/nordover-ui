# Format Contract — Token & Class Stability Guarantee

**Status:** Canonical, Stable, Machine-Parseable  
**Version:** 3.0  
**Updated:** 2026-06-12

---

## Purpose

This document defines the **format contract** — a stability guarantee for token names, class names, and token file formats. It ensures:

1. **Consumers can parse tokens programmatically** (Token Studio, design platforms, build systems)
2. **Tokens and classes are stable contracts** (safe to import, bundle, depend on)
3. **Format changes are versioned** (no surprise breaking changes)
4. **Deprecation is explicit** (clear migration paths)

---

## Token Contract (CSS Custom Properties)

### Stable Naming Pattern

All token names follow a **semantic, hierarchical pattern**:

```
--{semantic}-{modifier}?-{state}?
--{semantic}
```

**Examples:**

| Token | Category | Semantic | Modifier | State | Usage |
|-------|----------|----------|----------|-------|-------|
| `--color-accent` | Color | accent | — | — | Primary buttons, links, highlights |
| `--color-accent-hover` | Color | accent | — | hover | Hover state derivative |
| `--color-accent-active` | Color | accent | — | active | Active state derivative |
| `--accent-subtle` | Color | accent | subtle | — | Background tint |
| `--accent-muted` | Color | accent | muted | — | Reduced emphasis |
| `--shadow-md` | Shadow | shadow | md | — | Medium elevation |
| `--text-lg` | Typography | text | lg | — | Large font size |
| `--spacing-lg` | Spacing | spacing | lg | — | Large gap |

### Guarantees

✅ **Naming stability:** Token names will not change within a major version. Breaking renames only in `N.0.0`.

✅ **Semantic meaning:** Token names describe their purpose (not implementation). `--color-accent` means "primary action color" regardless of the actual RGB value.

✅ **Hierarchical:** Tokens at the same semantic level share a prefix (`--color-*`, `--shadow-*`, `--text-*`).

✅ **No abbreviations:** Names are spelled out (`--color-accent`, not `--clr-acc`). Enables searching and autocomplete.

✅ **Derivatives only via `-hover`, `-active`, `-subtle`, `-muted`, `-strong`** — no arbitrary suffixes.

---

## Class Contract (CSS Selectors)

### Stable Naming Pattern

All component classes follow a **semantic, state-based pattern**:

```
.{component}
.{component}-{variant}
.{component}.is-{state}
```

**Examples:**

| Class | Component | Variant | State | Usage |
|-------|-----------|---------|-------|-------|
| `.btn` | Button | — | — | Default button |
| `.btn-primary` | Button | primary | — | Primary action button |
| `.btn-secondary` | Button | secondary | — | Secondary button |
| `.btn.is-active` | Button | — | active | Active state |
| `.btn.is-disabled` | Button | — | disabled | Disabled state |
| `.form-input` | Form input | — | — | Default text input |
| `.form-input.is-error` | Form input | — | error | Error state |
| `.modal.is-open` | Modal | — | open | Visible modal |
| `.table-zebra` | Table | zebra | — | Striped table |
| `.t-heading-lg` | Typography | heading-lg | — | Large heading |
| `.t-body-sm` | Typography | body-sm | — | Small body text |

### Guarantees

✅ **Naming stability:** Class names are contracts. Changes only in major versions.

✅ **Semantic meaning:** Classes describe **what** not **how** (`.btn-primary` not `.btn-blue`).

✅ **State decoupling:** States use `.is-*` prefix (`.is-active`, `.is-disabled`, `.is-error`). Decoupled from component name.

✅ **No abbreviated classes:** Full names enable searching, IDE autocomplete, and clarity.

✅ **Utilities separate from components:** Component classes live in `components-*.css` with semantic intent. Utility classes live in separate `utilities-*.css` file (if needed).

✅ **Modifiers are `-` delimited:** `.btn-primary`, `.btn-secondary` (not `.btn_primary`, `.btn.primary`).

---

## Token File Format Contract

### CSS Variable Format

Tokens are expressed as **native CSS custom properties** in `tokens-*.css`:

```css
:root {
  --color-accent: #0066ff;
  --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);
  --shadow-md: 0 2px 4px 0 rgba(0,0,0,0.1);
}
```

**Guarantees:**

✅ **Valid CSS syntax:** All values are valid CSS (colors, sizes, shadows, gradients, calc expressions).

✅ **Browser-native:** No preprocessing required. Works in all modern browsers (CSS custom properties, `color-mix()`, `calc()`).

✅ **Composable:** Tokens reference other tokens via `var()` to avoid duplication (e.g., `--color-accent-hover` references `--color-accent`).

✅ **Dark mode support:** Theme-specific values switch via CSS cascade (`.light` / `.dark` selectors).

### JSON Token Format (DTCG)

Tokens are exported as **DTCG-compliant JSON** in `tokens-*.json` for machine consumption:

```json
{
  "color": {
    "accent": {
      "$value": "#0066ff",
      "$type": "color"
    },
    "accent-hover": {
      "$value": "color-mix(in oklch, var(--color-accent) 85%, white)",
      "$type": "color",
      "$extensions": {
        "com.nordover.cssText": true
      }
    }
  }
}
```

**Guarantees:**

✅ **DTCG-compliant schema:** Follows `$value`, `$type`, `$description` standard.

✅ **Derivable:** Tokens computed from source CSS via `scripts/build_tokens.py` (CSS is source of truth).

✅ **Machine-parseable:** Design tools, token studios, and build systems can consume JSON directly.

✅ **Round-trippable:** Export to JSON, re-import to CSS without loss.

✅ **Generated, not hand-edited:** JSON is auto-generated. Hand edits are overwritten on next build. Edit the CSS source instead.

---

## Component Contract

### HTML Structure Guarantee

Components ship as **semantic HTML + CSS** (no JavaScript dependencies):

```html
<button class="btn btn-primary" aria-label="Submit">
  Send
</button>
```

**Guarantees:**

✅ **Semantic HTML:** `<button>`, `<input>`, `<form>`, `<nav>` — not `<div>` elements styled as buttons.

✅ **ARIA labels:** Interactive elements include `role`, `aria-label`, `aria-pressed`, etc.

✅ **Keyboard accessible:** Tab order, Enter/Escape activation, focus states all functional.

✅ **CSS-only:** No JavaScript required (buttons, toggles, dropdowns, modals all pure CSS + HTML).

✅ **Responsive:** Layouts adapt to 3 breakpoints (mobile <576px, tablet 576–1024px, desktop >1024px).

---

## Stability Timeline

| Phase | Duration | Action | Example |
|-------|----------|--------|---------|
| **Current Release** | — | Use the token/class normally | `--color-accent` works as expected |
| **+1 minor release** (8 weeks) | Deprecation window | Token marked `@deprecated` in comments | `--text-8xl /* @deprecated since v3.2.0 */` |
| **+2 minor releases** (16 weeks) | Removal phase | Token deleted. Changelog documents removal. | v3.3.0 removes `--text-8xl`, users must update to `--text-7xl` |

---

## Breaking Changes (Rare)

Breaking changes (token removals, class renames, format changes) only occur in **major versions** (X.0.0):

- Announced in prior release notes
- Documented in `CHANGELOG.md` under "Breaking Changes"
- Migration guide provided in `docs/wiki/decisions/`
- Example: v2 → v3 redesign had new color semantics, documented in `2026-03-01-color-semantic-rework.md`

---

## Verification

### How to Verify Token Stability

```bash
# Tokens are checked at CI time
npm run check:tokens

# Output: ✅ tokens-web.json matches tokens-web.css
#         ✅ tokens-app.json matches tokens-app.css
```

### How to Verify Class Names Are Stable

```bash
# Extract all class names from styleguide
grep -oE '\.[a-z][a-z0-9-]*' docs/visual/styleguide.html | sort -u

# Export from CSS components
grep -oE '\.[a-z][a-z0-9-]*' docs/visual/components/*.css | sort -u

# These must match (1:1 parity between styleguide and CSS)
```

---

## Consumer Responsibilities

If you **import Nordover tokens or classes**, you should:

1. ✅ **Lock to a major version** in `package.json`:
   ```json
   "nordover": "~3.0.0"
   ```

2. ✅ **Subscribe to deprecation notices** — watch `docs/wiki/decisions/` for `@deprecated` notices.

3. ✅ **Plan for major version upgrades** — test before upgrading X.0.0.

4. ✅ **Report breaking changes** — if you find a token/class broken mid-version, file an issue.

---

## Derivable Tokens (No Contract)

The following are **derived** from base tokens and are **not contracted**:

- Computed colors via `color-mix()`
- Contrast ratio variants (`--error-subtle`, `--error-strong`)
- Gradient fills
- Shadow stacks
- Type scale derivatives (e.g., `--text-sm` derives from `--text-base`)

These **can change** to improve aesthetics or accessibility. The **base tokens** (`.color-accent`, `--text-base`, `--shadow-base`) are stable.

---

## Specification Documents

- **Token Spec:** `docs/visual/TOKEN-SPEC.md`
- **Component Spec:** `docs/visual/SYSTEM.md`
- **Deprecation Policy:** `docs/wiki/decisions/2026-06-12-deprecation-policy.md`
- **Elementor Integration:** `docs/handoff/ELEMENTOR-TEMPLATE-LIBRARY.md`

---

## Contact / Questions

- **Token changes:** File issue in `nordover-ui` repo
- **Breaking changes:** See migration guides in `docs/wiki/decisions/`
- **Consumer feedback:** Discussions in `nordover-ui` repo welcome

---

**This contract is binding for v3.x. Changes documented in CHANGELOG.md.**
