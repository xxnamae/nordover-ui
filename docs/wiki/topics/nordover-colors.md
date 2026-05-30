# Color System — Nordover

**Status:** Complete  
**Package:** `tokens-web.css` and `tokens-app.css`

## Overview

Nordover uses OKLCH color space with a semantic token system. Colors are defined as CSS variables with light/dark mode variants.

---

## OKLCH Color Space

Why OKLCH?

- **O**K: Lightness (0–1, perceptually uniform)
- **L**: Chroma (0–0.4, color saturation)
- **C**: Hue (0–360°, color wheel)

**Benefits:**
- Perceptually uniform (equal steps = equal visual difference)
- Better dark mode support (adjust lightness, keep hue/saturation)
- Easy to generate color families (vary L, keep H+C constant)
- Works in modern browsers (Chrome 111+, Firefox 113+, Safari 15.4+)

**Example:**
```css
--color-accent: oklch(0.55 0.20 230); /* 55% lightness, 0.20 chroma, 230° hue (blue) */
```

---

## Semantic Token Structure

### Core Palette

```css
:root {
  /* Background & Surface */
  --color-bg: #FFFFFF;           /* Page background (light mode) */
  --color-surface: #FFFFFF;      /* Card/input background */
  --color-subtle: var(--gray-100); /* Subtle backgrounds (hover) */
  
  /* Foreground & Text */
  --color-fg: var(--gray-900);   /* Primary text color */
  --color-muted: var(--gray-500); /* Secondary text, disabled */
  
  /* Accent & Interaction */
  --color-accent: var(--gray-900);        /* Primary button, links */
  --color-accent-fg: var(--gray-50);      /* Text on accent background */
  --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);
  --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, white);
  --color-focus: #0066FF;         /* Focus ring color (high contrast) */
  
  /* Borders */
  --color-border: var(--gray-200); /* Card borders, dividers */
  
  /* Semantic Colors (Status) */
  --success: oklch(0.56 0.16 160);       /* Green */
  --error: oklch(0.55 0.22 28);          /* Red */
  --warning: oklch(0.66 0.17 65);        /* Amber */
  --info: oklch(0.58 0.18 245);          /* Blue */
  
  /* Subtle/Strong variants */
  --success-subtle: color-mix(in oklch, var(--success) 10%, var(--color-bg));
  --success-strong: color-mix(in oklch, var(--success) 70%, black);
  --error-subtle: color-mix(in oklch, var(--error) 10%, var(--color-bg));
  --error-strong: color-mix(in oklch, var(--error) 75%, black);
  --warning-subtle: color-mix(in oklch, var(--warning) 14%, var(--color-bg));
  --warning-strong: color-mix(in oklch, var(--warning) 72%, black);
  --info-subtle: color-mix(in oklch, var(--info) 10%, var(--color-bg));
  --info-strong: color-mix(in oklch, var(--info) 68%, black);
}
```

---

## Neutral Grayscale

Nordover uses a **single-axis neutral system**: change `--neutral-h` (hue) to shift all grays.

```css
:root {
  --neutral-h: 250;          /* Blue-ish hue (default) */
  --neutral-c: 0.004;        /* Minimal chroma (nearly neutral) */
  
  --gray-50:   oklch(0.99  var(--neutral-c) var(--neutral-h));  /* Brightest */
  --gray-100:  oklch(0.965 var(--neutral-c) var(--neutral-h));
  --gray-200:  oklch(0.92  var(--neutral-c) var(--neutral-h));
  --gray-300:  oklch(0.87  var(--neutral-c) var(--neutral-h));
  --gray-400:  oklch(0.72  var(--neutral-c) var(--neutral-h));
  --gray-500:  oklch(0.50  var(--neutral-c) var(--neutral-h));  /* Mid-tone */
  --gray-600:  oklch(0.43  var(--neutral-c) var(--neutral-h));
  --gray-700:  oklch(0.30  var(--neutral-c) var(--neutral-h));
  --gray-800:  oklch(0.17  var(--neutral-c) var(--neutral-h));
  --gray-900:  oklch(0.10  var(--neutral-c) var(--neutral-h));  /* Darkest */
  --gray-950:  oklch(0.07  var(--neutral-c) var(--neutral-h));
}
```

### Gray Scale Contrast Ratios (WCAG AA)

| From | To | Ratio | WCAG AA |
|------|-------|--------|----------|
| gray-50 (bg) | gray-900 (text) | 18:1 | ✅ Pass (AAA) |
| gray-50 (bg) | gray-700 (text) | 10.5:1 | ✅ Pass (AAA) |
| gray-100 (bg) | gray-700 (text) | 8.8:1 | ✅ Pass (AAA) |
| gray-100 (bg) | gray-600 (text) | 5.2:1 | ✅ Pass (AA) |

---

## Light Mode (Web Package Default)

```css
:root {
  --color-bg: #FFFFFF;           /* white */
  --color-fg: var(--gray-900);   /* near-black */
  --color-accent: var(--gray-900); /* black buttons */
  --neutral-h: 250; /* cool grays */
}
```

**Characteristics:**
- High contrast (black on white = 21:1)
- Accent is dark/bold
- Suitable for content-rich, editorial designs
- Default for `tokens-web.css`

---

## Dark Mode (App Package Default)

Triggered by CSS selector: `:root:has(#dark:checked)`

```html
<input id="dark" type="checkbox" class="sr-only" />
```

