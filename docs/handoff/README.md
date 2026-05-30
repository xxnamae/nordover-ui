# Nordover — handoff for implementerings-agenter

> **Du som leser dette:** Du er en Claude Code-agent (eller utvikler) som skal bruke **Nordover-rammeverket** i et prosjekt. Denne fila er din kanoniske inngang. Den er **produkt-agnostisk** — den forklarer hvordan rammeverket konsumeres, ikke hva du skal bygge med det. Det vet du allerede.

## Hvordan du leser rammeverket (uansett hvor du jobber)

`xxnamae/nordover-ui` er et **public** GitHub-repo (MIT-lisensiert). Du trenger ingen MCP-tilgang, ingen clone, ingen scope-utvidelse. Bruk innebygd `WebFetch` mot raw-URL-er:

| Fil | URL |
|---|---|
| Denne fila (handoff) | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/handoff/README.md` |
| Monorepo-bootstrap | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/handoff/monorepo-bootstrap.md` |
| Tokens-app CSS | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-app.css` |
| Components-app CSS | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-app.css` |
| Tokens-web CSS | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css` |
| Components-web CSS | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css` |
| Wiki-topics | `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/wiki/topics/nordover-<navn>.md` |

**Modell:** Les wiki on-demand via `WebFetch`. **Kopier tokens + components CSS-en** inn i prosjektet (to filer, ~50KB totalt). Aldri kopier wikien lokalt — den drifter ut av sync.

---

## 1. Hva Nordover er (kort)

Nordover er et CSS-fundament + et katalogisert pattern-bibliotek. Det leverer:

- **Tokens** (`@layer tokens`) — alle CSS-variabler for type, farger, spacing, radius, shadow, motion, button-surface, input. Ligger i `tokens-{web,app}.css`.
- **Reset** (`@layer reset`) — Inter-fallback med `size-adjust` (null CLS), `prefers-reduced-motion`-garanti, box-sizing. Ligger i `tokens-{web,app}.css`.
- **Komponenter** (`@layer primitives, components, utilities`) — buttons, forms, data tables, modals, cards, etc. Ligger i `components-{web,app}.css`.
- **Universell a11y** — global `:focus-visible`, `.sr-only`, motion-respekt.
- **Motion-system** — keyframes + animation utilities + transition utils. Fullt tilgjengelig i `components-{web,app}.css`.
- **Mønstre & spesifikasjon** — dyp dokumentasjon i wiki for arkitektur, design decisions, og use cases.

Det finnes **to pakker** med samme arkitektur, ulike defaults:

| Pakke | Bruksområde | Body-base | Type-skala | Knapper | Tema-default |
|---|---|---|---|---|---|
| `tokens-web` | Marketing-nettsider, landingssider, editorial | 16px | Fluid clamp xs → 8xl (opp til 160px) | Flate (elevated som opt-in) | Light |
| `tokens-app` | SaaS-grensesnitt, dashboards, arbeidsverktøy | 14px | Statisk 2xs → 5xl | Tactile (gradient + inset) | Dark |

**Velg én** basert på prosjektet. Begge har identisk `@layer`-arkitektur, identisk OKLCH-gråskala-mønster, identisk a11y-garanti, identisk motion-system. Forskjellen er kun defaults (type, spacing-tetthet, button-surface, accent).

Hvis du er i tvil: bygger du noe **du leser** (artikler, info, presentasjon) → web. Bygger du noe **du jobber i** (skjermer, arbeidsflyt, data) → app.

---

## 2. Quick-start (5 steg)

### Steg 1: hent CSS-filene (to per plattform)

Rammeverket er to halvdeler som alltid lastes sammen: tokens FØRST, komponenter ETTER. Via `WebFetch` (anbefalt — null setup, alltid nyeste):

```
# For app-prosjekt:
WebFetch https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-app.css
→ skriv til styles/nordover-tokens.css

WebFetch https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-app.css
→ skriv til styles/nordover-components.css

# For nettside-prosjekt:
WebFetch https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-web.css
→ skriv til styles/nordover-tokens.css

WebFetch https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-web.css
→ skriv til styles/nordover-components.css
```

Header-kommentaren i CSS-filene inneholder commit-hash for sync-sporing.

### Steg 2: importér i app-entry

```ts
// app/layout.tsx
import "./styles/nordover-tokens.css";       // tokens + reset (FØRST)
import "./styles/nordover-components.css";    // primitives + components + utilities
import "./styles/brand.css";   // legges på TOPPEN av Nordover
```

### Steg 3: legg til theme-toggle

```tsx
<input id="dark" type="checkbox" className="sr-only" aria-label="Mørk modus" defaultChecked />
```

CSS-mekanisme: `:root:has(#dark:checked) { /* dark tokens */ }`

### Steg 4: bygg komponenter

Bruk token-variabler i CSS:

```css
.btn {
  padding: var(--space-3) var(--space-5);
  font-size: var(--text-base);
  border-radius: var(--button-radius);
  background: var(--button-surface-bg-rest);
}
```

### Steg 5: legg til Inter Variable

```html
<link rel="preconnect" href="https://rsms.me">
<link rel="stylesheet" href="https://rsms.me/inter/inter.css">
```

---

## 3. Full dokumentasjon

Se wiki-topics for detaljer:
- `nordover-arkitektur.md` — tokens-spec og WCAG-tabell
- `nordover-typografi.md` — font-vekter og headings
- `nordover-buttons.md` — button-varianter
- `nordover-forms.md` — input/select/checkbox
- `nordover-patterns-basis.md` — Tag, Badge, Avatar osv.
- `nordover-app-patterns.md` — Modal, Drawer, Toast osv.
- `nordover-section-patterns.md` — Hero, Feature, CTA osv.

---

## 4. Brand-overstyring

Definer brand-laget i ditt eget prosjekt:

```css
/* prosjekt/styles/brand.css */
@layer brand {
  :root {
    --color-accent: oklch(0.55 0.20 230);
    --neutral-h: 30;  /* varme gråtoner */
  }
}
```

**Regler:**
- Endre aldri `--gray-*` direkte (bryter kontrast). Endre `--neutral-h` i stedet.
- Aldri overstyr tokens på komponent-nivå.
- Kopier kun tokens-CSS-en — aldri hele wikien lokalt.

---

## 5. Tilbakemeldinger

Hvis du finner en bug eller trenger en pattern: lag issue i `xxnamae/nordover-ui`.

Lykke til. Bygg fint.
