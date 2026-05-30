# Patterns-utvidelser

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter at både web-rammeverket (fase 2B) og app-rammeverket (fase 2A) var komplett, identifiserte vi seks utvidelser som dekker konkrete hull. Disse er ikke kritiske for første-leveranser men nødvendige for å gjøre rammeverket reelt komplett før implementering.

**Patterns:** Testimonial (3 varianter), Newsletter Signup, Hero med video, Mega-menu, Chart-wrappers, Empty State med illustrasjoner.

---

## 1. Testimonial — 3 varianter

**Valgt:** Card, Large Quote, Video.

**Hvorfor 3:**
- Card dekker standard SaaS-bruk (grid av customer-quotes).
- Large Quote er editorial — bra for premium landing pages.
- Video er nødvendig for moderne marketing (konvertering er høyere med video-testimonials).
- 3 dekker behov uten å eksplodere variant-overflate.

---

## 2. Newsletter Signup som section-pattern (ikke separat komponent)

**Valgt:** Composed section som bruker eksisterende Form + Button.

**Hvorfor:** ingen ny komponent nødvendig — det er en composition + styling av eksisterende primitiver. Dokumenteres som pattern, ikke som component-spec.

---

## 3. Hero med video — performance-aware default

**Valgt:** Default-implementasjon med IntersectionObserver-trigger, poster-fallback, `preload="metadata"`, autoplay-muted-playsInline.

**Hvorfor:**
- Naive `<video autoplay>` koster bandwidth + battery for brukere som scroller forbi.
- Mobile-browsers nekter autoplay uten muted + playsInline.
- Poster gir umiddelbar visuell oppfattelse mens video laster.
- Reduced-motion override skjuler videoen helt og viser kun poster.

---

## 4. Mega-menu via Radix NavigationMenu

**Valgt:** `@radix-ui/react-navigation-menu` som underliggende.

**Hvorfor:**
- A11y for komplekse nav-menus er ikke-trivielt (escape, arrow-keys, focus-management).
- Radix har dette innebygget.
- Mobile-fallback: kollapser til full-bredde i samme menu-overlay (bruker mobile-toggle fra Site Header).

---

## 5. Chart-wrappers via Recharts

**Spørsmål:** Recharts, Visx, Nivo, Chart.js eller noe annet?

**Valgt:** Recharts.

**Hvorfor:**
- Declarative React API — matches våre patterns.
- D3-basert under panseret — battle-tested matte.
- Mindre bundle enn Nivo, mer dekkende enn Visx (out-of-the-box).
- Recharts er state-of-the-art for SaaS-dashboards i 2026.

**Wrappers:**
- LineChartCard, BarChartCard, AreaChartCard, StackedBarChartCard, PieChartCard, DonutChartCard
- Felles props: `data`, `series` (med color via `--chart-N`-tokens), `title?`, `height?`
- Custom Tooltip-styling matcher våre tokens (bg, border, shadow-popover).

**Bundle-strategi:** opt-in via dynamic import per chart-type. Sider uten charts laster ikke Recharts.

---

## 6. Empty State med innebygde illustrasjoner

**Valgt:** Ship 6-8 SVG-illustrasjoner som del av rammeverket. Line-art, stroke-only, `currentColor`.

**Hvorfor:**
- Empty state illustrasjoner er signaturdetalj i moderne SaaS.
- Hver kunde-leveranse ville ellers brukt time på å sortere ut illustrasjoner.
- Token-aware (currentColor) gjør at de adapter dark/light + brand-overstyringer.
- Scandi-min editorial-stil (linje-art, ikke filled) passer husstilen.

**Illustrasjons-sett:**
1. empty-inbox
2. empty-search
3. empty-folder
4. empty-data
5. empty-list
6. empty-error
7. empty-success
8. empty-users

**API:** `<EmptyState illustration="empty-inbox" />` (string-name) eller `<EmptyState illustration={<CustomSvg/>} />` (custom node).

---

**Konsekvenser samlet:**
- Rammeverket har nå dekning for nesten alle behov i moderne SaaS + marketing-sider.
- Total ekstra bundle ved full bruk: ~60kb gzip (Recharts ~40, nav-menu ~20).
- SVG-illustrasjoner er små (~1-2kb hver, kan inline'es).
- Kunde-leveranser kan starte fra et komplett bibliotek — ingen "fyll inn etterpå".

**Reverseringskostnad:** Lav. Hvert pattern er additive. Library-bytte (eks. Recharts → Visx) er en lokal komponent-migrering.

## Hva som fortsatt ikke er drodlet (parker for senere)

- Multi-step Wizard
- Inline edit pattern
- Filter Bar (kompositt Tag + Dropdown)
- Notification Feed (forskjellig fra Activity Stream)
- 3D/parallax-effekter
- Skjelett-illustrasjoner utover de 6-8 vi ship'er
