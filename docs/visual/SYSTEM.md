# Nordover Design System v3.0

**Versjon:** 3.0.0  
**Oppdatert:** 2026-06-12  
**Status:** Produksjon (begge pakker live: app + web)

---

## Systemets kjerne

Nordover er et **universelt rammeverk av designtokens og gjenbrukbare komponenter** for web- og app-grensesnitt. Målgruppe: SaaS-produkter, marketing-nettsted, editorske plattformer.

### Designfilosofi

1. **Tokens som kontrakter** — Navn er offentlig API; verdier kan variere (web/app)
2. **Klassemapping-konsistens** — Samme `.t-body-lg` bruker `--text-md` i begge pakker
3. **Maskin-generering** — Åpent for Token Studio, automatisert tema-generering
4. **Tilgjengelighet som gulv** — WCAG AA som minimum; ingen unntak

### To pakker, ett system

| Pakke | Formål | Typografi | Densitet | Accent |
|-------|--------|-----------|----------|--------|
| **app** | SaaS-dashboard | Fast (rem) | Kompakt (1rem gap) | Blå (brand) |
| **web** | Marketing, editorial | Fluid (clamp) | Luftig (1.5rem gap) | Nøytral (sort) |

**Invariant:** Klasse→token-mappinger identiske. Verdier kan være ulike.

---

## Typografi

### Semantic classes (`.t-*`)

**Display-familie** (Inter Tight, display-tekst)
- `.t-display-2xl` → `--text-6xl` (60px app, 65-80px web)
- `.t-display-xl` → `--text-5xl` (48px app, 50-64px web)
- `.t-display-lg` → `--text-4xl` (36px app, 40-56px web)
- `.t-display-md` → `--text-3xl` (30px app, 30-42px web)
- `.t-display-sm` → `--text-2xl` (24px app, 24-32px web)

**Heading-familie** (Inter Tight, section headers)
- `.t-heading-xl` → `--text-3xl` (30px app, 30-42px web)
- `.t-heading-lg` → `--text-2xl` (24px app, 24-32px web)
- `.t-heading-md` → `--text-xl` (20px app, 20-24px web)
- `.t-heading-sm` → `--text-lg` (18px app, 18-20px web)

**Body-familie** (Inter, content/UI)
- `.t-body-xl` → `--text-lg` (18px app, 18-20px web) — lead paragraph
- `.t-body-lg` → `--text-md` (16px app, 17-18px web) — prominent content
- `.t-body` → `--text-base` (14px app, 16px web) — default reading text
- `.t-body-sm` → `--text-sm` (13px app, 14px web) — secondary content

**UI-vekter** (app-only, Linear-inspirert)
- `--fw-ui: 510` — Standard UI (nav, labels, buttons)
- `--fw-ui-strong: 590` — Emphasized UI (active states, headers)

**Font features** (Inter Variable optimization)
- `tnum` — Tabular numbers (tabeller, badges, values)
- `ss01` — Stylistic set (open figures for disambiguation, if needed)

---

## Farger

### Grayscale (Kontrast-ankerpunkt)

```
--gray-50: L 0.985   (white fallback)
--gray-100: L 0.96   (very light)
--gray-200: L 0.92   (light)
--gray-300: L 0.865  (light-mid)
--gray-400: L 0.70   (medium, --color-muted)
--gray-500: L 0.52   (mid-dark)
--gray-900: L 0.13   (darkest, dark-mode base)
--gray-950: L 0.06   (pure dark fallback)
```

**Høykontrast-variant:** Justér gray-50 (whiter) og gray-900 (blacker) for ΔL ≥ 0.995.

### Semantiske farger

**Accent** (brand)
- App: oklch(0.50 0.22 260) — Brand blå
- Web: Gray-900 — Nøytral svart

**Status** (universal)
- `--success: oklch(0.64 0.16 150)` — Grønt
- `--error: oklch(0.62 0.22 25)` — Rødt
- `--warning: oklch(0.74 0.16 75)` — Gult
- `--info: oklch(0.62 0.19 250)` — Blått

