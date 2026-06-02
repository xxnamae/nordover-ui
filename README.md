# Nordover — Design System for Nordic Web & Apps

Production-ready CSS framework combining semantic tokens, reusable components, and utilities for both marketing sites and SaaS dashboards.

**Status:** v1.2.0 ✨ | **Components:** 34 core + variants | **WCAG:** AA compliant | **Dark mode:** tonal elevation

## Features

✅ **Dual Packages** — Web (editorial) & App (SaaS) variants with appropriate defaults  
✅ **34 Core Components** — Buttons, forms, cards, tables, modals, navigation, layout primitives, more  
✅ **Semantic Tokens** — OKLCH colors, fluid typography, spacing, motion, shadows  
✅ **Utility Classes** — 100+ utilities for rapid composition without custom CSS  
✅ **Accessibility** — WCAG AA, keyboard navigation, motion preferences, focus management  
✅ **Mobile First** — Touch-friendly targets, responsive breakpoints, container queries  
✅ **Dark Mode** — CSS-based toggle, no JavaScript required  
✅ **Framework Agnostic** — Works with Next.js, Vue, React, plain HTML, static sites  
✅ **Production Ready** — Comprehensive testing strategy, CI/CD ready  
✅ **Well Documented** — Component specs, variant system, real-world examples, testing guides  

## Quick Start

### Plain HTML

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://rsms.me/inter/inter.css">
  <link rel="stylesheet" href="https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css">
  <link rel="stylesheet" href="https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css">
</head>
<body>
  <input type="checkbox" id="dark" class="sr-only" role="switch">
  
  <main class="page">
    <h1 class="t-display-lg">Welcome</h1>
    <button class="btn btn-primary btn-lg">Get Started</button>
  </main>
</body>
</html>
```

### Next.js

```bash
# 1. Copy CSS files to your project
mkdir -p src/styles
wget https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css -O src/styles/nordover-tokens.css
wget https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css -O src/styles/nordover-components.css

# 2. Import in app/layout.tsx
import '@/styles/nordover-tokens.css'
import '@/styles/nordover-components.css'

# 3. Use in components
<button className="btn btn-primary">Click me</button>
```

See [Real-World Examples](docs/handoff/real-world-examples.md) for Vue, React, Svelte, and static site setups.

## Documentation

| Topic | Links |
|-------|-------|
| **Getting Started** | [Handoff Guide](docs/handoff/README.md) • [Real-World Examples](docs/handoff/real-world-examples.md) • [Monorepo Setup](docs/handoff/monorepo-bootstrap.md) |
| **Components** | [Buttons](docs/wiki/topics/nordover-buttons.md) • [Forms](docs/wiki/topics/nordover-forms.md) • [Styleguide](docs/visual/styleguide-web.html) |
| **Architecture** | [Component Library ADR](docs/wiki/decisions/2026-05-30-comprehensive-component-library.md) • [Variant System](docs/wiki/decisions/2026-05-30-variant-system.md) • [Testing Strategy](docs/wiki/decisions/2026-05-30-testing-strategy.md) |
| **Full Wiki** | [Browse Documentation](docs/wiki/README.md) |

## Component Overview

### Foundation (Fase 1A-1D)
- **Buttons**: Primary, secondary, ghost, link, elevated (8 variants)
- **Forms**: Input, textarea, checkbox, radio, select, toggle, range (10+ types)
- **Sections**: Hero, feature grid, CTA cards, pricing cards
- **Data Display**: Tables, pagination, badges, alerts, modals, FAQ

### High-Value (Fase 1J)
- **Date Picker**: Calendar UI with month navigation
- **Tag Input**: Autocomplete with suggestions
- **Stepper**: Multi-step form with progress
- **File Upload**: Drag-drop, progress tracking
- **Data Table**: Sorting, filtering, inline editing

### Content (Fase 1K - Web Only)
- **Blog Cards**: Metadata, categories, read time
- **Testimonials**: Quote blocks with author info
- **Timeline**: Event timeline with dates
- **Search Bar**: Icon-overlaid input with results
- **Accordion**: Collapsible content sections

### Responsive (Fase 1L)
- Mobile navigation drawer with slide animation
- Touch-friendly targets (44×44px minimum)
- Responsive table wrapper
- Responsive breakpoints (60rem, 48rem, 36rem)
- Container queries for adaptive layouts

### Polish (Fase 1M)
- Icon color variants (primary, success, error, warning, info)
- Animation utilities (spin, pulse, bounce, fade, slide, scale)
- Transition utilities (fast, base, slow)
- Full motion accessibility support

### Utilities
- 100+ utility classes for display, flex, spacing, typography, colors, sizing, borders, shadows

## File Sizes

| Package | Tokens | Components | Combined |
|---------|--------|-----------|----------|
| Web | 20 KB | 84 KB | **~104 KB** |
| App | 20 KB | 72 KB | **~92 KB** |

All sizes are uncompressed. With gzip: ~4-5 KB tokens, ~13-16 KB components (total ~17.5 KB web).

## Browser Support

| Browser | Version | Support |
|---------|---------|---------|
| Chrome/Edge | 90+ | ✅ Full |
| Firefox | 88+ | ✅ Full |
| Safari | 14+ | ✅ Full |
| Mobile Chrome | 90+ | ✅ Full |
| Mobile Safari | 14+ | ✅ Full |

**Note:** CSS `@layer`, `color-mix()`, and `:has()` require modern browsers. Graceful degradation for older browsers.

## WCAG Compliance

- ✅ **WCAG AA** - All text passes 4.5:1 contrast minimum
- ✅ **Keyboard Navigation** - All interactive elements focusable and operable
- ✅ **Focus Indicators** - Clear, high-contrast focus rings (3px)
- ✅ **Motion** - Respects `prefers-reduced-motion` media query
- ✅ **Semantic HTML** - Proper heading hierarchy, form labels, ARIA attributes
- ✅ **Dark Mode** - Contrast maintained in both light and dark themes

Accessibility audit checklist: [Testing Strategy](docs/wiki/decisions/2026-05-30-testing-strategy.md)

## Customization

Override tokens in your own CSS:

```css
@layer brand {
  :root {
    /* Primary brand color */
    --color-accent: oklch(0.55 0.20 230);
    
    /* Typography scale */
    --text-base: 16px;
    
    /* Spacing */
    --space-5: 1.5rem;
    
    /* Border radius */
    --radius-md: 8px;
  }
}
```

Never modify:
- `--gray-*` directly (breaks contrast) — use `--neutral-h` instead
- Component CSS in your HTML (edit CSS layer)
- Token names (they're contracts for downstream consumers)

See [Framework Handoff](docs/handoff/README.md) for full customization guide.

## Architecture

```
@layer tokens, reset, primitives, components, utilities, brand
```

1. **Tokens**: CSS variables (colors, spacing, typography, effects)
2. **Reset**: Browser normalization, Inter font fallback
3. **Primitives**: Layout foundations (.stack, .cluster, .page)
4. **Components**: Reusable UI components (buttons, forms, data, content)
5. **Utilities**: Utility classes for composition
6. **Brand**: Your custom token overrides (always last)

See [Component Library ADR](docs/wiki/decisions/2026-05-30-comprehensive-component-library.md) for architecture rationale.

## Variant System

Components support three-tier variants:

```html
<!-- Style variant + Size variant -->
<button class="btn btn-primary btn-lg">Large Primary Button</button>

