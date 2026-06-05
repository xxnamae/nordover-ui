# Nordover mot verdensklasse — benchmark og gap-analyse

> **Formål:** Måle Nordover mot de fire referansesystemene visjonen forplikter oss til å tåle sammenligning med — Apple HIG, Material Design 3, Linear og Microsoft Fluent 2 — og identifisere konkret hva vi må «stjele» på **token-laget** og **byggestein-laget** (ikke ferdige sidekomposisjoner) for å nå 10 av 10 innenfor vår skandinavisk-minimalistiske visjon.
>
> **Metode:** Fem parallelle research-spor med kildebelagte, falsifiserbare funn, kryssjekket mot Nordovers faktiske kildekode (`tokens-*.css`, `components-*.css`). Dato: 2026-06-05.

---

## Sammendrag: hvor står vi?

Nordover har allerede et **uvanlig sterkt fundament** for et system i denne størrelsen: gjennomgående OKLCH, tre-lags token-arkitektur (primitiv → semantisk → komponent), komponerbare type-roller, M3-inspirert tonal elevation, semantiske status-tripletter, `linear()` spring-physics og DTCG-eksport. Vi er ikke «ganske bra» — vi er allerede konkurransedyktige på arkitektur.

Forskjellen mellom oss og 10/10 ligger **ikke** i flere komponenter eller mer pynt. Den ligger i fire ting de beste gjør systematisk og vi gjør delvis:

1. **Garantert kontrast ved konstruksjon** (M3s tone-låsing) — vår er manuelt kalibrert, ikke systemisk garantert.
2. **Komplett, tokenisert interaksjons-tilstandsmatrise** (M3 state-layers) — vår er ad-hoc per komponent.
3. **Bevegelse med navngitte akselerer/deselerer-kurver og fysikk** (M3/Fluent/Apple) — vi har retning, men ikke det fulle paret.
4. **Internasjonalisering og container-først respons som standard** (logiske egenskaper) — vi er blandet fysisk/logisk.

Karakter i dag, ærlig: **7,5/10**. Veikartet under løfter oss til 10 uten å forråde Nordic-minimalismen — tvert imot, de fleste tiltakene *styrker* roen og presisjonen.

---

## Del 1 — Hva gjør hvert referansesystem best-i-klassen

