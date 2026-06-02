# Nordover Design System — Framework Integration Guides

**Version:** 3.0.0  
**Last Updated:** 2026-06-01  
**Status:** Production Ready

---

## Overview

Nordover is a **pure CSS design system** designed to work with any framework or no framework at all. This guide covers integration patterns for popular frameworks and build setups.

## Core Principles

1. **Framework-agnostic** — Nordover is pure CSS. No runtime dependencies.
2. **Composition-first** — Use HTML class names to compose components
3. **CSS Cascade** — System tokens → components → brand layer overrides
4. **Dark mode via DOM** — Toggle `<input id="dark" type="checkbox">` for theme switching
5. **No CSS-in-JS bloat** — Use native CSS custom properties and `@layer` for scoping

---

## Quick Start (All Frameworks)

### Step 1: Install

```bash
npm install @xxnamae/nordover-ui
```

### Step 2: Import CSS

Choose your platform:

```html
<!-- Web -->
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css">
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/components/components-web.css">

<!-- App -->
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/tokens/tokens-app.css">
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/components/components-app.css">
```

### Step 3: Use Classes

```html
<div class="page">
  <h1 class="t-display-lg">Welcome</h1>
  <button class="btn btn-primary">Get Started</button>
</div>
```

### Step 4: Dark Mode (Optional)

Add a checkbox to toggle dark mode:

```html
<input id="dark" type="checkbox" class="sr-only" role="switch" aria-label="Dark mode">
```

When checked, `:root:has(#dark:checked)` activates dark mode.

---

## Framework-Specific Guides

### React

#### Setup

```typescript
// App.tsx
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';

export default function App() {
  return (
    <div className="page">
      <h1 className="t-display-lg">Hello React</h1>
      <button className="btn btn-primary">Click Me</button>
    </div>
  );
}
```

#### Dark Mode Hook

```typescript
// useDarkMode.ts
import { useEffect, useState } from 'react';

export function useDarkMode() {
  const [isDark, setIsDark] = useState(false);

  useEffect(() => {
    const checkbox = document.getElementById('dark') as HTMLInputElement;
    if (!checkbox) return;

    const handleChange = () => setIsDark(checkbox.checked);
    checkbox.addEventListener('change', handleChange);

    return () => checkbox.removeEventListener('change', handleChange);
  }, []);

  return {
    isDark,
    toggle: () => {
      const checkbox = document.getElementById('dark') as HTMLInputElement;
      if (checkbox) checkbox.checked = !checkbox.checked;
    }
  };
}
```

#### Component Example

```typescript
// Button.tsx
import React from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'lg' | 'touch';
  children: React.ReactNode;
}

export function Button({ variant = 'primary', size, children }: ButtonProps) {
  const className = ['btn', `btn-${variant}`, size && `btn-${size}`]
    .filter(Boolean)
    .join(' ');

  return <button className={className}>{children}</button>;
}
```

#### CSS Binding Pattern

```typescript
// Use classnames helper for complex logic
import classnames from 'classnames';

<button className={classnames(
  'btn',
  {
    'btn-primary': isPrimary,
    'btn-disabled': isDisabled,
  }
)}>
  {label}
</button>
```

---

### Vue 3

#### Setup

```javascript
// main.ts
import { createApp } from 'vue';
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';
import App from './App.vue';

createApp(App).mount('#app');
```

#### Component Example

```vue
<!-- Button.vue -->
<template>
  <button :class="['btn', `btn-${variant}`, sizeClass]">
    <slot />
  </button>
</template>

<script setup lang="ts">
const props = withDefaults(defineProps<{
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'lg' | 'touch';
}>(), {
  variant: 'primary'
});

const sizeClass = props.size ? `btn-${props.size}` : '';
</script>
```

#### Dark Mode Composable

```typescript
// useDarkMode.ts
import { ref, onMounted } from 'vue';

export function useDarkMode() {
  const isDark = ref(false);

  onMounted(() => {
    const checkbox = document.getElementById('dark') as HTMLInputElement;
    if (checkbox) {
      isDark.value = checkbox.checked;
      checkbox.addEventListener('change', () => {
        isDark.value = checkbox.checked;
      });
    }
  });

  const toggle = () => {
    const checkbox = document.getElementById('dark') as HTMLInputElement;
    if (checkbox) checkbox.checked = !checkbox.checked;
  };

  return { isDark, toggle };
}
```

