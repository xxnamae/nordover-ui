# ADR: Verdensklasse-løft — interaksjons-tokens, liquid glass, eksempel-lag og tema-generator

**Dato:** 2026-06-05 | **Status:** ACCEPTED | **Bygger på:** `nordover-benchmark-verdensklasse.md`, `2026-06-04-rammeverk-fokus-byggesteiner.md`, `2026-06-02-verdensklasse-token-oppgradering.md`

## Spørsmålet

Benchmarken mot Apple HIG, Material Design 3, Linear og Fluent 2 ga karakter 7,5/10 og pekte på fire systemiske gap. Eieren (CTO) ba om å lukke alle, og la til tre punkter som delvis reverserer tidligere beslutninger: ta inn **liquid glass**, og lever **ferdige sidekomposisjoner som eksempler**. Hvordan gjør vi dette uten å forråde verken Nordic-minimalismen eller byggestein-kontrakten?

## Beslutning

Fire additive løft. Ingen token- eller klassenavn fjernes; alt er nytt og bakoverkompatibelt.

### 1. Interaksjons-fundament-tokens (lukker gap 1–3 fra benchmarken)

Nye token-grupper speilet i `tokens-web.css` + `tokens-app.css`:

| Gruppe | Tokens | Stjålet fra |
|---|---|---|
| State-layers | `--state-hover/-focus/-pressed/-selected/-dragged` (6/10/12/14/18 %) + `--state-disabled-opacity` | Material 3 |
| Fokus-ring | `--focus-ring-width/-offset/-color/-halo` (to-tonet, WCAG 2.4.13-grad) | WCAG 2.2 + Sara Soueidan |
| Target-size | `--target-min` 24px (WCAG 2.5.8 AA) + `--target-comfortable` 44px (Apple) | WCAG 2.2 + HIG |
| Density | `--density` + `--density-control-height` + `.density-compact/-comfortable` | Linear |
| Bevegelse | `--ease-decelerate`/`--ease-accelerate` (M3-par) + `--motion-smooth/-snappy/-bouncy` | M3 + Apple |

`:focus-visible` (begge pakker) er nå token-drevet. Knapper/inputs bruker `max(--target-comfortable, --density-control-height)` for høyde. App beholder SaaS-tetthet (ingen tvungen 44px på desktop; touch sikret via mobil-query).

### 2. Liquid glass — raffinert, ikke maksimalt (reverserer benchmarkens «ikke stjel»)

`.glass-liquid` / `.glass-liquid-strong`: backdrop-blur + saturate, opplyst topp-kant, myk diagonal specular-sheen (som **bakgrunnslag**, ikke pseudo-element, så innhold aldri havner under). Nye tokens `--glass-highlight/-sheen/-depth-shadow`. Faller tilbake til solid flate under `prefers-reduced-transparency`. Brukes **sparsomt** på nøkkelflater — følger Apples eget råd. Bevarer roen; ingen refleksjon/refraksjon.

### 3. Eksempel-lag (`docs/examples/`) — oppfyller «revurder hvis» i ADR 2026-06-04

Ferdige sidekomposisjoner som **ikke-shippbart referanselag**, ikke kjerne-kontrakter. Dette er nøyaktig det forrige ADR åpnet for: «Flere prosjekter trenger identiske komposisjoner → eget valgfritt recipes-bibliotek, ikke kjerne-kontrakter.»

- `marketing-landing.html` (web), `saas-dashboard.html` (app)
- Lenker alltid de shippbare filene; komponerer kun eksisterende klasser
- Byggestein-kontrakten i `components-*.css` er **uendret** — laget forurenser ikke rammeverket

### 4. Tema-generator (`scripts/generate_theme.py`) — Linear-modellen

Tre innputt (nøytral hue/chroma + accent + contrast) → komplett `:root` lys/mørk-blokk på OKLCH. `contrast`-knappen styrer L-spredning, så tilgjengelighet er en genereringsinput. Output-only; rører aldri de kanoniske tokenene (CSS forblir sannhetskilde).

## Hvorfor dette ikke bryter visjonen

- **State-layers og target-size styrker roen og tilgjengeligheten** — færre tilfeldige hover-nyanser, garantert treffområde.
- **Liquid glass i raffinert form** er deference-dybde (Apple), ikke pynt.
- **Eksempel-laget er eksplisitt utenfor kontrakten** — byggestein-fokuset står.
- **Generatoren tjener visjonens kjernemål:** «minimer designtid på nye prosjekter».

## Hva vi fortsatt IKKE tar inn

Material You bakgrunnsfarge · Apple full glass-refleksjon/refraksjon · Fluent «Nudge»-halvtrinn (6/10px) · Linears sync-motor/Cmd-K · sidekomposisjoner *som kontrakter* (kun som eksempler).

## Konsekvenser

- Karakter-mål etter løftet: 9–10/10 på fundamentet. APCA-dobbeltspor (B4) og tone-basert kontrast-garanti (C2) gjenstår som oppfølging.
- Styleguide dokumenterer liquid glass + density; full state/focus/target-galleri følger.
- JSON regenerert; `check:tokens` grønn.

## Revurder hvis

- State-layer-opasitetene viser seg for sterke/svake i reell QA på tvers av de tre breakpointene.
- Eksempel-laget begynner å bli behandlet som kontrakt av konsumenter (da: tydeligere «ikke importer»-merking eller egen repo).
