# Tokens-iterasjon 2 — moderne semantiske farger + tactile buttons som default i tokens-app

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter at hele rammeverket var spec'et og visualisert, identifiserte vi to forbedringer: (a) semantiske farger (error/success/warning) bruker Tailwind 700-shades som leser corporate/dated, og (b) Apple/Stripe-aktig tactile button-pattern passer i SaaS-kontekst men ikke i Scandi-min editorial. Dette er en tokens-iterasjon, ikke en rearkitektur — vi endrer verdier og legger til ett surface-token-lag, men token-shapen er stabil.

---

## 1. Moderniserte semantiske farger via OKLCH

**Spørsmål:** error/success/warning føles "corporate" / "dated". Hvilke verdier holder i 2026?

**Valgt:**

| Token | tokens-web (refined) | tokens-app (bright) |
|---|---|---|
| `--color-error` | `oklch(0.58 0.22 28)` ≈ #D63A30 | `oklch(0.65 0.23 25)` ≈ #EE4646 |
| `--color-success` | `oklch(0.60 0.16 160)` ≈ #16A07A | `oklch(0.70 0.18 155)` ≈ #25B377 |
| `--color-warning` | `oklch(0.68 0.17 65)` ≈ #DC8B22 (ny) | `oklch(0.74 0.18 65)` ≈ #F09124 (oppdatert) |
| `--color-info` | (ikke i tokens-web — utelatt bevisst) | `oklch(0.62 0.18 245)` ≈ #2778E0 (oppdatert) |

**Hvorfor:**
- OKLCH som source of truth — perseptuelt jevnt, predictable adjustments.
- Hex som kommentar for referanse (designere leser hex naturlig).
- tokens-web: refined, warmere, mindre saturert — passer Scandi-min editorial.
- tokens-app: lysere og mer mettede — viktig for synlighet i tett SaaS-UI.
- `--color-warning` introdusert i tokens-web (var ikke der før).
- `--color-info` forblir utelatt i tokens-web — marketing-sider trenger sjelden "info"-tilstand som distinct farge.

**Migrasjon for eksisterende prosjekter:** ingen — tokens-shapen er uendret, kun verdiene. Komponenter som leser `var(--color-error)` får ny verdi automatisk.

---

## 2. Tactile buttons som default i tokens-app

**Spørsmål:** Apple/Stripe-aktig tactile button-pattern — hvor passer det?

**Valgt:** Default i `tokens-app`. Opt-in via `btn-elevated` i `tokens-web`.

**Hvorfor:**
- SaaS-UI lever i close-up interaction. Buttons er den mest brukte komponenten. Tactile rendering gir bedre interaksjons-feedback ("dette er klikkbart, og det føles tilfredsstillende å trykke").
- Marketing-sider tjener på roligere uttrykk — flate knapper passer Scandi-min editorial.
- Apple, Stripe, Linear, Vercel bruker alle tactile pattern i sine apps. Dette er konvensjon i 2026 SaaS-UI.
- Opt-in i tokens-web (`btn-elevated`) gir oss verktøyet for spesielle hero-CTAs uten å gjøre default for premium-aktig.

---

## 3. Implementasjon: surface-token-lag

**Spørsmål:** Hvordan får vi samme button-CSS til å rendre flat eller tactile basert på pakke?

**Valgt:** Fem nye CSS-variabler eksponert i `:root` per token-pakke:

```css
--button-surface-bg-rest
--button-surface-bg-hover
--button-surface-bg-active
--button-surface-shadow-rest
--button-surface-shadow-active
```

**tokens-web (flat default):**
- `bg-rest` = `var(--color-accent)` (solid)
- `shadow-rest` = `none`

**tokens-app (tactile default):**
- `bg-rest` = gradient fra `color-mix(--color-accent, white 8%)` til `--color-accent`
- `shadow-rest` = inner-highlight + bottom-edge + drop-shadow (3 lag)

`@utility btn-primary` leser fra `--button-surface-*`-tokens. Samme CSS, ulik rendering basert på pakke.

`@utility btn-elevated` overstyrer `--button-surface-*`-tokens lokalt på button-en til tactile-verdier — opt-in escape hatch for tokens-web.

**Hvorfor token-lag i stedet for to separate CSS-filer:**
- Vi har én buttons.css å vedlikeholde.
- Brand-overstyringer kan finjustere surface-uttrykket per kunde (eks. mindre dramatisk highlight, annen gradient-retning).
- Tone-prop (`danger`/`success`) fortsetter å fungere — den overstyrer `--color-accent` lokalt, surface-tokens bruker den nye fargen i gradients automatisk.
- Konsistent med vårt allerede etablerte pattern (`--button-radius`, `--input-radius`, `--lift-distance`).

---

## 4. `btn-elevated` som modifier i tokens-web

**Spørsmål:** Skal `elevated` være en femte variant (`variant="elevated"`) eller en modifier på toppen av andre variants?

**Valgt:** Modifier-prop på Button (`<Button variant="primary" elevated>`).

**Hvorfor:**
- `elevated` er ortogonal til variant — det handler om surface-rendering, ikke hierarki.
- I tokens-app er `elevated` redundant (allerede default) — React-komponenten advarer (dev-warning) hvis prop er satt i tokens-app-kontekst.
- Sparer en variant-slot i API-en.
- Konsistent med `tone`-prop (også orthogonal akse).

---

**Konsekvenser samlet:**
- Visuelt uttrykk i `tokens-app` blir merkbart annerledes — mer "premium", mer "tactile". Konsistent med moderne SaaS-konvensjon.
- Visuelt uttrykk i `tokens-web` er uendret — flat default. Editorial-aesthetic respektert.
- Nye `--button-surface-*`-tokens etablerer pattern for fremtidige overflate-relaterte tokens (eks. `--input-surface-*` hvis vi vil ha tactile inputs senere — anbefales ikke i utgangspunktet).
- Farge-modernisering er en visuell oppgradering med null breaking change for konsumenter.

**Reverseringskostnad:** Lav. Bytte tactile av i tokens-app = sette `--button-surface-shadow-rest: none` og `--button-surface-bg-rest: var(--color-accent)` i én fil. Bytte farger tilbake = sette gamle hex-verdier.
