# Patterns — basis-batch

Ti konvensjonelle composite components batchet i én økt fordi de har lav arkitektur-overflate (få reelle valg, mye konvensjon). Bygger utelukkende på eksisterende tokens og primitiver.

**Komponentene:** Tag, Badge, Avatar, Spinner, Tooltip, Breadcrumbs, Pagination, Skeleton, Divider, Kbd.

Se [decision 2026-05-27 — patterns-basis-batch1](../decisions/2026-05-27-patterns-basis-batch1.md).

---

## 1. Tag

Liten inline-label for kategorier, taxonomi, statuser.

**Props:** `variant` (`subtle` | `solid` | `outline`), `tone` (`neutral` | `danger` | `success` | `warning` | `info`), `size` (`sm` | `md`), `onRemove?` (gjør den dismissible).

**CSS:**
```css
@utility tag {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding-block: 0.125rem;
  padding-inline: 0.5rem;
  font-size: var(--text-xs);
  font-weight: var(--font-weight-medium);
  border-radius: var(--radius-sm);
  white-space: nowrap;
  line-height: 1.4;
  background: var(--color-subtle);
  color: var(--color-fg);
}

@utility tag-md {
  font-size: var(--text-sm);
  padding-block: 0.25rem;
  padding-inline: 0.625rem;
}

@utility tag-solid {
  background: var(--color-accent);
  color: var(--color-accent-fg);
}

@utility tag-outline {
  background: transparent;
  border: var(--border-card);
}

@utility tag-tone-danger {
  --color-accent: var(--color-error);
  background: color-mix(in oklch, var(--color-error) 12%, var(--color-bg));
  color: var(--color-error);
}
@utility tag-tone-success {
  --color-accent: var(--color-success);
  background: color-mix(in oklch, var(--color-success) 12%, var(--color-bg));
  color: var(--color-success);
}
@utility tag-tone-warning {
  --color-accent: var(--color-warning);
  background: color-mix(in oklch, var(--color-warning) 14%, var(--color-bg));
  color: color-mix(in oklch, var(--color-warning) 70%, black);
}
@utility tag-tone-info {
  --color-accent: var(--color-info, var(--color-focus));
  background: color-mix(in oklch, var(--color-info, var(--color-focus)) 12%, var(--color-bg));
  color: var(--color-info, var(--color-focus));
}
```

**Bruk:**
```jsx
<Cluster gap="tight">
  <Tag>Design</Tag>
  <Tag tone="success">Aktiv</Tag>
  <Tag tone="danger" variant="solid">Slettet</Tag>
  <Tag tone="warning" onRemove={() => ...}>Venter</Tag>
</Cluster>
```

---

## 2. Badge

Liten teller eller dot for notifikasjoner, status-indikator.

**Props:** `dot?` (boolean — vis kun prikk), `tone` (`neutral` | `danger` | `success` | `warning`), `max?` (number — vis "99+" hvis over).

**CSS:**
```css
@utility badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 1.25rem;
  height: 1.25rem;
  padding-inline: 0.375rem;
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  line-height: 1;
  border-radius: var(--radius-full);
  background: var(--color-accent);
  color: var(--color-accent-fg);
  font-variant-numeric: tabular-nums;
}

@utility badge-dot {
  width: 0.5rem;
  height: 0.5rem;
  min-width: unset;
  padding: 0;
}

@utility badge-tone-danger { background: var(--color-error); color: white; }
@utility badge-tone-success { background: var(--color-success); color: white; }
@utility badge-tone-warning { background: var(--color-warning); color: black; }
```

**Bruk:**
```jsx
<button class="relative">
  <Bell />
  <Badge tone="danger" class="absolute -top-1 -right-1">3</Badge>
</button>

<Cluster gap="tight" align="center">
  <Badge dot tone="success" />
  <span>Online</span>
</Cluster>

<Badge max={99}>{142}</Badge>   {/* → "99+" */}
```

---

## 3. Avatar

Sirkulær bilde- eller initial-visning.

