#!/usr/bin/env python3
"""Generate a Nordover semantic theme from three inputs (Linear-grade).

Mirrors Linear's "whole theme from base + accent + contrast" model, adapted to
Nordover's OKLCH single-L-axis architecture. Given a neutral hue/chroma, an
accent colour, and a contrast level, this emits a ready-to-paste `:root` (light)
and `:root:has(#dark:checked)` (dark) block that is drop-in compatible with
tokens-web.css / tokens-app.css — so spinning up a new branded project becomes a
token swap, not a redesign.

The neutral ramp is generated on a perceptually-even L-axis (OKLCH), the same
principle the hand-tuned ramp in tokens-*.css follows. The `contrast` knob widens
or narrows the L-spread between background and foreground, which is exactly how
Linear exposes accessibility as a first-class generation input.

Usage:
  python3 scripts/generate_theme.py \
      --accent "oklch(0.55 0.20 260)" --hue 250 --chroma 0.004 --contrast normal
  python3 scripts/generate_theme.py --accent "oklch(0.62 0.17 150)" --contrast high

Output goes to stdout. Pipe it into a project's theme file; it never edits the
canonical tokens (CSS stays the single source of truth).
"""
from __future__ import annotations

import argparse
import re
import sys

# Perceptually-even L stops for the neutral ramp at "normal" contrast.
# These match the hand-tuned ladder in tokens-*.css (gray-50 .. gray-950).
BASE_L = {
    50: 0.985, 100: 0.96, 200: 0.92, 300: 0.865, 400: 0.70,
    500: 0.52, 600: 0.435, 700: 0.33, 800: 0.22, 900: 0.13, 950: 0.08,
}

# Contrast presets scale how far each stop is pushed away from mid (L 0.5).
# >1 = more contrast (darks darker, lights lighter); <1 = softer/calmer.
CONTRAST = {"low": 0.88, "normal": 1.0, "high": 1.08}

MID = 0.5


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def scale_l(l: float, factor: float) -> float:
    """Push lightness away from (or toward) mid by `factor`, then clamp."""
    return round(clamp(MID + (l - MID) * factor), 4)


def parse_accent(s: str) -> tuple[float, float, float]:
    m = re.search(r"oklch\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)", s)
    if not m:
        sys.exit(f"error: --accent must be oklch(L C H), got: {s!r}")
    return float(m.group(1)), float(m.group(2)), float(m.group(3))


def build(accent: str, hue: float, chroma: float, contrast: str) -> str:
    factor = CONTRAST[contrast]
    al, ac, ah = parse_accent(accent)
    ramp = {k: scale_l(v, factor) for k, v in BASE_L.items()}

    def gray(stop: int) -> str:
        return f"oklch({ramp[stop]} {chroma} {hue})"

    # Accent foreground: pick near-white or near-black by accent lightness.
    accent_fg = gray(50) if al < 0.6 else gray(950)
    dark_accent_fg = gray(950) if al < 0.6 else gray(50)

    out: list[str] = []
    out.append("/* === Generated theme (scripts/generate_theme.py) ===")
    out.append(f"   accent={accent} · neutral-h={hue} · neutral-c={chroma}")
    out.append(f"   contrast={contrast} (L-factor {factor}). Drop into a project")
    out.append("   theme file; never hand-edit the canonical tokens. */")
    out.append(":root {")
    out.append(f"  --neutral-h: {hue}; --neutral-c: {chroma};")
    for stop in BASE_L:
        out.append(f"  --gray-{stop}: {gray(stop)};")
    out.append("")
    out.append("  /* Semantic (light) */")
    out.append("  --color-bg: oklch(1 0 0);")
    out.append("  --color-surface: oklch(1 0 0);")
    out.append("  --color-fg: var(--gray-900);")
    out.append("  --color-muted: var(--gray-500);")
    out.append("  --color-subtle: var(--gray-100);")
    out.append("  --color-border: var(--gray-200);")
    out.append(f"  --color-accent: {accent};")
    out.append(f"  --color-accent-fg: {accent_fg};")
    out.append("  --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, white);")
    out.append("  --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, white);")
    focus_l = round(clamp(al + 0.02, 0, 0.7), 3)
    focus_c = round(min(ac + 0.08, 0.3), 3)
    out.append(f"  --color-focus: oklch({focus_l} {focus_c} {ah:g});")
    out.append("}")
    out.append("")
    out.append(":root:has(#dark:checked) {")
    out.append("  --color-bg: var(--gray-950);")
    out.append("  --color-surface: var(--gray-900);")
    out.append("  --color-fg: var(--gray-50);")
    out.append("  --color-muted: var(--gray-400);")
    out.append("  --color-subtle: var(--gray-800);")
    out.append("  --color-border: var(--gray-700);")
    # In dark, lift accent lightness for contrast against near-black.
    out.append(f"  --color-accent: oklch({round(clamp(al + 0.12, 0, 0.92), 3)} {ac:g} {ah:g});")
    out.append(f"  --color-accent-fg: {dark_accent_fg};")
    out.append("  --color-accent-hover: color-mix(in oklch, var(--color-accent) 85%, black);")
    out.append("  --color-accent-active: color-mix(in oklch, var(--color-accent) 70%, black);")
    out.append("}")
    out.append("")
    # Lightweight, honest contrast note (WCAG 2 + APCA direction).
    fg_l = ramp[900]
    out.append(f"/* fg L={fg_l} on bg L=1.0 → high contrast (AA/AAA body). "
               "Verify accent pairs against APCA Lc>=75 for body text. */")
    return "\n".join(out)


def main() -> None:
    p = argparse.ArgumentParser(description="Generate a Nordover theme from 3 inputs.")
    p.add_argument("--accent", required=True, help="accent colour as oklch(L C H)")
    p.add_argument("--hue", type=float, default=250, help="neutral hue (default 250)")
    p.add_argument("--chroma", type=float, default=0.004, help="neutral chroma (default 0.004)")
    p.add_argument("--contrast", choices=CONTRAST, default="normal", help="contrast level")
    args = p.parse_args()
    print(build(args.accent, args.hue, args.chroma, args.contrast))


if __name__ == "__main__":
    main()
