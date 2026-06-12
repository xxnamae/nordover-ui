# Icon Set — Nordover Visual System

Nordover ships **24 curated, minimalist glyphs** on a 24×24px grid. All icons:
- **Stroke-based** (no fill): `stroke-width: 1.5`, `stroke-linecap: round`, `stroke-linejoin: round`
- **currentColor**: colors inherit from parent `.icon` styles
- **MIT-licensed**: subset from Lucide Icons
- **Responsive**: scale via `.icon-sm`, `.icon`, `.icon-lg` CSS classes (existing sizing)

## Navigation Glyphs (7)
For navigation, section toggles, and directional indicators.

| Icon | File | Use Case |
|------|------|----------|
| ↓ | `icon-chevron-down.svg` | Collapse/expand, dropdown toggle |
| → | `icon-chevron-right.svg` | Next, submenu, disclosure |
| ↑ | `icon-chevron-up.svg` | Collapse to hide, scrolling up |
| ☰ | `icon-menu.svg` | Primary navigation toggle (mobile) |
| ✕ | `icon-x-close.svg` | Dismiss, close modal, remove item |
| ↗ | `icon-arrow-external.svg` | External link, opens in new tab |
| 🔍 | `icon-search.svg` | Find, filter, search input |

## Status Glyphs (4)
For validation, success, error, and informational states.

| Icon | File | Use Case |
|------|------|----------|
| ✓ | `icon-check.svg` | Success, task completed, valid |
| ✗ | `icon-x-mark.svg` | Error, failed, invalid, destructive |
| ⚠ | `icon-alert-triangle.svg` | Warning, caution, review required |
| ℹ | `icon-info-circle.svg` | Information, help, details |

## Action Glyphs (7)
For user interactions and common operations.

| Icon | File | Use Case |
|------|------|----------|
| ⬇ | `icon-download.svg` | Download file, export |
| ◻ | `icon-copy.svg` | Duplicate, copy to clipboard |
| ✏ | `icon-edit.svg` | Edit, modify, pencil tool |
| 🗑 | `icon-trash-2.svg` | Delete, remove permanently |
| ✚ | `icon-plus.svg` | Add new, create, increment |
| ⚙ | `icon-settings.svg` | Configuration, options, preferences |
| 🔄 | `icon-reload.svg` | Refresh, reload, retry, sync |

## Content Glyphs (7)
For labeling and representing common content types.

| Icon | File | Use Case |
|------|------|----------|
| 📅 | `icon-calendar.svg` | Date picker, schedule, calendar widget |
| 🕐 | `icon-clock.svg` | Time, duration, scheduling |
| 👤 | `icon-user.svg` | Profile, account, user identity |
| 📁 | `icon-folder.svg` | Directory, file navigation, collections |
| 🖼 | `icon-image.svg` | Image, photo, asset, media |
| 📧 | `icon-mail.svg` | Email, message, contact |
| ☎ | `icon-phone.svg` | Phone number, call, phone input |

## Integration

### Individual SVG (preferred)
```html
<!-- navigation -->
<svg class="icon" aria-label="Open menu">
  <use href="/docs/visual/icons/icon-menu.svg#icon"></use>
</svg>

<!-- or direct embed -->
<button type="button" aria-label="Open menu">
  <svg class="icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" …>
    <!-- content -->
  </svg>
</button>
```

### CSS Classes
Size via existing `.icon`, `.icon-sm`, `.icon-lg` in `components-web.css` and `components-app.css`. Colors via `.icon-success`, `.icon-error`, `.icon-warning`, `.icon-info` (if defined in component system).

### Sprite (optional, batch)
For pages with many icons:
```html
<svg style="display: none">
  <use href="/docs/visual/icons/sprite.svg"></use>
</svg>

<!-- reference -->
<svg class="icon"><use href="#icon-check"></use></svg>
```

## Grid & Sizing

- **Canvas:** 24×24 px
- **Safe zone:** 20×20 px (2px margins)
- **Stroke:** 1.5 px, rounded (linecap/linejoin)
- **Scaling:** Use viewBox 0 0 24 24 throughout

## Accessibility

- All `.icon` renders must have explicit `aria-label` or semantic context
- No decorative icons should omit `aria-hidden="true"`
- Status glyphs (check, x, alert) should pair with color tokens (green, red, orange, blue)

## Maintenance

This manifest reflects the authoritative set. Adding new icons requires:
1. Creating the SVG file (24×24 grid, 1.5 stroke)
2. Updating this manifest
3. Exporting to sprite (if using batch rendering)
4. Updating styleguide with usage examples

All icons are **immutable once published**; renaming requires deprecation notices in CHANGELOG.
