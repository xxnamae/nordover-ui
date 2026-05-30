# v2 Hardening — arkitektonisk modning til "10/10"

**Dato:** 2026-05-27
**Status:** Delvis superseded — dark-mekanisme (`[data-theme="dark"]` i §2a) reversert av [v3 Rebuilding](2026-05-27-v3-rebuilding.md). Resten av v2 (gråskala, triplets, a11y, spacing, fallback, polish) er fortsatt aktiv.
**Etterfølger:** [2026-05-27 v3 Rebuilding](2026-05-27-v3-rebuilding.md), [2026-05-29 v3 Polish & shippable](2026-05-29-v3-polish-og-shippable.md)

**Kontekst:**
Etter en grundig ekstern review (sammenlignet med prisbelønte systemer som Every Layout, Tailwind, Linear) ble seks reelle hull identifisert som skiller "veldig bra" fra "uovervinnelig produksjonsklart". Disse er ikke nye features — det er **arkitektonisk modning** som låser inn kvalitet, a11y og motstandsdyktighet.

Tas i én samlet "v2 hardening"-iterasjon. Påvirker både token-spec og begge handoff-styleguider.

---

## 1. CSS `@layer`-arkitektur

**Problem:** I store prosjekter (særlig der rammeverket møter Elementor, WordPress-themes, eller andre tredjeparts CSS) eksploderer specificity-kriger. `!important` blir nødvendig der det aldri burde være det.

**Valgt:** Native CSS-lag med fast hierarki:

```css
@layer tokens, reset, primitives, components, utilities;

@layer tokens {
  :root { /* alle CSS-variabler */ }
}
@layer reset {
  * { box-sizing: border-box; }
  body { font-family: var(--font-sans); /* ... */ }
}
@layer primitives {
  .stack, .cluster, .grid-auto, .container { /* ... */ }
}
@layer components {
  .btn, .card, .form-input, .toast { /* ... */ }
}
@layer utilities {
  .muted, .text-eyebrow, /* utility-classes */ { /* ... */ }
}
```

**Hvorfor kritisk for Nordover:** vi har bestemt at rammeverket **delvis skal brukes i Elementor** (decision 2026-05-27 patterns-utvidelser-batch2 bekreftet behov for class-names). Elementor injiserer tonnevis av høy-specificity-CSS. Uten `@layer` havner vi i `!important`-helvete. Med `@layer`: lag-rekkefølgen er kontrakten, og **utility trumper alltid komponent uavhengig av kildekode-rekkefølge**.

**Brand-overstyringer** (`clients/<slug>.css`) får sitt eget lag på toppen:
```css
@layer tokens, reset, primitives, components, utilities, brand;
@layer brand {
  :root { --color-accent: #brand; }
}
```

---

## 2. Fargesystem: nøytral gråskala + semantiske tripletter

**Problem:** Vi har gode funksjonelle farger (`--color-error`, `--color-success`), men de er enkeltverdier. For å lage subtle bg, sterke borders, eller dempet text må vi ad-hoc bruke `color-mix()` overalt. Det er ikke "ad-hoc" som beslutning (color-mix var bevisst valgt for hover-states) — men **for tonale varianter** mangler vi systematikk.

**Valgt:**

### 2a. Nøytral gråskala via OKLCH

Én skala i bunnen. Alle nøytrale tokens deriverer fra den.

```css
@layer tokens {
  :root {
    --neutral-h: 250;        /* hue — svakt blå-nøytralt, kan brand overstyre */
    --neutral-c: 0.005;      /* chroma — nesten null = ekte nøytral */

    --gray-50:  oklch(0.98 var(--neutral-c) var(--neutral-h));   /* near-white */
    --gray-100: oklch(0.96 var(--neutral-c) var(--neutral-h));
    --gray-200: oklch(0.92 var(--neutral-c) var(--neutral-h));
    --gray-300: oklch(0.86 var(--neutral-c) var(--neutral-h));
    --gray-400: oklch(0.72 var(--neutral-c) var(--neutral-h));
    --gray-500: oklch(0.55 var(--neutral-c) var(--neutral-h));   /* midtpunkt — muted-text */
    --gray-600: oklch(0.43 var(--neutral-c) var(--neutral-h));
    --gray-700: oklch(0.30 var(--neutral-c) var(--neutral-h));
    --gray-800: oklch(0.18 var(--neutral-c) var(--neutral-h));
    --gray-900: oklch(0.10 var(--neutral-c) var(--neutral-h));   /* near-black */

    /* Semantiske deriverer */
    --color-bg: var(--gray-50);
    --color-fg: var(--gray-900);
    --color-muted: var(--gray-500);
    --color-subtle: var(--gray-100);
    --color-border: var(--gray-200);
  }

  [data-theme="dark"] {
    --color-bg: var(--gray-900);
    --color-fg: var(--gray-50);
    --color-muted: var(--gray-400);
    --color-subtle: var(--gray-800);
    --color-border: var(--gray-700);
  }
}
```

