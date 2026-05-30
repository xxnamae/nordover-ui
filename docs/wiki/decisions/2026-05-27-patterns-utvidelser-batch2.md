# Patterns-utvidelser batch 2 (Linear/Stacked/Off Menu-inspirert)

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Etter at user delte 7 PDF-referanser fra Linear (marketing + app), Stacked (marketing) og Off Menu (light editorial), identifiserte vi 7 nye patterns + utvidelser som mangler i rammeverket. Spec'et i én batch.

---

## 1. Site Header — 3 nye varianter (totalt 4)

**Spørsmål:** Hvor mange site header-varianter, og hvilke?

**Valgt:** 4 — Glass (eksisterende), Stacked, Linear, Off Menu.

**Hvorfor:**
- Hver dekker en distinkt marketing-tone:
  - **Glass:** moderne SaaS med transparency (default).
  - **Stacked:** klassisk SaaS landing med pill-CTA-par.
  - **Linear:** produkt-fokusert med "Open app" som primær handling.
  - **Off Menu:** editorial brand (design-studio, agency) med kompakt dots-trigger.
- Flere enn 4 ville overlappe. Færre ville ikke dekke editorial-stil.

---

## 2. Footer — 2 nye varianter (totalt 3)

**Valgt:** Default (eksisterende), Linear-stil (5 columns + bottom), Minimal (1 rad).

**Hvorfor:**
- Default dekker SaaS-marketing (mellom-størrelse).
- Linear-stil for komplekse prosjekter med mange resource-/feature-lenker.
- Minimal for landingssider og app-shells der full footer er for tungt.

---

## 3. AI Assistant Panel

**Valgt:** Ny pattern — floating chat-overlay med agent-avatar, intro-melding, klikkbare suggestion-pills, og input.

**Hvorfor:**
- Off Menu sin "Remi" og Linear sin "Ask Linear" er begge eksempler på et moderne SaaS-mønster som er økende vanlig (Intercom, Drift, ChatGPT-baserte assistents).
- Brukes både for support og som onboarding-guide.
- Skal kunne posisjoneres bottom-left eller bottom-right.
- Variants: `portrait` (med agent-bilde, Off Menu-stil) og `compact` (kun tekst).

**Arkitektur:**
- Bygger på Radix Dialog for focus-trap + scroll-lock.
- Suggestions er klikkbare pills som fyller ut input + sender.
- Input-input + send-knapp + valgfri tab-bar (Chat / Contact).

---

## 4. Onboarding Flow (Wizard-variant)

**Spørsmål:** Skal onboarding være en variant av eksisterende Wizard, eller en ny komponent?

**Valgt:** Variant av Wizard (`<OnboardingFlow>`) — relevant for applikasjoner.

**Hvorfor:**
- Wizard og OnboardingFlow deler core-pattern (kontrollert state, navigation, validering).
- Onboarding er distinkt nok i layout (full-screen, dot-paginasjon, dekorativ media-pane) til å fortjene egen wrapper.
- Linear sitt onboarding-mønster (split-screen + dots + Skip) er industri-standard for SaaS-første-gangs-bruk.

**Forskjeller fra Wizard:**

| | Wizard | OnboardingFlow |
|---|---|---|
| Layout | Inline | Full-screen overlay |
| Progress | Numerated circles | Dot-pagination (active = 1.5rem wide) |
| Validation | Strict (next disabled hvis feil) | Soft (Skip alltid tilgjengelig) |
| Media | Ingen | Visuell pane høyre side |
| Bruksområde | Settings, forms | Førstegangs-onboarding |

---

## 5. Numerated Service List

**Valgt:** Ny editorial pattern — full-width rader med title venstre + nummer høyre, hover ekspanderer padding.

**Hvorfor:**
- Off Menu sitt service-list-pattern (01-06: Brand Design / Web & Experiential / etc.) er signaturdetalj for design-studio og agency-sider.
- Brukes også som "feature index" i editorial-sammenheng.
- Hover-effekt med padding-økning gir interaktiv kvalitet uten visuell støy.

**Bruksområder utenfor service-list:**
- Capability-index ("Hva vi gjør")
- Process-overview (steg 01-04)
- Editorial table-of-contents

---

## 6. Sticky Sub-nav

**Valgt:** Ny pattern — venstre-sidet sticky-nav som scroller med innhold.

**Hvorfor:**
- Stacked sin features-side bruker dette for å navigere mellom Subscriptions / Paid content / Analytics / Integrations / AI tools / Agency.
- Pattern for lange feature-sider eller doc-sider.
- Auto-active basert på scroll-position via Intersection Observer.

**Mobile:** kollapser til horisontal scrollable-bar over innholdet.

---

## 7. Feature Row

**Valgt:** Ny pattern — tekst-venstre + UI-preview-høyre composition.

**Hvorfor:**
- Stacked har dette på hver feature-page-seksjon: store overskrift + paragraph + "Get started →" + embedded dashboard-screenshot.
- Linear har varianter også (split-screen-hero med høyre-side product preview).
- Veksle reverse/non-reverse for visuell rytme i lange sider.
- Mobile: stables alltid med tekst over preview.

---

## SVG-ikon-system (utvidelse)

**Valgt:** Bytte ut alle emoji-ikoner og system-tegn (☆ ◯ ⌂ 📥) med outline SVG-ikoner som matcher empty-state-illustrasjonene.

**Stil:**
- 1.5px stroke-width
- `stroke="currentColor"`, `fill="none"`
- 24x24 viewBox
- `stroke-linecap="round"`, `stroke-linejoin="round"`

**Implementasjon i styleguide:** lagt til `.icon` / `.icon-sm` / `.icon-lg` utility-klasser. Brukes per komponent.

**Ikoner ferdig produsert (i styleguide-iter 5):**
- Sidebar nav: Home / Inbox / Team / Folder / Analytics
- Menu items: Edit / Copy / Share / Trash
- Command palette: Search / Plus / Calendar / Home / Users
- Mega menu: Home / Inbox

**Komplett ikon-bibliotek (~30-40 ikoner) ship'es senere som SVG-sprite eller individual JSX-komponenter i `@nordover/icons`-pakke.

---

**Konsekvenser samlet:**
- Rammeverket utvides med 7 patterns (4 site headers, 3 footers, AI assistant, onboarding, service-list, sticky-sub-nav, feature-row).
- Ikon-systemet er nå konsekvent outline-stil på tvers.
- Dekker både SaaS-konvensjoner (Linear/Stacked) og editorial (Off Menu).
- Total komponent-overflate: 61+ patterns/komponenter.

**Reverseringskostnad:** Lav. Hver pattern er additive. Hvis en variant ikke brukes, kan den fjernes uten å påvirke andre.
