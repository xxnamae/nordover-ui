# Patterns — basis-batch 2

Andre batch konvensjonelle patterns, kuratert ut fra screen-referanser fra Stacked og Linear. Dekker både web-rammeverk (hero-CTA, FAQ-strukturer) og app-rammeverk (stats card, status indicator, sidebar-elementer).

**Komponentene:** Stats Card, Avatar Pill, Empty State, Section Header, Status Indicator, Priority Indicator, Star Toggle, CTA Pair (Hero-pattern), Counter Nav, Selection Group.

Se [decision 2026-05-27 — patterns-basis-batch2](../decisions/2026-05-27-patterns-basis-batch2.md).

---

## 1. Stats Card

Tall + label + delta-indikator. Vanlig i analytics-dashboards (app) og marketing-stats-strips (web).

**Props:** `label`, `value`, `delta?` (number — positiv = grønn, negativ = rød), `deltaLabel?`, `tone?` (`neutral` | `accent`).

**CSS:**
```css
@utility stats-card {
  padding: var(--gap-component);
  border: var(--border-card);
  border-radius: var(--radius-lg);
  background: var(--color-bg);
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility stats-card-label {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-muted);
}

@utility stats-card-value {
  font-size: var(--text-3xl);
  font-weight: var(--font-weight-semibold);
  font-variant-numeric: tabular-nums;
  font-family: var(--font-display, var(--font-sans));
  letter-spacing: var(--tracking-tight);
  color: var(--color-fg);
  line-height: 1;
}

@utility stats-card-delta {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  font-variant-numeric: tabular-nums;
}

@utility stats-card-delta-positive { color: var(--color-success); }
@utility stats-card-delta-negative { color: var(--color-error); }
```

**Bruk:**
```jsx
<Grid min="14rem">
  <StatsCard label="Total Revenue" value="$156,392" delta={18.2} deltaLabel="vs previous 30 days" />
  <StatsCard label="Total Members" value="10,247" delta={14.3} />
  <StatsCard label="MRR" value="$28,400" delta={-2.1} />
</Grid>
```

Verdi-feltet bruker `font-variant-numeric: tabular-nums` slik at $156,392 og $99,999 har samme bredde.

---

## 2. Avatar Pill

Avatar + navn i pill-form. Linear/Stacked-signatur — brukes i "Assigned to", member-lists, mentions.

**Props:** `name`, `src?` (image), `tone?` (`neutral` | `accent`), `onRemove?` (gjør dismissible), `size` (`sm` | `md`).

**CSS:**
```css
@utility avatar-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding-block: 0.25rem;
  padding-inline: 0.5rem 0.75rem;
  border-radius: var(--radius-full);
  background: var(--color-subtle);
  border: var(--border-card);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  white-space: nowrap;
}

@utility avatar-pill .avatar {
  width: 1.25rem;
  height: 1.25rem;
  font-size: 0.5rem;
}

@utility avatar-pill-sm {
  font-size: var(--text-xs);
  padding-block: 0.125rem;
  padding-inline: 0.375rem 0.5rem;
}
```

**Bruk:**
```jsx
<Cluster gap="tight">
  <AvatarPill name="Sofia Belle" src="/sofia.jpg" />
  <AvatarPill name="Jasmine Reyes" src="/jasmine.jpg" />
  <AvatarPill name="mikiii" src="/miki.jpg" />
</Cluster>
```

---

## 3. Empty State

Når en liste, tabell eller view er tom. Standard pattern: ikon + heading + beskrivelse + valgfri CTA.

**Props:** `icon?`, `title`, `description?`, `action?` (button-element).

**CSS:**
```css
@utility empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding-block: var(--spacing-section-sm);
  padding-inline: var(--gap-component);
  gap: var(--gap-tight);
  color: var(--color-muted);
}

@utility empty-state-icon {
  width: 2.5rem;
  height: 2.5rem;
  color: var(--color-muted);
  opacity: 0.6;
  margin-bottom: var(--gap-tight);
}

@utility empty-state-title {
  font-size: var(--text-base);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
}

@utility empty-state-description {
  font-size: var(--text-sm);
  color: var(--color-muted);
  max-width: 32ch;
}

@utility empty-state-action {
  margin-top: var(--gap-component);
}

/* Minimal-variant — kun tekst, til sidebar-seksjoner (eks. "No pinned projects") */
@utility empty-state-minimal {
  padding: var(--gap-tight);
  font-size: var(--text-sm);
  color: var(--color-muted);
}
```

**Bruk:**
```jsx
<EmptyState
  icon={<InboxIcon />}
  title="Ingen meldinger ennå"
  description="Når du får svar fra teamet, dukker de opp her."
  action={<Button variant="secondary">Inviter team</Button>}
/>

{/* Minimal i sidebar */}
<p className="empty-state-minimal">No pinned projects</p>
```

