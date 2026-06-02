# Patterns — utvidelser batch 2

Andre runde utvidelser etter referanser fra Linear, Stacked og Off Menu. Dekker:
- 3 nye Site Header-varianter (totalt 4 inkl. eksisterende glass)
- 2 nye Footer-varianter (totalt 3)
- AI Assistant Panel (Off Menu Remi / Linear "Ask Linear"-pattern)
- Onboarding Flow (Wizard-variant for applikasjoner)
- Numerated Service List (editorial nummerert lenkeliste)
- Sticky Sub-nav (left sticky-nav for feature-sider)
- Feature Row (text + UI preview composition)

Se [decision 2026-05-27 — patterns-utvidelser-batch2](../decisions/2026-05-27-patterns-utvidelser-batch2.md).

---

## 1. Site Header-varianter (4 totalt)

### 1a. Glass (default — sticky)

Allerede spec'et i [nordover-section-patterns.md](nordover-section-patterns.md#6-header--site-nav-marketing). Sticky med `backdrop-filter` + `--glass-bg`. Standard for SaaS-marketing.

### 1b. Stacked-stil (sentrert nav, pill-CTA-par)

Solid bg, sentrert horisontalt nav, to pill-knapper (en fylt + en outlined) til høyre.

**Props:** `logo`, `links` (array), `loginLabel?` (default "Log in"), `signupLabel?` (default "Sign up").

**CSS:**
```css
@utility site-header-stacked {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background: var(--color-bg);
}

@utility site-header-stacked-nav {
  display: flex;
  gap: 1.75rem;
  font-size: var(--text-sm);
  color: var(--color-muted);
}

@utility btn-pill-light {
  background: var(--color-fg);
  color: var(--color-bg);
  padding: 0.375rem 0.875rem;
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-sm);
  border: none;
}

@utility btn-pill-outline {
  background: transparent;
  color: var(--color-fg);
  padding: 0.375rem 0.875rem;
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-sm);
  border: var(--border-card);
}
```

**Brukes:** SaaS-marketing der konvertering er primært (Stacked, Vercel, Linear).

### 1c. Linear-stil (minimal, "Open app"-pill)

Logo + nav-lenker + divider + Docs-lenke + "Open app"-pill. Veldig minimalistisk.

**Props:** `logo`, `links`, `docsLabel?`, `appUrl`.

**CSS:**
```css
@utility site-header-linear {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.875rem 1.25rem;
  background: var(--color-bg);
}

@utility site-header-linear-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

@utility site-header-linear-divider {
  width: 1px;
  height: 1rem;
  background: var(--color-border);
}

@utility btn-pill-fill {
  background: var(--color-fg);
  color: var(--color-bg);
  padding: 0.375rem 0.875rem;
  border-radius: var(--radius-full);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-sm);
  border: none;
}
```

**Brukes:** Produkt-fokuserte SaaS-sider der "Open app" er primær handling for eksisterende brukere.

### 1d. Off Menu-stil (light editorial, dots-toggle)

Light bg, logo + 3x3 grid-dot-trigger som åpner dropdown med Resources-seksjon under hovedlenkene.

**Props:** `logo`, `mainLinks` (array), `resourceLinks` (array).

**CSS:**
```css
@utility site-header-offmenu {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 1.5rem;
}

@utility site-header-offmenu-dot-toggle {
  display: inline-grid;
  grid-template-columns: repeat(3, 4px);
  grid-template-rows: repeat(3, 4px);
  gap: 4px;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  border-radius: var(--radius-sm);
}

@utility site-header-offmenu-dot-toggle span {
  width: 4px;
  height: 4px;
  border-radius: var(--radius-full);
  background: var(--color-fg);
}

@utility site-header-offmenu-menu {
  position: absolute;
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-md);
  padding: 0.75rem 1rem;
  box-shadow: var(--shadow-md);
  min-width: 14rem;
}

@utility site-header-offmenu-menu-label {
  font-size: var(--text-xs);
  color: var(--color-muted);
  margin-top: 0.75rem;
  border-top: var(--border-divider);
  padding-top: 0.75rem;
}
```

