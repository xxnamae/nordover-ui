# App-patterns (fase 2A)

Tretten arkitektur-tunge patterns for app/webapp-rammeverket. Bygger på `tokens-app` og batch 1/1b-komponentene.

**Underliggende logikk:** Radix Primitives (focus-trap, keyboard-nav, ARIA, portal, scroll-lock). Vår jobb er styling og semantiske API. Radix er MIT, headless, tree-shake-bart, og er industri-standard for komplekse komponenter.

Se [decision 2026-05-27 — app-patterns-arkitektur](../decisions/2026-05-27-app-patterns-arkitektur.md).

---

## Felles arkitektur-prinsipper

1. **Portal-pattern:** Modal, Drawer, Toast, Menu, Tooltip, Command Palette rendres i en portal-container utenfor app-roten. App-root inkluderer `<NordoverProvider>` som setter opp portal-mountpoint.
2. **Data-state-attributter:** `data-state="open|closed"` på rot-element. CSS-transisjoner reagerer på state-skift (Radix-konvensjon).
3. **Controlled + uncontrolled:** Hver overlay-komponent støtter både via `open + onOpenChange` (controlled) eller `defaultOpen` (uncontrolled).
4. **Polymorphic `as`-prop** der det gir mening (i tråd med layout-primitivene).
5. **Animasjon:** CSS-transisjoner på `data-state` + `--duration-base`. Reduced-motion via eksisterende media query.
6. **Z-index:** alle bruker vår z-index-skala (`--z-modal`, `--z-tooltip`, etc.).
7. **Tone-akse:** komponenter med semantiske tilstander (Toast/Alert) støtter `tone="neutral|danger|success|warning|info"`.

---

# GRUPPE 1: Foundation

## 1. Card

Bygger på `--border-card`, `--shadow-card-hover`, `hover-lift`-utility.

**Props:** `variant` (`bordered` | `elevated` | `subtle` | `interactive`), `as`, `padding` (`compact` | `default` | `loose`).

**CSS:**
```css
@utility card {
  background: var(--color-bg);
  border-radius: var(--radius-lg);
  padding: var(--gap-component);
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  position: relative;
}

@utility card-bordered { border: var(--border-card); }

@utility card-elevated {
  box-shadow: var(--shadow-card-hover);
  border: none;
}

@utility card-subtle {
  background: var(--color-subtle);
  border: none;
}

@utility card-interactive {
  border: var(--border-card);
  cursor: pointer;
  transition: transform var(--duration-base) var(--ease-out),
              box-shadow var(--duration-base) var(--ease-out),
              border-color var(--duration-fast) var(--ease-out);
  text-decoration: none;
  color: inherit;
}

@utility card-interactive:hover {
  transform: translateY(var(--lift-distance));
  box-shadow: var(--lift-shadow-to);
  border-color: var(--color-muted);
}

@utility card-padding-compact { padding: var(--gap-tight); }
@utility card-padding-loose { padding: clamp(1.5rem, 3vw, 2rem); }

/* Sub-komposisjons-elementer */
@utility card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--gap-component);
}

@utility card-title {
  font-size: var(--text-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--color-fg);
}

@utility card-meta {
  font-size: var(--text-sm);
  color: var(--color-muted);
}

@utility card-footer {
  margin-top: auto;
  padding-top: var(--gap-component);
  border-top: var(--border-divider);
}
```

**Bruk:**
```jsx
<Card variant="interactive" as="a" href="/sak/142">
  <div className="card-header">
    <div>
      <p className="card-meta">ENG-142</p>
      <h3 className="card-title">Vannlekkasje i kjeller</h3>
    </div>
    <Badge tone="danger">Akutt</Badge>
  </div>
  <p className="text-body">Beboer i 3. etg melder om vann i kjeller.</p>
  <div className="card-footer">
    <Cluster justify="between" align="center">
      <AvatarPill name="Eirik" />
      <span className="text-caption">2 timer siden</span>
    </Cluster>
  </div>
</Card>
```

---

# GRUPPE 2: Overlays

Alle bruker portal, focus-trap, scroll-lock og ESC-håndtering via Radix.

## 2. Modal / Dialog

**Underliggende:** Radix Dialog.

**Props:** `open`, `onOpenChange`, `title`, `description?`, `children`, `size` (`sm` | `md` | `lg` | `xl`), `dismissible?` (default true).