<!-- Only style required, size and state are optional -->
<button class="btn btn-secondary">Normal Secondary</button>

<!-- With behavioral state -->
<button class="btn btn-primary" aria-busy="true" disabled>
  <span class="spinner"></span>
  Loading...
</button>
```

See [Variant System ADR](docs/wiki/decisions/2026-05-30-variant-system.md) for complete guide.

## Real-World Examples

Framework integrations for popular tools:

- ✅ **Plain HTML** - No build process needed
- ✅ **Next.js** - App Router support with dark mode
- ✅ **Vue 3** - Component wrapper examples
- ✅ **React** - Custom hooks and components
- ✅ **Svelte** - Store-based theme management
- ✅ **Static Generators** - Hugo, Jekyll, 11ty examples
- ✅ **Monorepos** - Shared components and tokens

See [Real-World Examples](docs/handoff/real-world-examples.md).

## Testing & Quality

- ✅ **Visual Regression** - Baseline screenshots with Percy
- ✅ **Accessibility** - axe-core automated + manual WCAG AA audit
- ✅ **Performance** - < 60KB budget, optimized selectors
- ✅ **Browser Compatibility** - Tested across 5+ browsers and viewports
- ✅ **Component Behavior** - Interactive state testing
- ✅ **Documentation** - Code examples validated

Testing strategy and CI/CD setup: [Testing Strategy ADR](docs/wiki/decisions/2026-05-30-testing-strategy.md)

## Project Structure

```
nordover-ui/
├── docs/
│   ├── handoff/                 # Consumer guides
│   │   ├── README.md           (How to use framework)
│   │   ├── monorepo-bootstrap.md
│   │   └── real-world-examples.md
│   ├── visual/
│   │   ├── tokens/             # Canonical CSS tokens
│   │   │   ├── tokens-web.css
│   │   │   └── tokens-app.css
│   │   ├── components/         # Canonical CSS components
│   │   │   ├── components-web.css
│   │   │   └── components-app.css
│   │   ├── styleguide-web.html (Interactive component showcase)
│   │   └── styleguide-app.html
│   └── wiki/                   # Documentation
│       ├── topics/             (Component specifications)
│       ├── decisions/          (ADRs)
│       └── glossary.md
├── index.html                  # Landing page
├── CLAUDE.md                   # Development guidelines
├── LICENSE
└── README.md (this file)
```

## Contributing

To contribute:

1. All changes must maintain WCAG AA compliance
2. CSS file sizes must respect budget (< 60KB)
3. Both web and app packages must stay in sync
4. Comprehensive documentation required
5. Components tested in styleguides

See [CLAUDE.md](CLAUDE.md) for development rules.

## License

MIT License — See [LICENSE](LICENSE) for details.

## Acknowledgments

**Design Inspiration:**
- Linear Design System (onboarding patterns)
- AppStil (SaaS components)
- Nordic Minimalism (Scandinavian simplicity)

**Technical Foundation:**
- WCAG 2.1 AA Compliance
- OKLCH color space (future-proof)
- CSS `@layer` (cascade control)
- Open source best practices

## Support

- 📖 **Documentation:** [Wiki](docs/wiki/README.md)
- 🐛 **Issues:** [GitHub Issues](https://github.com/xxnamae/nordover-ui/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/xxnamae/nordover-ui/discussions)
- 📧 **Contact:** eirikfoleide@gmail.com

---

**Built for Nordic web with ❤️**

Nordover v1.2.0 | [Repository](https://github.com/xxnamae/nordover-ui) | [License](LICENSE)
