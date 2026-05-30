# ADR: Component Variant System

**Status:** Approved  
**Date:** 2026-05-30  
**Author:** Claude Code Agent

## Summary

Establish a structured variant system for Nordover components that enables composition, state management, and behavioral variants without duplicating component code.

## Problem

Current implementation provides:
- Base components (.btn, .form-input, .badge)
- Size modifiers (.btn-sm, .btn-lg)
- Style modifiers (.btn-primary, .btn-secondary)
- State variants (disabled, checked, open)

**Missing:**
- Systematic approach to combining variants
- Behavioral variants (loading, skeleton, error)
- Composition patterns for complex UI
- Visual state matrix documentation
- Guidance on variant combinations

**Pain point:** Developers must discover variants through CSS inspection or documentation.

## Solution

Implement a three-tier variant system:

### Tier 1: Style Variants (mutually exclusive)
Applied to same element, choose ONE per category:

**Button Styles:**
- `.btn-primary` - Primary action (accent color)
- `.btn-secondary` - Secondary action (border)
- `.btn-ghost` - Tertiary action (no border)
- `.btn-link` - Text link style
- `.btn-elevated` - Tactile variant (app-context)

**Badge Styles:**
- `.badge-success` - Success state (green)
- `.badge-error` - Error state (red)
- `.badge-warning` - Warning state (orange)
- `.badge-info` - Info state (blue)

**Usage Rule:** Apply ONE style variant per element

### Tier 2: Size/Density Variants (independent)
Applied alongside style variants, can COMBINE:

**Button Sizes:**
- `.btn-sm` - Small (compact)
- (default) - Medium (standard)
- `.btn-lg` - Large (prominent)

**Button Spacing:**
- `.btn-touch` - Mobile-friendly (44px minimum)

**Usage Rule:** Can apply WITH style variant:
```html
<button class="btn btn-primary btn-lg">Large Primary</button>
<button class="btn btn-secondary btn-sm">Small Secondary</button>
```

### Tier 3: State/Behavioral Variants (contextual)
Applied for specific states, OVERRIDE default behavior:

**Loading State:**
```html
<button class="btn btn-primary" aria-busy="true" disabled>
  <span class="spinner"></span>
  Loading...
</button>
```

**Error State:**
```html
<input class="form-input" aria-invalid="true">
<span class="field-error">Invalid input</span>
```

**Skeleton/Placeholder:**
```html
<div class="skeleton" style="height: 1.5rem; width: 12rem;"></div>
```

**Disabled State:**
```html
<button class="btn btn-primary" disabled>Disabled</button>
```

## Composition Matrix

### Button Variant Combinations

| Style | Small | Medium | Large | Touch | Disabled |
|-------|-------|--------|-------|-------|----------|
| Primary | ✅ | ✅ | ✅ | ✅ | ✅ |
| Secondary | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ghost | ✅ | ✅ | ✅ | ✅ | ✅ |
| Link | ❌ | ✅ | ❌ | ❌ | ❌ |
| Elevated | ✅ | ✅ | ✅ | ✅ | ✅ |

**Rules:**
- Link buttons skip sizes (always inherit text size)
- All style variants support sm/lg sizes
- Touch variant applies to all styles
- Disabled overrides all other states

### Form Input Variants

| Type | Disabled | Error | Focus | Read-only |
|------|----------|-------|-------|-----------|
| Text | ✅ | ✅ | ✅ | ✅ |
| Checkbox | ✅ | ❌ | ✅ | ✅ |
| Select | ✅ | ✅ | ✅ | ❌ |
| Textarea | ✅ | ✅ | ✅ | ✅ |
| Toggle | ✅ | ❌ | ✅ | ✅ |

## Behavioral Variants

### Loading/Pending
For components showing async work:
```html
<div class="spinner"></div> <!-- Spinner animation -->
<div class="skeleton" style="height: 2rem;"></div> <!-- Placeholder -->
```

