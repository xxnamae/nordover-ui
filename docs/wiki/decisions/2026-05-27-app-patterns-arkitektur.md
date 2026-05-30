# App-patterns arkitektur (fase 2A)

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Fase 2A fullfører app-rammeverket med arkitektur-tunge composite components. Forskjellen fra fase 2B (web section-patterns) er at disse har **reelle interaksjons-arkitekturvalg** — focus-trap, scroll-lock, portal, keyboard-nav, drag/drop, kontrollert state.

13 patterns spec'et: Card, Modal, Drawer, Side-panel, Toast/Alert, Sidebar Nav, Tabs, Accordion (animated), Menu/Dropdown, Command Palette, Data Table, Activity Stream, Kanban Board.

---

## 1. Radix Primitives som underliggende fundament

**Spørsmål:** Skal vi bygge alt fra null, bruke Radix, eller en annen library?

**Valgt:** Radix Primitives (`@radix-ui/react-*`) for alle interaksjons-komplekse komponenter. Vår styling oppå.

**Hvorfor:**
- Radix er industri-standard 2026 for headless React-komponenter (brukes av Vercel, shadcn/ui, Linear, etc.).
- A11y er gjort riktig: focus-trap, keyboard-nav, ARIA-roller, screen reader-annonsering.
- Headless = ingen styling-låsing. Vi eier alt visuelt.
- MIT-lisens, ingen telemetri, ingen tracking.
- Tree-shake-bar — kun det du importerer havner i bundle.
- Bytte-mulighet bevart: hvis vi senere vil bytte, kan vi swap-out én komponent av gangen siden API-et er stort sett identisk på tvers av headless-libraries.

**Alternativer forkastet:**
- **Bygge alt fra null:** for mye a11y-arbeid (fokus-trap alene er en 200-linje-bibsel).
- **Headless UI (Tailwind Labs):** mindre overflate, ikke like aktiv som Radix i 2026.
- **Material UI / Chakra:** for mye styling-overhead, vi mister kontroll over visuelt uttrykk.

---

## 2. Andre library-valg per pattern

**Command Palette: `cmdk`** (Vercel/Paco Coursey)
- De facto standard for ⌘K-paletter (brukt av Vercel dashboard, Linear).
- Headless, søk + keyboard-nav + grupper innebygget.

**Data Table: `@tanstack/react-table`**
- Headless, ingen styling.
- Håndterer sortering, filtering, paginering, kolonne-bredder, row-selection.
- Vi styler oppå med våre tokens.

**Kanban drag/drop: `@dnd-kit/core` + `@dnd-kit/sortable`**
- Moderne, a11y-fokusert (keyboard-drag støttet ut av boksen).
- Mer aktivt vedlikeholdt enn react-beautiful-dnd.

**Hvorfor disse spesifikt:** alle er headless, MIT, well-maintained, tree-shake-bare. Total tilleggsbundle ~30-40kb gzip.

---

## 3. Portal-pattern via NordoverProvider

**Spørsmål:** Hvor mounter overlays?

**Valgt:** `<NordoverProvider>` på app-rot inkluderer Radix' `Portal`-targets + Toast-viewport + global Command Palette + tooltip-provider.

**Hvorfor:**
- Én provider å huske på, alle overlays "bare fungerer".
- Eliminerer "hvor er den portal-rooten min?" spørsmålet.
- ToastProvider og TooltipProvider hører hjemme her uansett pga queue/timer-state.

---

## 4. Card med 4 varianter

**Spørsmål:** Hvilke variant-akser?

**Valgt:** `variant` (`bordered` | `elevated` | `subtle` | `interactive`).

**Hvorfor:**
- `bordered` (default): kort med kun border, ingen shadow. Scandi-min basisuttrykk.
- `elevated`: shadow-card-hover. Apple-aktig.
- `subtle`: bg-subtle uten border. Grupperer uten å rame inn.
- `interactive`: bordered + hover-lift. For klikkbare kort.
- 4 dekker behov uten å eksplodere overflate.

---

## 5. Modal vs Drawer vs Side-panel — distinkte komponenter

**Spørsmål:** Skal disse være én komponent med posisjons-prop, eller separate?

**Valgt:** Tre separate komponenter med ulik bruks-intensjon.

**Hvorfor:**
- **Modal:** sentrert overlay, fokus-blokkering, "stopper deg". For confirmations, viktige skjemaer.
- **Drawer:** side-slide overlay, fokus-blokkering, "tar over en kontekst". For settings, multi-step.
- **Side-panel:** inline-layout endring, IKKE overlay, IKKE focus-trap. For detalj-views i tre-kolonne-layouter (Linear-pattern).

Side-panel er strukturelt anderledes (layout-skift, ikke overlay). Drawer og Modal deler underliggende Radix Dialog men har distinkte animasjoner og bruksintensjoner.

