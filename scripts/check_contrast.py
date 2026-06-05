#!/usr/bin/env python3
"""Assert Nordover's semantic colour pairs meet WCAG 2 AA — contrast by construction.

This turns the hand-tuned OKLCH ramp's contrast from "trust the calibration" into
an automated build-time assertion (benchmark roadmap C2). It parses the canonical
`--gray-*` ramp and the light- and dark-mode semantic assignments from
tokens-web.css, converts OKLCH → linear sRGB → WCAG relative luminance (Ottosson's
OKLab matrices), and checks each foreground/background pair against its threshold.

Usage:  python3 scripts/check_contrast.py          # report all pairs
        python3 scripts/check_contrast.py --strict  # exit 1 if any AA pair fails

CSS stays the single source of truth; this only reads it.
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "docs" / "visual" / "tokens" / "tokens-web.css"

# Pairs to assert: (label, fg-token, bg-token, min_ratio). 4.5 = AA body text, 3.0 = AA large/UI.
# Status BASE hues are for icons/badges/borders/large text (3:1); body text on tints uses
# the `-strong` variants (color-mix, resolved at runtime, so not statically asserted here).
PAIRS = [
    ("body text (fg / bg)",         "--color-fg",        "--color-bg",      4.5),
    ("muted text (muted / bg)",     "--color-muted",     "--color-bg",      4.5),
    ("accent label (accent-fg / accent)", "--color-accent-fg", "--color-accent", 4.5),
    ("error UI/icon (error / bg)",  "--error",           "--color-bg",      3.0),
    ("success UI/icon (success / bg)", "--success",      "--color-bg",      3.0),
    ("info UI/icon (info / bg)",    "--info",            "--color-bg",      3.0),
]


def parse_oklch(s: str, base: dict[str, str] | None = None) -> tuple[float, float, float] | None:
    """Parse oklch(L C H); substitute --neutral-c/--neutral-h refs from `base`."""
    if base:
        for var in ("--neutral-c", "--neutral-h"):
            if var in base:
                s = s.replace(f"var({var})", base[var].strip())
    m = re.search(r"oklch\(\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)", s)
    if not m:
        return None
    return float(m.group(1)), float(m.group(2)), float(m.group(3))


def load_block(text: str, selector: str) -> dict[str, str]:
    """Return {token: raw-value} for the given selector's first block."""
    start = text.index(selector)
    depth, i, body_start = 0, text.index("{", start), 0
    for i in range(text.index("{", start), len(text)):
        if text[i] == "{":
            if depth == 0:
                body_start = i + 1
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                body = text[body_start:i]
                break
    out = {}
    for name, val in re.findall(r"(--[\w-]+)\s*:\s*([^;]+);", body):
        out[name] = val.strip()
    return out


def resolve(token: str, scope: dict[str, str], base: dict[str, str]) -> tuple[float, float, float] | None:
    """Resolve a token to OKLCH, following one level of var() + the gray ramp."""
    val = scope.get(token) or base.get(token)
    if val is None:
        return None
    ref = re.match(r"var\((--[\w-]+)\)", val)
    if ref:
        name = ref.group(1)
        raw = base.get(name) or scope.get(name)
        return parse_oklch(raw, base) if raw else None
    return parse_oklch(val, base)


def oklch_to_linear_srgb(L: float, C: float, H: float) -> tuple[float, float, float]:
    a = C * math.cos(math.radians(H))
    b = C * math.sin(math.radians(H))
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    bb = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
    return tuple(min(1.0, max(0.0, x)) for x in (r, g, bb))


def luminance(oklch: tuple[float, float, float]) -> float:
    r, g, b = oklch_to_linear_srgb(*oklch)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg: tuple, bg: tuple) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def check(mode: str, scope: dict, base: dict) -> list[tuple]:
    rows = []
    for label, fg_t, bg_t, threshold in PAIRS:
        fg, bg = resolve(fg_t, scope, base), resolve(bg_t, scope, base)
        if not fg or not bg:
            rows.append((mode, label, None, threshold, "skip (color-mix/unresolved)"))
            continue
        r = ratio(fg, bg)
        ok = r >= threshold
        rows.append((mode, label, r, threshold, "PASS" if ok else "FAIL"))
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="exit 1 on any AA failure")
    args = ap.parse_args()

    text = TOKENS.read_text()
    base = load_block(text, ":root {")
    dark = load_block(text, ":root:has(#dark:checked)")

    rows = check("light", {}, base) + check("dark", dark, base)
    failed = False
    print(f"{'mode':6} {'pair':36} {'ratio':>7}  {'min':>4}  result")
    print("-" * 70)
    for mode, label, r, thr, result in rows:
        rs = f"{r:5.2f}:1" if r is not None else "   -  "
        print(f"{mode:6} {label:36} {rs:>7}  {thr:>4}  {result}")
        if result == "FAIL":
            failed = True

    if failed and args.strict:
        print("\nFAIL: one or more AA pairs below threshold", file=sys.stderr)
        sys.exit(1)
    print("\nNote: pairs using color-mix()/derived values are skipped (need a CSS runtime).")


if __name__ == "__main__":
    main()
