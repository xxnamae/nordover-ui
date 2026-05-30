# Typografi-utilities

Lag av semantiske typografi-klasser, heading-defaults, prose-styling og site-wide CSS-defaults som bygger på `tokens-web`/`tokens-app`.

Bygger direkte på [Nordover-arkitektur § tokens](nordover-arkitektur.md#tokens-arkitektur).

## Font-loading: Inter Variable + Inter Tight Variable

Begge token-pakker bruker **variable fonts** som primær — én fil per familie, hele vekt-spekteret (100-900) tilgjengelig kontinuerlig. Lavere bandwidth, færre HTTP-requests, mulighet for finkalibrerte vekter per komponent.

Se [decision: Inter Variable som primær font](../decisions/2026-05-27-inter-variable-font.md).

**Self-hosted (anbefales):**
```css
/* base.css — øverst, før alle andre stiler */
@font-face {
  font-family: "Inter Variable";
  src: url("/fonts/InterVariable.woff2") format("woff2-variations"),
       url("/fonts/InterVariable.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Inter Variable";
  src: url("/fonts/InterVariable-Italic.woff2") format("woff2-variations"),
       url("/fonts/InterVariable-Italic.woff2") format("woff2");
  font-weight: 100 900;
  font-style: italic;
  font-display: swap;
}
@font-face {
  font-family: "Inter Tight Variable";
  src: url("/fonts/InterTight-Variable.woff2") format("woff2-variations"),
       url("/fonts/InterTight-Variable.woff2") format("woff2");
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
```

**Preload kritiske fonter** i `<head>`:
```html
<link rel="preload" href="/fonts/InterVariable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/InterTight-Variable.woff2" as="font" type="font/woff2" crossorigin>
```

**Alternativ: rsms.me-distribusjon** (uoffisiell CDN, samme kilde som fonts):
```html
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
```
For raskt prototype-arbeid. For produksjon: self-host for kontroll + ingen tredjeparts-DNS.

## Finkalibrerte vekter (variable font superpower)

Med variable font kan vi sette hvilken som helst `font-weight` mellom 100-900, ikke bare 400/500/600/700. Vi kan også sette via `font-variation-settings: 'wght' 437` for ekstra presisjon.

**Anbefaling for Nordover-husstilen:**

| Klasse | Vekt | Hvorfor |
|---|---|---|
| `text-display-xl` (text-8xl) | 380 | Lett-medium for elegant editorial display |
| `text-display-lg` (text-6xl) | 400 | Regular for store displays |
| `text-display-md` (text-4xl) | 420 | Litt heavier — bedre kontrast på medium displays |
| `text-heading-lg` (text-3xl) | 440 | Mellom regular og medium |
| `text-heading-md` (text-2xl) | 480 | Nesten medium |
| `text-heading-sm` (text-xl) | 500 | Medium — standard for små headings |
| `text-body-lg` / `text-body` | 400 | Regular for prosa |
| `text-body-sm` | 520 | Medium+ — bedre lesbarhet på små størrelser |
| `text-eyebrow` | 600 | Semibold for capitals |
| `text-caption` | 520 | Medium+ for UI-metadata |

Implementert via CSS-variabler så brand kan overstyre:
```css
:root {
  --font-weight-display-xl: 380;
  --font-weight-display-lg: 400;
  --font-weight-display-md: 420;
  --font-weight-heading-lg: 440;
  --font-weight-heading-md: 480;
  --font-weight-heading-sm: 500;
  --font-weight-body: 400;
  --font-weight-body-sm: 520;
  --font-weight-eyebrow: 600;
  --font-weight-caption: 520;
}
```

Hvert semantisk typografi-klasse bruker sin token:
```css
@utility text-display-xl {
  @apply text-8xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display-xl);
}
```

**Fallback:** når Inter Variable ikke laster (eller browser ikke støtter variable fonts), faller alle vekter til nærmeste 100-step (380 → 400, 520 → 500). Variabel-styling er progressive enhancement.

## Filosofi

Hybrid-tilnærming: semantiske klasser for 90% av bruken, atomic Tailwind-utilities for spesialtilfeller. Display-fonten kobles til **intensjon** (semantisk klasse), ikke til HTML-tag. Editorial-konvensjoner (text-balance, lining-nums, negativ tracking på display) er site-wide defaults — ikke noe utviklere må huske å aktivere.

Se [decision 2026-05-27 — typografi-utilities-arkitektur](../decisions/2026-05-27-typografi-utilities-arkitektur.md).

## Token-collision å fikse i tokens-web

`--font-display` (font-family) og `--font-weight-display` (font-weight) er begge eksponert i `@theme`-blokken i `tokens-web`. Tailwind v4 ville generert kolliderende `font-display`-utilities for begge.

**Fix:** Flytt `--font-weight-display` fra `@theme` til `:root` i tokens-web. Tokenet beholder semantikk (kan overstyres av brand), men eksponeres ikke som Tailwind-utility. Brukes via direkte `var(--font-weight-display)` i semantiske klasser.

## Site-wide CSS-defaults (legges i `base.css` eller globals)

```css
@layer base {
  body {
    font-family: var(--font-sans);
    font-size: var(--text-base);
    line-height: var(--text-base--line-height);
    color: var(--color-fg);
    background: var(--color-bg);
    text-wrap: pretty;
    font-variant-numeric: lining-nums;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  /* Heading-defaults: font-family, weight, leading — IKKE size.
     Size må settes eksplisitt via semantisk klasse eller atomic utility. */
  h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-display);
    font-weight: var(--font-weight-display);
    line-height: 1.15;
    letter-spacing: var(--tracking-tight);
    text-wrap: balance;
  }

  /* Tall i tabeller bør aligne — overstyr default lining-nums med tabular-nums */
  table {
    font-variant-numeric: lining-nums tabular-nums;
  }
}
```

## Semantiske typografi-klasser (Tailwind v4 `@utility`)

Definert i `@nordover/typografi.css` eller tilsvarende. Komponerer atomic-utilities + tokens for å gi én klasse = komplett typografi-mønster.

```css
/* === Display — for hero, store statements === */
@utility text-display-xl {
  @apply text-8xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
}

@utility text-display-lg {
  @apply text-6xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
}

@utility text-display-md {
  @apply text-4xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
}

/* === Headings — for seksjonstitler === */
@utility text-heading-lg {
  @apply text-3xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
}

@utility text-heading-md {
  @apply text-2xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
}

@utility text-heading-sm {
  @apply text-xl;
  font-family: var(--font-display);
  font-weight: var(--font-weight-display);
}

/* === Body — for innhold === */
@utility text-body-lg {
  @apply text-lg font-sans font-normal;
}

@utility text-body {
  @apply text-base font-sans font-normal;
}

@utility text-body-sm {
  @apply text-sm font-sans font-medium;   /* 500 — UI-bruk, ikke prosa. .prose body overstyrer til 400. */
}

/* === Spesielle === */
@utility text-eyebrow {
  @apply text-xs font-sans font-semibold uppercase;
  letter-spacing: var(--tracking-widest);
  color: var(--color-muted);
}

@utility text-caption {
  @apply text-xs font-sans font-medium;   /* 500 — UI-metadata leser bedre i medium */
  color: var(--color-muted);
}
```

**Bruksmønster i komponenter:**
```html
<h1 class="text-display-xl">Stor headline</h1>
<h2 class="text-heading-lg">Seksjonstittel</h2>
<p class="text-body">Brødtekst.</p>
<span class="text-eyebrow">Kategori</span>
```

**Når man bryter mønsteret:** atomic utilities er fortsatt tilgjengelige. `<h2 class="text-5xl font-medium tracking-normal">` fungerer for engangstilfeller.

## Prose — egen implementasjon for lang-form

Ikke `@tailwindcss/typography`. Egen `.prose`-klasse tunet for Scandi-min:

```css
.prose {
  max-width: var(--container-prose);
  color: var(--color-fg);
  font-size: var(--text-base);
  line-height: 1.7;

  & > * + * {
    margin-top: 1.25em;
  }

  & h1 {
    font-size: var(--text-5xl);
    margin-top: 2em;
    margin-bottom: 0.5em;
  }

  & h2 {
    font-size: var(--text-3xl);
    margin-top: 2.5em;
    margin-bottom: 0.5em;
  }

  & h3 {
    font-size: var(--text-2xl);
    margin-top: 2em;
    margin-bottom: 0.4em;
  }

  & h4 {
    font-size: var(--text-xl);
    margin-top: 1.75em;
    margin-bottom: 0.3em;
  }

  & p {
    text-wrap: pretty;
    font-weight: var(--font-weight-normal);   /* prose body overstyrer text-body-sm til 400 */
  }

  & blockquote {
    font-family: var(--font-display);
    font-size: var(--text-xl);
    font-style: italic;
    line-height: 1.4;
    border-inline-start: 2px solid var(--color-fg);
    padding-inline-start: 1.5em;
    margin-block: 2em;
    text-wrap: balance;
  }

  & a {
    color: var(--color-accent);
    text-decoration: underline;
    text-underline-offset: 0.2em;
    text-decoration-thickness: 1px;
    transition: color var(--duration-fast) var(--ease-out);
  }

  & a:hover {
    color: var(--color-accent-hover);
  }

  & ul, & ol {
    padding-inline-start: 1.5em;
  }

  & li + li {
    margin-top: 0.5em;
  }

  & code {
    font-family: var(--font-mono);
    font-size: 0.9em;
    background: var(--color-subtle);
    padding: 0.125em 0.375em;
    border-radius: var(--radius-sm);
  }

  & pre {
    font-family: var(--font-mono);
    background: var(--color-subtle);
    padding: 1em 1.25em;
    border-radius: var(--radius-md);
    overflow-x: auto;
    line-height: 1.5;
  }

  & pre code {
    background: transparent;
    padding: 0;
    font-size: 1em;
  }

  & img,
  & figure {
    margin-block: 2em;
    border-radius: var(--radius-md);
  }

  & figcaption {
    font-size: var(--text-sm);
    color: var(--color-muted);
    text-align: center;
    margin-top: 0.5em;
  }

  & hr {
    border: none;
    border-top: 1px solid var(--color-border);
    margin-block: 3em;
  }
}

/* Opt-in editorial-modifier: drop-cap på første paragraf */
.prose-editorial > p:first-of-type::first-letter {
  font-family: var(--font-display);
  font-size: 3.5em;
  font-weight: var(--font-weight-display);
  float: inline-start;
  line-height: 0.85;
  margin-inline-end: 0.1em;
  margin-block-start: 0.05em;
}
```

## Tilleggsutilities for OpenType-bryting

Default er `lining-nums` på `body` og `tabular-nums lining-nums` på `table`. Utilities for å bryte:

```css
@utility tabular-nums { font-variant-numeric: tabular-nums lining-nums; }
@utility oldstyle-nums { font-variant-numeric: oldstyle-nums; }
@utility small-caps { font-variant-caps: small-caps; }
```

Brukes på statistikk-blokker, datoer, prislisting der tall skal aligne (`tabular-nums`), eller på editorial-detaljer der "old-style"-tall passer estetikken (`oldstyle-nums`).

## Hva utelater vi bevisst

- **Stretched-text utilities** (`text-stretched-narrow`, etc.) — variable fonts er bra, men adder kompleksitet uten klart behov for Nordover-husstilen ennå.
- **`text-balance`-utility** — er allerede default på headings via base-laget. Atomic Tailwind-utility (`text-balance`/`text-pretty`) er tilgjengelig hvis man vil overstyre.
- **Drop-cap som default i `.prose`** — kun via `.prose-editorial`-modifier. Ikke alle artikler skal ha drop-cap; opt-in unngår overkill.

## Implementeringsrekkefølge i Nordover-repoet

1. Fiks token-kollisjonen: flytt `--font-weight-display` fra `@theme` til `:root` i `tokens-web.css`.
2. Lag `base.css` med site-wide defaults (body, h1-h6, table).
3. Lag `typografi.css` med `@utility`-blokkene for semantiske klasser.
4. Lag `prose.css` med `.prose`- og `.prose-editorial`-klassene.
5. Import-rekkefølge per app: `tokens-web.css` → `base.css` → `typografi.css` → `prose.css` → `clients/<slug>.css`.

## Se også

- [Nordover-arkitektur — tokens](nordover-arkitektur.md)
- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: typografi-utilities-arkitektur](../decisions/2026-05-27-typografi-utilities-arkitektur.md)
