# To tokens-pakker: web og app

**Dato:** 2026-05-27
**Status:** Aktiv

**Kontekst:**
Nordover-stacken brukes både til marketing-nettsider og til SaaS-grensesnitt (Omhu, framtidige produkter). Disse har motstridende krav til typografi-skala, spacing og fluid-strategi. Vi måtte velge om ett token-sett skulle dekke begge, eller om vi skulle splitte.

**Alternativer:**
- A) **Én preset for alt.** Brand-overstyring i `clients/<slug>.css` håndterer forskjeller. Færre filer, mindre vedlikehold.
- B) **To pakker:** `@nordover/tokens-web` (marketing) og `@nordover/tokens-app` (SaaS). Hver med eget skala-grunnlag.
- C) **Én base + to "registre"** i samme fil (eks. `--text-display-6xl` og `--ui-text-base`). Felles fil, ulike namespaces.

**Valgt:** B — to separate pakker.

**Hvorfor:**
- Marketing trenger fluid display-sizes opp til 76px og fluid section-spacing for visuell flyt. Apper trenger statiske, kompakte verdier for info-tetthet.
- Body-size er forskjellig: 16px for marketing (lesbarhet), 14px for SaaS (info-tetthet). Det betyr at `--text-base` MÅ bety ulike ting i de to kontekstene — kan ikke leve i samme fil.
- C-alternativet (felles fil, ulike namespaces) ble vurdert, men gir en utvikler-felle: "hvilken skala bruker jeg her?" — to filer gjør valget eksplisitt allerede ved import.
- A-alternativet ble forkastet fordi det ville krevd overstyring av nesten alle tokens i Omhu sin brand-fil — det er ikke en brand-overstyring, det er et nytt token-sett.

**Konsekvenser:**
- Vedlikehold av to skala-systemer i stedet for ett. Aksepteres som pris for klarhet.
- Felles prinsipper (line-height-kurve, z-index, focus-ring, reduced-motion, dark mode) må synkroniseres mellom pakkene manuelt — vurder å ekstrahere `tokens-core.css` senere hvis det blir tungt.
- Brand-overstyrings-patternet (`clients/<slug>.css`) består uendret per pakke.
- Komponenter i `@nordover/ui` må enten være token-agnostiske eller leveres som to varianter. Trolig token-agnostiske: bruker semantiske tokens som finnes i begge pakker (`--color-fg`, `--color-bg`, `--spacing-section`).

**Reverseringskostnad:** Middels. Hvis vi vil slå sammen senere må vi rename tokens i alle Omhu-/Nordover-prosjekter samtidig. Ikke katastrofalt, men ikke gratis.
