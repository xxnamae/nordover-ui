# ADR: Web vs. App Token Separation

**Date:** 2026-06-03 | **Status:** ACCEPTED | **Affects:** tokens-{web,app}.css, components-{web,app}.css

## The Question

Should we unify `tokens-web.css` + `tokens-app.css` into a single `tokens-shared.css` with platform-specific overrides?

## Decision

**Keep separate.** Do not consolidate.

**Why:** Web (editorial/marketing) and app (SaaS/dashboard) are fundamentally different design systems, not variants of one system. Unifying them creates compromise instead of excellence in either context.

### Evidence (Full Audit)

## Key Differences (Web vs. App)

| Aspect | Web (Editorial) | App (SaaS) | % CSS Divergence |
|--------|---|---|---|
| **Type Scale** | Fluid clamp() 0.65–10rem | Static 0.625–3.75rem | 100% |
| **Body Size** | 1rem (16px) | 0.875rem (14px) | Different |
| **Gap (components)** | 1.5rem (generous) | 1rem (compact) | 60% of all CSS |
| **Accent Color** | black (`--gray-900`) | brand-blue (`oklch(0.50...)`) | Different |
| **Color Semantics** | Tuned for light default | Tuned for dark default | Different |
| **Button Style** | Flat | Tactile + elevated | Different |
| **Backdrop** | Blur (modal) | Absent (performance) | Different |
| **Spacing Tokens** | Space-4: 1rem | Space-4: 1rem (but gaps differ) | Context-dependent |

**Total code divergence:** 60% of components-*.css is genuinely different (2163 of 3591 lines).

## Why Not Consolidate?

If we created a "shared" file:

```css
/* ❌ Result: Unreadable, fragile, hard to optimize */
--gap-component: var(--gap-web, var(--gap-app, 1.25rem));
--button-padding: var(--space-4-web, var(--space-4-app, 1rem));
/* ... 50+ conditional tokens ... */
```

**Cost-Benefit Analysis:**
- **Savings:** ~1000 lines (duplicated selectors)
- **Cost:** Conditional logic, harder debugging, slower parsing, brittle maintenance
- **Verdict:** Negative ROI. **Separation is the right call.**

## Governance

See `docs/visual/tokens/TOKEN-CONSISTENCY.md` for:
- 153 shared token names (must exist in both)
- 30+ platform-exclusive tokens (documented)
- Checklist for token changes
- CI validation strategy

## Tradeoffs

| What You Get | What You Give Up |
|---|---|
| ✅ Best-in-class design for each platform | ⚠️ Token changes must sync across both files |
| ✅ No forced compromises (airy or cramped?) | ⚠️ Coordination needed for shared names |
| ✅ Independent evolution if needed | ⚠️ 55% code duplication (inevitable) |
| ✅ Clear contracts for implementers | — |

**Maintenance Cost:** Low. Token consistency is validated in CI. See TOKEN-CONSISTENCY.md.

## Revisit If

- Token count exceeds 300 (reconsider tooling, not consolidation)
- Native iOS/Android platform added (unification becomes critical)
- Token Studio integration becomes standard (tooling can abstract the split)
