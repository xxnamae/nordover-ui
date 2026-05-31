# CLAUDE.md — `xxnamae/nordover-ui`

This repository contains the **shippable framework specification** for the Nordover design system. It is public and MIT-licensed. Strategy notes, research, and session logs remain in a separate private repository.

## Four Foundational Principles

1. **Think first** — surface tradeoffs explicitly; decisions are traceable in `docs/wiki/decisions/`
2. **Simplicity first** — minimal code, fewer tokens, fewer abstractions
3. **Surgical changes** — modify only what the issue/PR addresses; avoid cleanup
4. **Stable API** — token names are contracts; breaking changes require ADR + clear changelog

## What Belongs Here

Framework content for public consumption:
- Consumption guides for implementers (`docs/handoff/`)
- Canonical shippable CSS (`docs/visual/tokens/*.css` + `docs/visual/components/*.css`)
- Rendered reference styleguides
- Component family specifications (`docs/wiki/topics/nordover-*.md`)
- Architecture Decision Records (`docs/wiki/decisions/`)
- Framework glossary
- Public-facing docs (LICENSE, README.md)

## What Doesn't Belong Here

Keep in the private `xxnamae/notater` repository:
- Session logs and development notes
- Research materials and explorations
- Customer-specific strategy documents
- Owner prompts for onboarding other agents

## Change Rules

- **Tokens are contracts**: CSS variable names are public contracts; renaming breaks downstream compatibility
- **Published ADRs are immutable**: Record reversals in new ADRs rather than editing old ones
- **WCAG compliance required**: Color token changes must maintain WCAG AA contrast standards
- **Language**: Norwegian Bokmål for wiki/decisions; English for code comments
- **Mirroring**: Changes to token values must be applied to both `tokens-web.css` and `tokens-app.css` in the same commit. The same applies to shared component structure across `components-web.css` and `components-app.css`
- **Component classes are contracts**: Class names in `components-*.css` are public contracts (like token names). They live there as the single source of truth — never re-embed component CSS inside styleguide HTML; the styleguides must link the shippable files
- **Styleguides are authoritative**: Styleguides must always reflect 100% of components in framework. If a component exists in CSS but not in styleguide, it doesn't exist for users. See `docs/visual/STYLEGUIDE-MAINTENANCE.md`
- **Styleguide workflow is mandatory**: Framework changes and styleguide updates must occur in the same commit. No CSS commit without corresponding styleguide documentation. Follow `docs/visual/STYLEGUIDE-WORKFLOW.md`
