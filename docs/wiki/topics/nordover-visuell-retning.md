# Nordover — Visuell retning (fra inspirasjon)

**Status:** Referansedokument, etablert 2026-06-01 fra kundeleverte inspirasjonskilder.
**Formål:** Konkretisere "nordisk minimalisme + Apple HIG" med faktiske visuelle referanser.

---

## Inspirasjonskilder (levert)

| Kilde | Type | Karakter |
|-------|------|----------|
| **Linear (app)** | App-UI | Mørk, tett, monokrom + diskré lilla/blå aksent. Rask. Tastatur-drevet. Ekstremt raffinert. |
| **Linear (marketing)** | Nettside | Mørk. Enorm display-type med blandet vekt (bold + lett kursiv). Logo-vegg. 3D-minimalistiske illustrasjoner. Generøs luft. |
| **Stacked** | Nettside | Mørk. Dristig display, dashboard-mockups, monokrom, minimal. |
| **Off Menu (O/M)** | Nettside | **Lys/hvit.** Ekstrem whitespace. Flytende sirkulære thumbnails. Blandet serif/sans display. Mest "nordisk" av alle. |
| **Linear onboarding** | App-flyt | Mørk. Split-screen: skjema venstre, showcase høyre. Dot-paginering. Minimal. |
| **Stacked widgets** | Dashboard | Mørk. Revenue-charts (gradient-barer), stat-cards, feed-tabeller, asset-lister, analytics. Monokrom + flerfarget data-viz. |
| **Linear widgets** | Produkt-UI | Mørk. Kommando-barer, issue-kort med status-ikoner, lagdelte kunde-kort med dybde/blur, lydbølge-konnektorer, tastatur-grid. |

---

## Felles DNA på tvers av alle kildene

Dette er kjernen i den visuelle retningen — gjelder uansett lys/mørk:

1. **Selvsikker, overdimensjonert typografi.** Store display-grader bærer komposisjonen. Få ord, mye vekt.
2. **Ekstrem tilbakeholdenhet.** Monokrom base. Aksent brukes nesten aldri — kun til ett fokuspunkt.
3. **Generøs whitespace.** Luft er et designelement, ikke tomrom.
4. **Raffinert mikro-detalj.** Subtile skygger, presise radier, rolig bevegelse.
5. **Innhold > chrome.** UI trekker seg tilbake; innholdet er helten.
6. **Hastighetsfølelse.** Snappy interaksjon (Linear-DNA), aldri treig.

---

## Plattform-retning

### App (SaaS) → Linear-modellen
- **Mørk-først.** Dette stemmer med dagens `tokens-app.css` (dark-first) — behold.
- Tett informasjonstetthet, kompakt spacing, 14px base.
- Monokrom gråskala + én diskré aksent (dagens blå er konvensjonell; vurder å nærme seg Linears mer dempede lilla/indigo).
- Rask bevegelse (100–150ms), tastatur-først, kommandopalett-tankegang.

### Web (editorial/marketing) → to gyldige spor
Inspirasjonen viser **både** mørk-dristig (Linear/Stacked) **og** lys-luftig (Off Menu). Begge er "modern minimal". Dette er en reell forgrening som påvirker token-defaults:

- **Spor A — Lys-luftig (Off Menu):** Hvit base, maksimal whitespace, blandet serif/sans, mest nordisk. Stemmer med dagens light-first `tokens-web.css`.
- **Spor B — Mørk-dristig (Linear/Stacked):** Mørk base, enorm display-type, dashboard-showcase, dramatisk.

> **Åpent valg:** Hvilket spor (eller begge via tema-variant) web skal default til, er ikke avgjort. Se beslutning i ADR når valgt.

---

## Konkrete løft mot referansenivå (gap i dag)

Basert på sammenligning mellom inspirasjon og nåværende styleguides:

- **Display-typografi:** Inspirasjonen går større og mer selvsikkert enn dagens web-hero. Vurder å øke topp-grad og stramme tracking ytterligere.
- **Blandet font-vekt i én tittel** (Linear-mønster: bold + lett kursiv) finnes ikke i dag — kandidat for et signatur-grep.
- **Aksent-disiplin:** App bruker konvensjonell blå overalt; referansene bruker aksent langt mer sparsomt.
- **3D/illustrasjon-språk:** Referansene bruker subtile, monokrome 3D-objekter som signatur. Nordover har ingen illustrasjonsstandard.
- **Onboarding-mønster** (split-screen, dot-paginering) finnes ikke som dokumentert pattern.
- **Data-viz:** Stacked-widgetene viser revenue-charts med gradient-barer på mørk. Nordover har ingen chart/data-viz-token-standard.
- **Lagdelte kort med dybde:** Linear-widgetene stabler kunde-kort med blur/dybde. Dagens `.card`/elevation er flatere — vurder et "stacked cards"-mønster.

---

## Se også

- [Visjon](nordover-visjon.md)
- [Farger](nordover-colors.md) · [Typografi](nordover-typografi.md) · [Bevegelse](nordover-motion.md)
- [Reality-Check Audit](../../visual/AUDIT-2026-06-01-REALITY-CHECK.md)
