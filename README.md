# nordover-ui

Nordover is a CSS framework and pattern library for the Nordover agency. It offers two packages with identical architecture but different defaults:

- **tokens-web** — for marketing sites and editorial content (light theme, fluid typography, flat buttons)
- **tokens-app** — for SaaS interfaces and dashboards (dark theme, static typography, tactile buttons)

## Getting Started

Start with [`docs/handoff/README.md`](docs/handoff/README.md), the canonical entry point for framework consumption.

The framework can be implemented in five steps:
1. Retrieve the appropriate tokens file (`tokens-web.css` or `tokens-app.css`)
2. Import it into your application entry point
3. Add a theme toggle (light/dark)
4. Build components using CSS custom properties
5. Load the Inter Variable font

## Key Resources

- **Handoff docs**: `docs/handoff/README.md` — framework consumption guidance
- **Tokens**: `docs/visual/tokens/` — CSS variable files for both packages
- **Styleguides**: `docs/visual/styleguide-web.html` and `styleguide-app.html` — visual reference
- **Component specs**: `docs/wiki/topics/nordover-*.md` — detailed specifications by family
- **ADRs**: `docs/wiki/decisions/` — architectural decision records

## Current Status

Framework version 3, currently in polish phase (2026-05-29). Changes are documented in CSS header comments.

## License

MIT — see [`LICENSE`](LICENSE) file.

## Issues & Contributions

Issues and pull requests welcome in the main repository.
