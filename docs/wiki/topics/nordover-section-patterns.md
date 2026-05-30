# Section-patterns (web-rammeverk)

Composite section-level patterns for marketing/landingssider. Hver komponent er en seksjon av en side (Hero, Feature Grid, CTA, FAQ, Footer, etc.) som komponerer fra primitivene og batch 1/1b-patterns.

**Primært for `tokens-web`** (Scandi-min editorial), men flere fungerer også i `tokens-app`-kontekst (Stats-strip, CTA, Footer).

**Responsivitet** er gjennomgående: alle patterns er fluid og kollapser elegant fra desktop til tablet til mobil. Hovedmekanisme: `Grid auto-fit` + `Container` + `clamp()`-tokens vi allerede har.

Se [decision 2026-05-27 — section-patterns-web](../decisions/2026-05-27-section-patterns-web.md).

---

## 1. Hero

Fire varianter dekker marketing-bruk.

### 1a. Hero-Centered (default)

Sentrert display + subtittel + CTA-par. Mest brukt.

**Props:** `eyebrow?`, `title`, `description?`, `primaryCTA`, `secondaryCTA?`, `bg?` (`default` | `gradient` | `subtle`).

**CSS:**
```css
@utility hero-centered {
  position: relative;
  padding-block: clamp(5rem, 14vw, 12rem);
  text-align: center;
  overflow: hidden;
}

@utility hero-centered-bg-gradient::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--gradient-radial-accent);
  pointer-events: none;
}

@utility hero-centered-eyebrow {
  /* Bruker .text-eyebrow */
  margin-bottom: var(--gap-component);
}

@utility hero-centered-title {
  /* Bruker .text-display-lg eller .text-display-xl */
  max-width: 20ch;
  margin-inline: auto;
}

@utility hero-centered-description {
  font-size: var(--text-lg);
  color: var(--color-muted);
  max-width: 50ch;
  margin-inline: auto;
  margin-top: clamp(1rem, 2vw, 2rem);
  text-wrap: pretty;
}

@utility hero-centered-actions {
  margin-top: clamp(1.5rem, 3vw, 2.5rem);
}
```

**Bruk:**
```jsx
<section className="hero-centered hero-centered-bg-gradient">
  <Container>
    <p className="text-eyebrow hero-centered-eyebrow">Lansert i 2026</p>
    <h1 className="text-display-xl hero-centered-title">
      Skandinavisk minimalisme, komponert i tokens.
    </h1>
    <p className="hero-centered-description">
      Et komplett rammeverk for marketingsider og webapplikasjoner.
    </p>
    <Cluster className="hero-centered-actions" justify="center" gap="tight">
      <Button size="lg">Kom i gang</Button>
      <Button size="lg" variant="secondary">Les mer</Button>
    </Cluster>
  </Container>
</section>
```

### 1b. Hero-Split

Display + tekst på venstre, media (bilde/video/illustrasjon) på høyre. Mobil: stables.

**Props:** `eyebrow?`, `title`, `description?`, `primaryCTA`, `secondaryCTA?`, `media` (node — img/video/komponent), `mediaPosition?` (`right` | `left`).

**CSS:**
```css
@utility hero-split {
  padding-block: clamp(4rem, 10vw, 8rem);
  container-type: inline-size;
}

@utility hero-split-grid {
  display: grid;
  gap: clamp(2rem, 6vw, 5rem);
  align-items: center;
  grid-template-columns: 1fr;
}

@container (min-width: 48rem) {
  @utility hero-split-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@utility hero-split-media-left .hero-split-grid > :first-child {
  order: 2;
}
```

**Bruk:**
```jsx
<section className="hero-split">
  <Container>
    <div className="hero-split-grid">
      <div>
        <p className="text-eyebrow">For borettslag</p>
        <h1 className="text-display-lg">Vedlikehold gjort enkelt.</h1>
        <p className="text-body-lg" style={{ color: 'var(--color-muted)', marginTop: '1.5rem' }}>
          Omhu samler alle vedlikeholdssaker på ett sted.
        </p>
        <Cluster gap="tight" style={{ marginTop: '2rem' }}>
          <Button size="lg">Prøv gratis</Button>
          <Button size="lg" variant="link">Se demo</Button>
        </Cluster>
      </div>
      <div>
        <img src="/dashboard-preview.png" alt="Omhu dashboard" />
      </div>
    </div>
  </Container>
</section>
```

