# Elevation / shadows

Skyggesystem + flat-elevation (borders) + hover-lift-pattern. Bygger på `--shadow-*`-tokens og introduserer border-tokens og lift-tokens.

Filosofien er **Scandi-min editorial**: shadows er subtilere enn industristandard, og borders er en likeverdig "flat" elevation-strategi — ikke alt skal flyte.

Se [decision 2026-05-27 — elevation-arkitektur](../decisions/2026-05-27-elevation-arkitektur.md).

## Skala — fem nivåer + inset

Tokens lagt til `@theme` i begge token-pakker. Genererer `shadow-xs`/`sm`/`md`/`lg`/`xl`/`inset` Tailwind-utilities.

**tokens-web (Scandi-min editorial):**
```css
--shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.04);
--shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.04);
--shadow-md: 0 4px 8px -2px rgb(0 0 0 / 0.08), 0 2px 4px -2px rgb(0 0 0 / 0.05);
--shadow-lg: 0 12px 20px -4px rgb(0 0 0 / 0.1), 0 6px 8px -4px rgb(0 0 0 / 0.06);
--shadow-xl: 0 24px 40px -8px rgb(0 0 0 / 0.12), 0 10px 16px -8px rgb(0 0 0 / 0.08);
--shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.06);
```

**tokens-app (enda tettere, SaaS-info-tetthet):**
```css
--shadow-xs: 0 1px 1px 0 rgb(0 0 0 / 0.03);
--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.04), 0 1px 1px -1px rgb(0 0 0 / 0.03);
--shadow-md: 0 2px 4px -1px rgb(0 0 0 / 0.06), 0 1px 2px -1px rgb(0 0 0 / 0.04);
--shadow-lg: 0 8px 12px -3px rgb(0 0 0 / 0.08), 0 3px 5px -3px rgb(0 0 0 / 0.06);
--shadow-xl: 0 16px 24px -6px rgb(0 0 0 / 0.1), 0 6px 10px -6px rgb(0 0 0 / 0.07);
--shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.05);
```

**Begge bruker multi-layer shadows** (ambient + key) for mer realistisk dybde enn enkelt-shadow.

## Semantiske aliaser

På toppen av t-shirt-navnene. Komponenter foretrekker disse:

```css
--shadow-inset: inset 0 1px 2px 0 rgb(0 0 0 / 0.06);  /* primitiv — web; app 0.05 */
--shadow-tooltip: var(--shadow-sm);
--shadow-popover: var(--shadow-md);
--shadow-modal: var(--shadow-lg);
--shadow-drawer: var(--shadow-xl);
--shadow-card-hover: var(--shadow-md);
```

`--shadow-inset` er en egen primitiv (ikke et alias) — verdien deepens i dark mode (alpha 0.3). De øvrige aliaser elevation-skalaen og arver dermed dark-mode-redefineringene automatisk.

**Hvorfor begge lag:** t-shirt-skala er primitiv (mappes til Tailwind-utility), semantisk gir kontekst. Brand kan endre `--shadow-modal` uten å rotere alle `--shadow-lg`-bruk.

## Border-tokens — flat elevation

I Scandi-min editorial er borders ofte riktigere enn shadows. Et kort med tynn border ser mer "norsk" ut enn ett med drop-shadow.

Lagt til `:root` i begge token-pakker (samme verdier). Bredde-primitivene heter `--bw-*` (ikke `--border-width-*`):

```css
--bw-hairline: 0.5px;     /* Luksuriøst på retina, snaps til 1px på lavoppløst */
--bw-thin: 1px;           /* Standard */
--bw-medium: 2px;         /* Vekt, fremheving (også brukt av fokus-outline) */

--border-card: var(--bw-thin) solid var(--color-border);
--border-divider: var(--bw-thin) solid var(--color-border);
```

> Det finnes kun to ferdig-komponerte border-shorthands i tokens: `--border-card` og `--border-divider`. Inputs og fokus-ringer komponeres direkte fra `--bw-*` i komponent-CSS (fokus-outline bruker f.eks. `var(--bw-medium) solid var(--color-focus)`), ikke via egne `--border-input`/`--border-focus`-tokens.

Brand kan overstyre til hairline for ekstra editorial:
```css
/* clients/<brand>.css */
:root {
  --border-card: var(--bw-hairline) solid var(--color-border);
}
```

## Hover-lift — `@utility` + customizable tokens

Lift-tokens i `:root`:

**tokens-web:**
```css
--lift-distance: -2px;
--lift-shadow-from: var(--shadow-xs);
--lift-shadow-to: var(--shadow-md);
```

**tokens-app (mindre dramatisk):**
```css
--lift-distance: -1px;
--lift-shadow-from: var(--shadow-xs);
--lift-shadow-to: var(--shadow-sm);
```

`@utility`-definisjon (i `elevation.css` eller tilsvarende):

```css
@utility hover-lift {
  transition: transform var(--duration-base) var(--ease-out),
              box-shadow var(--duration-base) var(--ease-out);
  box-shadow: var(--lift-shadow-from);
  will-change: transform;

  &:hover {
    transform: translateY(var(--lift-distance));
    box-shadow: var(--lift-shadow-to);
  }
}
```

