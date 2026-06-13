# ADR: Editorial-prosa med Off Menu-emphasis (web-pakken)

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `docs/visual/components/components-web.css`, `docs/visual/styleguide.html`

## Kontekst

I QA mot Off Menu pekte deres mest gjenkjennelige typografiske signatur seg ut: store
narrative avsnitt der **brødteksten ligger i en rolig mid-tone**, **nøkkelfraser løftes til
full ink** (svart/tyngre), og **avsluttende tanker tones ned** til en lys grå. En liten
mono «Fig 0.2»-plate-caption følger med. Dette gir tekst et redaksjonelt, kuratert preg —
leseren ledes gjennom et hierarki *inni* avsnittet, ikke bare mellom overskrift og brødtekst.

Web-pakken (editorial/marketing) hadde ingen primitiv for dette. `.numbered-text` er flat
muted, og `.t-body*` er nøytral brødtekst.

## Beslutning

**Ny editorial-typografi-primitiv i web-pakken:** `.t-editorial` med tre emphasis-nivåer.

- `.t-editorial` — container i mid-tone: `color-mix(in oklch, var(--color-fg) 56%, var(--color-bg))`,
  stor responsiv `font-size` (clamp 1.25–1.75rem), `line-height: 1.5`, `max-width: 34rem`.
- `.t-editorial strong`, `.t-editorial .t-key` — løft til full ink (`--color-fg`) + `--fw-medium`.
  `<strong>` brukes som default-mekanisme, så nøkkelfrasen er *semantisk* fremhevet (a11y).
- `.t-editorial .t-faded` — nedtoning til `color-mix(… 30% …)` for avsluttende, ikke-essensiell tekst.
- `.t-figure` — liten mono plate-caption (`--font-mono`, `--text-xs`, sperret).

**Alle toner er `color-mix` mot `--color-bg`**, så de adapterer automatisk til lys/mørk uten
egne mode-regler (verifisert i begge moduser).

## Konsekvenser

- Web-pakken får Off Menus redaksjonelle uttrykk som en gjenbrukbar primitiv.
- **App-pakken berøres ikke** — dette er web-spesifikk editorial-identitet (jf. `numbered-*`,
  `frame-crosshair` som også er `data-pkg="web"`). Ingen app-speiling, ingen token-JSON.
- `.t-faded` er bevisst lav-kontrast og kun for *ikke-essensiell* tekst (dekorativ nedtoning);
  alt meningsbærende ligger i mid-tone eller ink, som holder lesbar kontrast på editorial-størrelse.
- Dokumentert i styleguiden som egen web-seksjon (`#editorial-prose`) med nav-lenke.
