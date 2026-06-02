# Nordover — Common UI Patterns & Recipes

**Version:** 1.2.0  
**Status:** Pattern Catalog  
**Last Updated:** 2026-06-02

---

## Introduction

This guide catalogs common UI patterns built from Nordover's base components and tokens. Each pattern provides:

1. **HTML structure** — Semantic, accessible markup
2. **Explanation** — Why this pattern is structured this way
3. **Variations** — Common alternatives
4. **Dark mode notes** — How the pattern adapts
5. **Accessibility checklist** — What to verify

Use these as templates for common layouts and interactions.

---

## Section 1: Data Display Patterns

### Pattern: Sortable Data Table

**Use case:** Lists of data that users may want to sort/filter

```html
<div class="table-container">
  <table class="table">
    <thead>
      <tr>
        <th>
          <button class="table-sort" aria-label="Sort by name">
            Name
            <svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg>
          </button>
        </th>
        <th>
          <button class="table-sort" aria-label="Sort by date">
            Date
            <svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg>
          </button>
        </th>
        <th>Status</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Alice Johnson</td>
        <td>2026-05-15</td>
        <td><span class="badge badge-success">Active</span></td>
        <td>
          <button class="btn btn-ghost btn-sm" aria-label="Edit Alice Johnson">
            <svg class="icon"><use href="#i-edit"/></svg>
          </button>
          <button class="btn btn-ghost btn-sm" aria-label="Delete Alice Johnson">
            <svg class="icon"><use href="#i-trash"/></svg>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

**Accessibility:**
- [ ] Sort buttons have `aria-label` describing the action
- [ ] Current sort indicator is visible (icon or text)
- [ ] Table headers are actual `<th>` elements
- [ ] Row actions are keyboard accessible

**Variation: Vertical Card Layout (Mobile)**

```html
<div class="stack gap-3">
  <div class="table-row-card">
    <div class="table-row-label">Name</div>
    <div class="table-row-value">Alice Johnson</div>
    
    <div class="table-row-label">Date</div>
    <div class="table-row-value">2026-05-15</div>
    
    <div class="table-row-label">Status</div>
    <div class="table-row-value">
      <span class="badge badge-success">Active</span>
    </div>
  </div>
</div>
```

---

### Pattern: Statistics Dashboard

**Use case:** Overview cards showing key metrics

```html
<div class="grid-auto">
  <div class="stat-card">
    <div class="stat-value">1,234</div>
    <div class="stat-label">Total Users</div>
    <div class="stat-change positive">
      <svg class="icon-sm"><use href="#i-arrow-up"/></svg>
      12% this month
    </div>
  </div>
  
  <div class="stat-card">
    <div class="stat-value">$45.2K</div>
    <div class="stat-label">Revenue</div>
    <div class="stat-change positive">
      <svg class="icon-sm"><use href="#i-arrow-up"/></svg>
      8% MoM growth
    </div>
  </div>
  
  <div class="stat-card">
    <div class="stat-value">92.5%</div>
    <div class="stat-label">Uptime</div>
    <div class="stat-change negative">
      <svg class="icon-sm"><use href="#i-arrow-down"/></svg>
      0.5% down from last month
    </div>
  </div>
</div>
```

**CSS for stat card:**

```css
@layer brand {
  .stat-card {
    padding: var(--space-5);
    border-radius: var(--radius-lg);
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }
  
  .stat-value {
    font-size: var(--text-4xl);
    font-weight: var(--fw-bold);
    color: var(--color-accent);
  }
  
  .stat-label {
    font-size: var(--text-sm);
    color: var(--color-muted);
    text-transform: uppercase;
    letter-spacing: var(--tracking-wider);
  }
  
  .stat-change {
    display: flex;
    align-items: center;
    gap: var(--space-1);
    font-size: var(--text-sm);
  }
  
  .stat-change.positive {
    color: var(--color-success);
  }
  
  .stat-change.negative {
    color: var(--color-error);
  }
}
```

---

## Section 2: Form Patterns

### Pattern: Multi-Step Form (Stepper)

**Use case:** Long forms broken into logical steps

```html
<div class="form-stepper">
  <!-- Progress indicator -->
  <div class="stepper-progress">
    <div class="stepper-step active" aria-current="step">
      <div class="stepper-number">1</div>
      <div class="stepper-label">Personal Info</div>
    </div>
    <div class="stepper-connector"></div>
    <div class="stepper-step">
      <div class="stepper-number">2</div>
      <div class="stepper-label">Address</div>
    </div>
    <div class="stepper-connector"></div>
    <div class="stepper-step">
      <div class="stepper-number">3</div>
      <div class="stepper-label">Review</div>
    </div>
  </div>

  <!-- Form content -->
  <form class="stack gap-5">
    <!-- Step 1 -->
    <fieldset class="stepper-content active">
      <legend class="t-heading-md">Personal Information</legend>
      
      <div class="stack gap-4">
        <label for="firstName">First Name *</label>
        <input id="firstName" type="text" class="form-input" required>
      </div>
      
      <div class="stack gap-4">
        <label for="lastName">Last Name *</label>
        <input id="lastName" type="text" class="form-input" required>
      </div>
    </fieldset>

    <!-- Navigation -->
    <div class="cluster gap-3">
      <button type="button" class="btn btn-secondary" disabled>← Back</button>
      <button type="button" class="btn btn-primary">Next →</button>
    </div>
  </form>
