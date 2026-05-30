# Styleguide Maintenance Policy

**Status:** Active Policy  
**Purpose:** Ensure styleguides are always authoritative, complete references of the framework

## Core Principle

**Styleguides are the single source of truth for what exists in Nordover.**

If a component exists in `components-web.css` or `components-app.css`, it **MUST** be shown in the corresponding styleguide. If it's not in a styleguide, it doesn't exist for users.

---

## Styleguide Files

| File | Framework | Purpose |
|------|-----------|---------|
| `styleguide-web.html` | tokens-web.css + components-web.css | Editorial sites, marketing, content-rich apps |
| `styleguide-app.html` | tokens-app.css + components-app.css | SaaS, dashboards, data-dense interfaces |

Both must be linked to canonical CSS files (not embedded):
```html
<link rel="stylesheet" href="./tokens/tokens-web.css">
<link rel="stylesheet" href="./components/components-web.css">
```

---

## Required Component Coverage

### All styleguides must include:

**Foundation (Tokens & System)**
- ✅ Colors & grayscale with swatches
- ✅ Typography (all classes)
- ✅ Spacing scale
- ✅ Motion system with demos
- ✅ Icons with sizing and color variants

**Interactive Components**
- ✅ Buttons (all variants × sizes)
- ✅ Forms (inputs, checkboxes, radios, selects, toggles, switches)
- ✅ Form validation (errors, help text, disabled states)
- ✅ Badges (all color variants)
- ✅ Tags & Tag Input
- ✅ Alerts (all types)

**Data Display**
- ✅ Tables (standard + responsive)
- ✅ Pagination
- ✅ Data filtering UI (if exists)
- ✅ Inline editing hooks (if exists)

**Complex Components**
- ✅ Modals & Dialogs (with states)
- ✅ Accordions/Details
- ✅ Date Picker
- ✅ File Upload
- ✅ Stepper (multi-step)
- ✅ Search Bar with results

**Patterns & Sections**
- ✅ Hero sections (centered, split, editorial)
- ✅ Feature grids
- ✅ CTA cards
- ✅ Pricing cards
- ✅ FAQ/Accordion
- ✅ Blog cards (web only)
- ✅ Testimonials (web only)
- ✅ Timeline (web only)
- ✅ Footer (web only)
- ✅ Mobile navigation drawer
- ✅ Breadcrumbs
- ✅ Tabs
- ✅ Empty states

**Utilities & Helpers**
- ✅ Layout utilities (.stack, .cluster, .grid-auto, .page)
- ✅ Display utilities (.flex, .block, .hidden, etc.)
- ✅ Spacing utilities (.gap-*, .m-*, .p-*)
- ✅ Typography utilities (.text-center, .uppercase, .truncate, etc.)
- ✅ Animation utilities (.animate-fade-in, .slide-in-*, .bounce-in)
- ✅ Color utilities (.text-accent, .bg-subtle, etc.)
- ✅ Sizing utilities (.w-full, .max-w-*)
- ✅ Shadow utilities (.shadow-sm, .shadow-md)

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

Before declaring styleguides "complete," verify:

- [ ] All classes in CSS file have corresponding demo
- [ ] All variants are shown (color, size, state)
- [ ] All interactive states visible (hover, focus, active, disabled)
- [ ] Responsive behavior demonstrated (if applicable)
- [ ] Dark mode works (toggle in top-right)
- [ ] Mobile navigation works (hamburger menu)
- [ ] No broken links or missing icons
- [ ] Component descriptions are accurate
- [ ] CSS class names are documented

---

## Why This Matters

**Without complete styleguides:**
- Users don't know what components exist
- Developers duplicate work (re-implement what already exists)
- Framework appears incomplete/immature
- "What does Nordover provide?" becomes unanswerable
- Quality perception drops (10/10 → 6/10)

**With complete styleguides:**
- Users discover all available components instantly
- Clear reference for what works
- Builds confidence in framework completeness
- Developers can copy-paste live examples
- Framework appears production-ready

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
| 2026-05-30 | Policy created. Styleguides migrated to canonical CSS. Component coverage audit shows ~40 components exist but <15 are documented. |

