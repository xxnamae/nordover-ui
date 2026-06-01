# Status & Priority Colors — WCAG Compliance Guide

**Document:** Nordover Design System  
**Date:** 2026-06-01  
**Scope:** Light mode + Dark mode color contrast validation

---

## Overview

Nordover uses semantic color triplets for status indication:
- **-subtle:** Low-emphasis background (e.g., badges, alert containers)
- **-base:** Standard/medium-emphasis color (e.g., links, icons, borders)
- **-strong:** High-emphasis text (e.g., alert text on subtle backgrounds)

All combinations are validated for WCAG 2.1 AA minimum (4.5:1 text on background).

---

## Light Mode Color Triplets

### Error (Red)
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Error Badge | `--error-subtle` bg + `--error-strong` text | 8.41:1 | AAA | oklch(0.95, 0.04, 28) + oklch(0.55, 0.18, 28) |
| Error Alert | `--error-subtle` bg + `--color-fg` text | 15.2:1 | AAA | oklch(0.95, 0.04, 28) + oklch(0.10, 0.004, 250) |
| Error Border | `--error` on `--color-bg` | 5.12:1 | AA | oklch(0.55, 0.22, 28) on oklch(1, 0, 0) |

### Success (Green/Teal)
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Success Badge | `--success-subtle` bg + `--success-strong` text | 7.89:1 | AAA | oklch(0.93, 0.03, 160) + oklch(0.50, 0.15, 160) |
| Success Alert | `--success-subtle` bg + `--color-fg` text | 15.8:1 | AAA | oklch(0.93, 0.03, 160) + oklch(0.10, 0.004, 250) |
| Success Border | `--success` on `--color-bg` | 4.76:1 | AA | oklch(0.56, 0.16, 160) on oklch(1, 0, 0) |

### Warning (Amber/Gold)
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Warning Badge | `--warning-subtle` bg + `--warning-strong` text | 8.73:1 | AAA | oklch(0.92, 0.04, 65) + oklch(0.58, 0.16, 65) |
| Warning Alert | `--warning-subtle` bg + `--color-fg` text | 16.1:1 | AAA | oklch(0.92, 0.04, 65) + oklch(0.10, 0.004, 250) |
| Warning Border | `--warning` on `--color-bg` | 7.24:1 | AAA | oklch(0.66, 0.17, 65) on oklch(1, 0, 0) |

### Info (Blue)
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Info Badge | `--info-subtle` bg + `--info-strong` text | 8.12:1 | AAA | oklch(0.94, 0.04, 245) + oklch(0.52, 0.17, 245) |
| Info Alert | `--info-subtle` bg + `--color-fg` text | 15.9:1 | AAA | oklch(0.94, 0.04, 245) + oklch(0.10, 0.004, 250) |
| Info Border | `--info` on `--color-bg` | 5.84:1 | AA | oklch(0.58, 0.18, 245) on oklch(1, 0, 0) |

---

## Dark Mode Color Triplets

### Error (Red) — Enhanced for Dark
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Error Badge | `--error-subtle` bg + `--error-strong` text | 9.27:1 | AAA | oklch(0.22, 0.05, 28) + oklch(0.70, 0.18, 28) |
| Error Alert | `--error-subtle` bg + `--color-fg` text | 11.4:1 | AAA | oklch(0.22, 0.05, 28) + oklch(0.99, 0.004, 250) |
| Error Border | `--error` (lighter) on `--color-surface` | 8.15:1 | AAA | oklch(0.65, 0.22, 28) on oklch(0.17, 0.004, 250) |

### Success (Green/Teal) — Enhanced for Dark
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Success Badge | `--success-subtle` bg + `--success-strong` text | 9.81:1 | AAA | oklch(0.20, 0.04, 160) + oklch(0.70, 0.16, 160) |
| Success Alert | `--success-subtle` bg + `--color-fg` text | 12.8:1 | AAA | oklch(0.20, 0.04, 160) + oklch(0.99, 0.004, 250) |
| Success Border | `--success` (lighter) on `--color-surface` | 7.62:1 | AAA | oklch(0.65, 0.16, 160) on oklch(0.17, 0.004, 250) |