**Stor gevinst:** dark mode er nå **mapping**, ikke duplisering. Endre en L-verdi i `--gray-200`, og *alle* borders i hele systemet justeres konsistent.

### 2b. Semantiske tripletter

For brand-accent og hver semantisk farge: tre nivåer (subtle / base / strong).

```css
@layer tokens {
  :root {
    /* Accent (brand) */
    --accent-subtle: color-mix(in oklch, var(--color-accent) 10%, var(--color-bg));
    --accent: var(--color-accent);   /* eksisterende */
    --accent-strong: color-mix(in oklch, var(--color-accent) 75%, black);

    /* Error */
    --error-subtle: color-mix(in oklch, var(--error) 10%, var(--color-bg));
    --error: oklch(0.58 0.22 28);
    --error-strong: oklch(0.45 0.22 28);

    /* Success, Warning, Info — samme mønster */
    --success-subtle: color-mix(in oklch, var(--success) 10%, var(--color-bg));
    --success: oklch(0.60 0.16 160);
    --success-strong: oklch(0.48 0.16 160);

    /* etc. */
  }
}
```

**Bruksmønstre:**
- Toast/Alert-bg: `var(--error-subtle)` (ikke lenger inline `color-mix(...)`)
- Toast-border: `var(--error)`
- Toast-icon-farge: `var(--error-strong)` (bedre kontrast på subtle bg)

**Behold `color-mix()` for hover/active.** Det er ikke ad-hoc — det er **én avledning** (`--color-accent-hover = color-mix(--color-accent, black, 15%)`), ikke ad-hoc fargevalg. Triplettene løser tonale **varianter**; color-mix løser **state-justering**.

### 2c. Hva vi *ikke* gjør

Ikke full Tailwind-skala (50, 100, ..., 900) på alle farger. Det ville være å kopiere et utility-first-mønster som strider mot vår token-først-filosofi og Scandi-min-restraint. Tripletter dekker 90% av reelle behov.

---

## 3. Universell tilgjengelighet (a11y)

**Tre konkrete tiltak:**

### 3a. Universell `:focus-visible`

```css
@layer utilities {
  :focus-visible {
    outline: 2px solid var(--color-focus);
    outline-offset: 2px;
    border-radius: var(--radius-sm);  /* matcher der relevant */
  }
}
```

Plassert i `utilities`-laget → trumper alle komponenters egne focus-stiler hvis de mangler. **Alle** interaktive elementer (klikkbare kort, accordion-trigger, checkbox, radio, kustom-toggles) får dette gratis.

### 3b. Global reduced-motion

```css
@layer reset {
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-delay: -1ms !important;
      animation-duration: 1ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0s !important;
      scroll-behavior: auto !important;
    }
  }
}
```

**`!important` her er bevisst:** dette er det eneste stedet der vi godtar !important i hele rammeverket — fordi det er en a11y-garanti som skal trumpe absolutt alt.

### 3c. ARIA på CSS-only-toggles

For styleguidene (og rammeverket generelt) der vi bruker `<input type="checkbox">` + `<label>` for dark mode / mobile menu:

```html
<input type="checkbox" id="dark" class="sr-only"
       aria-label="Aktiver mørk modus" role="switch">
<label for="dark" class="theme-toggle" aria-hidden="false">...</label>
```

`role="switch"` på checkbox kommuniserer toggle-natur. `aria-label` gir skjermlesere meningsfull beskrivelse. Labelen forblir interaktiv (klikkbar overflate), men aria-hidden=false sikrer at den ikke dobles opp i annonseringen.

---

## 4. Granulært spacing-system

**Problem:** vi har semantiske gaps (`tight` / `component` / `section`), men ad-hoc `0.625rem` / `1.25rem` i komponentene. Spacing-rytmen er ikke disiplinert.

**Valgt:** to-lags spacing (primitiv → semantisk), samme mønster som typografi.

### 4a. Numerisk primitiv-skala (utvidet høyere for web)

