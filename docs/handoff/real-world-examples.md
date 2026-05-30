# Real-World Integration Examples

This guide shows how to use Nordover in common project setups.

## Plain HTML / GitHub Pages

**Setup:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Site</title>
  
  <!-- Inter Font -->
  <link rel="preconnect" href="https://rsms.me">
  <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
  
  <!-- Nordover Framework (tokens + components) -->
  <link rel="stylesheet" href="https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css">
  <link rel="stylesheet" href="https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css">
  
  <!-- Your Brand Overrides -->
  <style>
    @layer brand {
      :root {
        --color-accent: oklch(0.55 0.20 230); /* Your brand color */
      }
    }
    
    /* Your custom styles on top of framework */
    .my-component { /* ... */ }
  </style>
</head>
<body>
  <input type="checkbox" id="dark" class="sr-only" role="switch" aria-label="Dark mode">
  
  <!-- Your content using Nordover classes -->
  <nav class="flex justify-between items-center p-3 border-b">
    <h1>My Brand</h1>
    <button class="btn btn-ghost">Menu</button>
  </nav>
  
  <main class="page">
    <section class="page-section">
      <h2 class="t-heading-lg">Welcome</h2>
      <p class="t-body-lg">Get started with Nordover framework</p>
      <button class="btn btn-primary btn-lg">Learn More</button>
    </section>
  </main>
</body>
</html>
```

**Benefits:**
- No build process required
- Zero JavaScript framework dependencies
- Works on GitHub Pages, Netlify static hosting
- Direct CDN consumption

## Next.js Project

**Installation:**
```bash
# Copy CSS files to your project
mkdir -p src/styles
wget https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css -O src/styles/nordover-tokens.css
wget https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css -O src/styles/nordover-components.css
```

**Layout Setup (app/layout.tsx):**
```tsx
import { Inter } from 'next/font/google'
import '@/styles/nordover-tokens.css'
import '@/styles/nordover-components.css'
import '@/styles/brand.css'

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body className={inter.className}>
        <input id="dark" type="checkbox" className="sr-only" role="switch" />
        {children}
      </body>
    </html>
  )
}
```

**Component Example (components/Hero.tsx):**
```tsx
export default function Hero() {
  return (
    <section className="hero-centered py-20 px-4">
      <h1 className="t-display-lg mb-5">Welcome to My App</h1>
      <p className="t-body-lg text-muted mb-8 max-w-2xl mx-auto">
        Built with Nordover design system for beautiful, consistent UI
      </p>
      <div className="cluster gap-4">
        <button className="btn btn-primary btn-lg">Get Started</button>
        <button className="btn btn-secondary btn-lg">Learn More</button>
      </div>
    </section>
  )
}
```

**Theme Toggle (app/ThemeToggle.tsx):**
```tsx
'use client'

import { useEffect, useState } from 'react'

export default function ThemeToggle() {
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    const dark = document.getElementById('dark') as HTMLInputElement
    if (dark) {
      dark.checked = localStorage.getItem('theme') === 'dark'
      setIsDark(dark.checked)
    }
  }, [])

  const toggle = () => {
    const dark = document.getElementById('dark') as HTMLInputElement
    dark.checked = !dark.checked
    localStorage.setItem('theme', dark.checked ? 'dark' : 'light')
    setIsDark(dark.checked)
  }

  return (
    <button onClick={toggle} className="btn btn-ghost" aria-label="Toggle theme">
      {isDark ? '☀️' : '🌙'}
    </button>
  )
}
```

## Vue 3 Project

**Setup (main.ts):**
```ts
import { createApp } from 'vue'
import './styles/nordover-tokens.css'
import './styles/nordover-components.css'
import './styles/brand.css'
import App from './App.vue'

createApp(App).mount('#app')
```

**Component Example (Button.vue):**
```vue
<template>
  <button 
    :class="[
      'btn',
      `btn-${variant}`,
      { 'btn-sm': size === 'sm', 'btn-lg': size === 'lg' }
    ]"
    :disabled="disabled"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
defineProps({
  variant: { type: String, default: 'primary' },
  size: { type: String, default: 'md' },
  disabled: { type: Boolean, default: false }
})
</script>
```

**Usage in Template:**
```vue
<template>
  <div class="page">
    <h1 class="t-heading-lg mb-5">My App</h1>
    <Button variant="primary" size="lg">Click me</Button>
  </div>
</template>

<script setup>
import Button from './components/Button.vue'
</script>
```

## Svelte Project

**Setup (app.svelte):**
```svelte
<script>
  import '../styles/nordover-tokens.css'
  import '../styles/nordover-components.css'
  import '../styles/brand.css'
</script>

<input type="checkbox" id="dark" class="sr-only" role="switch" />

<main class="page">
  <h1 class="t-display-lg mb-5">Welcome</h1>
  <slot />
</main>

<style>
  :global(html) {
    font-family: var(--font-sans);
  }
</style>
```

**Component Example (Button.svelte):**
```svelte
<script>
  export let variant = 'primary'
  export let size = 'md'
  export let disabled = false
</script>

<button
  class="btn btn-{variant}"
  class:btn-sm={size === 'sm'}
  class:btn-lg={size === 'lg'}
  {disabled}