**CSS:**
```css
@utility modal-overlay {
  position: fixed;
  inset: 0;
  background: color-mix(in oklch, var(--color-fg) 50%, transparent);
  backdrop-filter: blur(4px);
  z-index: var(--z-modal);
  animation: modal-overlay-in var(--duration-base) var(--ease-out);
}

@utility modal-overlay[data-state="closed"] {
  animation: modal-overlay-out var(--duration-fast) var(--ease-out);
}

@utility modal-content {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: min(calc(100vw - 2 * var(--page-padding)), 32rem);
  max-height: calc(100vh - 2 * var(--page-padding));
  overflow-y: auto;
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-modal);
  padding: clamp(1.5rem, 3vw, 2rem);
  z-index: calc(var(--z-modal) + 1);
  animation: modal-content-in var(--duration-base) var(--ease-spring);
}

@utility modal-sm { width: min(calc(100vw - 2 * var(--page-padding)), 24rem); }
@utility modal-lg { width: min(calc(100vw - 2 * var(--page-padding)), 48rem); }
@utility modal-xl { width: min(calc(100vw - 2 * var(--page-padding)), 64rem); }

@utility modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--gap-component);
  margin-bottom: var(--gap-component);
}

@utility modal-title {
  font-size: var(--text-xl);
  font-weight: var(--font-weight-semibold);
}

@utility modal-description {
  color: var(--color-muted);
  font-size: var(--text-sm);
  margin-top: 0.25rem;
}

@utility modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--gap-tight);
  margin-top: var(--gap-component);
  padding-top: var(--gap-component);
  border-top: var(--border-divider);
}

@keyframes modal-overlay-in {
  from { opacity: 0; }
  to { opacity: 1; }
}
@keyframes modal-content-in {
  from { opacity: 0; transform: translate(-50%, -48%) scale(0.96); }
  to { opacity: 1; transform: translate(-50%, -50%) scale(1); }
}
```

