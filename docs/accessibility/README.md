# Accessibility Documentation — Nordover Design System

Nordover is committed to **WCAG 2.1 Level AA** accessibility compliance. This directory contains guidance for implementing, testing, and maintaining accessible components.

## Quick Links

### For Implementers
- **[Testing Guide](./TESTING-GUIDE.md)** — How to test components for accessibility
  - Interactive audit tool
  - CLI testing with PA11y
  - Common violations and fixes
  - Component testing checklist

- **[Accessibility Standards](./A11Y-STANDARDS.md)** — Nordover's accessibility requirements
  - WCAG 2.1 Level AA commitments
  - Component baseline
  - Color contrast standards
  - Keyboard interaction patterns
  - ARIA guidelines

### For Designers
- Focus indicator design (min 2px visible)
- Color contrast ratios (4.5:1 for text)
- Touch target sizes (44x44px minimum)
- Dark mode contrast verification
- Keyboard state indicators

### For Developers
- Semantic HTML requirements
- ARIA attribute usage
- Focus management patterns
- Screen reader testing
- Automated testing setup

## What's Automated

The framework includes:

### Unified Interactive Styleguide
File: `/docs/visual/styleguide.html`

- ✅ **Inspect components** — Browse all building blocks with live examples
- ✅ **Test accessibility** — Use browser DevTools axe extension or PA11y
- ✅ **Web and app variants** — Toggle between web (editorial) and app (SaaS) frameworks
- ✅ **Dark mode testing** — Toggle dark mode to verify contrast in both themes

**No installation needed** — Open in browser

### GitHub Actions CI/CD
File: `.github/workflows/a11y-audit.yml`

- ✅ **Automatic testing** — Runs on every commit
- ✅ **PR comments** — Posts summary of violations
- ✅ **Artifact reports** — Stores detailed results
- ✅ **Build failures** — Critical issues block merge

## Key Accessibility Features

| Feature | Status | Standard |
|---------|--------|----------|
| Color contrast (text) | ✅ Enforced | 4.5:1 (WCAG AA) |
| Color contrast (UI) | ✅ Enforced | 3:1 (WCAG AA) |
| Keyboard navigation | ✅ Enforced | Full coverage |
| Focus indicators | ✅ Enforced | Visible on all interactive |
| Form labels | ✅ Enforced | Semantic `<label>` |
| ARIA landmarks | ✅ Enforced | `<nav>`, `<main>`, `<footer>` |
| Heading hierarchy | ✅ Enforced | h1 → h2 → h3 |
| Alt text on images | ✅ Enforced | Descriptive or decorative |
| Screen reader support | ✅ Tested | VoiceOver, NVDA |
| Dark mode contrast | ✅ Verified | 4.5:1 maintained |
| Zoom to 200% | ✅ Tested | No overlap, readable |
| High contrast mode | ✅ Tested | Uses `prefers-contrast` |

## Testing Accessibility

### Option 1: Interactive Browser Tool (Easiest)

```
1. Open docs/visual/styleguide.html
2. Use browser DevTools (F12) → Axe DevTools extension
3. Run scan (click "Scan ALL of my page")
4. Review violations with fixes
```

No setup required. Install Axe DevTools extension from your browser's extension store.

### Option 2: Command Line (Advanced)

```bash
# Install tools (one-time)
npm install -g pa11y pa11y-ci axe-core

# Run audit
pa11y-ci --config .pa11yci.json

# Audit individual styleguide
pa11y docs/visual/styleguide.html --standard WCAG2AA
```

### Option 3: CI Pipeline (Automatic)

Push to GitHub and the workflow automatically:
- Scans both styleguides
- Reports results in PR comment
- Fails build if critical violations found
- Uploads artifact with detailed report

## Common Violations & Quick Fixes

### Low Color Contrast
**Severity:** Critical  
**Fix:** Check `docs/accessibility/TESTING-GUIDE.md` → Color Contrast section

### Missing Form Labels
**Severity:** Critical  
**Fix:** Use semantic `<label for="id">` element

### Keyboard Not Working
**Severity:** Critical  
**Fix:** Add `:focus-visible` styles, test Tab key navigation

### Missing Focus Indicator
**Severity:** Serious  
**Fix:** Add CSS: `outline: 2px solid var(--color-focus);`

### Bad Heading Hierarchy
**Severity:** Moderate  
**Fix:** Use h1 → h2 → h3, don't skip levels

See **[TESTING-GUIDE.md](./TESTING-GUIDE.md)** for detailed remediation steps.