### 1c. Hero-Image (full-bleed bg + venstre/høyre/sentrert tekst)

For brand-statement-helter med stort foto/video. Tekst plassert i overlay over bilde med gradient for lesbarhet.

**Props:** `image` (URL eller node), `align` (`left` | `right` | `center`, default `left`), `eyebrow?`, `title`, `description?`, `primaryCTA`, `secondaryCTA?`, `minHeight?` (default `60vh`).

**CSS:**
```css
@utility hero-image {
  position: relative;
  min-height: 60vh;
  border-radius: var(--radius-lg);
  overflow: hidden;
  display: flex;
  align-items: center;
  background-size: cover;
  background-position: center;
}

@utility hero-image-overlay-left {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.45) 35%, transparent 70%);
}
@utility hero-image-overlay-right {
  position: absolute;
  inset: 0;
  background: linear-gradient(to left, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.45) 35%, transparent 70%);
}
@utility hero-image-overlay-center {
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.6) 100%);
}

@utility hero-image-content {
  position: relative;
  z-index: 2;
  color: white;
  padding: clamp(2rem, 5vw, 4rem) clamp(1.5rem, 4vw, 3rem);
  max-width: 36rem;
  width: 100%;
}

@utility hero-image-align-left .hero-image-content { margin-right: auto; }
@utility hero-image-align-right .hero-image-content { margin-left: auto; text-align: right; }
@utility hero-image-align-right .hero-image-content > * { margin-left: auto; }
@utility hero-image-align-center { justify-content: center; }
@utility hero-image-align-center .hero-image-content { text-align: center; }

/* Mobile: text-overlay blir alltid bottom-gradient + venstrejustert (uansett align-prop) */
@media (max-width: 48rem) {
  @utility hero-image-overlay-left,
  @utility hero-image-overlay-right {
    background: linear-gradient(to bottom, rgba(0,0,0,0.3), rgba(0,0,0,0.7));
  }
  @utility hero-image-align-right .hero-image-content { text-align: left; }
  @utility hero-image-align-right .hero-image-content > * { margin-left: 0; }
}
```

**Bruk:**
```jsx
<section
  className="hero-image hero-image-align-left"
  style={{ backgroundImage: `url(${imageSrc})` }}
>
  <div className="hero-image-overlay-left" />
  <Container>
    <div className="hero-image-content">
      <p className="text-eyebrow" style={{ color: 'rgba(255,255,255,0.7)' }}>{eyebrow}</p>
      <h1 className="text-display-md">{title}</h1>
      <p className="text-body-lg">{description}</p>
      <Cluster gap="tight">
        <Button size="lg" style={{ background: 'white', color: 'var(--color-fg)' }}>
          {primaryCTA}
        </Button>
      </Cluster>
    </div>
  </Container>
</section>
```

**Variant-bruk:**
- `align="left"` (default) — vanligst, naturlig leseretning. Bilde har "negative space" til høyre.
- `align="right"` — for variasjon eller når bilde-fokus er til venstre.
- `align="center"` — sentrale brand-statements, korte budskap, full-bleed.

**Performance:**
- Bruk `<img>` med `loading="eager"` for above-the-fold + `srcset` for responsive bilder.
- `background-image` er fine for små bilder eller når du trenger ren CSS.
- Mobile: vurder mindre bilde-versjon via `<picture>` for å spare data.

**A11y:**
- Tekst over bilde må ha kontrast — overlay-gradient sikrer dette.
- Hvis bildet er dekorativt: `aria-hidden="true"`. Hvis innholdsbærende: meningsfull `alt`.

**Knapper på mørk bg:** Primary-knapp får hvit bg + mørk tekst (overstyring i komponentet). Secondary/ghost forblir transparent med hvit tekst.

