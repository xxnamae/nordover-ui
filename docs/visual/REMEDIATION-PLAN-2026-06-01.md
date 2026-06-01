# Nordover — Remedieringsplan (mot ekte 8+/10)

**Status:** UTKAST TIL GODKJENNING. Ingen koding før eier godkjenner.
**Grunnlag:** `AUDIT-2026-06-01-REALITY-CHECK.md` + `nordover-visuell-retning.md`
**Beslutninger fra eier (2026-06-01):**
- Web: **lys default + full dark-mode-paritet** (begge via tema-variant)
- App: behold mørk-først (Linear-modellen)

---

## Prinsipper som styrer all utførelse

- **Tokens er kontrakter:** verdiendringer speiles i begge token-filer i samme commit; navne-endringer krever ADR.
- **Styleguide-workflow:** CSS-endring + styleguide-oppdatering i samme commit.
- **Publiserte ADR-er er immutable:** reverseringer skrives som nye ADR-er.
- **Kirurgisk per fase:** hver fase er selvstendig, testbar, og commit-bar alene.

---

## Faseoversikt

| Fase | Tema | Prioritet | Estimat |
|------|------|-----------|---------|
| 0 | Token-kontrakt & arkitektur-integritet | P0 | M |
| 1 | Brand-lag (kjerneløftet) | P0 | M |
| 2 | Dedup & konsolidering | P0 | M |
| 3 | Responsiv korrekthet | P0 | L |
| 4 | Web dark-mode-paritet | P0 | L |
| 5 | Konsistens & kvalitet | P1 | M |
| 6 | Styleguide-autoritet | P1 | L |
| 7 | Multi-platform fundament | P2 | M |
| 8 | Visuelt løft mot referansenivå | P2 | L |

P0 = blokkerer visjonen. P1 = kvalitet/konsistens. P2 = differensiering/fremtid.

---

## Fase 0 — Token-kontrakt & arkitektur-integritet (P0)

**Mål:** `tokens-*.css` er eneste kilde til token-verdier. Ingen komponentfil overstyrer tokens.

1. Fjern `:root`-blokken i `components-web.css` `@layer primitives` (linje ~22–39) som redefinerer `--color-bg`, `--color-fg`, `--color-muted` m.fl. Verifiser at styleguiden fortsatt rendrer korrekt mot `tokens-web.css`.
2. Erstatt 29 hardkodede font-størrelser (0.65rem, 0.7rem …) med `var(--text-*)`. Der en verdi mangler i skalaen: legg til token, ikke hardkod.
3. Erstatt hardkodede `rgba(0,0,0,.5)` (modal-backdrop), `box-shadow`-literaler og `4px`-borders med eksisterende tokens (`color-mix`, `--shadow-*`, `--bw-*`).

**Akseptanse:** Et søk etter hex/rgba/px-literaler i komponentfiler gir kun bevisste unntak. Token-override fra komponentlag = 0.

---

## Fase 1 — Brand-lag (P0, innfrir kjerneløftet)

**Mål:** En ny kunde starter med KUN `clients/<slug>.css`.

1. Definer hvilke tokens som er **brand-overstyrbare** (farge-aksent, evt. font, radius-tone) vs. **låste** (spacing-grid, motion). Dokumenteres som kontrakt.
2. Opprett `docs/visual/clients/_template.css` + ett ekte eksempel (`docs/visual/clients/example.css`) som kun setter brand-tokens i `@layer brand`.
3. Lag `docs/handoff/brand-styling.md`: hvordan ta i bruk, hva som er trygt å overstyre, hva som brytes hvis man går utenfor.
4. ADR: `docs/wiki/decisions/2026-06-01-brand-lag-kontrakt.md`.

**Akseptanse:** Bytte av `example.css` endrer hele styleguidens merkevare uten å røre komponent-CSS.

---

## Fase 2 — Dedup & konsolidering (P0)

**Mål:** Én kanonisk definisjon per klasse.

1. Slå sammen til én definisjon: `.btn` (3→1), `.hero-centered` (4→1), `.pricing-grid` (5→1), `.feature-grid` (5→1), og øvrige Phase-1L-duplikater.
2. Fjern dobbel typografi-rolle-definisjon (primitives vs components) — behold tokens-baserte i primitives, fjern hardkodede i components.
3. Slett dødt CSS etter sammenslåing.

**Akseptanse:** Hver klasse defineres nøyaktig én gang. Visuell paritet før/etter verifiseres i styleguide.

---

## Fase 3 — Responsiv korrekthet (P0)

**Mål:** Korrekt på Mobile <480, Tablet 768–1024, Desktop >1024.

