# Nordover — Universal Design System Foundation

Production-ready CSS framework providing semantic tokens and building blocks for both web and app projects. Each project composes patterns and pages on top—Nordover provides the foundation, not finished compositions.

**Status:** v1.2.0 ✨ | **Building Blocks:** 30+ semantic components | **WCAG:** AA compliant | **Dark mode:** tonal elevation

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
✅ **Focused Scope** — Building blocks + tokens only (no patterns) — each project composes its own  

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
| **Components** | [Buttons](docs/wiki/topics/nordover-buttons.md) • [Forms](docs/wiki/topics/nordover-forms.md) • [Interactive Styleguide](docs/visual/styleguide.html) |
| **Architecture** | [Component Library ADR](docs/wiki/decisions/2026-05-30-comprehensive-component-library.md) • [Variant System](docs/wiki/decisions/2026-05-30-variant-system.md) • [Testing Strategy](docs/wiki/decisions/2026-05-30-testing-strategy.md) |
| **Full Wiki** | [Browse Documentation](docs/wiki/README.md) |

## Building Blocks

Nordover provides tokens and semantic building blocks for construction, not finished compositions. Each project composes its own patterns and pages using the foundation.

### Tokens (Foundation)
- **Colors**: Semantic OKLCH palette (light/dark modes)
- **Typography**: Display, heading, body scales
- **Spacing**: 8px base grid (--space-1 to --space-8)
- **Motion**: Durations, easing functions
- **Shadows, Radius, Borders**: Semantic system

### Interactive Components
- **Buttons**: Primary, secondary, ghost, tonal, elevated, link (3 sizes)
- **Forms**: Inputs, textarea, checkbox, radio, select, switch
- **Badges & Alerts**: Semantic color variants (success, error, warning, info)
- **Cards**: Default, elevated, bordered, subtle
- **Data Display**: Tables, pagination, avatar, skeleton, empty states

### Complex Components
- **Modals & Dialogs**: Header, content, footer sections
- **Accordion**: Expandable content sections
- **Tabs**: List triggers and content panes
- **Date Picker**: Month calendar with navigation
- **File Upload**: Drag-drop, file list, progress
- **Stepper**: Multi-step progress indicator
- **Search Bar**: Input with results dropdown
- **Tooltip & Menu**: Popup, content, trigger patterns
- **Toast & Notifications**: Viewport positioning
- **Breadcrumb & Navigation**: Link trails

### Layout Utilities
- **Primitives**: `.stack`, `.cluster`, `.grid-auto`, `.page`, `.section`
- **Spacing**: Gap, margin, padding utilities
- **Typography**: Text alignment, sizing, weight utilities
- **Display**: Flex, block, hidden utilities
- **Animation**: Fade-in, slide, scale, spin utilities
- **Responsive**: Mobile-first breakpoints, container queries
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
│   │   ├── styleguide.html     # Unified interactive styleguide
│   │   └── styleguide-chrome.css
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
