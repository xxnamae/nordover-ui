# Data Display Components — Nordover

**Status:** Complete  
**Package:** `components-web.css` and `components-app.css`

## Overview

Data display components present structured information in a way that's easy to scan, filter, sort, and navigate. This includes tables, pagination, badges, alerts, and feedback elements.

---

## Tables

### Basic Table

```html
<table class="data-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice Johnson</td>
      <td>alice@example.com</td>
      <td><span class="badge badge-success">Active</span></td>
    </tr>
    <tr>
      <td>Bob Smith</td>
      <td>bob@example.com</td>
      <td><span class="badge badge-warning">Pending</span></td>
    </tr>
  </tbody>
</table>
```

### Styles

- `.data-table` — Semantic table with borders and hover states
- Rows highlight on hover (subtle background change)
- Headers use `--fw-semibold` (600) weight for distinction
- Cell padding: `var(--space-3)` vertical, `var(--space-4)` horizontal

### Sortable Columns

```html
<th class="sortable" data-sort-key="email">
  Email
  <svg class="icon-sm sort-icon" aria-hidden="true"><!-- ▲▼ --></svg>
</th>
```

**JavaScript requirement:** Consumer implements sort logic and toggles `.active` class on `.sort-icon`.

### Responsive Table

On mobile (`@media (max-width: 48rem)`), wrap in `.table-responsive`:

```html
<div class="table-responsive">
  <table class="data-table"><!-- ... --></table>
</div>
```

Adds horizontal scroll with `overflow-x: auto` and `white-space: nowrap`.

---

## Pagination

### Basic Pagination

```html
<nav class="pagination" aria-label="Pagination">
  <button class="pagination-btn" disabled>&larr; Previous</button>
  <button class="pagination-dot" aria-current="page">1</button>
  <button class="pagination-dot">2</button>
  <button class="pagination-dot">3</button>
  <button class="pagination-btn">Next &rarr;</button>
</nav>
```

### Styles

- `.pagination` — Flexbox row with `gap: var(--space-2)`
- `.pagination-dot` — 2rem square, centered, border on default state
- `.pagination-dot[aria-current="page"]` — filled with `--color-accent`
- `.pagination-btn` — standard button styling (secondary style)
- Disabled state: `opacity: 0.5; cursor: not-allowed`

### Accessibility

- Wrap in `<nav>` with `aria-label="Pagination"`
- Current page: use `aria-current="page"` on active dot
- Buttons are keyboard-navigable (inherit `:focus-visible` from reset layer)

---

## Badges

Inline labels for status, categories, or metadata.

### Variants

```html
<!-- Default (neutral) -->
<span class="badge">Draft</span>

<!-- Color variants -->
<span class="badge badge-success">Active</span>
<span class="badge badge-error">Failed</span>
<span class="badge badge-warning">Pending</span>
<span class="badge badge-info">New</span>

<!-- Outline style (secondary) -->
<span class="badge badge-outline">Optional</span>
```

### Styles

- Display: `inline-flex` with padding `var(--space-1) var(--space-2)`
- Border-radius: `var(--radius-full)` (pill-shaped)
- Font-size: `var(--text-xs)`, font-weight: `--fw-semibold`
- Default: neutral gray background
- `.badge-success`: green background, white text
- `.badge-error`: red background, white text
- `.badge-warning`: amber background, dark text
- `.badge-info`: blue background, white text
- `.badge-outline`: no background, colored border + text

---

## Alerts

Contextual feedback messages for user actions.

### Structure

```html
<div class="alert alert-success" role="alert">
  <svg class="icon-sm" aria-hidden="true"><!-- checkmark --></svg>
  <div>
    <strong>Success!</strong>
    <p>Your changes have been saved.</p>
  </div>
  <button class="alert-close" aria-label="Close">✕</button>
</div>
```

### Variants

- `.alert-success` — green accent, checkmark icon
- `.alert-error` — red accent, X icon
- `.alert-warning` — amber accent, ! icon
- `.alert-info` — blue accent, ℹ icon

### Styles

- Padding: `var(--space-4)`
- Border-left: 4px solid color variant
- Border-radius: `var(--radius-md)`
- Display: flex with `gap: var(--space-3)` and `align-items: flex-start`
- Background: semantic color with 10% opacity (`--*-subtle`)
- `.alert-close` — transparent button, opacity 0.6 on hover

### Accessibility

- `role="alert"` for screen readers (announces immediately)
- Icon has `aria-hidden="true"` (decorative)
- Close button is optional but recommended for dismissible alerts

---

## Modals

### Structure

```html
<dialog class="modal" open>
  <div class="modal-backdrop" onclick="this.closest('dialog').close()"></div>
  <div class="modal-content">
    <header class="modal-header">
      <h2>Dialog Title</h2>
      <button class="modal-close" aria-label="Close">&times;</button>
    </header>
    <div class="modal-body">
      <!-- content -->
    </div>
    <footer class="modal-footer">
      <button class="btn btn-ghost">Cancel</button>
      <button class="btn btn-primary">Confirm</button>
    </footer>
  </div>
</dialog>
```