### 1c. Hero-Editorial

Asymmetrisk, dramatisk. Display tar all bredde, supportekst i kolonne under.

**CSS:**
```css
@utility hero-editorial {
  padding-block: clamp(6rem, 18vw, 14rem);
}

@utility hero-editorial-title {
  /* text-display-xl eller text-8xl */
  letter-spacing: -0.04em;
  line-height: 0.9;
  max-width: 18ch;
}

@utility hero-editorial-meta {
  margin-top: clamp(3rem, 8vw, 6rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 3rem);
  grid-template-columns: 1fr;
}

@container (min-width: 48rem) {
  @utility hero-editorial-meta {
    grid-template-columns: 2fr 1fr 1fr;
  }
}
```

**Bruk:**
```jsx
<section className="hero-editorial">
  <Container>
    <p className="text-eyebrow">Capsule 01</p>
    <h1 className="text-display-xl hero-editorial-title">Designet for stillhet.</h1>
    <div className="hero-editorial-meta">
      <p className="text-body-lg">Lange linjer, ren typografi, ingen unødvendige elementer. En markedside som lar innholdet bære.</p>
      <div>
        <p className="text-caption">Lansert</p>
        <p className="text-body">2026-05</p>
      </div>
      <div>
        <p className="text-caption">Stack</p>
        <p className="text-body">Nordover · Next.js · Payload</p>
      </div>
    </div>
  </Container>
</section>
```

---

## 2. Feature Grid

Auto-responsiv grid av feature-kort. Hver karte: ikon + heading + beskrivelse + valgfri link.

**Props (Feature):** `icon`, `title`, `description`, `link?`.

**CSS:**
```css
@utility feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(20rem, 100%), 1fr));
  gap: clamp(1.5rem, 3vw, 2.5rem);
}

@utility feature-card {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  padding: var(--gap-component);
}

@utility feature-card-bordered {
  border: var(--border-card);
  border-radius: var(--radius-lg);
  padding: clamp(1.5rem, 3vw, 2rem);
}

@utility feature-card-icon {
  width: 2.5rem;
  height: 2.5rem;
  color: var(--color-accent);
  margin-bottom: var(--gap-tight);
}

@utility feature-card-title {
  /* .text-heading-sm */
}

@utility feature-card-description {
  color: var(--color-muted);
  text-wrap: pretty;
}
```

**Bruk:**
```jsx
<Section>
  <Container>
    <Stack gap="component">
      <div style={{ textAlign: 'center' }}>
        <p className="text-eyebrow">Features</p>
        <h2 className="text-display-md">Alt du trenger.</h2>
      </div>
      <div className="feature-grid">
        <article className="feature-card feature-card-bordered">
          <Sparkle className="feature-card-icon" />
          <h3 className="text-heading-sm">AI-drevet</h3>
          <p className="feature-card-description">Auto-kategoriserer henvendelser og foreslår løsninger.</p>
        </article>
        {/* ... flere kort */}
      </div>
    </Stack>
  </Container>
</Section>
```

---

## 3. CTA Section

Konverterings-fokus seksjon. Sentrert, ofte med gradient eller subtle bg. Display + beskrivelse + CTA-par.

**CSS:**
```css
@utility cta-section {
  position: relative;
  padding-block: clamp(4rem, 10vw, 8rem);
  text-align: center;
  overflow: hidden;
}

@utility cta-section-card {
  position: relative;
  background: var(--color-subtle);
  border-radius: var(--radius-xl);
  padding: clamp(3rem, 8vw, 6rem) clamp(1.5rem, 4vw, 4rem);
  overflow: hidden;
}

@utility cta-section-card::before {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--gradient-radial-accent);
  pointer-events: none;
}

@utility cta-section-title {
  /* .text-display-md eller .text-display-lg */
  max-width: 18ch;
  margin-inline: auto;
  position: relative;
}

@utility cta-section-description {
  color: var(--color-muted);
  max-width: 50ch;
  margin-inline: auto;
  margin-top: 1.5rem;
  position: relative;
}

@utility cta-section-actions {
  margin-top: clamp(1.5rem, 3vw, 2.5rem);
  position: relative;
}
```

