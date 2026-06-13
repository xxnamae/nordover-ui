# ADR: Bolk 5 — Komposisjonsbevis i eksempel-filene

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/examples/marketing-landing.html`, `docs/examples/saas-dashboard.html`
- **Bygger på:** `2026-06-13-web-palett-og-editorial-blokker.md` (Bolk 4), `2026-06-13-status-priority-indicators.md` (Bolk 1)

## Kontekst

Bolk 1–4 la til totalt 30+ nye klasser fordelt på to pakker (app og web). Uten et levende bevis
på komposabilitet risikerer vi at byggesteinene oppfattes som isolerte atomer fremfor et sammenhengende
designsystem. Bolk 5 sin hensikt er å demonstrere at alle Bolk 1–4-komponentene **faktisk komponerer
inn i realistiske sideskall** — uten tilleggskode, uten CSS-overrides på rammeverksnivå.

Eksempel-filene er **ikke shippbare**: de representerer en per-prosjekt komposisjon som skal inspirere
implementatorer, ikke en side som rammeverket eier.

## Beslutning

### 1. `marketing-landing.html` — web editorial-pakken

Eksisterende fil ble oppgradert med Bolk 4-byggesteinene:

- **`.btn-pill`** på alle CTAer (nav «Kom i gang», hero «Start gratis» og «Se funksjoner», CTA-boks
  «Start gratis nå»). Erstatter rektangulære knapper med den editoriale pill-profilen.
- **`.crosshair-lg`** flankerer hero-eyebrow — Off Menu registreringsmerke-estetikk.
- **Prinsipp-seksjon** (`#principles`) med `.frame-crosshair` som ytre ramme og `.numbered-list`
  med fire prinsipp-rader (01–04). Demonstrerer kombinasjonen av crosshair-frame + numbered rows
  slik ADR-en for Bolk 4 beskrev som tiltenkt bruk.

### 2. `saas-dashboard.html` → omskrevet til Issue-tracker (app-pakken)

Komplett omskriving fra generisk KPI-dashbord til en Linear-inspirert issue-tracker:

- **⌘K Command bar** (`#cmd-overlay`, `.command-bar-overlay`) — åpnes med `⌘K` eller søke-knapp
  i topbar. Viser siste oppgaver med `.status-dot` og `.priority-indicator`, pluss kommandosnarveier.
- **`.filter-bar`** med aktive `.filter-chip.is-active` for «Pågår» og «Kritisk», med
  fjern-knapper. Demonstrerer filter-bar i kombinasjon med aktive chip-tilstander.
- **Issue-liste** — 8 issues gruppert etter status (Pågår / Todo / Ferdig / Kansellert).
  Hver rad bruker `.list-row` + `.list-row-check` + `.list-row-status` + `.list-row-body` +
  `.list-row-aside` (`.label-dot-group` + `.priority-indicator`) + `.list-row-actions`.
- **Detalj-panel** (desktop ≥1024px, skjult på mobil/nettbrett via CSS):
  - `.field-row` × 6 (Status, Prioritet, Tildelt, Prosjekt, Frist, Etiketter)
  - `.activity-feed` × 3 hendelser med fargede avatar-initialer
  - `.comment-composer` med integrert `.toolbar` (B / I / ⌘ / @) og `.comment-composer-footer`
  - `.attachment` (FIG-fil)

### 3. Responsivt oppsett

| Breakpoint | Marketing | Issue-tracker |
|---|---|---|
| Mobil <480px | Enkeltkolonne, pill-knapper stacker, principles full bredde | Liste kun, aside skjult, hamburger synlig |
| Nettbrett 768–1024px | To-kolonne feature-kort, prisliste stacker | Sidebar synlig, ett-kolonne liste, detalj skjult |
| Desktop >1024px | Full tre-kolonne prisliste, frame-crosshair principles | To-kolonne split: liste (1fr) + detalj (22rem) |

Mørk modus virker parametrisk i begge filer via `#dark`-checkbox — ingen ekstra overrides.

## Konsekvenser

- Ingen nye CSS-klasser i rammeverket — all ny CSS er i `<style>`-blokker med `ex-`-prefix
  (per-prosjekt navnerom).
- Demonstrerer komposabilitet: 11 rammeverksprimitivar komponerer til en fullstendig SaaS-flyt
  uten én linje rammeverk-CSS som måtte endres.
- Bekrefter at `.command-bar-overlay.is-open` + JS `classList.add()` er den korrekte mekanismen
  for overlay-åpning (ingen CSS-only hack).
- Bolk 5 er siste bolk i den planlagte migrasjonssesjonen. Neste steg er Elementor JSON-verifisering
  og eventuelle Bolk 6-byggesteiner (accordion, tabs, modal).