**Bruk:**
```jsx
import * as Dialog from "@radix-ui/react-dialog";

function ConfirmDeleteModal({ open, onOpenChange, onConfirm }) {
  return (
    <Dialog.Root open={open} onOpenChange={onOpenChange}>
      <Dialog.Portal>
        <Dialog.Overlay className="modal-overlay" />
        <Dialog.Content className="modal-content modal-sm">
          <div className="modal-header">
            <div>
              <Dialog.Title className="modal-title">Slett sak?</Dialog.Title>
              <Dialog.Description className="modal-description">
                Dette kan ikke angres.
              </Dialog.Description>
            </div>
            <Dialog.Close asChild>
              <Button iconOnly variant="ghost" aria-label="Lukk"><X /></Button>
            </Dialog.Close>
          </div>
          <p className="text-body">Saken og alle tilhørende kommentarer fjernes permanent.</p>
          <div className="modal-footer">
            <Dialog.Close asChild><Button variant="ghost">Avbryt</Button></Dialog.Close>
            <Button tone="danger" onClick={onConfirm}>Slett</Button>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

---

## 3. Drawer

Slide-in panel fra side (høyre/venstre). Bruker samme Radix Dialog som Modal, kun annen styling og animasjon.

**Props:** `open`, `onOpenChange`, `side` (`right` | `left`, default `right`), `size` (`sm` | `md` | `lg`).

**CSS:**
```css
@utility drawer-content {
  position: fixed;
  top: 0;
  bottom: 0;
  width: min(calc(100vw - 3rem), 28rem);
  background: var(--color-bg);
  border-inline-start: var(--border-card);
  box-shadow: var(--shadow-drawer);
  padding: var(--gap-component);
  z-index: calc(var(--z-drawer) + 1);
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

@utility drawer-right { right: 0; }
@utility drawer-left {
  left: 0;
  border-inline-start: none;
  border-inline-end: var(--border-card);
}

@utility drawer-content[data-state="open"][data-side="right"] {
  animation: drawer-slide-in-right var(--duration-base) var(--ease-out);
}
@utility drawer-content[data-state="closed"][data-side="right"] {
  animation: drawer-slide-out-right var(--duration-fast) var(--ease-out);
}

@keyframes drawer-slide-in-right {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}
@keyframes drawer-slide-out-right {
  from { transform: translateX(0); }
  to { transform: translateX(100%); }
}
/* Mirror for left side */
```

**Bruk:** Strukturelt likt Modal, men `<Dialog.Content className="drawer-content drawer-right">`.

---

## 4. Side-panel

Inline panel (ikke overlay) som "expander" fra siden av hovedinnholdet. Brukes til detalj-view i Linear-stil (klikk en issue → panel åpner ved siden av listen, ikke over).

**Forskjell fra Drawer:** ikke en overlay med backdrop, men en del av layout-en som tar plass.

**Props:** `open`, `onOpenChange`, `width?` (default `28rem`).

**CSS:**
```css
@utility side-panel-layout {
  display: grid;
  grid-template-columns: 1fr;
  transition: grid-template-columns var(--duration-base) var(--ease-out);
}

@utility side-panel-layout[data-panel-state="open"] {
  grid-template-columns: 1fr var(--side-panel-width, 28rem);
}

@utility side-panel {
  background: var(--color-bg);
  border-inline-start: var(--border-card);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

@utility side-panel[data-state="closed"] {
  display: none;
}
```

**Bruk:**
```jsx
<div className="side-panel-layout" data-panel-state={selected ? "open" : "closed"}>
  <main>
    <IssueList onSelect={setSelected} />
  </main>
  <aside className="side-panel" data-state={selected ? "open" : "closed"}>
    {selected && <IssueDetail issue={selected} onClose={() => setSelected(null)} />}
  </aside>
</div>
```

**A11y-note:** Side-panel skifter ikke focus automatisk (i motsetning til Modal/Drawer). Det er en sidekontekst, ikke en avbrytende.

---

## 5. Toast / Alert

**Underliggende:** Radix Toast.

**Props (Toast):** `title`, `description?`, `tone` (`neutral|danger|success|warning|info`), `duration?` (default 5000ms), `action?`.

**Queue + position:** håndteres av `<ToastProvider position="bottom-right">` på app-root.

**CSS:**
```css
@utility toast {
  position: relative;
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-md);
  padding: var(--gap-component);
  box-shadow: var(--shadow-popover);
  min-width: 18rem;
  max-width: 24rem;
  display: flex;
  gap: var(--gap-tight);
  align-items: flex-start;
}

@utility toast-tone-danger { border-color: var(--color-error); }
@utility toast-tone-success { border-color: var(--color-success); }
@utility toast-tone-warning { border-color: var(--color-warning); }
@utility toast-tone-info { border-color: var(--color-info, var(--color-focus)); }

@utility toast-icon {
  flex-shrink: 0;
  width: 1.25rem;
  height: 1.25rem;
}
@utility toast-tone-danger .toast-icon { color: var(--color-error); }
@utility toast-tone-success .toast-icon { color: var(--color-success); }
/* etc */

@utility toast-body { flex: 1; }
@utility toast-title { font-size: var(--text-sm); font-weight: var(--font-weight-semibold); }
@utility toast-description { font-size: var(--text-sm); color: var(--color-muted); margin-top: 0.125rem; }

@utility toast-viewport {
  position: fixed;
  bottom: var(--page-padding);
  right: var(--page-padding);
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  z-index: var(--z-toast);
  max-width: calc(100vw - 2 * var(--page-padding));
}

@utility toast[data-state="open"] {
  animation: toast-slide-in var(--duration-base) var(--ease-spring);
}
@utility toast[data-state="closed"] {
  animation: toast-slide-out var(--duration-fast) var(--ease-out);
}
@keyframes toast-slide-in {
  from { transform: translateX(calc(100% + var(--page-padding))); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}
@keyframes toast-slide-out {
  to { transform: translateX(calc(100% + var(--page-padding))); opacity: 0; }
}
```

**Bruk:**
```jsx
const { toast } = useToast();

<Button onClick={() => toast({
  tone: "success",
  title: "Lagret",
  description: "Endringene er bekreftet.",
  action: <Button size="sm" variant="ghost">Angre</Button>
})}>
  Lagre
</Button>
```

`<ToastProvider/>` mount'es én gang på app-rot. `useToast()`-hook gir queue-API.

**Alert (statisk variant):** samme styling som Toast, men inline i layout (ikke overlay). Brukes for skjema-feilmeldinger, banner-meldinger.

```jsx
<Alert tone="warning" icon={<AlertTriangle />}>
  <AlertTitle>Endringer ikke lagret</AlertTitle>
  <AlertDescription>Du har gjort endringer som ikke er lagret.</AlertDescription>
</Alert>
```

---

# GRUPPE 3: Navigation & Structure

## 6. Sidebar Nav

**Den viktigste app-komponenten** — multi-level med sections, collapse-toggle, sub-items, active state.

**Props (Sidebar):** `collapsed?`, `onCollapseChange?`, children.
**Props (SidebarItem):** `icon?`, `href`, `active?`, `badge?`, `children` (label).
**Props (SidebarSection):** `label?`, `defaultExpanded?`, `collapsible?`.

**CSS:**
```css
@utility sidebar {
  display: flex;
  flex-direction: column;
  width: var(--sidebar-width, 16rem);
  height: 100vh;
  background: var(--color-bg);
  border-inline-end: var(--border-card);
  padding: var(--gap-tight);
  gap: 0.125rem;
  transition: width var(--duration-base) var(--ease-out);
  overflow-y: auto;
}

@utility sidebar-collapsed {
  --sidebar-width: 3.5rem;
}

@utility sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--gap-tight);
  margin-bottom: var(--gap-tight);
}

