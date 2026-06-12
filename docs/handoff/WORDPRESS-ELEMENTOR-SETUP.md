# WordPress + Elementor Integration Guide

Rask oppsetting av kundenesider på WordPress med Elementor og Nordover Design System.

## Oversikt

Denne veiledningen viser hvordan du setter opp WordPress + Elementor + Nordover for å bygge kundesider med "global standard" på kort tid.

## System Requirements

### Server/Hosting
- **PHP:** 7.4 eller høyere (anbefalt 8.1+)
- **WordPress:** 6.0 eller høyere
- **Elementor:** v4.0+ (eller v3.15+ for eldre installasjoner)
- **Memory limit:** 256 MB (anbefalt 512 MB+)
- **SSL:** Påkrevd (HTTPS)

### Plugins Påkrevd
- **Elementor** (free eller Pro)
- **Nordover Tokens CSS** (eget plugin eller lastet som stylesheet)
- **WooCommerce** (hvis e-handel ønskes)
- **Contact Form 7** (eller Elementor Pro forms)
- **Yoast SEO** (anbefalt for SEO)

### Plugins Anbefalt
- **Jetpack** (CDN, performance, backup)
- **WP Rocket** eller **Autoptimize** (caching, optimization)
- **Redirection** (URL management, 301 redirects)
- **Better Search and Replace** (batch content updates)

## Steg 1: Fresh WordPress Install + Nordover Setup

```bash
# 1. Create fresh WordPress site (via hosting provider or local dev)
wp-cli site create --title="Brand Name"

# 2. Install Elementor
wp plugin install elementor --activate

# 3. Download Nordover CSS
# Fra: https://github.com/xxnamae/nordover-ui/tree/main/docs/visual/tokens
wget -O wp-content/themes/custom/nordover-tokens-app.css \
  https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/tokens/tokens-app.css

wget -O wp-content/themes/custom/nordover-components-app.css \
  https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/visual/components/components-app.css

# 4. Register stylesheets in functions.php
function enqueue_nordover_styles() {
  wp_enqueue_style('nordover-tokens', get_template_directory_uri() . '/nordover-tokens-app.css', array(), '3.0.0');
  wp_enqueue_style('nordover-components', get_template_directory_uri() . '/nordover-components-app.css', array('nordover-tokens'), '3.0.0');
}
add_action('wp_enqueue_scripts', 'enqueue_nordover_styles');
```

## Steg 2: Import Elementor Kit

Elementor Kits eksporterer alle globale variabler (farger, typografi, spacing) for hele nettstedet.

### For Elementor v4+

```bash
# 1. Åpne WordPress admin → Elementor → Settings → Kits
# 2. Klikk "Import Kit"
# 3. Velg: docs/handoff/elementor-templates/kits/nordover-kit-app.json
# 4. Klikk "Import"

# Kit installeres automatisk — alle farger/typografi synkroniserer globalt
```

### For Elementor v3

```bash
# Elementor v3 har begrenset kit-støtte
# I stedet:
# 1. Åpne Elementor Library → Add "Global Widget"
# 2. Kopier CSS fra kit-filen inn i custom CSS
# 3. Definér globale farger manuelt i Elementor Settings
```

## Steg 3: Import Section Templates

Section templates er ferdige blokker (hero, features, pricing, footer osv.) som kan brukes direkte.

### For Elementor v4+

```bash
# 1. Opprett ny side
# 2. Åpne Elementor editor
# 3. Library → "Import from JSON"
# 4. Velg: docs/handoff/elementor-templates/sections/hero-classic.json
# 5. Dra inn i siden
# 6. Gjenta for alle sections du trenger (features, cta, footer osv.)
```

### For Elementor v3

```bash
# Manuell prosess:
# 1. Åpne hero-classic.json i editor
# 2. Kopier HTML-strukturen
# 3. Kopier CSS-klassene
# 4. I Elementor v3: Custom HTML → Paste
# 5. Lik opp stilene ved å verifisere CSS-klassene
```

## Steg 4: Use Wireframe Templates for Full Pages

Wireframe templates kombinerer multiple sections inn i fullstendige sider (landing page, product page, osv.).

```bash
# 1. Lag ny side (f.eks. "Landing Page")
# 2. Elementor editor → Library → Import from JSON
# 3. Velg: docs/handoff/elementor-templates/wireframes/landing-page.json
# 4. Alle seksjoner importeres og er klare til redigering
# 5. Endre tekst, bilder, linker basert på kundens merkevare
```