**Bruk:**
```jsx
<section className="cta-section">
  <Container size="narrow">
    <div className="cta-section-card">
      <h2 className="text-display-md cta-section-title">Klar til å komme i gang?</h2>
      <p className="cta-section-description">14 dager gratis prøve. Ingen kortinfo nødvendig.</p>
      <Cluster className="cta-section-actions" justify="center" gap="tight">
        <Button size="lg">Start gratis</Button>
        <Button size="lg" variant="ghost">Snakk med oss</Button>
      </Cluster>
    </div>
  </Container>
</section>
```

---

## 4. FAQ (Accordion-basert)

Single-open accordion (kun ett FAQ-spørsmål åpent av gangen). Smooth height-animasjon via CSS-only (`details`/`summary`-element).

**Props (FAQ-item):** `question`, `answer`, `defaultOpen?`.

**CSS (bruker native `<details>`):**
```css
@utility faq-list {
  display: flex;
  flex-direction: column;
}

@utility faq-item {
  border-bottom: var(--border-divider);
  padding-block: 1.25rem;
}

@utility faq-item-summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  cursor: pointer;
  font-size: var(--text-lg);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  list-style: none;
  padding-block: 0.5rem;
}

@utility faq-item-summary::-webkit-details-marker { display: none; }

@utility faq-item-summary::after {
  content: "";
  width: 1rem;
  height: 1rem;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'><path d='M4 6l4 4 4-4' stroke='currentColor' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>");
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  flex-shrink: 0;
  transition: transform var(--duration-base) var(--ease-out);
}

@utility faq-item[open] .faq-item-summary::after {
  transform: rotate(180deg);
}

@utility faq-item-answer {
  padding-top: var(--gap-tight);
  padding-bottom: 0.5rem;
  color: var(--color-muted);
  font-size: var(--text-body);
  line-height: 1.6;
  text-wrap: pretty;
  max-width: 75ch;
}
```

**Bruk:**
```jsx
<Section>
  <Container size="prose">
    <Stack gap="component">
      <h2 className="text-display-md">Vanlige spørsmål</h2>
      <div className="faq-list">
        <details className="faq-item" open>
          <summary className="faq-item-summary">Hvordan kommer jeg i gang?</summary>
          <p className="faq-item-answer">Opprett en konto, koble til betalingsmetode, og du er klar.</p>
        </details>
        <details className="faq-item">
          <summary className="faq-item-summary">Kan jeg avbryte når som helst?</summary>
          <p className="faq-item-answer">Ja, ingen bindingstid.</p>
        </details>
      </div>
    </Stack>
  </Container>
</Section>
```

**Begrensning:** native `<details>` har ikke smooth height-animasjon i alle browsere (CSS-only). For premium-følelse kan vi senere bytte til JS-basert med `useState` + `max-height`-animasjon eller Radix Accordion. For 2026-baseline er native god nok.

---

## 5. Footer

Multi-column med logo + lenke-kolonner + bottom-bar.

**Sections:** brand-column (logo + tagline + sosiale), 2-4 link-columns, bottom-bar (copyright + ekstra-lenker).

**CSS:**
```css
@utility site-footer {
  padding-block: clamp(3rem, 6vw, 5rem) clamp(2rem, 4vw, 3rem);
  border-top: var(--border-divider);
  color: var(--color-muted);
}

@utility site-footer-grid {
  display: grid;
  gap: clamp(2rem, 4vw, 3rem);
  grid-template-columns: 1fr;
}

@container (min-width: 40rem) {
  @utility site-footer-grid {
    grid-template-columns: 2fr 1fr 1fr 1fr;
  }
}

@utility site-footer-brand {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility site-footer-column {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility site-footer-column-title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  margin-bottom: var(--gap-tight);
}

@utility site-footer-link {
  font-size: var(--text-sm);
  color: var(--color-muted);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}
@utility site-footer-link:hover {
  color: var(--color-fg);
}

@utility site-footer-bottom {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-top: clamp(2rem, 4vw, 3rem);
  padding-top: clamp(1.5rem, 3vw, 2rem);
  border-top: var(--border-divider);
  font-size: var(--text-sm);
}
```

