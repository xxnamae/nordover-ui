# CLAUDE.md — `xxnamae/nordover-ui`

This repository contains the **shippable framework specification** for the Nordover design system. It is public and MIT-licensed. Strategy notes, research, and session logs remain in a separate private repository.

## Vision

Nordover is a **universal foundation of building blocks of global top quality** — tokens and reusable primitives that every application and website builds on. The goal is to **minimize design time on new projects** by providing the structural, accessibility, and responsive foundation, so each project composes its own pages on top rather than reinventing the base. Nordover ships **tokens** and **building blocks** (button, form elements, card shell, badge, alert, table base, layout primitives, navigation, modal, accordion, tabs, etc.) — it deliberately does **not** ship finished page compositions (hero, pricing, blog, testimonials, dashboards); those are per-project design decisions. See `docs/wiki/decisions/2026-06-04-rammeverk-fokus-byggesteiner.md`.

- **Market:** all-purpose (SaaS, editorial/marketing, e-commerce, consumer apps)
- **Platform:** multi-platform (web-first, mappable to native iOS/Android and desktop)
- **Aesthetic:** modern/minimal, grounded in **Nordic minimalism**, with **Apple HIG** as interaction inspiration and **Linear** as SaaS-density reference
- **Benchmarks:** must withstand comparison with Apple HIG, Material Design 3, Linear, Fluent
- **Breakpoints (official QA):** Mobile <480px · Tablet 768–1024px · Desktop >1024px — every component evaluated on all three

Full vision: `docs/wiki/topics/nordover-visjon.md`. All design decisions trace back to this vision.

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
- **Language**: Norwegian Bokmål for wiki/decisions, user communication, and agent sessions; English for code comments and CSS
- **Claude communication**: Claude agent communicates in Norwegian Bokmål (Norsk bokmål) with the user unless explicitly directed otherwise
- **Model suggestions**: Claude foreslår proaktivt hvilken modell (og effort-nivå) som passer for kommende oppgaver — f.eks. lettere modell for mekaniske/avgrensede endringer, sterkere modell + høyere effort for arkitektur, kontrast/tilgjengelighet, kryssfil-konsistens og visuelle beslutninger
- **Mirroring**: Changes to token values must be applied to both `tokens-web.css` and `tokens-app.css` in the same commit. The same applies to shared component structure across `components-web.css` and `components-app.css`
- **Token JSON is generated**: `tokens-*.json` are derived DTCG artifacts built from the CSS by `scripts/build_tokens.py` (CSS is the single source of truth — never hand-edit JSON). Any token value change must regenerate JSON in the same commit (`npm run build:tokens`); CI enforces sync via `npm run check:tokens`. See `docs/wiki/decisions/2026-06-01-json-token-eksport-dtcg.md`
- **Component classes are contracts**: Class names in `components-*.css` are public contracts (like token names). They live there as the single source of truth — never re-embed component CSS inside styleguide HTML; the styleguides must link the shippable files
- **Naming convention (v2.0)**: One consistent system, per `docs/wiki/decisions/2026-06-05-unifisert-navnekonvensjon.md`. (a) **States use `.is-*`** (`.is-active`, `.is-open`, `.is-selected`, `.is-error`, …) — decoupled from the component name. (b) **One `.table` system** with opt-in modifiers (`.table-sticky/-zebra/-numeric/-responsive/-inline-edit/-filter`); sort state via `[aria-sort]`, never a `.sort-*` class. (c) **One status vocabulary everywhere**: `success / warning / error / info` (a destructive button is `.btn-error`). (d) Sizes: `-xs / -sm / (default) / -lg / -xl`. (e) `.t-*` is the semantic-typography namespace; `.text-*` is utilities. New classes must follow these patterns and exist in both packages.
- **No styleguide chrome in shippable CSS**: `components-*.css` must contain only framework building blocks. Styleguide-only classes (`.doc-*`, `.swatch*`, `.chip*`, `.props-table`, doc-pattern blocks) live in `docs/visual/styleguide-chrome.css`.
- **Styleguides are authoritative**: Styleguides must always reflect 100% of components in framework. If a component exists in CSS but not in styleguide, it doesn't exist for users. See `docs/visual/STYLEGUIDE-MAINTENANCE.md`
- **Styleguide workflow is mandatory**: Framework changes and styleguide updates must occur in the same commit. No CSS commit without corresponding styleguide documentation. Follow `docs/visual/STYLEGUIDE-WORKFLOW.md`
- **Push to main always**: All completed work is pushed directly to `main`. The live GitHub Pages site at https://xxnamae.github.io/nordover-ui/docs/visual/styleguide.html is the single source of truth for reviewing the design system — this is the only place the owner inspects and evaluates the full styleguide.
