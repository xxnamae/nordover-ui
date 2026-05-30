# Nordover-rammeverk — visuell oversikt

Arkitektur-diagrammer over hvordan alt henger sammen. For rendert design-spesimen (faktiske farger, typografi, knapper), åpne [`docs/visual/preview.html`](../../visual/preview.html) i en browser.

## Lag-diagram

Rammeverket er bygget i 5 lag. Hvert lag avhenger av de under, og eksponerer noe nytt til de over.

```mermaid
graph TD
  T["<b>Tokens</b><br/>tokens-web.css / tokens-app.css<br/>~60 tokens per pakke"]
  B["<b>Base CSS</b><br/>body-defaults, heading-rules<br/>text-wrap, lining-nums"]
  U["<b>Utilities</b><br/>typografi-klasser, gap-*<br/>hover-lift, focus-ring"]
  L["<b>Layout-primitiver</b><br/>Container · Section · Stack<br/>Grid · Cluster"]
  C["<b>Interactive</b><br/>Button · Input · Textarea<br/>Select · Checkbox · Radio · Switch<br/>Field · Form"]
  P["<b>Patterns (ikke drodlet)</b><br/>Card · Modal · Toast<br/>Tooltip · Menu · Tabs · ..."]

  T --> B
  T --> U
  B --> C
  U --> L
  U --> C
  L --> P
  C --> P

  style T fill:#e8f0ff
  style B fill:#f0f0f0
  style U fill:#f0f0f0
  style L fill:#ffffff
  style C fill:#ffffff
  style P fill:#fff5e8,stroke-dasharray: 5 5
```

## Token-namespace

To token-pakker for to bruksområder. Brand-overstyring per kunde via en tredje CSS-fil.

```mermaid
graph LR
  W["<b>tokens-web</b><br/>Editorial Scandi-min<br/>16px base · ratio 1.333<br/>fluid type opp til 160px"]
  A["<b>tokens-app</b><br/>SaaS info-tetthet<br/>14px base · statisk skala<br/>kompakte spacing"]

  W --> M["Marketing-nettsider<br/>(Nordover-leveranser)"]
  A --> S["SaaS-produkter<br/>(Omhu)"]

  BR["<b>clients/&lt;slug&gt;.css</b><br/>brand-overstyringer"] --> M
  BR --> S

  style W fill:#e8f0ff
  style A fill:#fff0e8
  style BR fill:#f8f0ff
```

## Komponent-avhengighet (utvalgt)

Hvordan komponenter komponerer fra primitivene. Stiplet = pattern, ikke implementert.

```mermaid
graph TD
  subgraph "Form-familie"
    Form --> Field
    Field --> Input
    Field --> Textarea
    Field --> Select
    Field -.aria-describedby.-> Help
    Field -.aria-describedby.-> Error
  end

  subgraph "Layout"
    Section --> Container
    Container --> Stack
    Container --> Cluster
    Container --> Grid
  end

  subgraph "Patterns (ikke drodlet)"
    Card -.-> Stack
    Card -.-> HoverLift["hover-lift utility"]
    Card -.-> BorderCard["--border-card token"]
    Modal -.-> ShadowModal["--shadow-modal token"]
    Toast -.-> ColorAccent["lokal --color-accent overstyring<br/>(samme pattern som Button tone)"]
  end

  style Card fill:#fff5e8,stroke-dasharray: 5 5
  style Modal fill:#fff5e8,stroke-dasharray: 5 5
  style Toast fill:#fff5e8,stroke-dasharray: 5 5
```

## Import-rekkefølge i en app

Hvordan CSS-filene stables i et Nordover-prosjekt.

```mermaid
graph LR
  T["tokens-web.css<br/>eller tokens-app.css"] --> Base["base.css<br/>body, h1-h6, table"]
  Base --> Typ["typografi.css<br/>semantiske klasser"]
  Typ --> Layout["layout.css<br/>Container, Section, ..."]
  Layout --> Elev["elevation.css<br/>hover-lift"]
  Elev --> Btn["buttons.css"]
  Btn --> Forms["forms.css"]
  Forms --> Prose["prose.css"]
  Prose --> Brand["clients/&lt;slug&gt;.css<br/>brand-overstyring"]

  style T fill:#e8f0ff
  style Brand fill:#f8f0ff
```

## Decision-tree: når bruker du hva?

```mermaid
graph TD
  Q1{Skal innhold rammes inn?}
  Q1 -- "Visuelt skille (kort, panel)" --> Q2{Klikkbar?}
  Q1 -- "Bare grupperer" --> Stack["Stack med gap"]
  Q1 -- "Flyter over annet innhold" --> Q3{Hvor høyt?}

  Q2 -- Ja --> BorderHover["Card med border + hover-lift"]
  Q2 -- Nei --> Border["Card med border alene"]

  Q3 -- "Lavt (tooltip)" --> ST["shadow-tooltip"]
  Q3 -- "Middels (popover, dropdown)" --> SP["shadow-popover"]
  Q3 -- "Høyt (modal)" --> SM["shadow-modal"]
  Q3 -- "Høyest (drawer)" --> SD["shadow-drawer"]

  style BorderHover fill:#fff5e8,stroke-dasharray: 5 5
  style Border fill:#fff5e8,stroke-dasharray: 5 5
```

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Visuell spesimen (HTML)](../../visual/preview.html) — alle tokens og primitiver rendret
- [Decisions-mappe](../decisions/)
