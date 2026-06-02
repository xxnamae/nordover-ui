# Phase 6 Implementation Plan — Styleguide Authority

**Objective:** Achieve 100% CSS class coverage in styleguides; eliminate inline styles per CLAUDE.md

**Scope:**
- 322 unique CSS classes defined in components-web.css
- 305 classes currently documented in styleguides
- ~1559 inline `style=""` attributes in styleguide-web.html
- ~871 inline `style=""` attributes in styleguide-app.html
- 5 `<style>` blocks per file (embedded keyframes + utilities)

**Constraints:**
- Per CLAUDE.md: Component CSS lives in framework, not per-client
- Styleguides are authoritative: if component exists in CSS but not styleguide, it doesn't exist for users
- No hard-coding hex colors; all color in OKLCH via tokens

---

## Execution Strategy

### Phase 6A: Foundation (Utility Classes + Documentation)
**Status:** In progress  
**Time:** ~1-2 hours

1. ✅ Created 100+ utility classes in styleguide-enhancements.css
   - Color: .text-{muted,fg,accent}, .bg-{subtle,accent}
   - Padding: .p-{1..8}, .px-{2,3,4}, .py-{2,3,4}
   - Margins: .m-0, .mb-{1..6}, .mt-{1..4}
   - Layout: .flex, .flex-col, .items-center, .justify-center, .gap-{1..4}
   - Radius: .rounded-{sm,md,lg,full}
   - Text: .text-{center,left,right}, .text-{xs,sm,base,lg}
   - Font: .font-{normal,medium,semibold,bold}

2. Next: Document critical missing components

### Phase 6B: Critical Components Documentation
**Components to add:** 4-6 major families

#### B1: Empty States
**File:** styleguide-web.html  
**Missing classes:** empty-state-icon, empty-state-title, empty-state-text  
**Action:** Create section with 3-4 example patterns (no items, error state, etc.)

#### B2: Footer Layouts
**File:** styleguide-web.html  
**Missing classes:** footer-3col, footer-4col  
**Status:** Defined in CSS (line 1718-1719) but no doc examples  
**Action:** Add responsive footer grid examples with real content

#### B3: Mobile Navigation
**File:** styleguide-web.html  
**Missing classes:** mobile-nav-*, mobile-nav-trigger, mobile-nav-close  
**Status:** Defined (line 1645-1648) but poor documentation  
**Action:** Create mobile nav demo with toggle examples

#### B4: Dividers & Separators
**File:** styleguide-web.html  
**Missing classes:** divider, section-divider, section-divider-icon  
**Action:** Document divider variants (horizontal, with label, with icon)

#### B5: Responsive Stack
**File:** styleguide-web.html  
**Missing classes:** responsive-stack  
**Action:** Document responsive grid that adapts to viewport

#### B6: Date Picker (App)
**File:** styleguide-app.html  
**Missing classes:** date-picker-*, date-picker-input  
**Action:** Create date picker component documentation

### Phase 6C: Inline Style Removal (Systematic)
**Time:** ~3-4 hours  
**Approach:** Batch + manual

#### Strategy C1: High-Impact Batch Replacements
Most common patterns (total 250+ instances):

```
style="color:var(--color-muted);margin-bottom:var(--space-3)"
  → class="text-muted mb-3"

style="padding:var(--space-4);background:var(--color-subtle);border-radius:var(--radius-md)"
  → class="p-4 bg-subtle rounded-md"

style="display:flex;gap:var(--space-2);align-items:center"
  → class="flex gap-2 items-center"
```

**Method:** sed/perl one-liners for each pattern, verify output

#### Strategy C2: Manual Cleanup
After batch replacements:
1. Merge classes with existing `class=""` attributes
2. Remove redundant utilities
3. Verify DOM structure unchanged
4. Visual regression test in browser

#### Strategy C3: Embedded <style> Block Removal
5 blocks per file:
1. `.code-block/.copy-btn` → Move to styleguide-enhancements.css
2. `@keyframes slideRight/fadeIn/bounce/pulse` → Move to components CSS or leave (animation examples)

---

## Priority Order

**Tier 1 (Do Now):**
- Empty states (heavily used in examples)
- Footer grids (common pattern)
- Mobile navigation (critical for responsive demo)

**Tier 2 (Do Next):**
- Dividers
- Animation utilities
- Blog card metadata

**Tier 3 (Do After):**
- Icon utilities
- Less common helper classes
- Inline style cleanup (safe patterns only)

---

## Validation Checklist

After each section:
- [ ] All new classes render correctly in browser
- [ ] No inline styles remain in that section (except edge cases)
- [ ] Responsive behavior (mobile/tablet/desktop) verified
- [ ] Dark mode toggle works
- [ ] No WCAG contrast regressions

---

## File Modifications

### styleguide-web.html
- Add ~6 new component sections (empty states, footers, mobile nav, etc.)
- Remove inline styles from updated sections (batch 1: 150-200 instances)
- Move embedded CSS to styleguide-enhancements.css

### styleguide-app.html
- Add date picker documentation
- Remove inline styles from updated sections (batch 1: 100-150 instances)

### styleguide-enhancements.css
- Add utility class library (✅ done)
- Migrate embedded .code-block/.copy-btn styles
- Migrate animation keyframes if necessary

### components-web.css & components-app.css
- No changes (CSS is authoritative)

---

## Success Criteria

- 100% CSS class documentation (322 → 322 documented in web, 289 → 289 in app)
- < 100 remaining inline styles in styleguides (down from 1559 + 871)
- All embedded <style> blocks migrated or justified
- Visual regression tests pass
- WCAG compliance maintained

---

## Known Risks

1. **Class explosion:** Too many utility classes can become unmaintainable
   - Mitigation: Stick to token-based (no magic numbers)
   - Keep utilities minimal; prefer component classes

2. **HTML merge conflicts:** Combining multiple inline styles into class list
   - Mitigation: Single sed pass per pattern, manual verification
   - Use git diff to inspect before commit

3. **Dark mode edge cases:** Some inline colors might not auto-adjust
   - Mitigation: All colors MUST use CSS tokens (no hex)
   - Test both light/dark modes in browser

4. **Breaking styleguide rendering:** Removing styles too aggressively
   - Mitigation: Work on copies, test incrementally
   - Commit after each validated section

---

## Estimated Completion Time

- **Phase 6A (foundation):** 1-2 hours ✅ IN PROGRESS
- **Phase 6B (documentation):** 2-3 hours
- **Phase 6C (style removal):** 3-4 hours
- **Testing & fixes:** 1-2 hours

**Total:** 7-11 hours of focused work

---

## Next Steps

1. Complete Phase 6A (utility classes) ← NOW
2. Start Phase 6B.1 (empty states documentation)
3. Batch-replace first 200 instances of inline styles
4. Verify in browser, commit
5. Continue with remaining critical components
