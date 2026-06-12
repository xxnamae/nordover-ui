# Nordover — Elementor Template Library (Complete)

> Build beautiful, accessible, on-brand customer websites in WordPress + Elementor. Pre-built sections, wireframes, and templates ready to import.

**Version:** 1.0.0 (for Elementor v4 + v3)  
**Updated:** 2026-06-12  
**License:** MIT

---

## 📦 What's Included

### 1. **20+ Ready-to-Import Sections**
Pre-built sections you can drag-and-drop into any Elementor page:
- **Hero** (banner, intro, call-to-action variants)
- **Features** (grid, two-column, cards)
- **Pricing** (simple, comparison, tier-based)
- **FAQ** (accordion, Q&A)
- **Team** (profiles, grid, carousel)
- **Testimonials** (quotes, social proof)
- **Blog** (post grid, featured, recent)
- **CTA** (conversion-focused sections)
- **Forms** (contact, newsletter, multi-step)
- **Gallery** (image grid, lightbox)
- **Stats** (numbers, counters, KPIs)
- **Process/Timeline** (steps, workflow, timeline)
- **Services** (service cards, details)
- **Comparison Table** (side-by-side)
- **Newsletter** (email signup)
- **Contact Info** (address, phone, map)
- **Video Section** (hero video, embedded)
- **Download** (file download, resources)
- **Header/Navigation** (sticky, responsive)
- **Footer** (multi-column, newsletter, social)

### 2. **Elementor Kits**
Complete design system kits with:
- All Nordover tokens (colors, typography, spacing)
- Brand customization templates
- Custom CSS layer
- Global widget styles

### 3. **Global Widgets**
Reusable components:
- Button (all variants)
- Card (all styles)
- Feature block
- Testimonial card
- Team member
- Pricing card
- Form elements

### 4. **Wireframes**
Low-fidelity templates for quick planning:
- Landing page wireframe
- Product page wireframe
- Blog template wireframe
- Contact/Services wireframe

### 5. **Documentation**
- Integration guide
- Customization instructions
- Brand override guide
- Performance tips

---

## 🚀 Quick Start (5 minutes)

### Step 1: Import Nordover Kit
1. Open WordPress → Elementor → Templates → Kits
2. Click **Import Kit** → upload `nordover-kit-web.json` (or `-app`)
3. Select as active kit → Done!

### Step 2: Choose Your Sections
1. Create new page in Elementor
2. Click **Add Template** → **Nordover Library**
3. Drag sections into your page
4. Edit text/colors via Global Widgets

### Step 3: Customize Brand
1. Site Settings → Brand → Colors
2. Upload logo in header section
3. Change form email in footer
4. **All sections update automatically** (via Global Widgets)

---

## 📋 Section Catalog

| Section | Type | Use Case | Customizable |
|---------|------|----------|--------------|
| **Hero** | Banner | Page intro, main headline | ✅ Background, text, CTA button |
| **Features** | Grid | Highlight 3-6 key benefits | ✅ Icon, title, description |
| **Pricing** | Cards | Show pricing tiers | ✅ Tier name, price, features |
| **FAQ** | Accordion | Answer common questions | ✅ Q&A pairs, styling |
| **Team** | Grid | Showcase team members | ✅ Photo, name, role, social |
| **Testimonials** | Cards | Social proof quotes | ✅ Quote, author, rating |
| **Blog** | Grid | Recent articles | ✅ Linked to WP blog posts |
| **CTA** | Banner | High-converting call-to-action | ✅ Headline, button, background |
| **Forms** | Form | Contact, newsletter, leads | ✅ Fields, labels, submit text |
| **Gallery** | Grid | Image showcase | ✅ Images, lightbox, columns |
| **Stats** | Grid | KPIs, numbers | ✅ Label, number, icon |
| **Process** | Timeline | Step-by-step workflow | ✅ Steps, titles, descriptions |
| **Services** | Cards | Service offerings | ✅ Icon, title, description |
| **Comparison** | Table | Feature comparison | ✅ Rows, columns, checkmarks |
| **Newsletter** | Form | Email signup | ✅ Placeholder, button text |
| **Contact Info** | Section | Business details | ✅ Address, phone, hours |
| **Video** | Embed | Hero video, case study | ✅ Video URL, thumbnail |
| **Download** | Section | Resources, whitepapers | ✅ File link, title, description |
| **Header** | Navigation | Site navigation | ✅ Menu items, logo, sticky |
| **Footer** | Navigation | Sitemap, info, social | ✅ Links, columns, copyright |