```css
@layer tokens {
  :root {
    --space-0: 0;
    --space-1: 0.25rem;    /* 4px */
    --space-2: 0.5rem;     /* 8px */
    --space-3: 0.75rem;    /* 12px */
    --space-4: 1rem;       /* 16px */
    --space-5: 1.5rem;     /* 24px */
    --space-6: 2rem;       /* 32px */
    --space-7: 2.5rem;     /* 40px */
    --space-8: 3rem;       /* 48px */
    --space-10: 4rem;      /* 64px */
    --space-12: 6rem;      /* 96px */
    --space-16: 8rem;      /* 128px */
    --space-20: 10rem;     /* 160px */
    --space-24: 12rem;     /* 192px */
    --space-32: 16rem;     /* 256px */
    --space-40: 20rem;     /* 320px */
    --space-48: 24rem;     /* 384px */
  }
}
```

**Hvorfor høyere enn 8** (etter brukerens eksplisitte ønske): editorial luft i marketing-sider trenger 128-256px section-padding. App-rammeverket bruker stort sett 1-12, web bruker hele skalaen.

Skala-pattern (4, 8, 12, 16, 24, 32, 40, 48, **deretter doblet for de store**: 64, 96, 128...) matcher Tailwind sin spacing-konvensjon — utviklere kjenner den.

### 4b. Semantiske aliases (eksisterende, nå deriverer)

```css
@layer tokens {
  :root {
    /* Web */
    --gap-tight: var(--space-2);          /* 8px */
    --gap-component: var(--space-5);      /* 24px */
    --spacing-section: clamp(var(--space-12), 12vw, var(--space-20));  /* 96-160 fluid */

    /* Page-padding fluid */
    --page-padding: clamp(var(--space-5), 4vw, var(--space-8));   /* 24-48px */
  }
}
```

App-context overstyrer til tettere defaults:
```css
.app-context {
  --gap-tight: var(--space-1);           /* 4px (litt mer kompakt) */
  --gap-component: var(--space-4);       /* 16px */
}
```

### 4c. Komponenter slutter med magiske tall

**Før:**
```css
.btn { padding: 0.625rem 1.25rem; }
.card { padding: 1.5rem; }
```

**Etter:**
```css
.btn { padding: var(--space-2) var(--space-4); }       /* 8 16 */
.btn-sm { padding: var(--space-1) var(--space-3); }    /* 4 12 */
.btn-lg { padding: var(--space-3) var(--space-6); }    /* 12 32 */
.card { padding: var(--space-5); }                     /* 24 */
```

Tar tid å migrere alle komponenter, men en gang gjort er rytmen permanent disciplined.

---

## 5. Komponent-polish

### 5a. Checkbox/radio i `em` (skalerer med tekst)

**Før:**
```css
.form-checkbox { width: 1.125rem; height: 1.125rem; }
```

**Etter:**
```css
.form-checkbox { width: 1.125em; height: 1.125em; }
```

Da brukeren forstørrer fonten (browser zoom eller settings), vokser checkboxen i takt. Spesielt viktig for synshemmede brukere som setter font-size høyere globalt.

### 5b. Inline-edit padding-lås

**Sikre at display og editing har eksakt samme box-metrics** så ingen layout-hopp:

```css
.inline-edit-display,
.inline-edit-input {
  padding: var(--space-1) var(--space-2);
  border: 1px solid transparent;       /* viktig: matcher input-border-tykkelsen */
  line-height: 1.5;
  font: inherit;
  border-radius: var(--radius-sm);
}
.inline-edit-input {
  border-color: color-mix(in oklch, var(--color-border) 70%, var(--color-focus) 30%);
  background: var(--color-bg);
}
```

Display-mode har **transparent border** med samme tykkelse — så når editing aktiveres, "blinker" border bare inn fargen, og hverken padding eller posisjon endres.

### 5c. Data Table responsive — opt-in card-mode

**Default:** horizontal scroll (eksisterende). For dashboards med tall-tunge tabeller er dette best.

**Opt-in:** `.data-table-responsive` transformerer rader til kort under 40rem viewport.

```css
@media (max-width: 40rem) {
  .data-table-responsive thead {
    position: absolute;
    width: 1px; height: 1px;
    overflow: hidden;
    clip: rect(0,0,0,0);
  }
  .data-table-responsive tr {
    display: block;
    border: var(--border-card);
    border-radius: var(--radius-md);
    padding: var(--space-3);
    margin-bottom: var(--space-3);
  }
  .data-table-responsive td {
    display: flex;
    justify-content: space-between;
    padding: var(--space-1) 0;
    border-bottom: none;
  }
  .data-table-responsive td::before {
    content: attr(data-label);
    font-weight: var(--font-weight-medium);
    color: var(--color-muted);
    margin-right: var(--space-2);
  }
}
```

