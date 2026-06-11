# ADR: Designløft Token Studio — spor B (komponentestetikk oppstrøms)

- **Dato:** 2026-06-11
- **Status:** Vedtatt (Eirik ga mandat: «designe på intuisjon og research fra globale ledere»)
- **Kontekst-lenker:** `docs/wiki/topics/nordover-visjon.md`, `docs/wiki/decisions/2026-06-05-unifisert-navnekonvensjon.md`

## Kontekst

Token Studio (redigeringsflaten oppå nordover-ui) er funksjonelt komplett og
deployet. Skallet ble bevisst bygget enkelt; nå løftes UX/UI til nivået hos de
beste interne verktøyene (referansepunkter: **Linear**, **Vercel/Geist**,
**Stripe Dashboard**, **Figma**).

**Prinsipp-avklaring (permanent):** Token Studio **erstatter ikke** nordover-ui.
nordover-ui er designsystemet — kilden til tokens og komponent-CSS. Alle
kundesider OG Token Studio-previewen bygger på den. Et designløft gjøres derfor i
**to spor**, og komponent-løftet skjer **oppstrøms** slik at alle flater høster
det:

- **Spor A** — studio-krommet (app-kode i Token Studio-repoet). Løftes lokalt med
  eksisterende tokens. *Utenfor dette repoet.*
- **Spor B** — komponentene og pattern-estetikken (her i nordover-ui). Løftes i
  rammeverket og synces til konsumentene via vanlig sync-rutine.

Denne ADR-en dekker **spor B**.

## Beslutning

Vi løfter komponent- og token-estetikken i nordover-ui langs en prioritert
kandidatliste. Alle endringer respekterer rammeverkets ufravikelige regler:
**WCAG AA-kontrast** og **`prefers-reduced-motion`** (global guard i `:root`).

Kandidatliste (prioritert):

1. **Skygge-/elevasjonsskala** — mykere, lagdelte skygger (Stripe-stil): flere
   stablede lag med progressiv blur og lav opasitet for et roligere, mer
   realistisk dybdeinntrykk. *(denne økten)*
2. **Hover/active-mikrobevegelse** på interaktive flater — tokenisert
   trykk/løft, reduced-motion-trygt via eksisterende global guard. *(denne økten)*
3. **Strammere typografisk skala** for display-størrelser — Inter Tight utnyttes
   bedre i store snitt (tettere tracking + leading). *(neste økt)*
4. **Form-elementenes fokusring og feiltilstand harmoniseres** — én tokenisert
   ring-kontrakt, konsekvent feil-/suksess-fokus. *(neste økt)*
5. **Section-patterns: mer luft i default-rytmen** (luftig som referanse).
   *(neste økt)*

## Prinsipper

1. **Tokens er fortsatt sannhetskilden.** Verdiendringer speiles til både
   `tokens-web.css` og `tokens-app.css` i samme commit; JSON regenereres
   (`npm run build:tokens`), CI håndhever synk.
2. **Web og app beholder sine karakterer.** Web er romslig/editorial, app er
   kompakt/tett. Skygger og bevegelse kalibreres per pakke — ikke identiske
   verdier, men samme *struktur*.
3. **Ingen nye avhengigheter.** Ingen ikon-bibliotek eller stilrammeverk; rene
   CSS-tokens og -primitiver (jf. CLAUDE.md «ikke i scope»).
4. **Reduced-motion er ufravikelig.** All mikrobevegelse er liten (≤1px / ≤2%)
   og går gjennom den globale `prefers-reduced-motion`-guarden som nullstiller
   transition-varighet — samme kontrakt som eksisterende `.btn-primary:hover`.
5. **Styleguide følger med i samme commit** (jf. STYLEGUIDE-WORKFLOW.md).

## Ikke i scope

- Nye avhengigheter, ikon-bibliotek eller stilrammeverk.
- Token-endringer lokalt i vendored pakker (går alltid oppstrøms — dette er
  oppstrøms).
- Mobil-first redesign av editor-panelet (spor A, egen oppgave).

## Konsekvenser

- Konsumenter (kundesider + Token Studio-preview) høster den løftede estetikken
  automatisk ved neste sync.
- Skygge- og bevegelses-tokenene er kontrakter: navnene består, verdiene mykere.
- Punkt 3–5 dokumenteres som oppfølging i samme ADR-spor når de implementeres.
