# CSS Format Contract — Nordover Design System

**External consumers transform these files via machine parsing.** This document specifies the CSS structure constraints that cannot be refactored without breaking consumers.

## Invariants

### Selector Formatting
- **One selector list per line**, ending with `{`
- Selectors on the same line separated by comma (no newline between siblings)
- Example: `✓ .btn, .button { color: red; }`
- Example: `✗ .btn,\n.button { color: red; }`

### Token Definitions
- All design tokens (`--*` variables) defined exclusively in `:root` blocks
- Tokens in light mode: `:root { --color-fg: ...; }`
- Tokens in dark mode: `:root:has(#dark:checked) { --color-fg: ...; }` or `:root.dark { --color-fg: ...; }`
- No tokens inside selectors that aren't `:root` variants
- No CSS custom property fallbacks within component rules (keep tokens pure)

### No CSS Nesting
- All selectors written flat; no nested syntax (`&` operator)
- Even though modern CSS supports nesting, consumers parse line-by-line and don't understand nesting
- If nesting is needed for readability, use separate rule blocks instead

### Special Rules
- `@keyframes` definitions: preserve as-is (not transformed)
- `@font-face` definitions: preserve as-is
- `@layer` directives: preserve as-is
- `@media` queries: preserve structure (but tokens inside `:root:has()` variants are transformed)

### Component Rules
- Component rules start with a selector like `.btn`, `.card`, `.modal`
- Properties follow immediately (no pseudo-classes/elements mixed with properties)
- Pseudo-classes/pseudo-elements on separate lines: `.btn:hover { ... }` (separate rule)
- Example ✓:
  ```css
  .btn { 
    display: inline-block;
    color: var(--color-fg);
  }
  .btn:hover {
    background: var(--color-accent);
  }
  ```
- Example ✗ (not parseable):
  ```css
  .btn {
    display: inline-block;
    &:hover { background: var(--color-accent); }
  }
  ```

### Import vs Inline
- `@import` statements at top of file (not supported by all transformers; prefer direct inclusion)
- If importing, use `@import url(...)` syntax, not bare `@import "file.css"`

## Why This Matters

Nordover's consumers (Token Studio, design system platforms) use line-by-line parsing to:
1. **Extract token definitions** from `:root` blocks
2. **Scope selectors** into component namespaces (e.g., wrap `.btn` as `.nordover .btn`)
3. **Inject overrides** for themes/variants
4. **Map tokens** to platform-native design systems

Violations break these transformations silently. Changes to this file should be announced in release notes with `major` version bump.

## Changelog

- **2026-06-12**: Contract established. Current files (`tokens-*.css`, `components-*.css`) adhere fully.