Krever at hver `<td>` får `data-label="Status"` etc. — men det er en lokal kostnad for et opt-in mønster. Apper som har dashboards beholder horizontal-scroll. Apper med innholds-fokuserte lister bruker card-mode.

---

## 6. Font-fallback med size-adjust (null CLS)

**Problem:** når Inter Variable laster fra `rsms.me` (eller self-hosted), oppstår FOUT/FOIT: layouten "hopper" når font-en bytter fra system-fallback til Inter, fordi metrics ikke matcher.

**Valgt:** definert fallback-font med justerte metrikker som matcher Inter visuelt, så swap blir umerkelig.

```css
@layer reset {
  /* Optimized Arial-fallback for Inter — verdier matcher Vercel's next/font for Inter */
  @font-face {
    font-family: "Inter Fallback";
    src: local("Arial");
    size-adjust: 107%;
    ascent-override: 90%;
    descent-override: 22.5%;
    line-gap-override: 0%;
  }
}

@layer tokens {
  :root {
    --font-sans: "Inter Variable", "Inter Fallback", system-ui, sans-serif;
    --font-display: "Inter Tight Variable", "Inter Fallback", system-ui, sans-serif;
  }
}
```

**Resultat:**
- Når Inter laster: glatt overgang, nesten ingen synlig endring
- Når Inter ikke laster (offline, CDN-bråk): fallback ser "nesten-Inter" ut

**Variable-vekt-degradering** er fortsatt en risiko ved fallback (vekt 380 snapper til 400 i Arial). Hvis vi vil løse det 100%: bruk `@supports (font-variation-settings: normal)` til å skille adferd. Men 90% gevinst ligger i size-adjust alene.

---

## Konsekvenser samlet

| Område | Før v2 | Etter v2 |
|---|---|---|
| **Specificity-håndtering** | Risiko for `!important`-kriger med Elementor | Garantert kaskade via `@layer` |
| **Dark mode** | 8-10 hex-overrides per pakke | Mapping på gråskala (én L-axis) |
| **Fokus a11y** | Per-komponent fokus-stiler | Universell via utilities-lag |
| **Reduced-motion** | Ikke håndtert globalt | Garantert globalt slettet |
| **Spacing-disiplin** | Magiske `0.625rem` / `1.25rem` overalt | To-lags skala, alt deriverer |
| **CLS ved font-load** | Synlig hopp | Tilnærmet null |
| **Checkbox-skalering** | Hardkodet rem | Vokser med font-size (em) |
| **Inline edit-stabilitet** | Mulig layout-hopp ved mode-skift | Transparent-border-lås |
| **Mobile data-table** | Bare horizontal scroll | Opt-in card-mode tilgjengelig |

**Reverseringskostnad:** Lav per item. `@layer` er additive (gamle stilark uten layers blander seg fint inn). Numerisk spacing erstatter ikke semantisk, det legger seg under. Gråskala kan defineres uten å bytte ut eksisterende color-tokens (ny som default, gamle som overrides hvis nødvendig).

**Implementasjons-rekkefølge anbefalt:**
1. `@layer` (arkitektur-fundament — alt annet sitter inne i lagene)
2. Universell focus + reduced-motion (a11y er ikke forhandlingsbart)
3. Gråskala + tripletter (dark mode-renselse)
4. Numerisk spacing-skala
5. Font-fallback
6. Komponent-polish (em, inline-edit, data-table)

---

## Hva som *ikke* endres

- Token-shape forblir stabil for konsumenter. `--color-bg` peker fortsatt til samme verdi (bare derivert nå).
- Eksisterende komponenter trenger ikke API-endringer.
- Semantiske gap-tokens (`--gap-tight` etc.) beholdes — bare deriverer nå fra `--space-N`.
- Decision-historikken er intakt. Dette er **modning**, ikke arkitekturskifte.

**Konkret leveranse:** oppdatert `nordover-arkitektur.md` (v2 token-system), begge handoff-styleguider med `@layer` + nye tokens + a11y-lag.

> **Merknad 2026-05-29:** v3-tillegget som tidligere lå her er flyttet til egen fil — [2026-05-27 v3 Rebuilding](2026-05-27-v3-rebuilding.md). Begrunnelse: én decision per arkitekturskift gjør historikken sporbar.
