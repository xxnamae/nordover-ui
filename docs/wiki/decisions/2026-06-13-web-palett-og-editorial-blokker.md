# ADR: Web-palett beholdes (editorial sort-på-hvit) + web-only editorial-blokker

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/visual/tokens/tokens-web.css`, `docs/visual/components/components-web.css`, `docs/visual/styleguide.html`
- **Bygger på:** `2026-06-13-linear-tonet-app-palett.md` (app-sporet), `2026-06-12-styleguide-chrome-constant.md`

## Kontekst

Web-sporet (Bolk 4) skal løftes til Off Menu-kvalitet — lys editorial. Off Menus
visuelle DNA er **lys/hvit bakgrunn, tung Inter Tight display-type, enorm
whitespace, nummererte prinsipp-rader, og en minimal «engineering-drawing»-estetikk
med stiplede rammer og crosshair-merker**.

Spørsmålet var todelt:
1. **Skal web-paletten endres** for å treffe Off Menu?
2. **Hvilke nye byggesteiner** trengs for det editoriale uttrykket?

Web-pakken hadde allerede: `--color-bg: oklch(1 0 0)` (ren hvit), `--color-accent:
var(--gray-900)` (sort), nær-nøytral gråskala (`--neutral-h: 250`, `--neutral-c:
0.004`), Inter Tight display-font, og en clamp-fluid type-skala (`--text-4xl` …
`--text-7xl`). Pakken har også **full dark mode** parametrisk fra samme nøytral.

## Beslutning

### 1. Paletten beholdes uendret (variant «ren hvit»)

Tre varianter ble rendret side om side i **både lys og dark** (ren hvit · varm papir ·
kjølig stein) og evaluert mot Off Menu og visjonens nordiske minimalisme. **Ren hvit
ble valgt:**

- Den matcher allerede Off Menus stark-hvite editorial-uttrykk («lys/hvit»).
- Den er sannest mot nordisk minimalisme — ingen tonet «sepia»- eller fargestikk.
- **Surgical changes**-prinsippet: ingen grunn til å endre en kontrakt-token
  (`--color-bg`) som allerede gjør jobben. En palett-endring ville krevd ADR for
  brytende verdiendring, ny WCAG-verifisering i begge moduser, og Elementor-regen —
  uten estetisk gevinst.

Konsekvens: **ingen token-endring i Bolk 4.** App og web forblir bevisst divergerende
(mørk kjølig Linear-SaaS vs. lys stark editorial), slik app-ADR-en etablerte.

### 2. Web-only editorial-byggesteiner

Følgende legges til **kun i `components-web.css`** (web-editorial-identitet):

- **`.btn-pill`** — fullt avrundet CTA (modifier på delt `.btn`). Marketing-motstykket
  til app-pakkens tettere rektangulære knapper.
- **`.numbered-list` / `.numbered-item` / `.numbered-num` / `.numbered-title` /
  `.numbered-text`** — stor display-numeral + tittel + tekst, hårlinje-delt. For
  prinsipp-lister, prosess-steg, nummerert FAQ.
- **`.frame-dashed`** — stiplet editorial bounding-box.
- **`.crosshair` / `.crosshair-lg`** — minimalistisk «+»-registreringsmerke (dekorativ
  utility, tegnet med gradient-kryss).
- **`.frame-crosshair`** — hårlinje-boks med «+» sentrert på hvert hjørne. Ett
  `::after` maler fire hjørne-pluss via en `mask`-et bakgrunn som arver `currentColor`
  → adapterer automatisk til lys/dark.

**Mirroring-vurdering:** Speilingsregelen gjelder delt *struktur*, ikke pakke-spesifikk
*identitet*. Pille-knapper, nummererte editorial-rader og crosshair-estetikk er web-only
visuell identitet — app (tett Linear-SaaS) bruker dem ikke. De speiles derfor **ikke**
til app. Delte byggesteiner som ble berørt (meny-utvidelser, label-dots) ble speilet til
web i samme bolk (se Model A nedenfor).

### 3. Styleguide-modell A — pakke-scoped seksjoner

App og web er to divergerende design-systemer på ett token-fundament. Styleguiden tagger
nå doc-seksjoner og nav-lenker med `data-pkg="app|web"`; pakkebytteren skjuler
ikke-matchende seksjoner. Utagget = delt (synlig i begge). Dette løser gjelden der
app-only Bolk 1–3-komponenter ellers ble ustylet ved bytte til web.

## Konsekvenser

- Ingen verdiendring på web-tokens → ingen brytende kontrakt, ingen JSON/Elementor-regen.
- Web-editorial-blokkene vises kun i web-modus i styleguiden (egen «Editorial (Web)»-gruppe).
- Crosshair-frame bruker `mask` (bred støtte i moderne nettlesere; rent dekorativt, så
  graceful degradation til en hårlinje-boks uten hjørnemerker er akseptabelt).
- Bolk 5 vil komponere disse til en dokumentert marketing-oppskrift (bevis på
  komposabilitet), ikke en shippet sidekomposisjon.