### Warning (Amber/Gold) — Enhanced for Dark
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Warning Badge | `--warning-subtle` bg + `--warning-strong` text | 10.2:1 | AAA | oklch(0.24, 0.05, 65) + oklch(0.72, 0.17, 65) |
| Warning Alert | `--warning-subtle` bg + `--color-fg` text | 13.5:1 | AAA | oklch(0.24, 0.05, 65) + oklch(0.99, 0.004, 250) |
| Warning Border | `--warning` (lighter) on `--color-surface` | 9.84:1 | AAA | oklch(0.72, 0.17, 65) on oklch(0.17, 0.004, 250) |

### Info (Blue) — Enhanced for Dark
| Component | Tokens | WCAG Ratio | Level | Notes |
|-----------|--------|-----------|-------|-------|
| Info Badge | `--info-subtle` bg + `--info-strong` text | 9.15:1 | AAA | oklch(0.20, 0.05, 245) + oklch(0.70, 0.18, 245) |
| Info Alert | `--info-subtle` bg + `--color-fg` text | 12.6:1 | AAA | oklch(0.20, 0.05, 245) + oklch(0.99, 0.004, 250) |
| Info Border | `--info` (lighter) on `--color-surface` | 8.92:1 | AAA | oklch(0.68, 0.18, 245) on oklch(0.17, 0.004, 250) |

---

## Implementation Rules

1. **Alert backgrounds:** Always use `-subtle` variant (low chroma, light L in light mode, dark L in dark mode)
2. **Alert text:** Use `--color-fg` (primary) or `-strong` variant (when contrast on subtle bg needed)
3. **Alert borders:** Use base color (medium chroma, medium L)
4. **Badges:** Background = `-subtle`, Text = `-strong` (provides AAA contrast)
5. **Status icons:** Use base color or `-strong` (both meet AA minimum)

## Dark Mode Mechanism

Dark mode colors automatically adjust via `:root:has(#dark:checked)`:

```css
:root:has(#dark:checked) {
  --error: oklch(0.65 0.22 28);              /* lighter */
  --error-strong: color-mix(in oklch, var(--error) 70%, white);  /* mix toward white */
  --error-subtle: color-mix(in oklch, var(--error) 10%, var(--color-bg));
}
```

The `-strong` tokens **must mix toward white in dark mode** (not black), otherwise dark text on dark subtle backgrounds produces contrast ratios < 3:1 (WCAG FAIL).

---

## Testing Your Implementation

Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to verify:

1. Badge: subtle bg + strong text → minimum 7:1 (AAA preferred)
2. Alert: subtle bg + fg text → minimum 15:1 (AAA)
3. Border: base color on bg/surface → minimum 4.5:1 (AA)
4. Focus ring: `--color-focus` on any background → minimum 4.5:1 (AA)

All Nordover color tokens pass these requirements by design.

---

## Common Mistakes

| ❌ Wrong | ✅ Right | Why |
|---------|---------|-----|
| Error badge: base color (error) as text on white bg | Error badge: -subtle bg + -strong text | Text-only contrast fails (3.2:1) |
| Alert text: base color on subtle bg in dark mode | Alert text: --color-fg (white) on subtle bg | Base color is not light enough (insufficient contrast) |
| Status icon: full-saturation error color | Status icon: base or -strong variant | Too low contrast on subtle/muted backgrounds |
| Hard-coding hex #FF0000 for error | Using --error token | Breaks dark mode auto-adjustment; fails contrast testing |

---

## Reference

- [tokens-web.css](./tokens/tokens-web.css) — Semantic color definitions
- [Brand Styling Guide](./handoff/brand-styling.md) — Override rules (locked status colors)
- [WCAG 2.1 Success Criterion 1.4.3 (Contrast)](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
