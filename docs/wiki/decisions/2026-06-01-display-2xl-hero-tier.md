# Ny typografi-tier: `t-display-2xl` for landingsside-hero

**Dato:** 2026-06-01
**Status:** Aktiv

**Kontekst:**
Landingssidens hero trengte mer visuell tyngde. Systemets største eksisterende
display-tier (`t-display-xl`) bruker på web `--text-8xl` (fluid opptil 10rem/160px),
som ble opplevd som for liten for en marketing-hero med maksimal impact. Å øke
hele display-skalaen ville vært en bredt-virkende kontraktsendring som påvirker
alle store headinger overalt. Vi ville isolere endringen til hero-bruk.

**Alternativer:**
- A) **Egen ny tier `t-display-2xl`** over `t-display-xl`. Additiv — påvirker ikke
  eksisterende headinger. Ny størrelses-token per pakke (`--text-9xl` web,
  `--text-6xl` app) og ny semantisk klasse. Stabil API (kun tillegg).
- B) **Øk hele display-skalaen** (`--text-7xl/8xl`). Størst effekt, men endrer
  verdien på en publisert kontrakt og forstørrer alle store headinger system-vidt
  — uønsket bredde og risiko for regresjon i eksisterende sider/styleguides.
- C) **Side-spesifikk override** i `index.html`. Avvist — bryter prinsippet om at
  styleguidene/systemet er fundament for all styling; ville ikke vært gjenbrukbart.

**Beslutning:**
Valg **A**. Ny tier `t-display-2xl`, definert i begge pakker (speilet klassenavn,
divergerende verdi per skalafilosofi):

| Pakke | Størrelses-token | Verdi | Klasse |
|---|---|---|---|
| web | `--text-9xl` | `clamp(4.25rem, 1.8rem + 11vw, 12rem)` (≈68→192px, mobil-trygg min) | `.t-display-2xl` (weight `--fw-display-xl`, tracking −0.045em) |
| app | `--text-6xl` | `3.75rem` (60px, statisk kompakt skala) | `.t-display-2xl` (weight `--fw-display-xl`, tracking −0.04em) |

Web er fluid (marketing), app er statisk og kompakt (SaaS-tetthet) — i tråd med
`2026-05-30-token-divergence-policy.md`. Mobil-min på web (4.25rem) er valgt slik
at «Nordover» (8 tegn) ikke overflower ved 375px.

**Konsekvenser:**
- **Stabil API:** Rent additivt — ingen eksisterende token eller klasse endret.
- **Mirroring:** Begge token-filer og begge komponent-filer oppdatert i samme commit;
  DTCG-JSON regenerert (`npm run build:tokens`).
- **Styleguide:** `t-display-2xl` dokumentert i både `styleguide-web.html` og
  `styleguide-app.html` (Type Scale / Display Scale). Web-showcaset fikk samtidig
  inn den manglende `t-display-xl` for 100% dekning.
- **Bruk:** Reservert for landingsside-hero / maksimal impact. `t-display-xl` forblir
  standard for vanlige hero-seksjoner.
