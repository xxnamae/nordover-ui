# Tokens — API og bygging

## Hva ligger her

- `tokens-app.css` — CSS-variable pakke for SaaS, dashboards (dark default)
- `tokens-web.css` — CSS-variable pakke for marketing-sites (light default)

Begge filer:
- Identisk `@layer`-arkitektur
- Identisk token-navn (no breaking between packages)
- Eneste forskjell: defaults (type-skala, spacing-tetthet, button-surface, theme-default)

## Bruksmodell

1. **Kopier en fil** til ditt prosjekt (velg app eller web basert på use-case)
2. **Importer før dine egne styles**
3. **Bruk token-variabler** i komponenter
4. **Synk ved behov** — WebFetch på nytt når du vil oppdatere

## CSS-arkitektur

Begge filer bruker Cascade Layers (`@layer`):

```css
@layer reset { /* ... Inter fallback, focus-visible, sr-only, prefers-reduced-motion ... */ }
@layer tokens { /* ... CSS custom properties: --space-*, --color-*, etc. ... */ }
@layer utilities { /* ... generic .animate-*, .sr-only, .stagger, etc. ... */ }
```

**Viktig:** Din egen CSS skal ligge **etter** disse lagene i import-rekkefølge:

```ts
// app/layout.tsx
import "./styles/nordover-tokens.css";  // @layer reset, tokens, utilities
import "./styles/brand.css";             // Din @layer brand (overstyringer)
import "./styles/components.css";       // Din egne komponenter
```

### Rekkefølgen sikrer

1. **Reset-laget** initialiserer globale defaults (ingen CLS, a11y built-in)
2. **Token-laget** definerer alle variabler
3. **Utilities-laget** gir generiske klasser (`.animate-*`, `.sr-only`)
4. **Brand-laget** kan overstyre token-verdier per prosjekt (f.eks. annen accent-farge)
5. **Component-laget** konsumerer brand-overstyringene

Kaskaden sikrer at brand alltid vinner uavhengig av CSS-filens internal rekkefølge.

## Header-kommentar (versjonering)

Toppen av filen inneholder:

```css
/* Nordover tokens-web v3 (2026-05-29) | commit: abc1234... | ... */
```

Ved senere oppdateringer:
1. WebFetch på nytt
2. Diff header-kommentaren
3. Les `../../../docs/wiki/decisions/` for endringer datert nyere enn din last commit
4. Overskriv filen og test visuelt (dark-mode, buttons, spacing)

## Token-katalog

Se `nordover-arkitektur.md` for full liste. Kort oversikt:

| Kategori | Eksempel | Bruk |
|---|---|---|
| Colors | `--color-accent`, `--gray-500` | Farger |
| Spacing | `--space-2`, `--space-8` | Padding, margin, gap |
| Typography | `--text-base`, `--text-lg` | Font-size + line-height |
| Radius | `--radius-sm`, `--radius-md` | border-radius |
| Shadows | `--shadow-sm`, `--shadow-lg` | box-shadow |
| Button surfaces | `--button-surface-bg-rest` | Komplette button-design |
| Motion | `--duration-fast`, `--ease-out` | Transitions, animations |

## Dark-mode

Mekanisme: `:root:has(#dark:checked) { /* dark overrides */ }`

I prosjektet:

```tsx
<input id="dark" type="checkbox" className="sr-only" defaultChecked={/* true for app, false for web */} />
```

Tokens-fila håndterer resten — ingen behov for `prefers-color-scheme` media queries (Nordover bytter via `:has()`).

## Prosjekt-spesifikke overstyringer

Lag `brand.css` i ditt prosjekt:

```css
@layer brand {
  :root {
    /* Overstyring av tokens */
    --color-accent: oklch(0.55 0.20 230);
    --neutral-h: 30;  /* Varme gråtoner i stedet for kjølige */
  }
  
  /* Dark-mode overstyringer */
  :root:has(#dark:checked) {
    --color-accent: oklch(0.65 0.20 230);
  }
}
```

**Viktig:** Aldri overstyr `--gray-*` direkte (bryter WCAG kontrast). Endre `--neutral-h` i stedet for å skifte tone på hele skalaen.

## Troubleshooting

| Problem | Årsak | Løsning |
|---|---|---|
| Fokusring mangler | Reset-laget lastet etter komponentene | Importer tokens-*.css først |
| Dark-mode bytter ikke | Checkbox-ID er feil | Sjekk at `id="dark"` på checkbox |
| Animasjoner fortsetter under `prefers-reduced-motion` | Tokens-fila har ikke reset-laget | Last nyeste versjon |
| Spacing ser annerledes ut | Token-navn varierer mellom pakker | Sjekk at du bruker samme pakke konsistent |

---

**Spørsmål?** Se `docs/handoff/README.md` eller åpne issue i `xxnamae/nordover-ui`.