>
  <slot />
</button>
```

## React Project (Without Next.js)

**Setup (index.css):**
```css
@import 'path/to/nordover-tokens.css';
@import 'path/to/nordover-components.css';
@import './brand.css';
```

**App Component (App.tsx):**
```tsx
import { useState } from 'react'

export default function App() {
  const [darkMode, setDarkMode] = useState(false)

  return (
    <>
      <input
        id="dark"
        type="checkbox"
        className="sr-only"
        checked={darkMode}
        onChange={(e) => {
          setDarkMode(e.target.checked)
          localStorage.setItem('theme', e.target.checked ? 'dark' : 'light')
        }}
      />
      
      <main className="page">
        <h1 className="t-display-lg mb-5">React + Nordover</h1>
        <section className="feature-grid">
          {/* Feature cards using Nordover classes */}
        </section>
      </main>
    </>
  )
}
```

## Static Site Generator (Hugo, Jekyll, etc.)

**Setup (config.toml for Hugo):**
```toml
[outputs]
  home = ["HTML"]

[outputFormats]
  [outputFormats.html]
    mediatype = "text/html"
    baseName = "index"
```

**Layout (layouts/_default/baseof.html):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ .Title }}</title>
  
  <link rel="preconnect" href="https://rsms.me">
  <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
  <link rel="stylesheet" href="https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css">
  <link rel="stylesheet" href="https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css">
  
  <style>
    @layer brand {
      :root {
        --color-accent: #2563eb;
      }
    }
  </style>
</head>
<body>
  <input type="checkbox" id="dark" class="sr-only" />
  
  <nav class="flex justify-between items-center p-3 border-b">
    <h1>{{ .Site.Title }}</h1>
  </nav>
  
  <main class="page">
    {{ block "main" . }}{{ end }}
  </main>
</body>
</html>
```

## Custom Monorepo Setup

**Structure:**
```
monorepo/
├── styles/
│   ├── nordover-tokens.css (vendored)
│   ├── nordover-components.css (vendored)
│   └── brand.css
├── packages/
│   ├── web-app/
│   │   └── src/
│   │       └── index.css (imports from ../../styles)
│   ├── mobile-app/
│   │   └── src/
│   │       └── index.css (imports tokens-app)
│   └── shared-components/
│       └── Button.tsx (uses Nordover classes)
```

**Shared Component (packages/shared-components/Button.tsx):**
```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'ghost'
  size?: 'sm' | 'lg'
  children: React.ReactNode
  [key: string]: any
}

export function Button({ 
  variant = 'primary', 
  size = 'md',
  children,
  ...props 
}: ButtonProps) {
  const classes = [
    'btn',
    `btn-${variant}`,
    { 'btn-sm': size === 'sm', 'btn-lg': size === 'lg' }
  ].filter(Boolean).join(' ')

  return <button className={classes} {...props}>{children}</button>
}
```

## Best Practices

### 1. Vendor Framework CSS
- Copy tokens-*.css and components-*.css to your project
- Version them in git
- Update together, never separately
- Pin versions in package.json comments

### 2. Brand Layer Organization
```
styles/
├── nordover-tokens.css (vendored)
├── nordover-components.css (vendored)
├── brand.css
├── typography.css (override --text-*, --fw-*)
├── colors.css (override --color-*, --neutral-h)
└── spacing.css (override --space-*)
```

### 3. Component Wrappers
Don't duplicate Nordover classes in your components:

```tsx
// ❌ Bad: Duplicating classes
function MyButton(props) {
  return <button className="btn btn-primary btn-lg p-3 rounded" {...props} />
}

// ✅ Good: Using framework classes directly
function MyButton({ variant = 'primary', ...props }) {
  return <button className={`btn btn-${variant}`} {...props} />
}
```

### 4. CSS Layering
Maintain @layer order:
```css
@layer tokens, reset, primitives, components, utilities, brand, custom;

@layer custom {
  /* Your custom styles here */
}
```

### 5. Dark Mode
Always include the dark mode toggle checkbox:
```html
<input type="checkbox" id="dark" class="sr-only" role="switch" aria-label="Toggle dark mode" />
```

Handle persistence with JavaScript:
```js
// Load theme from localStorage
const dark = document.getElementById('dark')
dark.checked = localStorage.getItem('theme') === 'dark'

// Save on change
dark.addEventListener('change', () => {
  localStorage.setItem('theme', dark.checked ? 'dark' : 'light')
})
```

## Troubleshooting

**Styles not loading:**
- Ensure CSS files are loaded in correct order (tokens first, then components)
- Check file paths (raw.githubusercontent.com URLs or local paths)
- Verify no CSS minification/purging removing @layer rules

**Dark mode not working:**
- Checkbox with id="dark" must be present in DOM
- Browser dev tools → check if `:root:has(#dark:checked)` selector visible
- Ensure dark mode toggle is wired to checkbox

**Components look different than styleguide:**
- Check if brand.css is overriding colors
- Verify token values match expected values
- Check browser zoom level (100%)

## Support

For issues, open an issue at: https://github.com/xxnamae/nordover-ui/issues
