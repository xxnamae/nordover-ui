# Icon System — Nordover

**Status:** Complete  
**Package:** `components-web.css` and `components-app.css`

## Overview

Nordover's icon system provides semantic sizing, color variants, and animation utilities for SVG icons. Icons are vector-based (not emoji) and inherit color from parent text color.

---

## Icon Sizing

All sizes use `stroke-width: 1.5` and `fill: none` for consistent line weight.

### Responsive Sizing

```html
<!-- Default (24px) -->
<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">
  <circle cx="12" cy="12" r="9" />
</svg>

<!-- Small (16px) -->
<svg class="icon-sm" viewBox="0 0 24 24">...</svg>

<!-- Large (32px) -->
<svg class="icon-lg" viewBox="0 0 24 24">...</svg>
```

### Size Tokens

| Class | Size | Usage |
|-------|------|-------|
| `.icon-sm` | 16px | inline labels, badges, small buttons |
| `.icon` | 24px | default, button icons, navigation |
| `.icon-lg` | 32px | hero sections, large buttons, feature cards |

**CSS:**
```css
.icon { width: var(--size-icon); height: var(--size-icon); }
.icon-sm { width: var(--size-icon-sm); height: var(--size-icon-sm); }
.icon-lg { width: var(--size-icon-lg); height: var(--size-icon-lg); }
```

Web package: `--size-icon: 24px`, `--size-icon-sm: 16px`, `--size-icon-lg: 32px`  
App package: `--size-icon: 20px`, `--size-icon-sm: 16px`, `--size-icon-lg: 28px` (compact)

---

## Color Variants

Icons inherit `currentColor` by default. Apply color via parent text or utility class.

### Semantic Colors

```html
<!-- Inherit parent color (default) -->
<svg class="icon" style="color: var(--color-fg);">...</svg>

<!-- Explicit variants -->
<svg class="icon icon-primary">...</svg>
<svg class="icon icon-success">...</svg>
<svg class="icon icon-error">...</svg>
<svg class="icon icon-warning">...</svg>
<svg class="icon icon-info">...</svg>
<svg class="icon icon-muted">...</svg>
<svg class="icon icon-subtle">...</svg>
```

**CSS:**
```css
.icon-primary { color: var(--color-accent); }
.icon-success { color: var(--color-success); }
.icon-error { color: var(--color-error); }
.icon-warning { color: var(--color-warning); }
.icon-info { color: var(--color-info); }
.icon-muted { color: var(--color-muted); }
.icon-subtle { color: var(--color-subtle); }
```

### Real-World Example

```html
<div class="alert alert-success">
  <svg class="icon-sm icon-success" viewBox="0 0 24 24">
    <polyline points="20 6 9 17 4 12" stroke="currentColor" stroke-width="2" fill="none" />
  </svg>
  <p>Changes saved successfully</p>
</div>
```

---

## Animations

### Spin Animation (Loading)

```html
<svg class="icon icon-spin" viewBox="0 0 24 24" aria-hidden="true">
  <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2" />
</svg>
```

**CSS:**
```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.icon-spin {
  animation: spin 1s linear infinite;
}
```

Used for: loading states, processing indicators.

### Pulse Animation (Attention)

```html
<svg class="icon icon-pulse" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="4" fill="currentColor" />
</svg>
```

**CSS:**
```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.icon-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
```

Used for: unread badges, live indicators.

### Bounce Animation (Action Call)

```html
<svg class="icon icon-bounce" viewBox="0 0 24 24">
  <path d="..." />
</svg>
```

**CSS:**
```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.icon-bounce {
  animation: bounce 1s ease-in-out infinite;
}
```

Used for: CTAs, promotional icons, scrolling hints.

### Reduced Motion

All animations respect `prefers-reduced-motion: reduce`:

```css
@media (prefers-reduced-motion: reduce) {
  .icon-spin, .icon-pulse, .icon-bounce {
    animation: none;
  }
}
```

---

## Icon Button Pattern

```html
<button class="btn btn-icon" aria-label="Close menu">
  <svg class="icon" viewBox="0 0 24 24">
    <line x1="18" y1="6" x2="6" y2="18" stroke="currentColor" stroke-width="2" />
    <line x1="6" y1="6" x2="18" y2="18" stroke="currentColor" stroke-width="2" />
  </svg>
</button>
```

