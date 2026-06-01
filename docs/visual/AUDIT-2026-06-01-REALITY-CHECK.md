# Nordover — Reality-Check Audit (2026-06-01)

**Status:** Korrigerende revisjon. Tre uavhengige agenter, instruert til å være kritiske og sitere fil:linje.
**Erstatter:** `docs/AUDIT_2026_06_01_FINAL.md` (som hevdet "10.0/10 PERFECT" — den vurderingen var oppblåst og ikke etterprøvbar; se §0).

---

## §0 Om den forrige "10/10"-rapporten

Den tidligere auditen påsto 95.8 % CSS-dekning, "41 komponenter", og 10.0/10. Uavhengig opptelling reproduserer ikke disse tallene. "41 komponenter" har ingen metodikk; "95.8 %" er ikke reproduserbart. Denne rapporten er den nøkterne erstatningen. Lærdom: selv-rapporterte perfekt-scorer fra agenter må verifiseres mot fil:linje.

---

## §1 Samlet vurdering

| Dimensjon | Score | Kilde |
|-----------|-------|-------|
| System vs visjon | **4/10** | Audit A |
| Responsiv — Mobile <480px | **4/10** | Audit B |
| Responsiv — Tablet 768–1024px | **3/10** | Audit B |
| Responsiv — Desktop >1024px | **7/10** | Audit B |
| HIG/Material/Linear-compliance | **7.3/10** | Audit C |

**Helhet: ~5/10.** Et lovende, moderne fundament (OKLCH, `@layer`, semantiske tokens, `prefers-reduced-motion`) — men ikke et ferdig rammeverk. Kjerneløftet i visjonen er ikke innfridd, og det finnes reelle bugs.

---

## §2 Kritiske funn (blokkerer visjonen)

### 2.1 Brand-løftet er skadet
- `components-web.css` (linje 22–39) redefinerer `--color-bg`, `--color-fg`, `--color-muted` m.fl. i `@layer primitives`. Siden `primitives` kommer etter `tokens` i lag-rekkefølgen, **overstyrer komponentfilen token-verdiene fra `tokens-web.css`**. Tokens-som-kontrakt er brutt.
- Ingen `clients/<slug>.css`-mekanisme eksisterer (ingen fil, ingen mappe, ingen workflow). Suksesskriterium 1 i visjonen er ikke møtt.
- 29 hardkodede font-størrelser (0.65rem, 0.7rem, …) utenfor token-skalaen i `components-web.css`.

### 2.2 Multi-platform = 0 %
Rent CSS/web. Ingen Style Dictionary, ingen JSON-tokeneksport, ingen iOS/Android-mapping. "Multi-platform" er per nå kun en ambisjon i visjonsdokumentet.

### 2.3 Touch-targets under HIG (44px) overalt
- `.btn` web: ~36–38px. `.btn` app: ~29px. `.btn-sm` app: ~19px.
- `.hamburger`, `.theme-toggle`: 40×40px. `.app-sidebar-close`, `.mobile-nav-*`: 32×32px.
- Eneste 44px-konforme element er `.btn-touch` — som er opt-in, ikke default.

### 2.4 Manglende 480px-breakpoint + uhåndtert tablet
- Ingen `@media` treffer 480px. Minste er 576px (`36rem`). Hull 480–576px.
- Layout hopper fra 1-kolonne (mobil) rett til 3-kolonne ved 768px. Tablet-sonen (768–1024) får ingen 2-kolonne-mellomting.
- App-footer er fast 4-kolonne ned til 576px.

### 2.5 Grids som knekker + ugyldig tabell-overflow
- Phase 1L-mønstre (`feature-grid`, `pricing-grid`, `footer-3col/4col`) bruker `minmax(16rem, 1fr)` **uten** `min()`-guard → horisontal scroll under ~256–352px.
- `data-table` får `overflow-x: auto` direkte på `<table>` i mobil-query — dette fungerer ikke uten wrapper. Ekte bug.