**Brukes:** Editorial brand-sider, design-studio, agencies. Light mode primært.

---

## 2. Footer-varianter (3 totalt)

### 2a. Default — 1 brand + 3 link-columns

Allerede spec'et. Standard for SaaS-marketing.

### 2b. Linear-stil — 5 link-columns + bottom-bar

5 like-bredde kolonner: logo-mark + Product / Features / Company / Resources / Connect. Bottom-bar med Privacy / Terms / DPA.

**CSS:**
```css
@utility footer-linear-style {
  padding: 4rem 2rem 3rem;
  background: var(--color-bg);
}

@utility footer-linear-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  gap: 2rem;
}

@utility footer-linear-bottom {
  display: flex;
  gap: 1rem;
  margin-top: 3rem;
  font-size: var(--text-sm);
  color: var(--color-muted);
}

@media (max-width: 48rem) {
  @utility footer-linear-grid { grid-template-columns: 1fr 1fr; }
}
```

**Brukes:** Større SaaS-leveranser med mange feature- og resource-lenker.

### 2c. Minimal — 1-rad

Brand + lenke-rad + copyright på samme linje. Bare separert med flexbox.

**CSS:**
```css
@utility footer-minimal {
  padding: 2.5rem 2rem;
  border-top: var(--border-divider);
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
}

@utility footer-minimal-links {
  display: flex;
  gap: 1.5rem;
  font-size: var(--text-sm);
  color: var(--color-muted);
}
```

**Brukes:** Landingssider, app-shells, app-marketing der full footer er for mye.

---

## 3. AI Assistant Panel

Floating chat-overlay som glir inn fra side (oftest bottom-left). Inneholder agent-avatar, intro-melding, suggested prompts som klikkbare pills, og input-felt. Off Menu sin "Remi" + Linear sin "Ask Linear".

**Props:**
- `agent` ({ name, avatar, role })
- `intro` (string — første melding)
- `suggestions` (array av string — klikkbare prompts)
- `placeholder?` (default "Spør om hva som helst")
- `position?` (`bottom-left` | `bottom-right`, default `bottom-left`)
- `onSubmit` (handler)
- `onClose`

**CSS:**
```css
@utility ai-assistant-panel {
  position: fixed;
  bottom: 1.5rem;
  inset-inline-start: 1.5rem;
  z-index: var(--z-modal);
  width: min(calc(100vw - 3rem), 22rem);
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  max-height: 70vh;
}

@utility ai-assistant-position-right {
  inset-inline-start: auto;
  inset-inline-end: 1.5rem;
}

@utility ai-assistant-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0.75rem;
  border-bottom: var(--border-divider);
}

@utility ai-assistant-tabs {
  display: flex;
  gap: 0.25rem;
}

@utility ai-assistant-tab {
  font-size: var(--text-xs);
  color: var(--color-muted);
  padding: 0.25rem 0.5rem;
  border-radius: var(--radius-sm);
}

@utility ai-assistant-tab-active {
  color: var(--color-fg);
  background: var(--color-subtle);
}

@utility ai-assistant-portrait {
  width: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  background: var(--color-subtle);
}

@utility ai-assistant-body {
  padding: var(--gap-component);
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility ai-assistant-agent-name {
  font-size: var(--text-xs);
  color: var(--color-muted);
}

@utility ai-assistant-intro {
  font-size: var(--text-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  text-wrap: pretty;
}

@utility ai-assistant-suggestions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.375rem;
  margin-top: var(--gap-tight);
}

@utility ai-assistant-suggestion {
  font-size: var(--text-xs);
  padding: 0.25rem 0.625rem;
  background: var(--color-subtle);
  border: var(--border-card);
  border-radius: var(--radius-full);
  cursor: pointer;
}

@utility ai-assistant-suggestion-secondary {
  background: transparent;
}

@utility ai-assistant-input-row {
  display: flex;
  align-items: center;
  gap: var(--gap-tight);
  padding: var(--gap-tight) var(--gap-component);
  border-top: var(--border-divider);
}

@utility ai-assistant-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: var(--text-sm);
  color: var(--color-fg);
}
```