**CSS:**
```css
.btn-icon {
  width: 2.5rem;
  height: 2.5rem;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-icon .icon {
  width: 1.25rem;
  height: 1.25rem;
}
```

**Accessibility:**
- Icon-only buttons MUST have `aria-label` describing action
- Icon has `aria-hidden="true"` (decorative)
- Button gets `:focus-visible` ring from reset layer

---

## Icon Library Structure

Recommended: store SVG icons in `assets/icons/` directory.

```
assets/icons/
├── check.svg          (24×24 viewBox)
├── close.svg
├── menu.svg
├── chevron-down.svg
├── arrow-right.svg
├── alert-circle.svg
├── check-circle.svg
└── ... (semantic naming)
```

### SVG Best Practices

1. **Viewbox**: Always use `viewBox="0 0 24 24"` (standard)
2. **Stroke**: Use `stroke="currentColor"` (inherit from parent color)
3. **Fill**: Use `fill="none"` for line icons, `fill="currentColor"` for solid icons
4. **Stroke-width**: 1.5px for consistency
5. **Semantic naming**: `check.svg`, `alert.svg`, not `icon-1.svg`

---

## Color + Size Combinations

```html
<!-- Small success icon -->
<svg class="icon-sm icon-success" viewBox="0 0 24 24">...</svg>

<!-- Large error icon -->
<svg class="icon-lg icon-error" viewBox="0 0 24 24">...</svg>

<!-- Spinning loading icon -->
<svg class="icon icon-spin icon-primary" viewBox="0 0 24 24">...</svg>
```

Classes compose freely: `.icon-{size}` + `.icon-{color}` + `.icon-{animation}`

---

## Accessibility Requirements

1. **Decorative icons**: `aria-hidden="true"`
   ```html
   <svg class="icon" aria-hidden="true">...</svg>
   ```

2. **Semantic icons**: provide accessible label via:
   - `aria-label` on parent button
   - `<title>` element inside SVG (screen reader announces)
   - Text label adjacent to icon

3. **Color conveyance**: Never rely on color alone; use icon shape + text or pattern

4. **Touch targets**: Icon buttons minimum 44×44px (mobile)
   ```css
   .btn-icon { width: 2.75rem; height: 2.75rem; } /* 44px on web */
   ```

---

## Token Dependencies

- **Sizing**: `--size-icon`, `--size-icon-sm`, `--size-icon-lg`
- **Colors**: `--color-accent`, `--color-success`, `--color-error`, `--color-warning`, `--color-info`, `--color-muted`, `--color-subtle`
- **Motion**: `--duration-base`, `--ease-out` (for animations)

---

## Common Icon Sizes by Context

| Context | Size | Class | Notes |
|---------|------|-------|-------|
| Inline badge | 16px | `.icon-sm` | within text, tight spacing |
| Button icon | 20–24px | `.icon` | standard interactive size |
| Navigation item | 20–24px | `.icon` | menu, sidebar, breadcrumbs |
| Feature card header | 32px | `.icon-lg` | visual emphasis |
| Section hero | 40–48px | custom | use inline `style` for non-standard |
| Alert/notification | 20px | `.icon-sm` or `.icon` | paired with 14–16px text |

---

## Examples

### Loading Spinner

```html
<div class="flex items-center gap-2">
  <svg class="icon icon-spin icon-primary" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2" />
  </svg>
  <p>Loading...</p>
</div>
```

### Success Message

```html
<div class="alert alert-success">
  <svg class="icon icon-success" viewBox="0 0 24 24">
    <polyline points="20 6 9 17 4 12" stroke="currentColor" stroke-width="2" fill="none" />
  </svg>
  <span>Success!</span>
</div>
```

### Icon Menu

```html
<nav class="flex gap-4">
  <button class="btn btn-icon" aria-label="Home">
    <svg class="icon" viewBox="0 0 24 24"><!-- home icon --></svg>
  </button>
  <button class="btn btn-icon" aria-label="Search">
    <svg class="icon" viewBox="0 0 24 24"><!-- search icon --></svg>
  </button>
</nav>
```

---

## References

- `components-web.css` primitives layer: icon sizing classes
- `nordover-motion.md`: animation keyframes and timing
- `nordover-accessibility.md`: focus management, ARIA patterns
- MDN: [Using the aria-label attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label)
