# Layout-primitiver — arkitektur

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter tokens og typografi måtte vi bestemme settet av layout-primitiver, deres API, og hvordan de komponerer. Seks koplete spørsmål besluttes samlet siden de definerer hele family-en.

---

## 1. Primitivt sett: Container, Section, Stack, Grid, Cluster

**Spørsmål:** Hvor mange primitiver, og hvilke?

**Valgt:** Fem — Container, Section, Stack, Grid, Cluster.

**Hvorfor:**
- Dekker ~95% av layouts i marketing og SaaS.
- Hver primitiv har ett ansvar: bredde-begrensning (Container), vertikal rytme (Section), vertikal stack (Stack), grid (Grid), horisontal wrap (Cluster).
- Center, Split, Sidebar utelates fordi Tailwind-utilities eller Grid dekker.
- Switcher utelates fordi den er kompleks og mangler konkret use-case. Kan legges til senere.

---

## 2. Dual API: komponenter + utility-klasser

**Spørsmål:** React-komponenter, Tailwind-utilities, eller begge?

**Valgt:** Begge. Komponent er primær; `@utility`-klasser er eksponert for non-React kontekster (CMS rikstekst, MDX).

**Hvorfor:**
- React-stack krever komponenter for ergonomi og type-safety.
- Payload-rikstekst og MDX renderer HTML — der trenger vi klasser, ikke komponenter.
- Komponenten setter klassene; klassene gjør all jobben. Ingen duplisering av logikk.

---

## 3. Eksplisitt Container/Section-komposisjon

**Spørsmål:** Skal Section auto-rendre Container, eller skal de være adskilte?

**Valgt:** Adskilte. Bruker komponerer eksplisitt: `<Section><Container>...</Container></Section>`.

**Hvorfor:**
- Marketing-layouts trenger ofte full-width bakgrunn (`<Section bg="subtle">`) med innhold begrenset til Container-bredde. Sammenslåing ville tvinge bakgrunn til container-bredden — en vanlig design-feil.
- Eksplisitt komposisjon er mer fleksibelt og mer lesbart selv om det er 1-2 ekstra tegn.

---

## 4. Auto-responsiv Grid som default

**Spørsmål:** Grid med media queries eller med auto-fit?

**Valgt:** Auto-fit som default (`grid-template-columns: repeat(auto-fit, minmax(min(var(--grid-min), 100%), 1fr))`). Eksakt kolonneantall via `columns`-prop overstyrer.

**Hvorfor:**
- Dekker det meste av kort-rader, galleri, produkt-grids uten å skrive breakpoints.
- Kolonner kollapser automatisk basert på tilgjengelig plass — fungerer i en hvilken som helst container, ikke bare på viewport-nivå.
- `min(var(--grid-min), 100%)` sørger for at kolonner ikke spruter ut av container på små viewports.
- `columns`-prop er en eskapé når layout-intensjon krever eksakt N kolonner (asymmetri, talls-statistikker).
- Hvis både `min` og `columns` settes, vinner `columns`.

---

## 5. Container queries der det gir mening (B + C-tendens)

**Spørsmål:** Skal primitiver bruke container queries internt?

**Valgt:** Section publiserer container-query-kontekst (`container-type: inline-size`, `container-name: section`). Andre primitiver bruker container queries når det er åpenbart behov.

**Hvorfor:**
- Container queries er bredt støttet i 2026.
- En `<Card>` som ligger i en smal Grid-kolonne eller en smal Section kan reagere på sin faktiske container, ikke viewport — mer gjenbrukbart.
- Vi tvinger ikke container queries på utvikleren; vi gjør det enkelt å bruke dem.
- Media queries er fortsatt riktig verktøy for page-level layout (eks. mobile-nav vs desktop-nav).

---

## 6. Polymorphic `as`-prop på alle primitiver

**Spørsmål:** Skal hver primitiv ha en `as`-prop?

**Valgt:** Ja.

**Hvorfor:**
- Semantisk HTML er kritisk for a11y og SEO. Bruker velger `as="article"`, `as="aside"`, `as="header"`.
- `as`-prop koster ~3 linjer kode per komponent.
- Default-tag matcher det vanligste use-caset: `<Section>` rendrer `<section>`, `<Container>` rendrer `<div>`, osv.

---

## 7. Semantisk gap-skala (Valg 6)

**Spørsmål:** T-shirt-skala (`xs/sm/md/lg/xl`) eller semantisk (`tight/component/section`)?

**Valgt:** Semantisk.

**Hvorfor:**
- Tvinger utvikleren til å tenke "hva er forholdet mellom barna?" — `gap="component"` signaliserer "disse hører sammen som en gruppe", `gap="section"` signaliserer "disse er separate seksjoner".
- T-shirt-skala (`gap="md"`) er meningsløs uten kontekst.
- Bare tre verdier reduserer beslutnings-tretthet.
- Tailwind-utilities (`gap-4`, `gap-8`) er fortsatt tilgjengelige som eskapé for finkontroll.

**Tokens-implementasjon:**
- `--gap-tight`, `--gap-component`, `--gap-section` legges til i `:root` i begge token-pakker.
- tokens-web: `0.5rem` / `1.5rem` / `var(--spacing-section)`.
- tokens-app: `0.375rem` / `1rem` / `var(--spacing-section)` (tettere).

---

## Sub-beslutninger (Q1-Q3)

**Q1: Ingen separat `<Section size="compact">`-modus.** `--spacing-section` er allerede fluid via `clamp()` i tokens-web; mobil-verdien er 64px. `size="sm"` dekker enda mindre behov.

**Q2: Stack/Cluster bruker `display: flex` + `gap`-property.** Ikke owl-selector (`> * + * { margin-top }`). Flex-gap er baseline i 2026 og enklere å resonnere om.

**Q3: Grid — `columns` vinner over `min` hvis begge settes.** Eksplisitt overstyrer implisitt auto-fit.

---

**Konsekvenser samlet:**
- Komponentbiblioteket starter med 5 primitiver, ikke 10+. Mindre overflate å vedlikeholde.
- CMS/MDX-kontekster har samme layout-muligheter som React-komponenter.
- Section som container-query-context gir et fundament for kontekst-bevisste underkomponenter (Card, etc.) uten media queries.
- Nye `--gap-*`-tokens i begge token-pakker — total token-overflate vokser litt, men gap-skalaen er sentral nok til å fortjene plassen.

**Reverseringskostnad:** Lav. Primitivene er små og kjente patterns. Hvis vi vil legge til Switcher eller bytte gap-skala-stil senere, koster det noen line-edits per komponent.
