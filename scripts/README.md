# `scripts/` — build &amp; QA tooling

Developer tooling for the Nordover design system. **Not shipped** in the npm
package (`package.json#files` only publishes the token/component CSS + JSON), so
these are free to depend on a local toolchain. CSS remains the single source of
truth; nothing here hand-edits the canonical tokens.

| Script | npm alias | What it does |
|---|---|---|
| `build_tokens.py` | `npm run build:tokens` | Generate DTCG JSON from the canonical CSS tokens. `--check` verifies sync (CI). |
| `validate-token-consistency.py` | — (CI) | Assert token names match across web/app packages. |
| `check_contrast.py` | `npm run check:contrast` | Convert the OKLCH ramp → WCAG luminance and assert every semantic fg/bg pair (light + dark) meets AA. `--strict` exits non-zero on failure (CI). |
| `generate_theme.py` | `npm run gen:theme` | Linear-style 3-input theme generator (base neutral + accent + contrast) → drop-in `:root` light/dark block. Output only. |
| `screenshots.cjs` | `npm run shots` | Render the styleguide + examples at the three QA breakpoints × light/dark via Playwright Chromium; writes PNGs to `/tmp/nordover-shots`. |

## Quality gates (CI — `.github/workflows/test.yml`)

On every push/PR the `tokens` job runs:
1. `build_tokens.py --check` — JSON in sync with CSS
2. `validate-token-consistency.py` — web/app token-name parity
3. `check_contrast.py --strict` — **contrast-by-construction** (AA, both modes)

A separate `a11y-audit.yml` runs pa11y/axe against the rendered styleguide.

## Examples

```bash
# Verify contrast (deterministic, no browser)
npm run check:contrast

# Generate a branded theme
npm run gen:theme -- --accent "oklch(0.58 0.13 215)" --contrast high > my-theme.css

# Visual QA — 18 frames (auto-starts a static server if none is running)
npm run shots
```

### `screenshots.cjs` notes

Self-contained: it resolves the `playwright` module from a local/global install,
prefers a pre-installed Chromium at `/opt/pw-browsers` (this managed env) and
otherwise uses Playwright's default cache, and auto-starts/stops a static server
on `:8000` when one isn't already running. For a fresh local checkout:

```bash
npm i -D playwright && npx playwright install chromium
npm run shots
```

To prove RTL-correctness (logical properties), set `dir="rtl"` on the document in
a one-off script — the sidebar, table alignment and badges mirror with no
RTL-specific CSS.
