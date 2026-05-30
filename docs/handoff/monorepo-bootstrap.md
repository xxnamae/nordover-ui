# Monorepo-bootstrap — Nordover-byråets web-stack

> **Du som leser dette:** Du er Claude Code-agenten som setter opp / utvider Nordover-byråets nye monorepo (Next.js 15 + Payload CMS 3 + Supabase). Denne fila beskriver **hvordan Nordover-rammeverket er strukturert i dette monorepoet** og hvordan nye apps konsumerer det. For generisk framework-konsum (uavhengig av monorepo), se [`README.md`](README.md). For arkitektur-rasjonale, se [decision: monorepo-distribusjon](../wiki/decisions/2026-05-29-nordover-monorepo-distribusjon.md).

---

## 1. Monorepo-strukturen (anbefalt)

```
nordover-monorepo/
├── package.json                       (workspaces declared)
├── pnpm-workspace.yaml                ("apps/*", "packages/*")
├── turbo.json                         (build-orchestrering, cache)
├── tsconfig.base.json                 (strict, alle pakker arver)
├── biome.json                         (lint + format — eller eslint+prettier)
├── CLAUDE.md                          (agent-regler for monorepoet — se § 6)
├── README.md                          (kort: peker til nordover-ui for spec)
│
├── apps/
│   ├── nordover-site/                 ← byrå-sida (første ut)
│   │   ├── package.json               (deps: @nordover/tokens-web)
│   │   ├── app/                       (Next.js 15 App Router)
│   │   │   ├── layout.tsx             (import tokens + brand + theme-toggle)
│   │   │   └── ...
│   │   ├── styles/
│   │   │   └── brand.css              (@layer brand med nordover-overstyringer)
│   │   ├── public/fonts/              (Inter Variable selvhostet)
│   │   └── payload.config.ts          (CMS-config med byrå-content-modeller)
│   │
│   └── <kunde>/                       ← kommer etter byrå-sida
│       └── (samme struktur, egen brand.css, egen payload.config)
│
└── packages/
    ├── tokens-web/                    ← framework-pakke for nettsider
    │   ├── package.json               ({"name": "@nordover/tokens-web", "main": "index.css"})
    │   ├── index.css                  ← KOPI av xxnamae/nordover-ui/docs/visual/tokens/tokens-web.css
    │   ├── components.css             ← KOPI av .../docs/visual/components/components-web.css
    │   └── README.md                  ← peker til nordover-ui wiki for spec
    │
    ├── tokens-app/                    ← framework-pakke for apper
    │   ├── package.json               ({"name": "@nordover/tokens-app", ...})
    │   ├── index.css                  ← KOPI av xxnamae/nordover-ui/docs/visual/tokens/tokens-app.css
    │   ├── components.css             ← KOPI av .../docs/visual/components/components-app.css
    │   └── README.md
    │
    ├── ui-web/                        ← felles React-komponenter for nettsider (vokser organisk)
    │   ├── package.json
    │   └── src/                       (Button, Card, Hero, Section, etc. — etter behov)
    │
    ├── ui-app/                        ← felles React-komponenter for apper
    │   └── src/
    │
    └── payload-blocks/                ← Payload Blocks som matcher Nordover-section-patterns
        ├── package.json
        └── src/
            ├── HeroBlock.ts           ← matcher nordover-section-patterns.md § Hero
            ├── FeatureGridBlock.ts    ← matcher § Feature Grid
            ├── CTABlock.ts
            └── ...
```

