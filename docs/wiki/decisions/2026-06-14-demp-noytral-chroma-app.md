# ADR: Demp nøytral-chroma i app-pakken (0.012 → 0.004)

- **Dato:** 2026-06-14
- **Status:** Vedtatt
- **Relatert:** `docs/visual/tokens/tokens-app.css`, `docs/visual/tokens/tokens-app.json`
- **Endrer:** `2026-06-13-linear-tonet-app-palett.md` (justerer chroma-verdien derfra; den ADR-en står ellers ved lag)

## Kontekst

ADR-en «Linear-tonet nøytralpalett» satte `--neutral-c: 0.012` (hue 265) for å gi app-pakken
Linears kjølige, lett lilla-tonede gråskala. I praktisk live-review viste det seg at 0.012
**bløder synlig lilla/blått inn i lyse subtile flater** — alert-bakgrunner, table-zebra,
badge-bakgrunner og callout-bokser fikk en tydelig lavendel/blå tone som leste som en
*farge*, ikke som nøytral grå. Det trekker ned «ren visuell kvalitet» og avviker fra Linear,
som i lys modus leser som nær-nøytral grå.

Web-pakken bruker allerede `--neutral-c: 0.004` og hadde ikke problemet.

## Beslutning

**Senk `--neutral-c` i app fra 0.012 → 0.004.**

- Hele app-gråskalaen (`--gray-50…950`) og alle avledede flater (`--color-subtle`, surfaces,
  table-zebra via `--color-fg`-mix) blir **nær-nøytral grå** med kun et hårfint kjølig stikk.
- Hue beholdes (265), så den minimale kjølige tonen fra Linear-referansen er intakt — bare
  dempet til den ikke lenger leser som farge.
- **L-aksen er uendret**, så all WCAG AA-kontrast på nøytraler er bevart (verifisert:
  `check:contrast` grønn).
- Accent (`--color-accent`, oklch 0.54 0.16 272) er et separat token og berøres ikke.

## Konsekvenser

- Én token-endring nøytraliserte alle blå-tinten i app-flatene (verifisert visuelt på
  table, alerts, badges, callouts).
- App-only verdi (web var allerede nøytral nok) — JSON regenerert (`npm run build:tokens`).
- Reverserbart: én verdi.