**Props:** `src?`, `alt?`, `name?` (for initialer-fallback), `size` (`xs` | `sm` | `md` | `lg` | `xl`).

**CSS:**
```css
@utility avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-full);
  background: var(--color-subtle);
  color: var(--color-fg);
  font-weight: var(--font-weight-medium);
  overflow: hidden;
  flex-shrink: 0;
  user-select: none;
  width: 2.5rem;
  height: 2.5rem;
  font-size: var(--text-sm);
}

@utility avatar-xs { width: 1.5rem; height: 1.5rem; font-size: 0.625rem; }
@utility avatar-sm { width: 2rem; height: 2rem; font-size: var(--text-xs); }
@utility avatar-lg { width: 3rem; height: 3rem; font-size: var(--text-md); }
@utility avatar-xl { width: 4rem; height: 4rem; font-size: var(--text-lg); }

@utility avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@utility avatar-group {
  display: inline-flex;
  isolation: isolate;
}

@utility avatar-group .avatar {
  border: 2px solid var(--color-bg);
  margin-inline-start: -0.5rem;
}

@utility avatar-group .avatar:first-child {
  margin-inline-start: 0;
}
```

**React-stub:**
```jsx
function Avatar({ src, alt, name, size = "md", ...rest }) {
  const sizeClass = size !== "md" ? `avatar-${size}` : "";
  const initials = name
    ? name.split(" ").map(w => w[0]).slice(0, 2).join("").toUpperCase()
    : null;

  return (
    <span className={`avatar ${sizeClass}`} {...rest}>
      {src ? <img src={src} alt={alt ?? name ?? ""} /> : initials}
    </span>
  );
}
```

**Bruk:**
```jsx
<Avatar name="Eirik Foleide" />              {/* "EF" */}
<Avatar src="/avatar.jpg" alt="Eirik" />
<Avatar size="xl" name="Anna B" />

<AvatarGroup>
  <Avatar name="A B" />
  <Avatar name="C D" />
  <Avatar name="E F" />
  <Avatar size="md">+3</Avatar>
</AvatarGroup>
```

---

## 4. Spinner

Loading-indikator. Brukes av Button loading-state og frittstående.

**Props:** `size` (`sm` | `md` | `lg`). Inherits `color` via `currentColor`.

**CSS:**
```css
@utility spinner {
  display: inline-block;
  width: 1rem;
  height: 1rem;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: var(--radius-full);
  animation: spinner-spin 0.65s linear infinite;
}

@utility spinner-sm {
  width: 0.875rem;
  height: 0.875rem;
  border-width: 1.5px;
}

@utility spinner-lg {
  width: 1.5rem;
  height: 1.5rem;
  border-width: 2.5px;
}

@keyframes spinner-spin {
  to { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  @utility spinner {
    animation-duration: 2s;   /* sakte i stedet for av — fortsatt synlig at noe skjer */
  }
}
```

**Bruk:**
```jsx
<Spinner />                              {/* default md, currentColor */}
<Spinner size="lg" />
<div style={{ color: 'var(--color-accent)' }}><Spinner /></div>
```

---

## 5. Tooltip

Hover/focus popup. **Basis-versjon med ren CSS** — for komplekse tilfeller (smart positionering, portals, kollisjons-deteksjon) bruk Radix Tooltip senere.

**Props:** `content` (string eller node), `position` (`top` | `bottom` | `left` | `right`, default `top`).

**Begrensning:** Ingen smart positionering. Kun for korte tekster og forutsigbar layout.

**CSS:**
```css
@utility tooltip-trigger {
  position: relative;
  display: inline-flex;
}

@utility tooltip {
  position: absolute;
  bottom: calc(100% + 0.5rem);
  left: 50%;
  transform: translateX(-50%) translateY(-2px);
  background: var(--color-fg);
  color: var(--color-bg);
  padding-block: 0.25rem;
  padding-inline: 0.5rem;
  border-radius: var(--radius-sm);
  font-size: var(--text-xs);
  font-weight: var(--font-weight-medium);
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--duration-fast) var(--ease-out),
              transform var(--duration-fast) var(--ease-out);
  box-shadow: var(--shadow-tooltip);
  z-index: var(--z-tooltip);
}

.tooltip-trigger:hover > .tooltip,
.tooltip-trigger:focus-visible > .tooltip,
.tooltip-trigger:focus-within > .tooltip {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}
```

