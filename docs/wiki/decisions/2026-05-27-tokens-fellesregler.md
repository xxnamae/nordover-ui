# Fellesregler for tokens-pakker (web og app)

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Tre konvensjons-spørsmål dukket opp under tokens-arkitektur-drodling. Disse handler ikke om strategiske retning, men om kode-konvensjoner som må gjelde likt for `@nordover/tokens-web` og `@nordover/tokens-app`.

---

## 1. Utopia-konfig committes som kommentar

**Spørsmål:** Skal Utopia-parametrene (min/max viewport, base, ratio, steps) lagres i repoet for reproduserbar regenerering?

**Alternativer:**
- A) Ikke lagre. Husk dem, eller eyeball-tweak eksisterende clamp-verdier.
- B) Kommentar-blokk øverst i hver `tokens-*.css` med eksakte parametre.
- C) Egen JSON/YAML-fil + build-step som henter fra Utopia.

**Valgt:** B.

**Hvorfor:** Regenerering skjer kanskje én gang per år. C er overkill. A taper informasjon. B koster en kommentar-blokk og er reproducerbar uten ekstra tooling.

**Format:**
```css
/*
 * Type-skala-parametre (for regenerering via https://utopia.fyi/type/calculator):
 *   min:   320px viewport, 16px base, ratio 1.2
 *   max:   1440px viewport, 18px base, ratio 1.333
 *   steps: -2 til 8
 */
```

---

## 2. `color-mix()` / OKLCH uten fallback

**Spørsmål:** Trenger Omhu (eller andre app-prosjekter) fallback-tokens for `color-mix(in oklch, ...)`-baserte hover/active-farger?

**Alternativer:**
- A) Eksplisitte hover/active-tokens for hver farge (`--color-accent-hover: #...`). Verbose, men full støtte.
- B) `color-mix()`-defaulter med eksplisitt overstyring kun ved behov per brand. Moderne baseline.
- C) `@supports`-blokk med fallback for browsere uten color-mix.

**Valgt:** B.

**Hvorfor:**
- `color-mix()` har bred støtte fra 2023 (Chrome 111, Safari 16.2, Firefox 113). I 2026 er det baseline.
- OKLCH-fargerom er kritisk for perseptuelt jevn hover-mørkning på tvers av brand-farger.
- Omhu sin målgruppe (borettslagsstyrer) bruker stort sett moderne browsere (auto-oppdaterte mobiler, nyere PC-er).
- Hvis et spesifikt brand-prosjekt har en eldre browser i sin SLA, kan de overstyre `--color-accent-hover` med en eksplisitt verdi i `clients/<slug>.css`. Lokal opt-out, ikke global byrde.

**Konsekvens:** Browserslist for Nordover-prosjekter bør være `"chrome >= 111, firefox >= 113, safari >= 16.2, edge >= 111"` eller løsere. Sjekkes per prosjekt før lansering.

---

## 3. `--color-accent` har felles semantikk i begge pakker

**Spørsmål:** Skal `--color-accent` bety det samme i `tokens-web` og `tokens-app`?

**Alternativer:**
- A) Samme semantikk: "primær brand-handlingsfarge". Ulike defaults per pakke, samme rolle.
- B) Kontekst-avhengig: "spotlight-aksent" i marketing, "dominerende handlingsfarge" i SaaS.
- C) Ulike token-navn per kontekst (`--color-spotlight` for marketing, `--color-action` for SaaS).

**Valgt:** A.

**Hvorfor:**
- Token-navn er kontrakter. Samme navn = samme mening i alle kontekster. Brudd på denne regelen skaper hidden gotchas.
- Delte komponenter (`@nordover/ui`-pakker) kan trygt bruke `var(--color-accent)` uten å vite om de havner i web- eller app-kontekst.
- Hvis et fremtidig behov krever ulik rolle, introduser **nytt** token (`--color-spotlight`, `--color-action`) — ikke gjenbruk eksisterende.

**Konsekvens:**
- `tokens-web` defaulter `--color-accent` til `#0A0A0A` (svart — minimalistisk).
- `tokens-app` defaulter `--color-accent` til `#0066FF` (blå — tydelig handlingsfarge).
- Defaulten er bare et utgangspunkt; brand-fila skal overstyre med faktisk brand-farge.
- Konvensjonen "samme navn = samme rolle" gjelder ALLE semantiske tokens, ikke bare `--color-accent`. Dokumenteres i felles-regler.

---

**Reverseringskostnad samlet:** Lav for alle tre. Konvensjonene er kommentarer og default-verdier — endring krever ingen rename i konsumenter.
