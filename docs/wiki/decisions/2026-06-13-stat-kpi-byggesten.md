# ADR: Stat/KPI-byggesten (`.stat`) — speilet i begge pakker

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/visual/components/components-app.css`, `docs/visual/components/components-web.css`, `docs/visual/styleguide.html`

## Kontekst

QA mot Linear og Stacked viste at begge bygger dashboards på en **KPI/metrikk-blokk**:
stort tabular-tall + dempet label + trend-delta med pil og farge («Total Revenue $156 392
↑18,2 %»). Nordover hadde **ingen** slik byggesten — `grep` for `.stat`/`.metric`/`.trend`
ga ingen treff. Et KPI-blokk er en klassisk, gjenbrukbar byggesten (ikke en ferdig
sidekomposisjon), så den hører hjemme i rammeverket.

## Beslutning

**Ny delt byggesten `.stat`** med subkomponenter og en responsiv gruppe:

- `.stat-group` — responsivt rutenett (`repeat(auto-fit, minmax(9rem, 1fr))`) for en rad KPI-er.
- `.stat` — vertikal blokk; `.stat-label` (dempet), `.stat-value` (stor, `--fw-semibold`,
  `tabular-nums`, `--tracking-display`), `.stat-trend`.
- `.stat-trend.is-up / .is-down / .is-flat` — semantisk farge (success/error/muted) og en
  ren-CSS pil-glyf via `--stat-arrow`-mask (opp som default, `is-down` roterer 180°, `is-flat`
  bytter til en strek). Tallene er `tabular-nums`.

**Speilet i begge pakker med identisk struktur.** Alle størrelser kommer fra tokens
(`--text-3xl`, `--text-xs`, `--fw-*`, `--tracking-display`) som er definert i begge pakker,
så blokken **adapterer automatisk**: tett/skarp i app, luftig/editorial i web (web bruker en
`clamp()`-basert `--text-3xl`). Verifisert i app-mørk og web-lys.

Bevisst valgt `--fw-semibold` (600, finnes i begge) framfor app-only `--fw-display-md`, så
den ikke faller tilbake til normal vekt i web.

## Konsekvenser

- Rammeverket dekker nå Linear/Stacked-dashboardenes mest brukte datablokk.
- Delt struktur → vedlikeholdes i begge `components-*.css` (jf. speilingsregelen). Ingen
  token-verdier endret, så ingen JSON-regenerering.
- Dokumentert i styleguiden under `#data-display` med eksempel som viser up/down/flat-trender.