---

### Svelte

#### Setup

```javascript
// src/main.ts
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';
import App from './App.svelte';

export default new App({ target: document.body });
```

#### Component Example

```svelte
<!-- Button.svelte -->
<script lang="ts">
  export let variant: 'primary' | 'secondary' | 'ghost' = 'primary';
  export let size: 'sm' | 'lg' | 'touch' | '' = '';

  let buttonClass = '';
  $: buttonClass = ['btn', `btn-${variant}`, size && `btn-${size}`]
    .filter(Boolean)
    .join(' ');
</script>

<button class={buttonClass}>
  <slot />
</button>
```

#### Dark Mode Store

```typescript
// src/stores/theme.ts
import { writable } from 'svelte/store';

export const isDark = writable(false);

export function toggleDark() {
  const checkbox = document.getElementById('dark') as HTMLInputElement;
  if (checkbox) {
    checkbox.checked = !checkbox.checked;
    isDark.set(checkbox.checked);
  }
}
```

---

### Web Components

#### Setup

```html
<!-- index.html -->
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css">
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/components/components-web.css">
```

#### Component Example

```typescript
// Button.ts
export class NordoverButton extends HTMLElement {
  connectedCallback() {
    const variant = this.getAttribute('variant') || 'primary';
    const size = this.getAttribute('size') || '';

    const button = document.createElement('button');
    button.className = ['btn', `btn-${variant}`, size && `btn-${size}`]
      .filter(Boolean)
      .join(' ');
    button.textContent = this.textContent;

    this.attachShadow({ mode: 'open' });
    this.shadowRoot!.appendChild(button);
  }
}

customElements.define('nordover-button', NordoverButton);
```

---

### Next.js / Nuxt / SvelteKit

#### CSS Import (Global)

```typescript
// app.tsx or nuxt.config.ts or layout.svelte
import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
import '@xxnamae/nordover-ui/docs/visual/components/components-web.css';
```

#### CSS Import (Specific Pages)

```typescript
// pages/dashboard.tsx
import styles from '@xxnamae/nordover-ui/docs/visual/components/components-web.css';

export default function Dashboard() {
  return (
    <div className="page">
      <h1 className="t-display-lg">Dashboard</h1>
    </div>
  );
}
```

---

## Build Tool Integration

### Vite

```typescript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  css: {
    preprocessorOptions: {
      scss: {
        // Optional: Use Sass for additional preprocessing
      }
    }
  },
  // No special config needed — CSS imports work out of the box
});
```

### Webpack

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  }
};
```

### PostCSS

```javascript
// postcss.config.js
module.exports = {
  plugins: {
    // Optional: Use plugins for CSS processing
    'postcss-nesting': {},
    'autoprefixer': {},
  }
};
```

---

## Dark Mode Implementation

### Option 1: Checkbox Toggle (Recommended)

```html
<input id="dark" type="checkbox" class="sr-only" role="switch" aria-label="Dark mode">
<label for="dark">🌙</label>
```

Nordover automatically activates dark mode when the checkbox is checked:

```css
:root:has(#dark:checked) {
  /* Dark mode tokens override */
}
```

### Option 2: Class-Based Toggle

If you prefer a class-based approach, add this to your brand layer:

```css
@layer brand {
  html.dark { 
    --color-bg: var(--gray-900);
    --color-fg: var(--gray-50);
    /* ... all other dark overrides ... */
  }
}
```

Then toggle the class in JavaScript:

```javascript
document.documentElement.classList.toggle('dark');
```

### Option 3: System Preference

To respect user's system preference:

```javascript
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
document.getElementById('dark').checked = prefersDark;
```

---

## Customization via Brand Layer

### Override Colors

```css
@layer brand {
  :root {
    --color-accent: oklch(0.5 0.2 210);  /* Change accent color */
    --color-bg: oklch(0.99 0 0);         /* Slightly off-white */
  }
}
```

### Override Spacing

```css
@layer brand {
  :root {
    --gap-component: 2rem;  /* Larger gaps */
    --page-padding: 2.5rem; /* More page margin */
  }
}
```

### Override Fonts

```css
@layer brand {
  :root {
    --font-display: "Poppins", sans-serif;
    --font-sans: "Inter", sans-serif;
  }
}
```

---

## Common Patterns

### Navigation Bar with Dark Mode Toggle

```tsx
// React example
export function Header() {
  const { isDark, toggle } = useDarkMode();

  return (
    <header className="app-topbar">
      <h1 className="app-topbar-title">My App</h1>
      <button 
        className={isDark ? 'is-active' : ''} 
        onClick={toggle}
        aria-label="Toggle dark mode"
      >
        {isDark ? '☀️' : '🌙'}
      </button>
    </header>
  );
}
```

### Responsive Grid Layout

```html
<div class="grid-auto">
  <div class="card">Item 1</div>
  <div class="card">Item 2</div>
  <div class="card">Item 3</div>
  <div class="card">Item 4</div>
