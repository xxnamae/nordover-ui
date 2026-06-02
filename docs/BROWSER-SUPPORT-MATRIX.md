# Nordover Browser Support Matrix

**Framework Version:** 1.2.0  
**Last Updated:** 2026-06-02  
**Support Status:** Chrome/Safari/Firefox modern versions (past 2 years)

---

## Core Features & Browser Support

| Feature | Chrome | Safari | Firefox | Edge | Status |
|---------|--------|--------|---------|------|--------|
| **CSS @layer** | 99+ | 15.4+ | 97+ | 99+ | ✅ Full Support |
| **CSS `:has()` selector** | 105+ | 15.4+ | 121+ | 105+ | ✅ Full Support |
| **OKLCH color space** | 111+ | 15.4+ | 113+ | 111+ | ⚠️ Requires Fallback |
| **`color-mix()` function** | 111+ | 15.4+ | 113+ | 111+ | ⚠️ Requires Fallback |
| **CSS Grid** | 57+ | 10.1+ | 52+ | 16+ | ✅ Full Support |
| **Flexbox** | 29+ | 9+ | 22+ | 11+ | ✅ Full Support |
| **CSS Custom Properties** | 49+ | 9.1+ | 31+ | 15+ | ✅ Full Support |
| **`:focus-visible`** | 86+ | 15.1+ | 4+ | 86+ | ✅ Full Support |

---

## Minimum Requirements

### For Full Feature Compatibility

- **Chrome:** 111+
- **Safari:** 15.4+
- **Firefox:** 113+
- **Edge:** 111+

### For Graceful Degradation (2020+ Browsers)

- **Chrome:** 99+
- **Safari:** 15.4+
- **Firefox:** 97+
- **Edge:** 99+

---

## Fallback Strategy

### OKLCH Color Space (Safari <15.4, Chrome <111, Firefox <113)

Nordover uses OKLCH as the primary color space for perceptual consistency. For browsers that don't support OKLCH, we use **CSS cascade fallbacks**:

```css
/* Fallback: uses RGB or earlier color space */
background: rgba(245, 245, 245, 1);

/* Modern: OKLCH with color-mix */
background: color-mix(in oklch, var(--color-accent) 10%, var(--color-subtle));
```

Browsers that support `color-mix()` will use the second declaration; older browsers fall back to RGB.

### Components Requiring Fallbacks

1. **Button Hover States** (`.btn-secondary:hover`, `.btn-elevated:hover`)
   - Uses `color-mix()` for accent blending
   - Fallback: Solid theme color

2. **Form Input States** (`.form-input.is-error`, `.form-input.is-success`)
   - Uses `color-mix()` for tinted backgrounds
   - Fallback: Solid semantic color background

3. **Focus Ring** (`:focus-visible`)
   - Uses OKLCH `oklch(0.50 0.28 260)`
   - Fallback: Standard blue (`rgb(59, 130, 246)`)

4. **Table & List Hover** (`.table tr:hover`, `.data-table tr:hover`)
   - Uses `color-mix()` for subtle background
   - Fallback: Transparent or very light gray

---

## Implementation Notes

### For Consumers

If you need to support older browsers:

1. **Add RGB fallbacks in your brand CSS layer:**
   ```css
   @layer brand {
     :root {
       /* Fallback: OKLCH unsupported */
       --color-accent-light-fallback: rgb(240, 245, 250);
       --color-accent: oklch(0.50 0.28 260); /* OKLCH modern */
     }
   }
   ```

2. **Test on target browsers:** Use BrowserStack or similar for verification

3. **Monitor real user usage:** Check your analytics for browser distribution

### For Maintainers

When adding new `color-mix()` declarations:

1. Add RGB fallback above the color-mix line
2. Document the original OKLCH values in a comment
3. Update this matrix if new color-mix patterns emerge

---

## Known Limitations

| Browser | Limitation | Workaround |
|---------|-----------|-----------|
| **Safari <15.4** | No OKLCH, `color-mix`, or `:has()` | Framework unavailable; use v2.x |
| **Firefox <113** | No OKLCH or `color-mix()` | RGB fallbacks sufficient |
| **Edge <111** | No OKLCH or `color-mix()` | RGB fallbacks sufficient |
| **IE 11** | No CSS Grid, `:has()`, @layer | Not supported (EOL: 10/2025) |

---

## Testing Checklist

Before shipping to production, verify:

- [ ] Buttons render readable in light & dark modes (all browsers)
- [ ] Form error/success states visible in unsupported browsers
- [ ] Focus indicators visible (`:focus-visible` works or fallback)
- [ ] Tables/lists readable on hover
- [ ] No console errors from unsupported CSS

---

## Release Cadence

This matrix is updated every major version or when adding new features that require specific browser versions.

**Last Audit:** 2026-06-01  
**Next Review:** v3.1 (2026-Q3)
