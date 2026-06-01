# ADR: Brand-lag kontrakt (2026-06-01)

**Status:** Vedtatt  
**Signerare:** Design system owner  
**Datering:** 2026-06-01  
**Revidert:** —

---

## Kontekst

Nordover visjon #1: *Et nytt kundeprosjekt kan starte med kun et brand-lag (`clients/<slug>.css`) — ingen strukturell design nødvendig.*

Foreløpig har `clients/<slug>.css`-mekanismen ikke eksistert. Token-overstyring har vært ad-hoc og udokumentert. For å ivareta visjonen må vi etablere en kontrakt som definerer:

1. Hvilke tokens er **merkevaredrivet** (lov å overstyring per kunde)?
2. Hvilke er **arkitektur-løste** (break the system hvis du endrer dem)?

---

## Avgjørelse

Vi etablerer tre kategorier av tokens i `clients/<slug>.css`:

### ✅ BRAND-OVERSTYRBARE (anbefalt overstyring per kunde)

Disse tokens kan overstyres trygt i `@layer brand` uten å ødelegge systemets integritet:

| Token | Bruk | Typisk overstyring |
|-------|------|-------------------|
| `--color-accent` | Primær merkevarefarve | → kunde-blå, rødt, etc. |
| `--color-accent-hover` / `-active` | Aksent-tilstander | → deriverte via color-mix |
| `--font-display` | Merkevaretypografi (display) | → kunde-serif, andre displayfont |
| `--font-sans` | Sanserif fallback | → kunde-sans (sjeldent) |
| `--radius-md` / `-lg` | Merkevare-tone (avrunding) | → skarpt (2px) eller mykt (16px) |
| `--color-focus` | Fokus-ring (kan være merkevare) | → kunde-blå, etc. |

### 🔒 LÅSTE (kritisk — ikke oversty)

Disse tokens er arkitektur-kritiske. Endring bryter responsivitet, a11y eller spacing-grid:

| Token | Årsak |
|-------|-------|
| `--text-*` (font-size skala) | Fluid type og breakpoint-integritet |
| `--space-*` (spacing grid) | Responsiv spacing-harmoni |
| `--bp-*` (breakpoints) | Media query kontrakter; endring = design-brudd |
| `--gap-*` / `--spacing-section` | Komponenter baseres på disse |
| `--duration-*` (motion) | Takt-integritet across components |
| `--shadow-*` (elevation) | Dybde-hierarki |
| `--bw-*` (border-width) | Struktur-presisjon |

**Unntak:** Disse kan justeres i klientlaget for særlige behov (feks. kompakt vs romslig), men må dokumenteres som "non-standard" og testes:
- `--gap-component`, `--spacing-section` → bare smalere (≥50% original), aldri bredere
- `--page-padding` → adaptive til viewport, kan overstyres
- Farger: `--color-bg`, `--color-surface`, `--color-fg`, `--color-muted`, `--color-border` → kan justeres for tema-tilpassning, men må opprettholde WCAG AA kontrast

### ⚠️ FORSIKTIG-OVERSTYRBARE (sjelden, dokumenter årsak)

Kun hvis kunde har særlige behov:
- `--radius-*` (andre enn md/lg) → kan justeres
- `--shadow-*` → kan gjøres subtilere for light-first design
- `--color-{error,success,warning,info}` → kan tilpasses for merkevare-pallett
- `--chart-*` → kan justeres for dataviz konsistens

---

## Implementering

**Mekanisme:**
```css
/* clients/example.css · ren brand-layer */
@layer brand {
  :root {
    --color-accent: oklch(0.55 0.30 260); /* kunde-blå */
    --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);
    --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, white);
    --font-display: "Fraunces", serif;
    --radius-md: 2px; /* skarpt */
  }
  /* Kun merkevare-tokens. Ingen komponent-klasser. */
}
```

**Import-rekkefølge (klient-app):**
```css
@import "path/to/tokens-web.css";
@import "path/to/base.css";
@import "path/to/typografi.css";
/* ... all components ... */
@import "clients/<slug>.css"; /* siste — overstyrer tokens */
```

---

## Godkjenning av dette ADR etablerer

1. ✓ Brand-layer (`clients/<slug>.css`) som kanonisk mekanisme
2. ✓ Token-kategorisering: Brand-overstyrbare / Låste / Forsiktig-overstyrbare
3. ✓ Handoff-dokumentasjon `docs/handoff/brand-styling.md` blir normativ
4. ✓ Nye kunder starter med mal (`docs/visual/clients/_template.css`)

---

## Se også

- `docs/handoff/brand-styling.md` — praktisk guide for implementørmedlemmer
- `docs/visual/clients/_template.css` — mal
- `docs/visual/clients/example.css` — eksempel-implementering
