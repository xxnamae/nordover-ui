# Styleguide Maintenance Policy

**Status:** Active Policy (Updated 2026-06-04)  
**Purpose:** Ensure styleguides are authoritative references of the framework building blocks

## Core Principle

**The styleguide is the single source of truth for what exists in Nordover.**

If a component exists in `components-web.css` or `components-app.css`, it **MUST** be shown in the styleguide. If it's not documented, it doesn't exist for users.

---

## Styleguide Architecture

| File | Purpose | Scope |
|------|---------|-------|
| **`styleguide.html`** (primary) | Unified reference for tokens + components | Both web and app with package switcher |
| `styleguide-web.html` | Legacy reference (deprecated) | Keep for backward compatibility during transition |
| `styleguide-app.html` | Legacy reference (deprecated) | Keep for backward compatibility during transition |

The new unified styleguide must be linked to canonical CSS files (not embedded):
```html
<link rel="stylesheet" href="./tokens/tokens-web.css" id="token-stylesheet">
<link rel="stylesheet" href="./components/components-web.css">
<link rel="stylesheet" href="./styleguide-chrome.css">
```

---

## Required Component Coverage

Per ADR 2026-06-04 (rammeverk-fokus-byggesteiner), Nordover focuses on Layer 1 + Layer 2 only:
- **Layer 1:** Tokens (colors, typography, spacing, motion, etc.)
- **Layer 2:** Building blocks (reusable primitives)
- **Layer 3:** Patterns (removed — projects compose their own)

### Styleguide must document:

**Foundation (Layer 1: Tokens)**
- ✅ Colors & semantic swatches (light/dark mode)
- ✅ Typography scale (display, heading, body, caption)
- ✅ Spacing & sizing scales
- ✅ Motion durations & easing
- ✅ Shadows, radius, borders

**Interactive Components (Layer 2: Building Blocks)**
- ✅ Buttons (all variants: primary, secondary, ghost, tonal, elevated, link; all sizes)
- ✅ Forms (inputs, checkboxes, radios, selects, textarea, switches)
- ✅ Badges (all color variants)
- ✅ Alerts (all severity levels: success, error, warning, info)
- ✅ Tags & Tag Input
- ✅ Cards (default, elevated, bordered, subtle)

**Data Display (Layer 2)**
- ✅ Tables (standard HTML tables with optional styling)
- ✅ Pagination
- ✅ Avatar (all sizes)
- ✅ Skeleton (loading placeholders)
- ✅ Empty states (icon, title, description)
- ✅ Breadcrumbs
- ✅ Tooltip

**Complex Components (Layer 2)**
- ✅ Modals & Dialogs (with header, content, footer)
- ✅ Accordions/Details
- ✅ Tabs
- ✅ Date Picker
- ✅ File Upload
- ✅ Stepper (multi-step process)
- ✅ Search Bar
- ✅ Menu/Dropdown
- ✅ Toast/Notification
- ✅ Kbd (keyboard key styling)

**Navigation (Layer 2)**
- ✅ Breadcrumbs
- ✅ Tabs
- ✅ Mobile navigation patterns

**Layout Utilities (Layer 2)**
- ✅ Layout primitives (.stack, .cluster, .grid-auto, .page, .section)
- ✅ Display utilities (.flex, .block, .hidden, .invisible)
- ✅ Spacing utilities (.gap-*, .m-*, .p-*, .mb-*, .mt-*)
- ✅ Typography utilities (.text-center, .text-left, .uppercase, .truncate)
- ✅ Animation utilities (.animate-fade-in, .slide-in-up, .scale-in)
- ✅ Responsive utilities

**NOT Documented (Layer 3: Removed)**
- ❌ Patterns: Hero sections, pricing grids, blog cards, testimonials, feature grids, CTA cards, timelines, dashboard layouts
- ❌ Page compositions (complete layouts — users compose these from building blocks)

---