</div>
```

The grid automatically wraps at `16rem` minimum, making it responsive.

### Form with Validation

```html
<form>
  <fieldset class="stack gap-4">
    <label class="cluster gap-2">
      <input type="email" placeholder="Email" class="form-input" required>
      <span class="form-hint">Required</span>
    </label>
    <label class="cluster gap-2">
      <input type="checkbox"> I agree to terms
    </label>
    <button type="submit" class="btn btn-primary">Submit</button>
  </fieldset>
</form>
```

---

## Performance Tips

1. **Import only what you need**
   ```typescript
   // Instead of importing both, choose one:
   import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css';
   // OR
   import '@xxnamae/nordover-ui/docs/visual/tokens/tokens-app.css';
   ```

2. **Leverage CSS Layers**
   - System components are in `@layer components`
   - Your styles go in `@layer brand`
   - This prevents specificity wars

3. **Use CSS Custom Properties**
   ```css
   .my-card {
     background: var(--color-surface);
     border-color: var(--color-border);
     /* Automatically updates with dark mode */
   }
   ```

4. **Minimize Runtime Bloat**
   - No JavaScript needed for styling
   - Dark mode toggle is pure CSS/HTML
   - Animations use CSS, not JavaScript

---

## Bundle Size Reference

| Platform | Gzipped | Format |
|----------|---------|--------|
| Web | 17.5 KB | CSS (2,082 lines) |
| App | 14.4 KB | CSS (1,465 lines) |

**Note:** This is the complete framework. When imported, your bundler will tree-shake unused CSS (depending on your build tool configuration).

---

## Troubleshooting

### Colors not changing in dark mode?
- Ensure `<input id="dark">` exists in your DOM
- Check that dark mode checkbox is actually toggled
- Use browser DevTools to verify `:has()` selector works (Safari 15.4+, Chrome 105+)

### Classes not applying?
- Verify CSS file is imported before your components
- Check for CSS specificity conflicts (use `@layer` to resolve)
- Ensure class names match exactly (no typos)

### Layout breaking on mobile?
- Check viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Use responsive classes (e.g., `.grid-auto` auto-wraps at 576px)
- Test at actual breakpoints: 480px, 768px, 1024px, 1280px

### Animations laggy?
- Check for `prefers-reduced-motion` setting on your device
- Use DevTools Performance tab to profile
- Verify animations use GPU-accelerated properties (`opacity`, `transform`)

---

## Additional Resources

- **API Reference:** `docs/visual/styleguide-web.html` (web) / `styleguide-app.html` (app)
- **Component Playground:** `docs/visual/playground.html`
- **Performance Benchmarks:** `docs/performance/METRICS.md`
- **Accessibility Testing:** `docs/visual/accessibility-audit.html`
- **GitHub Repo:** [xxnamae/nordover-ui](https://github.com/xxnamae/nordover-ui)

---

## Support & Contributing

- **Issues:** Report bugs on [GitHub Issues](https://github.com/xxnamae/nordover-ui/issues)
- **Discussions:** Share ideas on [GitHub Discussions](https://github.com/xxnamae/nordover-ui/discussions)
- **Contributing:** See `CONTRIBUTING.md` for guidelines

---

**License:** MIT  
**Last Updated:** 2026-06-01  
**Version:** 3.0.0 (Production-Perfect)
