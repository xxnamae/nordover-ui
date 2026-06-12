#!/usr/bin/env python3
"""Generate an Elementor v4 (Editor V4) Variables JSON from the canonical Nordover CSS.

The CSS token files (docs/visual/tokens/tokens-{web,app}.css) stay the single
source of truth. This emits a `global-variables` document in the exact shape
Elementor v4.1 produces on export:

    {"data": { "e-gv-<id>": {type,label,value,order,...}, ... },
     "watermark": N, "version": 1}

Four Elementor variable types are produced, matching a real kit export:
  - global-color-variable        hex (8-digit when alpha < 1); carries sync_to_v3
  - global-font-variable         first family name from the CSS stack
  - global-size-variable         a single rem/px/%/em/ch dimension
  - global-custom-size-variable  any computed expression (clamp(), calc(), …)

Because Elementor colour variables are concrete hex, OKLCH and color-mix() are
resolved here (reusing the OKLab matrices from check_contrast.py). clamp()/calc()
survive verbatim as custom-size — Elementor v4 accepts them.

Elementor variables hold one value each (no per-variable light/dark), so the
LIGHT/base block is exported. Dark mode in Elementor needs a separate mechanism.

Usage:  python3 scripts/build_elementor.py            # writes both packages
        python3 scripts/build_elementor.py --check     # verify up to date
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS_DIR = ROOT / "docs" / "visual" / "tokens"
OUT_DIR = ROOT / "docs" / "handoff"
PACKAGES = ["web", "app"]
NUM = r"-?\d+(?:\.\d+)?"
# Fixed timestamp so regeneration is deterministic (clean diffs, --check works).
# Elementor overwrites these with live values on import; they only need to exist.
TIMESTAMP = "2026-06-10 00:00:00"


# ---------------------------------------------------------------------------
# CSS parsing (mirrors build_tokens.py)
# ---------------------------------------------------------------------------
def _match_block(css: str, start: int) -> str:
    open_idx = css.index("{", start)
    depth = 0
    for i in range(open_idx, len(css)):
        if css[i] == "{":
            depth += 1
        elif css[i] == "}":
            depth -= 1
            if depth == 0:
                return css[open_idx + 1 : i]
    raise ValueError("unbalanced braces")


def parse_light(path: Path) -> list[tuple[str, str]]:
    """Ordered (name, raw-value) pairs from the `:root` block inside @layer tokens."""
    css = path.read_text(encoding="utf-8")
    layer_idx = css.index("@layer tokens {")
    root_idx = css.index(":root", layer_idx)
    body = re.sub(r"/\*.*?\*/", "", _match_block(css, root_idx), flags=re.DOTALL)
    decls: list[tuple[str, str]] = []
    for chunk in body.split(";"):
        chunk = chunk.strip()
        if not chunk.startswith("--"):
            continue
        name, _, value = chunk.partition(":")
        decls.append((name.strip()[2:], " ".join(value.split())))
    return [(n, v) for n, v in decls if n and v]


# ---------------------------------------------------------------------------
# var() expansion
# ---------------------------------------------------------------------------
def expand(value: str, scope: dict[str, str], seen: frozenset = frozenset()) -> str:
    """Recursively substitute every var(--x) with its resolved literal."""
    def repl(m: re.Match) -> str:
        key = m.group(1)[2:]  # scope keys are stored without the leading --
        if key in seen or key not in scope:
            return m.group(0)
        return expand(scope[key], scope, seen | {key})

    return re.sub(r"var\(\s*(--[\w-]+)\s*\)", repl, value).strip()


# ---------------------------------------------------------------------------
# Colour resolution → hex
# ---------------------------------------------------------------------------
def _oklch_to_srgb(L: float, C: float, H: float) -> tuple[float, float, float]:
    a = C * math.cos(math.radians(H))
    b = C * math.sin(math.radians(H))
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_
    g = -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_
    bb = -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_
    return tuple(min(1.0, max(0.0, x)) for x in (r, g, bb))


def _gamma(x: float) -> float:
    return 12.92 * x if x <= 0.0031308 else 1.055 * (x ** (1 / 2.4)) - 0.055


# An OKLCH colour carried as (L, C, H, alpha). H is None when achromatic.
Color = tuple


def parse_color(value: str, scope: dict[str, str], numeric: dict[str, str]):
    """Resolve a CSS colour expression to (L, C, H|None, alpha), or None."""
    v = expand(value, scope).strip()

    if v in ("transparent",):
        return (0.0, 0.0, None, 0.0)
    if v == "white":
        return (1.0, 0.0, None, 1.0)
    if v == "black":
        return (0.0, 0.0, None, 1.0)

    if v.startswith("oklch("):
        inner = v[v.index("(") + 1 : v.rindex(")")]
        inner = re.sub(
            r"var\(\s*(--[\w-]+)\s*\)",
            lambda m: numeric.get(m.group(1), m.group(0)),
            inner,
        )
        alpha = 1.0
        if "/" in inner:
            inner, _, a = inner.partition("/")
            a = a.strip()
            if re.fullmatch(NUM + r"%?", a):
                alpha = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        parts = inner.split()
        if len(parts) >= 3:
            L, C, H = (float(parts[0]), float(parts[1]), float(parts[2]))
            return (L, C, None if C < 1e-4 else H, alpha)
        return None

    if v.startswith("color-mix("):
        return _mix(v, scope, numeric)

    m = re.fullmatch(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?", v)
    if m:  # defensive: a literal hex (none in Nordover today)
        return _hex_to_oklch(m.group(0))

    return None


def _split_top(s: str) -> list[str]:
    """Split on top-level commas (ignores commas inside nested parens)."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def _mix(value: str, scope: dict[str, str], numeric: dict[str, str]):
    inner = value[value.index("(") + 1 : value.rindex(")")]
    args = _split_top(inner)
    if len(args) < 3 or "oklch" not in args[0]:
        return None
    a_color, a_pct = _color_and_pct(args[1])
    b_color, b_pct = _color_and_pct(args[2])
    ca = parse_color(a_color, scope, numeric)
    cb = parse_color(b_color, scope, numeric)
    if not ca or not cb:
        return None
    # Weights
    if a_pct is not None and b_pct is not None:
        w1, w2 = a_pct / 100, b_pct / 100
    elif a_pct is not None:
        w1, w2 = a_pct / 100, 1 - a_pct / 100
    elif b_pct is not None:
        w1, w2 = 1 - b_pct / 100, b_pct / 100
    else:
        w1 = w2 = 0.5
    return _interp(ca, cb, w1, w2)