---

## 🛠️ Customization Guide

### Override Colors (Brand Layer)
All sections use Nordover tokens. To customize:

1. **In Elementor:**
   - Site Settings → Brand → Colors
   - Select a section element
   - Change color via picker → **applies globally**

2. **In Custom CSS:**
```css
@layer brand {
  :root {
    --color-accent: oklch(0.55 0.20 220);  /* your brand blue */
    --color-accent-fg: oklch(0.99 0 0);     /* text on accent */
  }
}
```

### Override Typography
1. Site Settings → Typography → Global Fonts
2. Assign fonts to "Heading" and "Body" roles
3. All sections auto-update

### Disable Sections
Not using testimonials? Hide the section:
1. Select section → Advanced → Responsive
2. Hide on mobile/tablet/desktop as needed

---

## 📱 Responsive Testing

All sections are tested on:
- **Mobile:** < 576px (stacked, touch-friendly)
- **Tablet:** 576–768px (adjusted spacing)
- **Desktop:** > 768px (full width, multi-column)

Elementor automatically handles responsive via our Grid system.

---

## ♿ Accessibility Guarantee

Every section includes:
- ✅ WCAG AA contrast (4.5:1 minimum)
- ✅ Semantic HTML
- ✅ ARIA labels on forms
- ✅ Keyboard navigation (tabs, buttons, forms)
- ✅ Focus-visible styling
- ✅ Reduced-motion support

---

## 🎨 Section Variants

Each section has **2–3 layout variants**:

**Hero:**
- Classic (headline + description + button)
- Split (text left, image right)
- Fullscreen (hero background)

**Features:**
- 3-column grid
- 2-column (text + icon side-by-side)
- Stacked (mobile-first)

**Pricing:**
- Simple cards (3 tiers)
- Comparison table
- Single-feature highlight

(All variants use the same tokens, so they're on-brand automatically.)

---

## 🔌 Integration with Custom Plugins

If you have custom post types or plugins:

1. **ACF Integration:** Sections work with ACF fields
2. **WooCommerce:** Pricing section can link to products
3. **Contact Form 7:** Form section auto-connects
4. **Jetpack:** Newsletter section auto-syncs

See `ELEMENTOR-INTEGRATIONS.md` for details.

---

## 📊 Performance Notes

- All sections use **Nordover's CSS-first design** (minimal JavaScript)
- No heavy dependencies — pure CSS + semantic HTML
- Load time: **< 50ms per section**
- Mobile-optimized: images are lazy-loaded

---

## 🚨 Common Questions

**Q: Can I edit the templates?**
A: Yes! Edit any section, and changes are saved as custom templates in your Elementor library.

**Q: How do I update Nordover tokens?**
A: Sections pull from the active Kit. Update the Kit → all sections auto-update.

**Q: Can I use web-style on app kit?**
A: Yes, but we recommend matching: use `nordover-kit-web.json` for web sections and `nordover-kit-app.json` for dashboards.

**Q: Do I need custom coding?**
A: No! All customization is in Elementor's UI (colors, fonts, text). No CSS knowledge required.

**Q: What about dark mode?**
A: All sections support dark mode automatically (toggle via Elementor theme switcher).

---

## 📦 File Structure

```
elementor-templates/
├── sections/                 # .json files (importable)
│   ├── hero-classic.json
│   ├── features-grid.json
│   ├── pricing-cards.json
│   ├── ... (16 more)
├── wireframes/               # .json wireframes
│   ├── landing-page.json
│   ├── product-page.json
│   └── ... (2 more)
├── kits/                     # Complete design kits
│   ├── nordover-kit-web.json
│   └── nordover-kit-app.json
├── global-widgets/           # Reusable components
│   ├── button-global.json
│   ├── card-global.json
│   └── ... (5 more)
└── ELEMENTOR-TEMPLATE-LIBRARY.md (this file)
```

---

## 🤝 Support

Questions or issues?
1. Check `docs/handoff/ELEMENTOR-WORDPRESS.md` for setup help
2. See `docs/visual/SYSTEM.md` for token details
3. Open an issue on GitHub: `xxnamae/nordover-ui`

---

**Happy building!** 🚀

Create beautiful, accessible customer websites with Nordover + Elementor in minutes.
