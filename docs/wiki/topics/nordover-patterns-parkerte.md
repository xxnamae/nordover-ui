# Patterns — tidligere parkerte (app-side)

Fire patterns som ble parkert under fase 2A pga reelle arkitekturvalg. Spec'et nå med eksplisitte beslutninger.

**Komponenter:** Multi-step Wizard, Inline Edit, Filter Bar, Notification Feed.

Se [decision 2026-05-27 — patterns-parkerte](../decisions/2026-05-27-patterns-parkerte.md).

---

## 1. Multi-step Wizard

For onboarding-flow, multi-page-skjemaer, opprette-prosesser. Linear (ikke tree-graf) flow med back/next-navigasjon.

**Props (Wizard):** `steps` (array av `{ id, label, description? }`), `currentStep`, `onStepChange`, `onComplete`, `validateStep?` (async function).

**Props (WizardStep):** `id`, `children`.

**Arkitektur:**
- Kontrollert state (parent eier `currentStep`).
- Per-step validation via `validateStep(stepId, data) → Promise<boolean | errors>`.
- Linear flow (ingen "hopp over"), men `back` er alltid tillatt.
- Progress-indicator viser visited + current + upcoming.
- Mobile: progress-indicator kollapser til "Steg 2 av 5"-tekst.

**CSS:**
```css
@utility wizard {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
  max-width: 48rem;
  margin-inline: auto;
}

@utility wizard-progress {
  display: flex;
  align-items: center;
  gap: var(--gap-tight);
  padding-block: var(--gap-component);
}

@utility wizard-progress-step {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex: 1;
  min-width: 0;
}

@utility wizard-progress-circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.75rem;
  height: 1.75rem;
  border-radius: var(--radius-full);
  background: var(--color-subtle);
  border: var(--border-card);
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--color-muted);
  flex-shrink: 0;
  transition: background var(--duration-fast) var(--ease-out),
              border-color var(--duration-fast) var(--ease-out);
}

@utility wizard-progress-step[data-state="current"] .wizard-progress-circle {
  background: var(--color-accent);
  border-color: var(--color-accent);
  color: var(--color-accent-fg);
}

@utility wizard-progress-step[data-state="complete"] .wizard-progress-circle {
  background: var(--color-success);
  border-color: var(--color-success);
  color: white;
}

@utility wizard-progress-step[data-state="complete"] .wizard-progress-circle::before {
  content: "✓";
}

@utility wizard-progress-label {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@utility wizard-progress-step[data-state="current"] .wizard-progress-label {
  color: var(--color-fg);
}

@utility wizard-progress-connector {
  flex: 1;
  height: 1px;
  background: var(--color-border);
  margin-inline: 0.5rem;
}

@utility wizard-progress-step[data-state="complete"] + .wizard-progress-connector {
  background: var(--color-success);
}

/* Mobile: kollapser til text-only */
@container (max-width: 36rem) {
  @utility wizard-progress { display: none; }
  @utility wizard-progress-mobile {
    display: block;
    font-size: var(--text-sm);
    color: var(--color-muted);
    font-weight: var(--font-weight-medium);
  }
}

@utility wizard-step {
  display: flex;
  flex-direction: column;
  gap: var(--gap-component);
  min-height: 16rem;
}

@utility wizard-step-header {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

@utility wizard-step-title {
  font-size: var(--text-2xl);
  font-weight: var(--font-weight-semibold);
}

@utility wizard-step-description {
  color: var(--color-muted);
}

@utility wizard-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: var(--gap-component);
  border-top: var(--border-divider);
}
```

