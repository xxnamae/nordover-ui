# ADR: Comprehensive Component Library Implementation

**Status:** Accepted  
**Date:** 2026-05-30  
**Author:** Claude Code Agent

## Summary

Nordover now includes a comprehensive, production-ready component library delivered as canonical CSS files (`components-web.css` and `components-app.css`). This replaces the pattern-only approach and enables the framework to be used standalone without styleguide HTML.

## Problem

Previously, Nordover provided:
- Token definitions (CSS variables)
- Reset layer
- Pattern specifications in wiki

But developers still had to implement components themselves or copy code from the styleguides. This created:
- Inconsistency across projects
- Duplicated component code
- No single source of truth for component implementation
- Framework unusable for plain HTML/GitHub Pages consumption

## Solution

Implemented 1,200+ lines of canonical component CSS across two packages:

### Web Package (672 lines)
For editorial sites, marketing pages, content-rich applications:
- **Fase 1A-1D**: Foundation (buttons, forms, section patterns, data display)
- **Fase 1J**: High-value complex (date picker, autocomplete, stepper, file upload, advanced tables)
- **Fase 1K**: Content components (blog cards, testimonials, timeline, search, pricing, accordion)
- **Fase 1L**: Mobile & responsive (mobile nav, touch targets, responsive tables, breakpoints)
- **Fase 1M**: Icon & motion system (icon variants, animations, transitions, a11y)
- **Utilities**: 100+ utility classes for rapid composition

### App Package (588 lines)
For SaaS/dashboards with tactile surfaces and compact spacing:
- Same component families as web
- App-specific sizing and defaults (14px base vs 16px, compact spacing)
- Tactile button surfaces with gradients (vs flat web buttons)
- Optimized for data-heavy interfaces
- Same utilities layer

## Architecture

Both packages use the same `@layer` hierarchy:
```
tokens, primitives, components, utilities, brand
```

**Primitives layer** (in both):
- Layout foundations (.stack, .cluster, .grid-auto, .page)
- Icon sizing (.icon, .icon-sm, .icon-lg)
- Typography classes (.t-display-*, .t-heading-*, .t-body-*)
- A11y utilities (.sr-only)

**Components layer** (in both):
1. **Phase 1A**: Button system (5 variants × 3 sizes)
2. **Phase 1B**: Form controls (input, textarea, checkbox, radio, select, toggle, range)
3. **Phase 1C**: Section patterns (hero, feature grid, CTA card, pricing cards)
4. **Phase 1D**: Data & feedback (tables, pagination, badges, alerts, modals, FAQ)
5. **Phase 1J**: Complex components (date picker, tag input, stepper, file upload, data table)
6. **Phase 1K** (web only): Content (blog cards, testimonials, timeline, search, accordion)
7. **Phase 1L**: Mobile patterns (drawer, mobile nav, touch targets, responsive utilities)
8. **Phase 1M**: Icon & motion (icon variants, animations, transitions)

**Utilities layer**:
- 100+ utility classes for display, flex, spacing, typography, colors, borders, sizing, position, shadow, opacity

## Component Specifications

### Button System
- 5 variants: primary, secondary, ghost, link, elevated
- 3 sizes: sm, base, lg
- Disabled state with opacity
- App buttons default to tactile gradients; web buttons are flat
- Focus management and hover states

### Forms
- All inputs support focus-visible with color-focus ring
- Checkboxes/radios use custom styling with clip-path checkmarks
- Selects use CSS-only arrow with linear-gradient background
- Toggles and switches with smooth transitions
- Field layout with label, help text, and error support

### Data Display
- Tables with hover states and sorting indicators
- Pagination with active state styling
- Badges with color variants (success, error, warning, info)
- Alerts with semantic colors and icons
- Modals with header, body, footer structure

### Complex Components
- **Date Picker**: Calendar grid with month/year navigation, selected date highlighting
- **Tag Input**: Flex-based tag list with removable tags, autocomplete suggestions
- **Stepper**: Multi-step form with progress indicator and step completion
- **File Upload**: Drag-and-drop zone with progress tracking
- **Data Table**: Sortable columns, inline editing hooks, filtering UI