**Bruk:**
```jsx
<Tooltip content="Sletter dette permanent">
  <Button iconOnly variant="ghost" aria-label="Slett"><Trash /></Button>
</Tooltip>
```

---

## 6. Breadcrumbs

Hierarkisk navigasjon.

**Props:** `separator?` (default `"•"`), children = array av items eller `<BreadcrumbItem>`.

**CSS:**
```css
@utility breadcrumbs {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--gap-tight);
  font-size: var(--text-sm);
  color: var(--color-muted);
}

@utility breadcrumb-item {
  color: var(--color-muted);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}

@utility breadcrumb-item:hover { color: var(--color-fg); }

@utility breadcrumb-current {
  color: var(--color-fg);
  font-weight: var(--font-weight-medium);
}

@utility breadcrumb-separator {
  user-select: none;
  opacity: 0.5;
}
```

**Bruk:**
```jsx
<Breadcrumbs>
  <BreadcrumbItem href="/">Hjem</BreadcrumbItem>
  <BreadcrumbItem href="/saker">Saker</BreadcrumbItem>
  <BreadcrumbItem current>Sak #142</BreadcrumbItem>
</Breadcrumbs>
```

`<nav aria-label="Brødsmuler">` wrapper i React-implementasjonen for a11y.

---

## 7. Pagination

Side-navigasjon for paginerte data.

**Props:** `current`, `total`, `siblingCount` (default 1), `onPageChange`.

**CSS:**
```css
@utility pagination {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

@utility pagination-item {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 2rem;
  height: 2rem;
  padding-inline: 0.5rem;
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  font-variant-numeric: tabular-nums;
  border-radius: var(--radius-md);
  color: var(--color-fg);
  text-decoration: none;
  background: transparent;
  border: none;
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-out);
}

@utility pagination-item:hover:not(:disabled) {
  background: var(--color-subtle);
}

@utility pagination-current {
  background: var(--color-fg);
  color: var(--color-bg);
}

@utility pagination-ellipsis {
  color: var(--color-muted);
  user-select: none;
}
```

**Algoritme for ellipsis (kort):** vis alltid first + last + (current ± siblingCount). Fyll med ellipsis hvor det er gap > 1.

**Bruk:**
```jsx
<Pagination
  current={page}
  total={totalPages}
  onPageChange={setPage}
/>
```

---

## 8. Skeleton-loader

Animert placeholder mens innhold laster.

**Props:** `variant` (`text` | `circle` | `rect`), `width?`, `height?`, `lines?` (for text-variant, default 1).

**CSS:**
```css
@utility skeleton {
  display: block;
  background: linear-gradient(
    90deg,
    var(--color-subtle) 0%,
    color-mix(in oklch, var(--color-subtle) 50%, var(--color-bg)) 50%,
    var(--color-subtle) 100%
  );
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.5s ease-in-out infinite;
  border-radius: var(--radius-sm);
}

@utility skeleton-text {
  height: 1em;
  margin-block: 0.25em;
}

@utility skeleton-circle {
  border-radius: var(--radius-full);
}

@utility skeleton-rect {
  border-radius: var(--radius-md);
}

@keyframes skeleton-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

@media (prefers-reduced-motion: reduce) {
  @utility skeleton { animation: none; opacity: 0.7; }
}
```

**Bruk:**
```jsx
<Skeleton variant="text" width="60%" />
<Skeleton variant="text" lines={3} />
<Skeleton variant="circle" width="3rem" height="3rem" />
<Skeleton variant="rect" width="100%" height="12rem" />
```