**Begrunnelse for strukturen:**
- **apps/ vs packages/** er standard pnpm-pattern. Apps er deploy-bare enheter; packages er gjenbrukbar kode.
- **tokens-{web,app} er kun CSS**, ingen TypeScript-build. Pakkene har bare `index.css` + minimal `package.json`. Build-rask, tree-shake-trivial.
- **ui-{web,app} og payload-blocks vokser organisk** — ikke spec dem ferdig før dere trenger en gjenbruksanledning. To apps som har samme Hero-implementasjon → flytt til `ui-web`. Først dérfra.
- **Per-app brand.css** — aldri overstyr tokens i komponent-CSS, aldri i tokens-pakken selv.

## 2. Tooling-anbefalinger

| Lag | Anbefalt | Hvorfor |
|---|---|---|
| Package manager | **pnpm** | Raskere enn npm/yarn for monorepoer. Strenge node_modules. |
| Build orchestrering | **Turborepo** | Cache + parallell. Vercel-eid, integrerer godt med Next.js. |
| TypeScript | **strict + noUncheckedIndexedAccess** | Strict alle pakker, ingen unntak. Catch fail-on-build. |
| Lint + format | **Biome** | Én config, raskt, erstatter ESLint+Prettier. |
| Test | **Vitest** (unit) + **Playwright** (e2e) | Vitest matcher Vite-ekosystemet; Playwright for kritiske flows. |
| Deploy | **Vercel** (per app) | Per-app deploy via build-filter `--filter=apps/nordover-site`. |
| CMS | **Payload CMS 3** (self-hosted) | Per per-app Payload-instans deploy'd sammen med Next.js. |
| Database | **Supabase** (Postgres + Auth + Storage) | Felles instans per kunde, separate prosjekter for prod/staging. |

## 3. Hvordan tokens kommer inn i en app

### Steg 1: dependency

```json
// apps/nordover-site/package.json
{
  "dependencies": {
    "@nordover/tokens-web": "workspace:*"
  }
}
```

`workspace:*` er pnpm-syntax for "bruk siste workspace-versjon, ikke npm-publish".

### Steg 2: import i app entry

```ts
// apps/nordover-site/app/layout.tsx
import "@nordover/tokens-web/index.css";        // tokens + reset
import "@nordover/tokens-web/components.css";    // primitives + components + utilities
import "../styles/brand.css";   // alltid ETTER tokens+components — overstyrer

import { Inter } from "next/font/google";  // eller selvhostet variant — se Steg 4

export default function RootLayout({ children }) {
  return (
    <html lang="nb">
      <body>
        {/* Theme-toggle-checkbox + persistens — se Steg 3 */}
        <input id="dark" type="checkbox" className="sr-only" aria-label="Mørk modus" />
        {children}
        <ThemePersistScript />
      </body>
    </html>
  );
}
```

### Steg 3: ThemePersistScript

Egen komponent, render i RootLayout:

```tsx
// apps/nordover-site/components/theme-persist-script.tsx
export function ThemePersistScript() {
  return (
    <script
      dangerouslySetInnerHTML={{
        __html: `
          (function() {
            var key = 'nordover-theme';
            var input = document.getElementById('dark');
            if (!input) return;
            try {
              var saved = localStorage.getItem(key);
              if (saved === 'dark') input.checked = true;
              else if (saved === 'light') input.checked = false;
              else if (window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches) input.checked = true;
              input.addEventListener('change', function() {
                localStorage.setItem(key, this.checked ? 'dark' : 'light');
              });
            } catch (e) {}
          })();
        `,
      }}
    />
  );
}
```

For **kunde-apps med tokens-app** (dark default): sett `defaultChecked={true}` på `<input>` og kommentér ut `matchMedia`-linjen.

### Steg 4: Inter Variable

Anbefalt selvhostet for å unngå CDN-avhengighet:

```tsx
// apps/nordover-site/app/layout.tsx
import localFont from "next/font/local";

const interVariable = localFont({
  src: "../public/fonts/InterVariable.woff2",
  variable: "--font-inter",
  display: "swap",
  preload: true,
});

const interTightVariable = localFont({
  src: "../public/fonts/InterTightVariable.woff2",
  variable: "--font-inter-tight",
  display: "swap",
  preload: true,
});

// I <html className={`${interVariable.variable} ${interTightVariable.variable}`}>
```

Inter Fallback med `size-adjust` ligger allerede i `@nordover/tokens-web/index.css` — null CLS uansett.

## 4. Brand-overstyring per app

```css
/* apps/nordover-site/styles/brand.css */
@layer brand {
  :root {
    /* Nordover-byråets egen accent (eksempel — bytt til virkelig brand-farge): */
    --color-accent: oklch(0.55 0.18 230);
    --color-accent-fg: white;

    /* Hvis byrået vil ha varmere gråtoner: */
    --neutral-h: 30;

    /* Tyngre display-vekt for autoritet: */
    --fw-display-lg: 500;
  }

  :root:has(#dark:checked) {
    --color-accent: oklch(0.65 0.20 230);
  }
}
```

**Aldri** overstyr `--gray-*` direkte (bryter WCAG-validert kontrast). Endre `--neutral-h` (hue) for tone-shift.

## 5. Sync fra nordover-ui til monorepoet

Når tokens endres i `xxnamae/nordover-ui/docs/visual/tokens/*.css`:

1. **Diff først** mot forrige sync:
   ```sh
   git -C path/til/nordover-ui log --oneline docs/visual/tokens/tokens-web.css
   ```

2. **Les decision-filer** datert nyere enn forrige sync for å forstå hva som endret seg.

3. **Kopier CSS** (BÅDE tokens og komponenter — de er to halvdeler av samme rammeverk):
   ```sh
   cp path/til/nordover-ui/docs/visual/tokens/tokens-web.css packages/tokens-web/index.css
   cp path/til/nordover-ui/docs/visual/components/components-web.css packages/tokens-web/components.css
   cp path/til/nordover-ui/docs/visual/tokens/tokens-app.css packages/tokens-app/index.css
   cp path/til/nordover-ui/docs/visual/components/components-app.css packages/tokens-app/components.css
   ```

4. **Header-kommentar i index.css** oppdateres med nordover-ui-commit-hash:
   ```css
   /*
    * @nordover/tokens-web — synced fra xxnamae/nordover-ui
    * Nordover-ui commit: <hash>
    * Sync-dato: YYYY-MM-DD
    */
   ```

5. **Commit i monorepoet**:
   ```
   chore(tokens-web): sync fra nordover-ui <hash>
   ```

6. **Test alle apps visuelt** — særlig dark mode, focus-rings, knapper.

Hvis sync-frekvensen blir høy: vurder et `scripts/sync-nordover-tokens.sh` som automatiserer steg 3-4. Frem til da: manuelt.

## 6. CLAUDE.md i monorepoet (anbefalt)

Det nye monorepoet bør ha sin egen `CLAUDE.md` med regler. Inkluder minimum:

```markdown
# CLAUDE.md — nordover-monorepo

