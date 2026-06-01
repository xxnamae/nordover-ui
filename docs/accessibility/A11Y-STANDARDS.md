# Accessibility Standards — Nordover Framework

Nordover is built and tested to meet **WCAG 2.1 Level AA** accessibility standards. This document defines the framework's accessibility commitments.

## WCAG 2.1 Level AA Commitments

### Perceivable

**1.4.3 Contrast (Minimum)**
- [ ] Text and backgrounds meet 4.5:1 contrast ratio (normal text)
- [ ] Graphics and UI components meet 3:1 contrast ratio
- [ ] Large text (18pt+) can use 3:1 ratio
- **Exceptions:** Logos, incidental, purely decorative content

**1.4.11 Non-text Contrast (AA)**
- [ ] UI components and graphical elements ≥3:1 contrast
- [ ] Focus indicators clearly visible
- [ ] State changes visually distinct

**1.1 Text Alternatives**
- [ ] All images have descriptive alt text or are marked decorative
- [ ] No text embedded as images
- [ ] Icons use aria-label or visible label

### Operable

**2.1 Keyboard Accessible**
- [ ] All functionality available via keyboard
- [ ] No keyboard traps (can always Tab away)
- [ ] Tab order is logical and visible
- [ ] Shortcut keys don't conflict with browser defaults

**2.4.7 Focus Visible**
- [ ] Focus indicator visible on all interactive elements
- [ ] Focus indicator ≥2px or sufficient contrast
- [ ] Works with light and dark backgrounds

**2.5.5 Target Size (Enhanced) — Best Practice**
- [ ] Touch targets ≥44x44 CSS pixels
- [ ] Spacing prevents accidental activation
- [ ] Exception: Inline links or components in prose

### Understandable

**3.3 Input Assistance**
- [ ] Form inputs have associated labels
- [ ] Error messages clearly identify the problem
- [ ] Suggestions provided for invalid input
- [ ] Confirmation available for major actions

**3.2 Predictable**
- [ ] Navigation consistent across pages
- [ ] Component behavior consistent and documented
- [ ] Focus changes don't unexpectedly trigger actions

### Robust

**4.1 Compatible**
- [ ] Valid HTML structure (no duplicate IDs)
- [ ] Proper semantic elements used
- [ ] ARIA used to supplement, not replace, HTML
- [ ] State changes announced to assistive tech

**4.1.3 Status Messages**
- [ ] Dynamic content updates announced via aria-live
- [ ] Validation messages associated with inputs
- [ ] Loading/processing states communicated

## Component Accessibility Baseline

Every Nordover component must:

### HTML
```html
<!-- Semantic element: <button>, <input>, etc. -->
<button class="btn btn-primary">
  Action Label
</button>

<!-- Form field with label -->
<div class="form-group">
  <label for="field-id">Field Label</label>
  <input type="text" id="field-id" name="field">
</div>
```

### Keyboard
- [ ] Keyboard accessible (Tab, Enter, Escape, Arrow keys)
- [ ] Focus indicator visible (`:focus-visible`)
- [ ] Tab order logical

### Visual
- [ ] ≥4.5:1 text contrast
- [ ] ≥3:1 UI component contrast
- [ ] Active/disabled/focus states visually distinct
- [ ] Works in high-contrast mode

### Semantic
- [ ] Proper heading hierarchy (h1 → h2 → h3)
- [ ] Lists use `<ul>` / `<ol>` / `<li>`
- [ ] Buttons are `<button>` or have `role="button"`
- [ ] No nested interactive elements

### ARIA (when needed)
- [ ] `aria-label` for icon-only buttons
- [ ] `aria-expanded` for toggles/dropdowns
- [ ] `aria-live` for dynamic updates
- [ ] `aria-required`, `aria-invalid` for forms
- [ ] Roles only when semantic HTML unavailable

## Testing Requirements

### Automated (axe-core / PA11y)
- [ ] All violations fixed before merge
- [ ] Warnings reviewed and addressed
- [ ] Both styleguides pass WCAG AA scan

### Manual
- [ ] Tested with keyboard only (Tab, Enter, Escape)
- [ ] Tested with screen reader (VoiceOver/NVDA)
- [ ] Verified in high-contrast mode
- [ ] Tested with zoom at 200%
- [ ] Works with browser text resizing

### Documentation
- [ ] Accessibility requirements documented
- [ ] Code examples show proper HTML
- [ ] Known limitations listed
- [ ] Keyboard interactions described

## Color Contrast Standards

### Text Contrast

| Text Size | Standard | AA Requirement |
|-----------|----------|----------------|
| <18pt normal | 4.5:1 | Required |
| 18pt+ (24px normal) | 3:1 | Required |
| Decorative/logo | No requirement | — |

### Component Contrast

| Element | Standard | AA Requirement |
|---------|----------|----------------|
| UI components | 3:1 | Required |
| Graphics/icons | 3:1 | Required |
| Focus indicators | Sufficient | Required |
| Decorative only | No requirement | — |

### Tools for Testing

