# ADR: Styleguide-strukturen skal være konstant — kun innhold bytter med pakke

- **Dato:** 2026-06-12
- **Status:** Vedtatt
- **Relatert:** `docs/visual/styleguide.html`, `docs/visual/styleguide-chrome.css`

## Kontekst

Styleguiden bruker en **enkelt HTML-fil** med JavaScript-basert pakkebytting som svitsjer
`tokens-web.css` ↔ `tokens-app.css` dynamisk. Det originale designet lot *hele siden*
ta på seg den valgte pakken — dvs. overskrifter, sidebar-spacing, typografi, og
component-demoene endret seg alt sammen når du byttet pakke.

Dette skaper et problem: det er vanskelig å isolere hva som faktisk er en *pakkespesifikk
byggesteinforskjell* vs. bare at dokumentasjonsstrukturen selv tegner seg annerledes.
Referanserammen beveger seg med innholdet.

## Beslutning

**Styleguide-strukturen (sidebar, overskrifter, typografi, spacing) forblir konstant i
app-designet. Kun komponent- og token-demoene reflekterer den byttet pakken.**

- `styleguide-chrome.css` definerer all side-struktur med faste verdier (ikke token-avhengig)
- Faste typografi-verdier: faste `font-size`, `font-weight` (ikke `var(--fw-*)`),
  for å sikre at headings/nav alltid renner samme vei
- Token-switsjen påvirker **kun** komponent-showcase og token-demoer, ikke chrome-skin
- App-designet blir referansedesignen (styleguiden er selv en "app-aktig" dokumentasjonsverktøy)

## Konsekvenser

- Demoene blir rent pakke-fokusert — leseren ser **bare** de spesifikke byggesteinene
  som endres mellom web og app
- Styleguiden som helhet forblir lesbar og stabil på tvers av begge pakker
- Implementeringen krever to typer CSS: chrome-token-verdier settes fast, komponent/token-showcase
  får svitsj-oppførselen på plass
