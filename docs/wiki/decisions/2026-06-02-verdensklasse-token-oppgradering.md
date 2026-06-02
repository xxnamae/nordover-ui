# ADR: Verdensklasse token-oppgradering (2026-06-02)

**Status:** Vedtatt
**Signerare:** Design system owner
**Datering:** 2026-06-02
**Revidert:** —

---

## Kontekst

En dyp audit av token-fundamentet (fire uavhengige Opus-agenter benchmarket mot Apple HIG, Material Design 3, Linear og Fluent) avdekket at *verdiene* i token-CSS-en stort sett var verdensklasse-kalibrert, men at noen strukturelle hull skilte systemet fra de globale lederne. Det mest alvorlige — flagget uavhengig av tre av fire agenter — var at **dark mode manglet tonal surface elevation**: alle hevede flater delte én `--color-surface`, mens Material 3 og Apple lysner overflaten gradvis med høyde.

Målet for denne oppgraderingen er global verdensklasse på linje med Apple HIG og Material Design 3, uten å bryte eksisterende kontrakter. Token-**navn** er offentlige kontrakter; derfor er alle endringer enten additive (nye tokens) eller rene verdijusteringer.

---

## Avgjørelse

Vi legger til følgende token-tiere, speilet i både `tokens-web.css` og `tokens-app.css`:

### 1. Tonal surface elevation (`--surface-1..5`) — kjernegrepet

Et fem-trinns surface-system. I light mode er nivåene ~hvit/subtil (minimal visuell effekt); i dark mode lysner overflaten med elevation (OKLCH L 0.13 → 0.27), slik Material 3 sin tonal elevation fungerer.

| Token | Bruk |
|-------|------|
| `--surface-1` | Basispanel (= `--color-surface`, kontrakt-alias) |
| `--surface-2` | Kort/paneler |
| `--surface-3` | Dropdowns, popovers, menyer, kalendere |
| `--surface-4` | Modal-dialog, drawer |
| `--surface-5` | Topp-sheets |

`--color-surface` beholdes uendret som alias for `--surface-1` — eksisterende kontrakt er intakt.

### 2. Semantiske shadow-aliaser

`--shadow-inset`, `--shadow-tooltip`, `--shadow-popover`, `--shadow-modal`, `--shadow-drawer`, `--shadow-card-hover`. Wiki-en lovet flere av disse uten at de fantes i CSS — et reelt kontraktsbrudd som nå lukkes. De peker på eksisterende `--shadow-*`, og arver derfor dark-mode-redefinisjonen automatisk.

### 3. Accent-tier

`--accent-subtle`, `--accent-muted`, `--accent-emphasis`, `--on-accent-subtle` — gir en lavemfasis-flate (valgte rader, tonal-knapp, badges) og en branded primær-vei uten å redefinere flere uavhengige tokens.

### 4. Type-rolle-tokens

Komposisjonelle roller (`--type-{display,headline,title,body,label}-{size,leading,weight,tracking}`) gir Apple/M3-paritet og en stabil kontrakt for fremtidig native-mapping (iOS/Android), et eksplisitt visjonsmål. I tillegg tracking-roller: `--tracking-display`, `--tracking-heading`, `--tracking-title`.

### 5. Øvrige additive tokens

- `--radius-3xl` (32px web / 24px app) — generøs tier for store flater.
- `--ease-spring-physics` — ekte spring via `linear()` for signatur-bevegelse (eksisterende `--ease-spring` urørt).
- App: finkalibrerte variable-font-vekter (`--fw-display-lg`, `--fw-heading-lg/-md`, `--fw-body-sm`, `--fw-eyebrow`, `--fw-caption`) for paritet med web.

### 6. Gråskala — forsiktig L-jevning

Gråskalaen ble jevnet for et mer perseptuelt jevnt L-forløp, men `--color-muted` og `--color-border` ble holdt på WCAG-trygge verdier. Verifisert: `--color-muted` holder AA (light 5.51:1, dark 7.78:1); `--color-border` forblir subtil.

---

## Konsekvenser

- **Ingen breaking changes.** Alle endringer er additive eller verdijusteringer innenfor WCAG-grenser.
- **JSON regenereres** i samme commit (`npm run build:tokens`); CI håndhever synk (`npm run check:tokens`).
- **Komponenter kan nå** referere `--surface-2/3/4` for korrekt dark-elevation (se ADR for komponentoppgraderingen).
- **Mirroring:** alle tokens speilet web↔app; verdier divergerer kun der pakke-defaultene tilsier det (f.eks. inset-alpha, radius-3xl, vekter).

---

## Se også

- `docs/wiki/decisions/2026-06-02-nye-komponenter-og-varianter.md`
- `docs/wiki/decisions/2026-06-01-brand-lag-kontrakt.md`
- `docs/wiki/topics/nordover-elevation.md`
