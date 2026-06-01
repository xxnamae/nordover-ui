# Accessibility Guide for Nordover Implementers

**Framework-Agnostic Guide for Building Accessible Applications**

---

## Introduction

Nordover provides a foundation of accessible components, but **accessibility is a team effort**. This guide covers:

1. How Nordover supports accessibility
2. What implementers must do to maintain accessibility
3. Common patterns that preserve WCAG 2.1 Level AA compliance
4. Automated testing within your application

---

## Nordover's Accessibility Foundation

### ✅ What Nordover Provides

- **Semantic HTML structure** — Uses `<button>`, `<form>`, `<input>`, `<label>`, etc.
- **WCAG 2.1 Level AA colors** — Verified contrast ratios (text 4.5:1, UI components 3:1)
- **Focus indicators** — Visible `:focus-visible` outline (2px, 2px offset)
- **Dark mode support** — Maintains contrast in both light and dark modes
- **Keyboard navigation** — All interactive elements reachable via Tab key
- **ARIA attributes** — Proper roles on custom components (modal, switch, status, etc.)
- **Screen reader hints** — `aria-label`, `aria-describedby`, `aria-hidden` where needed
- **Reduced motion support** — Respects `prefers-reduced-motion` media query

### ⚠️ What Implementers Must Do

1. **Use semantic HTML** — Don't replace `<button>` with `<div class="btn">`
2. **Associate labels with inputs** — Use `<label for="input-id">` or wrap input in label
3. **Maintain color contrast** — When customizing colors, ensure 4.5:1 for text
4. **Provide alt text** — All images need meaningful `alt` attributes
5. **Use proper heading hierarchy** — h1 > h2 > h3 (no skipping levels)
6. **Test with screen readers** — NVDA (Windows), JAWS (Windows), VoiceOver (Mac)
7. **Test keyboard navigation** — Tab, Shift+Tab, Enter, Space, Escape, arrow keys

---

## Semantic HTML Patterns

### Buttons

✅ **Do this:**
```html
<button class="btn btn-primary">Click Me</button>
<button class="btn btn-secondary" disabled>Disabled</button>
```

❌ **Don't do this:**
```html
<div class="btn btn-primary" role="button">Click Me</div>
<span onclick="handleClick()" class="btn">Not a real button</span>
```

**Why:** Real `<button>` elements are automatically keyboard-accessible and announcement to screen readers.

### Forms & Inputs

✅ **Do this:**
```html
<form class="stack gap-4">
  <label for="email">Email</label>
  <input id="email" type="email" class="form-input" required>
  
  <label for="subscribe">
    <input id="subscribe" type="checkbox" class="form-checkbox">
    Subscribe to updates
  </label>
  
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

❌ **Don't do this:**
```html
<form>
  <input type="email" placeholder="Email">
  <input type="checkbox"> Subscribe
  <button>Submit</button>
</form>
```

**Why:** Labels must be associated with inputs. Placeholders are not labels (they disappear when typing).

### Links vs Buttons

✅ **Links for navigation:**
```html
<a href="/about" class="btn btn-primary">Learn More</a>
```

✅ **Buttons for actions:**
```html
<button class="btn btn-primary" onclick="handleDelete()">Delete Item</button>
```

❌ **Don't use links for actions:**
```html
<a href="javascript:handleDelete()" class="btn">Delete</a>
```

**Why:** Links have semantic meaning. When users see a link, they expect navigation.

### Icons with Text

✅ **Do this:**
```html
<button class="btn">
  <svg class="icon" aria-hidden="true"><use href="#icon-home"/></svg>
  <span>Home</span>
</button>
```

✅ **Or this (icon alone):**
```html
<button class="btn" aria-label="Home">
  <svg class="icon"><use href="#icon-home"/></svg>
</button>
```

❌ **Don't do this:**
```html
<button class="btn">
  <svg class="icon"><use href="#icon-home"/></svg>
</button>
<!-- No aria-label, screen reader reads "button" with no context -->
```

**Why:** Icon-only buttons need either visible text or an `aria-label`.

---

## ARIA Attributes (When Needed)

### role="switch" (Dark Mode Toggle)

```html
<input 
  id="dark" 
  type="checkbox" 
  class="sr-only" 
  role="switch" 
  aria-label="Enable dark mode"
>
<label for="dark">🌙</label>
```

Screen reader announces: "Enable dark mode switch, unchecked"

### role="status" (Status Messages)

```html
<div role="status" aria-live="polite" class="alert alert-success">
  ✓ Changes saved successfully
</div>
```

Screen reader announces dynamically when the message appears.

### aria-label (Unlabeled Controls)

```html
<button aria-label="Close menu" class="btn-icon">×</button>
```

Screen reader announces: "Close menu, button"

### aria-describedby (Additional Help Text)

```html
<input 
  id="password" 
  type="password" 
  class="form-input"
  aria-describedby="password-hint"
>
<div id="password-hint" class="form-hint">
  At least 12 characters, including a number
</div>
```

Screen reader announces the hint when the input is focused.

### aria-expanded (Collapsible Sections)

```html
<button aria-expanded="false" aria-controls="menu">
  Menu
</button>
<nav id="menu" style="display: none;">
  <!-- Menu items -->
</nav>
```

JavaScript toggles `aria-expanded` and visibility together.

---

## Color & Contrast

### Token-Based Approach (Recommended)

Use Nordover's semantic color tokens. They're pre-tested for contrast:

```css
.my-component {
  background: var(--color-surface);      /* Has 4.5:1 contrast */
  color: var(--color-fg);                 /* with foreground */
  border: 1px solid var(--color-border); /* Visible in light & dark */
}
```

### Custom Color Approach

If you need custom colors, verify contrast:

1. Use a contrast checker: https://webaim.org/resources/contrastchecker/
2. Test in both light and dark modes
3. Test with color-blind simulators: https://www.color-blindness.com/coblis-color-blindness-simulator/

```css
.error-badge {
  background: #dc2626;  /* 3:1 contrast minimum */
  color: white;         /* with white text */
}

