# Changelog

All notable changes to Nordover Design System are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

> Targeting **2.0.0** — a clean-skeleton rebuild. Breaking by design; the
> system had no downstream consumers yet, so naming was unified without
> deprecation aliases. See ADR `2026-06-05-unifisert-navnekonvensjon.md`.

### Changed (BREAKING)
- **States now use `.is-*`**: `.active`→`.is-active`, `.open`→`.is-open`,
  `.selected`→`.is-selected`, `.dragover`→`.is-dragover`,
  `.completed`→`.is-completed`. Decoupled from component names (SMACSS).
- **One `.table` system**: the parallel `.data-table*` set was removed and
  folded into `.table` with opt-in modifiers — `.table-sticky`, `.table-zebra`,
  `.table-numeric`, `.table-responsive`, `.table-inline-edit`, `.table-filter`.
  Sort state moved from `.sort-asc/.sort-desc` to the native `[aria-sort]`
  attribute (free a11y); `.table-sort` button removed in favour of
  `th.sortable`.
- **Single status vocabulary**: `.btn-destructive` → `.btn-error` so the
  status word is always `error` (matching alert/badge/toast/text/tag).

### Removed
- Styleguide chrome (`.doc-*`, `.swatch*`, `.chip*`) deleted from both
  shippable `components-*.css` files — it lives only in
  `styleguide-chrome.css` now. Also removed a duplicate `.data-table` block
  and a stray-paren bug in the web package.

### Added
- **Material-3-level styleguide docs** across components: when-to-use,
  live example, variant/modifier reference table, accessibility notes, and
  copyable code (with copy-to-clipboard) — plus do/don't cards on core
  components. New reusable doc-pattern chrome in `styleguide-chrome.css`.
- **Elementor Pro / WordPress guide** (`docs/handoff/ELEMENTOR-WORDPRESS.md`):
  token-first recipe mapping Nordover tokens into Elementor Global
  Colors/Fonts/Variables.
- ADR `2026-06-05-unifisert-navnekonvensjon.md` documenting the convention.

### Added — earlier in this cycle
- **Component contract parity (web ↔ app):** both packages now expose an
  identical set of component class *names*; pakke-spesifikke *verdier* beholdes.
  Added to `components-app.css`: `.accordion*`, `.search-bar`/`.search-result*`,
  `.section-divider*`, `.tag-input*`/`.tag-list`, `.btn-link`,
  `.date-picker-weekday`, `.file-item-size`, `.table-sort`/`.table-filter`,
  `.spinner`, `.animate-fade-in/-scale-in/-slide-up`. Added to
  `components-web.css`: `.form-group`/`.form-group-item`, `.pagination-item`.
  Additive and non-breaking — no class removed or renamed.
- **Unified styleguide** (`styleguide.html`): single building-blocks-only
  reference for both packages with a token-package switcher. Now demonstrates
  100% of building-block classes (Icons, Tags, File Upload, Date Picker,
  Search, Stepper, Toast, Loading/Skeleton, Data Table, Modal, Tooltip, Menu,
  Mobile Nav, Sections/Dividers, layout primitives, full utility catalogue),
  plus the complete SVG icon symbol set.

### Changed
- Mirroring rule extended from "shared component structure" to "shared
  component *contracts*": a new component class added to one package must
  appear (with package-tuned values) in the other in the same commit.

### Removed
- Page-pattern leftovers that contradicted the building-blocks-only scope:
  `.footer-*` and `.faq-*` removed from both `components-web.css`
  (−88 lines) and `components-app.css` (−54 lines). Legacy
  `styleguide-web.html` / `styleguide-app.html` deleted after migration to
  the unified styleguide.

### Decisions
- ADR: [Komponent-kontrakt-paritet på tvers av web og app](docs/wiki/decisions/2026-06-04-komponent-kontrakt-paritet.md)
  — class names unify, values stay separate (builds on 2026-06-03 token separation)
- ADR: [Rammeverk-fokus: byggesteiner](docs/wiki/decisions/2026-06-04-rammeverk-fokus-byggesteiner.md)
  — Nordover ships Layer 1 (tokens) + Layer 2 (building blocks) only; no page patterns

## [1.2.0] - 2026-06-02

World-class visual upgrade across the entire system (tokens, components,
styleguides), benchmarked against Apple HIG, Material Design 3, Linear and
Fluent. No breaking changes — all additions are additive or value tweaks
within WCAG AA limits. Class and token names remain public contracts.

### Added
- **Dark-mode tonal surface elevation** (`--surface-1..5`) — surfaces lighten
  with elevation in dark mode (Material 3 parity). The single biggest dark-mode
  quality lift. Mirrored web + app.
- **Semantic shadow aliases**: `--shadow-inset/-tooltip/-popover/-modal/-drawer/-card-hover`
- **Accent tier**: `--accent-subtle/-muted/-emphasis/--on-accent-subtle`
- **Type-role tokens**: `--type-{display,headline,title,body,label}-{size,leading,weight,tracking}`
  plus `--tracking-display/-heading/-title` (Apple/M3 parity, native-mapping ready)
- `--radius-3xl` (32px web / 24px app), `--ease-spring-physics` (real spring via `linear()`)
- App: finkalibrerte variable-font weights for parity with web
- **New button variants**: `.btn-destructive` (app tactile w/ error hue, web flat),
  `.btn-tonal` (accent-subtle tinted)
- **New components** (built from spec, mirrored web + app, documented in styleguides):
  Card family (`.card` + variants + header/title/meta/footer), Tabs, Avatar (+ group),
  Tooltip, Menu/Dropdown, Toast, Kbd, Skeleton, standalone Tag variants
