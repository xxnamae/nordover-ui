# ADR — Motion-token Platform Divergence (Web ≠ App)

**Date:** 2026-06-01  
**Status:** Accepted  
**Authors:** Nordover Team  
**Deciders:** Design system stewards

## Context

Motion tokens (--duration-fast, --duration-base, --duration-slower) exist in two variants:
- **tokens-web.css** — Desktop web (longer durations for editorial fluidity)
- **tokens-app.css** — Mobile app (shorter durations for responsiveness)

Current values:

| Token | Web | App | Ratio |
|-------|-----|-----|-------|
| --duration-fast | 150ms | 100ms | 1.5× |
| --duration-base | 250ms | 150ms | 1.67× |
| --duration-slower | 600ms | 400ms | 1.5× |

The divergence is **intentional and aligned with platform best practices**:
- **Web (desktop):** Longer durations = editorial polish, fluid micro-interactions, marketing credibility
- **App (mobile):** Shorter durations = perceived responsiveness, touch feedback, battery efficiency

## Decision

**Keep motion-token values intentionally divergent per platform.**

Web and app serve different user expectations:
1. **Desktop/editorial site visitor** → expects polish, trusts slower transitions
2. **Mobile app user** → expects snappy feedback, perceives slow transitions as lag

Synchronizing both to one duration would degrade UX on one or both platforms.

## Rationale

1. **Platform conventions differ:** iOS (HIG) and Material Design (Android) use fundamentally different motion timings for the same action types
2. **Network latency:** Mobile networks are slower; longer transitions mask perceived lag on web better
3. **Touch feedback:** Haptic + visual feedback requires faster confirmation on mobile
4. **User expectations:** Editorial site visitors and app users have different scrolling/interaction speeds

## Consequences

- **Pro:** Optimal UX on each platform; aligns with industry standards
- **Con:** Developers must understand two token namespaces; no single "system duration"
- **Migration:** Implementors using Nordover must select either tokens-web.css or tokens-app.css, not both

## Implementation Notes

- `components-web.css` uses `var(--duration-base)` → resolves to 250ms
- `components-app.css` uses `var(--duration-base)` → resolves to 150ms
- Both files are correct; no sync required
- Documentation (brand-styling.md, handoff/) must clarify that duration values are platform-specific

## See Also

- [Brand Styling Guide](../../handoff/brand-styling.md) — mentions motion-token stability
- tokens-web.css:L220-222
- tokens-app.css:L187-189
