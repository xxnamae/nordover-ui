# ADR: Nordover Testing Strategy (Fase 2.5)

**Status:** Approved  
**Date:** 2026-05-30  
**Author:** Claude Code Agent

## Overview

Comprehensive testing strategy for Nordover design system covering visual regression, accessibility, performance, and real-world integration.

## Testing Categories

### 1. Visual Regression Testing

**Goal:** Ensure component appearance remains consistent across browser updates and CSS changes.

**Approach:**
- Baseline screenshots of all components
- Automated comparison on CSS changes
- Browser coverage: Chrome, Firefox, Safari, Edge

**Implementation:**
```bash
# Using Percy.io or similar
npm install --save-dev @percy/cli @percy/puppeteer

# Run snapshots
percy snapshot docs/visual/styleguide-web.html
percy snapshot docs/visual/styleguide-app.html
```

**Coverage:**
- ✅ All button variants and sizes
- ✅ All form control types
- ✅ Data display components
- ✅ Complex components (date picker, file upload, table)
- ✅ Dark mode variants
- ✅ Mobile viewport (375px, 768px, 1024px)
- ✅ Hover/focus states (via CSS pseudo-selectors)

**Success Criteria:**
- 0 unintended visual changes
- All breakpoints render correctly
- Dark mode colors have sufficient contrast
- No layout shifts (CLS = 0)

### 2. Accessibility Audit

**Goal:** Ensure WCAG AA compliance across all components.

**Automated Testing:**
```bash
npm install --save-dev @axe-core/playwright

# Run audit
npx playwright test --project=a11y
```

**Test Cases:**
- ✅ Color contrast: All text >= 4.5:1 (AA), graphics >= 3:1
- ✅ Focus management: All interactive elements focusable
- ✅ Focus indicators: Clear, >= 3px, sufficient contrast
- ✅ Keyboard navigation: All components keyboard accessible
- ✅ ARIA attributes: Valid, properly associated
- ✅ Semantic HTML: Proper heading hierarchy, lists, etc.
- ✅ Motion: prefers-reduced-motion honored
- ✅ Zoom: 200% zoom doesn't break layout

**Tools:**
- axe-core: Automated violations
- WAVE: Manual review
- Screen reader testing: NVDA (Windows), VoiceOver (Mac)
- Keyboard-only navigation: Tab/Shift+Tab through all components

**Known Issues to Verify:**
- Checkboxes/radios use custom styling (ensure accessible)
- Date picker has proper ARIA labels
- File upload describes accepted formats
- Tables have proper header associations

### 3. Performance Testing

**Goal:** Ensure fast load times and smooth interactions.

**Metrics:**
- CSS file size: < 60KB uncompressed
- Paint time: First paint < 1s on 4G
- Layout shift: CLS < 0.1
- Interaction to paint: < 100ms

**Testing:**
```bash
npm install --save-dev @web/test-runner @web/test-runner-lighthouse

# Performance audit
npx web-test-runner --lighthouse
```

**Optimization Targets:**
- ✅ Minimize CSS specificity
- ✅ Avoid expensive selectors (attribute selectors in hot paths)
- ✅ No blocking animation keyframes on initial load
- ✅ CSS only (no JavaScript required)

**Size Budget:**
- tokens-web.css: < 15KB
- tokens-app.css: < 15KB
- components-web.css: < 35KB
- components-app.css: < 35KB
- Total: < 50KB

### 4. Browser Compatibility

**Goal:** Ensure consistent appearance and function across browsers.

**Supported Browsers:**
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile Chrome 90+
- Mobile Safari 14+

**Testing Approach:**
1. Browserstack or similar for cross-browser testing
2. Feature detection for CSS features:
   - `@layer`: Chrome 99+, Firefox 97+, Safari 15.4+
   - `color-mix()`: Chrome 111+, Safari 16.4+
   - `container-type`: Chrome 105+, Safari 16+

**Fallback Strategy:**
- `@supports` queries for optional features
- Graceful degradation for older browsers
- Polyfills only for critical features