**Bruk:**
```jsx
<footer className="site-footer">
  <Container>
    <div className="site-footer-grid">
      <div className="site-footer-brand">
        <Logo />
        <p className="text-body-sm">Et komplett rammeverk for moderne nettsider og apper.</p>
        <Cluster gap="tight">
          <a href="..." className="site-footer-link"><TwitterIcon /></a>
          <a href="..." className="site-footer-link"><LinkedInIcon /></a>
        </Cluster>
      </div>
      <div className="site-footer-column">
        <p className="site-footer-column-title">Produkt</p>
        <a className="site-footer-link" href="/features">Features</a>
        <a className="site-footer-link" href="/priser">Priser</a>
      </div>
      <div className="site-footer-column">
        <p className="site-footer-column-title">Selskap</p>
        <a className="site-footer-link" href="/om">Om oss</a>
        <a className="site-footer-link" href="/kontakt">Kontakt</a>
      </div>
      <div className="site-footer-column">
        <p className="site-footer-column-title">Juridisk</p>
        <a className="site-footer-link" href="/personvern">Personvern</a>
        <a className="site-footer-link" href="/vilkar">Vilkår</a>
      </div>
    </div>
    <div className="site-footer-bottom">
      <p>© 2026 Nordover</p>
      <p>Laget i Norge 🇳🇴</p>
    </div>
  </Container>
</footer>
```

---

## 6. Header / Site Nav (marketing)

Sticky top-nav med glass-effekt + logo + nav-links + CTA. Mobile: hamburger-meny som åpner full-screen overlay.

**Props:** `logo`, `links` (array), `primaryCTA`, `secondaryCTA?`.

**CSS:**
```css
@utility site-header {
  position: sticky;
  top: 0;
  z-index: var(--z-sticky);
  padding-block: 0.75rem;
  padding-inline: var(--page-padding);
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border-bottom: var(--glass-border);
  transition: padding var(--duration-base) var(--ease-out);
}

@utility site-header-logo {
  flex-shrink: 0;
}

@utility site-header-nav {
  display: none;
  align-items: center;
  gap: 2rem;
}

@container (min-width: 48rem) {
  @utility site-header-nav {
    display: flex;
  }
}

@utility site-header-nav-link {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}
@utility site-header-nav-link:hover {
  color: var(--color-muted);
}

@utility site-header-actions {
  display: flex;
  align-items: center;
  gap: var(--gap-tight);
}

@utility site-header-mobile-toggle {
  display: inline-flex;
}
@container (min-width: 48rem) {
  @utility site-header-mobile-toggle {
    display: none;
  }
}

@utility site-header-mobile-menu {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  background: var(--color-bg);
  padding: var(--page-padding);
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
}
```

**Mobile-menu-strategi:** full-screen overlay (ikke drawer). Enklere på små viewports, mer fokus på lenker.

**Bruk:**
```jsx
<header className="site-header">
  <Logo className="site-header-logo" />
  <nav className="site-header-nav">
    <a className="site-header-nav-link" href="/features">Features</a>
    <a className="site-header-nav-link" href="/priser">Priser</a>
    <a className="site-header-nav-link" href="/om">Om</a>
  </nav>
  <div className="site-header-actions">
    <Button variant="ghost" size="sm" href="/login">Logg inn</Button>
    <Button size="sm" href="/start">Kom i gang</Button>
    <Button iconOnly variant="ghost" className="site-header-mobile-toggle" aria-label="Meny">
      <MenuIcon />
    </Button>
  </div>
</header>
```

---

## 7. Logo Cloud

Horisontal strip av kunde/partner-logoer. Ofte grayscale med color-on-hover, eller alltid muted.

**Props:** `logos` (array av { src, alt, href? }), `label?` ("Brukt av:").

