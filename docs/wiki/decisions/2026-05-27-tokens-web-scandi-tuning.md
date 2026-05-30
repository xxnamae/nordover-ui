# tokens-web tunet for skandinavisk minimalisme

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Nordover-stacken brukes til marketing-nettsider med en konsekvent husstil: skandinavisk minimalisme med dramatisk typografi som primært designelement. Default-`tokens-web` måtte tunes for denne estetikken, ikke for "moderne web-default". Samtidig trenger systemet å være dempbart for klienter med andre uttrykk.

**Alternativer:**
- A) **Konservativ default, dramatisk via brand-overstyring.** Base lik klassisk web-skala (ratio 1.25, maks 76px). Hver Scandi-min-kunde må heve baseline.
- B) **Aggressiv Scandi-min default, brand-overstyring kan dempe.** Base går høyt og luftig. Tammere kunder demper via alias-overstyring (`--text-8xl: var(--text-5xl)`).
- C) **Tre presets:** `tokens-web-editorial`, `tokens-web-standard`, `tokens-web-compact`. Hver kunde velger ved import.

**Valgt:** B.

**Hvorfor:**
- 9 av 10 Nordover-leveranser følger husstilen. Default skal speile det, ikke fortynne det.
- Alias-overstyring (`--text-8xl: var(--text-5xl)`) er en billig, presis dempemekanisme — utvikleren beholder Tailwind-utility-navnene, men topp-trinn rendres som lavere trinn.
- C ble forkastet fordi det multipliserer vedlikehold (tre filer å holde i sync) og legger en valg-byrde på utvikleren ved hvert nye prosjekt.
- A ble forkastet fordi "default" definerer husstilen — hvis husstilen er Scandi-min, må default reflektere det. Ellers blir hver prosjektoppstart en kalibrerings-jobb.

**Konkrete tuning-valg:**
- Type-ratio 1.2 (mobil) → 1.333 (desktop). Tidligere 1.25 → 1.25.
- Topp-trinn: `--text-8xl` opp til 160px. Tidligere `--text-6xl` på 76px.
- Line-heights ned til 0.9 på `--text-8xl` (editorial-headlines sitter tett).
- Letter-spacing-tokens per step (negativ tracking fra `--text-2xl` og opp).
- `--font-weight-display: 400` (editorial regular, ikke bold).
- `--spacing-section`: clamp(4rem, 12vw, 10rem) — opp til 160px luft mellom seksjoner.
- `--page-padding`: clamp(1.5rem, 6vw, 6rem) — opp til 96px gutter på ultra-wide.
- `--container-edge: 100%` for editorial full-width-layouts.

**Konsekvenser:**
- Default-skala går høyere og luftigere enn industristandard. Krever bevissthet ved bruk av `--text-8xl`-utilities — disse er for hero/display, ikke generell innhold.
- Brand-overstyringer for konservative kunder må dokumenteres som mønster (se `nordover-arkitektur.md` § Tuning).
- `--font-weight-display: 400` betyr at h1/h2 ikke automatisk er bold — komponentene må sette dette eksplisitt via tokenet, ikke hardkode `font-bold`.
- Nordover-design-team må kjenne skala-toppen for å bruke den meningsfullt — ikke alle prosjekter skal bruke `--text-7xl`/`--text-8xl`.

**Reverseringskostnad:** Lav. Hvis husstilen endrer seg, juster clamp-verdier i én fil. Konsumenter trenger ikke rename — utility-navnene er stabile.