@utility sidebar-section {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
  margin-top: var(--gap-tight);
}

@utility sidebar-section-label {
  /* .section-header — fra batch 1b */
  padding-inline: var(--gap-tight);
  margin-block: var(--gap-tight) 0.25rem;
}

@utility sidebar-collapsed .sidebar-section-label { display: none; }

@utility sidebar-item {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding-block: 0.375rem;
  padding-inline: var(--gap-tight);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  text-decoration: none;
  border-radius: var(--nav-item-radius);
  transition: background var(--duration-fast) var(--ease-out);
  white-space: nowrap;
  overflow: hidden;
}

@utility sidebar-item:hover {
  background: var(--nav-item-bg-hover);
}

@utility sidebar-item-active {
  background: var(--nav-item-bg-active);
}

@utility sidebar-item-icon {
  width: 1.125rem;
  height: 1.125rem;
  flex-shrink: 0;
  color: var(--color-muted);
}

@utility sidebar-item-active .sidebar-item-icon {
  color: var(--color-fg);
}

@utility sidebar-collapsed .sidebar-item-label,
@utility sidebar-collapsed .sidebar-item-badge,
@utility sidebar-collapsed .sidebar-item-chevron {
  opacity: 0;
  pointer-events: none;
}

@utility sidebar-item-chevron {
  margin-inline-start: auto;
  width: 0.875rem;
  height: 0.875rem;
  color: var(--color-muted);
  transition: transform var(--duration-fast) var(--ease-out);
}

@utility sidebar-item[data-expanded="true"] .sidebar-item-chevron {
  transform: rotate(90deg);
}

@utility sidebar-sub-items {
  display: flex;
  flex-direction: column;
  padding-inline-start: 1.75rem;
  gap: 0.125rem;
}

/* Mobile: hide by default, show as drawer */
@media (max-width: 48rem) {
  @utility sidebar {
    position: fixed;
    inset: 0 auto 0 0;
    z-index: var(--z-modal);
    transform: translateX(-100%);
    transition: transform var(--duration-base) var(--ease-out);
  }
  @utility sidebar[data-mobile-open="true"] {
    transform: translateX(0);
  }
}
```

**Komposisjon-pattern:**
```jsx
<Sidebar collapsed={collapsed} onCollapseChange={setCollapsed}>
  <SidebarHeader>
    <Logo collapsed={collapsed} />
    <Button iconOnly variant="ghost" size="sm" onClick={() => setCollapsed(!collapsed)}>
      <PanelLeftIcon />
    </Button>
  </SidebarHeader>

  <SidebarItem icon={<HomeIcon />} href="/" active={pathname === "/"}>Hjem</SidebarItem>
  <SidebarItem icon={<InboxIcon />} href="/inbox" badge={3}>Innboks</SidebarItem>

  <SidebarSection label="Arbeid">
    <SidebarItem icon={<UsersIcon />} href="/team">Team</SidebarItem>
    <SidebarItem icon={<FolderIcon />} expandable defaultExpanded>
      Prosjekter
      <SidebarSubItems>
        <SidebarItem href="/projects/active">Aktive</SidebarItem>
        <SidebarItem href="/projects/archived">Arkiverte</SidebarItem>
      </SidebarSubItems>
    </SidebarItem>
  </SidebarSection>

  <SidebarSection label="Pinned" collapsible>
    <SidebarEmpty>No pinned projects</SidebarEmpty>
  </SidebarSection>
</Sidebar>
```

**Mobile:** sidebar er hidden by default, åpnes som drawer via `data-mobile-open` (toggle via en hamburger-button i header).

---

## 7. Tabs

**Underliggende:** Radix Tabs.

**Props (Tabs):** `value`, `onValueChange`, `orientation` (`horizontal` | `vertical`).
**Props (TabsList):** indicator-style.
**Props (TabsTrigger):** `value`, `disabled?`.

**CSS:**
```css
@utility tabs-list {
  display: inline-flex;
  align-items: center;
  gap: 0.125rem;
  position: relative;
  border-bottom: var(--border-divider);
}

@utility tabs-trigger {
  position: relative;
  padding-block: 0.5rem;
  padding-inline: 0.875rem;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-muted);
  background: transparent;
  border: none;
  cursor: pointer;
  border-radius: var(--radius-md) var(--radius-md) 0 0;
  transition: color var(--duration-fast) var(--ease-out),
              background var(--duration-fast) var(--ease-out);
  margin-bottom: -1px;  /* overlapper border */
}

@utility tabs-trigger:hover {
  color: var(--color-fg);
  background: var(--color-subtle);
}

@utility tabs-trigger[data-state="active"] {
  color: var(--color-fg);
  border-bottom: 2px solid var(--color-accent);
}

