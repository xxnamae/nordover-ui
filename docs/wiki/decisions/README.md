# Decisions — format-mal

Hver beslutning får sin egen fil i denne mappen. Filnavn: `YYYY-MM-DD-kort-tittel.md`.

## Mal

```markdown
# [Tittel]

**Dato:** YYYY-MM-DD
**Status:** Aktiv | Delvis superseded | Reversert | Vurdert
**Forgjenger:** [link til forrige beslutning hvis denne bygger på/reverserer en eldre]
**Etterfølger:** [legges til når en ny beslutning superseder denne]

**Kontekst:** [Hvorfor diskuterte vi dette?]
**Alternativer:**
- A) ...
- B) ...
**Valgt:** [Hvilket alternativ + hvorfor]
**Konsekvenser:** [Hva følger av dette valget?]
**Reverseringskostnad:** [Lav / Middels / Høy]
```

## Status-verdier

| Status | Betydning |
|---|---|
| **Aktiv** | Beslutningen gjelder. Default for nye filer. |
| **Delvis superseded** | Noen punkter er reversert av en senere beslutning. `Etterfølger:`-feltet peker dit. |
| **Reversert** | Hele beslutningen er reversert. `Etterfølger:` viser hva som gjelder nå. |
| **Vurdert** | Diskutert, ikke implementert. |

## Regler

- **Decisions er hellige som dokumentasjon, ikke som låste vedtak.** Vi kan snu — men da må vi reversere eksplisitt.
- Hvis en beslutning reverseres helt eller delvis: lag NY decision-fil som forklarer hvorfor, og oppdater `Status:` + `Etterfølger:` på den gamle.
- Aldri rediger eldre beslutninger sitt **innhold** (bevarer historikken). Kun `Status:` og `Etterfølger:` kan oppdateres i etterkant.

## Eksempel på supersede-kjede

Se kjeden:
1. [2026-05-27 v2 Hardening](2026-05-27-v2-hardening.md) → Status: Delvis superseded (kun §2a om `[data-theme="dark"]`)
2. [2026-05-27 v3 Rebuilding](2026-05-27-v3-rebuilding.md) → reverserer v2 §2a, gjør én dark-mekanisme via `:has(#dark:checked)`
3. [2026-05-29 v3 Polish](2026-05-29-v3-polish-og-shippable.md) → kompletterer v3 (localStorage, triplets, ekstrahert CSS)

Hver fil sier eksplisitt **hva** den endrer fra forgjengeren. Gammel fil beholder sitt opprinnelige innhold, men får en "Status:"-merknad på toppen som peker fremover.
