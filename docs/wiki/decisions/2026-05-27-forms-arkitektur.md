# Forms-arkitektur

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Forms er den siste og største komponentfamilien i Nordover-rammeverket. Den dekker både korte marketing-skjemaer (kontakt, newsletter) og komplekse SaaS-skjemaer (Omhu-settings, multi-step). Syv koblede valg om komponentsett, komposisjon, native vs custom, validering, sizing, labels.

---

## 1. Komponentsett: 6 primitiver + Field + Form (totalt 8)

**Valgt:** Input, Textarea, Select, Checkbox, Radio, Switch, Field (composer), Form (wrapper).

**Bevisst utenfor:** Datepicker, Combobox, MultiSelect, FileUpload, Slider, RichTextEditor.

**Hvorfor:**
- Disse 8 dekker ~80% av skjemaer.
- Komplekse komponenter (Datepicker, Combobox) krever egne arkitekturvalg (Radix UI, native, eller egen state-maskin). Hører hjemme i en framtidig "patterns"-familie.
- Switch er ikke et nativt HTML-element, men inkluderes fordi pattern er vanlig og verdt å standardisere.

---

## 2. `<Field>`-wrapper som primær API + render-prop som eskapé

**Valgt:** Composer-API med props (`<Field label="..." help="..." error="...">{children}</Field>`). Render-prop for spesialtilfeller (`<Field>{({ id, describedBy }) => ...}</Field>`).

**Hvorfor:**
- Composer-API dekker 90% av use cases med minst boilerplate.
- Field genererer `id`, kobler `htmlFor`/`aria-describedby`/`aria-invalid` automatisk — utvikleren glemmer ikke a11y-attributer.
- Render-prop løser cases der ett field har flere inputs (eks. landskode + telefonnummer).
- Implementeres via React-context: Field setter `{ id, describedBy, invalid, required }`; Input leser via `useField()`.

---

## 3. Native + custom visuelt lag (hybrid)

**Valgt:**

| Komponent | Strategi |
|---|---|
| Input, Textarea | Native, styled |
| Select | Native, styled (custom chevron via background-image) |
| Checkbox, Radio | Native input + `appearance: none` + custom visuell ved siden av |
| Switch | Custom (checkbox semantisk, `role="switch"`) |

**Hvorfor:**
- Native gir a11y, IME-støtte, autofill, form-submission gratis.
- Custom visuell-lag på native input gir styling-kontroll uten å miste a11y.
- Native Select er rotete cross-browser, men full custom (Radix) er overkill for enkle dropdowns. Hybrid: native styled som default, separat `<SelectMenu>` (Radix-basert) for komplekse cases (søk, multi-select, custom rendering) i fremtiden.
- Switch har ingen native ekvivalent. Bygges som checkbox semantisk med `role="switch"`.

---

## 4. Pluggbar validering — Field viser bare `error`

**Valgt:** Field har ingen intern valideringslogikk. `error`-prop er en string som vises og applikerer error-styling.

**Hvorfor:**
- Form-libraries (react-hook-form, conform, tanstack-form) er en aktiv del av React-økosystemet. Vi vil ikke duplikere eller låse oss til én.
- Field er en visuell komponent; validering er domene-logikk.
- Konsumenter kan bruke hvilken som helst form-library, eller egen state.
- `success`-prop tilgjengelig for confirmed validation (grønn border, checkmark).
- `<Input invalid />` kan brukes uten Field for spesialtilfeller.

---

## 5. Sizing: sm/md/lg + Form-density-prop

**Valgt:** Tre størrelser matcher Buttons. `<Form density="compact">` setter alle nested inputs til `size="sm"` via context.

**Hvorfor:**
- Konsistens med Button-systemet.
- SaaS-skjemaer er ofte ensartet dense. `density`-prop på Form sparer å sette `size="sm"` på hvert eneste Field.
- Padding-skala speilet fra Buttons med litt mindre `padding-inline` (inputs er bredere).

---

## 6. Top-labels, ingen floating

**Valgt:** Labels alltid over input. Ingen floating-label-modus.

**Hvorfor:**
- Top-labels er mest skannbart og mest a11y-kompatibelt.
- Floating labels er editorial-fristende, men har kjente a11y-issues (skjult label når feltet er tomt, og lest-rekkefølge-problemer for skjermlesere).
- Left-labels droppet — bedre å introdusere som `<Form labelPosition="left">` senere hvis dense SaaS-skjemaer trenger det.

---

## 7. "(valgfritt)"-marking som default, asterisk via opt-in

**Valgt:** Default: alt er required med mindre annet er sagt. Optional får "(valgfritt)"-suffiks i label. `<Form requiredMarking="asterisk">` bytter til asterisk-marking globalt.

**Hvorfor:**
- I korte skjemaer er det mer brukervennlig å markere unntakene (optional) enn regelen (required).
- Asterisk-marking er enkel å oversee — særlig for ikke-tekniske brukere.
- Compliance-kontekster (juridiske skjemaer, der "required" er kontraktsbegrep) kan trenge asterisk. Opt-in dekker dette uten å være default.

---

## Tilleggsbeslutninger

- **`--input-*`-tokens** lagt til `:root` i begge token-pakker: `--input-radius`, `--input-border-color`, `--input-border-color-focus`, `--input-border-color-error`, `--input-bg`, `--input-bg-disabled`.
- **`<Form>` har `noValidate` som default** — vi bruker custom error-rendering, ikke browser-default (som er stygt og engelsk).
- **Checkbox/Radio/Switch har label til høyre, ikke over.** Bruker ikke Field-wrapper, men har eget `label`-prop. Pattern er konsistent (label + input + help + error), bare layout-en er annerledes.
- **Fieldset/Legend** brukt for å gruppere radio-knapper. Egen tynn wrapper.

---

**Konsekvenser samlet:**
- 8 React-komponenter dekker primær-forms-bruk uten å gjøre antakelser om form-library.
- Field-context er gjenbrukbart pattern — kan brukes til future composer-wrappers (eks. `<FormSection label="..."><Field>...</Field></FormSection>`).
- Token-overflate vokser igjen — `--input-*` (6 tokens) lagt til hver pakke. Konsekvent med `--button-*`-pattern.
- "(valgfritt)"-pattern er et tydelig produktvalg — det kommuniserer en holdning om brukervennlighet over konvensjon. Kan blir et signaturtrekk for Nordover-leveranser.

**Reverseringskostnad:** Middels. Field-API endringer ville rippe gjennom alle skjemaer i alle prosjekter. Token-endringer er trygge. Bytte til floating labels eller annen valideringsstrategi er en arbeids-jobb, men ingen produkt-bryt.