## Stack
Next.js 15 (App Router) + Payload CMS 3 + Supabase. pnpm + Turborepo. TypeScript strict.

## Rammeverk
UI-fundament: Nordover (`@nordover/tokens-{web,app}`). Spec lever i xxnamae/nordover-ui.
Les xxnamae/nordover-ui/docs/handoff/README.md før du rører UI. Les
xxnamae/nordover-ui/docs/handoff/monorepo-bootstrap.md for denne monorepo-strukturen.

## Regler
- Aldri overstyr tokens på komponent-nivå. Brand-overstyringer kun i apps/<app>/styles/brand.css.
- Ikke patch tokens-pakkene lokalt — endringer går i nordover-ui, så syncs.
- Hvis pattern mangler eller token er feil: åpne issue i xxnamae/nordover-ui, ikke fix her.
- Per skjerm / per feature = egen commit. Norsk bokmål.
- Test både light og dark mode + a11y (tab, reduced-motion) før PR-ferdig.

## Stack-spesifikt
[Påfyll etter hvert som monorepoet vokser — Payload-konvensjoner, Supabase-tilgangslag, etc.]
```

## 7. Payload Blocks som matcher Nordover-section-patterns

Når dere bygger Payload-blocks for kundesider, map dem direkte til Nordover-section-patterns (fra `docs/wiki/topics/nordover-section-patterns.md` og `nordover-patterns-utvidelser-2.md` i nordover-ui):

```ts
// packages/payload-blocks/src/HeroCenteredBlock.ts
import type { Block } from "payload";

export const HeroCenteredBlock: Block = {
  slug: "hero-centered",
  labels: { singular: "Hero (centered)", plural: "Hero-seksjoner (centered)" },
  fields: [
    { name: "eyebrow", type: "text" },
    { name: "title", type: "text", required: true },
    { name: "subtitle", type: "textarea" },
    { name: "ctaPrimary", type: "group", fields: [...] },
    { name: "ctaSecondary", type: "group", fields: [...] },
  ],
};
```

Tilsvarende komponenter i `packages/ui-web/`:

```tsx
// packages/ui-web/src/blocks/HeroCentered.tsx
// Renderer Hero-centered med Nordover-tokens (class names matcher nordover-section-patterns.md)
```

Dette gir Payload-redaktører Elementor-lignende blokk-bygging, men med disciplin: hver blokk er en Nordover-pattern, ikke tomme div'er med custom styling.

## 8. Build & deploy

### Local dev
```sh
pnpm install
pnpm dev --filter=apps/nordover-site
```

### CI (GitHub Actions, eksempel)
```yaml
- pnpm install --frozen-lockfile
- pnpm turbo run typecheck lint test build
```

### Deploy
Per app via Vercel project. Root directory = `apps/nordover-site`. Build command = `pnpm turbo run build --filter=apps/nordover-site`.

Når en kunde-app legges til: ny Vercel project, samme mønster, peker til `apps/<kunde>/`.

## 9. Hva som IKKE bygges først

For å unngå over-engineering ved oppstart:

- **Ikke spec ui-web / ui-app pakkene før dere har to apps som faktisk deler komponenten.** Gjenbruk = forhastet abstraksjon.
- **Ikke bygg Payload-blocks før kunde-1 trenger dem.** Byrå-sida kan klare seg med hard-kodede Next.js-komponenter først.
- **Ikke automatiser sync-script før manuell sync er gjort 3-5 ganger** og dere kjenner friksjonen.

## 10. Hvis du sitter fast

- Generisk framework-spørsmål → [`docs/handoff/README.md`](README.md)
- Spec-detalj på en pattern → `xxnamae/nordover-ui/docs/wiki/topics/nordover-*.md`
- Token-detalj → `xxnamae/nordover-ui/docs/wiki/topics/nordover-arkitektur.md`
- Hvorfor noe er som det er → `xxnamae/nordover-ui/docs/wiki/decisions/`
- Strategi-spørsmål for monorepoet (stack-valg, arkitektur, content-model) → spør Eirik
