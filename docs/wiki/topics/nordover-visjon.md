# Nordover — Visjon

**Status:** Kanonisk visjonsdokument
**Etablert:** 2026-06-01

---

## Kjernevisjon

Å etablere en **universell og gjenbrukbar styleguide av global topp kvalitet** som fundament for alle applikasjoner og nettsider. Målet er å **minimere designtid på nye prosjekter**, slik at det eneste som gjenstår per kunde er implementering av **merkevareidentitet (brand styling)**.

Med andre ord: Nordover skal gjøre 90 % av designarbeidet ferdig før et prosjekt starter. Per kunde gjenstår kun brand-laget (farger, logo, font-valg, tone) — ikke struktur, komponenter, tilgjengelighet eller responsivitet.

---

## Bruksområde og plattform

- **Marked:** All-purpose — rammeverket skal fungere like godt for SaaS-dashboards, editorial/marketing-nettsider, e-handel og consumer-apper.
- **Plattform:** Multi-platform — web først, men token-arkitekturen og komponentspråket skal kunne mappes til native (iOS/Android) og desktop.

---

## Visuell filosofi

- **Stilorientering:** Modern / minimal.
- **Fundament:** **Nordisk minimalisme** — ro, luft, funksjonell klarhet, ærlige materialer, ingen dekorativ støy.
- **Inspirasjon:** **Apple Human Interface Guidelines (HIG)** for interaksjonsmønstre, presisjon og polish; **Linear** for tetthet, hastighetsfølelse og moderne SaaS-estetikk.
- **Mål:** Skal tåle sammenligning med verdens mest anerkjente designsystemer (Apple HIG, Material Design 3, Linear, Fluent) på kvalitet, konsistens og tilgjengelighet.

### Hva nordisk minimalisme + Apple HIG betyr konkret

| Prinsipp | Konsekvens i Nordover |
|----------|------------------------|
| Klarhet over dekor | Innhold styrer; chrome trekker seg tilbake |
| Generøs whitespace | Spacing-skala favoriserer luft, særlig web |
| Presis typografi | Optisk balansert hierarki, lining-numerals, tett tracking på store grader |
| Rolige farger | Lav metning som standard; aksent brukes sparsomt og bevisst |
| Taktil respons | Bevegelse er rask, subtil, fysisk troverdig (Apple-aktig easing) |
| Tilgjengelighet er ikke valgfritt | WCAG 2.1 AA som gulv, AAA der mulig |

---

## Referansesystemer (benchmark)

Nordover måles mot disse på tvers av alle skjermstørrelser:

- **Apple HIG** — interaksjon, touch-targets, bevegelse, klarhet
- **Material Design 3** — token-systematikk, elevation, state-layers, responsiv struktur
- **Linear** — tetthet, hastighet, moderne SaaS-polish
- **Fluent** — robusthet på tvers av plattform

---

## Skjermstørrelser (offisielle breakpoints for kvalitetssikring)

| Navn | Bredde | Fokus |
|------|--------|-------|
| Mobile | < 480px | Én kolonne, touch-first, 44px targets |
| Tablet | 768–1024px | Hybrid, 2-kolonne der relevant |
| Desktop | > 1024px | Full layout, hover-tilstander, tetthet |

Alle komponenter og patterns **må** vurderes på alle tre.

---

## Suksesskriterier

1. Et nytt kundeprosjekt kan starte med kun et brand-lag (`clients/<slug>.css`) — ingen strukturell design nødvendig.
2. Komponentdekning og styleguide-dekning er 100 % (styleguides er autoritative).
3. Visuell kvalitet tåler direkte sammenligning med Apple HIG / Linear / Material 3.
4. WCAG 2.1 AA på tvers av alle komponenter og skjermstørrelser.
5. Konsistens: samme problem løses likt overalt (spacing, farge, bevegelse, fokus).

---

## Se også

- [Nordover-oversikt](nordover-oversikt.md)
- [Farger](nordover-colors.md) · [Typografi](nordover-typografi.md) · [Spacing](nordover-spacing.md) · [Bevegelse](nordover-motion.md)
- [Tilgjengelighet](nordover-accessibility.md)
