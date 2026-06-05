# Nordover — eksempel-komposisjoner

> **Ikke-shippbart referanselag.** Disse sidene er *ikke* en del av rammeverket. De
> viser hvordan Nordovers byggesteiner (tokens + komponenter) settes sammen til
> ferdige sider, slik at andre agenter og prosjekter kan **stjele og tilpasse** i
> stedet for å starte fra blankt ark. Rammeverket selv shipper fortsatt bare
> byggesteiner, jf. ADR 2026-06-04 (byggestein-fokus) og 2026-06-05 (eksempel-lag).

## Hva som er her

| Fil | Bruksområde | Pakke |
|---|---|---|
| `marketing-landing.html` | Editorial/marketing-landingsside (hero, features, pricing, CTA) | `tokens-web` + `components-web` |
| `saas-dashboard.html` | SaaS-applikasjonsskall (sidebar, topbar, stat-kort, tabell) | `tokens-app` + `components-app` |

## Regler for eksempler

- **Lenker alltid de shippbare filene** (`../visual/tokens/*`, `../visual/components/*`) — aldri kopiert CSS.
- **Komponerer kun eksisterende klasser.** Trenger et eksempel noe nytt, hører det hjemme i rammeverket (og styleguide), ikke her.
- **Per-prosjekt-pynt** (sidespesifikk layout, copy, bilder) lever inline i eksemplet — det er nettopp det som ikke skal generaliseres.
- Eksemplene er en **startpakke**, ikke en fasit. Tilpass fritt.
