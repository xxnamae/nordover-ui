# Patterns basis — batch 2 + tokens-iter-3 refinements

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter mottak av visuelle referanser fra Stacked.com og Linear.app (begge brukt av mange SaaS-team som benchmark for moderne app-design), identifiserte vi:
(a) tokens-app dark mode skal være pure neutral black (ikke blå-tintet);
(b) status/priority-farge-tokens mangler;
(c) chart-color-palett for analytics mangler;
(d) 10 konvensjonelle patterns vi ikke har spec'et ennå.

Dette er **iter-3** av tokens (etter farge-modernisering og tactile-buttons) + en ny batch patterns.

**Husk: to parallelle rammeverk:**
- **tokens-web** for alle nettsider (marketing, landingssider, redaksjonelt)
- **tokens-app** for alle apper/webapplikasjoner (SaaS, dashboards, interne verktøy)

Begge skal være komplette og selvstendige rammeverk.

---

## 1. tokens-app dark mode: neutral pure-near-black

**Endret fra:** `--color-bg: #09090B` (blå-tintet) til `#0A0A0A` (neutral).
**Endret:** subtle (#131316 → #141414), border (#27272A → #1F1F1F), muted (#8A8F98 → #7C7C7C).

**Hvorfor:** Stacked og Linear bruker begge essentielt pure black. Blå-tintet bg leser som "trying too hard for Linear-inspired". Pure neutral er mer tidløst.

---

## 2. Status-farger (tokens-app)

Lagt til:
- `--status-backlog: #7C7C7C` (gray)
- `--status-todo: #94A3B8` (slate)
- `--status-in-progress: #F59E0B` (amber)
- `--status-in-review: #6366F1` (indigo)
- `--status-done: #22C55E` (green)
- `--status-canceled: #525252` (dim gray)
- `--status-blocked: #EF4444` (red)

Disse brukes av `StatusIndicator`-komponenten. Linear-mapping.

---

## 3. Priority-farger (tokens-app)

Lagt til:
- `--priority-urgent: #DC2626`
- `--priority-high: #F59E0B`
- `--priority-medium: #94A3B8`
- `--priority-low: #525252`
- `--priority-none: #404040`

Brukes av `PriorityIndicator`-komponenten.

---

## 4. Chart-color palett (begge pakker)

8 distinkte farger for data-viz, navngitt 1-8 (ikke semantisk). OKLCH-source for konsistent kontrast i begge themes.

**Hvorfor 1-8 (numerisk) ikke semantisk:** charts brukes til vilkårlige kategorier (Subs/PPV/Tips/Posts/Messages/Product/Referral i Stacked sitt tilfelle) — semantiske navn ville ikke matche use-case. Konsumenten map'er sin egen data til chart-1/chart-2/etc.

**Hvorfor i begge pakker:** marketing-sider har også stats-strips og data-viz (eks. hero med revenue-eksempel). Web-versjonen er litt dimmer/mindre saturert (passer Scandi-min editorial), app-versjonen er brighter (synlighet i dashboard).

---

## 5. Nav-item-tokens (tokens-app)

Lagt til:
- `--nav-item-bg-hover: color-mix(in oklch, var(--color-fg) 6%, transparent)`
- `--nav-item-bg-active: color-mix(in oklch, var(--color-fg) 10%, transparent)`
- `--nav-item-radius: var(--radius-md)`

Forberedelse for sidebar-nav-komponenten (batch 2 / mode A).

---

## 6. Refinements (A1-A5 + B6-B7 fra tidligere forslag)

Lagt til i begge pakker:

- `--focus-ring`: composite box-shadow string for `:focus-visible` (smoother enn outline)
- `--font-tabular`: monospace stack for tall (alternativ til sans der tabular-nums brukes)
- `--button-glow`: subtle radial glow rundt primary CTA (særlig synlig i dark mode på tokens-app)
- `--ease-spring`: `cubic-bezier(0.2, 0.8, 0.2, 1)` — litt "bouncy" feel for små interaksjoner
- `--ease-emphasized`: `cubic-bezier(0.3, 0, 0, 1)` — bestemt easing for hovedanimasjoner
- `::selection`-styling via `color-mix` på accent-color
- Scrollbar (webkit + firefox) — tynn, transparent track, border-tinted thumb
- `@media (prefers-color-scheme: dark)`-respekt når ingen eksplisitt `[data-theme]` settes

---

## 7. Nye patterns spec'et (batch 1b extended til 10 stk)

| Pattern | Web | App | Kompleksitet |
|---|---|---|---|
| Stats Card | ✓ (marketing stats-strip) | ✓ (analytics) | Lav |
| Avatar Pill | (sjelden) | ✓ (assignees, members) | Lav |
| Empty State | ✓ | ✓ | Lav |
| Section Header | (sjelden) | ✓ (sidebar) | Trivielt |
| Status Indicator | (sjelden) | ✓ (issue-lister, kanban) | Lav |
| Priority Indicator | (sjelden) | ✓ (issue-lister) | Lav |
| Star Toggle | (sjelden) | ✓ (favorites) | Trivielt |
| CTA Pair | ✓ (hero) | (sjelden) | Trivielt (komposisjon) |
| Counter Nav | (sjelden) | ✓ (record-paginering) | Lav |
| Selection Group | (sjelden) | ✓ (chart-legend) | Lav |

Web-spesifikke patterns (hero, FAQ, creator grid) kommer i fase 3 (section-patterns).

---

## Hva som fortsatt ikke er drodlet

Disse krever proper sparring (batch 2 / mode A):

- **Sidebar / Nav** — multi-level, sections, collapsible, sub-items, controlled state
- **Activity Stream** — Linear-pattern (avatar + name + action + timestamp)
- **Side-panel** — slides in fra høyre, fokus-trap, dismiss-handling
- **Kanban Board** — column-layout, drag/drop, scroll
- **Data Table** — sortable, selectable, hover-rows, edit-actions
- **Charts / Visualization** — krever library-valg (Recharts? Visx? Native SVG?)

---

**Konsekvenser samlet:**
- Token-overflate vokser betydelig (status, priority, chart, refinement). Akseptert som pris for å støtte real-world SaaS-bruk.
- `tokens-app` har nå nok overflate til å bygge en Linear/Stacked-aktig app uten å patche fundamentet.
- `tokens-web` har samme chart + refinement tokens — kan håndtere marketing-sider med stats og data-viz.
- 18 av 60+ patterns nå drodlet (10 batch 1 + 10 batch 1b/2).

**Reverseringskostnad:** Lav. Token-tillegg er additive. Pattern-additions kan fjernes uten breaking changes.
