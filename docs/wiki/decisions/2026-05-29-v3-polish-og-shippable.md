# v3 Polish & shippable — siste meter til "10/10 fundament"

**Dato:** 2026-05-29
**Status:** Aktiv
**Forgjenger:** [2026-05-27 v3 Rebuilding](2026-05-27-v3-rebuilding.md)

**Kontekst:**
Etter ekstern audit av v3-systemet ble syv reelle hindringer mot "shippable verdensklasse" identifisert. Disse er ikke nye features — det er **siste meter med opprydding og kompletthet** før rammeverket kan brukes som fundament for alle Nordover-prosjekter.

---

## 1. Legacy visual-filer arkivert

**Problem:** `styleguide.html` (v1), `preview.html` (v1) og `preview-app.html` (v1) lå i `docs/visual/` ved siden av v3-filene, uten "deprecated"-merke. Risiko: noen åpner v1 først, kopierer `[data-theme="dark"]`-mønstre, bryter systemet.

**Tiltak:** Flyttet til `docs/visual/_archive/` med suffiks `-v1`. Egen `_archive/README.md` forklarer hvorfor og hva man skal bruke i stedet. `docs/index.md` peker ikke lenger til dem.

---

## 2. Decision-integritet gjenopprettet

**Problem:** `2026-05-27-v2-hardening.md` blandet v2 + v3 i én fil (post hoc-utvidelse). Brøt repoets prinsipp om at decisions er ett vedtak per fil.

**Tiltak:**
- v2-hardening trimmet ned til kun v2-innhold.
- v3-tillegget flyttet til ny fil [2026-05-27 v3 Rebuilding](2026-05-27-v3-rebuilding.md).
- v2 markert med "Status: Delvis superseded" + lenke til v3.
- README.md i `decisions/` utvidet med eksplisitt eksempel på supersede-mønster.

---

## 3. Semantiske triplets fullført

**Problem:** Web-styleguide manglet `--info`-triplet og hadde færre semantiske farger eksponert som swatches enn app-styleguide. Inkonsistens mellom pakker.

**Tiltak:** Web fikk full info-triplet (`--info`, `--info-subtle`, `--info-strong`) og swatches for alle 4 semantiske farger × 3 nivåer = 12 swatches.

---

## 4. localStorage tema-persistens

**Problem:** v3 brukte ren CSS via `:has(#dark:checked)` for tema-toggle. Ingen JS = ingen persistens. Hver reload nullet brukerens valg.

**Tiltak:** Minimal inline-script (`<script>` rett før `</body>`) som leser/skriver `nordover-theme` i localStorage og setter `checkbox.checked` ved load. ~12 linjer JS, ingen avhengigheter, fungerer ved `file://`.

**Avveining:** Bryter "ren CSS"-prinsippet fra v3-rebuilding, men UX-gevinsten er stor. Hvis konsument vil ha pure CSS, kan scriptet droppes.

---

## 5. Kanonisk CSS ekstrahert til standalone-filer

**Problem:** "Implementerings-sannheten" levde i HTML-styleguidene. Når noen skal bygge `@nordover/tokens-web` npm-pakken, må de copy-paste fra HTML — feilkilde og duplikering.

**Tiltak:** Opprettet `docs/visual/tokens/tokens-web.css` og `docs/visual/tokens/tokens-app.css` som rene, copy-paste-klare CSS-filer. `docs/visual/tokens/README.md` dokumenterer bygg-pakke-prosedyren.

**Avveining:** Skaper duplisering mellom styleguide-HTML og standalone-CSS. Akseptert fordi:
- Styleguidene er handoff-dokumenter (én fil, åpne i browser, se alt). De må være selvstendige.
- Standalone-CSS er shippable artefakt.
- Begge oppdateres samtidig når tokens endres (kan auto-genereres senere via build-script).

---

## 6. WCAG-kontrast målt og dokumentert

**Problem:** OKLCH-gråskalaen ble valgt på fingerspissfølelse. Ingen verifisering mot WCAG AA/AAA.

**Tiltak:** Kontrast-matrise lagt til i `nordover-arkitektur.md` for alle kritiske kombinasjoner (fg/bg, muted/bg, accent/bg, error/bg osv.) i både light og dark. Verdier beregnet via OKLCH → sRGB → relativ luminans.

**Resultat:** Alle hovedkombinasjoner ≥ WCAG AA (4.5:1 for body, 3:1 for store tekster). Muted-text marginalt — anbefalt kun for sekundær info, ikke kritisk innhold.

---

## 7. Eksplisitt "spec vs pakke"-status

**Problem:** "Nordover-rammeverk" var beskrevet som komplett, men eksisterer bare som markdown-spec + standalone styleguide-HTML. Ingen faktisk `npm install @nordover/tokens-web` ennå.

**Tiltak:** SYSTEM.md fikk ny "Rammeverk-status"-seksjon som klart skiller:
- ✅ Spec komplett (wiki + tokens.css)
- ✅ Handoff-styleguider rendret
- ⏳ npm-pakke ikke bygget i dette repoet (per CLAUDE.md: ingen produksjonskode her)
- 📍 Implementeres i `xxnamae/nordover` ved første reelle bruk (Omhu)

---

## Småfikser samtidig

- `elevation.md` linje ~143: byttet `[data-theme="dark"]`-referanse til `:has(#dark:checked)` med v3-merknad.
- `nordover-arkitektur.md`: lagt til seksjon som dokumenterer bevisst forskjell i `--gap-component` (web 1.5rem / app 1rem).
- `patterns-basis-batch2.md`: oppdatert `[data-theme]`-referanse til `:has(#dark:checked)`.
- Lagt til "Status: Aktiv" som standard på alle eksisterende decision-filer som mangler det.

---

## Konsekvenser

| Område | Før polish | Etter polish |
|---|---|---|
| **Visual-mappe** | 5 filer, blandet v1+v3 | 2 v3-styleguider + arkiv + tokens/ |
| **Decisions** | Én fil blandet v2+v3, ingen superseded-merkering | Atskilte filer, eksplisitt supersedes-kjede, status-felt på alle |
| **Triplets** | Web manglet info, inkonsistent med app | Fullt symmetrisk i begge |
| **Tema-persistens** | Resettes ved reload | Lagres i localStorage |
| **CSS-distribusjon** | Innelåst i HTML-styleguider | Standalone .css-filer klare for npm-pakke |
| **WCAG-validering** | Ikke målt | Matrise i wiki, alle ≥ AA |
| **Pakke-status** | Uklart om dette er shippable | Eksplisitt: spec ja, npm-pakke ikke i dette repoet |

**Reverseringskostnad:** Lav per item. Alle endringer er additive eller flytting; ingen API-brudd for konsumenter.

**Vurdering:** Etter denne iterasjonen er rammeverket reelt **10/10 fundament**. Neste naturlige steg er ikke "mer rammeverk" — det er å bruke det (Omhu).
