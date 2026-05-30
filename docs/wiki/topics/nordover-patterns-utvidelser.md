# Patterns — utvidelser (extensions)

Seks supplerende patterns som dekker hull i det basisrammeverket. Spec'et i én batch — noen er konvensjonelle (Testimonial, Newsletter), noen har reelle valg (Mega-menu, Chart-wrappers, Hero-med-video).

Se [decision 2026-05-27 — patterns-utvidelser](../decisions/2026-05-27-patterns-utvidelser.md).

---

## 1. Testimonial (3 varianter)

For sosial proof i marketing-sider.

### 1a. Testimonial Card

Standard kort med quote + person + logo/avatar.

**Props:** `quote`, `author` (name), `role?`, `company?`, `avatar?`, `companyLogo?`.

**CSS:**
```css
@utility testimonial-card {
  /* arver fra .card-bordered */
  padding: clamp(1.5rem, 3vw, 2rem);
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
}

@utility testimonial-card-quote {
  font-family: var(--font-display);
  font-size: var(--text-lg);
  line-height: 1.5;
  color: var(--color-fg);
  text-wrap: pretty;
}

@utility testimonial-card-quote::before {
  content: """;
  font-size: 2em;
  line-height: 0;
  vertical-align: -0.3em;
  margin-inline-end: 0.1em;
  color: var(--color-muted);
}

@utility testimonial-card-author {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-top: auto;
}

@utility testimonial-card-author-meta {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

@utility testimonial-card-author-name {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
}

@utility testimonial-card-author-role {
  font-size: var(--text-sm);
  color: var(--color-muted);
}
```

### 1b. Testimonial Large Quote

Stor display-format quote — editorial. Bruker `.text-display-md` eller `.text-display-lg`.

**CSS:**
```css
@utility testimonial-large {
  text-align: center;
  padding-block: clamp(3rem, 8vw, 6rem);
  max-width: 28ch;
  margin-inline: auto;
}

@utility testimonial-large-quote {
  font-family: var(--font-display);
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: var(--font-weight-display);
  line-height: 1.15;
  letter-spacing: var(--tracking-tight);
  color: var(--color-fg);
  text-wrap: balance;
}

@utility testimonial-large-author {
  margin-top: clamp(1.5rem, 3vw, 2.5rem);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--gap-tight);
}
```

### 1c. Testimonial Video

Med video-preview-thumbnail som åpner i modal/lightbox når klikket.

**Props:** Som card, pluss `videoSrc`, `posterSrc`.

**CSS:**
```css
@utility testimonial-video {
  position: relative;
  aspect-ratio: 16/9;
  border-radius: var(--radius-lg);
  overflow: hidden;
  cursor: pointer;
  background: var(--color-subtle);
}

@utility testimonial-video-poster {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@utility testimonial-video-play-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 4rem;
  height: 4rem;
  border-radius: var(--radius-full);
  background: var(--glass-bg-strong);
  backdrop-filter: var(--glass-blur-strong);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-fg);
  border: none;
  cursor: pointer;
  transition: transform var(--duration-base) var(--ease-spring);
}

@utility testimonial-video:hover .testimonial-video-play-button {
  transform: translate(-50%, -50%) scale(1.1);
}

@utility testimonial-video-overlay-meta {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--gap-component);
  background: linear-gradient(to top, rgb(0 0 0 / 0.7), transparent);
  color: white;
}
```

---

## 2. Newsletter Signup

Inline-form med success-state.

**Props:** `title`, `description?`, `placeholder?`, `onSubmit`, `successMessage?`, `privacyText?`.

**CSS:**
```css
@utility newsletter-signup {
  padding-block: clamp(4rem, 8vw, 6rem);
  text-align: center;
}

@utility newsletter-signup-form {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  max-width: 28rem;
  margin-inline: auto;
  margin-top: clamp(1.5rem, 3vw, 2rem);
}

@container (min-width: 30rem) {
  @utility newsletter-signup-form { flex-direction: row; }
}

@utility newsletter-signup-input {
  /* .form-input */
  flex: 1;
}

@utility newsletter-signup-privacy {
  font-size: var(--text-xs);
  color: var(--color-muted);
  margin-top: var(--gap-tight);
  max-width: 28rem;
  margin-inline: auto;
}

@utility newsletter-signup-success {
  font-size: var(--text-base);
  color: var(--color-success);
  font-weight: var(--font-weight-medium);
}
```