**React:**
```jsx
function Wizard({ steps, currentStep, onStepChange, onComplete, validateStep, children }) {
  const currentIndex = steps.findIndex(s => s.id === currentStep);
  const [validating, setValidating] = useState(false);
  const [errors, setErrors] = useState(null);

  const goNext = async () => {
    if (validateStep) {
      setValidating(true);
      const result = await validateStep(currentStep);
      setValidating(false);
      if (result !== true) {
        setErrors(result);
        return;
      }
    }
    setErrors(null);
    if (currentIndex === steps.length - 1) onComplete?.();
    else onStepChange(steps[currentIndex + 1].id);
  };

  const goBack = () => {
    setErrors(null);
    if (currentIndex > 0) onStepChange(steps[currentIndex - 1].id);
  };

  return (
    <div className="wizard">
      <nav className="wizard-progress" aria-label="Fremdrift">
        {steps.map((step, i) => {
          const state = i < currentIndex ? "complete" : i === currentIndex ? "current" : "upcoming";
          return (
            <Fragment key={step.id}>
              <div className="wizard-progress-step" data-state={state}>
                <span className="wizard-progress-circle">
                  {state !== "complete" && i + 1}
                </span>
                <span className="wizard-progress-label">{step.label}</span>
              </div>
              {i < steps.length - 1 && <div className="wizard-progress-connector" />}
            </Fragment>
          );
        })}
      </nav>
      <p className="wizard-progress-mobile">
        Steg {currentIndex + 1} av {steps.length}: {steps[currentIndex].label}
      </p>

      {children /* WizardStep components — kun current rendres */}

      <div className="wizard-actions">
        <Button variant="ghost" onClick={goBack} disabled={currentIndex === 0}>
          Tilbake
        </Button>
        <Button onClick={goNext} loading={validating}>
          {currentIndex === steps.length - 1 ? "Fullfør" : "Neste"}
        </Button>
      </div>
    </div>
  );
}

function WizardStep({ id, children }) {
  const { currentStep } = useWizardContext();
  if (id !== currentStep) return null;
  return <div className="wizard-step">{children}</div>;
}
```

**Bruk:**
```jsx
<Wizard
  steps={[
    { id: "konto", label: "Konto" },
    { id: "team", label: "Team" },
    { id: "fakturering", label: "Fakturering" },
    { id: "ferdig", label: "Ferdig" },
  ]}
  currentStep={step}
  onStepChange={setStep}
  validateStep={async (id) => { /* validate */ return true; }}
  onComplete={() => router.push("/dashboard")}
>
  <WizardStep id="konto">
    <div className="wizard-step-header">
      <h2 className="wizard-step-title">Lag konto</h2>
      <p className="wizard-step-description">Vi trenger litt info om deg.</p>
    </div>
    <Field label="Navn" required><Input name="name" /></Field>
    <Field label="E-post" required><Input type="email" name="email" /></Field>
  </WizardStep>
  {/* flere steg */}
</Wizard>
```

---

## 2. Inline Edit

Click-to-edit pattern for celler, titler, beskrivelser. Veksler mellom read- og edit-mode.

**Props:** `value`, `onSave`, `placeholder?`, `multiline?` (default false), `validate?`, `saveOn?` (`blur` | `enter` | `explicit`, default `blur`).

**Arkitektur:**
- Tre tilstander: `idle` (read), `editing` (input synlig), `saving` (loading).
- Default save-strategi: `blur` (klikk utenfor) eller `Enter` for single-line.
- `Esc` avbryter alltid og reverter til original.
- Optimistisk update: vis ny verdi umiddelbart, rollback ved feil.
- `explicit`-modus viser save/cancel-knapper.

**CSS:**
```css
@utility inline-edit {
  position: relative;
  display: inline-flex;
  align-items: center;
  min-width: 0;
}

@utility inline-edit-display {
  display: inline-block;
  padding: 0.25rem 0.5rem;
  border-radius: var(--radius-sm);
  border: 1px solid transparent;
  cursor: text;
  color: var(--color-fg);
  min-width: 0;
}

@utility inline-edit-display:hover {
  background: var(--color-subtle);
  border-color: var(--color-border);
}

@utility inline-edit-display[data-empty="true"] {
  color: var(--color-muted);
  font-style: italic;
}

@utility inline-edit-input {
  padding: 0.25rem 0.5rem;
  border: 1px solid var(--color-focus);
  border-radius: var(--radius-sm);
  background: var(--color-bg);
  font-family: inherit;
  font-size: inherit;
  font-weight: inherit;
  color: var(--color-fg);
  outline: none;
  width: 100%;
  min-width: 6rem;
}

@utility inline-edit-input:focus-visible {
  box-shadow: var(--focus-ring);
}

@utility inline-edit-textarea {
  /* arver fra .inline-edit-input */
  resize: vertical;
  min-height: 3rem;
  font-family: inherit;
  line-height: 1.5;
}

@utility inline-edit-actions {
  display: inline-flex;
  gap: 0.25rem;
  margin-inline-start: 0.375rem;
}

@utility inline-edit-saving {
  position: absolute;
  inset: 0;
  display: inline-flex;
  align-items: center;
  padding-inline: 0.5rem;
  background: color-mix(in oklch, var(--color-bg) 70%, transparent);
}
```

