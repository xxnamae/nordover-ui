# Nordover Design System — Wiki & Documentation

Welcome to the Nordover design system documentation. This wiki contains comprehensive specifications, architecture decisions, and implementation guides.

## Quick Navigation

### 📚 Getting Started
- **[Framework Handoff](../handoff/README.md)** - How to consume Nordover in your project
- **[Real-World Examples](../handoff/real-world-examples.md)** - Integration with Next.js, React, Vue, plain HTML
- **[Monorepo Bootstrap](../handoff/monorepo-bootstrap.md)** - Setting up Nordover in a monorepo

### 🎨 Component Specifications
- **[Buttons](topics/nordover-buttons.md)** - Button variants, sizes, states, accessibility
- **[Forms](topics/nordover-forms.md)** - Inputs, validation, accessibility, layouts
- **[Data Display](#)** (Coming soon) - Tables, pagination, lists
- **[Patterns](#)** (Coming soon) - Section patterns, layouts
- **[Icons & Motion](#)** (Coming soon) - Icon system, animations

### 🏗️ Architecture & Decisions
- **[Component Library ADR](decisions/2026-05-30-comprehensive-component-library.md)** - Architecture of canonical CSS components
- **[Variant System ADR](decisions/2026-05-30-variant-system.md)** - How to compose and combine variants
- **[Testing Strategy ADR](decisions/2026-05-30-testing-strategy.md)** - Quality assurance approach
- **[Shippable Components ADR](decisions/2026-05-30-shippbar-komponent-css.md)** - Why components are extracted to canonical CSS

### 🔍 Reference
- **[Glossary](glossary.md)** - Terminology and concepts
- **[Color System](#)** (Coming soon) - OKLCH palette, contrast ratios
- **[Typography System](#)** (Coming soon) - Font scales, weights, line heights
- **[Spacing System](#)** (Coming soon) - Spacing scale and utilities
- **[Motion System](#)** (Coming soon) - Animation tokens and utilities

### 🧪 Quality & Testing
- **[Testing Strategy](decisions/2026-05-30-testing-strategy.md)** - Accessibility, visual regression, performance
- **[Accessibility Guidelines](#)** (Coming soon) - WCAG compliance, best practices
- **[Performance Budgets](#)** (Coming soon) - CSS file sizes, metrics

## Framework Status

### ✅ Completed Phases

**Fase 1A-1D: Foundation Components (560 lines)**
- Buttons: 5 variants × 3 sizes
- Forms: input, textarea, checkbox, radio, select, toggle
- Sections: hero, feature grid, CTA cards, pricing
- Data: tables, pagination, badges, alerts, modals

**Fase 1J: High-Value Complex Components (120 lines)**
- Date picker with calendar UI
- Autocomplete/tag input
- Multi-step stepper form
- File upload with progress
- Advanced data table

**Fase 1K: Web-Only Content Components (100 lines)**
- Blog cards with metadata
- Testimonials and quotes
- Timeline component
- Search bar with suggestions
- Accordion component

**Fase 1L: Mobile & Responsive (80 lines)**
- Mobile navigation drawer
- Touch-friendly targets (44px+)
- Responsive table wrapper
- Container queries support
- Responsive breakpoints

**Fase 1M: Icon & Motion System (120 lines)**
- Icon color variants
- Animation utilities (spin, pulse, fade, slide, scale)
- Transition utilities
- Accessibility (prefers-reduced-motion)

**UTILITIES: Composition Toolkit (200+ lines)**
- Display utilities (.flex, .grid, .block)
- Spacing utilities (.mt-*, .p-*, .gap-*)
- Typography utilities (.text-center, .font-bold)
- Color utilities (.text-accent, .bg-subtle)
- Sizing utilities (.w-full, .max-w-*)

### 📋 Documentation Completed

**Fase 4: Component Specifications**
- ✅ Button specifications (variants, sizes, states, accessibility)
- ✅ Form specifications (inputs, validation, accessibility)
- ⬜ Data display specifications (TBD)
- ⬜ Pattern specifications (TBD)

**Fase 2: Variant System**
- ✅ Documented three-tier variant system
- ✅ Created composition matrix
- ✅ Established naming conventions
- ✅ Behavioral variants roadmap

**Fase 5: Real-World Examples**
- ✅ Plain HTML setup
- ✅ Next.js integration
- ✅ Vue 3 setup
- ✅ Svelte setup
- ✅ React setup
- ✅ Static site generators
- ✅ Monorepo patterns
- ✅ Best practices & troubleshooting

**Fase 2.5: Testing Strategy**
- ✅ Visual regression testing approach
- ✅ Accessibility audit strategy (WCAG AA)
- ✅ Performance testing targets
- ✅ Browser compatibility matrix
- ✅ Integration testing plans
- ✅ CI/CD configuration
- ✅ Pre-release checklist

### 🔲 Pending Phases

**Fase 2: Variant System Implementation**
- Loading/loading variants
- Emphasis variants (outline, block)
- Color variants
- Responsive variants

**Data Display Specifications**
- Table patterns and best practices
- Pagination strategies
- List item patterns
- Grid layouts

**Pattern Specifications**
- Section patterns (hero, feature, CTA, pricing)
- Layout patterns (sidebar, main, footer)
- Navigation patterns

**Icon & Color Systems**
- Icon library definition
- Icon naming conventions
- Color palette documentation
- Contrast ratio verification

## Component Implementation Status

| Component | Status | Lines | Variants | Accessible | Responsive |
|-----------|--------|-------|----------|------------|-----------|
| Button | ✅ | 15 | 8+ | ✅ | ✅ |
| Input | ✅ | 12 | 1 | ✅ | ✅ |
| Checkbox | ✅ | 12 | 2 | ✅ | ✅ |
| Select | ✅ | 8 | 1 | ✅ | ✅ |
| Toggle | ✅ | 8 | 1 | ✅ | ✅ |
| Table | ✅ | 8 | 1 | ✅ | ✅ |
| Modal | ✅ | 10 | 1 | ✅ | ✅ |
| Badge | ✅ | 6 | 4 | ✅ | ✅ |
| Alert | ✅ | 6 | 4 | ✅ | ✅ |
| Date Picker | ✅ | 20 | 1 | ⚠️ | ✅ |
| Tag Input | ✅ | 15 | 1 | ✅ | ✅ |
| Stepper | ✅ | 12 | 1 | ✅ | ✅ |
| File Upload | ✅ | 18 | 1 | ✅ | ✅ |
| Data Table | ✅ | 12 | 1 | ✅ | ✅ |

**Legend:** ✅ Complete, ⚠️ Partial, ⬜ Pending

## File Structure

```
docs/
├── visual/
│   ├── tokens/
│   │   ├── tokens-web.css      (291 lines)
│   │   └── tokens-app.css      (299 lines)
│   ├── components/
│   │   ├── components-web.css  (672 lines)
│   │   └── components-app.css  (588 lines)
│   ├── styleguide-web.html
│   └── styleguide-app.html
├── handoff/
│   ├── README.md               (Framework consumption guide)
│   ├── monorepo-bootstrap.md   (Monorepo setup)
│   └── real-world-examples.md  (Framework integration examples)
├── wiki/
│   ├── README.md               (This file)
│   ├── glossary.md             (Terminology)
│   ├── topics/
│   │   ├── nordover-buttons.md
│   │   ├── nordover-forms.md
│   │   └── (more coming)
│   └── decisions/
│       ├── 2026-05-30-comprehensive-component-library.md
│       ├── 2026-05-30-variant-system.md
│       ├── 2026-05-30-testing-strategy.md
│       └── 2026-05-30-shippbar-komponent-css.md
```

## Key Metrics

| Metric | Value | Target |
|--------|-------|--------|
| Total CSS | 1,850 lines | < 2,000 |
| Tokens | 590 lines | < 600 |
| Components | 1,260 lines | < 1,500 |
| CSS File Size | ~50KB | < 60KB |
| Components | 40+ | > 30 |
| Button Variants | 8 | > 5 |
| Form Controls | 10 | > 8 |
| WCAG Compliance | AA | AA |
| Browser Support | 90%+ | > 85% |

## How to Use This Wiki

1. **New to Nordover?** Start with [Framework Handoff](../handoff/README.md)
2. **Building with a framework?** See [Real-World Examples](../handoff/real-world-examples.md)
3. **Need component specs?** Browse [Component Specifications](#component-specifications)
4. **Understanding decisions?** Read the [Architecture & Decisions](#architecture--decisions) section
5. **Contributing?** Check [Testing Strategy](decisions/2026-05-30-testing-strategy.md)

## Contributing

To contribute to Nordover:

1. All changes must maintain WCAG AA compliance
2. Components must work in both web and app contexts
3. CSS file size budget must be respected
4. Documentation must be updated alongside code
5. All variants must be tested in the styleguides

See [CLAUDE.md](../../CLAUDE.md) for development guidelines.

## Resources

- **Repository:** https://github.com/xxnamae/nordover-ui
- **Issues:** https://github.com/xxnamae/nordover-ui/issues
- **License:** MIT
- **Maintainer:** Eirik Foleide (eirikfoleide@gmail.com)

## Version History

| Version | Date | Status | Highlights |
|---------|------|--------|-----------|
| 1.0.0-alpha | 2026-05-30 | Current | Complete component library, full documentation |
| — | — | Planned | v1.0.0 stable, component variants, advanced patterns |

---

**Last updated:** 2026-05-30  
**Status:** Nordover v1.0.0-alpha — Complete component library with comprehensive documentation
