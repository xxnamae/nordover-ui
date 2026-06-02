#!/usr/bin/env python3
"""Build W3C DTCG token JSON from the canonical Nordover CSS token files.

The CSS files (docs/visual/tokens/tokens-{web,app}.css) remain the single
source of truth. This generator parses the `:root` token block (light/base)
and the `:root:has(#dark:checked)` block (dark overrides) and emits one DTCG
JSON file per package, mirroring the CSS 1:1.

Design (see ADR docs/wiki/decisions/0008-json-token-export.md):
  - Primitives get real DTCG types: color (oklch object), dimension, duration,
    cubicBezier, fontWeight (number), number.
  - Pure aliases (`var(--x)`) become DTCG references: `{group.token}`.
  - Computed/derived values that have no clean DTCG form (color-mix(), clamp(),
    gradients, glass, multi-prop borders, multi-layer shadows) are preserved
    losslessly: `$value` carries the raw CSS string and
    `$extensions["com.nordover.cssText"] = true` flags that a CSS runtime is
    required. This keeps the export honest and reversible.
  - Dark-mode overrides live on each affected token under
    `$extensions["com.nordover.dark"]` so every package stays a single file.

Usage:  python3 scripts/build_tokens.py          # writes JSON next to the CSS
        python3 scripts/build_tokens.py --check   # verify JSON is up to date
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS_DIR = ROOT / "docs" / "visual" / "tokens"
PACKAGES = ["web", "app"]

EXT = "com.nordover"  # extension namespace


# ---------------------------------------------------------------------------
# CSS parsing
# ---------------------------------------------------------------------------
def _match_block(css: str, start: int) -> tuple[str, int]:
    """Return the `{...}` body starting at the first `{` at/after `start`."""
    open_idx = css.index("{", start)
    depth = 0
    for i in range(open_idx, len(css)):
        c = css[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return css[open_idx + 1 : i], i
    raise ValueError("unbalanced braces")


def _declarations(body: str) -> list[tuple[str, str]]:
    """Extract `--name: value` pairs from a CSS rule body, in source order.

    Nested rules and comments are stripped; values never contain `;` here so a
    top-level split on `;` is safe for this codebase.
    """
    # drop /* ... */ comments
    body = re.sub(r"/\*.*?\*/", "", body, flags=re.DOTALL)
    decls: list[tuple[str, str]] = []
    for chunk in body.split(";"):
        chunk = chunk.strip()
        if not chunk.startswith("--"):
            continue
        name, _, value = chunk.partition(":")
        name = name.strip()[2:]  # drop leading --
        value = " ".join(value.split())  # collapse whitespace/newlines
        if name and value:
            decls.append((name, value))
    return decls


def parse_css(path: Path) -> tuple[list[tuple[str, str]], dict[str, str]]:
    """Return (light decls in order, dark overrides by name)."""
    css = path.read_text(encoding="utf-8")

    # Light/base block: the `:root {` inside `@layer tokens`.
    layer_idx = css.index("@layer tokens {")
    root_idx = css.index(":root", layer_idx)
    light_body, _ = _match_block(css, root_idx)
    light = _declarations(light_body)

    # Dark block: `:root:has(#dark:checked) {`.
    dark: dict[str, str] = {}
    dm = re.search(r":root:has\(#dark:checked\)", css)
    if dm:
        dark_body, _ = _match_block(css, dm.start())
        dark = dict(_declarations(dark_body))
    return light, dark


# ---------------------------------------------------------------------------
# Value typing
# ---------------------------------------------------------------------------
NUM = r"-?\d+(?:\.\d+)?"


def _resolve_numeric_vars(light: list[tuple[str, str]]) -> dict[str, str]:
    """Plain numeric custom props (e.g. --neutral-h: 250) for substitution."""
    out = {}
    for name, value in light:
        if re.fullmatch(NUM, value):
            out[name] = value
    return out


def alias_path(var_name: str, group_of) -> str:
    """DTCG reference path `{group.subgroup.leaf}` for a `var(--x)` target."""
    group, leaf = group_of(var_name)
    parts = group + [leaf]
    return "{" + ".".join(parts) + "}"


def type_value(name: str, value: str, numeric_vars: dict[str, str], group_of):
    """Return (dtcg_type or None, dtcg_value, is_raw_css)."""
    v = value.strip()

    # Reference / alias
    m = re.fullmatch(r"var\(--([a-z0-9-]+)\)", v)
    if m:
        return (None, alias_path(m.group(1), group_of), False)

    # cubic-bezier easing
    m = re.fullmatch(r"cubic-bezier\(\s*([^)]+)\)", v)
    if m:
        nums = [float(x) for x in m.group(1).split(",")]
        return ("cubicBezier", nums, False)

    # duration (ms)
    m = re.fullmatch(rf"({NUM})ms", v)
    if m:
        return ("duration", {"value": float(m.group(1)), "unit": "ms"}, False)

    # pure number (font-weights, z-index, line-heights, neutral-h/c)
    if re.fullmatch(NUM, v):
        num = float(v) if "." in v else int(v)
        return ("number", num, False)

    # single dimension
    m = re.fullmatch(rf"({NUM})(rem|px|em|ch|vw|vh)", v)
    if m:
        unit = m.group(2)
        return ("dimension", {"value": float(m.group(1)), "unit": unit}, False)

    # literal oklch color (substitute numeric vars like --neutral-c/-h)
    if v.startswith("oklch(") and v.endswith(")"):
        inner = v[len("oklch(") : -1]
        inner = re.sub(
            r"var\(--([a-z0-9-]+)\)",
            lambda mm: numeric_vars.get(mm.group(1), mm.group(0)),
            inner,
        )
        # split off optional "/ alpha"
        alpha = None
        if "/" in inner:
            inner, _, a = inner.partition("/")
            a = a.strip()
            if re.fullmatch(NUM, a):
                alpha = float(a)
        parts = inner.split()
        if len(parts) >= 3 and all(re.fullmatch(NUM, p) for p in parts[:3]):
            comps = [float(p) for p in parts[:3]]
            color = {"colorSpace": "oklch", "components": comps}
            if alpha is not None:
                color["alpha"] = alpha
            return ("color", color, False)

    # Everything else: preserve raw CSS losslessly.
    return (_raw_type_hint(name), v, True)


def _raw_type_hint(name: str) -> str:
    """Closest standard $type hint for a raw-CSS token (color-mix/clamp/etc)."""
    if name.startswith(("color", "gray", "chart", "error", "success", "warning", "info")):
        return "color"
    if name.startswith("shadow"):
        return "shadow"
    if name.startswith(("gradient", "glass")):
        return "gradient"
    if name.startswith("text"):
        return "dimension"
    if name.startswith(("border", "bw")):
        return "border"
    return "other"


# ---------------------------------------------------------------------------
# Grouping
# ---------------------------------------------------------------------------
# Ordered (regex, group-path, leaf-builder). First match wins.
def group_of(name: str) -> tuple[list[str], str]:
    """Map a token name to (group path list, leaf name)."""
    rules = [
        (r"neutral-(.+)", ["color", "neutral"], lambda m: m.group(1)),
        (r"gray-(.+)", ["color", "gray"], lambda m: m.group(1)),
        (r"chart-(.+)", ["color", "chart"], lambda m: m.group(1)),
        (r"(error|success|warning|info)(?:-(.+))?$", ["color"],
         lambda m: m.group(1) + ("-" + m.group(2) if m.group(2) else "")),
        # Backwards-compat aliases (--color-error -> --error) get their own
        # subgroup so they don't collide with the canonical --error primitive.
        (r"color-(error|success|warning|info)", ["color", "alias"],
         lambda m: m.group(1)),
        (r"color-(.+)", ["color"], lambda m: m.group(1)),
        (r"font-(.+)", ["font", "family"], lambda m: m.group(1)),
        (r"text-(.+)", ["font", "size"], lambda m: m.group(1)),
        (r"fw-(.+)", ["font", "weight"], lambda m: m.group(1)),
        (r"leading-(.+)", ["font", "lineHeight"], lambda m: m.group(1)),
        (r"tracking-(.+)", ["font", "letterSpacing"], lambda m: m.group(1)),
        (r"space-(.+)", ["space"], lambda m: m.group(1)),
        (r"(gap-.+|spacing-section|page-padding)", ["space", "semantic"],
         lambda m: m.group(1)),
        (r"radius-(.+)", ["radius"], lambda m: m.group(1)),
        (r"(bw-.+|border-.+)", ["border"], lambda m: m.group(1)),
        (r"shadow-(.+)", ["shadow"], lambda m: m.group(1)),
        (r"size-(.+)", ["size", "icon"], lambda m: m.group(1)),
        (r"z-(.+)", ["zIndex"], lambda m: m.group(1)),
        (r"duration-(.+)", ["motion", "duration"], lambda m: m.group(1)),
        (r"ease-(.+)", ["motion", "easing"], lambda m: m.group(1)),
        (r"lift-(.+)", ["motion", "lift"], lambda m: m.group(1)),
        (r"button-(.+)", ["component", "button"], lambda m: m.group(1)),
        (r"input-(.+)", ["component", "input"], lambda m: m.group(1)),
        (r"nav-(.+)", ["component", "nav"], lambda m: m.group(1)),
        (r"(gradient-.+|glass.*)", ["decorative"], lambda m: m.group(1)),
        (r"bp-(.+)", ["breakpoint"], lambda m: m.group(1)),
        (r"container-(.+)", ["size", "container"], lambda m: m.group(1)),
        (r"w-(.+)", ["size", "width"], lambda m: m.group(1)),
        (r"grid-(.+)", ["size", "grid"], lambda m: m.group(1)),
    ]
    for pat, group, leaf in rules:
        m = re.fullmatch(pat, name)
        if m:
            return group, leaf(m)
    return ["misc"], name


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
def build(package: str) -> dict:
    css_path = TOKENS_DIR / f"tokens-{package}.css"
    light, dark = parse_css(css_path)
    numeric_vars = _resolve_numeric_vars(light)

    root: dict = {
        "$description": (
            f"Nordover design tokens — {package} package (W3C DTCG format). "
            "Generated from tokens-{}.css by scripts/build_tokens.py — "
            "do not edit by hand.".format(package)
        ),
    }

    def ensure_group(path: list[str]) -> dict:
        node = root
        for part in path:
            node = node.setdefault(part, {})
        return node

    for name, value in light:
        group, leaf = group_of(name)
        dtype, dvalue, is_raw = type_value(name, value, numeric_vars, group_of)
        token: dict = {}
        if dtype is not None:
            token["$type"] = dtype
        token["$value"] = dvalue
        ext: dict = {}
        if is_raw:
            ext[f"{EXT}.cssText"] = True
        # dark override (if any) attached to the same token
        if name in dark:
            ddtype, ddvalue, draw = type_value(
                name, dark[name], numeric_vars, group_of
            )
            dark_entry: dict = {"$value": ddvalue}
            if draw:
                dark_entry["cssText"] = True
            ext[f"{EXT}.dark"] = dark_entry
        if ext:
            token["$extensions"] = ext
        ensure_group(group)[leaf] = token

    # Dark-only tokens (defined only in the dark block) — rare, but capture.
    light_names = {n for n, _ in light}
    for name, value in dark.items():
        if name in light_names:
            continue
        group, leaf = group_of(name)
        dtype, dvalue, is_raw = type_value(name, value, numeric_vars, group_of)
        token = {}
        if dtype is not None:
            token["$type"] = dtype
        token["$value"] = dvalue
        token["$extensions"] = {f"{EXT}.darkOnly": True}
        ensure_group(group)[leaf] = token

    return root


def main(argv: list[str]) -> int:
    check = "--check" in argv
    failed = False
    for pkg in PACKAGES:
        data = build(pkg)
        out = TOKENS_DIR / f"tokens-{pkg}.json"
        text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        if check:
            current = out.read_text(encoding="utf-8") if out.exists() else ""
            if current != text:
                print(f"OUT OF DATE: {out.relative_to(ROOT)}")
                failed = True
            else:
                print(f"ok: {out.relative_to(ROOT)}")
        else:
            out.write_text(text, encoding="utf-8")
            n = sum(1 for _ in re.finditer(r'"\$value"', text))
            print(f"wrote {out.relative_to(ROOT)} ({n} tokens)")
    if check and failed:
        print("\nRun: python3 scripts/build_tokens.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