@utility tabs-content {
  padding-block: var(--gap-component);
}

@utility tabs-content[data-state="inactive"] {
  display: none;
}
```

**Bruk:**
```jsx
import * as Tabs from "@radix-ui/react-tabs";

<Tabs.Root value={tab} onValueChange={setTab}>
  <Tabs.List className="tabs-list">
    <Tabs.Trigger value="overview" className="tabs-trigger">Oversikt</Tabs.Trigger>
    <Tabs.Trigger value="activity" className="tabs-trigger">Aktivitet</Tabs.Trigger>
    <Tabs.Trigger value="settings" className="tabs-trigger">Innstillinger</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="overview" className="tabs-content">...</Tabs.Content>
  <Tabs.Content value="activity" className="tabs-content">...</Tabs.Content>
  <Tabs.Content value="settings" className="tabs-content">...</Tabs.Content>
</Tabs.Root>
```

**Indicator-animasjon:** for smooth slide kan vi senere bytte til animated underline. For nå: static border-bottom.

---

## 8. Accordion (animated)

**Underliggende:** Radix Accordion.

**Props (Accordion):** `type` (`single` | `multiple`), `value`, `onValueChange`, `collapsible?` (kun for single).
**Props (AccordionItem):** `value`.

**CSS (med smooth height-animasjon via Radix data-attributes):**
```css
@utility accordion-item {
  border-bottom: var(--border-divider);
}

@utility accordion-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-block: 1rem;
  font-size: var(--text-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  background: transparent;
  border: none;
  cursor: pointer;
  text-align: left;
}

@utility accordion-trigger:hover { color: var(--color-muted); }

@utility accordion-trigger-icon {
  width: 1rem;
  height: 1rem;
  transition: transform var(--duration-base) var(--ease-out);
  flex-shrink: 0;
}

@utility accordion-trigger[data-state="open"] .accordion-trigger-icon {
  transform: rotate(180deg);
}

@utility accordion-content {
  overflow: hidden;
  font-size: var(--text-sm);
  color: var(--color-muted);
}

@utility accordion-content[data-state="open"] {
  animation: accordion-down var(--duration-base) var(--ease-out);
}
@utility accordion-content[data-state="closed"] {
  animation: accordion-up var(--duration-fast) var(--ease-out);
}

@keyframes accordion-down {
  from { height: 0; }
  to { height: var(--radix-accordion-content-height); }
}
@keyframes accordion-up {
  from { height: var(--radix-accordion-content-height); }
  to { height: 0; }
}

@utility accordion-content-inner {
  padding-block: 0 1rem;
}
```

Radix setter `--radix-accordion-content-height` automatisk — det er det som gir smooth animasjon mellom 0 og innholdets høyde.

**Forskjell fra FAQ (web):** FAQ bruker native `<details>` (ingen JS, ingen smooth-animasjon). Accordion bruker Radix for app-bruk med smooth animasjon og kontrollert state.

---

## 9. Menu / Dropdown

**Underliggende:** Radix DropdownMenu (også for Context Menu med Radix ContextMenu).

**Props (DropdownMenu):** `open`, `onOpenChange`, `children`.

**CSS:**
```css
@utility menu-trigger {
  /* arver fra Button eller egen */
}

@utility menu-content {
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-popover);
  padding: 0.25rem;
  min-width: 12rem;
  z-index: var(--z-dropdown);
  display: flex;
  flex-direction: column;
  gap: 0.0625rem;
}

@utility menu-content[data-state="open"] {
  animation: menu-in var(--duration-fast) var(--ease-out);
}

@utility menu-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding-block: 0.375rem;
  padding-inline: 0.625rem;
  font-size: var(--text-sm);
  color: var(--color-fg);
  border-radius: var(--radius-sm);
  cursor: pointer;
  user-select: none;
}

@utility menu-item[data-highlighted] {
  background: var(--color-subtle);
  outline: none;
}

@utility menu-item-icon {
  width: 0.875rem;
  height: 0.875rem;
  color: var(--color-muted);
}

@utility menu-item-shortcut {
  margin-inline-start: auto;
  font-size: var(--text-xs);
  color: var(--color-muted);
  font-family: var(--font-mono);
}

@utility menu-item-destructive { color: var(--color-error); }
@utility menu-item-destructive .menu-item-icon { color: var(--color-error); }

@utility menu-separator {
  height: 1px;
  background: var(--color-border);
  margin-block: 0.25rem;
}

@utility menu-label {
  padding-block: 0.375rem;
  padding-inline: 0.625rem;
  font-size: var(--text-xs);
  color: var(--color-muted);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
}

