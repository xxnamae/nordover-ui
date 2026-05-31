# STYLEGUIDE VALIDATION CHECKLIST

Use this checklist to verify styleguide completeness before merging any CSS changes.

---

## Pre-Merge Validation

### 1. CSS Changes Identified ✓
- [ ] What CSS files were changed? (components-web.css, components-app.css, tokens-*.css)
- [ ] List each new or modified component/utility:
  - Component/Utility 1: `[description]`
  - Component/Utility 2: `[description]`

### 2. Styleguide Changes Made ✓
- [ ] Are styleguide changes in the same commit as CSS changes?
- [ ] Which styleguides were updated?
  - [ ] styleguide-web.html
  - [ ] styleguide-app.html
  - [ ] Both (if component is in both)

### 3. Example Quality Check ✓

For each component/utility added or modified:

- [ ] **Example exists**: Is there an HTML example showing the component?
- [ ] **Uses framework only**: Does the example use ONLY framework classes? (No inline styles)
- [ ] **All variants shown**: Are all documented variants included?
  - If color token: all color swatches shown
  - If button: all sizes and variants shown
  - If form element: base + error state shown
  - If utility: example of usage shown
- [ ] **States documented**: Are interactive states shown?
  - [ ] Hover state (if interactive)
  - [ ] Active state (if interactive)
  - [ ] Disabled state (if applicable)
  - [ ] Error state (if applicable)
  - [ ] Focus state (if interactive, especially form elements)
- [ ] **Responsive shown**: Are responsive variants documented?
  - [ ] Mobile view (default, mobile-first)
  - [ ] Desktop view (48rem breakpoint)
- [ ] **Dark mode shown**: If component has dark mode variant:
  - [ ] Light mode example
  - [ ] Dark mode example

### 4. Organization ✓

- [ ] Is the component placed in the correct section?
  - [ ] Foundation (colors, typography, spacing, motion)
  - [ ] Components (UI elements)
  - [ ] Layout (primitives and patterns)
  - [ ] Utilities (utility classes)
- [ ] Is there a clear heading (h2 or h3)?
- [ ] Is the section logically organized if multiple examples?

### 5. Rendering Validation ✓

Test the rendered styleguide:
- [ ] Open the styleguide in browser (web and app if both updated)
- [ ] Visual appearance matches CSS intent
- [ ] No broken layouts
- [ ] All text is readable
- [ ] Colors display correctly
- [ ] Component examples are clear

### 6. Mobile Responsiveness ✓

For styleguides as a whole:
- [ ] Styleguide renders on mobile (320px width)
- [ ] Styleguide renders on tablet (768px width)
- [ ] Styleguide renders on desktop (1024px width)
- [ ] Navigation is usable on all sizes
- [ ] Examples are visible/readable on all sizes

### 7. Coverage Consistency ✓

- [ ] If component added to both web/app CSS:
  - [ ] Is it documented in both styleguides?
  - [ ] Do examples reflect platform differences (web: light/generous vs app: dark/compact)?
- [ ] If component is responsive:
  - [ ] Are both mobile and desktop examples shown?
- [ ] If component has multiple states:
  - [ ] Are all documented states shown?

### 8. Code Review Checklist ✓

Reviewer: Verify before approval:
- [ ] Commit message clearly describes CSS changes and styleguide updates
- [ ] CSS changes are in framework file (components-*.css or tokens-*.css)
- [ ] Styleguide changes are in same commit
- [ ] No inline CSS in styleguide HTML
- [ ] Examples are syntactically correct HTML
- [ ] All referenced classes exist in framework CSS
- [ ] Changes follow mirroring rule (web/app in sync if applicable)
- [ ] This PR maintains or improves coverage %

---

## Coverage Audit (Run if Adding Large Component Set)

If adding many components at once, run a coverage count:

### Web Styleguide Coverage

Count approximate sections:
```
Foundation: _____ items documented
Components: _____ items documented  
Layout: _____ items documented
Utilities: _____ items documented
Patterns: _____ items documented

Total documented: _____ / 316 (target: 100%)
Current %: _____ %
Previous %: [from audit file]
```

### App Styleguide Coverage

```
Foundation: _____ items documented
Components: _____ items documented
Layout: _____ items documented
Utilities: _____ items documented
Patterns: _____ items documented

Total documented: _____ / 268 (target: 100%)
Current %: _____ %
Previous %: [from audit file]
```

---

## Common Issues & Fixes

### ❌ Inline CSS in Styleguide
```html
<!-- WRONG -->
<div style="color: red; font-size: 18px;">Text</div>

<!-- RIGHT -->
<div class="text-error">Text</div>
```

### ❌ Missing Class Definitions
```html
<!-- WRONG - class doesn't exist in framework -->
<button class="btn-custom-blue">Click me</button>

<!-- RIGHT - use framework class -->
<button class="btn btn--primary">Click me</button>
```

### ❌ Incomplete Examples
```html
<!-- WRONG - only shows one variant -->
<input class="form-input" placeholder="Text input">

<!-- RIGHT - shows variants and states -->
<input class="form-input" placeholder="Normal state">
<input class="form-input is-error" placeholder="Error state">
<input class="form-input" placeholder="Disabled" disabled>
```

### ❌ Missing Mobile/Responsive
```html
<!-- WRONG - only works on desktop -->
<div class="flex gap-8">...</div>

<!-- RIGHT - shows mobile example too -->
<div class="flex gap-2 md:gap-8">...</div>
<!-- And explain mobile: gap-2, desktop: gap-8 -->
```

---

## Approval Criteria

A styleguide update is approved when:

1. ✅ CSS and styleguide changes are in same commit
2. ✅ All examples use framework classes only (no inline styles)
3. ✅ Examples match CSS behavior and intent
4. ✅ Mobile rendering works correctly
5. ✅ Coverage is maintained or improved
6. ✅ Mirroring rule followed (web/app in sync)
7. ✅ No broken links or syntax errors
8. ✅ Examples are clear and representative

---

## After Merge

- [ ] Update `docs/visual/STYLEGUIDE-AUDIT-*.md` with new coverage %
- [ ] If major changes, note in CHANGELOG or release notes
- [ ] Notify consuming agents/teams of framework updates
- [ ] Verify no regressions in dependent projects

---

## Quick Reference

**Remember:** Styleguides are the ONLY documentation users see. Every component must be:
- **Visible** - Appears in styleguide
- **Complete** - All variants and states shown
- **Usable** - HTML example they can copy
- **Current** - Matches actual framework CSS
