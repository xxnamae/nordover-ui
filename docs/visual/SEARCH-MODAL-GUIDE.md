# Search Modal — Styleguide Navigation

## Overview

The styleguide features a modern search modal dialog (not a browser `prompt()`) that enables fast navigation through components, tokens, and patterns.

## How to Use

### Opening the Modal
- Press **Ctrl+K** (Windows/Linux) or **Cmd+K** (Mac)
- The modal will open with focus automatically on the search input field

### Searching
- Type any component, token, or section name
- Results update in real-time as you type
- Each result shows the component title and a brief description

### Navigation & Selection
- **Arrow Up/Down**: Navigate through results
- **Enter**: Select the highlighted result and jump to that section
- **ESC**: Close the modal
- **Ctrl+K** again: Toggle modal open/closed

### Closing
- Press **ESC**
- Click the **X** button in the top-right
- Click outside the modal (backdrop)

## Architecture

### Files
- `search-modal.js` — Main SearchModal class
- `styleguide-enhancements.css` — Modal styling and animations
- `styleguide-web.html` — Web styleguide integration
- `styleguide-app.html` — App styleguide integration

### SearchModal Class

The `SearchModal` class is instantiated automatically when the DOM loads:

```javascript
class SearchModal {
  constructor()           // Initialize modal
  init()                  // Set up DOM and events
  createModal()          // Create <dialog> element
  setupEventListeners()  // Bind keyboard and click handlers
  open()                 // Display modal and focus input
  close()                // Hide modal
  search(query)          // Filter and display results
  renderResults()        // Render matching sections
  updateSelection(els)   // Highlight selected result
  showEmpty()            // Show empty state with shortcuts
  escapeHtml(text)       // Sanitize text for display
}
```

## Keyboard Support

| Key | Action |
|-----|--------|
| `Ctrl+K` / `Cmd+K` | Toggle modal |
| `↑` / `↓` | Navigate results |
| `Enter` | Select and jump |
| `ESC` | Close modal |
| `Tab` | Focus trap (stays within modal) |

## Accessibility Features

✓ **ARIA attributes:**
  - `role="dialog"` — Semantic role
  - `aria-labelledby="search-title"` — Dialog title reference
  - `aria-modal="true"` — Modal behavior
  - `aria-live="polite"` — Results announce changes
  - `aria-selected` — Selected result state
  - `aria-controls` — Input controls results

✓ **Focus management:**
  - Auto-focus on input when opened
  - Focus trap (Tab/Shift+Tab cycles within modal)
  - Visible focus indicators (blue outline)

✓ **Keyboard navigation:**
  - Full keyboard control (no mouse required)
  - Arrow keys for results list
  - Enter to select
  - ESC to close

## Styling

### CSS Classes

**Dialog structure:**
- `.search-dialog` — `<dialog>` element
- `.search-dialog::backdrop` — Semi-transparent overlay with blur
- `.search-dialog-content` — Main container
- `.search-dialog-header` — Title and close button
- `.search-dialog-input-wrapper` — Input field wrapper
- `.search-dialog-results` — Results container

**Results:**
- `.search-dialog-result` — Individual result item
- `.search-dialog-result.selected` — Highlighted result
- `.search-result-title` — Result heading
- `.search-result-desc` — Result description

**Empty/no results:**
- `.search-dialog-empty` — Empty state with shortcuts
- `.search-dialog-shortcuts` — Keyboard hint buttons
- `.search-dialog-no-results` — No matches message

### Animations

Two smooth animations play on open:

1. **Backdrop fade-in:** `fadeIn` (150ms)
2. **Modal slide-up:** `slideUp` (250ms)

Animations use CSS custom properties for timing:
- `var(--duration-fast)` — Backdrop fade
- `var(--duration-moderate)` — Modal slide

### Mobile Optimization

- Modal scales to 95vw on screens < 768px
- Input field and results stack vertically
- Shortcuts display in column layout on small screens
- Max height limited to 80vh for scrollable access

## Search Behavior

### Search Scope
The modal searches across all `.doc-section[id]` elements:
- Component titles (`<h2>`)
- Section descriptions (`<p>`)
- Results include section ID for anchor navigation

### Case-insensitive
Queries match regardless of case:
- "Button" = "button" = "BUTTON"

### Partial matching
Queries find partial matches:
- "btn" finds "button"
- "form" finds "form-input" and "form-select"

### Live updates
Results update as you type — no submit required.

## Integration

### Adding to a new styleguide
1. Link the CSS in `<head>`:
   ```html
   <link rel="stylesheet" href="./styleguide-enhancements.css">
   ```

2. Load the script before `</body>`:
   ```html
   <script src="./search-modal.js"></script>
   ```

3. Ensure content is in `.doc-section[id]` containers.

## Browser Support

- Chrome/Edge: Full support (native `<dialog>`)
- Firefox: Full support (native `<dialog>`)
- Safari: Full support (native `<dialog>`)
- Requires: CSS custom properties, ES6 classes, `showModal()` API

## Future Enhancements

Potential improvements:
- Recent searches (localStorage)
- Search history (up/down arrows)
- Fuzzy matching for typos
- Keyboard shortcuts display (Cmd+/)
- Search analytics
- Categories/facets (tokens vs. components)
- Linking to external docs