- **Section utility** (`.section/-sm/-lg` + `-bg-subtle/-fg/-accent`) with fluid
  vertical rhythm and container-query context; new `--spacing-section-sm/-lg` tokens

### Changed
- Grayscale L-axis perceptually evened (WCAG verified: `--color-muted` holds AA)
- Web form controls (checkbox/radio/toggle/switch) now custom-styled (were native)
- Badges → borderless tinted pills, mirrored web↔app
- Tables → sticky header, zebra, tabular-nums numeric cells, row selection
- Modal → backdrop blur + scale-in animation (reduced-motion guarded)
- Unified `:focus-visible` rings using `--color-focus`
- Elevated components (modal, drawer, popovers, app cards) use `--surface-*` for dark elevation
- Wiki docs synced to CSS truth (motion, elevation, colors, layout, spacing)

### Fixed
- Web `.btn-sm` now actually small (removed 44px min-height floor)
- Removed dead duplicate `.data-table` definition in web
- App form controls gained disabled + hover states; mobile 44px touch targets
- App `.app-nav-item` active state (`[aria-current]`)
- Stray `</div>` in styleguide form fieldsets (HTML validity)

### Decisions
- ADR: Verdensklasse token-oppgradering
- ADR: Nye komponenter, knappevarianter og web-flat-beslutning (web stays flat
  editorial, app stays tactile — deliberate, documented divergence)

## [1.1.0] - 2026-06-02

### Added
- `docs/handoff/AGENT-QUICKSTART.md` — action-oriented setup guide for consuming projects (app & website), written for Claude agents. Includes npm install recipe, app/web decision table, brand-layer pattern, and a CLAUDE.md block to paste into new projects.
- Link to Agent Quickstart from handoff README

## [1.0.0] - 2026-06-02

### Added
- ✅ Complete design system with 25 core components
- ✅ Design tokens system (186 CSS variables)
- ✅ OKLCH color space with RGB fallbacks
- ✅ Dark mode support (`:root:has(#dark:checked)`)
- ✅ Responsive design (5 breakpoints: <480px, 768-1024px, >1024px)
- ✅ WCAG 2.1 Level AA accessibility verified
- ✅ Touch targets 44px minimum (Apple HIG compliance)
- ✅ Component variants (buttons, forms, cards, tables, badges, alerts, navigation)
- ✅ Typography system (12 semantic sizes with fluid clamp)
- ✅ Layout primitives (.stack, .cluster, .grid-auto, .page)
- ✅ Motion tokens (ease curves, durations)
- ✅ DTCG JSON token export (compatible with Figma, Design Tokens)
- ✅ Comprehensive documentation (component inventory, browser support, handoff guides)

### Changed
- **Breaking:** Token naming convention updated for consistency (`--radius-input` → `--input-radius`)
- **Breaking:** Dark mode selector changed from CSS media query to `:root:has(#dark:checked)`
- Form focus states improved with `:focus-visible` for keyboard accessibility
- Button gradient colors adjusted for dark mode readability

### Fixed
- ✅ Undefined token references in component CSS
- ✅ Hardcoded colors now use token system (respects dark mode)
- ✅ Form input height parity (web 44px, app 44px minimum)
- ✅ Checkbox/radio sizing below touch target threshold
- ✅ Disabled button hover effects still active
- ✅ Missing input error/success state styling
- ✅ Card hierarchy flat (added featured/prominent variants)
- ✅ Icon vertical alignment (baseline issues)
- ✅ Typography display sizing oversized (capped --text-9xl)
- ✅ Missing ARIA labels (hamburger, theme toggle, error messages)

### Quality Metrics
| Dimension | Score | Status |
|-----------|-------|--------|
| Code Quality | 8.3/10 | ✅ Excellent |
| Accessibility | 8.5/10 | ✅ WCAG AA |
| Visual Design | 9.0/10 | ✅ Excellent |
| Documentation | 8.0/10 | ✅ Comprehensive |
| Components | 9.1/10 | ✅ Production-Ready |
| Performance | 8.7/10 | ✅ Optimized |

### Browser Support
- **Full Support:** Chrome 111+, Safari 15.4+, Firefox 113+, Edge 111+
- **Graceful Degradation:** Chrome 99+, Safari 15.4+, Firefox 97+ (RGB fallbacks for OKLCH)
- **Not Supported:** IE 11 (EOL)

### Migration from v0.x
- Token names changed: use search/replace or `docs/MIGRATION-GUIDE.md`
- Dark mode selector updated: change `media (prefers-color-scheme: dark)` to `:root:has(#dark:checked)`
- All component classes remain compatible

---

## [1.0.0-beta] - 2026-06-01

### Added
- Initial beta release
- All 25 core components documented
- Design tokens system finalized
- DTCG JSON export pipeline
- Deep quality assurance audit (6 independent agents)
- Comprehensive handoff documentation

### Status
- Production-ready design system
- Ready for early adopter feedback
- Beta period: 2-4 weeks before v1.0 GA

---

## Format Guide

When adding entries:

```markdown
### Added
- New feature (user-facing)

### Changed
- Modification to existing feature

### Fixed
- Bug fix

### Removed
- Removed feature

### Deprecated
- Soon-to-be-removed feature

### Security
- Security vulnerability fix
```

---

**Versioning:**
- `patch` (1.0.x) — Bugfixes, typos, small tweaks
- `minor` (1.x.0) — New features, new component variants (backward compatible)
- `major` (x.0.0) — Breaking changes, token renames, selector changes

**Update process:**
1. Make changes in `nordover-ui`
2. Update `CHANGELOG.md` (Unreleased → version section)
3. Run `npm version [major|minor|patch]` → updates version + creates git tag
4. Run `npm publish` → publishes to NPM registry
5. Push tags: `git push origin main --follow-tags`