## Standards We Follow

### WCAG 2.1 Level AA
- Internationally recognized accessibility standard
- Covers perceivability, operability, understandability, robustness
- Required for many government/public sector projects

### Web Content Accessibility Guidelines
- W3C Web Accessibility Initiative (WAI)
- Four principles: POUR (Perceivable, Operable, Understandable, Robust)
- 100+ testable success criteria

### Section 508 (US)
- US federal requirement
- Aligns closely with WCAG 2.1 Level AA

See **[A11Y-STANDARDS.md](./A11Y-STANDARDS.md)** for complete requirements.

## Testing with Assistive Technology

### Screen Readers (Manual Testing)

**Quick test:**
1. Enable VoiceOver (Mac: Cmd+F5) or NVDA (Windows: free download)
2. Tab through the styleguide
3. Listen for component names, states, labels being announced
4. Check that everything is readable and understandable

**What to listen for:**
- Role: "button", "link", "textbox"
- State: "expanded", "disabled", "required"
- Label: visible text or aria-label
- Errors: clearly stated and associated with field

### Keyboard-Only Testing

1. Unplug mouse or disable trackpad
2. Navigate styleguide using only Tab, Shift+Tab, Enter, Escape
3. Verify:
   - All interactive elements reachable via Tab
   - Tab order is logical
   - Enter activates buttons
   - Escape closes modals/dropdowns
   - Focus indicator always visible

### Color Contrast Testing

1. Use browser DevTools color picker
2. Check text vs. background
3. Verify ≥4.5:1 ratio for normal text
4. Verify ≥3:1 ratio for UI components
5. Test in dark mode too

Tools:
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) (web-based)
- [axe DevTools](https://www.deque.com/axe/devtools/) (Chrome extension)
- Browser DevTools (Chrome: Accessibility panel)

## File Structure

```
docs/
├── accessibility/               # This directory
│   ├── README.md               # Overview (you are here)
│   ├── TESTING-GUIDE.md        # How to test for a11y
│   ├── A11Y-STANDARDS.md       # Framework requirements
│   └── CI-INTEGRATION.md       # GitHub Actions setup
├── visual/
│   ├── ACCESSIBILITY-AUDIT-RESULTS.md
│   ├── styleguide.html              # Unified interactive styleguide
│   └── ...
└── wiki/
    ├── README.md
    └── decisions/              # Decision records (ADRs)
```

## Getting Help

### Finding Answers

1. **How do I test this?** → [TESTING-GUIDE.md](./TESTING-GUIDE.md)
2. **What's required?** → [A11Y-STANDARDS.md](./A11Y-STANDARDS.md)
3. **How do I fix X?** → Check TESTING-GUIDE violations section
4. **CI integration?** → See `.github/workflows/a11y-audit.yml`

### Asking Questions

- Open issue on GitHub with label `accessibility`
- Include component name, specific issue, and testing method
- Attach screenshot or video of the problem if helpful

### External Resources

- [WCAG 2.1 Quick Reference](https://www.w3.org/WAI/WCAG21/quickref/) — Official spec
- [WebAIM Guides](https://webaim.org/) — Practical tutorials
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) — Technical reference
- [Deque University](https://dequeuniversity.com/) — Training courses
- [A11y Project](https://www.a11yproject.com/) — Community resource

## Contributing Improvements

Found an accessibility issue? Want to improve our standards?

1. **File issue** with label `accessibility`
2. **Include:**
   - Component affected
   - Issue type (contrast, keyboard, semantic, etc.)
   - How to reproduce
   - Expected vs. actual behavior
   - WCAG criterion violated

3. **Propose solution** (fix, workaround, future timeline)
4. **Get feedback** from team
5. **Implement in PR** with tests

## Compliance Monitoring

### Continuous Testing
- ✅ Every commit automatically scanned
- ✅ PR comments report violations
- ✅ Critical issues block merge
- ✅ Artifacts stored for audit trail

### Quarterly Review
- Styleguide fully re-audited
- New components assessed
- Team accessibility training updated
- Customer feedback reviewed

### Annual Audit
- Third-party accessibility assessment
- WCAG AAA compliance check
- Screen reader testing expanded
- Accessibility roadmap updated

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.0 | 2026-06-01 | Initial accessibility testing framework |

---

**Status:** Active  
**Compliance Level:** WCAG 2.1 Level AA  
**Last Updated:** 2026-06-01  
**Next Review:** 2026-09-01