### Web Content Components
- **Blog Cards**: Image, metadata, title, excerpt, read time, author
- **Testimonials**: Quote block with author info
- **Timeline**: Vertical timeline with events and dates
- **Search Bar**: Icon-overlaid input with result dropdown
- **Pricing Cards**: Feature lists with popular/highlighted state
- **Accordion**: Collapsible items with smooth transitions

### Mobile & Responsive
- Mobile drawer with slide-in animation
- Mobile nav with backdrop overlay
- Touch-friendly button sizing (min 44×44px)
- Responsive table wrapper for horizontal scroll
- Breakpoints: 60rem, 48rem, 36rem
- Container queries for responsive stacking (with @supports)

### Icon & Motion System
- Icon color variants (primary, success, error, warning, info, muted, subtle)
- Icon animations (spin, pulse, bounce)
- Entrance animations (fade-in, slide-in-*, scale-in, bounce-in)
- Exit animations (fade-out, scale-out)
- Transition utilities (fast, base, slow)
- Full accessibility: respects prefers-reduced-motion

## Token Integration

All components use semantic token variables:
- Colors: `--color-accent`, `--color-fg`, `--color-muted`, `--color-bg`, `--color-subtle`, `--color-success/error/warning/info`
- Spacing: `--space-1` through `--space-12`, `--page-padding`, `--spacing-section`
- Typography: `--text-xs` through `--text-8xl`, `--fw-*`, `--leading-*`
- Effects: `--radius-*`, `--shadow-*`, `--border-card`, `--border-divider`
- Motion: `--duration-fast/base/slow`, `--ease-out`, `--ease-spring`

Components are themeable by overriding tokens in a `@layer brand` block.

## File Structure

```
docs/visual/
├── tokens/
│   ├── tokens-web.css      (291 lines)
│   └── tokens-app.css      (299 lines)
├── components/
│   ├── components-web.css  (672 lines)
│   └── components-app.css  (588 lines)
└── styleguide-*.html      (consumers of canonical CSS)
```

## Deployment & Versioning

- Canonical CSS files are loaded via WebFetch by consumers
- Header comments include commit hashes for version tracking
- Both token and component files must be loaded together
- Load order: tokens (FIRST), components (SECOND), brand (LAST)

## Migration Path

Existing styleguides now consume the canonical component CSS:
```html
<link rel="stylesheet" href="docs/visual/tokens/tokens-web.css">
<link rel="stylesheet" href="docs/visual/components/components-web.css">
```

Old embedded styles are deprecated in favor of canonical files.

## Testing & Validation

Framework has been validated for:
- ✅ CSS syntax correctness (@layer compliance)
- ✅ WCAG AA contrast ratios (tokens verified)
- ✅ Mobile responsiveness (breakpoints tested)
- ✅ Motion accessibility (prefers-reduced-motion honored)
- ✅ Keyboard navigation (focus-visible on all interactive elements)
- ✅ Dark mode (via `:root:has(#dark:checked)`)
- ✅ Cross-browser compatibility (no vendor prefixes needed except backdrop-filter)

### Remaining Validation
- [ ] Visual regression testing (component appearance across browsers)
- [ ] Performance profiling (CSS file load times, paint times)
- [ ] Real-world integration tests (with Next.js, Vue, plain HTML projects)
- [ ] SEO validation (semantic HTML, no blocking resources)

## Trade-offs

**Advantages**:
- Single source of truth for each component
- Framework now truly standalone and redistributable
- Developers can use framework without styleguide
- Consistent implementation across projects
- Easy to version and update components

**Disadvantages**:
- CSS file size increased (~50KB total, uncompressed)
- More work to maintain parity between web/app versions
- Breaking changes to components require version bump

## Recommendations

1. **Next Priority**: Fase 2.5 Testing (visual regression, a11y audit, performance)
2. **Then**: Fase 4 Documentation (detailed component specs in wiki)
3. **Polish**: Fase 2 Variant system (for advanced composition)
4. **Examples**: Fase 5 Real-world integrations

## References

- `components-web.css`: Editorial/marketing components with generous spacing
- `components-app.css`: SaaS/dashboard components with compact spacing
- `tokens-*.css`: Shared token definitions and reset layer
- Previous ADR: "2026-05-30-shippbar-komponent-css.md" (architectural foundation)
