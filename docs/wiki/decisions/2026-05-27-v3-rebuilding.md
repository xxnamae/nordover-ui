# v3 Rebuilding — én dark-mekanisme, motion-system, mobil-nav, full --space-migrasjon

**Dato:** 2026-05-27
**Status:** Aktiv
**Forgjenger:** [2026-05-27 v2 Hardening](2026-05-27-v2-hardening.md) (§2a om `[data-theme="dark"]` reverseres her)
**Etterfølger:** [2026-05-29 v3 Polish & shippable](2026-05-29-v3-polish-og-shippable.md)

**Kontekst:**
Etter v2-hardening ble begge handoff-styleguider testet på mobil. Tre bugs og fem manglende systemnivå-tokens dukket opp. I stedet for å patche ble begge styleguider gjenoppbygget rent på et enhetlig fundament. Denne fila dokumenterer hva som endret seg fra v2.

---

## Bugs reversert/fikset

### 1. Dark-mekanisme: én, ikke to (reverserer v2 §2a)

**v2 brukte:** `[data-theme="dark"]` som CSS-selector + JS-toggle som setter `<html data-theme>`.

**Problem:** I styleguidene hadde app-fila både `data-theme="dark"` hardkodet på `<html>` **og** et CSS-only `<input id="dark" type="checkbox" checked>` med `:has(#dark:checked)`-fallback. Når brukeren toggled av, ble checkbox unchecked, men `data-theme`-attributtet hang igjen → "stuck dark".

**v3 bruker:** kun `:root:has(#dark:checked)`. Ingen `data-theme`-attributt. App defaulter dark via `checked` i markup-input. Web defaulter light (input unchecked).

**Konsekvens:**
- Én sannhet for tema-state (checkbox `checked`-property).
- Ingen JS-bibliotek nødvendig for toggling — ren CSS via `:has()`.
- Krever Safari 15.4+ / Chrome 105+ / Firefox 121+ for `:has()`-støtte.
- **Avveining:** Mister tema-persistens på tvers av reloads — løses i [v3 Polish](2026-05-29-v3-polish-og-shippable.md) via minimal localStorage-script.

### 2. Mobil-navigasjon: hamburger + slide-in sidebar

**v2 leverte:** sidebar skjult under 60rem viewport, uten erstatning.

**Resultat:** mobile brukere kunne ikke navigere styleguidene. Hardening-seksjonene var i praksis usynlige.

**v3 leverer:** CSS-only mobile-meny via `<input id="nav" type="checkbox">`-toggle + hamburger-label + `:has(#nav:checked)`-trigger som åpner sidebar som slide-in fra venstre med backdrop-label som lukker ved klikk utenfor.

### 3. Responsive demoer kollapser

Flere demo-grid hadde faste `grid-template-columns: repeat(N, 1fr)` uten mobil-breakpoint. v3 bruker `repeat(auto-fit, minmax(min(15rem, 100%), 1fr))`-mønster gjennomgående.

---

## Systemutvidelser

### Enhetspolicy kanonisert

| Enhet | Brukes til |
|---|---|
| `rem` | Type-skala, spacing, container-bredder |
| `em` | Checkbox/radio (skalerer med tekst), tracking, ikon-i-knapp |
| `px` | Border-tykkelse, radius, shadow-offsets |
| `%` / `vw` | Fluid clamp-grenser |
| `ch` | Prose-bredder (`--container-prose: 65ch`) |
| (unitless) | `line-height` |

Hver enhet har én rolle. Magiske `0.625rem`-verdier er ikke lenger lov i komponent-CSS.

### Spacing utvidet til `--space-48`

`--space-0` (0) til `--space-48` (24rem / 384px). Web bruker hele skalaen for editorial luft i section-padding (opp til 256px). App bruker stort sett `--space-0` til `--space-12`.

### Type-trinn utvidet

App fikk 11 trinn (`--text-2xs` til `--text-5xl`). Web beholder fluid `--text-xs` til `--text-8xl`. Begge eksponerer semantiske klasser (`.t-display-xl`, `.t-heading-lg`, `.t-body-lg`, `.t-eyebrow` osv.).

### Line-height og letter-spacing nå skalaer

```css
--leading-none: 1; --leading-tight: 1.1; --leading-snug: 1.2;
--leading-normal: 1.5; --leading-relaxed: 1.625; --leading-loose: 2;

--tracking-tighter: -0.04em; --tracking-tight: -0.02em;
--tracking-normal: 0; --tracking-wide: 0.005em; --tracking-widest: 0.08em;
```

Tidligere ad-hoc i komponent-CSS, nå systematiske tokens.

### Icon-size + duration + utvidet z-index og radius

```css
--icon-xs: 0.875em; --icon-sm: 1em; --icon-md: 1.125em; --icon-lg: 1.5em;

--duration-instant: 0ms; --duration-fast: 150ms; --duration-base: 250ms;
--duration-slow: 400ms; --duration-slower: 600ms;

--radius-xs: 2px; --radius-sm: 4px; --radius-md: 6px;
--radius-lg: 8px; --radius-xl: 12px; --radius-2xl: 20px;

--z-base: 0; --z-dropdown: 10; --z-sticky: 20; --z-overlay: 25;
--z-modal: 30; --z-toast: 40; --z-tooltip: 50;
```

### Fullt motion-system

Ni navngitte keyframes: `fade-in`, `fade-out`, `slide-up`, `slide-down`, `slide-in-right`, `scale-in`, `pop`, `spin`, `shimmer`, `pulse`. Utility-klasser `.animate-*` matcher hver keyframe. `.stagger` med `--i: <index>` for sekvensiell animasjon i lister.

Tasteful Scandi-min: app raskere (`--duration-fast` 100ms), web mykere (`--duration-base` 250ms). Alt under `prefers-reduced-motion`-garanti fra v2.

### Full `--space`-migrasjon

Alle komponenter i begge styleguider bruker nå `var(--space-N)` eller semantisk alias (`--gap-tight`, `--gap-component`). Magiske `0.625rem` / `1.125rem`-verdier er fjernet fra komponent-CSS. Et fåtall em-baserte ikoner i sprite-SVG beholder em (riktig per enhetspolicy).

---

## Resultat

To rene single-mekanisme-styleguider:
- `docs/visual/styleguide-web.html` (light default, fluid type, flate knapper)
- `docs/visual/styleguide-app.html` (dark default, statisk type, tactile knapper)

Begge med komplett `@layer`-struktur, én dark-mekanisme, mobil-meny, og dedikerte doc-seksjoner for Skalaer/Enhetspolicy og Motion.

**Reverseringskostnad:** Lav. v3-tokens er supersett av v2. Ingen konsumenter er bygget på v2 ennå.