**Bruk:**
```jsx
<AIAssistantPanel
  agent={{ name: "Remi", role: "Nordover's AI assistant", avatar: "/remi.jpg" }}
  intro="Hey — I'm Remi, Nordover's AI assistant. Anything catch your eye?"
  suggestions={[
    "Where should I start?",
    "What do you do?",
    "I have a project",
  ]}
  onSubmit={(text) => sendMessage(text)}
  onClose={() => setOpen(false)}
/>
```

**A11y:**
- `role="dialog"` + `aria-label="AI assistant"`
- Esc lukker
- Focus-trap når åpen (Radix Dialog wrapper)
- Auto-focus på input ved åpning

**Variants:**
- `compact` — uten portrait-bilde, kun tekst
- `portrait` (default) — med agent-bilde øverst (Off Menu-stil)

---

## 4. Onboarding Flow (Wizard-variant)

Multi-step onboarding for nye app-brukere. Som Wizard, men med:
- Full-screen split-layout (innhold venstre, dekorativ media-bg høyre)
- Dot-paginasjon nederst (i stedet for nummerert progress)
- "Skip"-lenke ved siden av primary-CTA
- Mer dramatisk per-steg presentasjon

Linear-onboarding-mønsteret.

**Props:**
- `steps` (array av `{ id, title, description, content (node), media? }`)
- `currentStep`
- `onStepChange`
- `onComplete`
- `onSkip?`

**CSS:**
```css
@utility onboarding-flow {
  position: fixed;
  inset: 0;
  z-index: var(--z-modal);
  display: grid;
  grid-template-columns: 1fr 1fr;
  background: var(--color-bg);
}

@utility onboarding-flow-pane {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: clamp(2rem, 6vw, 6rem);
  position: relative;
}

@utility onboarding-flow-media {
  background: var(--color-subtle);
  background-size: cover;
  background-position: center;
  position: relative;
  overflow: hidden;
}

@utility onboarding-flow-step-title {
  font-size: var(--text-xl);
  font-weight: var(--font-weight-semibold);
  margin-bottom: var(--gap-tight);
}

@utility onboarding-flow-step-description {
  color: var(--color-muted);
  margin-bottom: var(--gap-component);
}

@utility onboarding-flow-step-content {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  margin-bottom: var(--gap-component);
}

@utility onboarding-flow-content-row {
  padding: 0.75rem 0;
  border-top: var(--border-divider);
}

@utility onboarding-flow-content-row-title {
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-sm);
  margin-bottom: 0.125rem;
}

@utility onboarding-flow-content-row-desc {
  font-size: var(--text-sm);
  color: var(--color-muted);
}

@utility onboarding-flow-actions {
  display: flex;
  align-items: center;
  gap: var(--gap-component);
  margin-top: var(--gap-component);
}

@utility onboarding-flow-skip {
  background: transparent;
  border: none;
  color: var(--color-muted);
  font-size: var(--text-sm);
  cursor: pointer;
}

@utility onboarding-flow-dots {
  position: absolute;
  bottom: var(--gap-component);
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 0.375rem;
}

@utility onboarding-flow-dot {
  width: 0.5rem;
  height: 0.25rem;
  border-radius: var(--radius-full);
  background: var(--color-border);
  transition: background var(--duration-fast) var(--ease-out),
              width var(--duration-fast) var(--ease-out);
}

@utility onboarding-flow-dot-active {
  background: var(--color-fg);
  width: 1.5rem;
}

/* Mobile: stables, media på toppen */
@media (max-width: 48rem) {
  @utility onboarding-flow {
    grid-template-columns: 1fr;
    grid-template-rows: 30vh 1fr;
  }
}
```