@utility menu-sub-trigger::after {
  content: "›";
  margin-inline-start: auto;
  color: var(--color-muted);
}

@keyframes menu-in {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}
```

**Bruk:**
```jsx
import * as DropdownMenu from "@radix-ui/react-dropdown-menu";

<DropdownMenu.Root>
  <DropdownMenu.Trigger asChild>
    <Button variant="ghost" iconOnly aria-label="Actions"><MoreIcon /></Button>
  </DropdownMenu.Trigger>
  <DropdownMenu.Portal>
    <DropdownMenu.Content className="menu-content" align="end">
      <DropdownMenu.Item className="menu-item">
        <EditIcon className="menu-item-icon" />
        Rediger
        <span className="menu-item-shortcut">⌘E</span>
      </DropdownMenu.Item>
      <DropdownMenu.Item className="menu-item">
        <CopyIcon className="menu-item-icon" />
        Dupliser
      </DropdownMenu.Item>
      <DropdownMenu.Separator className="menu-separator" />
      <DropdownMenu.Item className="menu-item menu-item-destructive">
        <TrashIcon className="menu-item-icon" />
        Slett
      </DropdownMenu.Item>
    </DropdownMenu.Content>
  </DropdownMenu.Portal>
</DropdownMenu.Root>
```

Sub-menus, radio-grupper og checkbox-items støttes via Radix-API.

---

## 10. Command Palette (⌘K)

**Moderne SaaS-must.** Search + keyboard-nav + action-registry.

**Underliggende:** [cmdk](https://github.com/pacocoursey/cmdk) — Vercel sin headless cmdk-bibliotek (samme team som Radix).

**Props (CommandPalette):** `open`, `onOpenChange`, `placeholder?`, children = registrerte actions.

**CSS:**
```css
@utility command-palette-overlay {
  /* samme som modal-overlay */
}

@utility command-palette-content {
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
  width: min(calc(100vw - 2 * var(--page-padding)), 36rem);
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-modal);
  z-index: calc(var(--z-modal) + 1);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  max-height: 60vh;
}

@utility command-palette-input-wrapper {
  display: flex;
  align-items: center;
  gap: var(--gap-tight);
  padding: var(--gap-component);
  border-bottom: var(--border-divider);
}

@utility command-palette-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  font-size: var(--text-base);
  color: var(--color-fg);
}

@utility command-palette-input::placeholder { color: var(--color-muted); }

@utility command-palette-list {
  overflow-y: auto;
  padding: 0.5rem;
}

@utility command-palette-empty {
  padding: var(--gap-component);
  text-align: center;
  color: var(--color-muted);
  font-size: var(--text-sm);
}

@utility command-palette-group { margin-bottom: var(--gap-tight); }

@utility command-palette-group-heading {
  /* .menu-label */
}

@utility command-palette-item {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding-block: 0.5rem;
  padding-inline: 0.625rem;
  font-size: var(--text-sm);
  border-radius: var(--radius-sm);
  cursor: pointer;
}

@utility command-palette-item[data-selected="true"] {
  background: var(--color-subtle);
}

@utility command-palette-item-shortcut {
  margin-inline-start: auto;
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--color-muted);
}

@utility command-palette-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem var(--gap-component);
  border-top: var(--border-divider);
  font-size: var(--text-xs);
  color: var(--color-muted);
}
```

**Bruk:**
```jsx
import { Command } from "cmdk";

function GlobalCommandPalette({ open, onOpenChange }) {
  // Global ⌘K-binding
  useEffect(() => {
    const down = (e) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        onOpenChange(!open);
      }
    };
    document.addEventListener("keydown", down);
    return () => document.removeEventListener("keydown", down);
  }, [open]);

  return (
    <Dialog.Root open={open} onOpenChange={onOpenChange}>
      <Dialog.Overlay className="command-palette-overlay" />
      <Dialog.Content className="command-palette-content">
        <Command>
          <div className="command-palette-input-wrapper">
            <SearchIcon style={{ color: 'var(--color-muted)' }} />
            <Command.Input placeholder="Hva vil du gjøre?" className="command-palette-input" />
          </div>
          <Command.List className="command-palette-list">
            <Command.Empty className="command-palette-empty">Ingen treff.</Command.Empty>

            <Command.Group heading="Hurtighandlinger" className="command-palette-group">
              <Command.Item className="command-palette-item">
                <PlusIcon /> Ny sak
                <span className="command-palette-item-shortcut">⌘N</span>
              </Command.Item>
              <Command.Item className="command-palette-item">
                <SearchIcon /> Søk i saker
              </Command.Item>
            </Command.Group>

            <Command.Group heading="Navigasjon" className="command-palette-group">
              <Command.Item>Gå til Dashboard</Command.Item>
              <Command.Item>Gå til Team</Command.Item>
            </Command.Group>
          </Command.List>
          <div className="command-palette-footer">
            <span><Kbd>↑↓</Kbd> Naviger</span>
            <span><Kbd>↵</Kbd> Velg</span>
            <span><Kbd>esc</Kbd> Lukk</span>
          </div>
        </Command>
      </Dialog.Content>
    </Dialog.Root>
  );
}
```

`<NordoverProvider/>` setter opp global ⌘K-binding og registrerer actions fra et globalt registry.

---

# GRUPPE 4: Data Display

## 11. Data Table

**Underliggende:** [TanStack Table](https://tanstack.com/table) (headless), vår styling oppå.

**Features (via TanStack):** sortering, filtering, paginering, kolonne-bredder, row-selection, expand/collapse.

**CSS:**
```css
@utility data-table-wrapper {
  border: var(--border-card);
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--color-bg);
}

