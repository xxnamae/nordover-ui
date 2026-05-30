# ADR 0009: Token Divergence — Web vs App by Design

**Date:** 2026-05-30  
**Status:** Accepted  
**Author:** Nordover Design System  
**Deciders:** Design System Core Team

## Context

The Nordover framework maintains two parallel token files:
- `tokens-web.css` — for editorial sites, marketing pages, long-form content
- `tokens-app.css` — for SaaS dashboards, data-dense applications

Token analysis reveals intentional divergence:

### Web Tokens (Editorial Context)
- **Typography scale:** 8 sizes (xs, sm, base, lg, xl, 2xl, 3xl, **6xl, 7xl, 8xl**)
- **Heading weights:** 6 weights (body-sm, caption, eyebrow, heading-sm, heading-md, heading-lg, **display-md, display-lg, display-xl**)
- **Fluid typography:** Clamp-based scaling from 14px to 160px+ for large displays
- **Gradient:** `--gradient-radial-accent` for hero/CTA sections

### App Tokens (Compact Context)
- **Typography scale:** 6 sizes (xs, sm, base, lg, xl, **5xl max**)
- **Heading weights:** 4 base weights (body-sm, caption, eyebrow, heading-sm/md/lg, display-md, display-lg)
- **Static typography:** Fixed pixel sizing optimized for 14px–22px body text
- **No radial gradient:** Accent colors via solid backgrounds

### Token Delta
Web has 16+ tokens that app does not:
- `--text-6xl`, `--text-7xl`, `--text-8xl` (large headline scale)
- `--fw-display-xl`, `--fw-display-lg` (editorial headline weights)
- `--gradient-radial-accent` (decorative gradient for web sections)
- Additional semantic spacing/shadow variants tuned for editorial layouts

## Decision

**Token divergence is intentional and will not be unified.**

Each platform defines its own canonical token set aligned with its use case:

1. **Web tokens** optimize for **editorial typography** (fluid scale, generous spacing, 6+ heading weights)
2. **App tokens** optimize for **data-dense dashboards** (compact, fixed sizing, 4 base weights)
3. **Framework CI does NOT synchronize tokens** between `tokens-web.css` and `tokens-app.css`
4. **Component CSS remains parallel:** Both `components-web.css` and `components-app.css` inherit their respective tokens
5. **No shared token layer:** Web and app are separate APIs with separate contracts

## Rationale

### Why Separate Tokens?
1. **Conflicting design philosophies:**
   - Web: Generous whitespace, fluid typography, long-form reading
   - App: Compact UI, dense information density, quick scanning
   
2. **Forcing unification breaks both:**
   - Cramming web's `--text-8xl` into an app context wastes space
   - Constraining app's compact scale to web creates undersized headlines
   - Single token set becomes a lowest-common-denominator compromise
   
3. **Scale inflation in apps:**
   - Editorial 24px body text → App 16px required for data tables
   - Editorial 160px hero headline → App 48px max for dashboard titles
   - Web's fluid clamp() scales → App's fixed pixels required for UI stability

4. **Type families differ:**
   - Web: Large display weights (380 fw–600 fw across 6 display variants)
   - App: Pragmatic 4-weight system (medium, semibold, bold focus)
   - Web uses `--fw-display-*`, app uses `--fw-heading-*`

### Maintainability
Single unified token set creates false coupling:
- Change for web alignment breaks app dashboards
- Change for app compactness breaks web readability
- Every token review becomes a tradeoff negotiation

Separate sets allow independent iteration. Each team owns its contracts.

## Consequences

### Positive
- Each platform can evolve typographically without sync friction
- Integrators building in one context aren't confused by the other's tokens
- CI/CD is simpler (no token sync logic needed)
- Component CSS inheritance is predictable (web components use web tokens, app components use app tokens)

### Negative
- Integrators building a **blog in the app package** must define their own heading tokens
  - *Mitigation:* Provide token override guide in ADR 0010 (future)
- **Token naming** requires discipline: prefix by context if ever shared (future-proofing)
- No single "source of truth" for typography across frameworks
  - *Mitigation:* Document design decisions separately for web and app contexts

### Migration Risk
- If future product unifies web + app into single codebase, separate tokens can be manually merged
- No breaking change to consuming code—only token redefining in CSS layer

## Alternatives Considered

### 1. "Sync All Tokens in CI"
**Rejected.** Would force:
- Web headlines into app (too large, breaks layouts)
- App compactness into web (undersized, reduces readability)
- Lowest-common-denominator compromise on both sides

### 2. "One Token, Two Contexts via @media"
**Rejected.** Scalable only if viewport-driven. App dashboards don't resize typography based on screen width—they have fixed design targets. Would pollute token definitions with conditional logic.

### 3. "Parent Tokens + Token Aliases"
**Rejected.** Adds indirection complexity. Better to define directly and document clearly than to abstract.

## Compliance

- **CLAUDE.md Section: "Mirroring"** — Tokens *are* mirrored within the same file (`tokens-web.css` ↔ `tokens-web.css`), but NOT across files. Token mirroring applies to components only (see `components-web.css` ↔ `components-app.css` structure).
- **CLAUDE.md Section: "Tokens are Contracts"** — Token names in each file are immutable contracts. Renaming breaks downstream compatibility *within that file's ecosystem*.
- **WCAG Compliance:** Token values (colors, sizing) must still be WCAG AA within their respective contexts.

## Related ADRs
- ADR 0001: Foundational principles  
- ADR 0003: CSS @layer architecture  
- ADR 0006: Component family specs  
- ADR 0010 (future): Token override guide for integrators

## Questions & FAQ

**Q: Can I use web tokens in an app?**  
A: No. Use the `tokens-app.css` import for your app. If you need web typography in a dashboard, define override tokens in your `@layer brand` block.

**Q: If I only need app tokens, do I import both files?**  
A: No. Import only the tokens file matching your context (`tokens-app.css` for apps, `tokens-web.css` for web).

**Q: Will tokens ever reunify?**  
A: Only if the product architecture converges. Separate tokens can be manually merged later without breaking public contracts—they're just CSS variable definitions.
