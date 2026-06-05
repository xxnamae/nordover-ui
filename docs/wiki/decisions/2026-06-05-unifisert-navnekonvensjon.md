# Unifisert navnekonvensjon (Nordover v2.0)

**Dato:** 2026-06-05
**Status:** Vurdert (til godkjenning — IKKE implementert ennå)
**Forgjenger:** [2026-06-04 Komponent-kontrakt-paritet](2026-06-04-komponent-kontrakt-paritet.md)

**Kontekst:**

Systemet er ennå ikke tatt i bruk av noen nedstrøms-forbruker. Det gir et engangsvindu til å rense opp navne-inkonsistenser **fullstendig** uten migrasjonssmerte eller deprecation-bagasje. En kvalitetsgjennomgang (benchmarket mot Material 3, Apple HIG, SMACSS) avdekket fire inkonsistenser:

1. **To parallelle table-systemer** (`.table*` og `.data-table*`) med overlappende ansvar.
2. **Blandede state-konvensjoner** (`.is-error` vs bare `.active`/`.open`/`.selected`/...).
3. **Splittet semantisk vokabular** (`.btn-destructive` vs `error` overalt ellers).
4. **Styleguide-chrome i shippable CSS** (`.doc-*`, `.swatch*`, `.chip*` i `components-web.css`).

**Alternativer:**
- A) Additivt med deprecering (behold gamle navn som aliaser)
- B) Full breaking opprydning (ingen forbrukere → ingen smerte)
- C) Kun dokumentér mønstrene

**Valgt: B) Full breaking opprydning.** Siden ingen avhengigheter finnes, gir aliaser kun støy. Vi lander på ett rent, forutsigbart system nå.

---

## Konvensjonen

### Kjerneregler
1. **Komponent-først, kebab-case:** `.komponent`, `.komponent-element`, `.komponent-variant`
2. **States via `.is-*`** (SMACSS) — frakoblet komponentnavn, JS-toggle-vennlig
3. **Størrelsesskala:** `-xs / -sm / (default uten suffiks) / -lg / -xl`
4. **Semantisk status — ÉN vokabular overalt:** `success / warning / error / info`
5. **`.t-*`** = semantisk typografi-navnerom (display/heading/body), distinkt fra `.text-*` utilities (alignment/color). Beholdes.
6. **Styleguide-chrome hører i `styleguide-chrome.css`**, aldri i shippable komponent-CSS.

### 1. State-klasser → alle `.is-*`

| Gammelt | Nytt | Merknad |
|---------|------|---------|
| `.active` | `.is-active` | nav, pagination, stepper |
| `.open` | `.is-open` | accordion, dropdown, calendar |
| `.selected` | `.is-selected` | data-rad, dag |
| `.dragover` | `.is-dragover` | file-upload |
| `.completed` | `.is-completed` | stepper |
| `.sort-asc` / `.sort-desc` | `[aria-sort="ascending\|descending"]` | bruk ARIA — best practice, gratis a11y |
| `.sortable` | `.sortable` (beholdt) | strukturell evne, ikke state |
| `.is-error` / `.is-success` | beholdt | allerede korrekt; legg til `.is-warning` ved behov |

Native states (`:disabled`, `:checked`, `:hover`, `:focus-visible`) brukes der de finnes — ingen `.disabled`-klasse for form-elementer.

### 2. Ett table-system (`.table` + opt-in modifiers)

`.data-table*` smelter inn i `.table*`. Sluttbilde:

| Gammelt | Nytt |
|---------|------|
| `.data-table` (base) | slå sammen inn i `.table` |
| `.data-table-zebra` | `.table-zebra` |
| `.data-table-cell-numeric` | `.table-numeric` |
| `.data-table-inline-edit` | `.table-inline-edit` |
| `.data-table-filter` | `.table-filter` (finnes alt — merge) |
| `.table-sort` | utgår → `th.sortable` + `[aria-sort]` |
| `.table-responsive` | beholdt |
| (ny) | `.table-sticky` — opt-in sticky header (var implisitt i data-table) |

Én `.table` med komponerbare modifiers: `.table-zebra`, `.table-sticky`, `.table-numeric`, `.table-responsive`, `.table-inline-edit`, `.table-filter`.

### 3. Semantisk vokabular → `error` overalt

| Gammelt | Nytt | Begrunnelse |
|---------|------|-------------|
| `.btn-destructive` | `.btn-error` | Status-ordet er alltid `error` (jf. `.alert-error`, `.badge-error`, `.toast-error`, `.text-error`). Full forutsigbarhet for agenter: «farge-status = alltid `error`». |

*Tradeoff:* Apple HIG kaller dette «destructive» og Bootstrap «danger». Vi velger intern konsistens (ett ord) over å matche ett eksternt system. Dette er det ene punktet verdt å bekrefte eksplisitt.

### 4. Variant-vokabular (tags)

`.tag-solid` / `.tag-outline` beskriver *fyll-stil* (en egen akse fra semantikk) og beholdes, men dokumenteres som en bevisst separat akse. Semantiske tag-farger følger status-vokabularet: `.tag-success` osv.

### 5. Chrome ut av shippable CSS

Flytt fra `components-web.css` → `styleguide-chrome.css`:
`.doc-section*`, `.doc-hero*`, `.doc-sub`, `.doc-demo`, `.swatch*`, `.chip`, `.chips`, `.component-grid`, `.state-item`, `.props-table` (og evt. andre styleguide-interne).

---

**Konsekvenser:**
- Breaking, men null forbrukere → ingen migrasjon nødvendig. Major-bump til **2.0.0**.
- Endringer speiles i begge pakker (`components-{web,app}.css`) i samme commit, JSON regenereres, styleguide + `index.html` + `docs/handoff/` oppdateres.
- ARIA-basert sortering gir gratis tilgjengelighetsgevinst.
- Etter dette: ett predikerbart system agenter kan stole på.

**Reverseringskostnad:** Lav (ingen forbrukere).
