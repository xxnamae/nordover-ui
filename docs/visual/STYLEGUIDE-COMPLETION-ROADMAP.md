# STYLEGUIDE COMPLETION ROADMAP

**Status:** 2026-05-31  
**Current Coverage:** App 46% (123/268), Web 4% (13/316)  
**Target:** 100% for both  
**Estimated Total Effort:** 15-20 hours

---

## Why This Matters

The styleguides are the **only place users see our framework**. If a component exists in CSS but not in styleguide, users will never discover it, and they'll ask us "why doesn't the framework have modals?" when it does.

This roadmap prioritizes high-impact work: hidden power components first, then utilities, then patterns.

---

## PRIORITY 1: Hidden Power Components (Tier 1J) — 2-3 hours

These are valuable, complex components that exist in CSS but are completely invisible.

### Web Styleguide
- [ ] **Modal/Dialog System** (4 classes)
  - `.modal`, `.modal-dialog`, `.modal-header`, `.modal-body`, `.modal-footer`
  - Show: basic modal, with title, with buttons, size variants
  - Add to: Components section

- [ ] **Advanced Data Table** (3 variants)
  - `.data-table-inline-edit`, `.data-table-filter`, `.data-table-sort`
  - Show: table with sort indicators, filter inputs, editable cells
  - Add to: Components section

- [ ] **Tag/Autocomplete Input** (4 classes)
  - `.tag-input`, `.tag`, `.tag-remove`, `.tag-suggestions`
  - Show: input with tags, adding tags, removing tags, suggestions
  - Add to: Components section

- [ ] **FAQ/Accordion** (3 classes)
  - `.faq-item`, `.faq-summary`, `.faq-answer`
  - Show: collapsed and expanded states, multiple items
  - Add to: Components section

### App Styleguide
Add same components if they exist in components-app.css

**Work items:** 8 components × ~15 min each = 2 hours

---

## PRIORITY 2: Missing Utility Classes — 3-4 hours

Utilities are the foundation of composition. Users can't build responsive layouts without them.

### Web Styleguide - New Utilities Section

**Display & Layout** (7 classes)
- [ ] `.flex`, `.flex-col`, `.flex-wrap`, `.flex-gap-*`
- [ ] `.grid`, `.grid-auto`
- [ ] `.block`, `.hidden`, `.inline`, `.inline-block`
- [ ] Show: flex row/col, flex wrap, grid auto, hidden elements

**Position Utilities** (5 classes)
- [ ] `.relative`, `.absolute`, `.fixed`, `.sticky`
- [ ] `.inset-0` (position: absolute; inset: 0)
- [ ] Show: overlays, sticky headers, modals

**Spacing Utilities** (20+ classes)
- [ ] `.gap-1` through `.gap-8`
- [ ] `.m-*`, `.mt-*`, `.mb-*`, `.ml-*`, `.mr-*`
- [ ] `.p-*`, `.pt-*`, `.pb-*`, `.pl-*`, `.pr-*`
- [ ] `.mx-auto`, `.my-auto`
- [ ] Show: gap examples, margin examples, padding examples, centering

**Typography Utilities** (10+ classes)
- [ ] `.font-bold`, `.font-semibold`, `.font-medium`, `.font-light`
- [ ] `.text-center`, `.text-left`, `.text-right`
- [ ] `.uppercase`, `.lowercase`, `.capitalize`
- [ ] `.truncate`, `.line-clamp-*`
- [ ] `.leading-tight`, `.leading-normal`, `.leading-loose`

**Color Utilities** (15+ classes)
- [ ] `.text-*` (text-primary, text-secondary, text-muted, text-error, text-success)
- [ ] `.bg-*` (bg-primary, bg-secondary, bg-muted, bg-error, bg-success)
- [ ] `.border-*` colors
- [ ] Show: color combinations with good contrast examples

**Border Utilities** (5+ classes)
- [ ] `.border`, `.border-t`, `.border-b`, `.border-l`, `.border-r`
- [ ] `.rounded`, `.rounded-sm`, `.rounded-lg`, `.rounded-full`
- [ ] Show: borders with different radii

**Shadow & Effects** (5+ classes)
- [ ] `.shadow-sm`, `.shadow-md`, `.shadow-lg`
- [ ] `.opacity-*` (opacity-50, opacity-75, opacity-100)
- [ ] `.backdrop-blur`
- [ ] Show: shadow depths, opacity examples, blur

**Size Utilities** (10+ classes)
- [ ] `.w-full`, `.h-full`
- [ ] `.max-w-sm`, `.max-w-md`, `.max-w-lg`, `.max-w-xl`, `.max-w-2xl`
- [ ] `.aspect-square`, `.aspect-video`
- [ ] Show: width examples, max-width constraints, aspect ratios

**Cursor & Interaction** (5+ classes)
- [ ] `.cursor-pointer`, `.cursor-not-allowed`, `.cursor-default`
- [ ] `.pointer-events-none`, `.pointer-events-auto`
- [ ] Show: hover states with cursor changes, disabled buttons

