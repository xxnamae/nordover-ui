# ADR: Linear-tonet nøytralpalett og blå-violett accent for app-pakken

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/visual/tokens/tokens-app.css`, `docs/visual/tokens/tokens-app.json`

## Kontekst

App-pakken (SaaS, mørk-tett) skal løftes til Linear-kvalitet. Linear bygger hele
flaten sin på en **kjølig, lett lilla-tonet nøytral gråskala** — bekreftet i deres egen
palett-dokumentasjon: «so many shades of grey with a purple hue … it plays nicely across
the app». Accent-fargen deres er en **blå-violett** (≈ `#5E6AD2`), mer blå og mindre mettet
enn vår tidligere violett.

Tidligere brukte app-pakken en tilnærmet nøytral gråskala (`--neutral-h: 250`,
`--neutral-c: 0.005`) og en mettet violett accent (`oklch(0.52 0.24 285)`). Tonen lå nær,
men ikke identisk med, Linear.

Token-arkitekturen er parametrisk: hele gråskalaen (`--gray-50` … `--gray-950`) og alle
surface-trinn (`--surface-1` … `--surface-5`) avledes fra `--neutral-h` og `--neutral-c`.
En toneendring er derfor en to-verdis endring som forplanter seg konsistent gjennom hele
pakken.

## Beslutning

**App-pakken får en kjølig, lilla-tonet nøytral og en Linear-tonet blå-violett accent.**

- **Nøytral:** `--neutral-h: 250 → 265`, `--neutral-c: 0.005 → 0.012`. Gir det
  karakteristiske kjølige/lilla stikket uten å bli en farget gråskala. L-aksen er uendret,
  så all WCAG AA-kontrast på nøytraler er bevart.
- **Accent (lys modus):** `oklch(0.52 0.24 285) → oklch(0.54 0.16 272)` — Linears hue og
  reduserte chroma. L holdes lavt nok til AA på lys bakgrunn.
- **Accent (mørk modus):** `oklch(0.62 0.26 285) → oklch(0.66 0.16 272)` — samme hue,
  oppløftet for kontrast på mørk bakgrunn (app-pakkens default-kontekst, der Linear lever).
- **Fokus:** følger accent-hue (272) med noe høyere chroma for synlighet.

**Accent forblir ett enkelt swappbart token.** Den nøytrale grunnmuren er kunde-agnostisk;
kunde-branding gjøres ved å bytte `--color-accent` alene, ikke ved å røre nøytralene.

**Web-pakken berøres ikke.** App og web er bevisst divergerende visuelle identiteter
(mørk/kjølig SaaS vs. lys editorial). Speilingsregelen gjelder delt *struktur* (spacing,
radius, type-skala), ikke pakke-spesifikke identitets-farger. Web-pakkens palett besluttes
i et eget ADR når web-sporet starter.

## Konsekvenser

- Alle app-surfaces (bg, kort, border, elevasjon) får umiddelbart den kjølige Linear-grunnen,
  uten endringer i komponent-CSS.
- DTCG-JSON (`tokens-app.json`) regenereres i samme commit (`npm run build:tokens`).
- WCAG AA verifiseres med `npm run check:contrast`; lys-modus-accent holdes med vilje litt
  mørkere enn Linears eksakte `#5E6AD2` der AA krever det — kontrast vinner over pixel-paritet
  (jf. CLAUDE.md: «WCAG compliance required»).
- Token-*navn* er uendret → ingen brytende kontraktsendring for konsumenter; kun verdier.
- Dette er Bolk 0 i Linear/Off Menu-løftet. Komponentlaget (primitiver, interaksjonsmønstre,
  composite-blokker) bygges i påfølgende bolker oppå denne foundationen.
