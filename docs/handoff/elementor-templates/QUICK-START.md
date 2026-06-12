# Nordover + Elementor — Quick Start Guide

Kom raskt i gang med å bygge kundesider med Nordover Design System + Elementor.

## TL;DR (30 sekunder)

1. **Install:** WordPress + Elementor v4+
2. **Paste CSS:** Nordover tokens + components stylesheets
3. **Import Kit:** `nordover-kit-app.json` eller `nordover-kit-web.json`
4. **Choose Template:** Landing page? Product page? Services? → Import wireframe JSON
5. **Edit:** Change text, images, links. **Done.**

**Resultat:** Professional, branded site på 2–4 timer. Alle komponenter bruker Nordover tokens.

---

## What's in the Box?

### Sections (17 stk.) — Pre-built Building Blocks
```
docs/handoff/elementor-templates/sections/
├── hero-classic.json ...................... Full-width hero banner
├── features-grid.json ..................... 3-column feature cards
├── cta-minimal.json ....................... High-converting CTA
├── pricing-cards.json ..................... 3-tier pricing
├── faq-accordion.json ..................... Q&A accordion
├── team-grid.json ......................... Team member showcase
├── testimonials-cards.json ................ Social proof quotes
├── blog-grid.json ......................... Post grid
├── newsletter-signup.json ................. Email signup form
├── contact-form.json ...................... Contact form
├── gallery-grid.json ...................... Image gallery + lightbox
├── stats-counters.json .................... KPI counters
├── process-timeline.json .................. Workflow steps
├── header-navigation.json ................. Sticky nav + logo
├── footer.json ............................ Multi-column footer
├── services.json .......................... Service showcase
└── comparison-table.json .................. Feature comparison table
```

**Use Case:** Drag sections into any page. Customize text/images. Styling automatic.

### Kits (2) — Global Variables
```
docs/handoff/elementor-templates/kits/
├── nordover-kit-app.json .................. Dark/compact (SaaS)
└── nordover-kit-web.json .................. Light/airy (marketing)
```

**Use Case:** One-click setup for all global colors, typography, spacing.

### Global Widgets (In Progress) — Reusable Components
```
docs/handoff/elementor-templates/global-widgets/
├── btn-primary.json ....................... Primary button
├── card-feature.json ...................... Feature card (coming)
├── card-testimonial.json .................. Testimonial card (coming)
├── card-team-member.json .................. Team member card (coming)
├── card-pricing.json ...................... Pricing card (coming)
└── form-field-group.json .................. Form input wrapper (coming)
```

**Use Case:** Drag individual components into any page. Styling automatic.

### Wireframes (6) — Full Page Templates
```
docs/handoff/elementor-templates/wireframes/
├── landing-page.json ...................... Hero + features + CTA
├── product-page.json ...................... Features + pricing + FAQ
├── blog-template.json ..................... Post grid + sidebar (coming)
├── contact-page.json ...................... Contact form + team (coming)
├── about-page.json ........................ Mission + team + story (coming)
└── pricing-page.json ...................... Pricing + comparison + FAQ (coming)
```

**Use Case:** Pre-assembled page = 7 sections combined. Change text/images. Publish.

### Integration Guides
```
docs/handoff/
├── ELEMENTOR-TEMPLATE-LIBRARY.md ......... Detailed library docs (1300+ lines)
├── WORDPRESS-ELEMENTOR-SETUP.md ......... 12-step WordPress setup guide
└── elementor-templates/README.md ........ Template catalog + customization
```

---

## Fastest Path to a New Site

### For v4 Users (Recommended)

**Time: ~2 hours**

```bash
# 1. Install WordPress + Elementor v4
# (hosting provider handles this)

# 2. Register Nordover CSS in theme
# Add to functions.php:
function enqueue_nordover() {
  wp_enqueue_style('nordover-tokens', 'path/to/tokens-app.css');
  wp_enqueue_style('nordover-components', 'path/to/components-app.css', ['nordover-tokens']);
}
add_action('wp_enqueue_scripts', 'enqueue_nordover');

# 3. Import Kit (5 min)
# WordPress admin → Elementor Settings → Kits → Import
# Select: nordover-kit-app.json (or nordover-kit-web.json)

# 4. Create landing page (90 min)
# Blank page → Library → Import wireframe → landing-page.json
# Edit text, upload images, update links

# 5. Publish
# ✅ Done
```

### For v3 Users

**Time: ~6–8 hours** (manual section creation)

```bash
# 1. Install WordPress + Elementor v3

# 2. Register Nordover CSS (same as v4)

# 3. Create sections manually
# - Open section JSON in editor
# - Copy HTML structure
# - Elementor: Custom HTML widget
# - Paste + verify styling

# 4. Repeat for 7 sections = ~6 hours

# 5. Publish
# Note: v3 doesn't sync with kit updates. Update colors manually if needed.
```

---

## Customization in 3 Steps

### Step 1: Override Tokens (Optional)

Add to your theme's custom CSS or `functions.php`:

```css
@layer brand {
  :root {
    /* Your brand colors */
    --color-accent: #your-brand-blue;
    --color-success: #your-brand-green;
    --color-error: #your-brand-red;
    
    /* Or override all 12 core colors */
    --color-fg: #your-text-color;
    --color-bg: #your-background;
    --color-surface: #your-surface;
    --color-muted: #your-muted;
    --color-border: #your-border;
    --color-secondary: #your-secondary;
    --color-info: #your-info;
    --color-warning: #your-warning;
  }
}
```

**All components automatically update.** No CSS knowledge required.

### Step 2: Edit Content (In Elementor)