def _color_and_pct(arg: str) -> tuple[str, float | None]:
    arg = arg.strip()
    m = re.search(r"\s(" + NUM + r")%$", arg)
    if m:
        return arg[: m.start()].strip(), float(m.group(1))
    return arg, None


def _interp(ca, cb, w1, w2):
    """Premultiplied-alpha OKLCH interpolation (matches CSS color-mix in oklch)."""
    L1, C1, H1, A1 = ca
    L2, C2, H2, A2 = cb
    out_a = w1 * A1 + w2 * A2
    if out_a <= 0:
        return (0.0, 0.0, None, 0.0)
    # Premultiply L/C by alpha, mix, then un-premultiply.
    L = (w1 * A1 * L1 + w2 * A2 * L2) / out_a
    C = (w1 * A1 * C1 + w2 * A2 * C2) / out_a
    # Hue: take the chromatic side; if both have hue, shortest-arc interp.
    if H1 is None and H2 is None:
        H = None
    elif H1 is None:
        H = H2
    elif H2 is None:
        H = H1
    else:
        d = ((H2 - H1 + 180) % 360) - 180
        H = (H1 + (w2 / (w1 + w2)) * d) % 360
    return (L, C, H, out_a)


def _hex_to_oklch(h: str):
    h = h.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    a = int(h[6:8], 16) / 255 if len(h) >= 8 else 1.0

    def lin(x):
        return x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4

    r, g, b = lin(r), lin(g), lin(b)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = l ** (1 / 3), m ** (1 / 3), s ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    C = math.hypot(A, B)
    H = math.degrees(math.atan2(B, A)) % 360
    return (L, C, None if C < 1e-4 else H, a)


def to_hex(color) -> str:
    L, C, H, alpha = color
    r, g, b = _oklch_to_srgb(L, C, H or 0.0)
    rgb = "".join(f"{round(_gamma(x) * 255):02x}" for x in (r, g, b))
    if alpha < 0.999:
        return f"#{rgb}{round(alpha * 255):02x}"
    return f"#{rgb}"


# ---------------------------------------------------------------------------
# Token selection + classification
# ---------------------------------------------------------------------------
def is_color(name: str) -> bool:
    if re.fullmatch(r"color-(error|success|warning|info)", name):
        return False  # skip back-compat aliases (dupes of --error etc.)
    return bool(
        re.match(r"gray-", name)
        or re.fullmatch(r"color-(bg|surface|fg|muted|subtle|border|accent"
                        r"|accent-fg|accent-hover|accent-active|focus|backdrop)", name)
        or re.fullmatch(r"(error|success|warning|info)(-(subtle|strong|light|dark))?", name)
        or re.match(r"chart-", name)
        or re.fullmatch(r"surface-[1-5]", name)
        or re.fullmatch(r"accent-(subtle|muted|emphasis)", name)
        or name == "on-accent-subtle"
    )