@utility data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: var(--text-sm);
}

@utility data-table thead {
  background: var(--color-subtle);
}

@utility data-table th {
  text-align: left;
  font-weight: var(--font-weight-medium);
  color: var(--color-muted);
  padding: 0.625rem var(--gap-component);
  border-bottom: var(--border-divider);
  white-space: nowrap;
  position: sticky;
  top: 0;
  background: var(--color-subtle);
  z-index: 1;
}

@utility data-table th[data-sortable="true"] {
  cursor: pointer;
  user-select: none;
}
@utility data-table th[data-sortable="true"]:hover { color: var(--color-fg); }

@utility data-table th[data-sort="asc"]::after { content: " ↑"; }
@utility data-table th[data-sort="desc"]::after { content: " ↓"; }

@utility data-table td {
  padding: 0.625rem var(--gap-component);
  border-bottom: var(--border-divider);
  color: var(--color-fg);
}

@utility data-table tbody tr:hover {
  background: var(--color-subtle);
}

@utility data-table tbody tr[data-selected="true"] {
  background: color-mix(in oklch, var(--color-accent) 8%, var(--color-bg));
}

@utility data-table-cell-numeric {
  text-align: right;
  font-variant-numeric: tabular-nums;
}

@utility data-table-cell-actions {
  text-align: right;
  width: 1%;
  white-space: nowrap;
}
```

**Bruk:**
```jsx
import { useReactTable, getCoreRowModel, getSortedRowModel, flexRender } from "@tanstack/react-table";

