# Token Consistency & Governance

This document ensures that `tokens-web.css` and `tokens-app.css` remain maintainable despite separation.

## Shared Token Names (Must Exist in Both Files)

The following 153 tokens **must be present** in both `tokens-web.css` and `tokens-app.css`. Values may differ (and are expected to differ). But the name must not diverge.

### Color Primitives
- `--gray-50`, `--gray-100`, `--gray-200`, `--gray-300`, `--gray-400`, `--gray-500`, `--gray-600`, `--gray-700`, `--gray-800`, `--gray-900`

### Color Semantics
- `--color-bg`, `--color-surface`, `--color-subtle`, `--color-fg`, `--color-muted`, `--color-border`
- `--color-accent`, `--color-accent-fg`, `--color-accent-hover`, `--color-accent-active`
- `--error`, `--error-subtle`, `--error-strong`
- `--success`, `--success-subtle`, `--success-strong`
- `--warning`, `--warning-subtle`, `--warning-strong`
- `--info`, `--info-subtle`, `--info-strong`

### Typography
- `--font-sans`, `--font-mono`, `--font-display`
- `--text-2xs`, `--text-xs`, `--text-sm`, `--text-base`, `--text-lg`, `--text-xl`, `--text-2xl`, `--text-3xl`, `--text-4xl`, `--text-5xl`, `--text-6xl`, (web: `--text-7xl`, `--text-8xl`, `--text-9xl`)
- (app: `--text-md`)

### Font Weights
- `--fw-eyebrow`, `--fw-caption`, `--fw-body-sm`, `--fw-body`, (web: `--fw-display-xl`), `--fw-display-lg`, `--fw-display-md`, `--fw-heading-lg`, `--fw-heading-md`, `--fw-heading-sm`, `--fw-semibold`, `--fw-medium`, `--fw-regular`, `--fw-bold`

### Line Height
- `--leading-none`, `--leading-tight`, `--leading-snug`, `--leading-normal`, `--leading-relaxed`, (app: `--leading-loose`)

### Letter Spacing
- `--tracking-tighter`, `--tracking-tight`, `--tracking-normal`, `--tracking-wide`, (app: `--tracking-wider`), `--tracking-widest`

### Spacing (Gap, Padding, Margin)
- `--space-1`, `--space-2`, `--space-3`, `--space-4`, `--space-5`, `--space-6`, `--space-7`, `--space-8`, `--space-10`, `--space-12`, `--space-16`, `--space-20`
- `--gap-component`, `--gap-tight`

### Border & Radius
- `--radius-sm`, `--radius-md`, `--radius-lg`, `--radius-full`
- `--bw-thin`, `--bw-medium`

### Shadows
- `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl`

### Motion
- `--duration-fast`, `--duration-moderate`, (web: `--duration-slow-base`), `--duration-slow`
- `--ease-out`, `--ease-in`, `--ease-in-out`

### Z-Index
- `--z-sticky`, `--z-modal`, `--z-tooltip`

### Sizing
- `--size-icon-sm`, `--size-icon-md`, `--size-icon-lg`

### Container Widths
- (web: `--w-5xl`), (app: `--container-default`)

---

## Platform-Specific Tokens (Documented, Not Validated)

These tokens exist in ONE platform only. They are intentional divergences and documented here (rather than validated by script, which would add complexity).

### App-Only Tokens

These exist **only in `tokens-app.css`** — SaaS/dashboard UI requirements:

**Workflow/Priority (not needed in marketing sites):**
- `--priority-none`, `--priority-low`, `--priority-medium`, `--priority-high`, `--priority-urgent`
- `--status-todo`, `--status-in-progress`, `--status-in-review`, `--status-done`, `--status-blocked`, `--status-canceled`, `--status-backlog`

**Component-specific:**
- `--nav-item-bg-active` (app sidebar hover state)
- `--size-icon-xl` (larger icons for app density)
- `--z-drawer` (drawer z-level)

