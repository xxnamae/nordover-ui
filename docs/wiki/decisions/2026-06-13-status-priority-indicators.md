# ADR: Status & Priority Indicator System for App

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/visual/components/components-app.css` (lines 1307-1325), `docs/visual/styleguide.html` (status-priority section)

## Kontekst

App-pakken er en SaaS-type system hvor brukere arbeider med oppgaver (issues, tasks, projects). Hver oppgave har minst to ortogonale attributter:
- **Status** (hva er tilstanden?) — todo, backlog, in-progress, done, cancelled
- **Priority** (hvor viktig er det?) — urgent, high, medium, low

Linear og liknende SaaS-løsninger bruker visuell signalering via små fargede indikatorer for å gjøre disse attributtene *scannable* i lange lister. Nordover hadde ingen primitive for disse — bare generiske badges (success/error/warning/info) som brukes for semantisk feedback, ikke for task-spesifikke stater.

## Beslutning

Introduser tre ortogonale indicator-systemer:

1. **Status dots (`.status-dot`)** — 8px fargede sirkler som viser oppgavens progresjon
   - `.is-todo`: `--color-border` (lysegrå, ustartet)
   - `.is-backlog`: `--color-muted` (mørkegrå, planlagt)
   - `.is-in-progress`: `--color-info` (blå, pågår)
   - `.is-done`: `--color-success` (grønn, fullført)
   - `.is-cancelled`: `--color-muted` (mørkegrå, 50% opacity, forlatt)

2. **Priority indicators (`.priority-indicator`)** — fargekodede badges med tekst
   - `.is-urgent`: error-fargen med fargeskala (rød)
   - `.is-high`: warning-fargen (oransje)
   - `.is-medium`: nøytral bakgrunn med standard tekst
   - `.is-low`: muted-fargen (grå)

3. **Status badges (`.status-badge`)** — semantisk fargekoding for generiske tilstander
   - Gjenbruker success/error/warning/info fra existerende badge-system
   - Separert fra task-status fordi semantikk er orthogonal til oppgaveprogresjon

Alle tre går gjennom `color-mix()` for bakgrunn (15% opacity) for å sikre WCAG AA kontrast mot `--color-surface` bakgrunn.

## Rationale

- **Scanability**: Farger alene er raskere å skanne enn tekst i lange lister
- **Composability**: Indicators er små og enkle — de komponerer inn i rows, cards, dialogs uten å dominere
- **Accessibility**: Alle uses kombinerer farge + tekst; ingen stol på bare farge. Focus-states er synlige.
- **Semantic clarity**: Status (what's the progression?) og Priority (how urgent?) er ikke synonyme — system gjør det eksplisitt
- **Linear coherence**: Fargevalg og størrelse speiler Linear's pattern — kjent for brukere som migrerer fra Linear

## Konsekvenser

- **Styleguide**: Ny "Status & Priority Indicators" seksjon dokumenterer alle stater, best practice for kombinering (status dot + priority badge i samme row)
- **Composition**: Task list rows (Bolk 3) vil kombinere `.status-dot` + oppgavenavn + `.priority-indicator` + metadata
- **Token naming**: Ikke nye tokens; rebruk av eksisterende `--color-*` familie
- **Issue Page**: (Bolk 5) vil demonstrere full workflow: task med status → priority → assignment → due date
- **Future**: Dersom filtermeny (Bolk 2) vil vise status-optioner, dette systemer gjør det lett — bare liste alle `.status-dot.is-*` klassekombinasjoner

## Alternativ forkastet

- **Bruk kun badge-farger for status**: Ville forvekslet oppgavestatus (todo vs. done) med semantisk feedback (success vs. error). Misvisende.
- **Bruk SVG-ikoner for hver status**: Ville vært tungere og mindre scannable. Prikker er raskere å prosessere.
- **Hardkod farger i HTML**: Bryt token-system. Ingen måte å endre paletter per kunde.
