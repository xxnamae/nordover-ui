# Buttons-arkitektur

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Buttons er den mest brukte interactive komponenten og kaskaderer overalt — links, CTAs, form-bunner, dialog-actions. Vi måtte definere variant-aksene, API for komposisjon, og hvordan link-vs-button-skillet håndteres.

---

## 1. 4 variants × `tone`-akse (ikke 12 variants)

**Spørsmål:** Hvor mange variants, og hvordan håndterer vi semantiske farger?

**Valgt:** 4 variants (`primary`, `secondary`, `ghost`, `link`) × `tone`-prop (`neutral` | `danger` | `success`).

**Hvorfor:**
- 4 visuelle hierarki-nivåer dekker behovet uten å multiplisere overflate.
- `tone` er en orthogonal akse — `<Button variant="ghost" tone="danger">` er gyldig kombinasjon uten å skape et nytt variant.
- Tone implementeres ved å lokalt overstyre `--color-accent`-familien innenfor button-en. Alle variants leser fra disse tokens, så hele variant-sett "fargelegges" automatisk.
- 4 × 3 = 12 logiske kombinasjoner uten 12 separate komponenter.
- `destructive` som eget variant ble forkastet — `tone="danger"` er kortere og mer komposisjonelt.

---

## 2. 3 størrelser: sm/md/lg

**Spørsmål:** Hvor mange størrelses-trinn?

**Valgt:** 3 — `sm`, `md`, `lg`.

**Hvorfor:**
- Industri-standard, dekker det meste.
- Omhu kan overstyre token-verdier i sin brand-fil hvis tetter SaaS-UI trengs.
- `xs` (mindre enn `sm`) blir konfliktfremmende i tette tabeller hvis tekst-størrelse går for langt ned. Bedre å håndtere via separate `<IconButton>` eller utility-overstyring.

---

## 3. Token-styrt radius via `--button-radius`

**Spørsmål:** Skal button-rounding være token-styrt eller hardkodet?

**Valgt:** Token-styrt. `--button-radius` defaulter til `--radius-md`, lagt til `:root` i begge token-pakker.

**Hvorfor:**
- Knapp-rounding er et signaturvalg per brand — pill, sharp, eller moderat.
- Hardkodet ville krevd å patche CSS for hver kunde.
- Brand-overstyring koster én linje: `:root { --button-radius: 0; }`.

---

## 4. Icon-API: props-basert (`leftIcon`/`rightIcon`)

**Spørsmål:** Props eller children for ikoner?

**Valgt:** Props (`leftIcon`, `rightIcon`, `iconOnly`).

**Hvorfor:**
- Eksplisitt API, type-safe, lett å oppdage.
- Button kan automatisk håndtere icon-størrelse via `--button-icon-size` (skalert med button-size).
- Button kan håndtere gap, alignment, a11y konsistent.
- `iconOnly`-modus håndteres som flag som setter `aspect-ratio: 1` og `padding-inline: 0`.

---

## 5. Loading: overlay-spinner med stabil bredde

**Spørsmål:** Hvordan vises loading-state?

**Valgt:** Tekst får `opacity: 0`, spinner sentreres absolutt over.

**Hvorfor:**
- Stabil bredde — ingen layout-hopping når loading toggler.
- Tekst forblir i DOM-en for skjermlesere; spinner er `aria-hidden="true"`.
- Pointer-events disables (samme som `disabled`).

---

## 6. Polymorphic `as` + auto-deteksjon av `href`

**Spørsmål:** Én Button eller separate Button/LinkButton?

**Valgt:** Én `Button` med polymorphic `as`-prop, og auto-rendering som `<a>` hvis `href` settes uten `as`.

**Hvorfor:**
- Konsistent med våre layout-primitiver (Container, Section, Stack, etc. har alle `as`).
- Eliminerer "hvilken button skal jeg bruke?"-spørsmålet for utvikleren.
- `as={Link}` fungerer for Next.js Link-integrasjon.
- `disabled` på `<a>` simuleres via `aria-disabled="true"` + fjernet `href` + `tabIndex: -1`.

---

## Tilleggsbeslutninger (TILLEGG: OK)

- **`fullWidth`-prop:** vanlig nok mønster (form-bunner, full-width CTA) til å fortjene egen prop. Setter `width: 100%`.
- **Active-state:** ingen translateY (amerikansk SaaS-pattern). I stedet: bakgrunnsfarge går til `--color-accent-active` (allerede definert via `color-mix()` i tokens). Subtilt for Scandi-min.
- **`--button-font-weight: 500`:** medium som default. Brand kan overstyre til 400 (lettere, editorial) eller 600 (tyngre, app-følelse).

---

**Konsekvenser samlet:**
- Én `<Button>`-komponent dekker primary, secondary, ghost, link, og semantiske toner.
- Variant-eksplosjon unngås via orthogonal `tone`-akse.
- `--button-radius` og `--button-font-weight` etablerer presedens for komponent-spesifikke brand-tokens — vi vil sannsynligvis gjøre samme for `<Input>`, `<Card>`, osv.
- Tone-implementasjonen (lokal CSS-variabel-overstyring) er et mønster vi vil gjenbruke for andre komponenter med semantiske farger (Toast, Alert, Badge).
- Polymorphic `as`-prop er nå etablert konvensjon på tvers av rammeverket — Container, Section, Stack, Cluster, Grid, Button. Alle interactive eller layout-komponenter bør følge dette mønsteret.

**Reverseringskostnad:** Lav-middels. Variant-navn endringer ville kreve søk-erstatt på tvers av prosjekter. Token-verdier kan endres uten konsekvenser for konsumenter.
