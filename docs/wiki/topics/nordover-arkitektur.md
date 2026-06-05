# Nordover-arkitektur

Notater om Nordover-rammeverket: tokens, komponenter, leveransestack.

> **Status 2026-05-27:** Rammeverket er på **v3** etter to runder hardening. Se [v3-seksjonen under](#v3-token-system-gjeldende--2026-05-27) for kanoniske token-blokker. Eldre seksjoner (fra `## Tokens-arkitektur` og nedover) er bevart som **historisk v1-arkiv** — bruk v3-blokkene som implementerings-sannhet.

## v3 Token-system (gjeldende — 2026-05-27)

Kanonisk kilde for v3-endringene: [decision: v2 hardening + v3 system-utvidelser](../decisions/2026-05-27-v2-hardening.md).

### Hva v3 legger til over v1

1. **`@layer`-arkitektur** — Elementor- og legacy-CSS-kompatibilitet via deterministisk kaskade.
2. **Nøytral OKLCH-gråskala** (`--gray-50` … `--gray-950`) — én skala styrer bg/fg/muted/subtle/border konsistent på tvers av light/dark.
3. **Semantiske triplets** (`error`, `success`, `warning`, `info` × `subtle`/`base`/`strong`) — alerts, badges og toast trenger ikke ad-hoc `color-mix()`.
4. **Granulær spacing-skala** `--space-0` … `--space-48` (0 → 384px) — utvider hovedseksjonene fra v1.
5. **Motion-system** — `@keyframes` (fade, slide, scale, pop, spin, shimmer) + `.animate-*`-utilities + `.stagger`.
6. **Universell a11y** — globale `:focus-visible`-styles, `prefers-reduced-motion` på alle keyframes, `role="switch"` og ARIA på CSS-only toggles.
7. **Font-fallback med `size-adjust`** — null CLS før Inter Variable er lastet (Inter Fallback @ `size-adjust: 107%`).
8. **Token-policy låst** — `rem` (type/spacing), `em` (checkbox/tracking), `px` (border/radius/shadow), `%`/`vw` (fluid), `ch` (prose), unitless (line-height).
9. **Én dark-mekanisme** — `:root:has(#dark:checked)` overstyrer tokens. Eldre `[data-theme="dark"]` er fjernet.

### Kanoniske v3-tokens — `@nordover/tokens-web`

```css
@layer tokens, reset, primitives, components, utilities, brand;

@layer tokens {
  :root {
    /* === Nøytral OKLCH-gråskala (styrer bg/fg/muted/subtle/border) === */
    --neutral-h: 250;            /* Subtil kjølig tone — endres per brand */
    --neutral-c: 0.005;          /* Chroma nær 0 for ren grå */
    --gray-50:  oklch(0.985 var(--neutral-c) var(--neutral-h));
    --gray-100: oklch(0.97  var(--neutral-c) var(--neutral-h));
    --gray-200: oklch(0.92  var(--neutral-c) var(--neutral-h));
    --gray-300: oklch(0.86  var(--neutral-c) var(--neutral-h));
    --gray-400: oklch(0.70  var(--neutral-c) var(--neutral-h));
    --gray-500: oklch(0.55  var(--neutral-c) var(--neutral-h));
    --gray-600: oklch(0.44  var(--neutral-c) var(--neutral-h));
    --gray-700: oklch(0.33  var(--neutral-c) var(--neutral-h));
    --gray-800: oklch(0.22  var(--neutral-c) var(--neutral-h));
    --gray-900: oklch(0.14  var(--neutral-c) var(--neutral-h));
    --gray-950: oklch(0.08  var(--neutral-c) var(--neutral-h));

    /* === Semantiske farger (light defaults) — én skala styrer all UI-grå === */
    --color-bg:      var(--gray-50);
    --color-fg:      var(--gray-950);
    --color-muted:   var(--gray-500);
    --color-subtle:  var(--gray-100);
    --color-border:  var(--gray-200);
    --color-accent:    var(--gray-950);
    --color-accent-fg: var(--gray-50);

    /* === Semantiske triplets (alerts, badges, toast) === */
    --error:         oklch(0.62 0.23 25);
    --error-subtle:  color-mix(in oklch, var(--error) 12%, var(--color-bg));
    --error-strong:  color-mix(in oklch, var(--error) 70%, black);
    --success:        oklch(0.62 0.16 160);
    --success-subtle: color-mix(in oklch, var(--success) 12%, var(--color-bg));
    --success-strong: color-mix(in oklch, var(--success) 70%, black);
    --warning:        oklch(0.70 0.17 65);
    --warning-subtle: color-mix(in oklch, var(--warning) 12%, var(--color-bg));
    --warning-strong: color-mix(in oklch, var(--warning) 70%, black);
    --info:           oklch(0.62 0.18 245);
    --info-subtle:    color-mix(in oklch, var(--info) 12%, var(--color-bg));
    --info-strong:    color-mix(in oklch, var(--info) 70%, black);

    /* === Granulær spacing-skala (0 → 384px) === */
    --space-0:   0;
    --space-px:  1px;
    --space-1:   0.25rem;  /*  4px */
    --space-2:   0.5rem;   /*  8px */
    --space-3:   0.75rem;  /* 12px */
    --space-4:   1rem;     /* 16px */
    --space-5:   1.25rem;  /* 20px */
    --space-6:   1.5rem;   /* 24px */
    --space-8:   2rem;     /* 32px */
    --space-10:  2.5rem;   /* 40px */
    --space-12:  3rem;     /* 48px */
    --space-16:  4rem;     /* 64px */
    --space-20:  5rem;     /* 80px */
    --space-24:  6rem;     /* 96px */
    --space-32:  8rem;     /* 128px */
    --space-40: 10rem;     /* 160px */
    --space-48: 24rem;     /* 384px — kun til hero/section-bunn */

    /* === Font-fallback (size-adjust gir null CLS før Inter laster) === */
    --font-sans: "Inter Variable", "Inter Fallback", system-ui, -apple-system, sans-serif;
    --font-display: "Inter Tight Variable", "Inter Tight Fallback", var(--font-sans);

    /* === Motion-tokens (samme som v1, men brukt av animate-utilities) === */
    --duration-fast: 150ms;
    --duration-base: 250ms;
    --duration-slow: 400ms;
    --ease-out: cubic-bezier(0.2, 0, 0, 1);
    --ease-spring: cubic-bezier(0.2, 0.8, 0.2, 1);
  }

  /* Dark mode — én mekanisme. Overskrift av semantiske tokens, ikke gråskala. */
  :root:has(#dark:checked) {
    --color-bg:      var(--gray-950);
    --color-fg:      var(--gray-50);
    --color-muted:   var(--gray-400);
    --color-subtle:  var(--gray-900);
    --color-border:  var(--gray-800);
    --color-accent:    var(--gray-50);
    --color-accent-fg: var(--gray-950);
  }
}

/* Universal a11y (utenfor @layer for å vinne kaskade) */
*:focus-visible {
  outline: 2px solid var(--color-focus, var(--color-accent));
  outline-offset: 2px;
  border-radius: var(--radius-sm, 4px);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0ms !important;
  }
}

@font-face {
  font-family: "Inter Fallback";
  src: local("Arial");
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
```

### Kanoniske v3-tokens — `@nordover/tokens-app`

Identiske `@layer`, gråskala, triplets, spacing og motion som tokens-web. Forskjeller:

```css
@layer tokens {
  :root {
    /* App defaulter mørkt — initial-check via #dark[checked] i markup. */
    --color-accent:    oklch(0.65 0.20 250);  /* Brand-blå, ikke neutral */
    --color-accent-fg: var(--gray-50);

    /* Kompakt body (14px) */
    --text-base: 0.875rem;
    --text-base--line-height: 1.5;

    /* Tactile button-surface — inset-skygger + gradient */
    --button-surface-bg-rest: linear-gradient(
      to bottom,
      color-mix(in oklch, var(--color-accent) 92%, white) 0%,
      var(--color-accent) 100%
    );
    --button-surface-shadow-rest:
      inset 0 0.5px 0 0 rgb(255 255 255 / 0.18),
      0 1px 0 0 color-mix(in oklch, var(--color-accent) 70%, black),
      var(--shadow-sm);
    --button-surface-shadow-active:
      inset 0 1px 2px 0 rgb(0 0 0 / 0.18),
      var(--shadow-xs);

    /* Tactile-overstyringer per tone — bunnkanten skal ALDRI være blå
       på danger/success — alltid mørkere variant av tone-fargen. */
  }

  /* tone-danger og tone-success overstyrer --button-surface-shadow-rest
     med color-mix på respektive tone-farger. Se styleguide.html. */
}
```

Se [`docs/visual/styleguide.html`](../../visual/styleguide.html) for fullt rendrede v3-blokker med alle utilities, komponenter og handoff-tabeller (unified web + app styleguide).

### Brand-overstyring (tokens-brand.css)

Brand-laget kjøres etter alle andre — overstyrer kun **semantiske** tokens, ikke gråskala-primitiver:

```css
@layer brand {
  :root {
    --neutral-h: 220;             /* Kjøligere brand-grå */
    --color-accent: oklch(0.55 0.20 145);  /* Egen brand-farge */
    --color-accent-fg: white;
  }
}
```

---

## Tokens-arkitektur

> **Historisk v1-arkiv (foreldet):** Innholdet under er bevart som referanse til hvordan tokens så ut før v2/v3-hardeningen. Bruk v3-blokkene over som implementerings-sannhet. Se [decision: v2 hardening](../decisions/2026-05-27-v2-hardening.md) for hvorfor dette ble endret.

### To pakker, ikke én

Nordover leverer **to separate token-pakker**, fordi marketing-nettsider og SaaS-apper har motstridende krav:

| | `@nordover/tokens-web` | `@nordover/tokens-app` |
|---|---|---|
| Mål | Marketing- og landingssider | SaaS-grensesnitt (eks. Omhu) |
| Type-scale | 1.2 → 1.333 (fluid, editorial) | 1.2 (statisk, kompakt) |
| Display-sizes | xl → 8xl (fluid clamp, opp til 160px) | maks 3xl (statisk) |
| Body | 16px base | 14px base (info-tetthet) |
| Section-spacing | Stort, fluid (opp til 160px) | Lite, statisk |
| Page-padding | Fluid clamp (opp til 96px) | Statisk |
| Fluid-strategi | Fluid alt fra `--text-lg` og opp | Static alt |
| Display font-weight | 400 (editorial default) | n/a (ingen display-font) |
| Letter-spacing-tokens | Ja (negativ tracking på display) | Nei |

Se [decision: to tokens-pakker](../decisions/2026-05-27-to-tokens-pakker.md) og [decision: tokens-web tunet for skandinavisk minimalisme](../decisions/2026-05-27-tokens-web-scandi-tuning.md).

### Tuning: skandinavisk minimalisme med dempbarhet

Nordovers husstil er skandinavisk minimalisme med dramatisk typografi som primært designelement. `tokens-web` er tunet for dette som default:
- Type-skala går høyt (opp til 160px display), med moderat aggressiv fluid-rampe.
- Section-spacing og page-padding gir mye luft.
- Display-vekt defaulter til `400` (editorial), ikke `700` (amerikansk SaaS-aesthetic).
- Letter-spacing-tokens for negativ tracking på store displays.

**Men dempbarhet er bygget inn.** Brand-overstyringer i `clients/<slug>.css` kan tone systemet ned for konservative kunder:

```css
/* Eksempel: tammere kunde — kappe topp-display og redusere spacing */
:root {
  /* Slå av topp-displays ved å aliase dem nedover */
  --text-8xl: var(--text-5xl);
  --text-7xl: var(--text-5xl);

  /* Strammere section-spacing */
  --spacing-section: clamp(3rem, 8vw, 6rem);

  /* Smalere page-padding */
  --page-padding: clamp(1.25rem, 4vw, 3rem);

  /* Tyngre display */
  --font-weight-display: 600;
}
```

Aliasering nedover (`--text-8xl: var(--text-5xl)`) er en billig måte å "fjerne" topp-trinn uten å fjerne dem fra Tailwind-utilities — utvikleren kan fortsatt bruke `text-8xl`-utility, den vil bare ikke skille seg fra `text-5xl`.

### Dekorative tokens (lagt til iterasjon 3)

Begge pakker har:
- **Gradient-tokens** for hero-bakgrunner: `--gradient-radial-accent`, `--gradient-radial-subtle`, `--gradient-fade-bottom`.
- **Glass / frosted blur** for sticky headers, overlays, floating bars: `--glass-bg`, `--glass-bg-strong`, `--glass-blur`, `--glass-blur-strong`, `--glass-border`.
- **Refinert dark mode** med Linear-inspirerte verdier (svakt blå-tintet bg, sofistikerte muted/border).

`@utility glass` og `@utility glass-strong` definert i `effects.css` (egen fil, importeres etter `elevation.css`).

### Felles prinsipper (begge pakker)

- **Tailwind v4 `@theme`-blokk** for tokens som blir utilities. `:root` for layout-mål som ikke trenger utility.
- **Tre nivåer**: primitiv (skala) → semantisk (intensjon) → komponent (bruk). `tokens.css` definerer de to første.
- **html font-size urørt.** All skalering går gjennom rem, brukerens 16px-default respekteres.
- **Line-heights unitless** og motsatt kurve av størrelse: små tekster trenger **mer** line-height (lesbarhet), display trenger mindre (kompakthet).
- **Dark mode via `<html data-theme="dark">`.** Husk: shadows må også overstyres, ikke bare farger.
- **`prefers-reduced-motion`-override** nuller ut alle `--duration-*`-tokens på rotnivå.
- **Container-bredder i rem**, ikke px. Containere handler om innhold; innhold skalerer med rem.
- **Color-states via `color-mix()` med token-overstyring.** `--color-accent-hover` defaulter til `color-mix(in oklch, var(--color-accent) 85%, black)`, men kan overstyres.
- **Z-index-skala** definert eksplisitt (ingen `z-9999`-kaos).

## `@nordover/tokens-web` (marketing)

```css
/*
 * @nordover/tokens-web — marketing-nettsider
 *
 * Tunet for skandinavisk minimalisme med dramatisk typografi.
 * Fluid type fra --text-lg og opp, opp til 160px på desktop.
 * Stort section-spacing, generøs page-padding.
 *
 * Type-skala-parametre (for regenerering via https://utopia.fyi/type/calculator):
 *   min:   320px viewport, 16px base, ratio 1.2
 *   max:   1440px viewport, 18px base, ratio 1.333
 *   steps: -2 til 8 (xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl, 6xl, 7xl, 8xl)
 *
 * Avrundet til hele px etter generering for lesbarhet.
 */

@import "tailwindcss";

@theme {
  /* === Typografi-stack === */
  --font-sans: "Inter Variable", "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-display: "Inter Tight Variable", "Inter Tight", "Inter Variable", "Inter", system-ui, sans-serif;
  --font-mono: ui-monospace, "SF Mono", "Menlo", monospace;

  /* === Type-skala — statisk under base, fluid fra lg og opp, ratio 1.2 → 1.333 === */
  --text-xs: 0.75rem;                                              /* 12px */
  --text-xs--line-height: 1.55;
  --text-xs--letter-spacing: 0.01em;
  --text-sm: 0.875rem;                                             /* 14px */
  --text-sm--line-height: 1.55;
  --text-sm--letter-spacing: 0.005em;
  --text-base: 1rem;                                               /* 16px */
  --text-base--line-height: 1.6;
  --text-base--letter-spacing: 0;
  --text-lg: clamp(1.125rem, 1.089rem + 0.179vw, 1.25rem);         /* 18 → 20 */
  --text-lg--line-height: 1.5;
  --text-lg--letter-spacing: 0;
  --text-xl: clamp(1.25rem, 1.179rem + 0.357vw, 1.5rem);           /* 20 → 24 */
  --text-xl--line-height: 1.4;
  --text-xl--letter-spacing: -0.005em;
  --text-2xl: clamp(1.5rem, 1.357rem + 0.714vw, 2rem);             /* 24 → 32 */
  --text-2xl--line-height: 1.3;
  --text-2xl--letter-spacing: -0.01em;
  --text-3xl: clamp(1.875rem, 1.661rem + 1.071vw, 2.625rem);       /* 30 → 42 */
  --text-3xl--line-height: 1.2;
  --text-3xl--letter-spacing: -0.02em;
  --text-4xl: clamp(2.25rem, 1.893rem + 1.786vw, 3.5rem);          /* 36 → 56 */
  --text-4xl--line-height: 1.1;
  --text-4xl--letter-spacing: -0.02em;
  --text-5xl: clamp(2.75rem, 2.25rem + 2.5vw, 4.5rem);             /* 44 → 72 */
  --text-5xl--line-height: 1.05;
  --text-5xl--letter-spacing: -0.025em;
  --text-6xl: clamp(3.25rem, 2.536rem + 3.571vw, 5.75rem);         /* 52 → 92 */
  --text-6xl--line-height: 1.0;
  --text-6xl--letter-spacing: -0.03em;
  --text-7xl: clamp(3.75rem, 2.679rem + 5.357vw, 7.5rem);          /* 60 → 120 */
  --text-7xl--line-height: 0.95;
  --text-7xl--letter-spacing: -0.035em;
  --text-8xl: clamp(4.5rem, 2.929rem + 7.857vw, 10rem);            /* 72 → 160 */
  --text-8xl--line-height: 0.9;
  --text-8xl--letter-spacing: -0.04em;

  /* === Font-vekter === */
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  /* OBS: --font-weight-display ligger i :root, ikke @theme, for å unngå
     Tailwind utility-kollisjon med --font-display (font-family). */

  /* === Letter-spacing (tracking) — semantiske tokens === */
  --tracking-tighter: -0.04em;   /* Display 7xl-8xl */
  --tracking-tight: -0.02em;     /* Display 3xl-6xl */
  --tracking-normal: 0;
  --tracking-wide: 0.005em;      /* Liten tekst */
  --tracking-widest: 0.08em;     /* Eyebrow / caps / labels */

  /* === Farger — semantiske, brand overstyrer === */
  --color-bg: #FFFFFF;
  --color-fg: #0A0A0A;
  --color-muted: #6B6B6B;
  --color-subtle: #F4F4F2;
  --color-accent: #0A0A0A;
  --color-accent-fg: #FFFFFF;
  --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, black);
  --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, black);
  --color-border: #E5E5E5;
  --color-focus: #0066FF;
  --color-error: oklch(0.58 0.22 28);      /* ≈ #D63A30 — warmer, refined */
  --color-success: oklch(0.60 0.16 160);   /* ≈ #16A07A — fresh emerald */
  --color-warning: oklch(0.68 0.17 65);    /* ≈ #DC8B22 — refined amber */

  /* === Spacing — Tailwinds 4px-skala beholdes. Semantiske layout-tokens: === */
  --spacing-section: clamp(4rem, 12vw, 10rem);          /* 64 → 160px */
  --spacing-section-sm: clamp(2.5rem, 7vw, 5rem);       /* 40 → 80px */
  --spacing-section-lg: clamp(6rem, 18vw, 15rem);       /* 96 → 240px */

  /* === Radius === */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 20px;
  --radius-full: 9999px;

  /* === Shadows — kalibrert for Scandi-min editorial (subtilere enn industri-default) === */
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.04);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.04);
  --shadow-md: 0 4px 8px -2px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.05);
  --shadow-lg: 0 12px 20px -4px rgb(0 0 0 / 0.1), 0 6px 8px -4px rgb(0 0 0 / 0.06);
  --shadow-xl: 0 24px 40px -8px rgb(0 0 0 / 0.12), 0 10px 16px -8px rgb(0 0 0 / 0.08);
  --shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.06);

  /* Semantiske shadow-aliaser — komponenter foretrekker disse over t-shirt-navn */
  --shadow-tooltip: var(--shadow-sm);
  --shadow-popover: var(--shadow-md);
  --shadow-modal: var(--shadow-lg);
  --shadow-drawer: var(--shadow-xl);
  --shadow-card-hover: var(--shadow-xs);

  /* === Motion === */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out: cubic-bezier(0.2, 0, 0, 1);
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;

  /* === Breakpoints === */
  --breakpoint-xs: 375px;
}

:root {
  /* === Layout — i rem så de skalerer med brukerens font-size === */
  --container-narrow: 45rem;    /* 720px */
  --container-default: 80rem;   /* 1280px */
  --container-wide: 90rem;      /* 1440px */
  --container-edge: 100%;       /* Ultra-wide editorial — kun page-padding rammer inn */
  --container-prose: 65ch;      /* Lang-tekst / artikler */

  /* === Page-padding — én fluid token, generøs på desktop === */
  --page-padding: clamp(1.5rem, 6vw, 6rem);            /* 24 → 96px */

  /* === Display-vekt — ligger her, ikke i @theme, for å unngå
     navnekollisjon med --font-display (font-family) i Tailwind. === */
  --font-weight-display: 400;   /* Editorial default — brand kan overstyre til 300/600/700 */

  /* === Semantisk gap-skala (brukes av Stack/Cluster/Grid) === */
  --gap-tight: 0.5rem;          /* 8px — innenfor en komponent */
  --gap-component: 1.5rem;      /* 24px — mellom relaterte komponenter */
  --gap-section: var(--spacing-section);  /* mellom seksjoner — speiler --spacing-section */

  /* === Border-tokens — parallell "flat" elevation === */
  --border-width-hairline: 0.5px;     /* Subtilt — luksuriøs Scandi-feel på retina */
  --border-width-thin: 1px;           /* Standard */
  --border-width-medium: 2px;         /* Vekt, fremheving */

  --border-card: var(--border-width-thin) solid var(--color-border);
  --border-input: var(--border-width-thin) solid var(--color-border);
  --border-divider: var(--border-width-thin) solid var(--color-border);
  --border-focus: var(--focus-ring-width) solid var(--color-focus);

  /* === Hover-lift-tokens (brukes av @utility hover-lift) === */
  --lift-distance: -2px;
  --lift-shadow-from: var(--shadow-xs);
  --lift-shadow-to: var(--shadow-md);

  /* === Dekorative gradient-tokens (for hero, banner, section-bakgrunner) === */
  --gradient-radial-accent: radial-gradient(
    ellipse 80% 50% at 50% -20%,
    color-mix(in oklch, var(--color-accent) 8%, transparent) 0%,
    transparent 70%
  );
  --gradient-radial-subtle: radial-gradient(
    ellipse 100% 60% at 50% 0%,
    var(--color-subtle) 0%,
    transparent 70%
  );
  --gradient-fade-bottom: linear-gradient(
    to bottom,
    transparent 0%,
    var(--color-bg) 100%
  );

  /* === Glass / frosted blur (for sticky headers, overlays, floating bars) === */
  --glass-bg: color-mix(in oklch, var(--color-bg) 72%, transparent);
  --glass-bg-strong: color-mix(in oklch, var(--color-bg) 88%, transparent);
  --glass-blur: blur(12px) saturate(180%);
  --glass-blur-strong: blur(20px) saturate(180%);
  --glass-border: var(--border-width-thin) solid color-mix(in oklch, var(--color-border) 50%, transparent);

  /* === Chart/data-viz-palett (samme keys som tokens-app for konsistens) === */
  --chart-1: oklch(0.55 0.15 145);
  --chart-2: oklch(0.62 0.14 70);
  --chart-3: oklch(0.55 0.18 245);
  --chart-4: oklch(0.55 0.20 295);
  --chart-5: oklch(0.60 0.12 195);
  --chart-6: oklch(0.58 0.20 350);
  --chart-7: oklch(0.65 0.12 220);
  --chart-8: oklch(0.58 0.16 30);

  /* === Refinements === */
  --focus-ring: 0 0 0 var(--focus-ring-width) var(--color-focus);
  --focus-ring-offset-bg: var(--color-bg);
  --font-tabular: ui-monospace, "SF Mono", "Menlo", monospace;
  --button-glow: 0 0 32px 0 color-mix(in oklch, var(--color-accent) 25%, transparent);
  --ease-spring: cubic-bezier(0.2, 0.8, 0.2, 1);
  --ease-emphasized: cubic-bezier(0.3, 0, 0, 1);

  /* === Button-tokens === */
  --button-radius: var(--radius-md);
  --button-font-weight: 500;

  /* === Button-surface — flat default i tokens-web ===
     Eksponert som tokens slik at samme button-CSS kan rendre flat
     eller tactile basert på pakke. Tactile aktiveres via btn-elevated. */
  --button-surface-bg-rest: var(--color-accent);
  --button-surface-bg-hover: var(--color-accent-hover);
  --button-surface-bg-active: var(--color-accent-active);
  --button-surface-shadow-rest: none;
  --button-surface-shadow-active: none;

  /* === Input-tokens === */
  --input-radius: var(--radius-md);
  --input-border-color: var(--color-border);
  --input-border-color-focus: var(--color-focus);
  --input-border-color-error: var(--color-error);
  --input-bg: var(--color-bg);
  --input-bg-disabled: var(--color-subtle);

  /* === Z-index-skala === */
  --z-base: 0;
  --z-dropdown: 10;
  --z-sticky: 20;
  --z-modal: 30;
  --z-toast: 40;
  --z-tooltip: 50;

  /* === Focus-ring === */
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --focus-ring-color: var(--color-focus);
}

[data-theme="dark"] {
  /* Linear-inspirerte verdier — lett blå-tint i bakgrunnen, sofistikerte muted/border */
  --color-bg: #0A0A0B;             /* Nesten svart med subtil blå tone */
  --color-fg: #F7F7F8;
  --color-muted: #8A8F98;           /* Linear-style muted */
  --color-subtle: #18181B;          /* Kort-bakgrunn */
  --color-accent: #F7F7F8;
  --color-accent-fg: #0A0A0B;
  --color-border: #27272A;          /* Subtil border */
  --color-focus: #4D8DFF;           /* Lysere blå for bedre kontrast på mørk bg */
  --color-error: oklch(0.65 0.22 28);
  --color-success: oklch(0.65 0.16 160);
  --color-warning: oklch(0.72 0.17 65);

  /* Shadows må re-defineres i dark mode — svart på svart er usynlig */
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.3);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.4), 0 1px 2px -1px rgb(0 0 0 / 0.3);
  --shadow-md: 0 4px 8px -2px rgb(0 0 0 / 0.5), 0 2px 4px -2px rgb(0 0 0 / 0.4);
  --shadow-lg: 0 12px 20px -4px rgb(0 0 0 / 0.6), 0 6px 8px -4px rgb(0 0 0 / 0.4);
  --shadow-xl: 0 24px 40px -8px rgb(0 0 0 / 0.7), 0 10px 16px -8px rgb(0 0 0 / 0.5);
  --shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.3);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-base: 0ms;
    --duration-slow: 0ms;
  }
}
```

## `@nordover/tokens-app` (SaaS-grensesnitt)

```css
/*
 * @nordover/tokens-app — SaaS-apper (Omhu, framtidige produkter)
 * Statisk type-skala. Kompakt body (14px). Lite section-spacing.
 * Optimalisert for info-tetthet og forutsigbarhet, ikke visuell flyt.
 */

@import "tailwindcss";

@theme {
  /* === Typografi-stack === */
  --font-sans: "Inter Variable", "Inter", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SF Mono", "Menlo", monospace;
  /* Ingen --font-display — apper trenger ikke egen display-font */

  /* === Type-skala — statisk, kompakt, 14px base === */
  --text-xs: 0.6875rem;     /* 11px — labels, metadata */
  --text-xs--line-height: 1.5;
  --text-sm: 0.8125rem;     /* 13px — sekundær UI-tekst */
  --text-sm--line-height: 1.5;
  --text-base: 0.875rem;    /* 14px — primær UI-tekst */
  --text-base--line-height: 1.5;
  --text-md: 1rem;          /* 16px — content-view (artikler, lange tekster) */
  --text-md--line-height: 1.6;
  --text-lg: 1.125rem;      /* 18px — sub-headers */
  --text-lg--line-height: 1.4;
  --text-xl: 1.25rem;       /* 20px — section headers */
  --text-xl--line-height: 1.3;
  --text-2xl: 1.5rem;       /* 24px — page headers */
  --text-2xl--line-height: 1.25;
  --text-3xl: 1.875rem;     /* 30px — toppnivå (sjelden brukt) */
  --text-3xl--line-height: 1.2;
  /* Ingen 4xl/5xl/6xl — apper trenger ikke display-sizes */

  /* === Font-vekter === */
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* === Farger — samme semantikk som web, men app-defaults === */
  --color-bg: #FFFFFF;
  --color-fg: #0A0A0A;
  --color-muted: #6B6B6B;
  --color-subtle: #F7F7F5;
  --color-accent: #0066FF;     /* Apper trenger ofte en tydelig brand-farge */
  --color-accent-fg: #FFFFFF;
  --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, black);
  --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, black);
  --color-border: #E5E5E5;
  --color-focus: var(--color-accent);
  --color-error: oklch(0.65 0.23 25);      /* ≈ #EE4646 — bright, SaaS-synlig */
  --color-success: oklch(0.70 0.18 155);   /* ≈ #25B377 — bright emerald */
  --color-warning: oklch(0.74 0.18 65);    /* ≈ #F09124 — bright amber */
  --color-info: oklch(0.62 0.18 245);      /* ≈ #2778E0 — bright blue */

  /* === Spacing — Tailwinds 4px-skala. Statiske section-tokens === */
  --spacing-section: 3rem;
  --spacing-section-sm: 2rem;
  --spacing-section-lg: 4.5rem;

  /* === Radius — mindre enn web, mer "verktøy"-følelse === */
  --radius-sm: 3px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;

  /* === Shadows — tettere, mer subtile for SaaS-UI === */
  --shadow-xs: 0 1px 1px 0 rgb(0 0 0 / 0.03);
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.04), 0 1px 1px -1px rgb(0 0 0 / 0.03);
  --shadow-md: 0 2px 4px -1px rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.04);
  --shadow-lg: 0 8px 12px -3px rgb(0 0 0 / 0.08), 0 3px 5px -3px rgb(0 0 0 / 0.06);
  --shadow-xl: 0 16px 24px -6px rgb(0 0 0 / 0.1), 0 6px 10px -6px rgb(0 0 0 / 0.07);
  --shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.05);

  /* Semantiske aliaser */
  --shadow-tooltip: var(--shadow-sm);
  --shadow-popover: var(--shadow-md);
  --shadow-modal: var(--shadow-lg);
  --shadow-drawer: var(--shadow-xl);
  --shadow-card-hover: var(--shadow-xs);

  /* === Motion — raskere defaults, app-følelse === */
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out: cubic-bezier(0.2, 0, 0, 1);
  --duration-fast: 100ms;
  --duration-base: 150ms;
  --duration-slow: 250ms;

  /* === Breakpoints === */
  --breakpoint-xs: 375px;
}

:root {
  /* === Layout === */
  --container-narrow: 40rem;     /* 640px — forms, settings */
  --container-default: 80rem;    /* 1280px — dashboards */
  --container-wide: 100%;        /* Full-width dashboards uten max-width */
  --container-prose: 65ch;

  /* === Page-padding — statisk, mindre på mobil === */
  --page-padding: 1.5rem;
  --page-padding-sm: 1rem;       /* Bruk på små viewports via media query */

  /* === Semantisk gap-skala (tettere defaults for info-tetthet) === */
  --gap-tight: 0.375rem;         /* 6px */
  --gap-component: 1rem;         /* 16px */
  --gap-section: var(--spacing-section);

  /* === Border-tokens === */
  --border-width-hairline: 0.5px;
  --border-width-thin: 1px;
  --border-width-medium: 2px;

  --border-card: var(--border-width-thin) solid var(--color-border);
  --border-input: var(--border-width-thin) solid var(--color-border);
  --border-divider: var(--border-width-thin) solid var(--color-border);
  --border-focus: var(--focus-ring-width) solid var(--color-focus);

  /* === Hover-lift-tokens (mindre dramatiske for SaaS) === */
  --lift-distance: -1px;
  --lift-shadow-from: var(--shadow-xs);
  --lift-shadow-to: var(--shadow-sm);

  /* === Dekorative gradient-tokens === */
  --gradient-radial-accent: radial-gradient(
    ellipse 80% 50% at 50% -20%,
    color-mix(in oklch, var(--color-accent) 10%, transparent) 0%,
    transparent 70%
  );
  --gradient-radial-subtle: radial-gradient(
    ellipse 100% 60% at 50% 0%,
    var(--color-subtle) 0%,
    transparent 70%
  );
  --gradient-fade-bottom: linear-gradient(
    to bottom,
    transparent 0%,
    var(--color-bg) 100%
  );

  /* === Glass / frosted blur === */
  --glass-bg: color-mix(in oklch, var(--color-bg) 75%, transparent);
  --glass-bg-strong: color-mix(in oklch, var(--color-bg) 90%, transparent);
  --glass-blur: blur(10px) saturate(180%);
  --glass-blur-strong: blur(18px) saturate(180%);
  --glass-border: var(--border-width-thin) solid color-mix(in oklch, var(--color-border) 50%, transparent);

  /* === Status-farger (for SaaS-workflows: Todo, In Progress, etc.) === */
  --status-backlog: #7C7C7C;
  --status-todo: #94A3B8;
  --status-in-progress: #F59E0B;
  --status-in-review: #6366F1;
  --status-done: #22C55E;
  --status-canceled: #525252;
  --status-blocked: #EF4444;

  /* === Priority-farger (Linear-style) === */
  --priority-urgent: #DC2626;
  --priority-high: #F59E0B;
  --priority-medium: #94A3B8;
  --priority-low: #525252;
  --priority-none: #404040;

  /* === Chart/data-visualisering-palett (8 distinkte kategorier) === */
  --chart-1: oklch(0.72 0.18 145);    /* Green */
  --chart-2: oklch(0.78 0.16 70);     /* Amber */
  --chart-3: oklch(0.65 0.20 245);    /* Blue */
  --chart-4: oklch(0.65 0.22 295);    /* Purple */
  --chart-5: oklch(0.72 0.13 195);    /* Teal */
  --chart-6: oklch(0.68 0.22 350);    /* Pink */
  --chart-7: oklch(0.78 0.13 220);    /* Cyan */
  --chart-8: oklch(0.65 0.18 30);     /* Orange */

  /* === Nav-item-tokens (for sidebar) === */
  --nav-item-bg-hover: color-mix(in oklch, var(--color-fg) 6%, transparent);
  --nav-item-bg-active: color-mix(in oklch, var(--color-fg) 10%, transparent);
  --nav-item-radius: var(--radius-md);

  /* === Refinements: focus-ring via box-shadow, tabular font, glow, spring === */
  --focus-ring: 0 0 0 var(--focus-ring-width) var(--color-focus);
  --focus-ring-offset-bg: var(--color-bg);
  --font-tabular: ui-monospace, "SF Mono", "Menlo", monospace;
  --button-glow: 0 0 24px 0 color-mix(in oklch, var(--color-accent) 30%, transparent);
  --ease-spring: cubic-bezier(0.2, 0.8, 0.2, 1);
  --ease-emphasized: cubic-bezier(0.3, 0, 0, 1);

  /* === Button-tokens === */
  --button-radius: var(--radius-md);
  --button-font-weight: 500;

  /* === Button-surface — tactile default i tokens-app ===
     SaaS-UI har "trykk-bare" knapper som standard. Apple/Stripe-vibe.
     For flat-button: <Button variant="ghost"> eller brand-overstyring. */
  --button-surface-bg-rest: linear-gradient(
    to bottom,
    color-mix(in oklch, var(--color-accent) 92%, white) 0%,
    var(--color-accent) 100%
  );
  --button-surface-bg-hover: linear-gradient(
    to bottom,
    color-mix(in oklch, var(--color-accent-hover) 92%, white) 0%,
    var(--color-accent-hover) 100%
  );
  --button-surface-bg-active: var(--color-accent-active);
  --button-surface-shadow-rest:
    inset 0 0.5px 0 0 rgb(255 255 255 / 0.18),
    0 1px 0 0 var(--color-accent-active),
    var(--shadow-sm);
  --button-surface-shadow-active:
    inset 0 1px 2px 0 rgb(0 0 0 / 0.18),
    var(--shadow-xs);

  /* === Input-tokens === */
  --input-radius: var(--radius-md);
  --input-border-color: var(--color-border);
  --input-border-color-focus: var(--color-focus);
  --input-border-color-error: var(--color-error);
  --input-bg: var(--color-bg);
  --input-bg-disabled: var(--color-subtle);

  /* === Z-index-skala === */
  --z-base: 0;
  --z-dropdown: 10;
  --z-sticky: 20;
  --z-modal: 30;
  --z-toast: 40;
  --z-tooltip: 50;

  /* === Focus-ring === */
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --focus-ring-color: var(--color-focus);
}

[data-theme="dark"] {
  /* Stacked/Linear-inspirert SaaS dark mode — neutral pure-near-black */
  --color-bg: #0A0A0A;
  --color-fg: #F7F7F7;
  --color-muted: #7C7C7C;
  --color-subtle: #141414;
  --color-accent: #3B82F6;
  --color-accent-fg: #FFFFFF;
  --color-border: #1F1F1F;
  --color-error: oklch(0.68 0.22 25);
  --color-success: oklch(0.72 0.18 155);
  --color-warning: oklch(0.76 0.18 65);

  --shadow-xs: 0 1px 1px 0 rgb(0 0 0 / 0.25);
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.3), 0 1px 1px -1px rgb(0 0 0 / 0.25);
  --shadow-md: 0 2px 4px -1px rgb(0 0 0 / 0.4), 0 1px 2px -1px rgb(0 0 0 / 0.3);
  --shadow-lg: 0 8px 12px -3px rgb(0 0 0 / 0.5), 0 3px 5px -3px rgb(0 0 0 / 0.4);
  --shadow-xl: 0 16px 24px -6px rgb(0 0 0 / 0.6), 0 6px 10px -6px rgb(0 0 0 / 0.45);
  --shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.25);
}

@media (prefers-reduced-motion: reduce) {
  :root {
    --duration-fast: 0ms;
    --duration-base: 0ms;
    --duration-slow: 0ms;
  }
}
```

## Migrasjon fra nåværende `tokens.css`

Nåværende fil er nærmest `tokens-web` men med flere mangler:
1. Bytt statiske `--text-lg` → `--text-6xl` til clamp-versjoner.
2. Inverter line-height-kurven for små størrelser (xs/sm trenger ~1.55, ikke 1.4).
3. Utvid skala til `--text-7xl` og `--text-8xl` (opp til 160px) for editorial-displays.
4. Endre maks-ratio fra 1.25 til 1.333.
5. Legg til `letter-spacing`-tokens per step (negativ tracking på display).
6. Legg til `--tracking-*` semantiske tokens.
7. Legg til `--font-weight-display: 400` (editorial default).
8. Erstatt `--spacing-section: 6rem` (statisk) med fluid clamp opp til 160px.
9. Slett `--gutter-mobile/tablet/desktop`, erstatt med én `--page-padding`-token (opp til 96px).
10. Konverter container-bredder fra px til rem.
11. Legg til `--container-edge: 100%` og `--container-prose: 65ch`.
12. Legg til `--color-accent-hover/active` via `color-mix(in oklch, ...)`.
13. Legg til z-index-skala og focus-ring-tokens.
14. Legg til shadow-override i dark mode + reduced-motion-block.
15. Bytt `--font-weight-regular` → `--font-weight-normal`.

Pakk Omhu sin tokens-overstyring inn i `@nordover/tokens-app` i stedet for å patche `tokens-web`.

## Avklart 2026-05-27

Tre konvensjons-spørsmål om tokens-arkitektur er nå besluttet:

- **Utopia-konfig** committes som kommentar-blokk i toppen av hver tokens-fil med min/max viewport, base, ratio, steps. Reproduserbar regenerering uten egen tooling. Se [decision](../decisions/2026-05-27-tokens-fellesregler.md).
- **`color-mix()` / OKLCH** brukes uten fallback. Browsere fra 2023 og nyere støtter dette. Omhu kan legge til eksplisitte hover-farger som overstyring hvis behovet oppstår senere. Se [decision](../decisions/2026-05-27-tokens-fellesregler.md).
- **`--color-accent`** har samme semantikk i begge pakker — "primær brand-handling". Ulike defaults, samme rolle. Trenger man ulik rolle, lag nytt token (eks. `--color-spotlight`). Se [decision](../decisions/2026-05-27-tokens-fellesregler.md).

## WCAG-kontrast (målt 2026-05-29 via WCAG 2.1-formel)

Verdiene under er beregnet ved å konvertere OKLCH til lineær sRGB → relativ luminans → WCAG-formel `(L1+0.05)/(L2+0.05)`. Ikke estimater — faktiske tall fra Python-skript i [v3-polish-decision](../decisions/2026-05-29-v3-polish-og-shippable.md).

Etter polish-iterasjonen ble `--gray-500` justert fra L=0.55 til L=0.50 (web) og fra L=0.56 til L=0.50 (app), og app-light accent endret fra `#3B82F6` til `#2563EB` (blue-600). Tabellen reflekterer disse verdiene.

### Light mode

| Kombinasjon | Web | App | WCAG-krav | Status |
|---|---|---|---|---|
| `--color-fg` på `--color-bg` (body) | **20.59** | **19.27** | AA 4.5, AAA 7.0 | ✅ AAA |
| `--color-muted` på `--color-bg` (sekundær tekst) | **6.00** | **5.75** | AA 4.5 | ✅ AA |
| `--color-muted` på `--color-subtle` (kort-metadata) | **5.42** | **5.34** | AA 4.5 | ✅ AA |
| `--color-accent` på `--color-bg` (knapp-bg vs side-bg) | 20.59 | **4.95** | AA 3.0 (UI) / 4.5 (tekst) | ✅ AA |
| `--color-accent-fg` (hvit) på `--color-accent` (knapp-tekst) | 20.59 | **5.17** | AA 4.5 | ✅ AA |

### Dark mode

| Kombinasjon | Web | App | WCAG-krav | Status |
|---|---|---|---|---|
| `--color-fg` på `--color-bg` (body) | **20.27** | **19.83** | AA 4.5, AAA 7.0 | ✅ AAA |
| `--color-muted` på `--color-bg` (sekundær) | **8.41** | **8.35** | AA 4.5 | ✅ AAA |
| `--color-muted` på `--color-subtle` (kort-metadata) | **7.71** | **7.45** | AA 4.5 | ✅ AAA |
| `--color-accent` (hvit/blå) på `--color-bg` (knapp-bg) | 20.27 | **5.63** | AA 3.0 (UI) | ✅ AA |
| `--color-accent-fg` (hvit) på `--color-accent` (knapp-tekst, app) | 20.27 | **3.68** | AA 4.5 (body), 3.0 (large) | ⚠️ Bestått som AA-Large, faller på AA-body |

### Konklusjoner og merknader

- **Body-tekst:** AAA i alle modus, alle pakker.
- **Muted-tekst:** AA i alle kombinasjoner (forrige iterasjon hadde 4.46 — under AA. Nå 5.34+ på alle bg).
- **Triplets (subtle/base/strong):** Alle strong-on-subtle-kombinasjoner består AA (typisk 6-10 contrast). Sikre toast/alert-tekster.
- **App-light accent (#2563EB blue-600):** valgt for å bestå AA både mot lys bg (4.95) og med hvit knapp-tekst (5.17). #3B82F6 (blue-500) ble valgt bort fordi den ikke består AA (3.52 / 3.68).
- **App-dark accent (#3B82F6 blue-500):** beholdes for visuell synlighet. **Kjent kompromiss:** hvit tekst-kontrast på primær-knapp i dark er 3.68 — består WCAG AA-Large (≥3.0) og 1.4.11 (UI Components ≥3.0), men ikke 1.4.3 (Tekst ≥4.5). Dette er industristandard for SaaS-dark-mode (Linear, Stripe, GitHub samme tradeoff). Tactile-knappens gradient + inset-shadows + medium font-weight (500) gir ekstra visuell separasjon. **For strikt AA-compliance:** brand kan overstyre `--color-accent` i dark til `#5E6AD2` (Linear-stil indigo, 4.40/4.70) eller `#1D4ED8` (blue-700, 3.09/6.70).

### Re-måling

```python
# Python-snutt for re-validering når tokens endres
def lum(L, C, h):  # OKLCH → relativ luminans
    import math; hr = math.radians(h)
    a, b = C*math.cos(hr), C*math.sin(hr)
    l_=L+0.396*a+0.216*b; m_=L-0.106*a-0.064*b; s_=L-0.089*a-1.291*b
    l,m,s = l_**3, m_**3, s_**3
    r=4.077*l-3.308*m+0.231*s; g=-1.268*l+2.610*m-0.341*s; bl=-0.004*l-0.703*m+1.708*s
    return 0.2126*max(0,r) + 0.7152*max(0,g) + 0.0722*max(0,bl)
def contrast(l1, l2): return (max(l1,l2)+0.05)/(min(l1,l2)+0.05)
```

Eller bruk [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker) etter å ha konvertert OKLCH til hex via [oklch.com](https://oklch.com).

## Gap-skala forskjell web vs app (bevisst)

Tokens-web og tokens-app har ulik `--gap-component`-verdi. Dette er **bevisst**, ikke en bug:

| Token | Web | App | Begrunnelse |
|---|---|---|---|
| `--gap-tight` | `--space-2` (8px) | `--space-1` (4px) | App er info-tett, web har luft |
| `--gap-component` | `--space-5` (24px) | `--space-4` (16px) | Samme |
| `--gap-section` | `--space-8` (48px) | `--space-8` (48px) | Felles — seksjoner trenger luft uansett |

**Regel:** Hvis du henter en komponent fra ett rammeverk inn i det andre, bruker den de **semantiske** gap-tokens (`--gap-component`), så den justerer seg automatisk til konteksten. Du skal ikke hardkode `--space-N` i komponent-CSS når intent er "gap mellom komponenter".

Dokumentert som regel i [tokens-fellesregler-decision](../decisions/2026-05-27-tokens-fellesregler.md).

## Se også

- [Handoff for implementerings-agenter](../../handoff/README.md) — generisk konsum av rammeverket.
- [Decisions: to tokens-pakker](../decisions/2026-05-27-to-tokens-pakker.md)
- [Decisions: v2 hardening](../decisions/2026-05-27-v2-hardening.md) — arkitektur-modning (gråskala, triplets, a11y, spacing).
- [Decisions: v3 rebuilding](../decisions/2026-05-27-v3-rebuilding.md) — én dark-mekanisme, motion-system, mobil-nav, full --space-migrasjon.
- [Decisions: v3 polish & shippable](../decisions/2026-05-29-v3-polish-og-shippable.md) — info-triplet, localStorage, tokens-ekstraksjon, WCAG-måling.
- [Kanonisk CSS](../../visual/tokens/) — `tokens-web.css` og `tokens-app.css`, shippable.