**CSS:**
```css
@utility logo-cloud {
  padding-block: clamp(3rem, 6vw, 5rem);
}

@utility logo-cloud-label {
  /* .text-eyebrow, centered */
  text-align: center;
  margin-bottom: clamp(1.5rem, 3vw, 2.5rem);
}

@utility logo-cloud-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(8rem, 1fr));
  gap: clamp(1.5rem, 4vw, 3rem);
  align-items: center;
  justify-items: center;
}

@utility logo-cloud-item {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  max-height: 2rem;
  opacity: 0.6;
  filter: grayscale(100%);
  transition: opacity var(--duration-fast) var(--ease-out),
              filter var(--duration-fast) var(--ease-out);
}

@utility logo-cloud-item:hover {
  opacity: 1;
  filter: grayscale(0%);
}

@utility logo-cloud-item img {
  max-height: 100%;
  width: auto;
  object-fit: contain;
}
```

**Bruk:**
```jsx
<section className="logo-cloud">
  <Container>
    <p className="text-eyebrow logo-cloud-label">Brukt av norske borettslag</p>
    <div className="logo-cloud-grid">
      <a className="logo-cloud-item"><img src="/logos/usbl.svg" alt="USBL" /></a>
      <a className="logo-cloud-item"><img src="/logos/obos.svg" alt="OBOS" /></a>
      <a className="logo-cloud-item"><img src="/logos/bate.svg" alt="Bate" /></a>
      <a className="logo-cloud-item"><img src="/logos/nbbl.svg" alt="NBBL" /></a>
    </div>
  </Container>
</section>
```

---

## 8. Pricing

3-kolonne grid (eller 2/4) med priskort. Midt-kort markert "anbefalt".

**Props (PriceCard):** `tier`, `price`, `period?`, `description`, `features` (array), `cta`, `highlighted?`.

**CSS:**
```css
@utility pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(18rem, 100%), 1fr));
  gap: clamp(1.5rem, 3vw, 2rem);
  align-items: stretch;
}

@utility price-card {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
  padding: clamp(1.5rem, 3vw, 2.5rem);
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-lg);
}

@utility price-card-highlighted {
  border-color: var(--color-fg);
  position: relative;
  background: var(--color-subtle);
}

@utility price-card-highlighted::before {
  content: "Anbefalt";
  position: absolute;
  top: -0.75rem;
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-accent);
  color: var(--color-accent-fg);
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
  padding-block: 0.25rem;
  padding-inline: 0.625rem;
  border-radius: var(--radius-full);
}

@utility price-card-tier {
  font-size: var(--text-lg);
  font-weight: var(--font-weight-semibold);
}

@utility price-card-price {
  font-family: var(--font-display);
  font-size: var(--text-5xl);
  font-weight: var(--font-weight-display);
  letter-spacing: var(--tracking-tight);
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

@utility price-card-period {
  color: var(--color-muted);
  font-size: var(--text-base);
  font-weight: var(--font-weight-normal);
}

@utility price-card-description {
  color: var(--color-muted);
  font-size: var(--text-body);
}

@utility price-card-features {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  flex: 1;
}

@utility price-card-features li {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  font-size: var(--text-sm);
}

@utility price-card-features li::before {
  content: "✓";
  color: var(--color-success);
  font-weight: var(--font-weight-semibold);
  flex-shrink: 0;
}
```

**Bruk:**
```jsx
<Section>
  <Container>
    <Stack gap="component">
      <div style={{ textAlign: 'center' }}>
        <h2 className="text-display-md">Enkel prising</h2>
      </div>
      <div className="pricing-grid">
        <article className="price-card">
          <p className="price-card-tier">Starter</p>
          <p className="price-card-price">99<span className="price-card-period"> kr/mnd</span></p>
          <p className="price-card-description">For mindre borettslag.</p>
          <ul className="price-card-features">
            <li>Inntil 50 beboere</li>
            <li>Vedlikeholdslogg</li>
          </ul>
          <Button variant="secondary" fullWidth>Start gratis</Button>
        </article>
        <article className="price-card price-card-highlighted">
          <p className="price-card-tier">Pro</p>
          <p className="price-card-price">299<span className="price-card-period"> kr/mnd</span></p>
          <p className="price-card-description">For aktive borettslag.</p>
          <ul className="price-card-features">
            <li>Ubegrenset antall beboere</li>
            <li>Vedlikeholdslogg + planlegging</li>
            <li>SMS-varslinger</li>
          </ul>
          <Button fullWidth>Start gratis</Button>
        </article>
        <article className="price-card">
          <p className="price-card-tier">Enterprise</p>
          <p className="price-card-price">Kontakt oss</p>
          <p className="price-card-description">For boligbyggelag.</p>
          <ul className="price-card-features">
            <li>Multi-borettslag</li>
            <li>SLA + dedikert support</li>
          </ul>
          <Button variant="secondary" fullWidth>Snakk med oss</Button>
        </article>
      </div>
    </Stack>
  </Container>
</Section>
```

