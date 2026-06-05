# ADR: Valgfritt JS-atferdslag (`nordover.js`)

- **Dato:** 2026-06-05
- **Status:** Vedtatt
- **Kontekst-lenker:** `docs/handoff/BEHAVIORS-JS.md`, `docs/wiki/topics/nordover-visjon.md`

## Kontekst

Nordover er distribuert som **ren CSS** — tokens og byggesteiner uten kjøretids-avhengigheter. De fleste komponentene trenger ingen JavaScript: accordion er bygget på native `<details>`, tooltip vises på `:hover`/`:focus`, tema og sidebar-tilstand drives av CSS (`:checked`/`:has`).

Noen få byggesteiner har likevel en interaksjon som **ikke kan uttrykkes i CSS alene**:

- **Tabs** — bytte synlig panel når en fane velges (+ pil-taster, roving tabindex)
- **Modal** — åpne/lukke, fokusfelle, Esc, fokus tilbake til utløser
- **Meny/dropdown** — vise/skjule flate, utenfor-klikk, Esc, pil-navigasjon
- **Drawer** (mobil-nav) — åpne/lukke panel + backdrop

Tidligere lå disse som *statiske* demoer i styleguiden, og konsumenter måtte skrive sin egen atferd. Det bryter løftet om å «minimere designtid på nye prosjekter».

## Beslutning

Vi shipper et **valgfritt, avhengighetsfritt atferdslag**: `docs/visual/behaviors/nordover.js`, lagt til i `package.json#files` og `exports["./behaviors"]`.

Prinsipper:

1. **Progressive enhancement** — filen er opt-in (`<script src=".../nordover.js">`). Uten den fungerer CSS-strukturen fortsatt; med den blir tabs/modal/meny/drawer interaktive.
2. **Kontrakt = data-attributter + ARIA**, ikke nye klassenavn. Den bruker de **samme klassekontraktene CSS-en allerede definerer** (`.is-open` for modal/drawer, `[hidden]` for paneler), så ingen nye visuelle kontrakter introduseres.
3. **Null avhengigheter, ingen build** — vanlig ES5-kompatibel IIFE, ingen globaler lekker, idempotent init (trygg å laste to ganger).
4. **Tilgjengelighet innebygd** — roving tabindex på tabs/meny, fokusfelle + fokus-retur på modal, Esc overalt, `aria-expanded`/`aria-selected`/`aria-hidden` holdes i synk.

## Hva laget IKKE er

For å vokte visjonen (Nordic-ro, lav kompleksitet):

- Ikke et komponent-rammeverk, ingen virtuell DOM, ingen reaktivitet eller state-store.
- Ingen animasjons-motor (CSS eier bevegelse via motion-tokens).
- Ingen runtime-avhengighet for resten av systemet — CSS-en er fortsatt fullverdig alene.
- Accordion (`<details>`) og tooltip forblir CSS/native — laget rører dem ikke (unntatt opt-in `data-accordion="single"` for eksklusiv åpning).

## Konsekvenser

- Konsumenter får interaktiv atferd «gratis» med ett `<script>`-tag, eller kan importere via `@xxnamae/nordover-ui/behaviors`.
- Rammeverket forblir «CSS-først»: JS er et tillegg, ikke en forutsetning.
- Ny offentlig kontrakt: data-attributtene (`data-modal-open`, `data-drawer-open`, `data-menu-open`, …) og ARIA-mønstrene er nå dokumentert i `BEHAVIORS-JS.md` og må behandles som stabile (endringer krever ny ADR).

## Alternativer vurdert

- **Kun styleguide-demoer (ikke shippet):** raskere, men løser ikke konsumentens reelle behov — forkastet.
- **Hoppe over JS:** etterlater modal/tabs/meny/drawer som «struktur uten liv» — forkastet.
- **Per-komponent web components:** mer innkapsling, men drar inn et tyngre paradigme og bryter «ren CSS»-enkelheten — forkastet for nå.
