# ADR: Linear-tonet statusikonografi for `.status-dot` (app-pakken)

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/visual/components/components-app.css`, `docs/visual/styleguide.html`

## Kontekst

App-pakken skal tåle direkte sammenligning med Linear. I en visuell QA mot Linear,
Stacked og Off Menu var det tydeligste enkeltstående finish-gapet **statusindikatoren**:
Nordover brukte en **solid farget prikk** (`.status-dot.is-*` med `background: <farge>`),
mens Linears mest gjenkjennelige signatur er en **ikonografisk progress-glyf** — en ring
som visuelt forteller *hvor i løpet* en oppgave er:

- Backlog — stiplet ring
- Todo — tom, tynn ring
- In Progress — ring med pie-fyll
- Done — fylt sirkel med hake
- Cancelled — fylt sirkel med ×

En solid prikk bærer mindre informasjon enn ringen: den skiller statusene kun på farge,
mens Linears form gir et ekstra, fargeuavhengig lag (viktig også for fargesvakhet).

`.status-dot` er en **ren app-komponent** (web-pakken har den ikke; seksjonen er
`data-pkg="app"`), brukt 19 steder i styleguiden — i `.list-row`, `.command-bar`,
token-pills og status-demoen.

## Beslutning

**`.status-dot` rendres som Linear-tonede progress-glyfer i ren CSS, med uendret
klassekontrakt.**

- Klassenavnene `.status-dot.is-{todo,backlog,in-progress,done,cancelled}` beholdes 1:1,
  så **alle 19 bruksstedene oppgraderes automatisk** uten HTML-endring. Dette er en
  *rendrings*-endring, ikke en API-endring — token- og klassekontrakter er intakte.
- Glyfene er ren CSS: `border` (ring), `conic-gradient` på `::before` (pie-fyll), og
  `mask-image` med inline-SVG for hake/×. Ingen nye tokens, ingen nye ikon-assets.
- **Done/cancelled-glyfen er en knockout i `--color-bg`**, så haken/× adapterer automatisk
  til lys/mørk modus (mørk glyf på lys bakgrunn og omvendt) uten egne mode-regler.
- Standardstørrelsen økes fra `0.625rem` → `0.875rem` (10 → 14px) for at ringformen skal
  være lesbar på Linears nivå. Inline-overstyrte størrelser (token-pills) beholder sine.
- Glyfen er **dekorativ** og alltid paret med en tekst-label (jf. styleguidens
  «Avoid: color alone»), så den utløser ingen WCAG-tekstkrav.

## Konsekvenser

- App-statuser leser nå som Linear: form + farge, ikke bare farge.
- Visuelt verifisert i lys og mørk modus, og i kontekst (`.list-row`, `.command-bar`).
- **Web-pakken berøres ikke.** Ingen token-JSON-regenerering (endringen er strukturell
  komponent-CSS, ikke token-verdier).
- Reverserbart: én CSS-blokk; ingen nedstrøms klasse-/token-brudd.