**Transform & Animation** (10+ classes)
- [ ] `.scale-*`, `.rotate-*`
- [ ] `.transition-fast`, `.transition-base`, `.transition-slow`
- [ ] `.fade-in`, `.fade-out`, `.slide-in-*`, `.scale-in`, `.scale-out`
- [ ] `.bounce-in`, `.bounce-out`
- [ ] Show: before/after animations, transitions

**State Utilities** (5+ classes)
- [ ] `.active`, `.disabled`, `.focus`, `.hover`
- [ ] Show: button states, form states, interactive elements

**Responsive Prefix** (examples)
- [ ] Show: `@media (min-width: 48rem)` breakpoint
- [ ] Example: `.gap-2 md:gap-4` (mobile gap-2, desktop gap-4)
- [ ] Show responsive component sizing

**Work items:** Organize into subsections with examples = 3-4 hours

### App Styleguide - Same Utilities Section
Mirror web utilities section with app-appropriate examples

---

## PRIORITY 3: Complete Component Variants — 2-3 hours

Existing components need more variants and states documented.

### Web Styleguide

- [ ] **Buttons** (expand from 3 variants to full set)
  - [ ] Sizes: xs, sm, md, lg
  - [ ] Variants: primary, secondary, tertiary, danger, link
  - [ ] States: normal, hover, active, disabled
  - [ ] Show all combinations

- [ ] **Forms** (expand from 3 to full set)
  - [ ] Input types: text, email, password, number, textarea
  - [ ] States: empty, filled, error, disabled, focus
  - [ ] Validation: error message, help text
  - [ ] Accessibility: labels, required indicators

- [ ] **Alerts** (expand from 2 to 4 variants)
  - [ ] success, error, warning, info
  - [ ] With icon, with close button, with action button

- [ ] **Badges** (expand from 3 to 5+ variants)
  - [ ] All color variants
  - [ ] Sizes (sm, md, lg)
  - [ ] With icon

- [ ] **Cards** (add variants)
  - [ ] Basic card, card with header, card with footer
  - [ ] Hover states, interactive cards
  - [ ] Different layouts

**Work items:** 5 components × ~25 min = 2-3 hours

### App Styleguide
Same coverage for app-specific variants

---

## PRIORITY 4: Layout Primitives & Patterns — 3-4 hours

These are reusable layout patterns that users copy frequently.

### New Layout Primitives Section

- [ ] **Stack** (vertical layout)
  - `.stack` (normal spacing)
  - `.stack-tight` (reduced spacing)
  - Show: vertical component stacking, spacing examples

- [ ] **Cluster** (horizontal layout, wrappable)
  - `.cluster` (normal spacing)
  - `.cluster-tight` (reduced spacing)
  - Show: horizontal button groups, icon + text combinations

- [ ] **Grid Auto** (responsive grid)
  - `.grid-auto` (auto-fit columns)
  - Show: card grids, responsive column counts

- [ ] **Center** (flex centering)
  - `.flex .items-center .justify-center`
  - Show: icon + text, centered elements

### New Patterns Section

- [ ] **Dashboard Pattern** (expand from 1 example)
  - Multi-card layout
  - With sidebar
  - With top bar
  - With footer
  - Responsive behavior

- [ ] **Form Page Pattern**
  - Form with validation
  - Success/error states
  - Multi-section form
  - Responsive form layout

- [ ] **Card Grid Pattern**
  - 2-column, 3-column, 4-column examples
  - Responsive behavior
  - With hover effects

- [ ] **Multi-step Form Pattern**
  - Stepper component
  - Step navigation
  - Form content per step
  - Progress indication

- [ ] **Pricing Table Pattern**
  - Price cards in grid
  - Featured option
  - Responsive stacking

- [ ] **Blog Card Layout**
  - Image + title + excerpt + metadata
  - Card grid
  - Different image aspect ratios

- [ ] **Feature Section Pattern**
  - Feature + image alternating
  - Feature grid (3 columns)
  - With icons and descriptions

- [ ] **Hero Section Pattern**
  - Full-width hero
  - With background image
  - With CTA button
  - Responsive text sizing

- [ ] **Footer Pattern**
  - Footer grid
  - Footer links
  - Footer columns
  - Copyright section

- [ ] **Navigation Patterns**
  - Main navigation
  - Mobile drawer navigation
  - Breadcrumbs
  - Tab navigation

**Work items:** 10 patterns × ~20 min = 3-4 hours

---

## PRIORITY 5: Form Completeness — 1-2 hours

Forms are complex and need thorough documentation.

### Web Styleguide - Forms Section Expansion

- [ ] **Input States**
  - [ ] Normal
  - [ ] Focused
  - [ ] Error (with message)
  - [ ] Disabled
  - [ ] Read-only
  - [ ] With placeholder

- [ ] **Textarea**
  - [ ] Basic
  - [ ] With error
  - [ ] With helper text
  - [ ] Disabled

- [ ] **Select Dropdown**
  - [ ] Basic
  - [ ] With optgroup
  - [ ] Disabled
  - [ ] Multiple select