**Testing Checklist:**
- ✅ Buttons render correctly (all variants)
- ✅ Forms display properly (no height issues)
- ✅ Colors display correctly (OKLCH support)
- ✅ Dark mode works (CSS variable override)
- ✅ Responsive breakpoints trigger correctly

### 5. Real-World Integration Testing

**Goal:** Validate framework works in actual project contexts.

**Integration Tests:**
1. **Plain HTML:**
   - Load CSS files via CDN
   - Build sample page with all components
   - Verify rendering without JavaScript

2. **Next.js:**
   - Create sample app
   - Verify CSS minification works
   - Test dark mode toggle
   - Check SSR rendering

3. **Vue 3:**
   - Create component wrappers
   - Test reactivity with theme toggle
   - Verify no style conflicts

4. **React:**
   - Build component abstraction layer
   - Test with styled-components/emotion coexistence
   - Verify CSS cascade works

5. **Static Site (Hugo/Jekyll):**
   - Build minimal site
   - Verify CSS loading from CDN
   - Test responsive layouts

**Test Matrix:**
```
Framework × Browser × Viewport × Theme
= 5 × 4 × 3 × 2 = 120 combinations
```

### 6. Component Behavior Testing

**Goal:** Ensure interactive components work correctly.

**Test Cases:**
```javascript
// Date picker
- Opens on input click
- Navigates months
- Selects date
- Closes on select or Escape
- Keyboard navigation (arrows, Enter)

// File upload
- Drag and drop detection
- File selection dialog
- Progress tracking
- Error handling

// Form toggle
- Toggles on click
- Toggles with Space/Enter key
- Updates aria-checked attribute

// Modal
- Opens/closes
- Traps focus
- Closes on Escape
- Prevents background scroll
```

### 7. Documentation Testing

**Goal:** Ensure all examples in documentation work.

**Validation:**
- ✅ All code examples are syntactically valid HTML
- ✅ All CSS class names exist in framework
- ✅ All token variables are defined
- ✅ No dead links in wiki
- ✅ Examples render correctly

**Tools:**
- HTML validator: W3C HTML Validator
- Link checker: linkinator
- Code snippet validation: Custom regex patterns

## Testing Automation

### CI/CD Pipeline

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  visual:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: percy/snapshot-action@v1
        with:
          static-path: docs/visual
  
  a11y:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npx axe-core docs/visual/styleguide-web.html
      - run: npx axe-core docs/visual/styleguide-app.html
  
  performance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run test:performance
      - uses: GoogleChrome/lighthouse-ci-action@v9
  
  links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npx linkinator docs/ --recursive
```

## Testing Checklist

### Pre-Release

- [ ] Visual regression tests pass (all browsers)
- [ ] Accessibility audit: 0 violations
- [ ] Performance metrics within budget
- [ ] Browser compatibility tests pass
- [ ] Component behavior tests pass
- [ ] Documentation tests pass
- [ ] Real-world integration tests pass
- [ ] Changelog updated
- [ ] Version bumped
- [ ] Release notes prepared

### Per Component Change

- [ ] Visual tests updated
- [ ] Accessibility verified (if structure changed)
- [ ] Performance impact assessed
- [ ] Documentation updated
- [ ] Examples tested

## Known Limitations

1. **Pseudo-classes**: Hover/focus states tested manually or with JavaScript
2. **Browser-specific rendering**: Some minor variations expected
3. **CSS custom properties**: Limited to modern browsers (IE11 not supported)
4. **Interaction testing**: Limited to user events, not animation details

## Future Improvements

- [ ] Visual snapshot diffing with pixel-level analysis
- [ ] Automated visual regression on PR creation
- [ ] Accessibility testing on every CSS change
- [ ] Performance testing with real-world performance data
- [ ] Component interaction tests with Playwright
- [ ] Contrast ratio verification tool
- [ ] Responsive design testing automation

## References

- WCAG 2.1 AA: https://www.w3.org/WAI/WCAG21/quickref/
- axe DevTools: https://www.deque.com/axe/devtools/
- Percy.io: https://percy.io/
- Lighthouse: https://developers.google.com/web/tools/lighthouse/
