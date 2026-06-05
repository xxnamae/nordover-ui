# Nordover behaviours — the optional JS layer

Nordover ships as **pure CSS**. Most building blocks need no JavaScript
(accordion is native `<details>`, tooltip is `:hover`/`:focus`, theme/sidebar
state is CSS). For the few that genuinely need scripting — **tabs, modal, menu,
drawer** — load the optional, dependency-free behaviour layer.

```html
<script src="node_modules/@xxnamae/nordover-ui/docs/visual/behaviors/nordover.js" defer></script>
<!-- or via the export map -->
<!-- import "@xxnamae/nordover-ui/behaviors"; -->
```

It is **progressive enhancement**: without it the markup still renders; with it
the components become interactive. The script leaks no globals, adds no
dependencies, and is safe to load twice. It drives everything from
**data-attributes + ARIA** and reuses the CSS contracts (`.is-open`, `[hidden]`).

---

## Tabs

`role="tablist"` with `role="tab"` buttons; each tab points at its panel via
`aria-controls`. Panels are `role="tabpanel"` with matching `id`; hide the
inactive ones with `hidden`.

```html
<div class="tabs-list" role="tablist" aria-label="Account">
  <button class="tabs-trigger" role="tab" id="t1" aria-controls="p1" aria-selected="true">Overview</button>
  <button class="tabs-trigger" role="tab" id="t2" aria-controls="p2" aria-selected="false">Activity</button>
</div>
<div class="tabs-content" role="tabpanel" id="p1" aria-labelledby="t1">…</div>
<div class="tabs-content" role="tabpanel" id="p2" aria-labelledby="t2" hidden>…</div>
```

Click selects; **←/→/↑/↓, Home, End** move with roving `tabindex`.

---

## Modal

Trigger with `data-modal-open="ID"`; the overlay is `.modal#ID` (CSS shows it
via `.is-open`). Close with any `data-modal-close`, a backdrop click, or **Esc**.
Focus is trapped while open and returns to the trigger on close.

```html
<button class="btn btn-primary" data-modal-open="confirm">Delete…</button>

<div class="modal" id="confirm" role="dialog" aria-modal="true"
     aria-labelledby="confirm-title" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-header"><h2 id="confirm-title">Confirm action</h2>
      <button class="btn btn-ghost btn-sm" data-modal-close aria-label="Close">✕</button>
    </div>
    <div class="modal-body">This cannot be undone.</div>
    <div class="modal-footer">
      <button class="btn btn-ghost" data-modal-close>Cancel</button>
      <button class="btn btn-error" data-modal-close>Delete</button>
    </div>
  </div>
</div>
```

---

## Menu / dropdown

Trigger with `data-menu-open="ID"` (the script adds `aria-haspopup="menu"` and
manages `aria-expanded`). The surface is `.menu-content#ID` with
`role="menu"` and `role="menuitem"` children; it starts hidden. Opens on click,
closes on outside-click or **Esc**; **↑/↓** roam the items.

```html
<button class="btn btn-secondary" data-menu-open="actions">Actions ▾</button>
<div class="menu-content" id="actions" role="menu">
  <button class="menu-item" role="menuitem">Edit</button>
  <button class="menu-item" role="menuitem">Duplicate</button>
  <div class="menu-separator" role="separator"></div>
  <button class="menu-item" role="menuitem">Delete</button>
</div>
```

---

## Drawer (mobile nav)

Trigger with `data-drawer-open="ID"`; the panel is `.mobile-nav#ID` (CSS slides
it in via `.is-open`). Close with `data-drawer-close`, the backdrop, or **Esc**.
A `.mobile-backdrop` (or `[data-drawer-backdrop="ID"]`) is toggled in sync.

```html
<button class="mobile-nav-trigger" data-drawer-open="nav">☰</button>
<div class="mobile-backdrop" data-drawer-backdrop="nav"></div>
<nav class="mobile-nav" id="nav" aria-hidden="true">
  <div class="mobile-nav-header">Menu
    <button class="mobile-nav-close" data-drawer-close aria-label="Close">✕</button>
  </div>
  <ul class="mobile-nav-list">…</ul>
</nav>
```

---

## Accordion — no JS needed

`.accordion` is built on native `<details>/<summary>` and works without this
script. To make a group **exclusive** (opening one closes the others), add
`data-accordion="single"` to the `.accordion` wrapper — that is the only
accordion behaviour the layer touches.

---

## Contract stability

The data-attributes and ARIA patterns above are **public contracts** (like token
and class names). Changing them is a breaking change and requires a new ADR. See
`docs/wiki/decisions/2026-06-05-valgfritt-js-atferdslag.md`.
