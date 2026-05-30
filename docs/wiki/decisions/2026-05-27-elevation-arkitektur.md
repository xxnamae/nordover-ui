# Elevation-arkitektur

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter tokens, typografi og layout måtte vi spec'e elevation: shadows, borders, og hover-interactions. Fire koblede valg om hvordan vi tenker om "dybde" i Scandi-min editorial-kontekst.

---

## 1. Utvid shadow-skala til xs/sm/md/lg/xl + inset

**Spørsmål:** 3 trinn (dagens), 5 trinn (industri-standard), eller 5 + inset?

**Valgt:** 5 trinn (xs/sm/md/lg/xl) + separat `--shadow-inset`.

**Hvorfor:**
- 3 trinn gir for grov gradering for floating UI (popover vs modal vs drawer trenger ulik vekt).
- 5 trinn er industri-standard og dekker hele spekteret.
- `inset` er en egen kategori (trykk-tilstander, focused inputs), ikke en del av lineær skala.
- Verdiene er **kalibrert subtilere** enn industri-default for å passe Scandi-min: tokens-web bruker alphas 0.04-0.12 i lys modus, der amerikansk SaaS-standard ofte ligger på 0.1-0.25.
- Multi-layer shadows (ambient + key) gir mer realistisk dybde uten å øke styrke.

---

## 2. Semantiske aliaser på toppen av t-shirt-navn

**Spørsmål:** Bare t-shirt (`shadow-md`), bare semantiske (`shadow-popover`), eller begge?

**Valgt:** Begge.

**Hvorfor:**
- T-shirt-skala er primitiv-laget — det Tailwind genererer utilities fra.
- Semantiske aliaser (`--shadow-popover`, `--shadow-modal`, `--shadow-drawer`, `--shadow-tooltip`, `--shadow-card-hover`) gir kontekst-bevisst valg.
- Brand kan overstyre `--shadow-modal` uten å touche alle `--shadow-lg`-bruk (semantisk overstyring uten primitiv-rotering).
- Komponenter (`<Modal>`, `<Popover>`) refererer semantisk; ad-hoc bruk refererer t-shirt.

---

## 3. Border-tokens som parallell "flat elevation"

**Spørsmål:** Er borders bare en stil-utility, eller en likeverdig elevation-strategi?

**Valgt:** Likeverdig strategi, med dedikert token-sett.

**Hvorfor:**
- Scandi-min editorial bruker ofte borders der amerikansk design ville brukt shadows. Et bordered kort signaliserer "luksuriøs, rolig"; et shadowed kort signaliserer "klikk meg".
- Dedikerte tokens (`--border-card`, `--border-input`, `--border-divider`, `--border-focus`) lar komponenter bytte mellom flat og elevated via brand-overstyring.
- `--border-width-hairline: 0.5px` introdusert som premium-touch — snaps til 1px på lavoppløst, men ser luksuriøs ut på retina.

**Konsekvens for fremtidige komponenter:**
- `<Card variant="bordered">` (default) bruker `--border-card`.
- `<Card variant="elevated">` bruker `--shadow-card-hover` uten border.
- `<Card variant="subtle">` har verken border eller shadow — kun bakgrunn.

---

## 4. Hover-lift som `@utility` + customizable tokens

**Spørsmål:** Hver komponent skriver hover-pattern selv, eller felles `@utility`?

**Valgt:** Felles `@utility hover-lift` med tokens som lar brand justere uten å patche CSS.

**Tokens:**
- `--lift-distance` (default -2px web, -1px app)
- `--lift-shadow-from` (default `--shadow-xs`)
- `--lift-shadow-to` (default `--shadow-md` web, `--shadow-sm` app)

**Hvorfor:**
- Hover-lift er et gjenkommende mønster (kort, knapper, links). DRY.
- Customization via tokens betyr brand kan dempe eller forsterke uten å duplisere selectors.
- Slå av løft helt: sett `--lift-distance: 0` + `--lift-shadow-to: var(--lift-shadow-from)`.
- `prefers-reduced-motion`-override på `--duration-base` (allerede i tokens-spec) gjør at hover-animasjonen forsvinner automatisk for sensitive brukere — ingen ekstra a11y-arbeid kreves.

---

**Konsekvenser samlet:**
- Tre nye token-kategorier i begge pakker: utvidet shadow-skala, border-tokens, lift-tokens.
- Total token-overflate vokser, men gir gjengjeld i form av at komponenter (Card, Modal, Tooltip, etc.) blir veldig tynne wrappers rundt tokens.
- "Flat vs elevated" er nå en eksplisitt valgakse i designet — ikke et implisitt bortvalg.
- `@utility hover-lift` er den første interaksjons-utility — etablerer mønster for fremtidige interaksjoner (focus-ring-utility, press-shrink, etc.).

**Reverseringskostnad:** Lav. Token-verdier er tall i en fil. Hvis vi vil bytte til 3-trinns skala igjen, eller fjerne border-tokens, er det en kort jobb.