## Steg 5: Customize via @layer brand

Alle komponenter bruker CSS-variabler som er lett å overstyre.

### I theme functions.php eller custom CSS:

```css
@layer brand {
  :root {
    /* Override primary color */
    --color-accent: #your-brand-color;
    
    /* Override secondary colors */
    --color-success: #28a745;
    --color-error: #dc3545;
    --color-warning: #ffc107;
    
    /* Override typography */
    --font-sans: 'Your Font Family', sans-serif;
    
    /* Override spacing if needed */
    --spacing-base: 4px;
  }
}
```

Alle komponenter oppdateres automatisk via CSS-kaskade.

## Steg 6: Setup Forms + Email Integration

### Contact Form 7 (gratis)

```bash
wp plugin install contact-form-7 --activate

# 1. Contact → Add New
# 2. Velg "Nordover Contact Form" template
# 3. Endre recipient email
# 4. Kopier shortcode
# 5. Elementor → Shortcode widget → Paste
```

### Elementor Pro Forms

```bash
# Elementor Pro har innebygd form builder
# 1. Elementor editor → Add Widget → Form
# 2. Legg til felt: name, email, subject, message
# 3. Actions → Email → Endre "to" address
# 4. Styling bruker globale variabler automatisk
```

### Integration med Email Services

```php
// ExampleintegrationmedMailchimp (via plugin)
add_action('cf7_after_insert_post', function($contact_form) {
  // Sync Form 7 submissions to Mailchimp
  // Bruk plugin: "Contact Form 7 to Mailchimp"
});
```

## Steg 7: Setup Navigation Menus

```bash
# 1. WordPress admin → Appearance → Menus
# 2. Create "Main Menu"
# 3. Add pages: Home, About, Services, Blog, Contact
# 4. Set as "Primary Menu" under Display Location
# 5. Elementor header bruker denne menyen automatisk
```

## Steg 8: Configure SEO

### Yoast SEO Setup

```bash
wp plugin install wordpress-seo --activate

# 1. Yoast → General → Features → Enable
# 2. Search Appearance → Snippets preview
# 3. Readability → Set target keyword per page
# 4. Set page type (Homepage, About, Services, etc.)
```

### Schema.org Markup

```php
// I Nordover komponentene er schema allerede inkludert:
// - Product (for product pages)
// - FAQPage (for FAQ sections)
// - BreadcrumbList (for breadcrumbs)
// - Organization (i footer)
```

## Steg 9: Performance Optimization

### Enable Caching

```php
// Add to wp-config.php
define('WP_CACHE', true);

// Install caching plugin:
wp plugin install wp-rocket --activate
// eller: autoptimize, wp-super-cache
```

### Lazy Load Images

```php
// Elementor automatisk lazy-loader bilder
// Settings → Performance → Image Optimization → Enable
```

### CDN Setup (anbefalt)

```bash
wp plugin install jetpack --activate
# Jetpack → Settings → Performance → Automatic CDN
# Serverer statisk innhold (CSS, JS, images) via CDN
```

## Steg 10: Testing + QA

### Responsiveness Testing

```bash
# Chrome DevTools
1. F12 → Toggle Device Toolbar (Ctrl+Shift+M)
2. Test breakpoints: 375px (mobile), 768px (tablet), 1024px (desktop)
3. Verify: text readability, button sizes, image scaling
```

### Accessibility Testing

```bash
# Axe DevTools (Chrome extension)
1. Install: https://www.deque.com/axe/devtools/
2. Scan hver side
3. Fix violations (contrast, ARIA labels, keyboard nav)

# Manual checks
- Keyboard navigation (Tab through all interactive elements)
- Screen reader test (NVDA Windows, VoiceOver Mac)
- Color contrast (≥4.5:1 for normal text)
```

### Performance Testing

```bash
# Google PageSpeed Insights
https://pagespeed.web.dev/

# Target scores:
- Performance: ≥90
- Accessibility: ≥90
- Best Practices: ≥90
- SEO: ≥90
```

## Steg 11: Deployment Checklist

Før go-live:

- [ ] DNS-oppkobling ferdig (domain points to hosting)
- [ ] SSL-sertifikat installert (HTTPS) ✅
- [ ] Alle sider testet på mobil/tablet/desktop
- [ ] Skjemaer funker og sender e-post
- [ ] Bilder optimisert (< 100 KB per bilde)
- [ ] Cache aktivert (Elementor + Server + CDN)
- [ ] Backup konfigurert (daglig eller per endring)
- [ ] SEO meta tags på plass (title, description)
- [ ] Schema.org markup validert (https://schema.org/validator)
- [ ] Accessibility report ≥90% (Axe, WAVE, Lighthouse)
- [ ] Performance rapport ≥90% (PageSpeed, GTmetrix)

## Steg 12: Post-Launch Monitoring

### Weekly Tasks
- Monitor uptime (StatusCake, Uptime Robot)
- Check error logs (WordPress debug log)
- Verify form submissions arrive in email
- Spot-check page rendering

### Monthly Tasks
- Update WordPress, plugins, theme
- Review security (WordFence, Sucuri)
- Analyze traffic (Google Analytics 4)
- Review search rankings (Yoast, Google Search Console)

### Quarterly Tasks
- Content audit (outdated pages, broken links)
- Performance audit (Lighthouse, PageSpeed)
- Accessibility audit (WAVE, Axe DevTools)
- Security audit (plugin vulnerabilities)

## Troubleshooting

### Nordover CSS Not Loading

```bash
# Problem: Styles not applying
# Solution:
1. Verify CSS file paths in functions.php
2. Check: wp-content/themes/custom/nordover-*.css exists
3. Disable plugins one by one to find conflicts
4. Check browser console for 404 errors
```

### Elementor Kit Not Syncing

```bash
# Problem: Global color changes don't apply
# Solution v4:
1. Elementor → Kits → verify kit is active
2. Clear browser cache (Ctrl+Shift+Del)
3. WordPress admin → Settings → Permalinks → Re-save

# Solution v3:
1. Kits not fully supported — manually update CSS variables
2. Use custom CSS section in Elementor
```

### Form Submissions Not Sending

```bash
# Problem: Forms submitted but no email received
# Solution:
1. Check: Settings → General → Email address is valid
2. Verify: SMTP configured on hosting (often required)
3. Contact Form 7 → Check "Debug" log
4. Look in spam/junk folder
5. Test with plugin: "Post SMTP Mailer"
```

### Performance Issues

```bash
# Problem: Page loads slow
# Solution:
1. Identify bottleneck: PageSpeed Insights
2. If images: compress, convert to WebP
3. If plugins: disable unused plugins (especially sliders, lightboxes)
4. If fonts: use system fonts or google-fonts-subset
5. Enable caching plugin: WP Rocket, Autoptimize
```

## Best Practices

### Content
- ✅ Use descriptive headings (h1→h2→h3 hierarchy)
- ✅ Keep paragraphs under 3 sentences
- ✅ Use bullet lists for scannable content
- ✅ Include images every 300 words
- ✅ Use calls-to-action (CTA) every 2–3 sections

### Branding
- ✅ Use consistent color palette (override via @layer brand)
- ✅ Use 1–2 font families max
- ✅ Maintain whitespace (breathing room)
- ✅ Use icons consistently (from same set)
- ✅ Logo in header + footer

### Conversion
- ✅ CTA buttons above fold (hero)
- ✅ Form fields minimal (max 5 fields)
- ✅ Customer testimonials visible
- ✅ Trust badges (security, awards)
- ✅ Clear value proposition (hero section)

### SEO
- ✅ One h1 per page
- ✅ Descriptive page titles (50–60 chars)
- ✅ Meta descriptions (120–160 chars)
- ✅ Internal linking (3–5 per page)
- ✅ Image alt text (descriptive, include keyword)

## Support Resources

- **Nordover Docs:** https://github.com/xxnamae/nordover-ui/docs
- **Elementor Docs:** https://elementor.com/help/
- **WordPress Docs:** https://wordpress.org/support/
- **Community Forum:** https://wordpress.org/support/forums/

## Version Timeline

- **Elementor v4:** Latest, full Nordover support ✅
- **Elementor v3:** Supported, manual customization required ⚠️
- **Elementor v2:** Not supported ❌

For v3 users: plan migration to v4 within 12 months (security/performance benefits).

---

**Last updated:** 2026-06-12
**Nordover version:** 3.0