**Bruk:**
```jsx
<OnboardingFlow
  steps={[
    {
      id: "github",
      title: "Connect GitHub",
      description: "Automate your pull request and commit workflows",
      content: [
        { title: "Code reviews", desc: "Review and merge code directly in Linear" },
        { title: "Automate issues", desc: "Auto-assign issues and update status from PR activity" },
        { title: "Branch specific rules", desc: "Create workflow automations per target branch" },
      ],
      media: <CodeBackground />,
      primaryCTA: { label: "Authenticate with GitHub", icon: <GitHubIcon /> },
    },
    {
      id: "profile",
      title: "Set up your profile",
      description: "Choose how you'll appear in the app",
      content: <ProfileForm />,
    },
    {
      id: "invite",
      title: "Invite teammates",
      description: "Get your team on board to start working",
      content: <InvitationField />,
    },
  ]}
  currentStep={step}
  onStepChange={setStep}
  onComplete={() => router.push("/dashboard")}
  onSkip={() => router.push("/dashboard")}
/>
```

**Forskjell fra `<Wizard>`:**

| | Wizard | OnboardingFlow |
|---|---|---|
| Layout | Inline i container | Full-screen overlay |
| Progress | Nummerert med labels | Dot-paginasjon (1.5rem aktiv) |
| Validation | Per-step strict | Soft (Skip alltid tilgjengelig) |
| Media | Ingen | Visuell pane på høyre side |
| Bruksområde | Settings, opprette-flows | Førstegangs-onboarding |

---

## 5. Numerated Service List

Editorial lenkeliste med numererte rader (01, 02, ..., 06). Off Menu sitt service-list-mønster. Hver rad har title + nummer høyrejustert, full-width klikkbar med hover-bg.

**Props:** `items` (array av `{ id, title, href, number? }`).

**CSS:**
```css
@utility service-list {
  display: flex;
  flex-direction: column;
}

@utility service-list-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.25rem 0.5rem;
  border-top: var(--border-divider);
  color: var(--color-fg);
  text-decoration: none;
  transition: background var(--duration-fast) var(--ease-out),
              padding var(--duration-fast) var(--ease-out);
}

@utility service-list-item:hover {
  background: var(--color-subtle);
  padding-inline: 1rem;
}

@utility service-list-item:last-child {
  border-bottom: var(--border-divider);
}

@utility service-list-item-title {
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 2.5vw, 1.75rem);
  font-weight: var(--font-weight-heading-md);
  letter-spacing: var(--tracking-tight);
}

@utility service-list-item-number {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  color: var(--color-muted);
  font-variant-numeric: tabular-nums;
}
```

**Bruk:**
```jsx
<section>
  <p className="text-eyebrow">Services</p>
  <h2 className="text-display-md">Design delivered without compromise.</h2>
  <div className="service-list">
    <a className="service-list-item" href="/brand">
      <span className="service-list-item-title">Brand Design</span>
      <span className="service-list-item-number">01</span>
    </a>
    <a className="service-list-item" href="/web">
      <span className="service-list-item-title">Web & Experiential</span>
      <span className="service-list-item-number">02</span>
    </a>
    {/* ... */}
  </div>
</section>
```

**Variant:** `service-list-item-bordered` med vertikale dividers mellom title og nummer. Kan også brukes som "feature index" i editorial-prosjekter.

---

## 6. Sticky Sub-nav

Venstre-sidet sticky-nav som scroller med innhold. Brukt på lange feature-sider for å navigere mellom seksjoner. Stacked-pattern på "Scale your income"-siden.

**Props:** `sections` (array av `{ id, label }`), `activeSection`, `onSectionClick`.

**CSS:**
```css
@utility sticky-sub-nav-layout {
  display: grid;
  grid-template-columns: 14rem 1fr;
  gap: clamp(2rem, 5vw, 4rem);
  align-items: start;
}

@utility sticky-sub-nav {
  position: sticky;
  top: clamp(2rem, 5vh, 4rem);
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}

@utility sticky-sub-nav-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0;
  font-size: var(--text-sm);
  color: var(--color-muted);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out),
              padding-left var(--duration-fast) var(--ease-out);
}

@utility sticky-sub-nav-item:hover { color: var(--color-fg); }

@utility sticky-sub-nav-item-active {
  color: var(--color-fg);
  font-weight: var(--font-weight-medium);
}

@utility sticky-sub-nav-item-active::before {
  content: "→";
  margin-right: 0.25rem;
}

@media (max-width: 48rem) {
  @utility sticky-sub-nav-layout {
    grid-template-columns: 1fr;
  }
  @utility sticky-sub-nav {
    position: static;
    flex-direction: row;
    overflow-x: auto;
    gap: 1rem;
    border-bottom: var(--border-divider);
    padding-bottom: 0.5rem;
  }
}
```