1. Innfør `--bp-mobile: 30rem (480px)` og bruk den; rett opp navnekollisjon (token-«desktop» = 768px vs visjon-«tablet» = 768px) via ADR.
2. Legg til tablet-mellomledd (2-kolonne) i 768–1024 for `feature-grid`, `pricing-grid`, footer.
3. Sett 44px som **default** min touch-target på alle interaktive elementer (`.btn`, `.btn-sm` via touch-area, ikon-knapper, checkboxes/radios, nav-items, pagination). `.btn-touch` blir overflødig.
4. `min()`-guard på alle `auto-fit`-grids: `minmax(min(16rem,100%),1fr)`.
5. Pakk tabeller i `.table-responsive`-wrapper som default; fjern den ugyldige `overflow-x:auto` direkte på `<table>`.
6. Revurder `.blog-card` rad-flip og `.cluster`-tvang under 768px (for aggressiv).

**Akseptanse:** Ingen horisontal scroll ned til 320px. Alle targets ≥44px. Tablet får 2-kolonne der relevant.

---

## Fase 4 — Web dark-mode-paritet (P0/P1, per eier-beslutning)

**Mål:** Web har full, WCAG-konform dark-mode som førsteklasses variant (lys forblir default).

1. Komplett dark-token-sett i `tokens-web.css` (`[data-theme="dark"]` / `prefers-color-scheme`), paritet med light.
2. Verifiser AA-kontrast i begge moduser (inkl. `--color-muted`, fokusring, badge/alert på subtle).
3. Reskaler skygger for mørk bakgrunn (som app allerede gjør).
4. Styleguide-web viser begge moduser eksplisitt.

**Akseptanse:** Toggle gir komplett, kontrast-konform mørk web. Ingen «glemt» komponent i mørk modus.

---

## Fase 5 — Konsistens & kvalitet (P1)

1. Harmoniser motion-tokens web/app (ADR + speilet verdiendring). Behold `prefers-reduced-motion`.
2. Én kanonisk `:focus-visible`; fjern `outline-offset:-2px`; legg WHCM-fallback (`outline` + `box-shadow`).
3. Erstatt `transition: all` med spesifikke properties. Fjern `bounceIn` (bryter nordisk min.).
4. Rett radius-progresjon (web `--radius-xl` 20px → 16px).
5. Dokumenter status/prioritet-farger med kontrast; konverter til OKLCH.

---

## Fase 6 — Styleguide-autoritet (P1)

1. Dokumenter de 50 (web) / 63 (app) manglende klassene med live-eksempler.
2. Fjern ~1559 inline `style=""` + `<style>`-blokker → kun rammeverk-klasser (CLAUDE.md-krav).
3. Speil web/app der relevant.

**Akseptanse:** Inline-stiler = 0. Klassedekning i styleguide = 100 %.

---

## Fase 7 — Multi-platform fundament (P2)

1. Token-eksport til JSON (Style Dictionary-kompatibel) som maskinlesbar kilde.
2. Dokumenter mapping-vei til iOS (SwiftUI) og Android (Material) — minst som spesifikasjon.

**Akseptanse:** `tokens.json` genereres fra CSS; native-mapping-vei er dokumentert.

---

## Fase 8 — Visuelt løft mot referansenivå (P2)

Basert på inspirasjon (Linear/Stacked/Off Menu):

1. Større, mer selvsikker display-type; strammere tracking på topp-grader.
2. Signatur: blandet font-vekt i én tittel (bold + lett kursiv).
3. Aksent-disiplin: reduser app-blå-overbruk; aksent kun til ett fokuspunkt.
4. «Stacked cards»-dybdemønster (Linear-widgets).
5. Data-viz-token-standard (chart-farger, gradient-barer på mørk).
6. Onboarding split-screen-pattern med dot-paginering.

---

## Rekkefølge & avhengigheter

```
Fase 0 → 1 → 2  (fundament, må komme først)
        ↓
Fase 3 (responsiv) ‖ Fase 4 (dark-web)  (kan parallelliseres etter 0–2)
        ↓
Fase 5 → 6  (konsistens, så styleguide-sannhet)
        ↓
Fase 7 ‖ 8  (fremtid/differensiering)
```

**Forventet resultat:** Fase 0–4 løfter til ekte ~7. Fase 5–6 til ekte ~8. Fase 7–8 mot 9+.

---

## Det jeg trenger fra eier nå

Godkjenning av: (a) faserekkefølgen, (b) at jeg kan opprette ADR-er for de to navnekollisjonene (breakpoint + motion), (c) om jeg skal kjøre P0 (Fase 0–3) samlet eller fase-for-fase med stopp for review mellom hver.
