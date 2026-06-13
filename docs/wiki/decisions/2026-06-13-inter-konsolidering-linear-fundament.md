# ADR: Font-konsolidering til Inter Variable + Linear-fundament (Bolk A)

- **Dato:** 2026-06-13
- **Status:** Vedtatt
- **Relatert:** `tokens-app.css`, `tokens-web.css`, `components-app.css`, `styleguide-chrome.css`
- **Erstatter delvis:** `2026-05-27-inter-variable-font.md` (dobbel-font-perioden)

## Kontekst

Eieren delte de faktiske designreferansene (Linear app + design­system, Off Menu, Stacked)
og fastsatte at **APP-pakken skal være nærmest identisk med Linear**. Tre funn fra
referansene drev denne bolken:

1. **Én koherent grotesk.** Både Linear og Off Menu bruker *én* familie på alle grader,
   differensiert med vekt + tracking + optisk størrelse — ikke en egen condensed display-font.
   Vår dobbel-font (Inter Variable brød + Inter Tight display) skapte subtil disharmoni på
   heading/body-grensen.
2. **Lilla-tonet grå i hele rampen** — også i light mode. Vår `tokens-app.css` designet dette
   (`--neutral-h: 265`), men `components-app.css` overstyrte light mode til **ren grå
   (chroma 0)** og drepte signaturen.
3. **Medium vekt, ikke lett.** Linears display er ~510–540, ikke 420.

## Beslutning

### 1. Inter Variable overalt (begge pakker)
`--font-display` peker nå på samme stack som `--font-sans` (Inter Variable). Inter Tight
fjernet fra token-stacks, fra `@font-face`-fallback (web), fra chrome-`font-family`, og fra
`<link>`-lasting i styleguide + eksempler (fjerner én Google Fonts-forespørsel → raskere, mindre CLS).
Lagt til `font-optical-sizing: auto` i begge reset-blokker (Inter Variable har `opsz`-akse —
gir automatisk display-raffinering uten egen font).

### 2. Rekalibrert tracking + vekt for Inter
- App `--tracking-display`: −0.04 → **−0.022** (Inter tåler ikke Inter Tights stramhet).
- Web `--tracking-display`: −0.05 → **−0.025**.
- App display-vekter: 420/440/460 → **510/520/530** (Linear-skarphet).
- Web display-vekter: 380/400/420 → **440/470/500** (Off Menu editorial).
- `.t-display-*` inline letter-spacing → token-drevet (`var(--tracking-display)`).

### 3. Drept ren-grå-overstyringen i light mode
Slettet `:root:has(#dark:not(:checked))`-blokken i `components-app.css` som flatet ut til
`oklch(... 0 0)`. Light mode arver nå den parametriske lilla-grå direkte fra `:root`.

### 4. Monoton, tonet surface-rampe (app light)
`--surface-1..5` gikk tidligere opp-og-ned (`.98 .99 1.0 .99 .98`, chroma 0). Nå monoton mot
hvitt med nøytral-tone i bunn: `0.985(tinted) → 0.992(tinted) → white → white → white`.

## Konsekvenser

- **Kontrakt:** `--font-display` *navnet* består (kontrakt intakt); kun *verdien* endret. Ingen
  klasse-navn brutt. JSON regenerert i samme commit (`tokens-app/web.json`).
- **Mirroring:** Font-token-endringer speilet i begge pakker samme commit (regel oppfylt).
- **Visuelt:** App light + dark beholder nå Linears kjølige lilla-hue; display leser skarpt.
- **Neste bolker (mot near-identical Linear):** flate solide violette primærknapper (erstatte
  tactile gradient som default), dekor-/label-palett (teal/korall/oliven/gul/oransje/lavendel/
  blå/skifer/grønn), vekt-/easing-trim, og per-skjerm-finpuss (command bar, sidebar, issue-rad,
  issue-side) målt mot Linear-skissene.