### Empty State
When no content available:
```html
<div class="empty-state">
  <div class="empty-state-icon">📦</div>
  <h3 class="empty-state-title">No items</h3>
  <p class="empty-state-text">Create your first item</p>
</div>
```

### Error/Invalid
When validation fails:
```html
<input class="form-input" aria-invalid="true">
<span class="field-error">Invalid format</span>
```

### Success
When action succeeds:
```html
<span class="badge badge-success">
  <svg class="icon icon-sm"><use href="#i-check"/></svg>
  Saved
</span>
```

## Variant Naming Convention

### Naming Rules
1. **Descriptive**: Name describes visual or functional purpose
2. **Consistent**: Use same naming across component families
3. **Unambiguous**: No overlap with other variants
4. **Short**: Prefer `.sm` over `.small`, `.lg` over `.large`

### Naming Pattern

```
.COMPONENT-BASE[-STYLE-VARIANT][-SIZE-VARIANT]
```

Examples:
- `.btn-primary` - Button with primary style
- `.btn-primary-sm` - Small primary button (alternate: `.btn-primary.btn-sm`)
- `.badge-success` - Badge with success styling
- `.form-toggle` - Toggle switch variant of form input

### Breaking from Pattern (Justify)

Some variants break pattern for clarity:
- `.form-checkbox` vs `.form-radio` (different semantics)
- `.form-toggle` vs `.form-switch` (different purposes: general toggle vs app-specific)

## Variant Application Patterns

### Pattern 1: Modifier Classes
```html
<button class="btn btn-primary btn-lg">Large Primary</button>
```

**Pros:** Clear intent, multiple modifiers possible  
**Cons:** More classes in HTML  
**Use for:** Most components

### Pattern 2: Data Attributes (Alternative)
```html
<button class="btn" data-variant="primary" data-size="lg">Large Primary</button>
```

**Pros:** Cleaner HTML (fewer classes)  
**Cons:** Less obvious in markup  
**Not used:** Nordover uses modifier classes for clarity

### Pattern 3: Wrapper Classes (Complex)
```html
<div class="alert alert-error">
  <div class="alert-icon">!</div>
  <div class="alert-content">Error message</div>
</div>
```

**Pros:** Semantic structure for complex components  
**Cons:** More HTML nesting  
**Use for:** Multi-element components

## Future Variant Expansion

### Planned for Fase 2.5+

1. **Interaction Variants**
   - `.btn-loading` - Explicit loading state
   - `.form-input-loading` - Input with loading indicator

2. **Emphasis Variants**
   - `.badge-outline` - Outlined badge
   - `.btn-block` - Full-width button

3. **Color Variants**
   - `.btn-success`, `.btn-error`, `.btn-warning`
   - Custom color support via CSS variables

4. **Icon Variants**
   - `.icon-{color}` - Icon colors (.icon-success, .icon-error)
   - `.icon-sm`, `.icon-lg` - Icon sizes

5. **Responsive Variants** (CSS Grid pattern)
   - Hide/show variants based on breakpoint
   - Display variants (`.hidden`, `.visible-sm`, `.visible-md`)

## Implementation Checklist

- ✅ Document all current variants
- ✅ Establish composition matrix
- ✅ Define naming conventions
- ✅ Create variant examples in wiki
- ⬜ Implement loading variants
- ⬜ Implement emphasis variants
- ⬜ Add color variants to buttons/badges
- ⬜ Create responsive variant utilities
- ⬜ Write component variant reference guide

## Rationale

**Why modifiers over BEM blocks?**
- Modifiers are more composable (combine multiple)
- Simpler class names
- Aligns with utility-first approach

**Why explicit sizes over defaults?**
- Clarity in markup
- Easier to search/replace sizes
- Explicit over implicit (Zen of Python)

**Why separate style/size/state tiers?**
- Clear mental model for developers
- Reduces cognitive load
- Prevents invalid combinations

## References

- Components spec: `2026-05-30-comprehensive-component-library.md`
- Button reference: `nordover-buttons.md`
- Form reference: `nordover-forms.md`
