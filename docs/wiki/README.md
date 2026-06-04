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
- **[Data Display](topics/nordover-data-display.md)** - Tables, pagination, badges, alerts, modals
- **[Icons](topics/nordover-icon-system.md)** - Icon sizing, color variants, animations
- **[Motion](topics/nordover-motion.md)** - Animation keyframes, transitions, entrance/exit effects

### 🏗️ Architecture & Decisions
- **[Building Blocks Focus ADR](decisions/2026-06-04-rammeverk-fokus-byggesteiner.md)** - Framework scope: tokens + building blocks only (no patterns)
- **[Component Library ADR](decisions/2026-05-30-comprehensive-component-library.md)** - Architecture of canonical CSS components
- **[Variant System ADR](decisions/2026-05-30-variant-system.md)** - How to compose and combine variants
- **[Testing Strategy ADR](decisions/2026-05-30-testing-strategy.md)** - Quality assurance approach

### 🔍 Reference
- **[Glossary](glossary.md)** - Terminology and concepts
- **[Color System](topics/nordover-colors.md)** - OKLCH palette, semantic colors, dark mode, brand override
- **[Typography System](topics/nordover-typography.md)** - Font scales, weights, line heights, fluid sizing
- **[Spacing System](topics/nordover-spacing.md)** - Spacing scale, responsive gaps, touch targets
- **[Motion System](topics/nordover-motion.md)** - Animation tokens, transitions, entrance effects
- **[Accessibility](topics/nordover-accessibility.md)** - WCAG AA compliance, keyboard navigation, screen reader testing

### 🧪 Quality & Testing
- **[Testing Strategy](decisions/2026-05-30-testing-strategy.md)** - Accessibility, visual regression, performance
- **[Accessibility Guidelines](topics/nordover-accessibility.md)** - WCAG AA compliance, keyboard navigation, best practices
- **[Performance Budgets](#)** (Coming soon) - CSS file sizes, metrics

## Framework Status

### ✅ Completed Components (Layer 1 + Layer 2)

**Layer 1: Tokens**
- Colors (semantic OKLCH palette, light/dark modes)
- Typography (display, heading, body, caption scales)
- Spacing (8px base grid)
- Motion (durations, easing functions)
- Shadows, radius, borders

**Layer 2: Building Blocks (Interactive Components)**
- Buttons (6 variants × 3 sizes)
- Forms (input, textarea, checkbox, radio, select, switch)
- Badges & Alerts (4 color variants each)
- Cards (default, elevated, bordered, subtle)
- Data display (tables, pagination, avatar, skeleton, empty states)
- Complex components (modal, accordion, tabs, date picker, file upload, stepper, search bar, tooltip, menu, toast, breadcrumb, kbd)
- Layout primitives (.stack, .cluster, .grid-auto, .page, .section)
- Utilities (100+ display, spacing, typography, animation, responsive classes)

### 📋 Documentation Completed

**Component Specifications**
- ✅ Button specifications (variants, sizes, states, accessibility)
- ✅ Form specifications (inputs, validation, accessibility)
- ✅ Data display specifications (tables, pagination, badges, alerts, modals)
- ✅ Icon & Motion specifications (sizing, colors, animations, accessibility)

**Variant System & Architecture**
- ✅ Documented three-tier variant system
- ✅ Created composition matrix
- ✅ Established naming conventions
- ✅ Layer system: tokens + building blocks (no patterns)

**Real-World Examples**
- ✅ Plain HTML setup
- ✅ Next.js integration
- ✅ Vue 3 setup
- ✅ Svelte setup
- ✅ React setup
- ✅ Static site generators
- ✅ Monorepo patterns
- ✅ Best practices & troubleshooting

**Testing & Quality Strategy**
- ✅ Visual regression testing approach
- ✅ Accessibility audit strategy (WCAG AA)
- ✅ Performance testing targets
- ✅ Browser compatibility matrix

### 🔲 Upcoming Work

**Documentation Enhancements**
- [ ] Extend component specifications (all building blocks)
- [ ] Add icon system documentation
- [ ] Enhance color system guide
- [ ] Expand typography system guide
- [ ] Accessibility deep-dive (keyboard navigation, ARIA patterns, WCAG AA testing)

**Real-World Integration**
- [ ] Validate in Next.js project
- [ ] Validate in Vue 3 project
- [ ] Validate in React project
- [ ] Validate in Svelte project
- [ ] Performance profiling (CSS coverage, paint times)
- [ ] Browser compatibility testing (Chrome, Firefox, Safari, Edge)
- [ ] Screen reader testing (NVDA, VoiceOver)
- [ ] Interactive component testing (date picker, file upload, stepper)

**Release & Distribution**
- [ ] Version numbering (v1.2.0+)
- [ ] CHANGELOG.md
- [ ] Release notes
- [ ] Contributing guidelines (CONTRIBUTING.md)
- [ ] npm package publishing
- [ ] CDN hosting

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
│   ├── styleguide.html         (Unified interactive styleguide)
│   ├── styleguide-chrome.css   (Styleguide styling)
│   ├── STYLEGUIDE-MAINTENANCE.md (Update guidelines)
│   ├── tokens/
│   │   ├── tokens-web.css      (Semantic color, typography, spacing tokens)
│   │   └── tokens-app.css      (App-specific tokens)
│   ├── components/
│   │   ├── components-web.css  (Canonical component CSS)
│   │   └── components-app.css  (App component CSS)
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
│   │   └── more specifications
│   └── decisions/
│       ├── 2026-06-04-rammeverk-fokus-byggesteiner.md
│       ├── 2026-05-30-comprehensive-component-library.md
│       ├── 2026-05-30-variant-system.md
│       └── 2026-05-30-testing-strategy.md
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

**Last updated:** 2026-06-04  
**Status:** Nordover v1.2.0 — Building blocks + tokens foundation, full documentation, no patterns (per ADR 2026-06-04)