**SaaS-optimized motion (faster than web):**
- `--ease-in`, `--ease-in-out` (app has these, web doesn't)
- `--leading-loose` (app added for body comfort on compact scale)
- `--tracking-wider` (app added for header breathing room)

**Container constraints:**
- `--container-default`, `--container-wide` (app dashboard breakpoints)

### Web-Only Tokens

These exist **only in `tokens-web.css`** — editorial/marketing requirements:

**Fluid type-scale for hero displays (not in compact app scale):**
- `--text-7xl`, `--text-8xl`, `--text-9xl` (large clamp() scales up to 10rem)
- `--fw-display-xl`, `--fw-display-md` (web's broader weight range)
- `--fw-heading-sm`, `--fw-body` (editorial-specific weights)

**Editorial UI:**
- `--font-display` (includes "Inter Tight" variant for web typography hierarchy)
- `--color-backdrop` (backdrop blur for modals in marketing sites)
- `--z-overlay` (editorial modal positioning)

**Editorial motion:**
- `--duration-slow-base` (web's slower, more deliberate animations)

---

## Rules for Token Changes

### Adding a New Token

1. **If it applies to both platforms:**
   ```
   Add to BOTH files in the same commit.
   ```

2. **If it's platform-specific:**
   ```
   Add only to that file.
   Add comment: /* web-only */ or /* app-only */
   Document in this file's platform-specific section above.
   ```

### Changing a Token Value

```bash
# Edit the value in both files
vim docs/visual/tokens/tokens-web.css
vim docs/visual/tokens/tokens-app.css

# Regenerate JSON
npm run build:tokens

# Commit everything together
git add docs/visual/tokens/tokens-*.css docs/visual/tokens/tokens-*.json
git commit -m "Update --spacing-value for both platforms"
```

**CI will fail if:**
- JSON is out of sync with CSS (run `npm run build:tokens`)
- Token names diverge between platforms (see validation script below)

### Renaming a Token

**Never** rename a token without:
1. Adding a deprecation comment in the source file for 1 release cycle
2. Updating both platforms simultaneously
3. Communicating to downstream consumers (npm package maintainers, styleguide users)

Example:
```css
--color-accent: var(--gray-900);
/* Deprecated: v1.3.0 → use --color-accent-primary instead. Removal: v2.0.0 */
--color-accent-primary: var(--gray-900);
```

---

## Validation

### Manual Checklist (Before Committing)

- [ ] All shared tokens exist in both files
- [ ] Platform-specific tokens are marked with `/* platform-only */`
- [ ] `npm run build:tokens` passes (JSON is generated)
- [ ] `npm run check:tokens` passes (JSON is in sync)

### Automated CI Check (scripts/validate-token-consistency.py)

Checks that both files declare identical token names (except marked platform-exclusive):

```bash
python3 scripts/validate-token-consistency.py
```

**Exit codes:**
- `0` = Success, tokens are consistent
- `1` = Token name divergence detected (see output for details)

**Run in CI:**
```yaml
# .github/workflows/test.yml
- name: Validate token consistency
  run: python3 scripts/validate-token-consistency.py
```

---

## FAQ

**Q: Can I have a token in web but not app?**  
A: Yes, if it's platform-specific. Mark it clearly with `/* web-only */` comment and document above.

**Q: What if I change a token value in web but forget app?**  
A: The validation script will fail (token names must match). Apply the change to both in the next commit.

**Q: What if the two platforms need different token names?**  
A: This breaks the "consistent contract" principle. Discuss in a new ADR. Likely solution: add a new platform-exclusive token instead of renaming.

**Q: Can I add 10 new tokens at once?**  
A: Yes. Add to both files. Document in this file if platform-specific. Run validation before committing.

---

## Related

- `ADR: Web vs. App Token Separation` (`docs/wiki/decisions/2026-06-03-web-vs-app-token-separation.md`)
- Token README (`docs/visual/tokens/README.md`)
- Build script (`scripts/build_tokens.py`)
- Validation script (`scripts/validate-token-consistency.py`)