def is_font(name: str) -> bool:
    return name in ("font-sans", "font-display", "font-mono")


SIZE_PREFIXES = ("space-", "radius-", "bw-", "text-", "container-", "w-",
                 "size-icon", "gap-", "grid-")
SIZE_EXACT = {"spacing-section", "spacing-section-sm", "spacing-section-lg",
              "page-padding", "target-min", "target-comfortable",
              "density-control-height"}


def is_size(name: str) -> bool:
    return name.startswith(SIZE_PREFIXES) or name in SIZE_EXACT


SIMPLE_SIZE = re.compile(r"^" + NUM + r"(rem|px|em|ch|vw|vh|%)?$")


def classify_size(literal: str) -> str:
    return ("global-size-variable" if SIMPLE_SIZE.fullmatch(literal)
            else "global-custom-size-variable")


def first_family(stack: str) -> str:
    return _split_top(stack)[0].strip().strip('"').strip("'")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def gv_id(label: str) -> str:
    """Generate deterministic, stable Elementor global variable ID.

    Algorithm (FORMAT-CONTRACT.md § Elementor Global Variable ID Contract):
      Input:  CSS token name WITHOUT '--' prefix (e.g., 'color-accent')
      Hash:   MD5(label).hexdigest()[:7]
      Format: 'e-gv-' + hash
      Result: e.g., 'e-gv-99f8157'

    Guarantees:
      • Deterministic: Same label → same ID across regenerations
      • Stable: IDs never recycled or reassigned
      • Immutable: Once assigned, frozen for variable lifetime
      • Consumer-reproducible: Token Studio using MD5(label) produces identical IDs
      • Round-trippable: Export kit → modify in Elementor → re-import updates
        (matches IDs prevent duplication)

    See: docs/visual/FORMAT-CONTRACT.md for full contract.
    """
    return "e-gv-" + hashlib.md5(label.encode()).hexdigest()[:7]


def build(package: str) -> dict:
    light = parse_light(TOKENS_DIR / f"tokens-{package}.css")
    scope = dict(light)
    numeric = {f"--{n}": v for n, v in light if re.fullmatch(NUM, v)}

    data: dict = {}
    order = 0
    for name, raw in light:
        entry = None
        if is_color(name):
            c = parse_color(raw, scope, numeric)
            if c is not None:
                entry = {"type": "global-color-variable", "label": name,
                         "value": to_hex(c), "sync_to_v3": True}
        elif is_font(name):
            entry = {"type": "global-font-variable", "label": name,
                     "value": first_family(raw)}
        elif is_size(name):
            literal = expand(raw, scope)
            entry = {"type": classify_size(literal), "label": name,
                     "value": literal}
        if entry is None:
            continue
        order += 1
        # Field shape mirrors a real Elementor v4.1 kit export: every entry
        # carries created_at/updated_at; only colours carry sync_to_v3.
        record = {
            "type": entry["type"], "label": entry["label"],
            "value": entry["value"], "order": order,
            "created_at": TIMESTAMP, "updated_at": TIMESTAMP,
        }
        if entry["type"] == "global-color-variable":
            record["sync_to_v3"] = True
        data[gv_id(name)] = record
    return {"data": data, "watermark": len(data), "version": 1}


def main(argv: list[str]) -> int:
    check = "--check" in argv
    failed = False
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for pkg in PACKAGES:
        doc = build(pkg)
        out = OUT_DIR / f"nordover-elementor-v4-{pkg}.json"
        text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
        if check:
            current = out.read_text(encoding="utf-8") if out.exists() else ""
            if current != text:
                print(f"OUT OF DATE: {out.relative_to(ROOT)}")
                failed = True
            else:
                print(f"ok: {out.relative_to(ROOT)}")
        else:
            out.write_text(text, encoding="utf-8")
            counts: dict[str, int] = {}
            for v in doc["data"].values():
                counts[v["type"]] = counts.get(v["type"], 0) + 1
            summary = ", ".join(f"{k.replace('global-', '').replace('-variable', '')}: {n}"
                                for k, n in sorted(counts.items()))
            print(f"wrote {out.relative_to(ROOT)} ({len(doc['data'])} variables — {summary})")
    if check and failed:
        print("\nRun: python3 scripts/build_elementor.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
