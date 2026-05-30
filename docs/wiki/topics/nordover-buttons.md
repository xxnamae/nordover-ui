# Nordover — Buttons Specification

## Overview

Nordover provides a flexible button system with 5 semantic variants and 3 size options. Buttons are styled using semantic tokens and support multiple states.

## Button Variants

### Primary Button
Used for primary actions (form submission, navigation, CTAs).

```html
<button class="btn btn-primary">Submit</button>
```

**Styling:**
- Background: `--color-accent`
- Text: `--color-accent-fg`
- Hover: `--color-accent-hover` (lightened)
- Active: `--color-accent-active` (darkened)

**States:**
- Rest: solid accent background
- Hover: lighter accent
- Active: darker accent
- Disabled: 50% opacity

### Secondary Button
Used for alternative actions or to deprioritize actions.

```html
<button class="btn btn-secondary">Cancel</button>
```

**Styling:**
- Background: transparent
- Border: `--border-card`
- Text: `--color-fg`
- Hover: fills with `--color-subtle`

**Best for:** Cancel buttons, secondary navigation, less important actions

### Ghost Button
Used for subtle or tertiary actions.

```html
<button class="btn btn-ghost">Learn More</button>
```

**Styling:**
- Background: transparent
- No border
- Hover: fills with `--color-subtle`

**Best for:** Explore, additional options, low-priority actions

### Link Button
Renders as a text link but with full button accessibility.

```html
<button class="btn btn-link">Read Full Article</button>
```

**Styling:**
- Background: transparent
- Text color: `--color-accent`
- Text decoration: underline
- Hover: opacity change

**Best for:** Inline links, skippable content, web-specific navigation

### Elevated Button
Tactile variant with gradient and shadow (primarily for app context).

```html
<button class="btn btn-elevated">Confirm Action</button>
```

**Styling:**
- Background: Linear gradient (accent 92% → accent)
- Box shadow: Inset highlight + base shadow
- Hover: Enhanced shadow
- Active: Inset shadow effect

**Best for:** SaaS interfaces, important confirmations, tactile feedback

## Button Sizes

### Small (sm)
```html
<button class="btn btn-primary btn-sm">Small</button>
```
- Padding: `--space-2` vertical, `--space-4` horizontal
- Font size: `--text-sm`
- Use for: Compact layouts, data tables, inline actions

### Base (default)
```html
<button class="btn btn-primary">Normal</button>
```
- Padding: `--space-3` vertical, `--space-5` horizontal
- Font size: `--text-base`
- Use for: Most common buttons, navigation

### Large (lg)
```html
<button class="btn btn-primary btn-lg">Large</button>
```
- Padding: `--space-4` vertical, `--space-7` horizontal
- Font size: `--text-lg`
- Use for: Hero CTAs, prominent actions, mobile-focused

## Button States

### Disabled State
```html
<button class="btn btn-primary" disabled>Disabled</button>
```
- Opacity: 50%
- Cursor: `not-allowed`
- No hover effect
- Not focusable via keyboard

### Loading State
Add a spinner before text:
```html
<button class="btn btn-primary" disabled>
  <span class="spinner"></span>
  Processing...
</button>
```

### Icon Integration
```html
<button class="btn btn-primary">
  <svg class="icon icon-sm"><use href="#i-check"/></svg>
  Confirm
</button>
```
- Icon sits left of text with `--space-2` gap
- Use `.icon-sm` for compact buttons
- Remove gap if icon-only: add `aria-label`

## Composition Patterns

### Button Group
```html
<div class="cluster">
  <button class="btn btn-primary">Save</button>
  <button class="btn btn-secondary">Cancel</button>
</div>
```

### Full-width Button
```html
<button class="btn btn-primary w-full">Full Width Action</button>
```

### Button with Badge
```html
<button class="btn btn-secondary">
  Notifications
  <span class="badge badge-error">3</span>
</button>
```

## Touch-Friendly Variants

For mobile and touch devices, add `.btn-touch` for larger hit targets:

```html
<button class="btn btn-primary btn-touch">Touch-Friendly</button>
```
- Minimum 44×44px (touch target standard)
- Increased padding for comfort
- Recommended for mobile-first contexts

## Accessibility

### Keyboard Navigation
- All buttons fully keyboard accessible
- Tab stops on all buttons
- Enter/Space activates buttons
- `:focus-visible` provides clear focus indicator (3px `--color-focus` ring)

### ARIA Labels
- Icon-only buttons require `aria-label`:
  ```html
  <button class="btn btn-ghost" aria-label="Close dialog">×</button>
  ```
- Loading buttons should indicate state:
  ```html
  <button class="btn btn-primary" aria-busy="true">
    <span class="spinner"></span>
    Saving...
  </button>
  ```

### Color Contrast
All button variants meet WCAG AA contrast requirements:
- Primary button: 10.5:1 (text vs background)
- Secondary button: 7.2:1 (text vs background)
- Link button: 6.8:1 (text vs background)

## Theming

Override button colors via the `@layer brand` block:

```css
@layer brand {
  :root {
    --color-accent: oklch(0.55 0.20 230); /* Primary color */
    --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);
    --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, white);
  }
}
```

## Do's and Don'ts

✅ **Do:**
- Use primary buttons for main actions (submit, save, continue)
- Use secondary for alternatives (cancel, clear)
- Use ghost for tertiary actions (learn more, skip)
- Ensure disabled state is visually distinct
- Include icons for clarity when helpful
- Use appropriate size for context (lg on hero, sm in tables)

❌ **Don't:**
- Use all buttons with same variant (hierarchy matters)
- Put too many primary buttons in one view
- Make important buttons too small
- Add animations beyond built-in hover states
- Use buttons for navigation (use `<a>` instead unless styled consistently)
- Disable buttons without clear reason

## Examples

### Form Layout
```html
<form class="stack">
  <div class="field">
    <label class="field-label">Email</label>
    <input type="email" class="form-input" required>
  </div>
  <div class="cluster gap-3">
    <button type="submit" class="btn btn-primary">Send</button>
    <button type="reset" class="btn btn-secondary">Clear</button>
  </div>
</form>
```

### Navigation Bar
```html
<nav class="flex justify-between items-center p-3">
  <h1>Nordover</h1>
  <div class="cluster gap-2">
    <a href="/docs" class="btn btn-ghost">Docs</a>
    <button class="btn btn-primary btn-sm">Get Started</button>
  </div>
</nav>
```

### Empty State
```html
<div class="empty-state">
  <div class="empty-state-icon">📦</div>
  <h2 class="empty-state-title">No items yet</h2>
  <p class="empty-state-text">Create your first item to get started</p>
  <button class="btn btn-primary">Create Item</button>
</div>
```