</div>
```

**CSS for stepper:**

```css
@layer brand {
  .stepper-progress {
    display: flex;
    align-items: center;
    gap: var(--space-4);
    margin-bottom: var(--space-6);
  }
  
  .stepper-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-2);
  }
  
  .stepper-number {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--color-subtle);
    border: 2px solid var(--color-border);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: var(--fw-bold);
    transition: all var(--duration-base);
  }
  
  .stepper-step.active .stepper-number {
    background: var(--color-accent);
    color: var(--color-accent-fg);
    border-color: var(--color-accent);
  }
  
  .stepper-connector {
    flex: 1;
    height: 2px;
    background: var(--color-border);
  }
  
  .stepper-content {
    display: none;
  }
  
  .stepper-content.active {
    display: block;
  }
}
```

---

### Pattern: Inline Form Validation

**Use case:** Real-time feedback as users fill out forms

```html
<form class="stack gap-4">
  <div class="form-group">
    <label for="email">Email Address</label>
    <input 
      id="email" 
      type="email" 
      class="form-input" 
      aria-describedby="email-hint email-error"
      required
    >
    <div id="email-hint" class="form-hint">
      We'll never share your email
    </div>
    <div id="email-error" class="form-error" style="display: none;">
      ⚠️ Please enter a valid email address
    </div>
  </div>

  <div class="form-group">
    <label for="password">Password</label>
    <input 
      id="password" 
      type="password" 
      class="form-input" 
      aria-describedby="password-requirements"
      required
    >
    <div id="password-requirements" class="form-requirements">
      <div class="requirement unmet">
        <svg class="icon-sm"><use href="#i-x"/></svg>
        At least 12 characters
      </div>
      <div class="requirement unmet">
        <svg class="icon-sm"><use href="#i-x"/></svg>
        One uppercase letter
      </div>
      <div class="requirement met">
        <svg class="icon-sm"><use href="#i-check"/></svg>
        One number
      </div>
    </div>
  </div>

  <button type="submit" class="btn btn-primary">Create Account</button>
</form>
```

**CSS for validation:**

```css
@layer brand {
  .form-group {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
  }
  
  .form-input.error {
    border-color: var(--color-error);
    background: color-mix(in oklch, var(--color-error) 5%, var(--color-bg));
  }
  
  .form-error {
    color: var(--color-error);
    font-size: var(--text-sm);
  }
  
  .form-requirements {
    display: flex;
    flex-direction: column;
    gap: var(--space-2);
    padding: var(--space-3);
    background: var(--color-subtle);
    border-radius: var(--radius-sm);
  }
  
  .requirement {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    font-size: var(--text-sm);
    color: var(--color-muted);
  }
  
  .requirement.met {
    color: var(--color-success);
  }
}
```

---

## Section 3: Navigation Patterns

### Pattern: Breadcrumb Navigation

**Use case:** Show user's location in hierarchy

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li>
      <a href="/">Home</a>
    </li>
    <li>
      <svg class="icon-sm" aria-hidden="true"><use href="#i-chevron-right"/></svg>
      <a href="/products">Products</a>
    </li>
    <li>
      <svg class="icon-sm" aria-hidden="true"><use href="#i-chevron-right"/></svg>
      <a href="/products/laptops">Laptops</a>
    </li>
    <li aria-current="page">
      <svg class="icon-sm" aria-hidden="true"><use href="#i-chevron-right"/></svg>
      <span>MacBook Pro 16"</span>
    </li>
  </ol>
</nav>
```

**CSS:**