@media (prefers-color-scheme: dark) {
  .error-badge {
    background: #7f1d1d;  /* Lighter in dark mode */
  }
}
```

### Don't Rely on Color Alone

```html
<!-- ✅ Do this: Color + pattern -->
<div class="status status-error">❌ Error: Invalid email</div>

<!-- ❌ Avoid this: Color only -->
<div style="color: red;">❌ Invalid email</div>
```

---

## Keyboard Navigation

### Tab Order

```html
<!-- ✅ Natural order -->
<form>
  <input type="text" placeholder="Name">        <!-- Tab 1 -->
  <input type="email" placeholder="Email">      <!-- Tab 2 -->
  <button type="submit">Submit</button>         <!-- Tab 3 -->
</form>

<!-- ❌ Bad: Hidden elements in tab order -->
<form>
  <input type="hidden" style="position: absolute;">  <!-- Trap! -->
  <input type="text" placeholder="Name">
</form>
```

### tabindex Usage

```html
<!-- ✅ Only for custom components -->
<div role="button" tabindex="0" onclick="handleClick()">
  Action
</div>

<!-- ❌ Don't hijack natural order -->
<button tabindex="100">Submit</button>
<button tabindex="1">Login</button>
```

### Focus Indicators

Nordover provides `:focus-visible`. Don't remove it:

```css
/* ✅ Do this: Enhance if needed */
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}

/* ❌ Never do this */
:focus-visible {
  outline: none; /* Trap for keyboard users! */
}
```

---

## Screen Reader Testing

### Quick Checklist

- [ ] All buttons/links have clear labels
- [ ] All inputs are associated with labels
- [ ] Form validation messages are announced
- [ ] Images have alt text
- [ ] Headings are hierarchical (h1, h2, h3...)
- [ ] Modal dialogs trap focus and announce
- [ ] Error messages are announced immediately
- [ ] Status updates are announced live

### Test with VoiceOver (Mac)

```bash
# Enable VoiceOver
Cmd + F5

# Navigate
VO + Right Arrow = Next item
VO + Left Arrow = Previous item
VO + Space = Activate button
Cmd + Option + Arrow = Navigate rotor
```

### Test with NVDA (Windows)

```bash
# Download free: https://www.nvaccess.org/

# Navigate
Tab = Next focusable
Shift+Tab = Previous focusable
Enter = Activate button
Space = Toggle checkbox
Arrow keys = Move within component
```

---

## Common Mistakes

### ❌ Mistake 1: Placeholder as Label

```html
<input type="email" placeholder="Email address">
```

**Problem:** Placeholder disappears when typing. Screen reader doesn't announce it.

**Fix:**
```html
<label for="email">Email address</label>
<input id="email" type="email" placeholder="example@domain.com">
```

### ❌ Mistake 2: Image Without Alt Text

```html
<img src="company-logo.png">
```

**Problem:** Screen reader announces "image" with no context.

**Fix:**
```html
<img src="company-logo.png" alt="Acme Corporation logo">
```

### ❌ Mistake 3: Skip Heading Level

```html
<h1>Page Title</h1>
<h3>Section Heading</h3>  <!-- Skipped h2! -->
```

**Problem:** Screen readers expect h1 → h2 → h3 hierarchy.

**Fix:**
```html
<h1>Page Title</h1>
<h2>Section Heading</h2>
<h3>Subsection</h3>
```

### ❌ Mistake 4: Remove Focus Styles

```css
*:focus {
  outline: none; /* Trap for keyboard users! */
}
```

**Problem:** Keyboard users can't see where they are.

**Fix:**
```css
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

---

## Testing in Your Application

### Automated Testing with axe-core

```javascript
// React example
import { axe, toHaveNoViolations } from 'jest-axe';

describe('My Component', () => {
  test('has no accessibility violations', async () => {
    const { container } = render(<MyComponent />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
```

### Manual Testing Checklist

- [ ] Keyboard navigate entire site (Tab only)
- [ ] Test with screen reader
- [ ] Check color contrast (4.5:1 for text)
- [ ] Zoom to 200% — layout shouldn't break
- [ ] Test with reduced motion enabled
- [ ] Test with inverted colors (OS setting)
- [ ] Test color-blind mode

### Browser DevTools

**Chrome DevTools → Accessibility Tree:**
1. Right-click element
2. Select "Inspect"
3. Click "Accessibility" tab
4. Review role, name, state, properties

---

## Accessibility Resources

- **WCAG 2.1 Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/
- **WebAIM (Practical Tips):** https://webaim.org/
- **MDN Accessibility Guide:** https://developer.mozilla.org/en-US/docs/Web/Accessibility
- **Inclusive Components:** https://inclusive-components.design/
- **Contrast Checker:** https://webaim.org/resources/contrastchecker/
- **Color Blindness Simulator:** https://www.color-blindness.com/coblis-color-blindness-simulator/
- **ARIA Authoring Guide:** https://www.w3.org/WAI/ARIA/apg/

---

## Getting Help

If you find accessibility issues in Nordover:

1. **Report:** Open a GitHub issue with `[a11y]` tag
2. **Test:** Include how you discovered it (screen reader, contrast checker, etc.)
3. **Reference:** Link to WCAG guideline that's affected

Example issue title: `[a11y] Button focus indicator invisible on dark backgrounds`

---

**License:** MIT  
**Last Updated:** 2026-06-01  
**Nordover Version:** 3.0.0 (WCAG 2.1 Level AA)