---

## 9. Stats-strip

Horisontal strip med 3-4 stat-tall. Stor display-typografi for tall, eyebrow over.

**Props:** `items` (array av `{ label, value, suffix?, description? }`).

**CSS:**
```css
@utility stats-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(14rem, 100%), 1fr));
  gap: clamp(2rem, 5vw, 4rem);
}

@utility stats-strip-item {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  text-align: left;
}

@utility stats-strip-value {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  font-weight: var(--font-weight-display);
  font-variant-numeric: tabular-nums;
  letter-spacing: var(--tracking-tight);
  line-height: 1;
  color: var(--color-fg);
}

@utility stats-strip-label {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-muted);
}

@utility stats-strip-description {
  font-size: var(--text-sm);
  color: var(--color-muted);
  max-width: 28ch;
  margin-top: var(--gap-tight);
}
```

**Bruk:**
```jsx
<Section>
  <Container>
    <div className="stats-strip">
      <div className="stats-strip-item">
        <p className="stats-strip-value">240+</p>
        <p className="stats-strip-label">Aktive borettslag</p>
      </div>
      <div className="stats-strip-item">
        <p className="stats-strip-value">12k</p>
        <p className="stats-strip-label">Beboere på plattformen</p>
      </div>
      <div className="stats-strip-item">
        <p className="stats-strip-value">98%</p>
        <p className="stats-strip-label">Kundetilfredshet</p>
      </div>
    </div>
  </Container>
</Section>
```

---

## Felles responsivitets-prinsipper

Alle section-patterns følger:

1. **Container** rammer inn med fluid `--page-padding` (24-96px).
2. **Vertikal spacing** via `--spacing-section` (clamp 64-160px).
3. **Grid** kollapser via `auto-fit` med `min()` for å unngå overflow.
4. **Container queries** brukes på hero-layouts som har internal breakpoints (split/editorial).
5. **Type-skala** er allerede fluid via `clamp()` — ingen ekstra responsivitet-arbeid nødvendig.
6. **Container queries på 48rem** (~768px) er vår "tablet/desktop"-grense for layout-skift.

## Kombinasjon: typisk landingsside

Komplett landingsside-struktur:

```jsx
<>
  <SiteHeader logo={...} links={[...]} primaryCTA={...} />
  <HeroCentered eyebrow="..." title="..." description="..." primaryCTA={...} />
  <LogoCloud label="Brukt av..." logos={[...]} />
  <FeatureGrid features={[...]} />
  <StatsStrip items={[...]} />
  <CTASection title="..." actions={[...]} />
  <Pricing tiers={[...]} />
  <FAQ items={[...]} />
  <CTASection title="..." actions={[...]} />     {/* gjentas — Stacked-pattern */}
  <SiteFooter brand={...} columns={[...]} />
</>
```

## Hva som ikke er med (krever egen drodling)

- **Hero med video-bakgrunn** — krever performance-strategi (autoplay policy, poster-fallback).
- **Testimonial-section** — egen pattern med quote + avatar + name.
- **Newsletter-signup** — kombinerer Form + section-layout.
- **Animated section-transitions** (parallax, scroll-trigger) — krever JS-library-valg.
- **Mega-menu** (for komplekse site-headers) — fortjener egen sparring.

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: section-patterns-web](../decisions/2026-05-27-section-patterns-web.md)