**React:**
```jsx
function InlineEdit({
  value,
  onSave,
  placeholder = "Klikk for å redigere",
  multiline = false,
  validate,
  saveOn = "blur",
}) {
  const [mode, setMode] = useState("idle");
  const [draft, setDraft] = useState(value);
  const [error, setError] = useState(null);
  const inputRef = useRef(null);

  useEffect(() => {
    if (mode === "editing") inputRef.current?.focus();
  }, [mode]);

  const startEdit = () => {
    setDraft(value);
    setMode("editing");
  };

  const cancel = () => {
    setDraft(value);
    setMode("idle");
    setError(null);
  };

  const save = async () => {
    if (draft === value) return cancel();
    if (validate) {
      const result = validate(draft);
      if (result !== true) {
        setError(result);
        return;
      }
    }
    setMode("saving");
    try {
      await onSave(draft);
      setMode("idle");
    } catch (e) {
      setError(e.message);
      setMode("editing");
    }
  };

  const handleKey = (e) => {
    if (e.key === "Escape") {
      e.preventDefault();
      cancel();
    } else if (e.key === "Enter" && !multiline && saveOn !== "explicit") {
      e.preventDefault();
      save();
    } else if (e.key === "Enter" && multiline && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      save();
    }
  };

  if (mode === "idle") {
    return (
      <span className="inline-edit">
        <span
          className="inline-edit-display"
          data-empty={!value}
          onClick={startEdit}
          tabIndex={0}
          onKeyDown={(e) => (e.key === "Enter" || e.key === " ") && startEdit()}
        >
          {value || placeholder}
        </span>
      </span>
    );
  }

  const InputTag = multiline ? "textarea" : "input";
  return (
    <span className="inline-edit">
      <InputTag
        ref={inputRef}
        className={multiline ? "inline-edit-textarea" : "inline-edit-input"}
        value={draft}
        onChange={(e) => { setDraft(e.target.value); setError(null); }}
        onBlur={saveOn === "blur" ? save : undefined}
        onKeyDown={handleKey}
        disabled={mode === "saving"}
        aria-invalid={Boolean(error)}
      />
      {saveOn === "explicit" && mode === "editing" && (
        <span className="inline-edit-actions">
          <Button size="sm" onClick={save}>Lagre</Button>
          <Button size="sm" variant="ghost" onClick={cancel}>Avbryt</Button>
        </span>
      )}
      {mode === "saving" && <span className="inline-edit-saving"><Spinner size="sm" /></span>}
      {error && <p className="field-error" style={{ marginTop: 4 }}>{error}</p>}
    </span>
  );
}
```

**Bruk:**
```jsx
<h1>
  <InlineEdit value={title} onSave={updateTitle} />
</h1>

<InlineEdit
  value={description}
  onSave={updateDescription}
  multiline
  saveOn="explicit"
  placeholder="Legg til beskrivelse..."
/>
```

**A11y:**
- Display-mode er fokuserbar via `tabIndex={0}`, Enter/Space åpner edit-mode.
- Input får auto-focus når mode skifter.
- `aria-invalid` settes ved valideringsfeil.

---

## 3. Filter Bar

For listevisninger (Data Table, kort-grids). Kombinerer søk + dropdown-filtre + aktive filter-pills.

**Props:**
- `search`: string (controlled)
- `onSearchChange`
- `filters`: array av filter-definisjoner `{ id, label, type: "select" | "multi" | "date-range" | "boolean", options?: [], value? }`
- `onFilterChange`
- `onClearAll?`

