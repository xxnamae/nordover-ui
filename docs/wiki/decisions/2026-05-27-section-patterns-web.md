# Section-patterns for web-rammeverk (fase 2B)

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Fase 2B fokuserer på å fullføre web-rammeverket med komposisjons-patterns for marketing/landingssider. Hver kunde-leveranse må kunne starte fra disse patterns og tilpasses via brand-overstyringer — ikke gjenoppfinnes fra null.

Batchet i én økt fordi hver pattern er en **komposisjon** av primitiver + batch 1/1b-komponenter, ikke en ny komponent-familie med arkitekturvalg.

---

## 1. Hero — tre varianter (ikke flere)

**Spørsmål:** Hvor mange hero-varianter dekker reelle behov?

**Valgt:** Tre — Centered (default), Split (display + media), Editorial (asymmetrisk dramatisk).

**Hvorfor:**
- Centered dekker ~60% av use cases (SaaS landing, om-sider, lansering).
- Split dekker ~25% (produkt-fokus med visuell support).
- Editorial dekker ~15% (kunde-spesifikke premium-prosjekter med signatur-design).
- Hero-video, Hero-stats, Hero-3D etc. ble forkastet — disse er kunde-spesifikke og bør komponeres fra primitivene, ikke bake inn som varianter.
- 3 navngitte varianter er enklere å huske og lærer raskere enn 5-7.

---

## 2. FAQ med native `<details>`/`<summary>`

**Spørsmål:** Native HTML accordion, custom JS-animasjon, eller Radix Accordion?

**Valgt:** Native `<details>`/`<summary>` for batch-versjon. Refactor til Radix hvis vi trenger smooth height-animasjon i alle browsere.

**Hvorfor:**
- Native gir a11y (keyboard, screen reader) gratis.
- Ingen JS-runtime-kost.
- 2026-baseline browsere håndterer native godt — men smooth height-animasjon (auto → fixed) er ikke 100% konsistent.
- For FAQ-bruk (klikk for å åpne, ikke kritisk hvor smooth) er native god nok.
- Hvis vi senere trenger animert accordion for product-info eller settings-paneler, bytter vi til Radix Accordion da.

---

## 3. Site Header med glass-effekt + mobile full-screen overlay

**Spørsmål:** Mobile-meny strategy: dropdown, side-drawer, eller full-screen overlay?

**Valgt:** Full-screen overlay.

**Hvorfor:**
- Marketing-sider har korte nav-lister (5-8 lenker). Drawer er overkill.
- Full-screen gir mer "decisive" UX — bruker velger eksplisitt.
- Enklere implementasjon (ingen animasjons-koordinasjon med viewport).
- Stacked-stil. Linear bruker drawer i app, men ikke i marketing-site-header.

**Glass-effekt på header:** Sticky med `--glass-bg` + `--glass-blur`. Etablert pattern fra iter-3.

---

## 4. Pricing med "Anbefalt"-highlight

**Spørsmål:** Hvordan highlighte anbefalt tier?

**Valgt:** Egen border-farge (`--color-fg`) + subtle bg-skifte + "Anbefalt"-badge over kortet.

**Hvorfor:**
- Industri-konvensjon (Stripe, Vercel, Linear, etc.).
- Subtilt nok for Scandi-min, tydelig nok til å fungere.
- "Anbefalt"-tekst kan overstyres per brand (`--price-card-highlight-label` hvis behov dukker opp).

---

## 5. Footer-grid: 1 brand-column + 3 link-columns

**Spørsmål:** Hvilket grid?

**Valgt:** 1+3 (`grid-template-columns: 2fr 1fr 1fr 1fr` over 40rem). Kollapser til 1-kolonne under.

**Hvorfor:**
- Brand-column får dobbel bredde for å gi rom for tagline + sosiale.
- 3 link-columns dekker typisk struktur (Produkt / Selskap / Juridisk).
- Hvis flere link-kategorier trengs (Resources, Developers, etc.), kan grid-template-columns overstyres lokalt.

---

## 6. Container queries på 48rem som standard tablet/desktop-grense

**Spørsmål:** Hvilken bredde gjør vi layout-skiftet på?

**Valgt:** 48rem (~768px).

**Hvorfor:**
- Dekker iPad portrait som "tablet" og fjerner mobil-layout der.
- 64rem (1024px) er for sent — iPad landscape får da fortsatt mobil-layout.
- Container queries (ikke media queries) — komponenter reagerer på sin foreldre, ikke viewport. Mer gjenbrukbart.

---

## 7. Bevisst utenfor scope

- **Testimonial-section** — egen pattern, sannsynligvis 2-3 varianter (quote-card, video, large-quote).
- **Newsletter-signup-section** — kombinerer Form med section-layout, fortjener egen.
- **Hero med video** — performance-strategi (poster, autoplay-policy, fallback).
- **Animated transitions** (scroll-trigger, parallax) — krever JS-library-valg.
- **Mega-menu** — for komplekse marketing-sites med mange produktlinjer.

Disse kommer i fase 2B-utvidelser hvis konkrete behov dukker opp.

---

**Konsekvenser samlet:**
- Web-rammeverket har nå 9 section-patterns som dekker en komplett landingsside fra header til footer.
- Enhver ny Nordover-leveranse kan starte med: `<SiteHeader/><HeroCentered/><LogoCloud/><FeatureGrid/><StatsStrip/><CTASection/><Pricing/><FAQ/><SiteFooter/>` — og iterere derfra.
- Brand-overstyringer kan tilpasse alt via `clients/<slug>.css` uten å touche patterns.
- Container queries i hero-split og footer betyr patterns er truly responsive uten viewport-spesifikke breakpoints.

**Reverseringskostnad:** Lav-middels per pattern. Hvis hero-Split-varianten viser seg upraktisk kan vi fjerne den uten å bryte de andre.