## When Adding Components

**Every new component must:**

1. Be added to `components-web.css` or `components-app.css` (or both)
2. Have a demo section in the corresponding styleguide HTML
3. Show all variants, sizes, and states
4. Include live, interactive demos (not just screenshots)
5. Document CSS class names used

**Styleguide updates are a release requirement.** You cannot ship a new component without updating styleguides.

---

## Styleguide Structure

```html
<section class="doc-section" id="component-name">
  <h2 class="doc-section-title">Component Name</h2>
  <p class="doc-section-desc">Brief description of use case</p>
  
  <!-- Chips showing CSS class names -->
  <div class="chips">
    <span class="chip">.btn</span>
    <span class="chip">.btn-primary</span>
    <span class="chip">.btn-sm</span>
  </div>
  
  <!-- Live demo section -->
  <div class="doc-demo stack">
    <!-- All variants, sizes, states -->
    <button class="btn btn-primary">Primary</button>
    <button class="btn btn-secondary">Secondary</button>
    <!-- ... -->
  </div>
  
  <!-- Optional: specs table -->
  <table class="props-table">
    <thead><tr><th>Class</th><th>Purpose</th></tr></thead>
    <tbody><!-- ... --></tbody>
  </table>
</section>
```

---

## Validation Checklist

Before declaring styleguide complete, verify for **building blocks only** (Layer 2):

- [ ] All button variants documented (primary, secondary, ghost, tonal, elevated, link)
- [ ] All button sizes shown (sm, default, lg)
- [ ] Form inputs complete (text, password, textarea, checkbox, radio, select, switch)
- [ ] Badges and alerts with all color variants
- [ ] Cards with all style variants (default, elevated, bordered)
- [ ] Tables render correctly with proper cell alignment
- [ ] Complex components functional (accordion opens/closes, tabs switch, date picker interactive)
- [ ] Token gallery displays all semantic colors
- [ ] Typography scale shows all levels
- [ ] Spacing and sizing scales visual
- [ ] Dark mode works (toggle in top-right)
- [ ] Mobile responsive (sidebar collapses on mobile, hamburger menu functional)
- [ ] No broken links or missing icons
- [ ] Component descriptions are accurate
- [ ] CSS class names clearly labeled in "chips"
- [ ] Package switcher works (web ↔ app token switching)

---

## Why This Matters

**Without a complete, accurate styleguide:**
- Users don't know what building blocks exist
- Developers reinvent components (pattern vs. block confusion)
- Framework appears incomplete or over-engineered (includes patterns when only blocks are shipped)
- "What is Nordover's actual scope?" becomes unclear
- Quality perception drops (foundation seems untrustworthy)

**With a complete styleguide documenting building blocks only:**
- Users instantly see what they can build with
- Clear boundary: tokens + blocks (foundation) vs. project patterns
- Builds confidence: framework is focused and maintainable
- Developers confidently compose projects on top (not fighting against "wrong" patterns)
- Framework appears mature, well-scoped, reusable

---

## Related Files

- `docs/visual/styleguide-web.html` — Web styleguide (editorial)
- `docs/visual/styleguide-app.html` — App styleguide (SaaS)
- `docs/visual/components/components-web.css` — Component CSS (source of truth)
- `docs/visual/components/components-app.css` — App component CSS (source of truth)
- `docs/visual/tokens/tokens-web.css` — Token definitions
- `docs/visual/tokens/tokens-app.css` — App token definitions

---

## Version History

| Date | Change |
|------|--------|
| 2026-06-04 | Unified styleguide created (building blocks only, no patterns per ADR 2026-06-04). New `styleguide.html` with web/app package switcher, token galleries, and zero inline styles. Legacy `styleguide-web.html` and `styleguide-app.html` marked deprecated. |
| 2026-05-30 | Policy created. Styleguides migrated to canonical CSS. Component coverage audit shows ~40 components exist but <15 are documented. |

