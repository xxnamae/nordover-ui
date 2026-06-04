# Advanced Customization & Component Extension Guide

**For:** Teams extending Nordover with custom components or brand-specific variants  
**Audience:** Developers, designers  
**Difficulty:** Intermediate

---

## Table of Contents

1. [Understanding CSS Layers](#understanding-css-layers)
2. [Color Customization](#color-customization)
3. [Creating Custom Components](#creating-custom-components)
4. [Extending Existing Components](#extending-existing-components)
5. [Typography Customization](#typography-customization)
6. [Dark Mode Customization](#dark-mode-customization)
7. [Common Customization Patterns](#common-customization-patterns)
8. [Testing Custom Styles](#testing-custom-styles)

---

## Understanding CSS Layers

Nordover uses **CSS `@layer`** to create a clean hierarchy:

```css
@layer tokens        /* 1. Design tokens (variables) */
       reset         /* 2. Browser normalization */
       primitives    /* 3. Layout, typography foundations */
       components    /* 4. 41 pre-built components */
       utilities     /* 5. Responsive helpers */
       brand;        /* 6. YOUR CUSTOMIZATIONS (highest priority) */
```

**Key Principle:** Your brand layer automatically wins specificity wars.

### Why This Matters

```css
/* Nordover component (in @layer components) */
.btn { background: var(--color-primary); }

/* Your customization (in @layer brand) */
@layer brand {
  .btn { background: var(--color-accent); }
  /* This automatically overrides the component! */
}
```

**No need for `!important` or overly specific selectors.**

---

## Color Customization

### Approach 1: Override Semantic Colors (Simple)

Use this when your brand colors match Nordover's semantic structure:

```css
/* brand.css */
@layer brand {
  :root {
    /* Override semantic colors */
    --color-accent: oklch(0.50 0.20 210);      /* Brand blue */
    --color-accent-fg: oklch(1.0 0.0 0);       /* White for contrast */
    --color-success: oklch(0.55 0.18 140);     /* Brand green */
    --color-error: oklch(0.55 0.20 30);        /* Brand red */
    --color-warning: oklch(0.65 0.16 70);      /* Brand yellow */
  }
  
  :root:has(#dark:checked) {
    /* Dark mode overrides */
    --color-accent: oklch(0.70 0.18 210);      /* Lighter for dark */
    --color-success: oklch(0.70 0.15 140);
    --color-error: oklch(0.70 0.18 30);
  }
}
```

**Best for:** Standard brand color schemes

### Approach 2: Add New Named Colors (Moderate)

Use this when you need additional specialized colors:

```css
@layer brand {
  :root {
    /* New brand color palette */
    --color-brand-1: oklch(0.50 0.20 210);     /* Primary */
    --color-brand-2: oklch(0.45 0.15 200);     /* Secondary */
    --color-brand-neutral: oklch(0.50 0.008 250);  /* Neutral */
    
    /* Create new semantic tokens from them */
    --color-accent: var(--color-brand-1);
    --color-accent-secondary: var(--color-brand-2);
  }
}
```

**Best for:** Complex multi-color brands

### Approach 3: Neutral Tone Customization (Advanced)

Change the "gray" tone used throughout:

```css
@layer brand {
  :root {
    /* Shift neutral tone from cool blue-gray to warm beige */
    --neutral-h: 30;      /* Hue shift: blue (250) → beige (30) */
    --neutral-c: 0.004;   /* Keep chroma same for consistency */
    
    /* All grays update automatically! */
    /* --gray-50, --gray-100, ... --gray-950 are recalculated */
  }
}
```

**Best for:** Overall aesthetic shifts (warm/cool/colorful)

---

## Creating Custom Components

### Pattern 1: Simple Component (CSS Only)

```css
/* brand.css */
@layer brand {
  .testimonial {
    padding: var(--space-5);
    border-radius: var(--radius-lg);
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    position: relative;
  }
  
  .testimonial::before {
    content: '"';
    position: absolute;
    top: -10px;
    left: var(--space-4);
    font-size: 4rem;
    color: var(--color-accent);
    opacity: 0.2;
  }
  
  .testimonial-text {
    font-size: var(--text-lg);
    font-style: italic;
    margin-bottom: var(--space-3);
    color: var(--color-fg);
  }
  
  .testimonial-author {
    font-weight: var(--fw-semibold);
    font-size: var(--text-sm);
    color: var(--color-muted);
  }
}
```

**Usage:**
```html
<blockquote class="testimonial">
  <p class="testimonial-text">Nordover saved us weeks of design work</p>
  <footer class="testimonial-author">Sarah Johnson, Product Lead</footer>
</blockquote>
```

### Pattern 2: Component with Variants

```css
@layer brand {
  /* Base style */
  .badge-custom {
    padding: var(--space-2) var(--space-3);
    border-radius: var(--radius-full);
    font-size: var(--text-xs);
    font-weight: var(--fw-semibold);
    display: inline-block;
  }
  
  /* Variant: feature flag */
  .badge-custom.feature {
    background: color-mix(in oklch, var(--color-accent) 20%, var(--color-bg));
    color: var(--color-accent);
  }
  
  /* Variant: deprecated */
  .badge-custom.deprecated {
    background: var(--color-subtle);
    color: var(--color-muted);
    text-decoration: line-through;
  }
  
  /* Variant: experimental */
  .badge-custom.experimental {
    background: color-mix(in oklch, var(--color-warning) 20%, var(--color-bg));
    color: var(--color-warning);
    border: 1px dashed var(--color-warning);
  }
}
```

**Usage:**
```html
<span class="badge-custom feature">New</span>
<span class="badge-custom deprecated">Old API</span>
<span class="badge-custom experimental">Beta</span>
```

### Pattern 3: Complex Interactive Component

```css
@layer brand {
  /* Rating widget */
  .rating {
    display: flex;
    gap: var(--space-1);
  }
  
  .rating-star {
    background: transparent;
    border: none;
    cursor: pointer;
    font-size: 1.5rem;
    padding: 0;
    transition: all var(--duration-fast);
  }
  
  .rating-star:hover,
  .rating-star.active {
    transform: scale(1.1);
    color: var(--color-accent);
  }
  
  .rating-star:focus-visible {
    outline: 2px solid var(--color-accent);
    outline-offset: 2px;
    border-radius: 4px;
  }
}
```

**HTML + JavaScript:**
```html
<div class="rating" role="group" aria-label="Product rating">
  <button class="rating-star" aria-label="1 star" data-value="1">★</button>
  <button class="rating-star" aria-label="2 stars" data-value="2">★</button>
  <button class="rating-star" aria-label="3 stars" data-value="3">★</button>
  <button class="rating-star" aria-label="4 stars" data-value="4">★</button>
  <button class="rating-star" aria-label="5 stars" data-value="5">★</button>
</div>
```

---

## Extending Existing Components

### Example 1: Add Button Variant

```css
@layer brand {
  /* New button size */
  .btn.btn-xl {
    padding: var(--space-4) var(--space-6);
    font-size: var(--text-lg);
  }
  
  /* New button style */
  .btn.btn-gradient {
    background: linear-gradient(
      135deg,
      var(--color-accent) 0%,
      color-mix(in oklch, var(--color-accent) 80%, var(--color-primary)) 100%
    );
    color: var(--color-accent-fg);
    border-color: transparent;
  }
  
  .btn.btn-gradient:hover {
    filter: brightness(1.1);
  }
}
```

**Usage:**
```html
<button class="btn btn-gradient btn-xl">Get Started</button>
```

### Example 2: Extend Input with Additional States

```css
@layer brand {
  /* Success state */
  .form-input.success {
    border-color: var(--color-success);
    background: color-mix(in oklch, var(--color-success) 5%, var(--color-bg));
  }
  
  .form-input.success::after {
    content: '✓';
    position: absolute;
    right: var(--space-3);
    color: var(--color-success);
  }
  
  /* Disabled state enhancement */
  .form-input:disabled {
    cursor: not-allowed;
    opacity: 0.6;
  }
  
  /* Loading state */
  .form-input.loading {
    background: linear-gradient(
      90deg,
      var(--color-subtle),
      color-mix(in oklch, var(--color-accent) 10%, var(--color-bg)),
      var(--color-subtle)
    );
    background-size: 200% 100%;
    animation: shimmer 2s infinite;
  }
  
  @keyframes shimmer {
    0%, 100% { background-position: 200% 0; }
    50% { background-position: 0 0; }
  }
}
```

---

## Typography Customization

### Change Font Stack

```css
@layer brand {
  :root {
    --font-display: "Playfair Display", serif;  /* Custom serif */
    --font-sans: "DM Sans", sans-serif;         /* Custom sans */
    --font-mono: "Inconsolata", monospace;      /* Custom mono */
  }
}
```

**Don't forget:** Add `@font-face` rules or web font imports before your CSS

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
```

### Adjust Heading Sizes

```css
@layer brand {
  :root {
    /* Make headings slightly smaller/larger */
    --text-6xl: clamp(2.5rem, 2rem + 2.5vw, 4.5rem);  /* Was 3.25-5.75rem */
    --text-5xl: clamp(2rem, 1.75rem + 1.5vw, 3.5rem);
  }
}
```

### Add Letter Spacing to Headings

```css
@layer brand {
  .t-display-xl,
  .t-display-lg,
  .t-heading-lg {
    letter-spacing: -0.02em;  /* Tighter */
  }
}
```

---

## Dark Mode Customization

### Override Colors for Dark Mode Only

```css
@layer brand {
  /* Light mode (default) */
  :root {
    --color-accent: oklch(0.50 0.20 210);
  }
  
  /* Dark mode specific */
  :root:has(#dark:checked) {
    --color-accent: oklch(0.70 0.18 210);  /* Lighter in dark */
  }
}
```

### Add Dark Mode-Specific Styles

```css
@layer brand {
  /* Light mode */
  .card {
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  }
  
  /* Dark mode: stronger shadow */
  :root:has(#dark:checked) .card {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  }
}
```

---

## Common Customization Patterns

### Pattern: Add Accent Color Variants

```css
@layer brand {
  /* Base accent already exists */
  /* Add secondary accent for different purposes */
  
  --color-accent-secondary: oklch(0.55 0.18 340);  /* Pink/purple */
  --color-accent-tertiary: oklch(0.55 0.20 120);   /* Green */
  
  /* Use in components */
  .btn.btn-secondary { background: var(--color-accent-secondary); }
  .btn.btn-tertiary { background: var(--color-accent-tertiary); }
}
```

### Pattern: Add Custom Spacing Scale

```css
@layer brand {
  :root {
    /* Tighter spacing for dense layouts */
    --space-tight: var(--space-1);      /* 0.25rem */
    --space-compact: var(--space-2);    /* 0.5rem */
    --space-standard: var(--space-3);   /* 1rem */
    --space-generous: var(--space-5);   /* 1.5rem */
    --space-spacious: var(--space-6);   /* 2rem */
  }
  
  .dense .card { gap: var(--space-compact); }
  .normal .card { gap: var(--space-standard); }
  .spacious .card { gap: var(--space-spacious); }
}
```

### Pattern: Add Brand-Specific Shadows

```css
@layer brand {
  :root {
    --shadow-subtle: 0 1px 2px color-mix(in oklch, var(--color-fg) 5%, transparent);
    --shadow-base: 0 4px 12px color-mix(in oklch, var(--color-fg) 10%, transparent);
    --shadow-elevated: 0 12px 24px color-mix(in oklch, var(--color-fg) 15%, transparent);
  }
  
  .card { box-shadow: var(--shadow-base); }
  .card:hover { box-shadow: var(--shadow-elevated); }
}
```

---

## Testing Custom Styles

### Visual Regression Testing

Create a visual test checklist:

```markdown
## Custom Component Testing Checklist

### Light Mode
- [ ] Component renders without errors
- [ ] Colors are correct
- [ ] Spacing looks balanced
- [ ] Typography is readable
- [ ] No text overflow
- [ ] Hover states visible

### Dark Mode  
- [ ] Colors update correctly
- [ ] Contrast maintained (4.5:1 for text)
- [ ] No white or black hardcodes visible
- [ ] Shadows visible

### Responsive
- [ ] Looks good at 480px (mobile)
- [ ] Looks good at 768px (tablet)
- [ ] Looks good at 1024px (desktop)

### Accessibility
- [ ] Interactive elements focusable
- [ ] Focus indicators visible
- [ ] Color not only differentiator
- [ ] Works without hover (touch devices)
```

### CSS Validation

Check for common mistakes:

```css
/* ❌ WRONG: Hardcoded colors break dark mode */
@layer brand {
  .card { background: white; }
}

/* ✅ RIGHT: Use tokens */
@layer brand {
  .card { background: var(--color-surface); }
}

/* ❌ WRONG: Using !important defeats layer system */
@layer brand {
  .btn { background: blue !important; }
}

/* ✅ RIGHT: Let layer system work */
@layer brand {
  .btn { background: var(--color-accent); }
}
```

---

## Performance Considerations

### Minimize CSS Size

```css
/* ❌ Redundant: Repeat for every variant */
.btn-primary { padding: var(--space-3); font-size: var(--text-base); }
.btn-secondary { padding: var(--space-3); font-size: var(--text-base); }

/* ✅ Better: Use base class + modifier */
.btn { padding: var(--space-3); font-size: var(--text-base); }
.btn.btn-primary { background: var(--color-primary); }
.btn.btn-secondary { background: var(--color-secondary); }
```

### Leverage CSS Variables

```css
/* ❌ Inefficient: Calculate in CSS */
@layer brand {
  .stat { color: oklch(0.55 0.20 210); }
  .error { color: oklch(0.55 0.20 30); }
  .success { color: oklch(0.55 0.20 140); }
}

/* ✅ Efficient: Reuse with variables */
@layer brand {
  :root {
    --accent-h: 210;
    --accent-value: oklch(0.55 0.20 var(--accent-h));
  }
  
  .stat { color: var(--accent-value); }
  
  :root:has(#dark:checked) {
    --accent-h: 220;  /* Adjust hue, same lightness/chroma */
  }
}
```

---

## Advanced: CSS Custom Properties Cascade

Control style application order:

```css
/* Layer 1: Nordover defaults (lowest priority) */
/* @layer components { .btn { background: blue; } } */

/* Layer 2: Your brand overrides */
@layer brand {
  .btn { background: var(--color-accent); }
}

/* Outside layers: Inline styles (highest priority) */
/* <button style="background: red;"> would override! */
```

**Recommendation:** Keep everything in `@layer brand` to avoid specificity issues.

---

## Resources

- **Token Reference:** `docs/visual/tokens/tokens-web.css`
- **Component Examples:** `docs/visual/styleguide.html` (unified web + app)
- **Architecture & Decisions:** `docs/wiki/decisions/`
- **OKLCH Color Tool:** https://oklch.com/
- **CSS Layers Explainer:** https://developer.mozilla.org/en-US/docs/Web/CSS/@layer

---

## Common Issues & Solutions

### Issue: Colors don't update in dark mode

**Solution:** Use CSS variables, not hardcoded colors
```css
/* ❌ Won't update */
.card { background: #ffffff; }

/* ✅ Updates automatically */
.card { background: var(--color-surface); }
```

### Issue: Custom component conflicts with Nordover

**Solution:** Use `@layer brand` to ensure your styles win
```css
/* ✅ This always overrides Nordover components */
@layer brand {
  .btn { /* Your custom button styles */ }
}
```

### Issue: Spacing doesn't match rest of system

**Solution:** Use token variables for consistency
```css
/* ❌ Random value */
.card { padding: 20px; }

/* ✅ From token scale */
.card { padding: var(--space-5); }
```

---

**License:** MIT  
**Last Updated:** 2026-06-01  
**Nordover Version:** 1.2.0
