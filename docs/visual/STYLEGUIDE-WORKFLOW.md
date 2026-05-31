# STYLEGUIDE WORKFLOW

**Status:** Effective 2026-05-31  
**Policy:** Styleguides must always reflect 100% of framework CSS

---

## Principle

The styleguides are not supplementary documentation—they are **the authoritative reference** for framework users. If a component exists in CSS but not in styleguide, it does not exist for implementers.

**Central Rule:** Every change to `components-*.css` or `tokens-*.css` must have a corresponding update in the styleguides on the same commit.

---

## Workflow: Adding a New Component

### Step 1: Define CSS in Framework
Add the component to `docs/visual/components/components-web.css` or `components-app.css`.

```css
.my-new-component {
  /* CSS */
}

.my-new-component--variant {
  /* variant CSS */
}
```

### Step 2: Add Styleguide Entry (REQUIRED, SAME COMMIT)

**DO NOT commit CSS without updating styleguides.** This is enforced by code review.

Add a section to the appropriate styleguide:

#### For `styleguide-web.html`:
```html
<section class="styleguide-section" id="my-new-component">
  <h2>My New Component</h2>
  
  <h3>Basic</h3>
  <div class="my-new-component">
    Component example
  </div>
  
  <h3>Variant</h3>
  <div class="my-new-component my-new-component--variant">
    Variant example
  </div>
</section>
```

#### For `styleguide-app.html`:
Same pattern, add to the appropriate section.

### Step 3: Organize Within Styleguide

Place in the correct section based on component category:
- **Foundation** - Colors, typography, spacing, motion
- **Components** - UI elements (buttons, forms, cards, etc.)
- **Layout** - Layout primitives (.stack, .cluster, .grid-auto)
- **Utilities** - Utility classes (display, spacing, text, etc.)
- **Patterns** - Common layout patterns (dashboard, form page, etc.)

### Step 4: Validate Completeness

Before committing, run the validation checklist:

**Completeness Checklist:**
- [ ] CSS is in framework file (components-*.css or tokens-*.css)
- [ ] All variants documented (not just base)
- [ ] All states shown if applicable (hover, active, disabled, error, etc.)
- [ ] Mobile and desktop versions shown (for responsive components)
- [ ] Dark/light mode variants shown (if applicable)
- [ ] Inline styles are ZERO (use framework classes only)
- [ ] Component is placed in correct styleguide section
- [ ] Visual hierarchy is clear in HTML structure
- [ ] Rendered output matches CSS intent

---

## Workflow: Updating an Existing Component

### Step 1: Update Framework CSS
Modify `components-*.css` or `tokens-*.css`.

### Step 2: Update Styleguide (REQUIRED, SAME COMMIT)
If the change affects visual appearance, update styleguide examples.

**Criteria for styleguide update:**
- Token value changed → Update color swatch, size example, etc.
- CSS property changed → Update visual example
- New variant added → Add to styleguide
- Variant removed → Remove from styleguide

**Criteria for NO styleguide update needed:**
- Internal CSS refactor with no visual change (e.g., moving properties, restructuring selectors)
- Performance optimization
- Bug fix that doesn't change intended appearance

---

## Coverage Standards

### Foundation (100% coverage required)
- [ ] All color tokens documented with swatches
- [ ] All typography styles documented with specimens
- [ ] All spacing scales documented
- [ ] All motion/animation tokens documented

### Components (100% coverage required)
Every component in CSS must have:
- [ ] Base version shown
- [ ] All documented variants shown
- [ ] All states (hover, active, disabled, error, focus)
- [ ] All sizes (if applicable)
- [ ] Dark mode variant (if applicable)
- [ ] Mobile/responsive variant (if applicable)

### Utilities (100% coverage required)
Utilities must be organized into reference sections:
- [ ] Display & Layout (flex, grid, block, hidden, etc.)
- [ ] Spacing (gap, padding, margin classes)
- [ ] Typography (font weight, text transform, etc.)
- [ ] Colors (text, background, border colors)
- [ ] Sizing (width, height classes)
- [ ] Borders & Corners (border, rounded utilities)
- [ ] Effects (shadow, opacity, backdrop)
- [ ] Transforms & Animation (transition, animation classes)
- [ ] States (active, disabled, focus states)
- [ ] Responsive (mobile-first breakpoint examples)

### Patterns (100% coverage required)
- [ ] Dashboard layout example
- [ ] Form page layout example
- [ ] Card grid example
- [ ] Responsive stack example
- [ ] Multi-step form example
- [ ] Feature section example
- [ ] Pricing section example
- [ ] Blog card layout example
- [ ] Hero section example
- [ ] Footer layout example

---

## Validation: Coverage Audit

Run this audit before declaring styleguide complete:

```bash
# Count documented components vs CSS components
# Web: should have 316/316 (100%)
# App: should have 268/268 (100%)
```

**What counts as documented?**
- Has an `<h3>` heading (component name)
- Has at least one working HTML example
- Example uses only framework classes (no inline styles)
- Is placed in correct section

**What does NOT count?**
- Mentions in text without visual example
- Broken example (missing class, incorrect HTML)
- Inline CSS styling (must use framework classes)
- Example that doesn't match framework CSS

---

## Mirroring Rule

**Both web and app styleguides must stay synchronized.**

If a component is added to both `components-web.css` and `components-app.css`:
- Add to both styleguides in the same commit
- Account for design differences (web: light-first, generous spacing vs app: dark-first, compact)
- Show platform-appropriate examples

---

## Pre-Merge Checklist

Before PR merge, verify:
- [ ] New CSS added to framework file
- [ ] Styleguide updated with examples
- [ ] All variants documented
- [ ] No inline styles in styleguide HTML
- [ ] Rendered styleguide looks correct
- [ ] Coverage audit shows 100% (or maintains existing %)
- [ ] Mirroring rule followed (web/app in sync)

---

## Automation Possibilities

Future optimizations (not yet implemented):
1. **Automated coverage audit** - Script that counts CSS classes vs documented sections
2. **Template generator** - Script to scaffold styleguide HTML from CSS comments
3. **Validation bot** - CI check that fails if CSS changed but styleguide wasn't
4. **Visual regression testing** - Automated screenshots to catch rendering issues

---

## FAQ

**Q: Can I commit CSS without updating styleguide?**  
A: No. This breaks the "single source of truth" principle. Updates must be in same commit.

**Q: What if the CSS change is internal/invisible?**  
A: Check the "Criteria for NO styleguide update needed" section. If it's truly invisible, no update required, but document this reasoning in commit message.

**Q: What if styleguide is already complete?**  
A: It isn't (as of 2026-05-31, app is 46%, web is 4%). All PRs must improve coverage or maintain it.

**Q: How do I know where to place a new component?**  
A: Check "Organize Within Styleguide" section. If it doesn't fit an existing category, propose new section in code review.

**Q: Should styleguide show all breakpoints?**  
A: Show mobile (default) and desktop (48rem+) for responsive components. Use `@media (min-width: 48rem)` examples in HTML comments if needed.

---

## Related Documents

- `docs/visual/STYLEGUIDE-MAINTENANCE.md` - Policy and principles
- `docs/visual/STYLEGUIDE-AUDIT-2026-05-31.md` - Current coverage analysis
- `CLAUDE.md` - Foundational rules (Styleguides are authoritative)