### Styles

- `.modal` — `<dialog>` element with `position: fixed; inset: 0`
- `.modal-backdrop` — semi-transparent overlay (prevents background interaction)
- `.modal-content` — centered, `max-width: 32rem`, `border-radius: var(--radius-lg)`
- `.modal-header` — flex between, `border-bottom: var(--border-divider)`
- `.modal-body` — padding `var(--space-6)`, default `max-height: 60vh` with vertical scroll
- `.modal-footer` — flex row with `gap: var(--space-3)`, right-aligned buttons

### Focus Management

**JavaScript requirement:** Consumer must implement focus trap:
1. On open: save initial focus, focus first interactive element
2. On close: restore initial focus
3. Trap: prevent Tab/Shift+Tab from leaving modal

Example (vanilla JS):
```js
const modal = document.querySelector('dialog');
const closeBtn = modal.querySelector('.modal-close');

closeBtn.addEventListener('click', () => modal.close());
modal.showModal(); // browser API

// Focus trap: @see MDN dialog element spec
```

### Accessibility

- Use semantic `<dialog>` element (modern browsers)
- `.modal-close` button: `aria-label="Close"` or `title="Close"`
- Modal header `<h2>` or `.modal-title` identifies dialog
- Trap focus within modal (JavaScript responsibility)

---

## Data Table (Advanced)

For tables with sorting, filtering, inline editing hooks.

### Structure

```html
<table class="data-table">
  <thead>
    <tr>
      <th class="sortable" data-sort="name">Name</th>
      <th class="sortable" data-sort="date">Date</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr class="table-row">
      <td>Project Alpha</td>
      <td>2026-05-30</td>
      <td class="table-actions">
        <button class="btn btn-sm btn-ghost">Edit</button>
        <button class="btn btn-sm btn-ghost">Delete</button>
      </td>
    </tr>
  </tbody>
</table>
```

### Sortable Headers

- `.sortable` — cursor pointer, visual indicator of sortability
- Include `data-sort` attribute to identify column
- JavaScript implements sort on click, toggles `.active` class

### Inline Actions

- `.table-actions` — flex row with `gap: var(--space-2)`
- Use `.btn-sm` for compact spacing
- Show/hide based on row hover (optional)

### Responsive Stacking (Mobile)

```css
@supports (container-type: inline-size) {
  .data-table {
    container-type: inline-size;
  }
  
  @container (max-width: 36rem) {
    .data-table thead { display: none; }
    .data-table tbody, tr, td { display: block; }
    td::before { content: attr(data-label); font-weight: var(--fw-semibold); }
  }
}
```

Fallback: use `.table-responsive` wrapper with horizontal scroll.

---

## Component Specifications Summary

| Component | Classes | Key Props | Accessibility |
|-----------|---------|-----------|----------------|
| **Table** | `.data-table` | sorting (JS), responsive wrap | semantic `<thead>/<tbody>`, `.sortable` for headers |
| **Pagination** | `.pagination`, `.pagination-dot`, `.pagination-btn` | current page state | `aria-current="page"`, `<nav aria-label>`, `:focus-visible` |
| **Badge** | `.badge`, `.badge-{success/error/warning/info}`, `.badge-outline` | color, text | decorative (no ARIA) |
| **Alert** | `.alert`, `.alert-{success/error/warning/info}` | dismissible (button), icon | `role="alert"`, `aria-label` on close |
| **Modal** | `.modal`, `.modal-content`, `.modal-header`, `.modal-body`, `.modal-footer` | open/close state (JS), focus trap | `<dialog>`, focus management (JS), `.modal-close` labeled |

---

## Token Dependencies

All data display components use:
- **Colors**: `--color-accent`, `--color-success`, `--color-error`, `--color-warning`, `--color-info`, `--color-fg`, `--color-bg`, `--color-subtle`
- **Spacing**: `--space-1` through `--space-6`, `--gap-tight`, `--gap-component`
- **Typography**: `--text-xs`, `--text-sm`, `--text-base`, `--fw-semibold`, `--fw-medium`
- **Effects**: `--radius-md`, `--radius-full`, `--shadow-sm`, `--border-divider`, `--border-card`
- **Motion**: `--duration-fast`, `--ease-out`

---

## Best Practices

1. **Table readability**: Limit columns on mobile; use horizontal scroll or stacking
2. **Pagination**: Show max 5–7 page dots; use ellipsis (…) for >10 pages
3. **Badges**: Use semantic colors (success = green, error = red) consistently
4. **Alerts**: Dismiss time: 6–8s for success/info, 10s+ for warnings/errors
5. **Modals**: Lock scroll on `<body>` when modal is open (JavaScript)
6. **Focus management**: Always trap focus in modals; indicate with visible outline

---

## References

- `components-web.css` line 200+: badge, alert, modal, table styles
- `components-app.css` line 150+: app-optimized data display (compact spacing)
- `nordover-accessibility.md`: keyboard navigation, focus management details
- WCAG 2.1 SC 1.4.3 (Contrast): all data display colors meet 4.5:1 minimum