**Tripletter** (subtle / base / strong)
- `--error-subtle: color-mix(--error 22%, --color-bg)` — background
- `--error: oklch(...)` — base, text
- `--error-strong: color-mix(--error 70%, white|black)` — emphasized

---

## Elevasjon (Surface-stepping)

**Light mode** (L-offsets fra bg 0.98)
```
--surface-1: 0.98 L  (= bg, base level)
--surface-2: 0.99 L  (subtle elevation)
--surface-3: 1.0 L   (elevated panel/card)
--surface-4: 0.99 L  (= surface-2)
--surface-5: 0.98 L  (= surface-1)
```

**Dark mode** (L-offsets fra bg 0.13)
```
--surface-1: 0.13 L  (= bg, base)
--surface-2: 0.17 L  (+0.04 subtle lift)
--surface-3: 0.21 L  (+0.08 elevated)
--surface-4: 0.24 L  (+0.11 stronger)
--surface-5: 0.27 L  (+0.14 max elevation)
```

---

## Skygger

### Depth-skala

| Token | Light | Dark | Bruk |
|-------|-------|------|------|
| `--shadow-xs` | 0 1px 1px, 0 1px 2px | Higher opacity | Subtle lift |
| `--shadow-sm` | — | — | Tooltips, small popovers |
| `--shadow-md` | — | — | Cards, modals (default) |
| `--shadow-lg` | — | — | Modals, drawers |
| `--shadow-xl` | — | — | Drawers, overlays |

### Fargetonede skygger (Semantic)

- `--shadow-success` — Success-grønn tint + depth
- `--shadow-error` — Error-rød tint + depth
- `--shadow-warning` — Warning-gul tint + depth
- `--shadow-info` — Info-blå tint + depth
- `--shadow-accent` — Accent-blå tint + depth

**Opasitet:** Light 8-12%, Dark 10-12% (Linear-restrained).

---

## Spacing

### Skala

```
--space-0: 0          --space-4: 1rem (16px)
--space-px: 1px       --space-5: 1.5rem (24px)
--space-1: 0.25rem    --space-6: 2rem (32px)
--space-2: 0.5rem     --space-7: 2.5rem (40px)
--space-3: 0.75rem    --space-8: 3rem (48px)
```

### Component gaps

- `--gap-tight: var(--space-1)` (4px) — Minimal
- `--gap-component: var(--space-4)` (app: 16px, web: 24px) — Standard
- `--gap-section: var(--space-8)` (48px) — Large sections

---

## Grensesnittkomponenter

Se **COMPONENT-DOCUMENTATION-GUIDE.md** for mal. Hver komponent dokumentert som:

1. **Hva?** — Formål + scenario
2. **Varianter** — Tabell: navn, formål, når
3. **Do/Don't** — 3+ praksisorienterte regler
4. **A11y** — ARIA, tastatur, kontrast, fokus
5. **Kodetips** — Implementering (HTML/CSS)
6. **Relatert** — Lenker

### Hoveddokumenterte komponenter

- **Button** (`<button>`, `.btn-*`) — Primær/sekundær/destruktiv
- **Form** (Input, Textarea, Select, Checkbox, Radio) — Skjemaer
- **Navigation** (Nav-item, Sidebar, Topbar) — App structure
- **Card** (`.card`, `.card-header`, `.card-footer`) — Content containers
- **Modal** (`.modal-*`) — Dialogs, overlay
- **Alert** (`.alert-*`) — Status messages
- **Badge** (`.badge-*`) — Status indicators
- **Table** (`.table`) — Data display
- **Tabs** (`.tabs-*`) — Tab interface
- **Accordion** (`.accordion-*`) — Expandable sections
- **Breadcrumb** (`.breadcrumb-*`) — Navigation path
- **Pagination** (`.pagination-*`) — Large datasets
- **Toast** (`.toast-*`) — Notifications
- **Skeleton** (`.skeleton-*`) — Loading placeholder
- **Spinner** (`.spinner`) — Loading indicator