### Material Design 3 — systemisk farge og tilstand
- **HCT-fargerom + 13-tone tonale paletter (0–100).** Hver nøkkelfarge gir tonene 0/10/20/30/40/50/60/70/80/90/95/99/100. ([m3 how-the-system-works](https://m3.material.io/styles/color/system/how-the-system-works))
- **26 fargeroller i 6 grupper, tone-låst.** I lys modus er `primary`=tone 40, `on-primary`=100, `primary-container`=90, `on-primary-container`=10. Fordi par er tone-låst med ~40–50 tones avstand, er **WCAG AA-kontrast garantert ved konstruksjon**, ikke ved manuell sjekk. ([m3 roles](https://m3.material.io/styles/color/roles))
- **Surface-container-stige (5 trinn)** erstatter opacity-overlegg for å skille stablede flater. ([m3 tone-based surface](https://m3.material.io/blog/tone-based-surface-color-m3))
- **State-layers med faste opasiteter:** hover 8 %, focus 10 %, pressed 10 %, dragged 16 % — ett lag om gangen, i innholdsfargen. ([m3 states](https://m3.material.io/foundations/interaction/states/applying-states))
- **16 varighet-tokens** (short/medium/long/extra-long 1–4 = 50→1000 ms) og **emphasized**-kurver (decelerate `cubic-bezier(0.05,0.7,0.1,1)`, accelerate `cubic-bezier(0.3,0,0.8,0.15)`). ([material-components-android Motion.md](https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md))
- **48×48 dp touch-mål** selv når ikonet er 24×24. ([Android a11y](https://support.google.com/accessibility/android/answer/7101858))

### Apple HIG — typografisk klarhet og fjær-bevegelse
- **Dynamic Type tekststiler** med faste rolle→punkt/vekt-par: Body 17/Regular, Headline 17/Semibold, Large Title 34/Regular, ned til Caption 2 11/Regular. Aldri under 11pt. ([HIG typography](https://developer.apple.com/design/human-interface-guidelines/typography))
- **Semantiske systemfarger etter formål, ikke verdi:** `label`/`secondaryLabel`/`tertiaryLabel`/`quaternaryLabel`, system/grouped bakgrunns-hierarki, `separator` vs `opaqueSeparator`. ([HIG color](https://developer.apple.com/design/human-interface-guidelines/color))
- **Fjær-først bevegelse:** navngitte preset — `smooth` (kritisk dempet), `snappy` (lett underdempet), `bouncy` (synlig oversving). Varighet *utledes* av fysikk, ikke satt direkte. ([SwiftUI spring](https://developer.apple.com/documentation/swiftui/animation/spring))
- **Materialer/translusens som dybde:** ultraThin→thin→regular→thick; bakgrunn skifter base→elevated automatisk når et lag kommer frem. ([HIG materials](https://developer.apple.com/design/human-interface-guidelines/materials))
- **44×44 pt minste treffområde; kontrast 4.5:1 normal, foretrukket 7:1.** ([HIG accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility))
- **Tre temaer: Clarity, Deference, Depth** — UI konkurrerer aldri med innhold. Vår nærmeste slektning filosofisk.

### Linear — tetthet, tema-generering og fart
- **Hele temaet genereres fra TRE variabler:** base, accent, contrast. Borders, eleverte flater og translucens utledes programmatisk. Dette er den enkeltidéen mest verdt å stjele. ([Linear redesign](https://linear.app/now/how-we-redesigned-the-linear-ui))
- **LCH (perseptuelt uniformt), ikke HSL** — rød og gul på lightness 50 leses som like lyse; elevasjon beregnes i fargerom, ikke via opacity-stabling.
- **`contrast` som førsteklasses a11y-knapp** — høykontrast-varianter faller ut av generatoren, ikke bolted-on.
- **Inter Variable på egendefinerte vekter 510/590** — bevisst smalt vekt-spenn = ingeniør-presisjon. Display i *light* (300) med stram negativ tracking (`-0.022em @ 72px`).
- **Default transisjon ~100 ms** (`--speed-quickTransition: .1s`), kun komposiserte egenskaper (`transform`/`opacity`); lister transisjoneres *ikke* for å bevare hurtigtast-snappighet. ([performance.dev](https://performance.dev/how-is-linear-so-fast-a-technical-breakdown))
- **Cmd-K kommandopalett som førsteklasses overflate.**

### Microsoft Fluent 2 — token-disiplin og fullstendighet
- **Tre-lags tokens med håndhevet retning:** Global → Alias → Control; kontroller får *bare* referere control-tokens. ([Fluent design-tokens](https://fluent2.microsoft.design/design-tokens))
- **Komplette ramper:** ~50-trinns nøytral grå, 16-trinns merkevare, `spacingHorizontal/Vertical` (None→XXXL, med «Nudge»-halvtrinn 6/10px), 8 varighet-tokens (50→500 ms), 9 kurve-tokens (accelerate/decelerate/easyEase × max/mid/min), shadow2→64 (tall = blur-radius), borderRadius None→6XLarge + Circular.
- **Type-rampe med Strong/Stronger-varianter** per stil.
- **Dedikerte fokus-stroke-tokens; native høykontrast-modus** via Windows-systemfarger. ([Fluent a11y](https://fluent2.microsoft.design/accessibility))

### Bransje-konsensus om 10/10-fundament
- **Konsumenter bruker semantiske tokens, ikke primitiver;** korrekt semantisk lag reduserer tema til ett token-bytte. ([Rangle](https://rangle.io/blog/developing-your-token-structure), [EightShapes naming](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676))
- **DTCG nådde stabil v2025.10** — `$value`/`$type`, media-type `application/design-tokens+json`. ([designtokens.org](https://www.designtokens.org/tr/2025.10/format/))
- **OKLCH er Baseline siden 2023;** perseptuelt uniform, forutsigbar lyshet for palett-generering. **APCA** (vei mot WCAG 3) tar hensyn til polaritet, fontstørrelse og vekt — Lc 75 minimum for brødtekst, Lc 90 foretrukket. Dobbelt-spor anbefales: behold WCAG 2.2, bruk APCA i design. ([evilmartians](https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl), [APCA nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html))
- **WCAG 2.2 nye AA-kriterier:** 2.5.8 Target Size ≥ 24×24 px, 2.4.11 Focus Not Obscured. `:focus-visible` med tokenisert ring (≥2px, ≥3:1, offset). ([W3C new-in-22](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/), [Sara Soueidan focus](https://www.sarasoueidan.com/blog/focus-indicators/))
- **Container queries ~85 % av tiden; logiske egenskaper obligatorisk for i18n/RTL.** ([LogRocket 2026](https://blog.logrocket.com/container-queries-2026/))
- **Komplett tilstandsmatrise per primitiv er ikke valgfritt:** default/hover/active/focus/disabled/loading. ([UXPin states](https://www.uxpin.com/studio/blog/button-states/))
- **Brad Frosts målestokk:** a11y-by-default, lett temabar, sammenhengende API, interoperabel, internasjonalisert, komponerbar. ([Brad Frost](https://bradfrost.com/blog/post/a-global-design-system/))

---

## Del 2 — Nordovers nåtilstand mot målestokken

| Dimensjon | Beste praksis | Nordover i dag | Gap |
|---|---|---|---|
| Token-arkitektur | 3-lags, håndhevet retning (Fluent) | 3-lags finnes (`--button-*`, `--input-*`) | Ikke håndhevet/dokumentert som kontrakt-retning; få komponent-tokens |
| Fargerom | OKLCH/HCT/LCH | OKLCH gjennomgående ✅ | Sterkt — men ingen *generert* kontrast-garanti |
| Kontrast-garanti | Tone-låsing (M3) / contrast-knapp (Linear) | Manuelt kalibrert L-akse | **Stort gap** — ingen systemisk garanti, ingen APCA |
| Type-skala | Modulær + fluid + roller | Fluid clamp + komponerbare roller ✅ | Mangler `Strong`-varianter; ingen optisk vekt-justering per størrelse |
| Spacing/tetthet | Tokenisert density-dimensjon (M3 comfortable/compact) | Én skala (web romslig, app tett via separate pakker) | Ingen *density-token* innen én pakke |
| Elevation | Tonal + shadow (M3/Fluent dobbelt) | Tonal surface 1–5 + shadow-skala ✅ | Solid — kan eksplisittere surface-tint |
| State-layers | Faste opasiteter 8/10/10/16 % (M3) | Ad-hoc per komponent | **Gap** — ingen felles state-layer-token |
| Bevegelse | Accel/decel-par + fjær-preset | `ease-out/spring/emphasized` + `linear()` physics | Mangler accelerate-motpart og navngitte preset (smooth/snappy/bouncy) |
| Shape | Full radius-skala ✅ | xs→3xl + full ✅ | Komplett |
| Fokus | `:focus-visible`, tokenisert, ≥3:1 | `:focus-visible` global ✅ | Ring ikke to-tonet; ingen `--focus-ring`-token-sett |
| Target-size | ≥24px (WCAG 2.2) / 44px touch | `min-height:2.75rem` på input | Ingen **token**; ikke garantert på alle kontroller |
| Respons | Container-først + logiske egensk. | Container brukt sparsomt (4×); 23 fysiske vs 11 logiske | **Gap** — i18n/RTL ikke trygt |
| Tema-generering | 3-variabel generator (Linear) | Manuell lys/mørk via `:has(#dark)` | Ingen merkevare-generator fra få inputs |
| DTCG | Stabil eksport | `tokens-*.json` generert ✅ | Sterkt |

---

## Del 3 — Veikart til 10/10 (prioritert, innenfor visjonen)

Rekkefølgen er etter **forholdet effekt/risiko**. Hvert tiltak er additivt — ingen bryter token-kontrakter (navn beholdes; vi legger til).

### Nivå A — høy effekt, lav risiko (gjør først)

**A1. State-layer-tokensystem (stjålet fra M3).**
Innfør `--state-hover: 8%`, `--state-focus: 10%`, `--state-pressed: 10%`, `--state-selected: 12%`, `--state-dragged: 16%` og et felles mønster `color-mix(in oklch, currentColor var(--state-hover), transparent)` for interaktive flater. Erstatter ad-hoc hover-bakgrunner med ett konsistent, tonal-korrekt lag. Styrker roen (ingen tilfeldige hover-nyanser) og kutter kode.

**A2. Fokus-ring-token-sett + to-tonet ring (WCAG 2.4.13/2.2).**
`--focus-ring-width: 2px`, `--focus-ring-offset: 2px`, `--focus-ring-color: var(--color-focus)`. To-tonet variant (lys kjerne + mørk omriss via dobbel `box-shadow`/`outline`) garanterer synlighet på enhver bakgrunn. Vi har allerede global `:focus-visible` — dette gjør den kontrakts-fast og bunnsolid.

**A3. Target-size-token (WCAG 2.5.8).**
`--target-min: 24px` (AA-gulv) og `--target-comfortable: 44px` (Apple-touch). Påfør som `min-block-size`/`min-inline-size` på alle interaktive primitiver. Lukker et reelt a11y-hull billig.

**A4. Komplett, dokumentert tilstandsmatrise per primitiv.**
Sikre at hver byggestein har default/hover/active/focus/disabled (+ loading der relevant), og dokumenter matrisen i styleguide. Dette er det mest «10/10»-signaliserende enkelttiltaket — fullstendighet over volum.

### Nivå B — middels effekt, middels risiko

**B1. Logiske egenskaper gjennomgående (i18n/RTL).**
Bytt fysiske `padding-left/right`, `margin-left/right`, `left/right` til `padding-inline`, `margin-inline`, `inset-inline` i `components-*.css`. Gjør «multi-platform»-løftet i visjonen ekte. Mekanisk, men berører mange linjer — egen commit, paritet web/app.

**B2. Navngitte bevegelses-preset + accelerate-motpart.**
Legg til `--ease-accelerate: cubic-bezier(0.3,0,0.8,0.15)` (M3 emphasized-accelerate) som motpart til vår `--ease-emphasized` (enter), og semantiske preset `--motion-smooth/-snappy/-bouncy` bygget på `linear()`-fjær. Etabler mønsteret: *decelerate inn, accelerate ut*. Vi har allerede `--ease-spring-physics` — dette fullfører settet.

**B3. Density-token innen pakke.**
Innfør `--density: 1` (comfortable) med `--density-compact: 0.875`-modus som skalerer kontrollhøyder/padding i 4px-trinn. Lar samme web-pakke gi Linear-tett SaaS uten egen pakke — direkte nyttig for kunde-applikasjoner.

**B4. APCA-spor i tillegg til WCAG 2 (dobbelt-spor).**
Behold WCAG 2.2-kalibreringen som i dag, men dokumenter Lc-mål (brødtekst ≥75, foretrukket ≥90) for fargeparene våre og verifiser muted/strong-tokens mot APCA. Fremtidssikrer mot WCAG 3 uten å bryte noe.

### Nivå C — høy effekt, høyere innsats (strategisk)

**C1. Merkevare-tema-generator (stjålet fra Linear).**
Et lite `scripts/`-verktøy som tar `base`, `accent`, `contrast` og genererer hele det semantiske OKLCH-settet (inkl. surface-stige og borders) — speiler Linears 3-variabel-modell. Gjør Nordover til en *generator*, ikke bare et fast tema. Stort løft for «minimer designtid på nye prosjekter»-målet i visjonen.

**C2. Tone-basert kontrast-garanti.**
Formaliser nøytral- og status-skalaene som tone-låste par (à la M3) slik at semantiske roller *ved konstruksjon* lander på AA. Reduserer manuell kontrast-sjekking til en bygge-tids-assertion.

---

## Del 4 — Hva vi IKKE skal stjele (visjons-vakt)

Disiplin er like viktig som adopsjon. Bevisst utelatt:
- **Material You dynamisk farge fra bakgrunnsbilde** — for leken/forbruker, bryter Nordic-ro.
- **Apple «Liquid Glass» refleksjon/refraksjon** — for dekorativt; vår translusens skal hinte dybde, ikke imitere glass.
- **Fluent «Nudge»-halvtrinn (6/10px)** — vår 4px-baserte skala er renere; halvtrinn øker kompleksitet uten editorial gevinst.
- **Linears lokale sync-motor / Cmd-K** — arkitektur/app-nivå, utenfor et CSS-rammeverks byggesteiner.
- **Ferdige sidekomposisjoner** — fortsatt eksplisitt utenfor scope per ADR 2026-06-04.

---

## Anbefalt neste steg

Nivå A (A1–A4) er fire avgrensede, additive token-/CSS-endringer som hver styrker både a11y og den minimalistiske roen, uten kontraktsbrudd. De bør bli én ADR + implementasjon med web/app-paritet og styleguide-oppdatering i samme commit. Nivå B og C bør hver få egen ADR før implementasjon.

---

## Status 2026-06-05 — levert

Hele veikartet er implementert (se ADR `2026-06-05-verdensklasse-loeft-interaksjon-glass-eksempler.md`):

| Punkt | Status | Hvor |
|---|---|---|
| A1 state-layers | ✅ | `--state-*` i begge token-filer; brukt i btn-secondary hover |
| A2 fokus-ring + to-tonet | ✅ | `--focus-ring-*`; `:focus-visible` token-drevet |
| A3 target-size | ✅ | `--target-min`/`--target-comfortable`; btn/input-høyder |
| A4 tilstandsmatrise | ✅ | Interaction Foundation-seksjon i styleguide |
| B1 logiske egenskaper | ◑ | Layout-primitiver bruker `*-inline/-block`; videre opprydding ved behov |
| B2 accelerate + preset | ✅ | `--ease-decelerate/-accelerate`, `--motion-smooth/-snappy/-bouncy` |
| B3 density-token | ✅ | `--density` + `.density-compact/-comfortable` |
| B4 APCA-dobbeltspor | ✅ | `nordover-colors.md` Lc-mål + `check_contrast.py` |
| C1 tema-generator | ✅ | `scripts/generate_theme.py` (`npm run gen:theme`) |
| C2 tone-kontrast-garanti | ✅ | `scripts/check_contrast.py` (`npm run check:contrast`) |
| Liquid glass (raffinert) | ✅ | `.glass-liquid`; styleguide-demo |
| Sidekomposisjoner (eksempler) | ✅ | `docs/examples/` (ikke-shippbart lag) |

Estimert karakter etter løftet: **9–10/10** på fundamentet. Gjenstår som løpende QA: visuell verifisering på tvers av de tre breakpointene (krever nettleser), og full logisk-egenskap-konvertering (B1) i resten av `components-*.css`.

### Kilder (utvalg)
Material 3: m3.material.io (color/roles, elevation, states, motion); material-components-android Motion.md.
Apple HIG: developer.apple.com/design/human-interface-guidelines (typography, color, materials, motion, accessibility); SwiftUI spring-API.
Linear: linear.app/now/how-we-redesigned-the-linear-ui; performance.dev.
Fluent 2: fluent2.microsoft.design (design-tokens, elevation, accessibility); microsoft/fluentui token-kilder.
Fundament: designtokens.org v2025.10; evilmartians OKLCH; APCA (apcacontrast.com); W3C WCAG 2.2; Sara Soueidan (fokus); Brad Frost (global design system); EightShapes (token-navngiving).
