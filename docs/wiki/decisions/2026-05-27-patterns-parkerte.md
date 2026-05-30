# Patterns — tidligere parkerte (spec'et)

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Fire patterns ble parkert under fase 2A pga reelle arkitekturvalg som krevde sparring. Spec'et nå med eksplisitte beslutninger: Multi-step Wizard, Inline Edit, Filter Bar, Notification Feed.

---

## 1. Wizard: linear flow + kontrollert state + per-step validation

**Spørsmål:** Linear vs tree-graf, hoppbar vs strict, state-eierskap?

**Valgt:**
- **Linear flow** (steg 1 → 2 → 3 → ...). Ikke tree-graf.
- **Strict navigation:** ingen "hopp over" — neste-knappen er disabled hvis validering feiler.
- **Back er alltid tillatt** — bruker kan endre tidligere svar.
- **Kontrollert state** — parent eier `currentStep`. Komponenten emit'er `onStepChange`.
- **Per-step validation:** `validateStep(stepId) → Promise<true | errors>`. Async-støtte fordi validering ofte krever server-call.

**Hvorfor:**
- Tree-graf-wizards er sjeldne i moderne SaaS (de fleste flows er linear).
- Strict + back balanserer trygghet (bruker fullfører hele flow) med fleksibilitet (kan ombestemme seg).
- Kontrollert state lar parent koble til URL (eks. `/onboarding/team`) og persistere mellom sessions.

---

## 2. Inline Edit: blur som default save-strategi

**Spørsmål:** Save on blur, on enter, eller eksplisitt button?

**Valgt:** **Default: blur** (klikk utenfor). **Enter** lagrer single-line. **Esc** avbryter alltid. **Eksplisitt-modus** tilgjengelig som `saveOn="explicit"`-prop.

**Hvorfor:**
- Blur er mest "frictionless" — bruker klikker, redigerer, klikker bort. Som Google Docs, Notion.
- For multiline (textarea) er Enter ikke save (det er linjeskift) — bruker `Cmd/Ctrl+Enter` eller blur.
- Eksplisitt mode for kritiske felter (eks. pris, kontonummer) der utilsiktet endring er farlig.
- Optimistic UI: vis ny verdi umiddelbart, rollback ved feil. Parent håndterer dette via `onSave`-promise.

---

## 3. Filter Bar: kontrollert state, parent eier URL-sync

**Spørsmål:** Skal komponenten håndtere URL-state, debounce, mm?

**Valgt:** **Stateless** — kun rendrer det parent gir. Emit'er events, ingen intern state.

**Hvorfor:**
- URL-sync er prosjekt-spesifikt (Next.js router vs React Router vs egen).
- Debounce er server-spesifikt (noen API-er trenger 300ms, andre 0).
- TanStack Query / SWR har egne mønstre.
- Komponenten skal være kompatibel med alt → ingen interne assumptions.
- Aktive filtre vises som Tag-komponenter med `onRemove` — bruker kan klikke vekk individuelt eller "Fjern alle" for bulk.

**Filter-typer:** `select` (single), `multi` (multi-select), `date-range`, `boolean`. Hver med egen UI-konvensjon.

**Inactive filters:** vises i "Legg til filter"-dropdown — UI overflod unngås, men alle filtre er tilgjengelige.

---

## 4. Notification Feed ≠ Activity Stream

**Spørsmål:** Hva er forskjellen og hvorfor egen komponent?

**Valgt:** To distinkte komponenter.

| | Activity Stream | Notification Feed |
|---|---|---|
| Bruk | Issue-detalj, audit-log, kommentartråd | Inbox-dropdown, varslings-side |
| Actionable | Nei (read-only) | Ja (marker lest, dismiss) |
| Read state | n/a | Ja (uleste vs leste) |
| Klikk-effekt | Ingen (eller eksterne lenker) | Navigerer + marker lest |
| Layout | Tidslinje | Liste med separators |
| Aktor | Alltid (Eirik gjorde X) | Valgfritt (kan være system-message) |

**Hvorfor:** sammenslåing ville kreve en variant-eksplosjon. Renere som to komponenter.

**Notification Feed-features:**
- Uleste øverst, leste under section-divider.
- Hover viser dismiss-action (ikke alltid synlig — reduserer visuell støy).
- "Marker alle som lest"-knapp øverst når det finnes uleste.
- Tom-state med illustration.
- Load-more for paginering (server-controlled).

---

## Felles arkitektur-prinsipper

- **Kontrollert state** i alle 4. Parent eier sannheten, komponentene rendrer + emit'er.
- **Ingen intern routing** — parent kobler til `href`, `onSelect`, etc.
- **Ingen intern persistence** — parent håndterer localStorage / server-sync.
- **A11y først** — Wizard har `aria-label`, InlineEdit display er tab'bar, FilterBar bruker semantic `<input type="search">`, Notification-items er native `<a>` for keyboard-nav + middle-click-tab-åpning.

**Konsekvenser samlet:**
- 4 patterns til, rammeverket er nå reelt komplett for typiske SaaS-behov.
- Total komponent-overflate: 50+ patterns/komponenter.
- Ingen flere library-avhengigheter — alle 4 patterns bygger på Radix (DropdownMenu) eller custom CSS.

**Reverseringskostnad:** Lav. Hvert pattern kan fjernes uten å påvirke andre.
