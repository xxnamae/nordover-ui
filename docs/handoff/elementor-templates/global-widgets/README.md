# Global Widgets — Reusable Components

Global Widgets are pre-configured, reusable components that can be inserted into any Elementor design. They are built with Nordover tokens and can be customized via `@layer brand`.

## Available Global Widgets

### 1. Button (All Variants)
**File:** `btn-primary.json`, `btn-secondary.json`, `btn-ghost.json`

Pre-configured button widgets with:
- Semantic styling (primary, secondary, ghost/outline)
- Size variants (sm, md, lg)
- State styling (hover, active, disabled)
- Icon support
- Full WCAG AA compliance

**Usage:** Drag into any section, change link, customize via global variables.

### 2. Card — Feature Block
**File:** `card-feature.json`

Card component with:
- Icon placeholder (48px)
- Title (h3)
- Description (body-sm)
- CTA link with arrow
- Border and background from tokens
- Responsive padding

**Customization:** Replace icon, title, description; adjust link target.

### 3. Card — Testimonial
**File:** `card-testimonial.json`

Testimonial card with:
- Star rating (1–5 stars)
- Quote text
- Author name + role
- Avatar image (64px, 1:1 aspect ratio)
- Background color from surface token

**Customization:** Update quote, author, role, avatar image, star count.

### 4. Card — Team Member
**File:** `card-team-member.json`

Team member card with:
- Avatar image (240px, 1:1 aspect ratio)
- Name (h3)
- Role (body-sm, muted)
- Bio (body-md)
- Social links (optional)

**Customization:** Update photo, name, role, bio, social URLs.

### 5. Pricing Card
**File:** `card-pricing.json`

Pricing tier card with:
- Plan name (h3)
- Price + currency/period
- Feature list (bullets, left-aligned)
- CTA button (primary, full-width)
- Highlight state (border-accent option)

**Customization:** Update plan name, price, features, button label/link.

### 6. Form Field Group
**File:** `form-field-group.json`

Reusable form input wrapper with:
- Label (bound to input via aria-labelledby)
- Input field (text, email, tel, etc.)
- Help text (optional, below input)
- Error message display
- Focus state styling
- Validation icon (checkmark or ×)

**Customization:** Change label, input type, help text, validation state.

### 7. Feature List
**File:** `feature-list.json`

Vertical list of features with:
- Checkmark icon per feature
- Feature title
- Feature description
- Left-aligned icon
- Even spacing between items

**Customization:** Update feature titles/descriptions, modify icon style.

### 8. Stat Block
**File:** `stat-block.json`

Single KPI display with:
- Large accent-colored number
- Label text (body-lg)
- Optional trend indicator (↑/↓)
- Centered layout

**Customization:** Update number, label, trend direction.

## How to Use Global Widgets

### In Elementor v4
1. Go to **Library** → **Global Widgets**
2. Click **Import Global Widget** → Select JSON file
3. Drag global widget into your page
4. Customize text, images, links as needed
5. Changes to styling automatically update across all instances

### In Elementor v3
1. Create a new widget
2. Copy the HTML/CSS from the global widget JSON
3. Paste into your page
4. Customize manually

## Customization via @layer brand

All global widgets respect Nordover token variables. Customize appearance by overriding tokens in your brand layer:

```css
@layer brand {
  :root {
    --color-accent: #your-brand-color;
    --color-surface: #your-surface-color;
    /* ...more token overrides */
  }
}
```

Changes to token variables automatically update all global widgets using those tokens.

## Responsive Behavior

All global widgets are built with:
- **Mobile-first** layout approach
- **Flexible** width (100% parent by default)
- **Touch-friendly** tap targets (min 44–48px)
- **Readable** font sizes on all screen sizes

Responsiveness is built into the CSS — no additional configuration needed.

## Accessibility

Every global widget includes:
- **ARIA labels** and descriptions
- **Keyboard navigation** support
- **Focus states** for interactive elements
- **Color contrast** meeting WCAG AA (4.5:1 minimum)
- **Semantic HTML** (buttons, links, forms properly marked)

## Version Support

- **Elementor v4+:** Import JSON directly → instant sync with token updates
- **Elementor v3:** Copy HTML/CSS → static styling (no auto-sync with token changes)

For v3, manually update colors and spacing when token values change.
