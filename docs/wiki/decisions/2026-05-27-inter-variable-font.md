# Inter Variable som primær font

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Inter Variable + Inter Tight Variable er enkeltfil-variable-fonter som dekker hele vekt-spekteret (100-900) kontinuerlig. Statisk Inter-distribusjon krever én woff2-fil per vekt (typisk 9 filer × ~80kb). Variable-versjonen er ~140kb totalt og gir bonus: finkalibrerte vekter, smooth animasjon, optical sizing.

---

## Beslutning

**Bytt fra statisk Inter til Inter Variable som primær font i begge token-pakker.**

- `--font-sans`: `"Inter Variable", "Inter", system-ui, ...` (fallback til statisk Inter, så system)
- `--font-display`: `"Inter Tight Variable", "Inter Tight", "Inter Variable", "Inter", system-ui, ...`

---

## Hvorfor

**Tekniske gevinster:**
- **Lavere bundle:** ~140kb vs ~720kb hvis du bruker mange vekter.
- **Færre HTTP-requests:** 1 woff2 i stedet for 9.
- **Skarpere preload-strategi:** preload én fil, ferdig.

**Designgevinster:**
- **Finkalibrerte vekter:** ikke begrenset til 400/500/600. Display kan bruke 380 for elegant editorial; UI-labels kan bruke 520 for bedre screen-rendering.
- **Smooth animasjon:** weight-transisjon på hover/focus uten snap.
- **Future-proof:** hvis vi senere vil eksperimentere med custom axes (optical size, slant, width), er infrastrukturen klar.

**Risikoer:**
- **Browser-støtte:** variable fonts er baseline siden 2018. I 2026 er det 100% støttet i alle moderne browsere. Fallback til statisk Inter dekker enhver edge case.
- **Filstørrelse for én vekt:** hvis et prosjekt KUN trenger én vekt (uvanlig), statisk wins marginalt. Ikke et reelt scenario for Nordover.

---

## Self-host vs CDN

**Anbefaling:** **Self-host** woff2-filer i prosjektet (`/public/fonts/`).

**Hvorfor:**
- Ingen tredjeparts-DNS-lookup på første request.
- Ingen tracking-risiko.
- Mulighet for `preload` med `crossorigin`-attributter.
- Kontrollert versjon — ingen overraskelser hvis CDN-en endrer noe.
- GDPR-vennlig (ingen IP-deling med Google/CDN).

**rsms.me-CDN** brukes kun for raskt prototype-arbeid (eks. styleguide-demoer).

---

## Finkalibrerte weight-tokens

Nye tokens i `tokens-web` (og `tokens-app` der relevant) for å eksponere finkalibrert vekt per semantisk typografi-klasse:

```css
:root {
  --font-weight-display-xl: 380;   /* lett-medium, editorial display */
  --font-weight-display-lg: 400;
  --font-weight-display-md: 420;
  --font-weight-heading-lg: 440;
  --font-weight-heading-md: 480;
  --font-weight-heading-sm: 500;
  --font-weight-body: 400;
  --font-weight-body-sm: 520;      /* medium+ for bedre UI-rendering */
  --font-weight-eyebrow: 600;
  --font-weight-caption: 520;
}
```

**Brand kan overstyre** per prosjekt — for eks. en kunde som vil ha tyngre display:
```css
:root {
  --font-weight-display-xl: 500;
  --font-weight-display-lg: 480;
}
```

**Fallback:** ved statisk Inter eller systemfont snaps verdiene til nærmeste 100-step (380 → 400, 520 → 500) — ingenting går i stykker.

---

## Konsekvenser

- **Bytte i tokens-web og tokens-app** (1 linje hver — `--font-sans` og `--font-display`).
- **Nye weight-tokens** i `:root` i begge pakker.
- **Oppdaterte `@utility`-blokker** i typografi-spec for å bruke de finkalibrerte tokens.
- **Font-loading-dokumentasjon** lagt til i `nordover-typografi.md` (self-host pattern + preload-hint).
- **Implementerings-jobb i Nordover-repo:** legge woff2-filer i `public/fonts/`, @font-face i `base.css`, preload-hints i app-shell.

**Reverseringskostnad:** Lav. Bytte tilbake til statisk Inter er én linje per tokens-pakke. Weight-tokens kan rounds-up til nærmeste 100-step uten visuell skade.

---

## Kilder

- [Inter Variable (offisiell distribusjon)](https://rsms.me/inter/)
- [Inter Tight Variable](https://github.com/rsms/inter/releases) — egen "Tight" variant av Inter for display-bruk.
- [MDN: Variable fonts guide](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide)