---

## Tilgjengelighet (Mandatory)

### WCAG AA minimum

- **Kontrast:** Tekst ≥4.5:1 på bakgrunn, large tekst ≥3:1
- **Fokus:** Alle interaktive elementer `Tab`-navigerbar, `:focus-visible` styled
- **Tastatur:** `Enter`, `Space`, Piltaster hvor relevant
- **Navn:** Alle knapper/ikoner har a11y-navn (synlig tekst eller `aria-label`)
- **Rolle:** ARIA-roller korrekte (`role="button"`, `role="navigation"`, etc.)

### prefers-reduced-motion

Alle animasjoner og overganger **må** respektere `@media (prefers-reduced-motion: reduce)`:
```css
@media (prefers-reduced-motion: reduce) {
  * { transition-duration: 0s !important; animation-duration: 0s !important; }
}
```

---

## Deprecation policy

Tokens/klasser merket `@deprecated` er garantert til neste minor release (8 uker).

Eksempel:
```css
--text-8xl: /* @deprecated since v3.2.0 — use --text-7xl instead. Removing in v3.3.0. */
```

**Prosess:**
1. Minor `N.X.0`: Markerå `@deprecated` + skriv i release notes
2. Minor `N.X+1.0`: Fjern + listet breaking change

---

## Maskin-generering (Token Studio)

### Grayscale-adjustments for contrast

Token Studio kan regenerere tema ved å endre:
- `--gray-50` (lighter for higher contrast)
- `--gray-900` / `--gray-950` (darker)
- Alle deriverte tokens kaskaderer (WCAG automatisk)

### Surface-stepping

Generering av `--surface-*` via L-offsets:
```
surface-N = oklch(color-bg-L + offset, C, H)
```

### High-contrast variant

Sett ΔL(gray-50, gray-900) ≥ 0.995 for garantert WCAG AAA.

---

## CSS format-kontrakt

Maskin-transformasjoner avhenger av:
- Én selektor-liste per linje, slutter med `{`
- Tokens bare i `:root` blokker
- Ingen CSS-nesting
- `@keyframes`, `@font-face` uforandret

Se **CSS-FORMAT-CONTRACT.md**.

---

## Implementering

### NPM packages

```bash
npm install @nordover/tokens-app
npm install @nordover/tokens-web
npm install @nordover/components-app
npm install @nordover/components-web
```

### Import i prosjekt

**App:**
```css
@import "@nordover/tokens-app";
@import "@nordover/components-app";
```

**Web:**
```css
@import "@nordover/tokens-web";
@import "@nordover/components-web";
```

### Token JSON (DTCG)

- `tokens-app.json` — DTCG format, maskin-lesbar (Token Studio)
- `tokens-web.json` — Same format, different values
- Regenereres med `npm run build:tokens` (single source of truth: CSS)

---

## Versjonering

**SemVer:** `MAJOR.MINOR.PATCH`

- **PATCH:** Bug fixes, dokumentasjon, liten justering
- **MINOR:** Nye tokens, nye klasser, deprecated warnings (no breaking changes)
- **MAJOR:** Token-slettinger, klasseendringer, CSS-struktur-endringer

---

## Linker

- **Styleguide:** `docs/visual/styleguide.html` (live preview)
- **Komponenter:** `docs/visual/components/*.css` (source)
- **Tokens:** `docs/visual/tokens/*.css` (source)
- **Dokumentasjon:** `docs/visual/COMPONENT-DOCUMENTATION-GUIDE.md` (mal)
- **ADRs:** `docs/wiki/decisions/` (design decisions)

---

## Kontakt

Spørsmål? Åpne issue på GitHub eller kontakt `eirikfoleide@gmail.com`.