function IssueTable({ data }) {
  const columns = useMemo(() => [
    { accessorKey: "id", header: "ID" },
    { accessorKey: "title", header: "Tittel" },
    {
      accessorKey: "status",
      header: "Status",
      cell: ({ row }) => <StatusIndicator status={row.original.status} />
    },
    {
      accessorKey: "priority",
      header: "Prioritet",
      cell: ({ row }) => <PriorityIndicator priority={row.original.priority} />
    },
    {
      accessorKey: "assignee",
      header: "Tildelt",
      cell: ({ row }) => <AvatarPill name={row.original.assignee} />
    },
  ], []);

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  return (
    <div className="data-table-wrapper">
      <table className="data-table">
        <thead>
          {table.getHeaderGroups().map(hg => (
            <tr key={hg.id}>
              {hg.headers.map(h => (
                <th key={h.id} data-sortable={h.column.getCanSort()} onClick={h.column.getToggleSortingHandler()}>
                  {flexRender(h.column.columnDef.header, h.getContext())}
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map(row => (
            <tr key={row.id}>
              {row.getVisibleCells().map(cell => (
                <td key={cell.id}>{flexRender(cell.column.columnDef.cell, cell.getContext())}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

---

## 12. Activity Stream

Linear-pattern: avatar + name + action + timestamp + optional content.

**Props (ActivityItem):** `actor` (name + avatar), `action` (text/JSX), `timestamp`, `children?` (innhold som comment-tekst).

**CSS:**
```css
@utility activity-stream {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
}

@utility activity-item {
  display: grid;
  grid-template-columns: 2rem 1fr;
  gap: var(--gap-tight);
  align-items: flex-start;
}

@utility activity-item-avatar { grid-row: span 2; }

@utility activity-item-header {
  font-size: var(--text-sm);
  color: var(--color-muted);
  line-height: 1.4;
}

@utility activity-item-actor {
  color: var(--color-fg);
  font-weight: var(--font-weight-medium);
}

@utility activity-item-content {
  font-size: var(--text-sm);
  color: var(--color-fg);
  padding: var(--gap-tight);
  background: var(--color-subtle);
  border-radius: var(--radius-md);
  margin-top: 0.25rem;
}

@utility activity-item-content:empty { display: none; }
```

**Bruk:**
```jsx
<div className="activity-stream">
  <div className="activity-item">
    <Avatar name="Eirik" className="activity-item-avatar" size="sm" />
    <div>
      <p className="activity-item-header">
        <span className="activity-item-actor">Eirik</span> endret status til <StatusIndicator status="in-progress" /> · 2 timer siden
      </p>
    </div>
  </div>
  <div className="activity-item">
    <Avatar name="Anna" className="activity-item-avatar" size="sm" />
    <div>
      <p className="activity-item-header">
        <span className="activity-item-actor">Anna</span> · kommenterte · 1 time siden
      </p>
      <div className="activity-item-content">Bra jobbet — kan vi få dette ut før helgen?</div>
    </div>
  </div>
</div>
```

---

## 13. Kanban Board

Multi-column board med drag/drop.

**Underliggende:** [@dnd-kit](https://dndkit.com) (headless, a11y, keyboard-support).

**Props (KanbanBoard):** `columns`, `items`, `onMove`.

**CSS:**
```css
@utility kanban-board {
  display: flex;
  gap: var(--gap-component);
  overflow-x: auto;
  padding: var(--gap-component);
  min-height: calc(100vh - 8rem);
}

@utility kanban-column {
  flex: 0 0 18rem;
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility kanban-column-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.25rem var(--gap-tight);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-fg);
}

@utility kanban-column-count {
  color: var(--color-muted);
  font-weight: var(--font-weight-normal);
  font-variant-numeric: tabular-nums;
}

@utility kanban-column-body {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
  min-height: 4rem;
  padding: var(--gap-tight);
  border-radius: var(--radius-md);
  background: var(--color-subtle);
}

@utility kanban-column-body[data-droppable-over="true"] {
  background: color-mix(in oklch, var(--color-accent) 8%, var(--color-subtle));
}

@utility kanban-card {
  /* arver fra .card */
  cursor: grab;
}

@utility kanban-card[data-dragging="true"] {
  opacity: 0.5;
  cursor: grabbing;
}
```

**Bruk:**
```jsx
import { DndContext, DragOverlay } from "@dnd-kit/core";

<DndContext onDragEnd={handleDragEnd}>
  <div className="kanban-board">
    {columns.map(col => (
      <div key={col.id} className="kanban-column">
        <div className="kanban-column-header">
          <StatusIndicator status={col.status}>{col.label}</StatusIndicator>
          <span className="kanban-column-count">{col.items.length}</span>
        </div>
        <Droppable id={col.id} className="kanban-column-body">
          {col.items.map(item => (
            <Draggable key={item.id} id={item.id}>
              <Card className="kanban-card">
                <p className="card-meta">{item.id}</p>
                <p className="card-title">{item.title}</p>
                <Cluster gap="tight">
                  <PriorityIndicator priority={item.priority} />
                  <AvatarPill name={item.assignee} size="sm" />
                </Cluster>
              </Card>
            </Draggable>
          ))}
        </Droppable>
      </div>
    ))}
  </div>
</DndContext>
```

---

## Dependency-oversikt

App-rammeverket avhenger av:

| Pattern | Library |
|---|---|
| Modal, Drawer, Side-panel, Command Palette overlay | `@radix-ui/react-dialog` |
| Tabs | `@radix-ui/react-tabs` |
| Accordion | `@radix-ui/react-accordion` |
| Menu / Dropdown | `@radix-ui/react-dropdown-menu` |
| Toast | `@radix-ui/react-toast` |
| Command Palette | `cmdk` |
| Data Table | `@tanstack/react-table` |
| Kanban (drag/drop) | `@dnd-kit/core` + `@dnd-kit/sortable` |

Alle er headless, MIT, well-maintained, og tree-shake-bare. Total tilleggsbundle: ~30-40kb gzip når alt brukes.

Sidebar Nav, Card, Activity Stream er custom (ingen library-avhengighet).

## NordoverProvider

App-rot setter opp portal-mountpoint, toast-queue, og global keyboard-listener:

```jsx
import { TooltipProvider, ToastProvider } from "@radix-ui/react-toast";

function NordoverProvider({ children }) {
  const [commandPaletteOpen, setCommandPaletteOpen] = useState(false);

  return (
    <ToastProvider>
      <TooltipProvider delayDuration={300}>
        {children}
        <ToastViewport />
        <GlobalCommandPalette open={commandPaletteOpen} onOpenChange={setCommandPaletteOpen} />
      </TooltipProvider>
    </ToastProvider>
  );
}
```

Bruk:
```jsx
<NordoverProvider>
  <App />
</NordoverProvider>
```

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: app-patterns-arkitektur](../decisions/2026-05-27-app-patterns-arkitektur.md)