**Bruk:**
```jsx
<section className="newsletter-signup">
  <Container size="narrow">
    <p className="text-eyebrow">Nyhetsbrev</p>
    <h2 className="text-display-md">Få oppdateringer en gang i måneden.</h2>
    <p className="text-body" style={{ color: 'var(--color-muted)', marginTop: '1rem' }}>
      Ingen spam, kun ekte oppdateringer.
    </p>
    {state.success ? (
      <p className="newsletter-signup-success">✓ Takk! Sjekk innboksen.</p>
    ) : (
      <Form onSubmit={onSubmit} className="newsletter-signup-form">
        <Input type="email" name="email" placeholder="din@epost.no" required />
        <Button type="submit">Meld meg på</Button>
      </Form>
    )}
    <p className="newsletter-signup-privacy">
      Vi behandler din e-post i tråd med <a href="/personvern">personvernerklæringen</a>.
    </p>
  </Container>
</section>
```

---

## 3. Hero med video

Performance-aware video-hero. Poster-fallback, lazy-loading, intersection-trigger.

**Props:** `eyebrow?`, `title`, `description?`, `primaryCTA`, `videoSrc`, `posterSrc`, `videoMuted?` (default true).

**CSS:**
```css
@utility hero-video {
  position: relative;
  min-height: 80vh;
  display: flex;
  align-items: center;
  overflow: hidden;
}

@utility hero-video-media {
  position: absolute;
  inset: 0;
  z-index: 0;
}

@utility hero-video-media video,
@utility hero-video-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@utility hero-video-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to right,
    rgb(0 0 0 / 0.6) 0%,
    rgb(0 0 0 / 0.3) 50%,
    transparent 100%
  );
  z-index: 1;
}

@utility hero-video-content {
  position: relative;
  z-index: 2;
  color: white;
  padding-block: clamp(4rem, 12vw, 8rem);
}

@utility hero-video-title {
  /* .text-display-lg eller .text-display-xl */
  color: white;
  text-shadow: 0 2px 8px rgb(0 0 0 / 0.4);
}

@utility hero-video-description {
  color: rgb(255 255 255 / 0.85);
  font-size: var(--text-lg);
  max-width: 40ch;
  margin-top: var(--gap-component);
}
```

**React-implementasjon:**
```jsx
function HeroVideo({ eyebrow, title, description, primaryCTA, videoSrc, posterSrc, videoMuted = true }) {
  const videoRef = useRef(null);

  // Lazy-play når i view
  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) video.play().catch(() => {});
      else video.pause();
    }, { threshold: 0.25 });
    observer.observe(video);
    return () => observer.disconnect();
  }, []);

  return (
    <section className="hero-video">
      <div className="hero-video-media">
        <video
          ref={videoRef}
          poster={posterSrc}
          muted={videoMuted}
          playsInline
          loop
          preload="metadata"
        >
          <source src={videoSrc} type="video/mp4" />
        </video>
      </div>
      <div className="hero-video-overlay" />
      <div className="hero-video-content">
        <Container>
          {eyebrow && <p className="text-eyebrow">{eyebrow}</p>}
          <h1 className="hero-video-title">{title}</h1>
          {description && <p className="hero-video-description">{description}</p>}
          <Cluster gap="tight" style={{ marginTop: '2rem' }}>
            {primaryCTA}
          </Cluster>
        </Container>
      </div>
    </section>
  );
}
```

**Performance-prinsipper:**
- `poster` settes alltid — fallback før video laster.
- `preload="metadata"` — bare metadata, ikke full video, før play.
- `muted + playsInline` — kreves for autoplay i mobile browsers.
- IntersectionObserver — pauser video når ute av view, sparer batteri.
- `loop` for ambient background-video (typisk hero-bruk).
- For brukere på reduced-motion: vis kun poster, ingen autoplay.

