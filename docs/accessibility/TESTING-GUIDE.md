# Accessibility Testing Guide — Nordover Design System

Nordover implements automated accessibility testing for WCAG 2.1 Level AA compliance. This guide covers running tests locally and understanding CI/CD integration.

## Quick Start

### Interactive Audit Tool (Browser)

1. Open `docs/visual/styleguide.html` in any modern browser
2. Click **"Audit Web Styleguide"** or **"Audit App Styleguide"**
3. Wait for the scan to complete
4. Review violations by severity level
5. Click any violation to see remediation guidance

**Export options:**
- Download report as Markdown (`.md`)
- Export raw results as JSON (`.json`)

### Local CLI Testing

Install PA11y and dependencies:

```bash
npm install -g pa11y pa11y-ci axe-core html-validate
```

Run accessibility audit:

```bash
# Audit using config file
pa11y-ci --config .pa11yci.json

# Or audit individual styleguides
pa11y docs/visual/styleguide.html --standard WCAG2AA
pa11y docs/visual/styleguide.html --standard WCAG2AA
```

## Standards & Compliance

### WCAG 2.1 Level AA

All components must meet **WCAG 2.1 Level AA** accessibility standards:

- **Perceivable:** Content visible and distinguishable (≥4.5:1 color contrast for text)
- **Operable:** Full keyboard navigation, no traps, ≥44x44px touch targets
- **Understandable:** Clear language, predictable behavior, error messages
- **Robust:** Valid HTML, proper ARIA, compatible with assistive tech

See [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/) for details.

## Testing Tools

### axe-core

Primary automated accessibility scanner built into the interactive audit tool.

- **Pros:** Fast, accurate, detailed violation reports with code snippets
- **Cons:** Cannot test dynamic interactions
- **Rules:** 150+ accessibility rules covering WCAG AA and Section 508

### PA11y

Command-line accessibility testing with multiple runners.

- **Runners:** axe, HTML_CodeSniffer, and others
- **Output:** JSON, CSV, markdown formats
- **CI Integration:** Built-in support for GitHub Actions

### HTML Validator

Ensures valid HTML structure (prerequisite for accessibility).

```bash
html-validate docs/visual/styleguide.html
```

## Common Violations & Fixes

### 1. Color Contrast (Critical)

**Issue:** Text fails 4.5:1 contrast ratio (WCAG AA minimum)

**Check in styleguide:**
```html
<p style="color: #999; background: white;">Low contrast text</p>
```

**Fix:**
```html
<!-- Use darker color or higher contrast background -->
<p style="color: #666; background: white;">Better contrast text</p>
```

