# Typografi-utilities — arkitektur

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter at tokens-laget var spec'et, dukket fem koblede spørsmål opp om hva som skulle bygges på toppen: semantiske typografi-klasser, heading-defaults, prose-strategi, display-font-applikasjon, og site-wide CSS-defaults. Disse er tett koplet og besluttes samlet.

---

## 1. Hybrid semantiske klasser

**Spørsmål:** Atomic Tailwind-utilities, semantiske komposittklasser, eller hybrid?

**Valgt:** Hybrid.

**Hvorfor:**
- Semantiske klasser (`text-display-xl`, `text-heading-lg`, `text-body`, `text-eyebrow`, `text-caption`) fanger 90% av typografi-bruken med én klasse.
- Atomic utilities forblir tilgjengelige for engangstilfeller.
- Forhindrer både den vanlige Tailwind-atomic-suppen og den vanlige semantiske-klasse-eksplosjonen.

**Klassesett:**
- Display: `text-display-xl` (text-8xl), `text-display-lg` (text-6xl), `text-display-md` (text-4xl)
- Heading: `text-heading-lg` (text-3xl), `text-heading-md` (text-2xl), `text-heading-sm` (text-xl)
- Body: `text-body-lg` (text-lg), `text-body` (text-base), `text-body-sm` (text-sm)
- Spesielle: `text-eyebrow` (uppercase, wide-tracking, muted), `text-caption` (xs, muted)

---

## 2. Heading-defaults: sensible globals uten size

**Spørsmål:** Skal `<h1>`-`<h6>` ha default styling, eller leve med Tailwind-preflight?

**Valgt:** Globale defaults for font-family, weight, leading, letter-spacing, text-wrap — men IKKE size.

**Hvorfor:**
- Marketing-sider varierer size per kontekst — globalt h1-size ville feile halvparten av tiden.
- Men hvis size er det eneste man må sette, blir det rask å skrive.
- Konvensjon: glemmer du å sette klasse, ser headingen ut som "noe bestemt", men du må fortsatt være bevisst på størrelse.

---

## 3. Egen `.prose` framfor `@tailwindcss/typography`

**Spørsmål:** Plugin eller egen implementasjon for lang-form-innhold?

**Valgt:** Egen `.prose`.

**Hvorfor:**
- Plugin er kalibrert for amerikansk blog-aesthetic (bold headings, mye paragraf-margin).
- Scandi-min editorial trenger: regular-weight headings, tight kontroll over vertikal rytme, smal prose-bredde (`65ch`), display-font på blockquotes, presis link-underline-offset.
- Egen implementasjon = ~100 linjer CSS som vi kan vedlikeholde. Plugin = svart boks vi alltid ville overstyrt.
- Inkluderer opt-in `.prose-editorial`-modifier for drop-cap på første paragraf.

---

## 4. Display-font koblet til intensjon, ikke til tag

**Spørsmål:** Når skal `--font-display` (Inter Tight) brukes automatisk?

**Valgt:** Koplet til semantiske klasser (`text-display-*`, `text-heading-*`), ikke til HTML-tag.

**Hvorfor:**
- `<h2>` kan brukes til mye: editorial display, SaaS-dashboard-tabellkapittel, accordion-header. Display-font er feil for noen av disse.
- Semantiske klasser signaliserer intensjon — utvikleren har valgt "dette er display/heading".
- Atomic-utilities som `text-3xl` får ikke automatisk display-font; utvikleren må kombinere med `font-display` hvis det er ønsket.

**Konsekvens:** Base-laget setter også display-font på `h1`-`h6` (for fallback hvis ingen klasse settes), men semantiske klasser er kanonisk vei.

---

## 5. Site-wide defaults for text-wrap + lining-nums

**Spørsmål:** Skal moderne CSS-features settes globalt?

**Valgt:** Ja.

**Defaults:**
- `text-wrap: pretty` på `body` (bedre rag/orphans).
- `text-wrap: balance` på `h1`-`h6` (siste linje ikke enslig).
- `font-variant-numeric: lining-nums` på `body` (moderne tall-stil).
- `font-variant-numeric: lining-nums tabular-nums` på `table` (tall aligner i tabeller).

**Hvorfor:**
- Bred browser-støtte i 2026.
- Editorial-aesthetic krever balanced headings.
- Tabell-aligning er forventet i SaaS-apper (Omhu).
- Atomic utilities (`text-balance`, `tabular-nums`, `oldstyle-nums`, `small-caps`) finnes for overstyringer.

---

## Token-collision avdekket og dokumentert

`--font-display` (family) og `--font-weight-display` (weight) ville begge generert `font-display`-utility i Tailwind v4.

**Fix:** Flytt `--font-weight-display` fra `@theme` til `:root` i `tokens-web`. Token beholder semantikk; eksponeres ikke som utility; brukes via `var(--font-weight-display)` direkte i semantiske klasser.

Dette er en patch til [tokens-web-spec](../topics/nordover-arkitektur.md), ikke en separat decision.

---

**Konsekvenser samlet:**
- Komponenter får en lesbar, intensjons-bærende klasse-syntaks.
- Editorial-konvensjoner er på som default; utviklere må huske å skru av, ikke skru på.
- Egen `.prose` betyr én CSS-fil å vedlikeholde, men ingen plugin-versjons-låsninger.
- Token-collision-fix er en presedens: når vi navngir framtidige semantiske weight/family-tokens, må vi sjekke at de ikke kolliderer i Tailwind utility-namespace.

**Reverseringskostnad:** Middels. Hvis vi senere vil bytte fra egen `.prose` til plugin, eller kappe semantiske klasser tilbake til atomic-only, er det en arbeids-jobb på tvers av komponenter — men ingen produkt-bryt.
