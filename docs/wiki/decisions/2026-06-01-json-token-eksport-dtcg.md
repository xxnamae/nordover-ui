# JSON-token-eksport i W3C DTCG-format

**Dato:** 2026-06-01
**Status:** Aktiv

**Kontekst:**
Nordover-visjonen er multi-plattform (web-first, men mappbar til native iOS/Android og desktop). Tokens er i dag kun publisert som CSS-custom-properties (`tokens-web.css`, `tokens-app.css`) i OKLCH med `@layer`-arkitektur. CSS-variabler kan ikke konsumeres direkte av native-plattformer, Figma eller token-tooling (Style Dictionary, Tokens Studio). For å realisere multi-plattform-ambisjonen trenger vi et maskinlesbart, verktøy-vennlig eksportformat — uten å innføre et nytt sannhetskilde-kontrakt som driver fra CSS-en.

**Alternativer:**
- A) **W3C DTCG-format generert av build-script fra CSS-en.** CSS forblir eneste sannhetskilde; JSON er et avledet artefakt. Industristandard (Style Dictionary, Tokens Studio, Figma-import). Ingen tredje fil å synke manuelt.
- B) **Håndskrevet DTCG-JSON.** Samme format, men sjekkes inn direkte. Blir et tredje kontrakt som må synkes manuelt med begge CSS-filer — bryter ånden i mirroring-regelen og inviterer drift.
- C) **Enkel flat JSON** (`{ "color-accent": "..." }`). Lett å lese, men ikke-standard: ingen typer, aliaser eller composite-typer (shadow/gradient/easing). Lite tooling-verdi, avviker fra multi-plattform-ambisjonen.

**Beslutning:**
Valg **A**. Token-JSON i [W3C Design Tokens Community Group (DTCG)](https://tr.designtokens.org/format/)-format, generert av `scripts/build_tokens.py` fra de kanoniske CSS-filene. Output: `docs/visual/tokens/tokens-web.json` og `tokens-app.json`, ett artefakt per pakke (1:1 med CSS-filene).

**Verdihåndtering (tapsfri, ærlig):**
- **Primitiver** får ekte DTCG-typer:
  - Farger → `color` med OKLCH-objekt: `{ "colorSpace": "oklch", "components": [L, C, H] }` (numeriske vars som `--neutral-c/-h` substitueres inn).
  - Lengder → `dimension` (`{ value, unit }`), varigheter → `duration`, easings → `cubicBezier`, font-vekter/z-index/line-heights → `number`.
- **Rene aliaser** (`--color-fg: var(--gray-900)`) → DTCG-referanse `{color.gray.900}`.
- **Deriverte verdier** uten ren DTCG-form (`color-mix()`, `clamp()`, gradienter, glass, multi-lag shadows) bevares **losslessly**: `$value` bærer den rå CSS-strengen og `$extensions["com.nordover.cssText"] = true` flagger at en CSS-kapabel runtime kreves. Konsumenten ser eksakt CSS-intensjon i stedet for en tapt/feilberegnet tilnærming.
- **Dark-mode** (`:root:has(#dark:checked)`-overstyringer) henges på det berørte tokenet under `$extensions["com.nordover.dark"]`, så hver pakke forblir én selvstendig fil.
- **Bakoverkompatible aliaser** (`--color-error` → `--error`) rutes til egen undergruppe `color.alias.*` for å unngå kollisjon med det kanoniske primitivet.

**Konsekvenser:**
- **Pro:** Multi-plattform-konsum (native, Figma, Style Dictionary); ingen tredje sannhetskilde; verifiserbart i CI (`--check`); primitiver er fullt portable, deriverte verdier er ærlig merket.
- **Con:** Deriverte tokens (`color-mix`/`clamp`) krever en CSS-runtime hos konsumenten — native-plattformer må selv resolve disse (dokumentert via `cssText`-flagget). En fremtidig ADR kan legge til en valgfri «resolved»-variant hvis native-behovet vokser.
- **Mirroring:** Token-verdiendringer i CSS krever regenerering av JSON i samme commit. Håndheves av `scripts/build_tokens.py --check` i `test.yml`.

**Implementasjon:**
- Generator: `scripts/build_tokens.py` (parser `:root`- og `:root:has(#dark:checked)`-blokkene; ingen avhengigheter utover Python-stdlib).
- `npm run build:tokens` (regenerer) og `npm run check:tokens` (CI-verifisering).
- `package.json` `files` inkluderer JSON-filene i npm-pakken.
- Konsum dokumentert i `docs/visual/tokens/README.md` og `docs/handoff/`.

**Se også:**
- `scripts/build_tokens.py`
- `docs/visual/tokens/README.md` — konsum-guide
- `2026-05-27-to-tokens-pakker.md` — hvorfor to pakker
- `2026-06-01-motion-token-platform-divergence.md` — hvorfor web ≠ app
