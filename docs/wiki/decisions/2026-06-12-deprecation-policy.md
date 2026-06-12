# ADR: Deprecation Policy for Tokens and Classes

- **Dato:** 2026-06-12
- **Status:** Vedtatt
- **Relatert:** Removal of `text-8xl` and `text-9xl` (broken consumer sync in one release)

## Problem

Removing tokens or component classes without warning breaks downstream consumers who:
- Bundle or import Nordover CSS directly
- Transform tokens via machine parsing (Token Studio, design platforms)
- Have pinned versions in monorepos

The removal of `text-8xl` and `text-9xl` in a patch release broke a consumer's build without warning. This should have been caught by a deprecation window.

## Decision

**Deprecation Window: One Minor Release (8 weeks)**

1. **Deprecation phase** (minor version `N.X.0`)
   - Mark token/class for removal in comments: `/* @deprecated since v3.2.0 — use --text-7xl instead. Removing in v3.3.0. */`
   - Keep full functionality; no breaking changes
   - Include removal plan in release notes: "Tokens marked `@deprecated` will be removed in N+1.0"

2. **Removal phase** (minor version `N.X+1.0`)
   - Delete token/class
   - Update `CHANGELOG.md`: list all removed tokens in a dedicated section

3. **No exceptions** for patch releases
   - Removals only in minor versions (X.0.0)
   - Allows consumers time to detect deprecation and update

## Scope

Applies to:
- CSS custom properties (`--*` tokens)
- Class names (`.btn`, `.t-body`, etc.)
- `@layer` structure changes
- Does NOT apply to internal variables, comments, or performance optimizations

## Example

```css
/* Deprecated: --text-8xl */
--text-8xl: clamp(4.5rem, 2.93rem + 7.86vw, 10rem); /* @deprecated since v3.2.0 — use --text-7xl instead. Removing in v3.3.0. */
```

Release notes for v3.2.0:
```
## Deprecations
- `--text-8xl`, `--text-9xl` marked for removal. Use `--text-7xl` as maximum display size. These tokens will be removed in v3.3.0.
```

Release notes for v3.3.0:
```
## Breaking Changes
- Removed deprecated tokens: `--text-8xl`, `--text-9xl`. Use `--text-7xl` instead.
```

## Rationale

- **One minor release** = ~8 weeks on typical semver; enough time to detect via CI
- **Comments in code** = discoverable; searchable by consumers
- **Release notes** = forces explicit awareness
- **Minor (not patch)** = consumers can pin patch versions safely
