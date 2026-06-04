# ADR: Rammeverk-fokus — byggesteiner, ikke ferdige sider

**Dato:** 2026-06-04 | **Status:** ACCEPTED | **Erstatter visjonspunkt i:** CLAUDE.md, `2026-05-30-comprehensive-component-library.md`

## Spørsmålet

Skal Nordover levere ferdige komposisjoner (hero, pricing, blog, testimonials, dashboards) som offentlige kontrakter — eller skal rammeverket være et **fundament av byggesteiner** som hvert prosjekt bygger sine egne sider på?

## Beslutning

**Fokusér på byggesteiner.** Nordover er fra nå tre lag, der bare de to første er offentlige kontrakter:

| Lag | Innhold | Kontrakt? |
|---|---|---|
| **1. Tokens** | farger, type, space, motion, shadow, radius | ✅ Ja |
| **2. Byggesteiner** | button, form-elementer, card-skall, badge, alert, table-base, layout-primitiver, nav-elementer, modal, accordion, tabs, avatar, tooltip, menu, toast, kbd, skeleton, breadcrumb, pagination, search-bar, date-picker, stepper, file-upload, tag-input | ✅ Ja |
| **3. Patterns / komposisjoner** | hero, pricing-grid, blog-card, testimonial, timeline, cta-card, feature-grid/-card, dashboard-oppsett | ❌ Fjernet |

## Hvorfor

- **Gjenbruk faller med opinionering.** En knapp er universell; en "pricing card" er en design- og innholdsbeslutning per prosjekt. Lag 3 passer sjelden uendret, eldes raskest, og hvert prosjekt bygger dem om likevel.
- **Ærlig scope.** 60+ komponenter vokste i faser (1A→1M) uten samlende prinsipp. Lag 3 var overrekkevidden — ikke størrelsen i seg selv.
- **Fundament, ikke sider.** Samme filosofi som Radix Primitives + Tailwind: gi struktur, a11y og tokens — la produktet eie komposisjonen.
- **Forenkler web/app.** Det meste av web/app-divergensen lå i patterns og tetthet. På byggestein-nivå er forskjellene små; dette åpner for å forenkle to-pakke-modellen senere (egen ADR ved behov).

## Hva fjernes (konkret)

Følgende klasser slettes fra `components-web.css` og `components-app.css`:

`.hero-centered`, `.hero-split-content`, `.hero-split-image`, `.pricing-section`, `.pricing-grid`, `.pricing-header`, `.pricing-toggle*`, `.pricing-annual`, `.blog-card*`, `.testimonial*`, `.timeline*`, `.cta-card`, `.feature-grid`, `.feature-card*`, `.featured`

Patterns slettes **helt** (gjenopprettbart fra git-historikk om nødvendig). De er ikke arkivert som recipes.

## Konsekvenser

- **Styleguides bygges på nytt fra scratch** med rent fokus: token-gallerier + byggestein-katalog. Dette fjerner samtidig ~11k linjer inline-style-gjeld.
- **README og COMPONENT-INVENTORY** oppdateres til å reflektere fundament-scopet.
- **Eldre pattern-ADR-er** (`section-patterns-web`, `patterns-*`) forblir uendret som historikk (publiserte ADR-er er immutable) — denne ADR-en er reverseringen.

## Tradeoffs

| Vi får | Vi gir opp |
|---|---|
| ✅ Skarpt, gjenbrukbart fundament | ⚠️ Ingen ferdige markedsførings-sider out-of-the-box |
| ✅ Mindre vedlikehold, klarere kontrakter | ⚠️ Prosjekter må komponere egne patterns |
| ✅ Lever lenger uten å eldes | ⚠️ Engangskostnad: rydding + styleguide-rebuild |

## Revurder hvis

- Flere prosjekter viser seg å trenge *identiske* komposisjoner (da: eget valgfritt "recipes"-bibliotek, ikke kjerne-kontrakter)
