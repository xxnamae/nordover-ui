#!/usr/bin/env python3
"""Guard the semantic typography contract in components-*.css.

Checks the CANONICAL (non-@media) `.t-*` rules in each package:
  1. Each `.t-*` class is defined at most once outside @media blocks
     (a second, hard-coded definition silently wins the cascade — the
     `.t-eyebrow` bug this guard was written for).
  2. `font-weight` in those rules is a `var(--fw-*)` token, never a raw
     numeric literal.

@media responsive overrides are intentionally OUT of scope: they may
re-tune size/weight per breakpoint. The contract surface consumers
depend on is the base definition. `letter-spacing` is likewise not
checked — display classes carry legitimate per-size optical tracking
literals (-0.02em … -0.04em) for which no token exists.

Run: python3 scripts/check_components.py
Exit non-zero on any violation (wire into CI alongside check:tokens).
"""
import re
import sys
import pathlib

FILES = [
    "docs/visual/components/components-app.css",
    "docs/visual/components/components-web.css",
]


def strip_media(css: str) -> str:
    """Return css with every brace-balanced @media { … } block removed."""
    out, i, n = [], 0, len(css)
    media = re.compile(r'@media[^{]*\{')
    while i < n:
        m = media.match(css, i)
        if m:
            depth, j = 1, m.end()
            while j < n and depth:
                depth += (css[j] == '{') - (css[j] == '}')
                j += 1
            i = j
        else:
            out.append(css[i])
            i += 1
    return ''.join(out)


def check(path: str) -> list[str]:
    errors: list[str] = []
    css = pathlib.Path(path).read_text()
    base = strip_media(css)
    rule = re.compile(r'(\.t-(?:display|heading|body|eyebrow|caption)[a-z0-9-]*)\s*\{([^{}]*)\}')
    seen: dict[str, list[str]] = {}
    for m in rule.finditer(base):
        seen.setdefault(m.group(1), []).append(m.group(2))
    for cls, bodies in sorted(seen.items()):
        if len(bodies) > 1:
            errors.append(
                f"{path}: '{cls}' defined {len(bodies)}x outside @media "
                f"(duplicate canonical selector — one wins the cascade)"
            )
        for body in bodies:
            fw = re.search(r'font-weight:\s*([^;]+);', body)
            if fw and not fw.group(1).strip().startswith('var('):
                errors.append(
                    f"{path}: '{cls}' hard-codes font-weight: "
                    f"{fw.group(1).strip()} (use a var(--fw-*) token)"
                )
    return errors


def main() -> None:
    errors: list[str] = []
    for f in FILES:
        errors += check(f)
    if errors:
        print("✗ component typography contract violations:")
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("ok: component typography contract "
          "(.t-* canonical defs unique + token font-weight)")


if __name__ == "__main__":
    main()
