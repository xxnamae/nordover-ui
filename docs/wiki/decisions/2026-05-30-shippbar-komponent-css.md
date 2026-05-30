# Shippbar komponent-CSS skilt ut fra styleguidene

**Dato:** 2026-05-30
**Status:** Vedtatt
**Type:** Arkitektur / distribusjon

## Kontekst

`tokens-web.css` og `tokens-app.css` var deklarert som den kanoniske,
shippbare CSS-en (se CLAUDE.md). Men de fylte i praksis bare to av seks
`@layer`: `reset` og `tokens`. Lagene `primitives`, `components` og
`utilities` var deklarert, men tomme.

All komponent-CSS — `.btn`, `.hero-centered`, `.feature-grid`,
`.feature-card`, `.cta-card`, `.footer-grid`, `.theme-toggle`, de
semantiske `.t-*`-typeklassene, primitives som `.cluster`/`.stack`, og
hele app-komponentbiblioteket — lå **kun embedded i `<style>`-blokken**
i `styleguide-web.html` og `styleguide-app.html`.

Dette ga tre konkrete problemer:

1. **Halvt rammeverk shippet.** En konsument som importerte
   `tokens-web.css` fikk farger, fonter og spacing-variabler, men ingen
   knapper, grid eller section patterns. Ren HTML, GitHub Pages og
   Elementor hadde ingenting brukbart å konsumere.
2. **Duplisering uten sannhetskilde.** `.btn`, `.theme-toggle` m.fl. fantes
   i to kopier (web + app styleguide). Endring av en komponent krevde
   manuell synk to steder — i strid med «tokens er kontrakt»-disiplinen.
3. **Landingssiden traff veggen.** `index.html` lenket `tokens-web.css` og
   brukte komponentklasser som ikke fantes der → siden kollapset til rå
   browser-flow.

## Beslutning

Skill komponent-CSS ut i egne kanoniske, shippbare filer:

```
docs/visual/components/components-web.css   (primitives + components + utilities)
docs/visual/components/components-app.css
```

- **Konsumeres alltid sammen med tokens, i rekkefølge:**
  ```html
  <link rel="stylesheet" href=".../tokens/tokens-web.css">
  <link rel="stylesheet" href=".../components/components-web.css">
  ```
- **Styleguidene konsumerer nå disse filene** (lenker dem) i stedet for å
  embedde CSS. `styleguide-web.html` og `styleguide-app.html` er dermed
  ekte konsumenter, ikke sannhetskilder.
- **Sannhetskilde for komponenter = `components-{web,app}.css`.** Endringer
  gjøres der, aldri i styleguide-HTML.
- **Landingssiden konsumerer samme to filer** som styleguidene.

`@layer`-rekkefølgen (`tokens, reset, primitives, components, utilities,
brand`) deklareres i token-filene og re-deklareres idempotent i
komponent-filene, slik at kaskaden er forutsigbar uansett lastrekkefølge.

## Konsekvenser

- Rammeverket er nå konsumerbart for ren HTML, statiske sider og Elementor
  — ikke bare React-apper som bygger egne komponenter.
- Én sannhetskilde per komponent. Ingen dobbeltvedlikehold mellom
  styleguidene.
- Klassenavn er nå offentlige kontrakter på linje med token-navn:
  endring/fjerning er breaking og krever ny ADR + changelog.
- Synk til monorepoet utvides: kopier nå BÅDE token- og komponent-filer
  (se `docs/handoff/monorepo-bootstrap.md` § 5).
- Web- og app-komponentene speiles der strukturen er delt (samme prinsipp
  som token-mirroring), men avviker bevisst der uttrykket skiller seg
  (flate vs. taktile knapper, editorial vs. kompakt spacing).

## Reverserer

Delvis presisering av `2026-05-30-landingsside-design-system.md`:
landingssiden konsumerer fortsatt designsystemet, men nå via de uttrekte
komponent-filene i stedet for å forutsette komponent-CSS i tokens-filen.