---

## 4. Section Header

Liten muted overskrift for å dele opp innhold — vanlig i sidebar (eks. "Quick tools", "Pinned"), settings-paneler, og lange skjemaer.

**Props:** `children`, `as?` (default `"h3"`), `tone?` (`muted` | `default`).

**CSS:**
```css
@utility section-header {
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
  color: var(--color-muted);
  margin-block: var(--gap-component) var(--gap-tight);
  padding-inline: var(--gap-tight);
}
```

**Bruk:**
```jsx
<aside>
  <SectionHeader>Quick tools</SectionHeader>
  <NavItem icon={<Image />}>Image</NavItem>
  <NavItem icon={<Video />}>Video</NavItem>

  <SectionHeader>Pinned</SectionHeader>
  <p className="empty-state-minimal">No pinned projects</p>
</aside>
```

---

## 5. Status Indicator

Liten dot (eller ring/halv-fyll for "in progress") + label. Brukes i kanban-kort, issue-lister, og dashboard-rows. Linear-signatur.

**Props:** `status` (`backlog` | `todo` | `in-progress` | `in-review` | `done` | `canceled` | `blocked`), `label?` (default tar fra status), `iconOnly?`.

**CSS:**
```css
@utility status-indicator {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
}

@utility status-dot {
  width: 0.75rem;
  height: 0.75rem;
  border-radius: var(--radius-full);
  flex-shrink: 0;
  position: relative;
}

@utility status-dot-backlog {
  background: transparent;
  border: 1.5px dashed var(--status-backlog);
}
@utility status-dot-todo {
  background: transparent;
  border: 1.5px solid var(--status-todo);
}
@utility status-dot-in-progress {
  background: conic-gradient(var(--status-in-progress) 0deg 180deg, transparent 180deg 360deg);
  border: 1.5px solid var(--status-in-progress);
}
@utility status-dot-in-review {
  background: conic-gradient(var(--status-in-review) 0deg 270deg, transparent 270deg 360deg);
  border: 1.5px solid var(--status-in-review);
}
@utility status-dot-done {
  background: var(--status-done);
}
@utility status-dot-canceled {
  background: var(--status-canceled);
  opacity: 0.5;
}
@utility status-dot-blocked {
  background: var(--status-blocked);
}
```

**Bruk:**
```jsx
<StatusIndicator status="in-progress">In Progress</StatusIndicator>
<StatusIndicator status="done">Done</StatusIndicator>
<StatusIndicator status="blocked" iconOnly />
```

---

## 6. Priority Indicator

Bars-ikon med 4 nivåer + ekstra urgent-variant. Linear-pattern.

**Props:** `priority` (`urgent` | `high` | `medium` | `low` | `none`), `label?`.

**CSS:**
```css
@utility priority-indicator {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
}

@utility priority-bars {
  display: inline-grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5px;
  width: 0.875rem;
  height: 0.875rem;
  align-items: end;
}

@utility priority-bars > span {
  background: var(--priority-none);
  border-radius: 0.5px;
  width: 100%;
}
@utility priority-bars > span:nth-child(1) { height: 33%; }
@utility priority-bars > span:nth-child(2) { height: 66%; }
@utility priority-bars > span:nth-child(3) { height: 100%; }

@utility priority-high .priority-bars > span:nth-child(-n+2) { background: var(--priority-high); }
@utility priority-medium .priority-bars > span:nth-child(-n+1) { background: var(--priority-medium); }
@utility priority-low .priority-bars > span { background: var(--priority-low); opacity: 0.4; }
@utility priority-urgent .priority-bars > span { background: var(--priority-urgent); }
```

**Bruk:**
```jsx
<PriorityIndicator priority="urgent">Urgent</PriorityIndicator>
<PriorityIndicator priority="high" />
```

---

## 7. Star Toggle (Favorite)

Tom stjerne / fylt gul stjerne. Toggleable favorite-knapp.

**Props:** `active`, `onChange`, `size?` (`sm` | `md`).

**CSS:**
```css
@utility star-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: var(--radius-sm);
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--color-muted);
  transition: color var(--duration-fast) var(--ease-out),
              background var(--duration-fast) var(--ease-out);
}

@utility star-toggle:hover {
  background: var(--color-subtle);
  color: var(--color-fg);
}

@utility star-toggle-active {
  color: #F5A623;  /* Linear's yellow */
}
```

**Bruk:**
```jsx
<StarToggle active={isStarred} onChange={setStarred} aria-label="Toggle favorite" />
```

---

## 8. CTA Pair (Hero-pattern)

Standard "primary + secondary" CTA-par i hero-seksjoner — `<Button variant="primary">` + `<Button variant="secondary">`. Stacked-pattern: solid white + dark outline (i light mode), eller solid + outline (i dark mode).

