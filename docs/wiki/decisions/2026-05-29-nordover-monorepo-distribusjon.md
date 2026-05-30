# Nordover lever som workspace-pakker i agency-monorepo

**Dato:** 2026-05-29
**Status:** Aktiv
**Forgjenger:** [v3-polish-og-shippable](2026-05-29-v3-polish-og-shippable.md) (etablerte kanonisk CSS i `docs/visual/tokens/`)

**Kontekst:**
Nordover-byrået flytter fra WordPress + Elementor + WPEngine til Next.js 15 + Payload CMS 3 + Supabase. Et nytt monorepo skal eie hele agency-stack-en: byråets egen nettside (`apps/nordover-site/`) først, kundesider per-app (`apps/<kunde>/`) etter hvert. Claude er hovedutvikler; Nordover-teamet bidrar med design, brand og brief.

Spørsmål: hvor lever den shippable koden for `@nordover/tokens-{web,app}`?

**Alternativer:**

- **A) Workspace-pakker i monorepoet** — `packages/tokens-{web,app}/` med `index.css` = kopi av `xxnamae/notater/docs/visual/tokens/*.css`. Apps konsumerer via `workspace:*`.
- **B) Eget npm-pakke** publisert fra `xxnamae/nordover`, monorepoet konsumerer eksternt.
- **C) Inline-kopi** i hver app, ingen pakke-abstraksjon.

**Valgt:** **A — workspace-pakker i monorepoet.**

**Hvorfor:**
- **Eierskap matcher virkeligheten.** Monorepoet eier shippable kode + er testbench for framework-endringer. `xxnamae/notater` forblir spec/wiki/research-rom (per CLAUDE.md: ingen produksjonskode her).
- **Ingen npm-publish-friksjon** for interne endringer. Bump en token, alle apps får det ved neste build.
- **Tett iterasjon mellom rammeverk og første reelle bruk** (byrå-sida). Hvis monorepoet og notater hadde vært i én pakke-grense ville hver tokens-endring krevd publish.
- **Senere kan pakkene eksternaliseres** hvis tredjeparts-konsumenter dukker opp. Da publisheres fra monorepoet til npm. Reverseringskostnad lav.

**Konsekvenser:**

| Område | Konsekvens |
|---|---|
| Sannhetskilde for tokens-CSS | `xxnamae/notater/docs/visual/tokens/*.css` (spec) → kopieres til `nordover-monorepo/packages/tokens-{web,app}/index.css` (produksjon) |
| Sync-modell | Manuell kopi ved tokens-endring. Loggføres i begge repoer (notater: `docs/log.md`. Monorepo: CHANGELOG eller commit-melding med notater-commit-hash). |
| Drift-risiko | Monorepoets faktiske CSS kan drifte fra notater hvis sync glemmes. Mitigering: månedlig manuell diff, eller scripted check i CI. |
| Versjonering | Pakkene følger monorepoets release-syklus (ikke semver-publish), men `index.css` har kommentar-header som peker til notater-commit. |
| Brand-overstyringer | Per-app: `apps/<navn>/styles/brand.css`, importert etter `@nordover/tokens-*/index.css`. `@layer brand` garanterer kaskade. |

**Reverseringskostnad:** Lav. Hvis monorepoet senere skal slippe pakkene som ekstern npm, er det en build/publish-steg som legges på toppen. Ingen API-endring for konsumenter.

**Pekere:**
- Konkret monorepo-struktur og bootstrap-prosess: [`docs/handoff/monorepo-bootstrap.md`](../../handoff/monorepo-bootstrap.md)
- Generisk framework-konsumsjon: [`docs/handoff/README.md`](../../handoff/README.md)
- Token-spec: [tokens-web.css](../../visual/tokens/tokens-web.css), [tokens-app.css](../../visual/tokens/tokens-app.css)

**Avgjort sammen med (samme økt):**
- Per-kunde-modell: **én Next.js-app per kunde i `apps/<kunde>/`** (ikke multi-tenant, ikke template-fork). Bespoke design per kunde, egen brand.css, egen content-model, egen deploy.
- Bygge-rekkefølge: **byrå-sida først (`apps/nordover-site/`)**, så pilot-kunde. Validerer stack i lav-risiko miljø før kundens krav.