**Implementasjon (auto-active basert på scroll):**

```jsx
function StickySubNav({ sections, activeSection, onSectionClick }) {
  // Bruk Intersection Observer for å sette active basert på scroll
  return (
    <nav className="sticky-sub-nav" aria-label="Innhold">
      {sections.map(s => (
        <a
          key={s.id}
          href={`#${s.id}`}
          className={`sticky-sub-nav-item ${activeSection === s.id ? 'sticky-sub-nav-item-active' : ''}`}
          onClick={(e) => { e.preventDefault(); onSectionClick?.(s.id); }}
        >
          {s.label}
        </a>
      ))}
    </nav>
  );
}
```

---

## 7. Feature Row

Tekst-venstre + UI-preview-høyre pattern. Brukes til å vise hver feature med embedded screenshot/komponent-preview. Stacked-mønster.

**Props:** `eyebrow?`, `title`, `description`, `cta?` ({ label, href }), `preview` (node — screenshot, komponent, eller video).

**CSS:**
```css
@utility feature-row {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: clamp(2rem, 6vw, 5rem);
  align-items: center;
  padding-block: clamp(3rem, 8vw, 6rem);
}

@utility feature-row-reverse {
  grid-template-columns: 1.5fr 1fr;
}

@utility feature-row-reverse .feature-row-text {
  order: 2;
}

@utility feature-row-text {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
}

@utility feature-row-title {
  font-family: var(--font-display);
  font-size: var(--text-3xl);
  font-weight: var(--font-weight-heading-lg);
  letter-spacing: var(--tracking-tight);
  line-height: 1.15;
  text-wrap: balance;
}

@utility feature-row-description {
  color: var(--color-muted);
  font-size: var(--text-body);
  max-width: 38ch;
  text-wrap: pretty;
}

@utility feature-row-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  text-decoration: none;
  margin-top: var(--gap-tight);
}

@utility feature-row-cta::after {
  content: "→";
  transition: transform var(--duration-fast) var(--ease-out);
}

@utility feature-row-cta:hover::after {
  transform: translateX(2px);
}

@utility feature-row-preview {
  position: relative;
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--color-subtle);
  border: var(--border-card);
}

@media (max-width: 48rem) {
  @utility feature-row,
  @utility feature-row-reverse {
    grid-template-columns: 1fr;
  }
  @utility feature-row-reverse .feature-row-text { order: initial; }
}
```

**Bruk:**
```jsx
<section>
  <FeatureRow
    eyebrow="Subscriptions"
    title="Monthly revenue from your most dedicated fans"
    description="With custom tiers, perks, and pricing."
    cta={{ label: "Get started", href: "/start" }}
    preview={<DashboardPreview />}
  />
  <FeatureRow
    reverse
    eyebrow="Analytics"
    title="Maximize your earnings with advanced insights that evolve in real time."
    cta={{ label: "Get started", href: "/start" }}
    preview={<AnalyticsPreview />}
  />
</section>
```

**Variants:**
- `feature-row` (default — tekst venstre, preview høyre)
- `feature-row-reverse` (tekst høyre, preview venstre)
- Veksle reverse/non-reverse i en stack av features for visuell rytme.

---

## Bevisst utenfor scope (krever egen drodling)

- **Issue Tree visualization** (Linear-pattern med branch-connectors) — komplekst SVG, krever egen sparring
- **Customer detail cards** (Linear sin Unreal/XMP/ACME — stacked z-index layout) — kan bygges på Card-primitiv
- **Rule builder** (Linear "When/Then"-syntax) — krever form-arkitektur for complex logic
- **3-column isometric illustrations** (Linear marketing) — illustrasjons-arbeid, ikke pattern
- **Numbered feature sections** (1.0/1.1/2.0 — Linear "Intake/Plan/Build") — composition pattern

Disse parkeres til konkret behov dukker opp.

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: patterns-utvidelser-batch2](../decisions/2026-05-27-patterns-utvidelser-batch2.md)