- [ ] **Checkboxes**
  - [ ] Unchecked, checked, indeterminate
  - [ ] Disabled states
  - [ ] With label

- [ ] **Radio Buttons**
  - [ ] Unchecked, checked
  - [ ] Disabled states
  - [ ] With label

- [ ] **Field Groups**
  - [ ] Multiple inputs
  - [ ] With labels and help text
  - [ ] With validation messages

- [ ] **Form Layout Examples**
  - [ ] Vertical form (default)
  - [ ] Horizontal form
  - [ ] Inline form
  - [ ] Form with sections

**Work items:** Comprehensive form examples = 1-2 hours

---

## PRIORITY 6: Responsive Behavior Documentation — 1-2 hours

Show how components respond to different screen sizes.

- [ ] **Mobile-first examples** (all components)
  - Show mobile layout (320px)
  - Annotate breakpoint changes
  - Show desktop layout (1024px)

- [ ] **Responsive typography**
  - Show text scaling with `clamp()`
  - Show before/after sizes

- [ ] **Responsive spacing**
  - Show gap/padding changes at breakpoint
  - Show margin adjustments

- [ ] **Responsive images**
  - Picture element examples
  - srcset examples
  - Aspect ratio preservation

**Work items:** Add responsive annotations to existing examples = 1-2 hours

---

## PRIORITY 7: Dark Mode Variants — 1-2 hours

Show all components in both light and dark modes.

- [ ] **Toggle dark mode in styleguides** (already implemented)
- [ ] **Show each component in both modes**
  - Side-by-side examples or toggle
  - Annotate color changes

- [ ] **Dark mode guidance**
  - Which tokens change in dark mode
  - Contrast maintenance
  - When to use dark mode

**Work items:** Annotate dark mode examples = 1-2 hours

---

## PRIORITY 8: Accessibility Notes — 1-2 hours

Add accessibility guidance per component.

- [ ] **WCAG compliance notes**
  - Color contrast requirements
  - Focus indicators
  - Keyboard navigation

- [ ] **Semantic HTML examples**
  - Proper heading hierarchy
  - Button vs link semantics
  - Form label associations

- [ ] **Interactive component behavior**
  - Keyboard support
  - Screen reader announcements
  - Cursor indicators (pointer vs not-allowed)

**Work items:** Add WCAG guidance notes = 1-2 hours

---

## Implementation Sequence

### Phase 1: Foundation (Week 1) - 5-6 hours
1. **Hidden power components** (2-3 hours) - highest value
2. **Utility classes reference** (3-4 hours) - enables composition
3. Commit: "docs: Add power components and utilities reference"

### Phase 2: Completeness (Week 2) - 5-7 hours
4. **Component variants** (2-3 hours) - fill existing gaps
5. **Layout primitives & patterns** (3-4 hours) - show composition
6. Commit: "docs: Complete component variants and patterns"

### Phase 3: Polish (Week 3) - 4-6 hours
7. **Form completeness** (1-2 hours)
8. **Responsive documentation** (1-2 hours)
9. **Dark mode coverage** (1-2 hours)
10. **Accessibility notes** (1-2 hours)
11. Commit: "docs: Add responsive, dark mode, accessibility docs"

### Phase 4: Validation (Final)
- Run coverage audit
- Verify 100% (both web and app)
- Update audit report with final numbers
- Commit: "docs: Mark styleguides complete (100% coverage)"

---

## Success Criteria

When roadmap is complete:
- [ ] Web styleguide: 316/316 classes documented (100%)
- [ ] App styleguide: 268/268 classes documented (100%)
- [ ] All examples use framework classes only
- [ ] All mobile sizes render correctly
- [ ] Dark mode variants shown
- [ ] Responsive behavior documented
- [ ] Accessibility notes present
- [ ] Styleguides match rendered output perfectly
- [ ] Users can find any component they need

---

## Running the Coverage Audit

To verify progress:

```bash
# Count sections in styleguide
grep -c "<h2>" docs/visual/styleguide-web.html   # Count major sections
grep -c "<h3>" docs/visual/styleguide-web.html   # Count components

# Manually verify each section:
# 1. Open styleguide in browser
# 2. Compare each CSS class to documented examples
# 3. Mark missing items
# 4. Estimate hours to complete
```

---

## Notes for Developers

- **Framework classes only**: No inline styles in examples
- **HTML-only changes**: Styleguide is pure HTML, not HTML + inline CSS
- **Mobile-first**: Always show mobile first, then desktop
- **Mirroring**: Both web and app styleguides updated together
- **Testing**: Open in browser and verify rendering before committing

---

## Related Documents

- `STYLEGUIDE-WORKFLOW.md` - How to add components
- `STYLEGUIDE-VALIDATION-CHECKLIST.md` - How to validate completeness
- `STYLEGUIDE-MAINTENANCE.md` - Policy and principles
- `STYLEGUIDE-AUDIT-2026-05-31.md` - Detailed gap analysis
