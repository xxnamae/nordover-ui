# Patterns basis — batch 1

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter at fundamentet + 6 komponentfamilier var komplett, ble vi enige om hybrid arbeidsmåte for patterns: batch-modus (C) for konvensjonelle komponenter, sparring-modus (A) for arkitektur-tunge. Denne batchen dekker 10 konvensjonelle composite components i én økt.

**Komponenter i batch:** Tag, Badge, Avatar, Spinner, Tooltip, Breadcrumbs, Pagination, Skeleton, Divider, Kbd.

**Hvorfor batch-modus for disse:**
- Alle har lav arkitektur-overflate — konvensjonene er etablerte i industrien.
- Ingen krever nye tokens — komponert fra eksisterende `--color-*`, `--shadow-*`, `--border-*`, `--gap-*`.
- Få reelle valg per komponent (alternativene er stort sett bare "konvensjonell vs eksotisk", og vi velger alltid konvensjonell).
- Batch-skriving sparer 8-10 økter med marginal beslutnings-verdi.

---

## Sentrale konvensjons-valg

**Tag vs Badge:** Tag er for free-form labels (kategorier, statuser), Badge er for tellere og dots. To separate komponenter, ikke en med variant-prop.

**Tooltip i basis-versjon:** ren CSS uten smart positionering. Vi aksepterer at den ikke flipper når den treffer viewport-kanten. For 95% av use cases (knappetooltip, ikon-forklaring) er det godt nok. Komplekse tilfeller går via Radix Tooltip senere (egen drodling).

**Spinner-implementering:** ren CSS border-trick (border på alle sider + transparent på én, rotert). Lett, ingen SVG, currentColor-arvbar.

**Avatar fallback:** initialer auto-genereres fra `name`-prop (`"Eirik Foleide"` → `"EF"`). Bg er `--color-subtle` som default — ingen hash-til-farge-magi. Brand-overstyring kan introdusere hash-bg hvis ønsket.

**Pagination-algoritme:** vis first + last + (current ± siblingCount), fyll med ellipsis. Konvensjonell, dekker det meste.

**Skeleton-animasjon:** shimmer-gradient (200% bg-size, animert background-position). Reduced-motion: ikke `none` (gir false-positive "ferdig lastet"), men statisk opacity i stedet.

**Tone-pattern på Tag:** samme pattern som Button — lokal `--color-accent`-overstyring. Konsistent.

---

## Tilleggsbeslutninger

- **Ingen nye tokens** introdusert i denne batchen. Alle komponenter komponert fra eksisterende.
- **A11y konvensjoner:** Tooltip via `aria-describedby`, Badge dot med `aria-label`, Pagination i `<nav aria-label="">`, Skeleton-foreldre med `aria-busy="true"`.
- **Reduced motion:** Spinner saktes ned (ikke av), Skeleton statisk opacity (ikke usynlig).
- **Sizes følger eksisterende skala:** sm/md/lg der relevant — matcher Buttons.

---

## Hva som er bevisst NIKKE inkludert i denne batchen

Disse hørte naturlig hjemme, men ble løftet ut fordi de krever egen sparring:

- **Card** — har varianter (bordered/elevated/subtle) som er reelt arkitekturvalg. Egen drodling.
- **Modal/Dialog** — focus-trap, scroll-lock, portals, escape-handling. Egen drodling.
- **Drawer** — som Modal, pluss slide-animasjon og side-valg.
- **Tabs** — kontrollert vs ukontrollert state, ARIA-pattern, animert indicator.
- **Accordion** — single vs multi expansion, animasjons-strategi.
- **Menu/Dropdown** — Radix vs custom, keyboard nav, sub-menus.
- **Toast/Alert** — auto-dismiss, queue, position, tone-akse igjen.

Disse hører hjemme i batch 2 (patterns fase 2, mode A — én økt per).

---

**Konsekvenser samlet:**
- Komponentbiblioteket vokser med 10 stk på én økt — fra 8 til 18 komponenter totalt.
- Pattern for batch-modus etablert: konvensjonelle komponenter spec'es uten lang sparring, decision-fil dokumenterer kun avvik fra konvensjon.
- Tag/Badge etablerer tone-pattern også utenfor Button — bekrefter at lokal `--color-accent`-overstyring er Nordovers standardmodell for fargestyring per komponent-instans.

**Reverseringskostnad:** Lav per komponent. Hvis en pattern viser seg å være mer komplekst enn antatt (eks. Tooltip krever Radix), kan vi bytte implementering uten å touche API.