**Arkitektur:**
- Kontrollert state — Filter Bar er stateless, parent eier state.
- URL-sync er ansvar av parent (parent kan koble til router-query).
- Aktive filtre vises som pills under bar-en (kan klikkes vekk).
- "Legg til filter"-dropdown for valgfrie filtre som ikke er synlige.
- Søk har debounce — parent er ansvarlig (komponenten emit'er kun raw text).

**CSS:**
```css
@utility filter-bar {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility filter-bar-row {
  display: flex;
  align-items: center;
  gap: var(--gap-tight);
  flex-wrap: wrap;
}

@utility filter-bar-search {
  flex: 1;
  min-width: 12rem;
  position: relative;
}

@utility filter-bar-search-icon {
  position: absolute;
  inset-inline-start: 0.625rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-muted);
  width: 0.875rem;
  height: 0.875rem;
  pointer-events: none;
}

@utility filter-bar-search-input {
  /* .form-input */
  padding-inline-start: 2rem;
}

@utility filter-bar-active {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--gap-tight);
  padding-block: 0.25rem;
}

@utility filter-bar-active-label {
  font-size: var(--text-xs);
  color: var(--color-muted);
  font-weight: var(--font-weight-medium);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
}

@utility filter-bar-clear {
  font-size: var(--text-sm);
  color: var(--color-muted);
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 0.25rem 0.5rem;
}

@utility filter-bar-clear:hover {
  color: var(--color-fg);
  text-decoration: underline;
}

@utility filter-bar-add {
  /* dropdown-trigger som .btn-ghost-sm med + ikon */
}
```

**React:**
```jsx
function FilterBar({ search, onSearchChange, filters, onFilterChange, onClearAll }) {
  const activeFilters = filters.filter(f => f.value !== undefined && f.value !== null && f.value !== "");
  const inactiveFilters = filters.filter(f => f.value === undefined);

  return (
    <div className="filter-bar">
      <div className="filter-bar-row">
        <div className="filter-bar-search">
          <SearchIcon className="filter-bar-search-icon" />
          <input
            type="search"
            className="form-input filter-bar-search-input"
            placeholder="Søk..."
            value={search}
            onChange={(e) => onSearchChange(e.target.value)}
          />
        </div>

        {filters
          .filter(f => f.alwaysVisible)
          .map(f => (
            <FilterDropdown key={f.id} filter={f} onChange={onFilterChange} />
          ))}

        {inactiveFilters.length > 0 && (
          <DropdownMenu.Root>
            <DropdownMenu.Trigger asChild>
              <Button variant="ghost" size="sm" leftIcon={<PlusIcon />}>Legg til filter</Button>
            </DropdownMenu.Trigger>
            <DropdownMenu.Content className="menu-content">
              {inactiveFilters.map(f => (
                <DropdownMenu.Item
                  key={f.id}
                  className="menu-item"
                  onClick={() => onFilterChange(f.id, getDefaultValue(f))}
                >
                  {f.label}
                </DropdownMenu.Item>
              ))}
            </DropdownMenu.Content>
          </DropdownMenu.Root>
        )}
      </div>

      {activeFilters.length > 0 && (
        <div className="filter-bar-active">
          <span className="filter-bar-active-label">Filtre:</span>
          {activeFilters.map(f => (
            <Tag
              key={f.id}
              variant="outline"
              onRemove={() => onFilterChange(f.id, undefined)}
            >
              {f.label}: {formatFilterValue(f)}
            </Tag>
          ))}
          {onClearAll && (
            <button className="filter-bar-clear" onClick={onClearAll}>
              Fjern alle
            </button>
          )}
        </div>
      )}
    </div>
  );
}
```

**Bruk:**
```jsx
<FilterBar
  search={searchQuery}
  onSearchChange={setSearchQuery}
  filters={[
    { id: "status", label: "Status", type: "multi", options: STATUSES, value: filters.status, alwaysVisible: true },
    { id: "assignee", label: "Tildelt", type: "select", options: USERS, value: filters.assignee },
    { id: "priority", label: "Prioritet", type: "select", options: PRIORITIES, value: filters.priority },
    { id: "created", label: "Opprettet", type: "date-range", value: filters.created },
  ]}
  onFilterChange={(id, value) => setFilters({ ...filters, [id]: value })}
  onClearAll={() => setFilters({})}
/>
```

---

## 4. Notification Feed

For inbox/varslings-dropdown. Forskjellig fra Activity Stream — disse er **actionable** (klikk for å åpne, marker lest, dismiss).

**Props (NotificationFeed):** `notifications`, `onMarkRead`, `onDismiss`, `onMarkAllRead?`, `onLoadMore?`.
**Props (NotificationItem):** `id`, `icon?`, `title`, `description?`, `timestamp`, `read`, `actor?` (avatar+name), `href?` (klikk-target).

**Arkitektur:**
- Liste med uleste + leste, separert visuelt (uleste øverst, lest-rad over divider).
- Klikk-på-rad: navigerer til `href` + marker som lest.
- Hover viser dismiss-action.
- "Marker alle som lest" øverst når det finnes uleste.
- Tom-state med illustration.

**CSS:**
```css
@utility notification-feed {
  display: flex;
  flex-direction: column;
  max-height: 32rem;
  overflow-y: auto;
}

@utility notification-feed-header {
  position: sticky;
  top: 0;
  z-index: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--gap-tight) var(--gap-component);
  background: var(--color-bg);
  border-bottom: var(--border-divider);
}

@utility notification-feed-title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-semibold);
}

@utility notification-feed-mark-all {
  font-size: var(--text-sm);
  color: var(--color-accent);
  background: transparent;
  border: none;
  cursor: pointer;
}

@utility notification-feed-mark-all:hover {
  text-decoration: underline;
}

@utility notification-item {
  display: flex;
  gap: var(--gap-tight);
  padding: var(--gap-tight) var(--gap-component);
  border-bottom: var(--border-divider);
  cursor: pointer;
  text-decoration: none;
  color: var(--color-fg);
  position: relative;
  transition: background var(--duration-fast) var(--ease-out);
}

@utility notification-item:hover {
  background: var(--color-subtle);
}

@utility notification-item[data-read="false"] {
  background: color-mix(in oklch, var(--color-accent) 4%, var(--color-bg));
}

@utility notification-item[data-read="false"]::before {
  content: "";
  position: absolute;
  inset-inline-start: 0.5rem;
  top: 50%;
  transform: translateY(-50%);
  width: 0.5rem;
  height: 0.5rem;
  border-radius: var(--radius-full);
  background: var(--color-accent);
}

@utility notification-item[data-read="false"] {
  padding-inline-start: calc(var(--gap-component) + 0.75rem);
}

@utility notification-item-avatar {
  flex-shrink: 0;
}

@utility notification-item-icon {
  width: 2rem;
  height: 2rem;
  border-radius: var(--radius-full);
  background: var(--color-subtle);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: var(--color-muted);
  flex-shrink: 0;
}

@utility notification-item-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
  min-width: 0;
}

@utility notification-item-title {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
}

@utility notification-item-title strong {
  font-weight: var(--font-weight-semibold);
}

@utility notification-item-description {
  font-size: var(--text-sm);
  color: var(--color-muted);
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

@utility notification-item-timestamp {
  font-size: var(--text-xs);
  color: var(--color-muted);
}

@utility notification-item-dismiss {
  position: absolute;
  top: 0.5rem;
  inset-inline-end: 0.5rem;
  opacity: 0;
  width: 1.25rem;
  height: 1.25rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--color-bg);
  border: var(--border-card);
  border-radius: var(--radius-sm);
  cursor: pointer;
  color: var(--color-muted);
}

@utility notification-item:hover .notification-item-dismiss {
  opacity: 1;
}

@utility notification-feed-section-divider {
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
  color: var(--color-muted);
  padding: var(--gap-tight) var(--gap-component);
  background: var(--color-subtle);
}

@utility notification-feed-empty {
  /* .empty-state, mindre padding */
  padding-block: var(--gap-component);
}

@utility notification-feed-load-more {
  display: flex;
  justify-content: center;
  padding: var(--gap-component);
}
```

**React:**
```jsx
function NotificationFeed({ notifications, onMarkRead, onDismiss, onMarkAllRead, onLoadMore }) {
  const unread = notifications.filter(n => !n.read);
  const read = notifications.filter(n => n.read);

  if (notifications.length === 0) {
    return (
      <div className="notification-feed">
        <EmptyState
          illustration="empty-inbox"
          title="Ingen varslinger"
          description="Vi gir beskjed her når noe nytt skjer."
          className="notification-feed-empty"
        />
      </div>
    );
  }

  return (
    <div className="notification-feed">
      <div className="notification-feed-header">
        <p className="notification-feed-title">Varslinger</p>
        {unread.length > 0 && onMarkAllRead && (
          <button className="notification-feed-mark-all" onClick={onMarkAllRead}>
            Marker alle som lest
          </button>
        )}
      </div>

      {unread.length > 0 && (
        <>
          <div className="notification-feed-section-divider">Nye ({unread.length})</div>
          {unread.map(n => (
            <NotificationItem key={n.id} {...n} onMarkRead={onMarkRead} onDismiss={onDismiss} />
          ))}
        </>
      )}

      {read.length > 0 && (
        <>
          <div className="notification-feed-section-divider">Tidligere</div>
          {read.map(n => (
            <NotificationItem key={n.id} {...n} onMarkRead={onMarkRead} onDismiss={onDismiss} />
          ))}
        </>
      )}

      {onLoadMore && (
        <div className="notification-feed-load-more">
          <Button variant="ghost" size="sm" onClick={onLoadMore}>Vis flere</Button>
        </div>
      )}
    </div>
  );
}

function NotificationItem({ id, actor, icon, title, description, timestamp, read, href, onMarkRead, onDismiss }) {
  const handleClick = (e) => {
    if (!read) onMarkRead?.(id);
    // navigation skjer via href naturlig
  };

  return (
    <a
      className="notification-item"
      data-read={read}
      href={href}
      onClick={handleClick}
    >
      {actor ? (
        <Avatar name={actor.name} src={actor.avatar} size="sm" className="notification-item-avatar" />
      ) : icon ? (
        <span className="notification-item-icon">{icon}</span>
      ) : null}
      <div className="notification-item-body">
        <p className="notification-item-title">{title}</p>
        {description && <p className="notification-item-description">{description}</p>}
        <span className="notification-item-timestamp">{formatRelative(timestamp)}</span>
      </div>
      {onDismiss && (
        <button
          className="notification-item-dismiss"
          aria-label="Avvis"
          onClick={(e) => { e.preventDefault(); e.stopPropagation(); onDismiss(id); }}
        >
          <XIcon />
        </button>
      )}
    </a>
  );
}
```

**Bruk i header (Linear-style notification-dropdown):**
```jsx
<DropdownMenu.Root>
  <DropdownMenu.Trigger asChild>
    <Button iconOnly variant="ghost" aria-label="Varslinger" style={{ position: "relative" }}>
      <BellIcon />
      {unreadCount > 0 && (
        <Badge tone="danger" style={{ position: "absolute", top: -2, right: -2 }}>{unreadCount}</Badge>
      )}
    </Button>
  </DropdownMenu.Trigger>
  <DropdownMenu.Portal>
    <DropdownMenu.Content className="menu-content" style={{ width: "24rem", padding: 0 }}>
      <NotificationFeed
        notifications={notifications}
        onMarkRead={markRead}
        onDismiss={dismiss}
        onMarkAllRead={markAllRead}
        onLoadMore={loadMore}
      />
    </DropdownMenu.Content>
  </DropdownMenu.Portal>
</DropdownMenu.Root>
```

---

## Felles arkitektur-noter

- **Alle 4 komponenter er kontrollert** (parent eier state) — gjør dem trivielt integrerbare med URL-state, server-state-libraries (TanStack Query, SWR), eller form-libraries.
- **Optimistic UI** er ansvar av parent — komponentene rapporterer events, ikke håndterer rollback.
- **A11y:** Wizard har `aria-label="Fremdrift"` på progress. InlineEdit display-mode er fokuserbar. FilterBar bruker semantic `<input type="search">`. NotificationItem er `<a>` for native navigasjon.

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: patterns-parkerte](../decisions/2026-05-27-patterns-parkerte.md)