---

## 6. Sidebar Nav som signaturkomponent

**Spørsmål:** Hvor mange features ut av boksen?

**Valgt:** Multi-level, collapsible sections, expand/collapse hele sidebar, sub-items, active-state-tracking, mobile drawer-modus.

**Hvorfor:**
- Sidebar er **THE** signature element i Linear/Stacked/de fleste moderne SaaS-apper.
- Underspec'er vi her, må hver konsument bygge sin egen — bryter med rammeverk-formålet.
- CSS-only collapse via `data-collapsed`-attribute holder JavaScript minimalt.
- Mobile-modus: skjult by default, åpnes som drawer via hamburger. Reagerer på `@media (max-width: 48rem)`.

---

## 7. FAQ (web) vs Accordion (app) — to ulike implementeringer

**Spørsmål:** Bør FAQ og Accordion være samme komponent?

**Valgt:** Nei — FAQ bruker native `<details>`, Accordion bruker Radix.

**Hvorfor:**
- **FAQ-kontekst:** marketing-side, lavt JS-fotavtrykk ønsket, ingen kontrollert state nødvendig. Native løser dette.
- **Accordion-kontekst:** SaaS-bruk i settings/forms, kontrollert state ønsket, smooth animasjon viktig. Radix gir dette.
- Samme komponent ville vært et kompromiss som ikke tjente noen.

---

## 8. Tabs med statisk border-indicator (foreløpig)

**Spørsmål:** Smooth animated indicator eller statisk border?

**Valgt:** Statisk `border-bottom` på aktive trigger. Smooth indicator senere hvis behov.

**Hvorfor:**
- Statisk er enklere, mindre JS, mindre kode.
- Smooth animated indicator krever JS for å måle posisjoner og animere.
- Marginal UX-gevinst — kan oppgraderes senere uten breaking change.

---

## 9. Command Palette som standard del av app-rammeverket

**Spørsmål:** Skal command palette være innebygget eller opt-in?

**Valgt:** Innebygget via NordoverProvider med ⌘K-binding. Action-registry per app.

**Hvorfor:**
- Moderne SaaS-must (Linear, Stripe, Vercel, Notion, alle har det).
- ⌘K-konvensjon er internasjonal — brukere vet hva de skal trykke.
- Apps registrerer actions; rammeverket håndterer UX.

---

## 10. Toast med queue-håndtering

**Spørsmål:** Single vs queue, posisjon, auto-dismiss?

**Valgt:** Queue-håndtering via Radix ToastProvider. Default position: bottom-right. Default duration: 5000ms.

**Hvorfor:**
- Brukerstipa kan utløse flere toasts samtidig — queue forhindrer overlap-kaos.
- Bottom-right er standard SaaS-konvensjon (Stripe, Linear, etc.).
- Brand kan overstyre position via prop.

---

## 11. Data Table headless via TanStack

**Spørsmål:** Custom table eller library?

**Valgt:** TanStack Table (headless) + våre styling.

**Hvorfor:**
- Sorting, filtering, paginering, kolonne-resize, row-selection er komplekst å bygge fra null.
- TanStack er state-of-the-art i 2026.
- Vi mister INGEN styling-kontroll fordi det er headless.

---

## 12. Kanban Board med @dnd-kit

**Spørsmål:** Drag/drop library?

**Valgt:** @dnd-kit (over react-beautiful-dnd som er deprecated).

**Hvorfor:**
- Mer aktivt vedlikeholdt.
- A11y bedre (keyboard-drag støttet).
- Touch/mouse/keyboard unified.

---

## 13. Activity Stream som custom komponent

**Spørsmål:** Egen komponent eller bare pattern?

**Valgt:** Dedikert komponent fordi den brukes i mange kontekster (issue-detalj, audit-logs, kommentar-tråder).

**Hvorfor:** layout er stabilt nok til å fortjene egen abstraksjon — avatar + actor + action + timestamp + optional content. Custom CSS, ingen library nødvendig.

---

**Konsekvenser samlet:**
- App-rammeverket har nå et komplett komponent-sett som kan bygge en Linear/Stacked-aktig app uten å bygge fra null per prosjekt.
- Library-avhengigheter er minimalt (~30-40kb gzip ekstra når alt brukes).
- Konsumenter kan starte med `<NordoverProvider>` rundt sin app, importere komponenter, og være produktive på dag 1.
- Vedlikehold deles med Radix/TanStack/cmdk/dnd-kit — vi følger versjoner, ikke bygger ny fokus-trap selv.

**Reverseringskostnad:** Middels. Radix-bytte ville krevd komponent-for-komponent migrering, men API er konsistent på tvers av libraries. Bytte av enkelt-library (eks. TanStack → noe annet) er en lokal migrering.
