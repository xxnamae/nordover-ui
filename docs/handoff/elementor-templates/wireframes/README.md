# Wireframe Templates — Full Page Layouts

Wireframe templates are pre-assembled page layouts combining multiple sections into complete, functional page templates. Use these as starting points for common page types.

## Available Templates

### 1. Landing Page
**File:** `landing-page.json`

Complete landing page with:
- Header (sticky navigation)
- Hero section (headline + CTA)
- Features grid (3-column)
- Testimonials carousel or grid
- CTA section
- Newsletter signup
- Footer

**Use case:** Product launches, event sign-ups, campaign pages
**Customization:** Update images, copy, CTAs, branding colors

### 2. Product / Service Page
**File:** `product-page.json`

Detailed product/service page with:
- Header (sticky navigation)
- Hero with product image/video
- Features section (3-column cards)
- Pricing comparison table
- FAQ accordion
- Social proof testimonials
- CTA + newsletter
- Footer

**Use case:** SaaS products, services, digital products
**Customization:** Replace product image, pricing, features, FAQs

### 3. Blog Template
**File:** `blog-template.json`

Blog index/archive page with:
- Header (sticky navigation)
- Hero with blog title
- Featured post card (large, above fold)
- 3-column post grid
- Pagination or load-more
- Sidebar (optional): tags, recent posts, newsletter signup
- Footer

**Use case:** Blog homes, archive pages, category pages
**Customization:** Connect to blog post data, customize sidebar

### 4. Contact Page
**File:** `contact-page.json`

Complete contact page with:
- Header (sticky navigation)
- Hero with headline
- Two-column layout:
  - Left: Contact form (name, email, message)
  - Right: Contact info (address, phone, email, hours)
- Map embed (optional)
- Team showcase (3-column)
- FAQ section
- Footer

**Use case:** Contact, inquiry, support pages
**Customization:** Update form destination, contact info, team members

### 5. About / Team Page
**File:** `about-page.json`

Company/team overview page with:
- Header (sticky navigation)
- Hero with headline + description
- Mission statement section
- Team grid (3+ members)
- Company stats (KPI counters)
- Company story / timeline
- Values section (3-column cards)
- CTA to contact or careers
- Footer

**Use case:** About pages, team pages, company profiles
**Customization:** Update mission, add/remove team members, customize story

### 6. Pricing Page
**File:** `pricing-page.json`

SaaS pricing page with:
- Header (sticky navigation)
- Pricing hero (headline, description)
- 3-tier pricing card grid
- Feature comparison table
- FAQ accordion
- CTA (upgrade / sign up)
- Footer

**Use case:** SaaS pricing, product tiers, subscription plans
**Customization:** Update pricing, features, comparison table

## Wireframe Assembly

Each wireframe combines multiple section templates from `docs/handoff/elementor-templates/sections/`.

To modify:
1. Import wireframe template into Elementor
2. Edit individual sections (they use shared section styles)
3. Sections automatically update styling via Nordover tokens

## Responsive Behavior

All wireframe templates are:
- **Mobile-first** — optimized for <576px
- **Tablet-ready** — tested at 576–1024px
- **Desktop-optimized** — fully responsive >1024px

Grid columns automatically reduce on mobile (4→2→1 columns).

## Customization

### Brand Colors
Override colors via `@layer brand`:

```css
@layer brand {
  :root {
    --color-accent: #your-brand-color;
    --color-surface: #your-surface;
    /* ...more */
  }
}
```

### Content
1. Replace placeholder images with your own (minimum 1200×628 recommended)
2. Update copy, headings, descriptions
3. Add real contact info, team members, testimonials
4. Connect forms to backend (Elementor Pro or Contact Form 7)

### Layout
- Add/remove sections as needed (delete full container)
- Reorder sections by dragging in Elementor
- Adjust spacing/padding via Elementor's responsive editor

## Performance Tips

- **Lazy load images** — enable in Elementor settings
- **Optimize images** — use WebP where supported
- **Minimize HTTP requests** — combine small images into sprites
- **Cache** — enable browser and server caching

## A11y Checklist

Before publishing:
- ✅ All images have alt text
- ✅ Headings follow hierarchy (h1→h2→h3)
- ✅ Form labels properly bound to inputs
- ✅ Links have descriptive text (not "click here")
- ✅ Color contrast ≥ 4.5:1 (WCAG AA)
- ✅ Interactive elements are keyboard accessible
- ✅ Page tested with screen reader (NVDA, JAWS, VoiceOver)

## Version Support

- **Elementor v4+:** Import JSON wireframe directly
- **Elementor v3:** Manually recreate sections from JSON structure (2–3 hours per wireframe)

For v3, follow the section templates in `docs/handoff/elementor-templates/sections/` as a guide.
