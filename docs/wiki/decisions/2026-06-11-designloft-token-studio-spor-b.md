# ADR: Designløft Token Studio — spor B (komponentestetikk oppstrøms)

- **Dato:** 2026-06-11
- **Status:** Implementert (alle fem kandidater levert; to commit-økter)
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

Kandidatliste (prioritert, alle levert):

1. ✅ **Skygge-/elevasjonsskala** — mykere, lagdelte skygger (Stripe-stil): hver
   nivå stabler 2–3 skygger med progressiv blur og lav opasitet for roligere
   dybde. Web romslig, app strammere; lys + mørk. *(d0d7eb8)*
2. ✅ **Hover/active-mikrobevegelse** på interaktive flater — `--press-y` (`:active`)
   og `--hover-lift-y` (`:hover`), reduced-motion-trygt, ≤1px. *(d0d7eb8)*
3. ✅ **Strammere typografisk skala** for display-størrelser —
   `--tracking-display: -0.05em` (web), `-0.04em` (app) for Inter Tight;
   `--tracking-heading` harmonisert. *(509bf0c)*
4. ✅ **Form-fokusring + feiltilstand harmonisert** — nye tokens
   `--focus-ring-error` + `--focus-ring-success` for eksplisitt kontraktfesting.
   *(509bf0c)*
5. ✅ **Section-patterns: mer luft** — `--spacing-section` økt til 110–180px
   (web) / 60–110px (app); `--spacing-section-lg` til 140–212px (web) / 110–150px
   (app). *(509bf0c)*

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

## Gjennomføring

Spor B gjennomførtes i to økter, begge i denne sesjonen:

**Økt 1** (commit `d0d7eb8`): Punkt 1–2
- Lagdelt Stripe-stil elevassjonsskala (mykere falloff, lagdelt)
- Tokenisert mikrobevegelse (`--press-y`, `--hover-lift-y`) redusert-motion-trygt

**Økt 2** (commit `509bf0c`): Punkt 3–5
- Strammere tracking for display/heading (Inter Tight, -0.05em / -0.04em)
- Fokusring-tokens for error/success (`--focus-ring-error/success`)
- Økt default-seksjonsspacing (110–180px web, 60–110px app)

Alle CI-sjekker grønne; visuelt verifisert ved render på alle breakpoints × lys/mørk.

## Konsekvenser

- Konsumenter (kundesider + Token Studio-preview) høster den løftede estetikken
  automatisk ved neste sync.
- Skygge-, bevegelse-, typografi-, fokus- og spacing-tokenene er nå kontrakter.
- Token-navnene består stabile; verdiene er mykere/luftigere per benchmark.