```css
@layer brand {
  .breadcrumb {
    display: flex;
    align-items: center;
    gap: var(--space-2);
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .breadcrumb a {
    color: var(--color-accent);
    text-decoration: none;
    transition: color var(--duration-base);
  }
  
  .breadcrumb a:hover {
    color: var(--color-accent-hover);
  }
  
  .breadcrumb [aria-current="page"] {
    color: var(--color-muted);
  }
}
```

---

### Pattern: Tab Navigation

**Use case:** Switch between related content sections

```html
<div class="tabs">
  <div role="tablist" class="tabs-list">
    <button 
      role="tab" 
      aria-selected="true" 
      aria-controls="tab-content-1" 
      id="tab-1" 
      class="tab-button active"
    >
      Overview
    </button>
    <button 
      role="tab" 
      aria-selected="false" 
      aria-controls="tab-content-2" 
      id="tab-2" 
      class="tab-button"
    >
      Details
    </button>
    <button 
      role="tab" 
      aria-selected="false" 
      aria-controls="tab-content-3" 
      id="tab-3" 
      class="tab-button"
    >
      History
    </button>
  </div>

  <div id="tab-content-1" role="tabpanel" class="tab-panel active">
    <div class="stack gap-3">
      <h3>Overview</h3>
      <p>Content for overview tab...</p>
    </div>
  </div>

  <div id="tab-content-2" role="tabpanel" class="tab-panel" style="display: none;">
    <div class="stack gap-3">
      <h3>Details</h3>
      <p>Content for details tab...</p>
    </div>
  </div>

  <div id="tab-content-3" role="tabpanel" class="tab-panel" style="display: none;">
    <div class="stack gap-3">
      <h3>History</h3>
      <p>Content for history tab...</p>
    </div>
  </div>
</div>
```

**CSS:**

```css
@layer brand {
  .tabs-list {
    display: flex;
    border-bottom: 2px solid var(--color-border);
    gap: var(--space-1);
  }
  
  .tab-button {
    padding: var(--space-3) var(--space-4);
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    color: var(--color-muted);
    cursor: pointer;
    transition: all var(--duration-base);
  }
  
  .tab-button:hover {
    color: var(--color-fg);
  }
  
  .tab-button[aria-selected="true"] {
    color: var(--color-accent);
    border-bottom-color: var(--color-accent);
  }
  
  .tab-panel {
    padding: var(--space-4) 0;
  }
}
```

---

## Section 4: Feedback Patterns

### Pattern: Toast Notification

**Use case:** Non-blocking feedback messages

```html
<div role="status" aria-live="polite" aria-label="Notifications" class="toast-container">
  <div class="toast toast-success">
    <svg class="icon-sm"><use href="#i-check"/></svg>
    <span>Changes saved successfully</span>
    <button class="toast-close" aria-label="Close notification">×</button>
  </div>
</div>
```

**CSS:**

```css
@layer brand {
  .toast-container {
    position: fixed;
    bottom: var(--space-4);
    right: var(--space-4);
    z-index: 1000;
    display: flex;
    flex-direction: column;
    gap: var(--space-3);
  }
  
  .toast {
    display: flex;
    align-items: center;
    gap: var(--space-3);
    padding: var(--space-3) var(--space-4);
    border-radius: var(--radius-md);
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    animation: slideUp var(--duration-base) ease-out;
  }
  
  .toast-success {
    border-left: 4px solid var(--color-success);
    color: var(--color-success);
  }
  
  .toast-error {
    border-left: 4px solid var(--color-error);
    color: var(--color-error);
  }
  
  @keyframes slideUp {
    from {
      transform: translateY(100%);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
}
```

---

### Pattern: Modal Dialog

**Use case:** Get user confirmation or input

```html
<dialog class="modal" open>
  <div class="modal-content">
    <div class="modal-header">
      <h2 id="modal-title" class="t-heading-md">Delete Item?</h2>
      <button class="modal-close" aria-label="Close dialog">×</button>
    </div>
    
    <div class="modal-body">
      <p>This action cannot be undone. Are you sure?</p>
    </div>
    
    <div class="modal-footer">
      <button class="btn btn-secondary">Cancel</button>
      <button class="btn btn-error">Delete</button>
    </div>
  </div>
</dialog>
```

**CSS:**

