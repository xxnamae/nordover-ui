# Glossar — Nordover

**Pattern** — En repeaterbar, navngitt visuell/interaksjons-enhet. Eksempel: "Button" (komponent), "Modal" (pattern), "Hero" (section-pattern). Patterns dokumenteres i wiki som CSS + HTML-eksempler.

**Token** — En CSS custom property (`--variabel`) som representerer en design-beslutning (farge, spacing, font-størrelse, radius, shadow osv.). Tokens er kontraktsdokumenter — navn er stabile API'er.

**@layer** — CSS Cascade Layers mekanisme for eksplisitt kontroll over spesifisitet. Nordover bruker 3 lag: `@layer reset`, `@layer tokens`, `@layer utilities`. Ditt prosjekt legger til `@layer brand` (overstyringer) og komponent-lag.

**Triplet** — En tre-delt token-familie: `--*-fg` (forground/tekst), `--*-bg` (background), `--*-border` (border). Eksempel: `--button-surface-*-rest`, `--button-surface-*-hover`. Sikrer semantisk konsistens og WCAG-validert kontrast.

**OKLCH** — Fargespace (Open Color Lab Chroma Hue). Nordover bruker OKLCH fordi det gir lineær lysstyrke-oppfattelse og intuitive hue-rotasjoner. Støttes nativt i moderne browsere (fallback til `#hex` for eldre).

**WCAG** — Web Content Accessibility Guidelines. Nordover sikrer WCAG AA-kontrast (4.5:1 for tekst). Alle fargetripletparinger er validert.

**CLS** (Cumulative Layout Shift) — Et ytelsesmål for uønsket layout-endring under lasting. Nordover unngår CLS ved `size-adjust` på Inter Fallback (null fontmetrikk-endring under web-fonts-lasting).

**Brand-lag** — En `@layer brand { }` du definerer i ditt eget prosjekt for å overstyre token-verdier. Eksempel: custom accent-farge, varmeere gråtoner, custom font-stack.

**Dark-mode-mekanisme** — `:root:has(#dark:checked) { /* dark overrides */ }`. Sjekker om `<input id="dark" type="checkbox">` er checked; hvis ja, aktiverer dark-token-overrides.

**ADR** (Architectural Decision Record) — Et dokument som forklarer *hvorfor* en design-beslutning ble tatt. Alle ADR-er ligger i `docs/wiki/decisions/` datert. Ikke redigéres etter publisering — reversaler dokumenteres i nye ADR-er.

**Shippable** — Kode/filer som er produksjonsklar og kan pusjeres til live. Tokens CSS er shippable; wiki-topics er references (ikke shippable selv, men brukt under implementering).

**Tailwind v4 Syntax** — Nordover sin wiki bruker `@utility` (bare CSS, ingen runtime). Hvis prosjektet **ikke** bruker Tailwind v4, oversett til vanlig `.klasse { }` — laget er garantert av `@layer utilities` i tokens-fila.

**Headless** — UI-komponenter uten Style. Nordover spesifiserer *hva* komponenter gjør (Modal, Drawer osv.), ikke *hvordan* de ser ut (det gjør brand.css). Underliggende libraries (Radix Primitives, cmdk osv.) er headless.

**Component family** — Gruppe av relaterte komponenter. Eksempel: "Buttons" (Button primær, Button sekundær, Button ghost osv.), "Forms" (Input, Select, Checkbox osv.), "Patterns—basis" (Tag, Badge, Avatar osv.).

**Consumption** — Måten et prosjekt bruker Nordover. Model: kopier tokens-CSS, importer først, bruk variabler i egne komponenter, override via brand-lag.

**Monorepo** — Enkelt Git-repo som inneholder flere packages/apps. Eksempel: `apps/web` og `apps/dashboard` deler samme `tokens-web` og `tokens-app` henholdsvis. Bootstrap-guide ligger i `docs/handoff/monorepo-bootstrap.md`.

**localStorage-script** — Lite JS som persisterer tema-valg (`localStorage['theme'] = 'dark'`) så checkbox-state blir husket mellom sidevisninger.