1. Click any section
2. Edit text, images, links
3. Everything else is locked (can't break the design)
4. Publish

### Step 3: Connect Forms

```bash
# Contact Form 7 (free)
# 1. Install plugin
# 2. Contact → New
# 3. Copy shortcode
# 4. Elementor → Shortcode widget → paste

# Or: Elementor Pro forms (built-in)
# 1. Add widget → Form
# 2. Configure fields + destination email
# 3. Done
```

---

## Component Reference

### Typography

All components use semantic typography classes:

| Class | Size | Weight | Usage |
|-------|------|--------|-------|
| `.t-display-xl` | 56px (web) / 48px (app) | 700 | Hero headlines |
| `.t-display-lg` | 48px / 40px | 700 | Page titles |
| `.t-heading-2xl` | 40px / 36px | 700 | Section titles |
| `.t-heading-lg` | 32px / 28px | 700 | Card titles |
| `.t-heading-md` | 28px / 24px | 700 | Subsection titles |
| `.t-body-lg` | 18px / 16px | 400 | Body text |
| `.t-body-md` | 16px / 14px | 400 | Default body |
| `.t-body-sm` | 14px / 12px | 400 | Captions |
| `.t-body-xs` | 12px / 11px | 400 | Small labels |

Difference between **web** (airy, larger) and **app** (compact, smaller).

### Colors

| Semantic | Token | Usage |
|----------|-------|-------|
| Accent | `--color-accent` | Primary buttons, links, highlights |
| Secondary | `--color-secondary` | Secondary buttons |
| Success | `--color-success` | Checkmarks, success messages |
| Warning | `--color-warning` | Alerts, caution states |
| Error | `--color-error` | Errors, destructive actions |
| Info | `--color-info` | Info badges |
| Foreground | `--color-fg` | Body text (main) |
| Background | `--color-bg` | Page background |
| Surface | `--color-surface` | Cards, sections |
| Surface Elevated | `--color-surface-elevated` | Modals, elevated cards |
| Muted | `--color-muted` | Secondary text, captions |
| Border | `--color-border` | Lines, dividers |

**All WCAG AA compliant** (4.5:1 contrast minimum).

### Spacing

| Token | Value |
|-------|-------|
| `--spacing-xs` | 4px |
| `--spacing-sm` | 8px |
| `--spacing-md` | 16px |
| `--spacing-lg` | 24px |
| `--spacing-xl` | 32px |
| `--spacing-2xl` | 48px |
| `--spacing-3xl` | 64px |
| `--spacing-4xl` | 80px |

---

## FAQ

### Q: Which Elementor version should I use?
**A:** v4+ (recommended) for full kit support and auto-sync. v3 works but requires manual customization. **Don't use v2.**

### Q: Can I use the web kit (light) and app kit (dark) on the same site?
**A:** Yes, but not recommended. Choose one per site. If you need both: use separate subdomain or WordPress multisite.

### Q: How do I change colors globally?
**A:** Override tokens in `@layer brand`. One change updates everywhere.

### Q: Can I add my own sections?
**A:** Yes. Build new sections in Elementor, save as local. Or copy a section template and modify.

### Q: How often do you update the templates?
**A:** Templates are versioned. New sections/widgets added quarterly. Breaking changes trigger major version bump + migration guide.

### Q: Do the templates work with page builders other than Elementor?
**A:** Templates are JSON-format Elementor-specific. But CSS components are universal — use with any builder by pasting the CSS and HTML structure.

### Q: How do I migrate from v3 to v4?
**A:** See `docs/handoff/WORDPRESS-ELEMENTOR-SETUP.md` → "Elementor v3→v4 Migration" section (coming soon).

### Q: Can I share site changes across multiple WordPress installs?
**A:** Yes. Export site as JSON → Import on another WordPress + Elementor. Token overrides travel too.

---

## Performance Tips

- **Lazy load images** → Elementor settings → Performance → enable
- **Optimize images** → Convert to WebP (free tools: squoosh.app, tinypng.com)
- **Cache plugin** → WP Rocket, Autoptimize, WP Super Cache
- **Minimize font weights** → Use 400 + 700 only
- **Avoid custom fonts** → System fonts are fastest

**Target:** Lighthouse score ≥ 90 (performance).

---

## Support

- **Bug report:** GitHub Issues on nordover-ui repo
- **Feature request:** Discussions on nordover-ui repo
- **Installation help:** WordPress forums, Elementor community
- **General questions:** See detailed docs in `ELEMENTOR-TEMPLATE-LIBRARY.md`

---

## Roadmap

### Q3 2026 (Done ✅)
- [x] 17 section templates
- [x] 2 kits (app, web)
- [x] 1 global widget (button)
- [x] 2 wireframes (landing, product)
- [x] WordPress setup guide
- [x] Pre-commit token hook

### Q4 2026 (In Progress 🔄)
- [ ] 4 more global widgets (card variants)
- [ ] 4 more wireframes (blog, contact, about, pricing)
- [ ] WooCommerce integration examples
- [ ] Elementor v3 migration guide
- [ ] Google Lighthouse scorecard

### Q1 2027 (Planned 📋)
- [ ] Figma UI Kit sync (tokens → Figma)
- [ ] Component library (Storybook)
- [ ] Accessibility audit report
- [ ] Customer case studies

---

## Version

- **Nordover:** 3.0
- **Elementor:** v4+ recommended, v3+ supported
- **WordPress:** 6.0+
- **Browser support:** Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

Last updated: 2026-06-12

---

**Ready to build?** → [Full Library Documentation](./ELEMENTOR-TEMPLATE-LIBRARY.md)
