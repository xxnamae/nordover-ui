# Layout-primitiver

Fem layout-primitiver som dekker ~95% av sider og komponent-layouts: **Container**, **Section**, **Stack**, **Grid**, **Cluster**. Implementeres som React-komponenter med underliggende `@utility`-klasser slik at CMS/MDX-kontekster kan bruke samme primitiver uten React.

Bygger på `--container-*`, `--spacing-section`, `--page-padding` fra [nordover-arkitektur](nordover-arkitektur.md), og introduserer tre nye gap-tokens (se [tokens-patch](#nye-tokens-i-tokens-web-og-tokens-app)).

Se [decision 2026-05-27 — layout-primitiver-arkitektur](../decisions/2026-05-27-layout-primitiver-arkitektur.md).

## Felles prinsipper

- **Dual API:** Komponenter er primær — `<Container>`, `<Section>`, osv. Underliggende `@utility`-klasser (`container-default`, `section`, `stack`) er eksponert for non-React kontekster.
- **Eksplisitt komposisjon:** Section og Container er adskilte. Marketing-layout krever ofte full-width bakgrunn med begrenset innholdsbredde — det er bare mulig hvis primitivene er separate.
- **Container queries der det gir mening:** Section publiserer container-query-kontekst (`container-type: inline-size`). Switcher-pattern (komponent som bytter mellom flex/grid basert på containerbredde) er enkel å bygge på toppen.
- **Polymorphic `as`-prop på alle primitiver:** Lar utvikleren velge riktig semantisk HTML-tag (`<Section as="article">`).
- **Semantisk gap-skala:** `tight` / `component` / `section`. Tvinger utvikleren til å tenke "hva er forholdet mellom barna?" framfor å plukke et tilfeldig pixel-tall.

## Nye tokens i `tokens-web` og `tokens-app`

Lagt til i `:root` (ikke `@theme`, fordi de brukes via eksplisitte `@utility`-blokker, ikke Tailwind-generering).

**tokens-web:**
```css
:root {
  /* === Semantisk gap-skala === */
  --gap-tight: var(--space-2);     /* 8px — innenfor en komponent */
  --gap-component: var(--space-5); /* 24px — mellom relaterte komponenter */
  --gap-section: var(--space-8);   /* 48px — mellom seksjoner */
}
```

**tokens-app:**
```css
:root {
  /* Tettere defaults for SaaS-info-tetthet */
  --gap-tight: var(--space-1);     /* 4px (ikke 6px) */
  --gap-component: var(--space-4); /* 16px */
  --gap-section: var(--space-8);   /* 48px */
}
```

> `--gap-section` peker på `--space-8` (48px) i begge pakker — ikke på `--spacing-section` (den fluid clamp-en er en egen token for seksjons-padding).

## Delte gap-utilities

Disse utilities brukes av Stack, Cluster, Grid — én definisjon, gjenbrukbar:

```css
@utility gap-tight { gap: var(--gap-tight); }
@utility gap-component { gap: var(--gap-component); }
@utility gap-section { gap: var(--gap-section); }
```

---

## Container

**Formål:** max-width-wrapper + horizontal page-padding. Sentrerer innhold.

**Props:**
- `size`: `"narrow" | "default" | "wide" | "edge" | "prose"` (default: `"default"`)
- `as`: HTML-tag (default: `"div"`)

**Mapping til tokens:**

| `size` | max-width |
|---|---|
| `narrow` | `--container-narrow` (720px) |
| `default` | `--container-default` (1280px) |
| `wide` | `--container-wide` (1440px) |
| `edge` | `--container-edge` (100%) |
| `prose` | `--container-prose` (65ch) |

**CSS:**
```css
@utility container-narrow {
  width: 100%;
  max-width: var(--container-narrow);
  margin-inline: auto;
  padding-inline: var(--page-padding);
}
@utility container-default {
  width: 100%;
  max-width: var(--container-default);
  margin-inline: auto;
  padding-inline: var(--page-padding);
}
@utility container-wide {
  width: 100%;
  max-width: var(--container-wide);
  margin-inline: auto;
  padding-inline: var(--page-padding);
}
@utility container-edge {
  width: 100%;
  max-width: var(--container-edge);
  margin-inline: auto;
  padding-inline: var(--page-padding);
}
@utility container-prose {
  width: 100%;
  max-width: var(--container-prose);
  margin-inline: auto;
  padding-inline: var(--page-padding);
}
```

**React:**
```jsx
function Container({ size = "default", as: Tag = "div", className, children, ...rest }) {
  return (
    <Tag className={`container-${size} ${className ?? ""}`} {...rest}>
      {children}
    </Tag>
  );
}
```

**Bruk:**
```jsx
<Container size="prose">
  <article>...</article>
</Container>
```

---

## Section

**Formål:** vertikal rytme via `padding-block: var(--spacing-section)`. Publiserer container-query-kontekst slik at barn kan reagere på Section-bredde.

**Props:**
- `size`: `"default" | "sm" | "lg"` (default: `"default"`)
- `bg`: `"default" | "subtle" | "fg" | "accent"` (default: `"default"`)
- `as`: HTML-tag (default: `"section"`)

**CSS:**
```css
@utility section {
  container-type: inline-size;
  container-name: section;
  padding-block: var(--spacing-section);
}
@utility section-sm {
  padding-block: var(--spacing-section-sm);
}
@utility section-lg {
  padding-block: var(--spacing-section-lg);
}

@utility section-bg-subtle {
  background: var(--color-subtle);
}
@utility section-bg-fg {
  background: var(--color-fg);
  color: var(--color-bg);
}
@utility section-bg-accent {
  background: var(--color-accent);
  color: var(--color-accent-fg);
}
```

**React:**
```jsx
function Section({
  size = "default",
  bg = "default",
  as: Tag = "section",
  className,
  children,
  ...rest
}) {
  const sizeClass = size !== "default" ? `section-${size}` : "";
  const bgClass = bg !== "default" ? `section-bg-${bg}` : "";
  return (
    <Tag className={`section ${sizeClass} ${bgClass} ${className ?? ""}`.trim()} {...rest}>
      {children}
    </Tag>
  );
}
```

**Bruk:**
```jsx
<Section size="lg" bg="subtle">
  <Container size="default">
    <Stack gap="component">...</Stack>
  </Container>
</Section>
```

**Hvorfor adskilt fra Container:** marketing-sider trenger ofte full-width bakgrunn med innhold begrenset til Container-bredde. Sammenslåing ville tvinge bakgrunn til å være begrenset til container-bredden — en vanlig design-feil.

---

## Stack

**Formål:** vertikal flex-layout med semantisk gap.

**Props:**
- `gap`: `"tight" | "component" | "section"` (default: `"component"`)
- `align`: `"start" | "center" | "end" | "stretch"` (default: `"stretch"`)
- `as`: HTML-tag (default: `"div"`)

**CSS:**
```css
@utility stack {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);  /* default */
}
@utility stack-align-start { align-items: flex-start; }
@utility stack-align-center { align-items: center; }
@utility stack-align-end { align-items: flex-end; }
@utility stack-align-stretch { align-items: stretch; }
```

Gap-overstyring bruker delte `gap-*`-utilities.

**React:**
```jsx
function Stack({
  gap = "component",
  align = "stretch",
  as: Tag = "div",
  className,
  children,
  ...rest
}) {
  return (
    <Tag
      className={`stack gap-${gap} stack-align-${align} ${className ?? ""}`.trim()}
      {...rest}
    >
      {children}
    </Tag>
  );
}
```

**Bruk:**
```jsx
<Stack gap="component">
  <Heading />
  <Paragraph />
  <Button />
</Stack>

<Stack gap="section" align="center">
  <Hero />
  <Features />
  <CTA />
</Stack>
```

**Implementasjon-detalj:** flex med `gap`-property, ikke owl-selector (`> * + * { margin-top }`). Flex-gap er baseline i 2026 og enklere å resonnere om.

---

## Cluster

**Formål:** horisontal flex-layout med wrap. For nav-elementer, chip-rader, tag-lister, button-grupper.

**Props:**
- `gap`: `"tight" | "component" | "section"` (default: `"component"`)
- `align`: `"start" | "center" | "end" | "baseline"` (default: `"center"`)
- `justify`: `"start" | "center" | "end" | "between"` (default: `"start"`)
- `as`: HTML-tag (default: `"div"`)

**CSS:**
```css
@utility cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--gap-component);  /* default */
  align-items: center;
}
@utility cluster-align-start { align-items: flex-start; }
@utility cluster-align-center { align-items: center; }
@utility cluster-align-end { align-items: flex-end; }
@utility cluster-align-baseline { align-items: baseline; }

@utility cluster-justify-start { justify-content: flex-start; }
@utility cluster-justify-center { justify-content: center; }
@utility cluster-justify-end { justify-content: flex-end; }
@utility cluster-justify-between { justify-content: space-between; }
```

**React:**
```jsx
function Cluster({
  gap = "component",
  align = "center",
  justify = "start",
  as: Tag = "div",
  className,
  children,
  ...rest
}) {
  return (
    <Tag
      className={`cluster gap-${gap} cluster-align-${align} cluster-justify-${justify} ${className ?? ""}`.trim()}
      {...rest}
    >
      {children}
    </Tag>
  );
}
```

**Bruk:**
```jsx
<Cluster gap="tight">
  <Tag>Design</Tag>
  <Tag>Strategi</Tag>
  <Tag>Utvikling</Tag>
</Cluster>

<Cluster justify="between" align="center">
  <Logo />
  <Nav />
</Cluster>
```

---

## Grid

**Formål:** auto-responsiv grid uten media queries som default. Eksakt kolonneantall som overstyring.

**Props:**
- `min`: string (default: `"16rem"`) — minste kolonnebredde for auto-fit
- `columns`: number (optional) — hvis satt, overstyrer auto-fit
- `gap`: `"tight" | "component" | "section"` (default: `"component"`)
- `as`: HTML-tag (default: `"div"`)

**Hvis både `min` og `columns` settes:** `columns` vinner.

**CSS:**
```css
@utility grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(var(--grid-min, 16rem), 100%), 1fr));
  gap: var(--gap-component);
}
```

`min(var(--grid-min, 16rem), 100%)` sørger for at kolonner ikke "spruter" ut av container på små viewports — kollapser til 100% når plassen ikke holder.

**React:**
```jsx
function Grid({
  min = "16rem",
  columns,
  gap = "component",
  as: Tag = "div",
  className,
  style,
  children,
  ...rest
}) {
  const gridStyle = columns
    ? { ...style, gridTemplateColumns: `repeat(${columns}, 1fr)` }
    : { ...style, "--grid-min": min };
  const baseClass = columns ? "grid" : "grid-auto";
  return (
    <Tag
      className={`${baseClass} gap-${gap} ${className ?? ""}`.trim()}
      style={gridStyle}
      {...rest}
    >
      {children}
    </Tag>
  );
}
```

**Bruk:**
```jsx
{/* Auto-responsivt: kolonner kollapser når plass ikke holder */}
<Grid min="20rem" gap="component">
  <Card />
  <Card />
  <Card />
</Grid>

{/* Eksakt 3 kolonner uavhengig av viewport */}
<Grid columns={3}>
  <Stat />
  <Stat />
  <Stat />
</Grid>
```

**Hvorfor auto-fit som default:** dekker det meste av kort-rader, galleri, team-bilder, produkt-grids uten å skrive breakpoints. Eksakt-kolonner brukes når layout-intensjonen krever det (asymmetrisk design, talls-statistikker).

---

## Komposisjons-pattern

Typisk sidestruktur:

```jsx
<>
  <Section size="lg">
    <Container size="default">
      <Stack gap="component">
        <h1 className="text-display-xl">Headline</h1>
        <p className="text-body-lg">Subtitle</p>
        <Cluster gap="tight">
          <Button>Primær</Button>
          <Button variant="ghost">Sekundær</Button>
        </Cluster>
      </Stack>
    </Container>
  </Section>

  <Section bg="subtle">
    <Container>
      <Stack gap="section">
        <h2 className="text-heading-lg">Features</h2>
        <Grid min="22rem">
          <Card />
          <Card />
          <Card />
        </Grid>
      </Stack>
    </Container>
  </Section>
</>
```

Hver primitiv har ett ansvar. Komposisjonen er flat og lesbar.

---

## Container-query-bruksmønster

Section setter `container-type: inline-size`, så barn kan reagere på Section-bredde:

```css
/* Et kort som blir mer kompakt når Section er smal */
.card {
  padding: var(--gap-component);
}

@container section (max-width: 40rem) {
  .card {
    padding: var(--gap-tight);
  }
}
```

Dette betyr at samme `<Card>` blir kompakt når den ligger i en smal Section eller en smal Grid-kolonne, uten å vite noe om viewport. Mer gjenbrukbart enn media queries.

---

## Hva utelater vi bevisst

- **Center-primitiv** — `mx-auto`-utility eller `grid place-items-center` dekker.
- **Split-primitiv** — Grid med `columns={2}` + col-span dekker.
- **Sidebar-primitiv** — Grid + container query dekker.
- **Switcher-primitiv** — kraftig, men trengs ikke før det dukker opp et konkret behov. Kan legges til senere.
- **Header/Footer/Nav** — disse er **patterns**, ikke primitiver. De er sammensetninger av Container + Cluster + Stack. Hører hjemme i en framtidig "patterns"-familie.

## Implementeringsrekkefølge i Nordover-repoet

1. Legg til `--gap-*`-tokens i `:root` i både `tokens-web.css` og `tokens-app.css`.
2. Lag `layout.css` med alle `@utility`-blokker (`container-*`, `section*`, `stack*`, `cluster*`, `grid-auto`, `gap-*`).
3. Lag React-komponenter i `@nordover/ui/layout/`: `Container`, `Section`, `Stack`, `Cluster`, `Grid`.
4. Import-rekkefølge per app: `tokens-*.css` → `base.css` → `typografi.css` → `layout.css` → `prose.css` → `clients/<slug>.css`.

## Se også

- [Nordover-arkitektur — tokens](nordover-arkitektur.md)
- [Nordover-typografi](nordover-typografi.md)
- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: layout-primitiver-arkitektur](../decisions/2026-05-27-layout-primitiver-arkitektur.md)