- [WCAG Contrast Checker](https://webaim.org/resources/contrastchecker/) — Web-based
- [axe DevTools](https://www.deque.com/axe/devtools/) — Chrome extension
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/accessibility/reference) — Inspector panel

## Focus Management

### Visual Focus Indicator

Required on all interactive elements:

```css
button:focus-visible {
  outline: 2px solid var(--color-focus, currentColor);
  outline-offset: 2px;
}

/* Alternative: background/border change */
button:focus-visible {
  box-shadow: inset 0 0 0 2px var(--color-focus);
}
```

### Focus Order

- [ ] Tab order follows visual/reading order
- [ ] Skip to main content available on pages
- [ ] Modal/dialog manages focus inside container
- [ ] Focus returns to trigger element when closed

### Focus Visibility

- [ ] Works on light AND dark backgrounds
- [ ] Minimum 2:1 contrast with background
- [ ] Not removed with `outline: none` (CSS)
- [ ] Works at 200% zoom

## Screen Reader Testing

### Announcement Priority

Screen readers should announce, in order:
1. **Role** — "button", "link", "textbox"
2. **State** — "expanded", "disabled", "required"
3. **Label** — visible text or aria-label
4. **Value** — current input value
5. **Description** — aria-describedby

### ARIA Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `aria-label` | Label for elements without visible text | `<button aria-label="Close">✕</button>` |
| `aria-labelledby` | Reference another element as label | `<button aria-labelledby="modal-title">` |
| `aria-describedby` | Additional description | Form field with error message |
| `aria-expanded` | Expanded/collapsed state | Toggle buttons, accordions |
| `aria-hidden` | Hide from screen readers | Decorative icons, styling elements |
| `aria-live` | Announce dynamic updates | Loading states, validation messages |
| `aria-current` | Mark current page/item | Navigation menu |
| `aria-disabled` | Semantic disabled state | When not using native `disabled` |

## Keyboard Interaction Patterns

### Buttons
- [ ] Activated with Enter or Space
- [ ] Focus visible
- [ ] No nested buttons

### Links
- [ ] Activated with Enter
- [ ] Underlined or icon indication (not color alone)
- [ ] Focus visible

### Form Inputs
- [ ] Associated with `<label>`
- [ ] Focused when label clicked
- [ ] Error messages linked via `aria-describedby`
- [ ] Required/invalid states communicated

### Menus & Dropdowns
- [ ] Open with Enter/Space or ArrowDown
- [ ] Navigate with Arrow keys
- [ ] Close with Escape
- [ ] Close when item selected
- [ ] Return focus to trigger

### Modals & Dialogs
- [ ] Focus moves into modal on open
- [ ] Keyboard trapped inside modal (Tab loops)
- [ ] Escape closes modal
- [ ] Focus returns to trigger on close
- [ ] Title linked with `aria-labelledby`

### Tabs
- [ ] Arrow keys navigate between tabs
- [ ] Enter/Space activates tab
- [ ] Focus visible on active tab
- [ ] Content updates when tab activated

## Mobile & Touch Accessibility

### Touch Targets
- [ ] Minimum 44x44 CSS pixels (WCAG Enhanced, AAA)
- [ ] Adequate spacing between targets
- [ ] No hover-dependent functionality
- [ ] Accessible alternative for complex gestures

### Responsive
- [ ] Works at 320px width (mobile)
- [ ] Works at 200% zoom
- [ ] Doesn't rely on specific viewport size
- [ ] Touch-friendly navigation

### Dark Mode
- [ ] Contrast maintained in dark mode
- [ ] Colors not only distinguishing factor
- [ ] Works with `prefers-color-scheme` media query

## Documentation Standards

Every component in styleguide must document:

### Accessibility Section Template

```markdown
## Accessibility

### Keyboard Support
- **Tab** — Focus next element
- **Shift + Tab** — Focus previous element
- **Enter** — Activate button / Open dropdown
- **Escape** — Close dropdown / Modal

### Screen Reader
- Announced as: "button, [label]"
- States: disabled, pressed, expanded
- No extra announcements needed

### Color Contrast
- Text: 4.5:1 (AA) / 7:1 (AAA)
- Focus: 3:1 against background

### Known Limitations
- Requires JavaScript for X functionality
- Touch target 42px (just below AA minimum)

### References
- [WCAG 2.1 Success Criterion X.X.X](https://www.w3.org/WAI/WCAG21/quickref/)
```

## Compliance Verification

### Before Merge
- [ ] Automated audit passes (axe-core)
- [ ] No critical violations
- [ ] Warnings reviewed and documented if deferred
- [ ] Component tested with keyboard
- [ ] Focus indicators visible

### Quarterly Review
- [ ] Full styleguide re-audited
- [ ] New browser versions tested
- [ ] New framework components scanned
- [ ] Accessibility issues reviewed

### Annual Assessment
- [ ] Third-party accessibility audit
- [ ] WCAG AAA compliance check
- [ ] Screen reader testing expanded
- [ ] Customer accessibility feedback reviewed

## Exceptions & Deferrals

Accessibility issues may be deferred only with:

1. **Documented reason** — Why not fixing now
2. **Severity assessment** — Impact on users
3. **Remediation plan** — How and when to fix
4. **Approval** — Team consensus required

Example deferral record:

```markdown
## Deferred Issue: Link color in dark mode

**Issue:** Links in dark mode have 2.8:1 contrast (needs 4.5:1)

**Impact:** Users with low vision may struggle to identify links

**Timeline:** Fix in v2.0 (next major)

**Workaround:** Underline links to add visual distinction

**Issue #:** 123
```

## Training & Continuous Learning

### Team Responsibilities
- Learn WCAG 2.1 Level AA requirements
- Review this standards document quarterly
- Test components with assistive technology
- Contribute accessibility improvements

### Resources
- [WCAG 2.1 Spec](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Guides](https://webaim.org/)
- [Deque University](https://dequeuniversity.com/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)

---

**Standard Version:** 1.0  
**Last Updated:** 2026-06-01  
**Compliance Level:** WCAG 2.1 Level AA  
**Next Review:** 2027-06-01