**Test:**
- Use browser inspector's color picker to check contrast
- [Contrast Checker Tool](https://webaim.org/resources/contrastchecker/)

### 2. Missing Form Labels (Critical)

**Issue:** Form inputs without associated labels

**Bad:**
```html
<input type="email" placeholder="Email">
```

**Good:**
```html
<label for="email">Email address</label>
<input type="email" id="email" name="email">
```

### 3. Missing Alt Text (Critical)

**Issue:** Images without descriptive alt text

**Bad:**
```html
<img src="icon.svg">
```

**Good:**
```html
<img src="icon.svg" alt="Success checkmark">
```

### 4. Missing Focus Indicators (Serious)

**Issue:** Interactive elements lack visible focus states

**Fix in CSS:**
```css
button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

### 5. Insufficient Heading Hierarchy (Moderate)

**Issue:** Headings skip levels (h1 → h3)

**Bad:**
```html
<h1>Main Title</h1>
<h3>Subsection</h3> <!-- Should be h2 -->
```

**Good:**
```html
<h1>Main Title</h1>
<h2>Subsection</h2>
```

### 6. Empty Links (Serious)

**Issue:** Links with no descriptive text

**Bad:**
```html
<a href="/details">Click here</a>
```

**Good:**
```html
<a href="/product/details">View product details</a>
```

## Component Testing Checklist

When adding a new component to the framework:

### Visual & Contrast
- [ ] Text has ≥4.5:1 contrast ratio with background
- [ ] Active/focus states are visually distinct
- [ ] Color is not the only means of information
- [ ] Component works in dark mode (if applicable)

### Keyboard Accessibility
- [ ] All interactive elements are reachable via Tab
- [ ] Tab order is logical and visible (focus indicators)
- [ ] No keyboard traps (Tab gets stuck)
- [ ] Enter/Space activate buttons appropriately
- [ ] Escape closes modals/dropdowns

### Semantic HTML
- [ ] Uses semantic elements (`<button>`, `<input>`, `<nav>`, etc.)
- [ ] Form inputs have associated `<label>` elements
- [ ] Images have alt text (or `alt=""` if decorative)
- [ ] Headings use proper hierarchy (h1 → h2 → h3...)
- [ ] Lists use `<ul>`, `<ol>`, `<li>` elements

### ARIA & Dynamic Content
- [ ] Dynamic content updates announced to screen readers (`aria-live`)
- [ ] Hidden content marked with `aria-hidden="true"`
- [ ] Icon buttons have aria-label if no visible text
- [ ] Role attributes used only when necessary
- [ ] States properly communicated (`aria-expanded`, `aria-selected`, etc.)

### Documentation
- [ ] Component includes accessibility notes
- [ ] Code examples show proper HTML structure
- [ ] Styleguide documents keyboard interactions
- [ ] Any known limitations are noted

## CI/CD Integration

### GitHub Actions Workflow

The `.github/workflows/a11y-audit.yml` workflow:

1. **Triggers:** Every push to `main`/`claude/**` and pull requests
2. **Runs:** PA11y audit against both styleguides
3. **Reports:** Posts summary in PR comments
4. **Fails Build:** If critical violations are found
5. **Artifacts:** Uploads detailed audit report

### PR Comment

When you submit a PR, the workflow posts results:

```
## ✅ Accessibility Audit Results

| Severity | Count |
|----------|-------|
| 🔴 Critical Issues | 0 |
| 🟠 Warnings | 2 |
| 🟡 Notices | 5 |

Standard: WCAG 2.1 Level AA
```

### Interpreting Results

- **Critical Issues:** Build fails, must fix before merge
- **Warnings:** Should address, not blocking
- **Notices:** Informational, often require manual review

## Manual Testing with Screen Readers

Automated testing catches most issues, but some require manual verification:

### Setup

**macOS:**
- VoiceOver (built-in): Cmd + F5
- [NVDA (free)](https://www.nvaccess.org/)

**Windows:**
- [NVDA (free)](https://www.nvaccess.org/)
- JAWS (commercial)

**Linux:**
- [Orca (built-in on GNOME)](https://help.gnome.org/users/orca/stable/)

### Testing Steps

1. Enable screen reader
2. Navigate styleguide using only keyboard (Tab, Arrow keys)
3. Listen for:
   - Component names announced
   - States described ("button, expanded")
   - Form labels read with inputs
   - Error messages clearly stated
4. Document any unclear announcements

## Creating Accessible Components

### Base CSS Patterns

**Focus indicator template:**
```css
.interactive:focus-visible {
  outline: 2px solid var(--color-focus, #3b82f6);
  outline-offset: 2px;
}
```

**Visually hidden text (screen reader only):**
```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

**High contrast mode support:**
```css
@media (prefers-contrast: more) {
  .component {
    border-width: 2px;
    color: inherit;
  }
}
```

### HTML Structure Template

```html
<!-- Button component example -->
<button class="btn btn-primary" aria-label="Submit form">
  Submit
</button>

<!-- Form example -->
<div class="form-group">
  <label for="name">Full name</label>
  <input 
    type="text" 
    id="name" 
    name="name"
    required
    aria-required="true"
  >
</div>

<!-- Dropdown menu -->
<div class="dropdown">
  <button aria-expanded="false" aria-haspopup="menu">
    Menu
  </button>
  <ul role="menu" hidden>
    <li role="menuitem"><a href="#">Option 1</a></li>
    <li role="menuitem"><a href="#">Option 2</a></li>
  </ul>
</div>
```

## Accessibility Resources

### Documentation
- [WCAG 2.1 Specification](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Accessibility Guide](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM Articles](https://webaim.org/)
- [Deque University](https://dequeuniversity.com/)

### Tools
- [axe DevTools Extension](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Lighthouse (Chrome DevTools)](https://developers.google.com/web/tools/lighthouse)
- [Contrast Checker](https://webaim.org/resources/contrastchecker/)

### Community
- [#a11y on Twitter](https://twitter.com/search?q=%23a11y)
- [WebAIM Discussion Forum](https://webaim.org/discussion/)
- [A11y Project](https://www.a11yproject.com/)

## Troubleshooting

### Tool Reports Different Results

Different tools use different rulesets and may flag different issues. If axe and PA11y disagree:

1. Consult the WCAG guideline directly
2. Check both tool documentations
3. Default to the stricter interpretation

### False Positives

Some tools flag issues that aren't actually violations:

- Incomplete review items in axe often require manual assessment


### Styleguide HTML Issues

The styleguides themselves have audit infrastructure HTML that shouldn't be in production CSS:

- Focus only on violations in actual component examples
- Structural elements like navigation are scaffolding, not framework contracts

## Reporting Accessibility Issues

Found an accessibility issue?

1. **Document:** Component name, violation type, affected elements
2. **Test:** Confirm with accessibility audit tool
3. **Create Issue:** Use GitHub with label `accessibility`
4. **Include:** 
   - Component name
   - Expected behavior
   - Current behavior
   - How it affects users
5. **Assign:** Nordover team for triage

## Best Practices

✅ **Do:**
- Test with real keyboard and assistive tech
- Maintain color contrast in dark mode too
- Use semantic HTML as foundation
- Document accessibility in comments
- Test with multiple tools
- Consider mobile screen readers

❌ **Don't:**
- Use color alone to convey meaning
- Create custom controls without ARIA
- Hide required information from screen readers
- Nest interactive elements (no button in button)
- Use placeholder as label replacement
- Forget about keyboard navigation

---

**Last Updated:** 2026-06-01  
**Maintained By:** Nordover Team  
**Questions?** Check `/docs/accessibility/` or open an issue