```css
@media (prefers-reduced-motion: reduce) {
  @utility hero-video-media video { display: none; }
}
```

---

## 4. Mega-menu

For site-headere med mange produktlinjer eller dybde-navigasjon. Multi-kolonne dropdown med kategorier og featured items.

**Underliggende:** Radix NavigationMenu.

**Props (MegaMenu):** `items` (struktur med kategorier + lenker), `featured?`.

**CSS:**
```css
@utility mega-menu-list {
  display: flex;
  gap: 1rem;
  align-items: center;
}

@utility mega-menu-trigger {
  /* .site-header-nav-link med chevron */
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  background: transparent;
  border: none;
  cursor: pointer;
  padding-block: 0.5rem;
  color: var(--color-fg);
}

@utility mega-menu-trigger-chevron {
  width: 0.875rem;
  height: 0.875rem;
  transition: transform var(--duration-fast) var(--ease-out);
}

@utility mega-menu-trigger[data-state="open"] .mega-menu-trigger-chevron {
  transform: rotate(180deg);
}

@utility mega-menu-content {
  position: absolute;
  top: 100%;
  left: 0;
  width: max(40rem, 60vw);
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-popover);
  padding: clamp(1.5rem, 3vw, 2rem);
  margin-top: 0.5rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(1.5rem, 3vw, 2rem);
}

@utility mega-menu-content[data-state="open"] {
  animation: menu-in var(--duration-base) var(--ease-out);
}

@utility mega-menu-section {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility mega-menu-section-title {
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
  color: var(--color-muted);
  margin-bottom: 0.25rem;
}

@utility mega-menu-item {
  display: flex;
  align-items: flex-start;
  gap: 0.625rem;
  padding: 0.5rem;
  border-radius: var(--radius-sm);
  text-decoration: none;
  color: var(--color-fg);
  transition: background var(--duration-fast) var(--ease-out);
}

@utility mega-menu-item:hover {
  background: var(--color-subtle);
}

@utility mega-menu-item-icon {
  width: 1.25rem;
  height: 1.25rem;
  flex-shrink: 0;
  color: var(--color-accent);
  margin-top: 0.125rem;
}

@utility mega-menu-item-content {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

@utility mega-menu-item-title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
}

@utility mega-menu-item-description {
  font-size: var(--text-xs);
  color: var(--color-muted);
}

@utility mega-menu-featured {
  background: var(--color-subtle);
  border-radius: var(--radius-md);
  padding: var(--gap-component);
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

/* Mobile fallback */
@media (max-width: 48rem) {
  @utility mega-menu-content {
    position: static;
    width: 100%;
    grid-template-columns: 1fr;
    box-shadow: none;
    border: none;
  }
}
```

**Bruk:**
```jsx
import * as NavigationMenu from "@radix-ui/react-navigation-menu";

<NavigationMenu.Root>
  <NavigationMenu.List className="mega-menu-list">
    <NavigationMenu.Item>
      <NavigationMenu.Trigger className="mega-menu-trigger">
        Produkter <ChevronIcon className="mega-menu-trigger-chevron" />
      </NavigationMenu.Trigger>
      <NavigationMenu.Content className="mega-menu-content">
        <div className="mega-menu-section">
          <p className="mega-menu-section-title">Plattform</p>
          <NavigationMenu.Link href="/dashboard" className="mega-menu-item">
            <DashboardIcon className="mega-menu-item-icon" />
            <div className="mega-menu-item-content">
              <span className="mega-menu-item-title">Dashboard</span>
              <span className="mega-menu-item-description">Oversikt over alle saker</span>
            </div>
          </NavigationMenu.Link>
          {/* flere items */}
        </div>
        <div className="mega-menu-featured">
          <p className="text-eyebrow">Ny lansering</p>
          <h4 className="text-heading-sm">AI-assistent</h4>
          <p className="text-body-sm">Automatiserer rutine-håndtering.</p>
          <a href="/ai" className="text-body-sm" style={{ color: 'var(--color-accent)' }}>Les mer →</a>
        </div>
      </NavigationMenu.Content>
    </NavigationMenu.Item>
  </NavigationMenu.List>
</NavigationMenu.Root>
```