Dette er ikke et nytt komponent, men en **dokumentert komposisjon**:

```jsx
<Cluster gap="tight" justify="center">
  <Button size="lg" href="/start">Start earning</Button>
  <Button size="lg" variant="secondary" href="/join">Join as a fan</Button>
</Cluster>
```

For hero med dramatic spacing:
```css
@utility cta-pair {
  display: inline-flex;
  gap: var(--gap-tight);
  flex-wrap: wrap;
  justify-content: center;
}
```

---

## 9. Counter Nav

Brukes på sider med navigerbar liste — "02 / 145" + prev/next-pile. Linear bruker dette på issue-detalj-siden.

**Props:** `current`, `total`, `onPrev`, `onNext`.

**CSS:**
```css
@utility counter-nav {
  display: inline-flex;
  align-items: center;
  gap: var(--gap-tight);
  font-size: var(--text-sm);
  font-variant-numeric: tabular-nums;
  color: var(--color-muted);
}

@utility counter-nav-position {
  font-weight: var(--font-weight-medium);
}

@utility counter-nav-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: var(--radius-sm);
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--color-muted);
}
@utility counter-nav-button:hover {
  background: var(--color-subtle);
  color: var(--color-fg);
}
@utility counter-nav-button:disabled { opacity: 0.3; cursor: not-allowed; }
```

**Bruk:**
```jsx
<CounterNav current={2} total={145} onPrev={...} onNext={...} />
```

---

## 10. Selection Group

Multi-color legend / kategori-velger fra Stacked sin revenue-chart. Pills med farget dot + label.

**Props:** `items` (array av `{ id, label, color }`), `selected?` (array av id), `onChange?`.

**CSS:**
```css
@utility selection-group {
  display: inline-flex;
  flex-wrap: wrap;
  gap: var(--gap-tight);
}

@utility selection-group-item {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  padding-block: 0.25rem;
  padding-inline: 0.625rem;
  border-radius: var(--radius-full);
  border: var(--border-card);
  background: transparent;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
  cursor: pointer;
}

@utility selection-group-item-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: var(--radius-full);
  flex-shrink: 0;
}

@utility selection-group-item[aria-pressed="true"] {
  background: var(--color-subtle);
}
```

**Bruk:**
```jsx
<SelectionGroup
  items={[
    { id: 'subs', label: 'Subs', color: 'var(--chart-1)' },
    { id: 'ppv', label: 'PPV', color: 'var(--chart-2)' },
    { id: 'tips', label: 'Tips', color: 'var(--chart-3)' },
    /* ... */
  ]}
  selected={selectedCategories}
  onChange={setSelectedCategories}
/>
```

---

## Felles refinements lagt til i samme batch

Disse er ikke patterns, men globale forbedringer (definert i `base.css` eller `effects.css`):

**Focus-ring via box-shadow** (smoother enn outline, følger border-radius):
```css
*:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}
/* Komponenter som har egne backgrounds bruker den eksisterende outline-tilnærmingen */
```

**Selection-styling:**
```css
::selection {
  background: color-mix(in oklch, var(--color-accent) 30%, transparent);
  color: var(--color-fg);
}
```

**Scrollbar (webkit + firefox):**
```css
* {
  scrollbar-width: thin;
  scrollbar-color: var(--color-border) transparent;
}
*::-webkit-scrollbar { width: 8px; height: 8px; }
*::-webkit-scrollbar-track { background: transparent; }
*::-webkit-scrollbar-thumb {
  background: var(--color-border);
  border-radius: var(--radius-full);
}
*::-webkit-scrollbar-thumb:hover { background: var(--color-muted); }
```

**Prefers-color-scheme auto-detect (v3 — håndteres via localStorage-script):**
```html
<input id="dark" type="checkbox" class="sr-only">
<script>
(function() {
  var key = 'nordover-theme';
  var input = document.getElementById('dark');
  var saved = localStorage.getItem(key);
  if (saved === 'dark') input.checked = true;
  else if (saved === 'light') input.checked = false;
  else if (matchMedia('(prefers-color-scheme: dark)').matches) input.checked = true;
  input.addEventListener('change', function() {
    localStorage.setItem(key, this.checked ? 'dark' : 'light');
  });
})();
</script>
```
Avgjørelses-rekkefølge: lagret valg > system-preferanse > markup-default. `:has(#dark:checked)`-CSS-mekanismen er uendret. *(v1-spec brukte `[data-theme="light"]` — reversert av [v3 Rebuilding](../decisions/2026-05-27-v3-rebuilding.md).)*

**Glow under primary CTA (tokens-app):** brand-overstyring kan slå på via:
```css
.btn-primary {
  filter: drop-shadow(var(--button-glow));
}
```

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: patterns-basis-batch2](../decisions/2026-05-27-patterns-basis-batch2.md)