**Bruk:**
```html
<a class="hover-lift" href="/artikkel">
  <article>...</article>
</a>
```

**Brand-overstyringer:**
```css
/* Mer dramatisk løft */
:root { --lift-distance: -4px; --lift-shadow-to: var(--shadow-lg); }

/* Slå av løft helt */
:root { --lift-distance: 0; --lift-shadow-to: var(--lift-shadow-from); }
```

`prefers-reduced-motion` nuller ut `--duration-base` på rotnivå — hover-lift mister animasjon automatisk for brukere som ber om det.

## Bruksmønster — når bruke hva

| Situasjon | Verktøy |
|---|---|
| Kort i liste/grid med lignende kort | `border-card` (flat) |
| Kort som er klikkbart | `border-card` + `hover-lift` |
| Dropdown-meny, popover | `shadow-popover` |
| Modal | `shadow-modal` + overlay |
| Drawer (side-panel) | `shadow-drawer` |
| Tooltip | `shadow-tooltip` |
| Trykt knapp, focused input | `shadow-inset` |
| Skille mellom seksjoner | `border-divider` |
| Eyebrow / "luksuriøs" kort | hairline-border overstyring |

**Tommelregel:** flytende UI (popovers, modaler, tooltips) bruker shadows. Innholds-grupperinger (kort, paneler, seksjoner) starter med borders. Hover-states kan introdusere shadow.

## Surface-elevation — tonal elevation (Material 3-mønster)

I tillegg til shadows og borders finnes en **surface-elevation-skala** `--surface-1..5`. I dark mode lysner overflaten progressivt med høyden (Material 3 tonal elevation) — et høyere element får en lysere bakgrunn i stedet for å lene seg utelukkende på skygge, som er svak mot mørk bakgrunn.

**tokens-web — light (alle nivåer holder seg nær-hvitt/subtilt):**
```css
--surface-1: var(--color-surface);
--surface-2: var(--gray-50);
--surface-3: var(--gray-100);
--surface-4: var(--color-surface);
--surface-5: var(--color-surface);
```

**tokens-web — dark (lysner progressivt fra gray-900):**
```css
--surface-1: var(--gray-900);                               /* base */
--surface-2: oklch(0.17 var(--neutral-c) var(--neutral-h)); /* kort */
--surface-3: oklch(0.21 var(--neutral-c) var(--neutral-h)); /* popover/dropdown */
--surface-4: oklch(0.24 var(--neutral-c) var(--neutral-h)); /* modal/drawer */
--surface-5: oklch(0.27 var(--neutral-c) var(--neutral-h)); /* topp-sheet */
```

`tokens-app` bruker identiske verdier for `--surface-1..5` (mirrored).

**Nivå-mapping:**

| Token | Høyde | Typisk bruk |
|---|---|---|
| `--surface-1` | base | sidebakgrunn / grunnflate |
| `--surface-2` | lav | kort |
| `--surface-3` | middels | popover, dropdown |
| `--surface-4` | høy | modal, drawer |
| `--surface-5` | topp | sheet på toppen av alt |

`--color-surface` forblir en egen kontrakt; `--surface-*` er additivt. I light mode er nivåene visuelt nesten like (Scandi-min holder lyst flatt) — det er i dark mode tonal elevation gjør jobben.

## Dark mode

Shadow-verdiene overstyres i `:root:has(#dark:checked)` med høyere alpha (0.25-0.7 i stedet for 0.03-0.12) for å være synlige mot mørk bakgrunn. Allerede inkludert i tokens-spec. *(Merknad: v1-spec brukte `[data-theme="dark"]` — reversert av [v3 Rebuilding](../decisions/2026-05-27-v3-rebuilding.md).)*

I dark mode kombineres dette med tonal **surface-elevation** (se over): høyere elementer får lysere bakgrunn via `--surface-2..5`, ikke bare sterkere skygge.

**Border-tokens trenger ikke override** — de bruker `--color-border` som allerede skifter i dark mode.

## Hva utelater vi bevisst

- **Color-tintede shadows** (eks. shadows i brand-farge): kan komplekse opp uten klart visuelt gevinst. Vurder per prosjekt hvis brand krever det.
- **Layered z-axis-skygger med blur og spread** (Material-stil): for visuelt støyende for Scandi-min.
- **Glow-effekter**: ikke en del av husstilen. Brand kan introdusere per prosjekt.

## Implementeringsrekkefølge

1. Patch shadow-skala i `tokens-web.css` og `tokens-app.css` (utvid til xs/sm/md/lg/xl + inset, oppdater dark mode).
2. Legg til semantiske shadow-aliaser i `@theme` i begge pakker.
3. Legg til border-tokens og lift-tokens i `:root` i begge pakker.
4. Lag `elevation.css` med `@utility hover-lift`-blokken (kan også legges i `interaction.css` hvis vi får flere interaksjons-utilities senere).
5. Import-rekkefølge per app: `tokens-*.css` → `base.css` → `typografi.css` → `layout.css` → `elevation.css` → `prose.css` → `clients/<slug>.css`.

## Se også

- [Nordover-arkitektur — tokens](nordover-arkitektur.md)
- [Nordover-layout](nordover-layout.md)
- [Decision: elevation-arkitektur](../decisions/2026-05-27-elevation-arkitektur.md)