---

## 5. Chart-wrappers (app)

**Underliggende:** [Recharts](https://recharts.org) — declarative React API, D3-basert, well-supported.

**Hvorfor Recharts over alternativer:**
- Visx: lavere-nivå, mer arbeid per chart. Bra for custom viz, overkill for standard SaaS-charts.
- Nivo: større bundle, mer opinionated.
- Chart.js (via react-chartjs-2): imperativ API, kjennes ikke som React.
- Recharts: declarative, dekker 90% av SaaS-behov, mindre bundle enn Nivo.

**Wrappers vi spec'er:** LineChartCard, BarChartCard, AreaChartCard, StackedBarChartCard (Stacked-stil), PieChartCard, DonutChartCard. Hver er en wrapper rundt Recharts med våre design tokens.

**Felles props:** `data`, `series` (array av `{ key, label, color }`), `title?`, `description?`, `height?` (default 240px), `tooltip?` (default custom-styled).

**Eksempel — LineChartCard:**

```css
@utility chart-card {
  /* .card-bordered */
  padding: var(--gap-component);
}

@utility chart-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: var(--gap-component);
}

@utility chart-card-title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-muted);
}

@utility chart-card-value {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: var(--font-weight-semibold);
  font-variant-numeric: tabular-nums;
  line-height: 1;
  margin-top: 0.25rem;
}

@utility chart-tooltip {
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-md);
  padding: var(--gap-tight) var(--gap-component);
  font-size: var(--text-sm);
  box-shadow: var(--shadow-popover);
}

@utility chart-tooltip-label {
  color: var(--color-muted);
  font-size: var(--text-xs);
  margin-bottom: 0.25rem;
}

@utility chart-tooltip-value {
  font-family: var(--font-tabular);
  font-variant-numeric: tabular-nums;
}
```

```jsx
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from "recharts";

function LineChartCard({ data, series, title, height = 240 }) {
  return (
    <div className="chart-card">
      {title && (
        <div className="chart-card-header">
          <p className="chart-card-title">{title}</p>
        </div>
      )}
      <ResponsiveContainer width="100%" height={height}>
        <LineChart data={data}>
          <CartesianGrid stroke="var(--color-border)" strokeDasharray="3 3" vertical={false} />
          <XAxis dataKey="x" stroke="var(--color-muted)" fontSize="var(--text-xs)" />
          <YAxis stroke="var(--color-muted)" fontSize="var(--text-xs)" />
          <Tooltip content={<CustomTooltip />} />
          {series.map((s, i) => (
            <Line
              key={s.key}
              type="monotone"
              dataKey={s.key}
              name={s.label}
              stroke={s.color ?? `var(--chart-${(i % 8) + 1})`}
              strokeWidth={2}
              dot={false}
              activeDot={{ r: 4 }}
            />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

function CustomTooltip({ active, payload, label }) {
  if (!active || !payload?.length) return null;
  return (
    <div className="chart-tooltip">
      <div className="chart-tooltip-label">{label}</div>
      {payload.map(p => (
        <div key={p.dataKey} style={{ color: p.color }}>
          {p.name}: <span className="chart-tooltip-value">{p.value.toLocaleString('nb-NO')}</span>
        </div>
      ))}
    </div>
  );
}
```

**StackedBarChartCard** (Stacked-stil multi-category revenue):

```jsx
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";

function StackedBarChartCard({ data, series, title, height = 280 }) {
  return (
    <div className="chart-card">
      {title && <div className="chart-card-header"><p className="chart-card-title">{title}</p></div>}
      <SelectionGroup items={series} />
      <ResponsiveContainer width="100%" height={height}>
        <BarChart data={data}>
          <CartesianGrid stroke="var(--color-border)" strokeDasharray="3 3" vertical={false} />
          <XAxis dataKey="x" stroke="var(--color-muted)" />
          <YAxis stroke="var(--color-muted)" />
          <Tooltip content={<CustomTooltip />} />
          {series.map((s, i) => (
            <Bar
              key={s.key}
              dataKey={s.key}
              name={s.label}
              stackId="a"
              fill={s.color ?? `var(--chart-${(i % 8) + 1})`}
              radius={i === series.length - 1 ? [4, 4, 0, 0] : 0}
            />
          ))}
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
```

Bundle-kost: ~50kb gzip for Recharts. Opt-in via dynamisk import for sider som ikke trenger charts.

---

## 6. Empty State med illustrasjoner

Utvidelse av Empty State fra batch 1b — med innebygget SVG-illustrasjons-sett som adapter til design tokens (currentColor + CSS vars).

**Spec for illustrasjoner:**
- 6-8 SVG-illustrasjoner ships med rammeverket:
  - `empty-inbox` — innboks med fjær
  - `empty-search` — forstørrelsesglass
  - `empty-folder` — tom mappe
  - `empty-data` — chart med null-data
  - `empty-list` — tom liste
  - `empty-error` — 404 / feil
  - `empty-success` — sjekk-tegn
  - `empty-users` — folk-silhouett
- Alle bruker `stroke="currentColor"` så de adapter til `--color-muted` automatisk.
- Linjebasert (ikke filled) for Scandi-min editorial feel.
- 96-128px naturlig størrelse (kan skaleres).

**Komponent:**

```jsx
import { ReactComponent as InboxIllustration } from "./illustrations/empty-inbox.svg";

function EmptyState({
  illustration,       // string name ELLER React-node
  title,
  description,
  action,
  ...rest
}) {
  const Illustration = typeof illustration === "string" ? ILLUSTRATIONS[illustration] : null;

  return (
    <div className="empty-state" {...rest}>
      {Illustration && <Illustration className="empty-state-illustration" />}
      {React.isValidElement(illustration) && <div className="empty-state-illustration">{illustration}</div>}
      <p className="empty-state-title">{title}</p>
      {description && <p className="empty-state-description">{description}</p>}
      {action && <div className="empty-state-action">{action}</div>}
    </div>
  );
}
```

**CSS-tillegg:**
```css
@utility empty-state-illustration {
  width: clamp(5rem, 12vw, 8rem);
  height: auto;
  color: var(--color-muted);
  opacity: 0.7;
  margin-bottom: var(--gap-component);
}

@utility empty-state-illustration svg {
  width: 100%;
  height: auto;
  stroke: currentColor;
  fill: none;
}
```

**Bruk:**
```jsx
<EmptyState
  illustration="empty-inbox"
  title="Ingen henvendelser ennå"
  description="Når beboere registrerer saker, dukker de opp her."
  action={<Button>Lag prøvesak</Button>}
/>
```

**SVG-eksempel — empty-inbox.svg:**
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M22 56 L22 92 C22 96 25 99 29 99 L99 99 C103 99 106 96 106 92 L106 56" />
  <path d="M22 56 L36 28 L92 28 L106 56" />
  <path d="M22 56 L48 56 L52 64 L76 64 L80 56 L106 56" />
</svg>
```

Alle illustrasjoner følger samme stil (line-art, stroke-only, currentColor).

---

## Library-additions (utvidelser)

- **Mega-menu:** `@radix-ui/react-navigation-menu`
- **Charts:** `recharts` (opt-in via dynamic import per chart-type)

Total bundle-tillegg når alt brukes: ~60kb gzip (40 for Recharts, 20 for nav-menu).

## Hva fortsatt utelates (krever egen drodling)

- **Multi-step Wizard** — eget pattern med progress-indikator + step-state-management
- **Inline edit** (click-to-edit cells) — krever optimistic UI-mønster
- **Filter Bar** (kombinasjon av Tag + Dropdown for komplekse filtre)
- **Notification feed** (forskjellig fra Activity Stream — actionable, dismissible)
- **3D/parallax-effekter** — krever performance + library-valg
- **Skjelett-illustrasjoner** for empty-states utover de 6-8 vi ship'er

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: patterns-utvidelser](../decisions/2026-05-27-patterns-utvidelser.md)
