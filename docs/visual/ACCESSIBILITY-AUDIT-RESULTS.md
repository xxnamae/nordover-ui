# Accessibility Audit Results — Nordover Styleguides

**Generated:** 2026-06-01  
**WCAG Standard:** WCAG 2.1 Level AA  
**Test Tool:** axe-core 4.8.0

## How to Generate These Results

1. Open `/docs/visual/accessibility-audit.html` in a web browser
2. Click "Audit Web Styleguide" or "Audit App Styleguide"
3. Wait for the audit to complete
4. Review violations and export results

**For CI/CD Integration:** See `.github/workflows/a11y-audit.yml`

## Summary

This document is **auto-populated** when the GitHub Actions workflow runs on each commit.

| Metric | Count |
|--------|-------|
| Critical Issues | *pending* |
| Warnings | *pending* |
| Passed Rules | *pending* |
| Needs Manual Review | *pending* |

## Initial Audit

Initial automated scans have identified the following categories of issues across the styleguide components:

### Common Issue Categories

1. **Color Contrast Violations**
   - Severity: Critical
   - Occurs when text fails WCAG AA contrast ratio standards
   - Remediation: Adjust foreground/background color combinations

2. **Missing Alt Text on Images**
   - Severity: Critical
   - Affects any images in component examples
   - Remediation: Add descriptive alt attributes

3. **Missing Form Labels**
   - Severity: Critical
   - Form inputs without associated labels
   - Remediation: Use `<label>` elements with proper `for` attributes

4. **Missing ARIA Landmarks**
   - Severity: Serious
   - Sections without semantic landmarks
   - Remediation: Use proper `<header>`, `<nav>`, `<main>`, `<footer>` elements

5. **Keyboard Navigation Issues**
   - Severity: Serious
   - Interactive elements not keyboard accessible
   - Remediation: Ensure all interactive elements are in tab order with proper focus states

6. **Missing Focus Indicators**
   - Severity: Serious
   - Interactive elements without visible focus states
   - Remediation: Add `:focus` and `:focus-visible` styles

7. **Insufficient Heading Hierarchy**
   - Severity: Moderate
   - Headings skip levels (e.g., h1 → h3)
   - Remediation: Maintain proper h1 → h2 → h3 structure

8. **Insufficient Link Context**
   - Severity: Moderate
   - Links use generic text like "click here"
   - Remediation: Use descriptive link text

## Compliance Tracking

### WCAG 2.1 Level AA Checklist

- [ ] Perceivable: Content must be presentable to users in ways they can perceive
  - [ ] Text alternatives for non-text content
  - [ ] Sufficient color contrast (4.5:1 for normal text)
  - [ ] Reflow and display flexibility
  
- [ ] Operable: Interface must be operable via keyboard
  - [ ] Full keyboard accessibility
  - [ ] No keyboard traps
  - [ ] Sufficient target size (44x44 CSS pixels minimum)
  - [ ] Clear focus indicators
  
- [ ] Understandable: Users must be able to understand content
  - [ ] Readable language and text
  - [ ] Predictable behavior
  - [ ] Input assistance and error messages
  
- [ ] Robust: Content must be compatible with assistive technologies
  - [ ] Valid HTML structure
  - [ ] Proper ARIA usage
  - [ ] Semantic HTML elements

## Component-Specific Findings

Audit results are organized by component family. Each violation includes:

- **Issue ID:** axe-core identifier
- **Severity:** Critical / Serious / Moderate / Minor
- **Impact:** How it affects users
- **Remediation:** Steps to resolve
- **Affected Elements:** Count and HTML snippets

## Running Manual Verification

Use the accessibility audit tool at `/docs/visual/accessibility-audit.html` to:

1. Load and inspect any styleguide
2. View violations with severity levels
3. Examine affected HTML elements
4. Get remediation guidance for each issue
5. Export detailed reports in Markdown or JSON format

## Continuous Integration

The GitHub Actions workflow at `.github/workflows/a11y-audit.yml`:

- Runs on every commit to `main` and `claude/**` branches
- Scans both web and app styleguides
- Reports critical violations in PR comments
- Generates downloadable audit reports
- **Fails build** if critical violations are found (configurable)

## Remediation Workflow

1. **Identify violations** via automated audit
2. **Assign severity** (critical → serious → moderate → minor)
3. **Research standards** using WCAG resources
4. **Apply fixes** to CSS/HTML
5. **Re-audit** to confirm resolution
6. **Document decision** if choosing to defer non-critical issues

## Resources

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [axe DevTools Documentation](https://www.deque.com/axe/devtools/)
- [WebAIM Resources](https://webaim.org/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)

## Next Steps

1. Implement automated testing (see `docs/accessibility/TESTING-GUIDE.md`)
2. Address critical violations first
3. Schedule quarterly audits of the entire design system
4. Monitor accessibility metrics in CI/CD pipeline
5. Train team on WCAG compliance practices

---

**Last Updated:** 2026-06-01  
**Maintainer:** Nordover Design System Team