### 2.6 Duplikate/inkonsistente definisjoner
- `.pricing-grid` og `.feature-grid`: 5 definisjoner hver. `.hero-centered`: 4 (ulike egenskaper). `.btn`: 3 (ulik padding). Siste vinner; resten er dødt, forvirrende CSS.
- Typografi-roller (`.t-display-lg` m.fl.) defineres både i `@layer primitives` og `@layer components` med **avvikende** font-weights.

### 2.7 Motion-token-navnekollisjon web vs app
| Token | Web | App |
|-------|-----|-----|
| `--duration-fast` | 150ms | 100ms |
| `--duration-base` | 250ms | 150ms |
| `--duration-slow` | 400ms | 250ms |
Samme navn, ulik verdi → uforutsigbar porting mellom plattformene.

### 2.8 Styleguide-autoritet brutt
- 50 (web) / 63 (app) CSS-klasser er ikke demonstrert i styleguide-HTML (testimonial-, timeline-, mobile-nav-, spinner-familiene m.fl.).
- ~1559 inline `style=""`-attributter + 4 `<style>`-blokker i styleguide-HTML — bryter CLAUDE.md-regelen "never re-embed component CSS".

---

## §3 Best-practice-funn (kvalitet, ikke blokkerende)

- **Fokus:** Fire ulike `:focus-visible`-implementeringer. `.app-nav-item` bruker `outline-offset: -2px` (innover — kan skjules). Form-inputs bruker `box-shadow`-glow uten Windows High Contrast-fallback.
- **Motion:** `transition: all` (anti-pattern, trigger layout-recalc). `--duration-slower: 600ms` for langt for UI. `bounceIn`-keyframe bryter nordisk minimalisme.
- **Farge:** `--color-muted` (L=0.50) på hvit ≈ 4.7:1 — akkurat på AA-grensen for liten tekst. Status/prioritet-farger i app er hardkodet hex uten kontrastdokumentasjon.
- **Radius:** web `--radius-xl: 20px` bryter progresjonen (8→12→20).

---

## §4 Hva som faktisk er bra

- OKLCH gjennomgående, lav-chroma kald gråskala (gjennomtenkt).
- `@layer`-arkitektur, `color-mix()` for semantiske subtle-varianter.
- `prefers-reduced-motion` aggressivt og korrekt implementert.
- Skygger fysisk troverdige, to-lags, lave opasiteter — nær Apple, passer nordisk minimalisme.
- Typografi-rollesystemet og negativ tracking på store grader (Apple-mønster) er riktig tenkt.
- Web/app radius- og spacing-differensiering (editorial vs SaaS-tetthet) er bevisst og fornuftig.

---

## §5 Prioritert vei videre (mot ekte 8+)

**P0 — integritet i fundamentet**
1. Fjern `:root`-redefinisjonen i `components-web.css` `@layer primitives`; la `tokens-*.css` eie alle token-verdier.
2. Etabler `clients/<slug>.css`-mekanisme + ett eksempel-brand + workflow-doc. Innfri kjerneløftet.
3. Dedupliser klassedefinisjoner (én kanonisk `.btn`, `.hero-centered`, `.pricing-grid`, `.feature-grid`).

**P0 — responsiv korrekthet**
4. Innfør 480px-breakpoint; legg til tablet-mellomledd (2-kol) i 768–1024.
5. Garantér 44px touch-targets som default på alle interaktive elementer.
6. `min()`-guard på alle `auto-fit`-grids; pakk tabeller i `.table-responsive`-wrapper.

**P1 — konsistens og kvalitet**
7. Harmoniser motion-token-verdier (eller dokumenter bevisst divergens eksplisitt).
8. Én kanonisk `:focus-visible`; fjern negativ offset; WHCM-fallback.
9. Erstatt `transition: all` med spesifikke properties; fjern `bounceIn`.
10. Dokumenter 100 % av klassene i styleguide; fjern inline-stiler.

---

*Tre agent-rapporter i full lengde ligger i sesjonsloggen. Denne filen er sammendraget.*