```css
:root:has(#dark:checked) {
  --color-bg: var(--gray-950);       /* near-black */
  --color-fg: var(--gray-50);        /* white text */
  --color-surface: var(--gray-900);  /* dark cards */
  --color-subtle: var(--gray-800);   /* dark hover */
  --color-accent: oklch(0.65 0.20 240); /* lighter blue for contrast */
  --neutral-h: 250; /* maintain consistency */
}
```

**Characteristics:**
- Reduced eye strain in low-light environments
- Accent is lighter/brighter
- Surface details subtly elevated
- Default for `tokens-app.css` (can toggle via checkbox)

### Dark Mode Contrast Verification

| Element | Light | Dark | Ratio | WCAG |
|---------|-------|------|-------|------|
| **Text on bg** | gray-900 on white | gray-50 on gray-950 | 18:1 | ✅ AAA |
| **Accent button** | gray-900 | oklch(0.65 0.20 240) | 8.5:1 | ✅ AA |
| **Muted text** | gray-500 | gray-400 | 6.2:1 | ✅ AA |
| **Success badge** | oklch(0.56 0.16 160) | oklch(0.60 0.18 160) | 4.5:1 | ✅ AA |

---

## Brand Override Pattern

In your project's CSS, add a `@layer brand` block:

```css
/* project/styles/brand.css */
@layer brand {
  :root {
    /* Shift all grays to warmer tone */
    --neutral-h: 30; /* warm orange-ish hue */
    
    /* Override accent color */
    --color-accent: oklch(0.55 0.20 230); /* branded blue */
    --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);
    --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, white);
    
    /* Optional: override semantic colors */
    --success: oklch(0.56 0.16 140); /* lime green instead of teal */
  }
  
  /* Dark mode overrides */
  :root:has(#dark:checked) {
    --color-accent: oklch(0.65 0.20 230); /* lighter for dark mode */
  }
}
```

**Rules:**
- ✅ Change `--neutral-h` to shift grayscale
- ✅ Override `--color-accent` and semantic colors
- ❌ Never change `--gray-*` directly (breaks contrast)
- ❌ Never override tokens on component level
- ✅ Always maintain WCAG AA contrast (4.5:1 minimum)

---

## Semantic Color Usage

### Success
- Background: `--success-subtle` (soft green)
- Text: `--success-strong` (dark green)
- Icon/accent: `--success` (green)

**Example:**
```html
<div style="background: var(--success-subtle); color: var(--success-strong);">
  ✓ Changes saved
</div>
```

### Error
- Background: `--error-subtle` (soft red)
- Text: `--error-strong` (dark red)
- Icon/accent: `--error` (red)

### Warning
- Background: `--warning-subtle` (soft amber)
- Text: `--warning-strong` (dark amber)
- Icon/accent: `--warning` (amber)

### Info
- Background: `--info-subtle` (soft blue)
- Text: `--info-strong` (dark blue)
- Icon/accent: `--info` (blue)

---

## Generating Color Variants

### Using `color-mix()` (modern approach)

```css
/* 85% of color mixed with white = lighter */
--color-hover: color-mix(in oklch, var(--color-accent) 85%, white);

/* 70% of color mixed with white = even lighter */
--color-active: color-mix(in oklch, var(--color-accent) 70%, white);

/* 50% of color mixed with black = darker */
--color-dark: color-mix(in oklch, var(--color-accent) 50%, black);
```

### OKLCH Lightness Adjustment

If you need precise control, directly adjust lightness:

```css
/* Original: oklch(0.55 0.20 230) — 55% lightness */
/* Lighter version: 70% lightness */
--color-accent-light: oklch(0.70 0.20 230);

/* Darker version: 40% lightness */
--color-accent-dark: oklch(0.40 0.20 230);
```

---

## Chart & Data Visualization Colors

For use in charts, data visualizations, and multi-series displays:

```css
--chart-1: oklch(0.55 0.15 145); /* teal */
--chart-2: oklch(0.62 0.14 70);  /* orange */
--chart-3: oklch(0.55 0.18 245); /* blue */
--chart-4: oklch(0.55 0.20 295); /* purple */
--chart-5: oklch(0.60 0.12 195); /* cyan */
--chart-6: oklch(0.58 0.20 350); /* red-pink */
--chart-7: oklch(0.65 0.12 220); /* light blue */
--chart-8: oklch(0.58 0.16 30);  /* warm red */
```

**Characteristics:**
- All colors meet WCAG AA contrast on white/dark backgrounds
- Hues equally spaced for visual distinction
- 8-color palette covers most chart needs

---

## Accessibility Requirements

1. **Contrast Minimum**: All text must meet WCAG AA (4.5:1 for normal text, 3:1 for large text)
2. **No Color Alone**: Status/meaning cannot rely on color; use patterns, text, or icons
3. **Focus Indicator**: `--color-focus` is always `#0066FF` (high contrast, standard)
4. **Motion**: Colors should transition smoothly with `--duration-fast` easing

---

## Testing Your Color System

### Contrast Checker
Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to verify:
```
Foreground: oklch(0.55 0.20 230)
Background: #FFFFFF
Ratio: 5.2:1 ✅
```

### Dark Mode Testing
1. Add `<input id="dark" type="checkbox">` to HTML
2. Open DevTools
3. Click checkbox to toggle dark mode
4. Verify contrast ratios in both modes

---

## References

- `tokens-web.css`: Light mode, editorial defaults
- `tokens-app.css`: Dark mode default, compact app design
- [OKLCH in CSS](https://oklch.com/) — interactive color picker
- [WCAG 2.1 SC 1.4.3 Contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