```css
@layer brand {
  .modal {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(0, 0, 0, 0.5);
    border: none;
    padding: 0;
    margin: 0;
    z-index: 999;
  }
  
  .modal-content {
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    max-width: 500px;
    width: 90%;
    display: flex;
    flex-direction: column;
  }
  
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--space-5);
    border-bottom: 1px solid var(--color-border);
  }
  
  .modal-body {
    padding: var(--space-5);
    flex: 1;
  }
  
  .modal-footer {
    display: flex;
    justify-content: flex-end;
    gap: var(--space-3);
    padding: var(--space-5);
    border-top: 1px solid var(--color-border);
  }
  
  .modal-close {
    background: transparent;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: var(--color-muted);
  }
}
```

---

## Section 5: Layout Patterns

### Pattern: Sidebar + Main Layout

**Use case:** App with persistent navigation

```html
<div class="app-layout">
  <aside class="sidebar">
    <nav class="sidebar-nav">
      <a href="/" class="sidebar-link active">Dashboard</a>
      <a href="/users" class="sidebar-link">Users</a>
      <a href="/settings" class="sidebar-link">Settings</a>
    </nav>
  </aside>
  
  <main class="main-content">
    <div class="page-content">
      <h1>Dashboard</h1>
      <!-- Page content -->
    </div>
  </main>
</div>
```

**CSS:**

```css
@layer brand {
  .app-layout {
    display: grid;
    grid-template-columns: 250px 1fr;
    min-height: 100vh;
  }
  
  .sidebar {
    background: var(--color-surface);
    border-right: 1px solid var(--color-border);
    padding: var(--space-4);
    overflow-y: auto;
  }
  
  .sidebar-nav {
    display: flex;
    flex-direction: column;
    gap: var(--space-1);
  }
  
  .sidebar-link {
    padding: var(--space-3);
    border-radius: var(--radius-sm);
    color: var(--color-fg);
    text-decoration: none;
    transition: all var(--duration-base);
  }
  
  .sidebar-link:hover {
    background: var(--color-subtle);
  }
  
  .sidebar-link.active {
    background: var(--color-accent);
    color: var(--color-accent-fg);
  }
  
  @media (max-width: 768px) {
    .app-layout {
      grid-template-columns: 1fr;
    }
    
    .sidebar {
      display: none;
    }
  }
}
```

---

## Pattern Development Guide

### How to Create a New Pattern

1. **Identify need** — What problem does this pattern solve?
2. **Write semantic HTML** — Use real elements (`<button>`, `<form>`, `<nav>`)
3. **Add ARIA attributes** — Labels, roles, live regions if needed
4. **Define CSS** — Use Nordover tokens in `@layer brand`
5. **Document variations** — Show mobile, light/dark, different states
6. **Accessibility checklist** — List what to verify

### Accessibility Checklist Template

```markdown
**Accessibility:**
- [ ] Semantic HTML (real buttons, forms, etc.)
- [ ] Labels on form inputs
- [ ] ARIA attributes where needed
- [ ] Keyboard navigation works
- [ ] Focus indicators visible
- [ ] Color contrast 4.5:1 for text
- [ ] Works in light and dark mode
- [ ] Tested with screen reader
```

---

## Testing Patterns

### Manual Testing Checklist

For each pattern:

1. **Visual**
   - [ ] Looks good in light mode
   - [ ] Looks good in dark mode
   - [ ] Responsive on mobile (480px)
   - [ ] Responsive on tablet (768px)
   - [ ] Responsive on desktop (1024px+)

2. **Interaction**
   - [ ] All buttons/links are clickable
   - [ ] Hover states are visible
   - [ ] Focus states are visible
   - [ ] Touch-friendly (min 44px tap target)

3. **Keyboard**
   - [ ] Tab navigates through all interactive elements
   - [ ] Shift+Tab goes backward
   - [ ] Enter/Space activates buttons
   - [ ] Escape closes modals/dropdowns

4. **Screen Reader**
   - [ ] All buttons have accessible names
   - [ ] All form inputs have labels
   - [ ] Dynamic content is announced
   - [ ] No confusing or redundant announcements

5. **Performance**
   - [ ] Animations are smooth (60 FPS)
   - [ ] No layout shifts
   - [ ] No jank on interactions

---

## Resources

- **Component Reference:** `docs/visual/styleguide-web.html`
- **Interactive Playground:** `docs/visual/playground.html`
- **Token Documentation:** `docs/visual/tokens/tokens-web.css`
- **Accessibility Guide:** `docs/handoff/ACCESSIBILITY-FOR-IMPLEMENTERS.md`

---

**License:** MIT  
**Last Updated:** 2026-06-01  
**Nordover Version:** 3.0.0
