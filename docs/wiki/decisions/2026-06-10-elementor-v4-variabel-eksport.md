# ADR: Elementor v4-variabeleksport (`build_elementor.py`)

- **Dato:** 2026-06-10
- **Status:** Vedtatt
- **Kontekst-lenker:** `docs/handoff/ELEMENTOR-WORDPRESS.md`, `docs/wiki/decisions/2026-06-01-json-token-eksport-dtcg.md`

## Kontekst

Nordover konsumeres i Elementor som et **token-lag** (komponent-CSS-en treffer
ikke widget-markup). Hittil var eneste vei å lime hele token-CSS-en inn i
*Custom CSS*. Det er trofast (beholder `clamp()`, `color-mix()`, dark mode), men
gir ingen native opplevelse: tokenene dukker ikke opp i Elementors farge-,
typografi- og størrelsesvelgere.

Elementor **Editor V4** (3.33+/4.x) har en **Variables Manager** med eksport/
import. En faktisk kit-eksport fra en ekte v4.1-installasjon avdekket det
nøyaktige skjemaet:

```json
{"data": {"e-gv-<id>": {"type","label","value","order","created_at","updated_at","sync_to_v3"}},
 "watermark": N, "version": 1}
```

Fire variabeltyper: `global-color-variable` (hex), `global-font-variable`
(font-navn), `global-size-variable` (enkel dimensjon), og
`global-custom-size-variable` (vilkårlig uttrykk — `clamp()`/`calc()` aksepteres).

## Beslutning

Vi shipper en **generator**, `scripts/build_elementor.py`, som leser de
kanoniske token-CSS-filene og produserer en v4-variabel-JSON per pakke
(`docs/handoff/nordover-elementor-v4-{web,app}.json`).

Prinsipper:

1. **CSS er fortsatt sannhetskilden.** JSON-en genereres; den redigeres aldri
   for hånd. `npm run build:elementor` regenererer; CI (`--check`) håndhever
   synk mot CSS — nøyaktig som DTCG-token-JSON-en.
2. **Gjenbruk eksisterende matte.** OKLCH→sRGB fra `check_contrast.py` og
   CSS-parsingen fra `build_tokens.py`; ingen ny avhengighet.
3. **Resolve det Elementor ikke forstår.** OKLCH og `color-mix()` regnes ut til
   konkret hex (8-sifret ved alpha < 1). `var()`-kjeder ekspanderes til
   literaler (Elementor-variabler kan ikke referere hverandre).
4. **Behold det Elementor forstår.** `clamp()`-verdier beholdes verbatim som
   `global-custom-size-variable` — fluid typografi/spacing overlever native.
5. **Deterministisk output.** Stabile `e-gv`-id-er (hash av label) og fast
   tidsstempel gir rene differ og fungerende `--check`.

## Hva eksporten IKKE er

- **Ikke en levende kobling.** Fargene er et **øyeblikksbilde**: å endre
  `--color-accent` etterpå rekomputerer ikke `accent-hover` (den er allerede
  flatet til hex). Custom-CSS-ruten beholder den deriverte relasjonen.
- **Ingen lys/mørk per variabel.** Hver variabel har én verdi → vi eksporterer
  **lys/base**-blokken. Dark mode krever fortsatt Custom-CSS-ruten eller et
  duplisert variabelsett.
- **Bevisst utelatt:** vekter, line-height/letter-spacing, motion (varighet/
  easing), skygger, gradienter og glass — ingen av dem har en v4-variabeltype.

## Konsekvenser

- Konsumenter på Editor V4 får hele token-settet som native variabler med ett
  import-steg, on-brand i alle velgere.
- De to rutene er komplementære, ikke gjensidig utelukkende: native variabler
  for redigerings-UX, Custom-CSS for det variabler ikke kan uttrykke
  (fluid type bevares riktignok i begge).
- Ny generert artefakt under CI-synk. Token-verdiendringer må regenerere
  Elementor-JSON i samme commit (`npm run build:elementor`).

## Alternativer vurdert

- **Kun Custom-CSS (status quo):** trofast, men ingen native velger-opplevelse —
  utilstrekkelig for team som bygger i Editor V4.
- **Generere mot et gjettet skjema:** forkastet — vi ventet på en ekte
  kit-eksport og bygde mot det verifiserte formatet felt-for-felt.
- **Full kit-zip (manifest + alle filer):** større overflate og usikker intern
  mappestruktur; vi shipper variabel-JSON-en (det verifiserte artefaktet) og
  dokumenterer importveien.