`aria-busy="true"` på foreldre-container under loading.

---

## 9. Divider

Horisontal eller vertikal skille-linje, med valgfri label.

**Props:** `orientation` (`horizontal` | `vertical`, default horizontal), `label?` (vises midt på linjen).

**CSS:**
```css
@utility divider {
  border: none;
  border-top: var(--border-divider);
  margin-block: var(--gap-component);
  width: 100%;
}

@utility divider-vertical {
  border-top: none;
  border-left: var(--border-divider);
  margin-block: 0;
  margin-inline: var(--gap-component);
  align-self: stretch;
  width: 0;
}

@utility divider-labeled {
  display: flex;
  align-items: center;
  gap: 1rem;
  border: none;
  font-size: var(--text-xs);
  font-weight: var(--font-weight-semibold);
  color: var(--color-muted);
  text-transform: uppercase;
  letter-spacing: var(--tracking-widest);
}

@utility divider-labeled::before,
@utility divider-labeled::after {
  content: "";
  flex: 1;
  border-top: var(--border-divider);
}
```

**Bruk:**
```jsx
<Divider />
<Divider label="eller" />
<Cluster><span>A</span><Divider orientation="vertical" /><span>B</span></Cluster>
```

---

## 10. Kbd

Tastatur-tast for shortcuts og dokumentasjon.

**Props:** children = teksten på tasten.

**CSS:**
```css
@utility kbd {
  display: inline-flex;
  align-items: center;
  padding-block: 0.0625rem;
  padding-inline: 0.375rem;
  font-family: var(--font-mono);
  font-size: 0.85em;
  font-weight: var(--font-weight-medium);
  background: var(--color-subtle);
  color: var(--color-fg);
  border: var(--border-card);
  border-bottom-width: 2px;
  border-radius: var(--radius-sm);
  box-shadow: var(--shadow-xs);
  line-height: 1;
  vertical-align: baseline;
}
```

**Bruk:**
```jsx
<p>Trykk <Kbd>⌘</Kbd> + <Kbd>K</Kbd> for å åpne søk.</p>
```

---

## Felles prinsipper for batch C

- **Ingen nye tokens** — alle komponenter komponert fra eksisterende.
- **Polymorphic `as`-prop** der det gir mening (Tag, Avatar når den klikkes, Breadcrumb-items).
- **A11y:** Tooltip kobles til trigger via `aria-describedby`, Badge dot har `aria-label` for tilstand, Pagination wrapper i `<nav aria-label="Sidenavigasjon">`, Skeleton-foreldre har `aria-busy="true"`.
- **Reduced-motion:** Spinner blir 3x saktere (ikke av), Skeleton-shimmer stoppes med statisk opacity.
- **Sizes følger eksisterende skala** — sm/md/lg matcher Buttons der relevant.

## Hva som ikke er med (krever egen drodling)

- **Tooltip med smart positionering** (kollisjons-deteksjon, portals) — Radix Tooltip senere.
- **Pagination med URL-sync, jump-to-page-input** — bygges på toppen av basis-Pagination.
- **Avatar med presence-indikator** (online/offline-dot) — kombineres med Badge når trengs.

## Implementeringsrekkefølge

1. Lag `patterns-basis.css` med alle 10 `@utility`-blokker.
2. Lag React-komponenter i `@nordover/ui/patterns/`: Tag, Badge, Avatar, Spinner, Tooltip, Breadcrumbs, Pagination, Skeleton, Divider, Kbd.
3. TypeScript: diskriminerende unions der det er constraints (eks. Badge: `dot` ekskluderer children).
4. Import-rekkefølge: `tokens-*.css` → `base.css` → `typografi.css` → `layout.css` → `elevation.css` → `buttons.css` → `forms.css` → `patterns-basis.css` → `prose.css` → `clients/<slug>.css`.

## Se også

- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: patterns-basis-batch1](../decisions/2026-05-27-patterns-basis-batch1.md)
- Visuell spesimen oppdatert med flere av disse komponentene
