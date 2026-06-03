# Token Consistency & Governance

**153 shared tokens** exist in both files. Values differ, but names must not diverge.

## Shared Token Categories

**Color primitives:** `--gray-50` to `--gray-950`, `--neutral-h`, `--neutral-c`  
**Color semantics:** `--color-{bg,surface,fg,subtle,muted,border}`, `--color-accent*`, `--error*`, `--success*`, `--warning*`, `--info*`  
**Typography:** `--font-{sans,mono}`, `--text-{2xs..6xl}`, `--fw-*`, `--leading-*`, `--tracking-*`  
**Spacing:** `--space-{0,px,1..48}`, `--gap-{tight,component}`  
**Radius & borders:** `--radius-*`, `--bw-*`  
**Shadows:** `--shadow-*`  
**Motion:** `--duration-*`, `--ease-out`, `--ease-spring*`  
**UI:** `--z-{base,dropdown,sticky,modal,toast,tooltip}`, `--size-icon-{sm,md,lg}`

**Full list:** See tokens-web.css `:root` block (lines 90–290)

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
