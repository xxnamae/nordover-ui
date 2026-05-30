# Nordover-rammeverk

Oversikt over alle komponentfamilier i Nordover-stacken. Hver familie får egen wiki-side når den er drodlet. Status oppdateres etter hver økt.

## Familier

| Familie | Wiki-side | Status |
|---|---|---|
| Tokens (web + app) | [nordover-arkitektur.md](nordover-arkitektur.md#tokens-arkitektur) | Drodlet 2026-05-27 |
| Typografi-utilities | [nordover-typografi.md](nordover-typografi.md) | Drodlet 2026-05-27 |
| Layout-primitiver (Container, Section, Stack, Grid, Cluster) | [nordover-layout.md](nordover-layout.md) | Drodlet 2026-05-27 |
| Elevation / shadows / borders / hover-lift | [nordover-elevation.md](nordover-elevation.md) | Drodlet 2026-05-27 |
| Buttons + interactive states | [nordover-buttons.md](nordover-buttons.md) | Drodlet 2026-05-27 |
| Form-elementer | [nordover-forms.md](nordover-forms.md) | Drodlet 2026-05-27 |

## Composite components / patterns

Bygger på primitivene over.

### Batch 1 — basis (drodlet 2026-05-27)

Se [nordover-patterns-basis.md](nordover-patterns-basis.md).

| Pattern | Status |
|---|---|
| Tag | Drodlet ✓ |
| Badge | Drodlet ✓ |
| Avatar | Drodlet ✓ |
| Spinner | Drodlet ✓ |
| Tooltip (basis, ren CSS) | Drodlet ✓ |
| Breadcrumbs | Drodlet ✓ |
| Pagination | Drodlet ✓ |
| Skeleton-loader | Drodlet ✓ |
| Divider | Drodlet ✓ |
| Kbd | Drodlet ✓ |

### Batch 1b — basis fortsatt (drodlet 2026-05-27)

Se [nordover-patterns-basis-2.md](nordover-patterns-basis-2.md).

| Pattern | Status |
|---|---|
| Stats Card | Drodlet ✓ |
| Avatar Pill | Drodlet ✓ |
| Empty State | Drodlet ✓ |
| Section Header | Drodlet ✓ |
| Status Indicator | Drodlet ✓ |
| Priority Indicator | Drodlet ✓ |
| Star Toggle | Drodlet ✓ |
| CTA Pair (Hero) | Drodlet ✓ |
| Counter Nav | Drodlet ✓ |
| Selection Group | Drodlet ✓ |

### Fase 2B — Web-rammeverk: section-patterns (drodlet 2026-05-27)

Se [nordover-section-patterns.md](nordover-section-patterns.md). For komplette landingsside-leveranser.

| Pattern | Status |
|---|---|
| Hero — Centered | Drodlet ✓ |
| Hero — Split (display + media) | Drodlet ✓ |
| Hero — Editorial (asymmetrisk) | Drodlet ✓ |
| Feature Grid | Drodlet ✓ |
| CTA Section | Drodlet ✓ |
| FAQ (native details/summary) | Drodlet ✓ |
| Site Header (sticky glass + mobile overlay) | Drodlet ✓ |
| Logo Cloud | Drodlet ✓ |
| Pricing (3-tier med highlight) | Drodlet ✓ |
| Stats-strip | Drodlet ✓ |
| Site Footer (1 brand + 3 link columns) | Drodlet ✓ |

### Fase 2A — App-rammeverk: arkitektur-tunge patterns (drodlet 2026-05-27)

Se [nordover-app-patterns.md](nordover-app-patterns.md). Bygger på Radix Primitives + TanStack + cmdk + dnd-kit som headless underlying.

| Pattern | Underliggende | Status |
|---|---|---|
| Card (4 varianter) | custom | Drodlet ✓ |
| Modal / Dialog | Radix Dialog | Drodlet ✓ |
| Drawer | Radix Dialog | Drodlet ✓ |
| Side-panel (inline, ikke overlay) | custom | Drodlet ✓ |
| Toast / Alert | Radix Toast | Drodlet ✓ |
| Sidebar Nav | custom | Drodlet ✓ |
| Tabs | Radix Tabs | Drodlet ✓ |
| Accordion (animated) | Radix Accordion | Drodlet ✓ |
| Menu / Dropdown | Radix DropdownMenu | Drodlet ✓ |
| Command Palette (⌘K) | cmdk | Drodlet ✓ |
| Data Table | TanStack Table | Drodlet ✓ |
| Activity Stream | custom | Drodlet ✓ |
| Kanban Board | @dnd-kit | Drodlet ✓ |

### Senere — utvidelser (drodlet 2026-05-27)

Se [nordover-patterns-utvidelser.md](nordover-patterns-utvidelser.md).

| Pattern | Underliggende | Status |
|---|---|---|
| Testimonial — Card | custom | Drodlet ✓ |
| Testimonial — Large Quote | custom | Drodlet ✓ |
| Testimonial — Video | custom + lightbox-modal | Drodlet ✓ |
| Newsletter Signup | Form + Button comp | Drodlet ✓ |
| Hero med video | IntersectionObserver | Drodlet ✓ |
| Mega-menu | Radix NavigationMenu | Drodlet ✓ |
| Chart-wrappers (Line/Bar/Area/Stacked/Pie/Donut) | Recharts | Drodlet ✓ |
| Empty State med illustrasjoner (8 SVG-er) | custom | Drodlet ✓ |

### Tidligere parkerte — nå drodlet (2026-05-27)

Se [nordover-patterns-parkerte.md](nordover-patterns-parkerte.md).

| Pattern | Underliggende | Status |
|---|---|---|
| Multi-step Wizard | custom | Drodlet ✓ |
| Inline Edit | custom | Drodlet ✓ |
| Filter Bar | Radix DropdownMenu + Tag | Drodlet ✓ |
| Notification Feed | custom | Drodlet ✓ |

### Patterns-utvidelser batch 2 (drodlet 2026-05-27)

Etter Linear/Stacked/Off Menu-referanser. Se [nordover-patterns-utvidelser-2.md](nordover-patterns-utvidelser-2.md).

| Pattern | Underliggende | Status |
|---|---|---|
| Site Header — Stacked-stil | custom | Drodlet ✓ |
| Site Header — Linear-stil | custom | Drodlet ✓ |
| Site Header — Off Menu-stil | custom | Drodlet ✓ |
| Footer — Linear-stil (5 cols) | custom | Drodlet ✓ |
| Footer — Minimal (1 rad) | custom | Drodlet ✓ |
| AI Assistant Panel | Radix Dialog | Drodlet ✓ |
| Onboarding Flow (Wizard-variant) | custom | Drodlet ✓ |
| Numerated Service List | custom | Drodlet ✓ |
| Sticky Sub-nav | Intersection Observer | Drodlet ✓ |
| Feature Row | custom | Drodlet ✓ |

**Filosofi:** Vi har bevisst valgt å stoppe ved fundament + primitiver i denne omgangen. Composite components krever ofte tredjeparts-libraries (Radix UI for focus-trap, Floating UI for popover-positionering) eller egne arkitekturvalg som ikke kan forhåndsbestemmes på samme måte som tokens.

**Hvordan komme videre:** Hver pattern får egen drodlings-økt, samme rytme som tokens/buttons/forms-øktene. Prioriter etter konkrete behov i Nordover-prosjekter — ikke alle patterns trenger å eksistere før første leveranse.

## Felles prinsipper

Disse vokser etter hvert som vi drodler hver familie. Foreløpig:

- **Token-først.** Alle komponenter bruker semantiske tokens fra `tokens-web` eller `tokens-app`. Ingen hardkodede verdier.
- **Token-agnostiske komponenter.** Komponenter bruker token-navn som finnes i **begge** pakker (`--color-fg`, `--color-bg`, `--spacing-section`). Samme `<Button>` skal fungere både i marketing og SaaS.
- **Brand-overstyring per kunde** skjer kun via `clients/<slug>.css`, aldri i komponentene.
- **A11y er ikke valgfritt.** Focus-states, `prefers-reduced-motion`, semantiske HTML-tagger fra dag én.
- **Dempbarhet.** Hvis komponenter er tunet for skandinavisk minimalisme, må de kunne dempes via brand-tokens uten å patche kildekoden.

## Arbeidsflyt per familie

Hver drodlings-økt for en familie følger samme rytme:

1. Identifiser de reelle spennene (ikke hvilken syntaks, men hvilke arkitekturvalg).
2. Surface 2-3 alternativer per spenn med tradeoffs.
3. Bestem og dokumenter i en eller flere decision-filer.
4. Skriv konkret spec inn i familiens wiki-side.
5. Oppdater denne indeksen + `log.md`. Commit + push.

## Hva som IKKE havner her

- Faktisk implementasjons-kode (det hører hjemme i `xxnamae/nordover`).
- Kunde-spesifikke brand-overstyringer (de hører hjemme i hver kundes repo).
- Endelige CSS-filer klare til import (her er det spec, ikke artefakt).

## Se også

- [Nordover-arkitektur — tokens](nordover-arkitektur.md)
- [Decisions-mappe](../decisions/)
