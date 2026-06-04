#!/usr/bin/env python3
"""Validate that tokens-web.css and tokens-app.css have consistent token names.

Ensures that both files declare the same tokens (except marked platform-exclusive).
Platform-exclusive tokens must be marked with /* web-only */ or /* app-only */ comment.

Exit: 0 if valid, 1 if divergence found.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS_DIR = ROOT / "docs" / "visual" / "tokens"
WEB_FILE = TOKENS_DIR / "tokens-web.css"
APP_FILE = TOKENS_DIR / "tokens-app.css"


def extract_tokens(file_path: Path) -> tuple[set[str], dict[str, bool]]:
    """Parse CSS and extract all token names from :root {} block.

    Returns:
        (all_token_names, {token_name: is_platform_exclusive})
    """
    css = file_path.read_text(encoding="utf-8")

    # Find :root { ... } block within @layer tokens
    layer_start = css.find("@layer tokens")
    if layer_start == -1:
        raise ValueError(f"@layer tokens not found in {file_path}")

    root_start = css.find(":root {", layer_start)
    if root_start == -1:
        raise ValueError(f":root {{ not found in {file_path}")

    # Find matching closing brace
    depth = 0
    pos = root_start + len(":root ")
    while pos < len(css):
        if css[pos] == "{":
            depth += 1
        elif css[pos] == "}":
            depth -= 1
            if depth == 0:
                root_body = css[root_start : pos + 1]
                break
        pos += 1
    else:
        raise ValueError(f"Unmatched braces in :root block in {file_path}")

    # Extract token declarations: --name: value;  /* optional comment */
    # Match each declaration up to its terminating ; capturing any trailing
    # comment (which may carry a /* web-only */ or /* app-only */ marker).
    tokens = set()
    platform_exclusive = {}

    decl_re = re.compile(r"(--[\w-]+)\s*:\s*[^;]*;(?:[ \t]*/\*[^*]*\*/)?")
    for match in decl_re.finditer(root_body):
        token_name = match.group(1)
        tokens.add(token_name)

        # Check the full matched declaration for a platform-exclusive marker.
        # Accepts both bare markers (/* web-only */) and descriptive ones
        # (/* web-only: hero display scale */).
        decl_text = match.group(0)
        is_exclusive = "web-only" in decl_text or "app-only" in decl_text
        platform_exclusive[token_name] = is_exclusive

    return tokens, platform_exclusive


def main():
    print("Validating token consistency...")
    print(f"  Web:  {WEB_FILE}")
    print(f"  App:  {APP_FILE}")
    print()

    try:
        web_tokens, web_exclusive = extract_tokens(WEB_FILE)
        app_tokens, app_exclusive = extract_tokens(APP_FILE)
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Error parsing token files: {e}")
        return 1

    print(f"Web tokens: {len(web_tokens)}")
    print(f"App tokens: {len(app_tokens)}")
    print()

    # Tokens that should exist in both (not platform-exclusive)
    web_shared = {t for t in web_tokens if not web_exclusive.get(t, False)}
    app_shared = {t for t in app_tokens if not app_exclusive.get(t, False)}

    web_exclusive_tokens = {t for t in web_tokens if web_exclusive.get(t, False)}
    app_exclusive_tokens = {t for t in app_tokens if app_exclusive.get(t, False)}

    # Find divergence
    missing_in_app = web_shared - app_shared
    missing_in_web = app_shared - web_shared

    errors = []

    if missing_in_app:
        errors.append(
            f"❌ Tokens in web but not app (and not marked /* web-only */):\n"
            + "\n".join(f"   {t}" for t in sorted(missing_in_app))
        )

    if missing_in_web:
        errors.append(
            f"❌ Tokens in app but not web (and not marked /* app-only */):\n"
            + "\n".join(f"   {t}" for t in sorted(missing_in_web))
        )

    if errors:
        print("\n".join(errors))
        print()
        print("💡 To fix:")
        print("  1. Add missing tokens to the corresponding file")
        print("  2. If platform-specific, mark with /* web-only */ or /* app-only */")
        print("  3. Update docs/visual/tokens/TOKEN-CONSISTENCY.md")
        return 1

    print(f"✅ Shared tokens: {len(web_shared)}")
    print(f"✅ Web-exclusive: {len(web_exclusive_tokens)}")
    print(f"✅ App-exclusive: {len(app_exclusive_tokens)}")
    print()
    print("✅ Token names are consistent!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
