/*!
 * Nordover behaviours — optional, dependency-free progressive enhancement.
 * ---------------------------------------------------------------------------
 * The framework ships as pure CSS; this file is opt-in. It wires the few
 * building blocks that genuinely need scripting (tabs panel-switching, modal,
 * dropdown menu, drawer) using the SAME class + ARIA contracts the CSS already
 * defines. Accordion (<details>) and tooltip are pure-CSS and need nothing here.
 *
 * Usage:  <script src="…/behaviors/nordover.js" defer></script>
 * Markup is driven by data-attributes + ARIA — see docs/handoff/BEHAVIORS-JS.md.
 * No globals are leaked; safe to load more than once (idempotent init guard).
 */
(function () {
  'use strict';
  var doc = document;
  if (doc.documentElement.hasAttribute('data-nordover-js')) return; // idempotent
  doc.documentElement.setAttribute('data-nordover-js', '');

  function qsa(sel, root) {
    return Array.prototype.slice.call((root || doc).querySelectorAll(sel));
  }
  function focusables(el) {
    return qsa(
      'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])',
      el
    ).filter(function (n) { return n.offsetParent !== null || n === doc.activeElement; });
  }

  /* ============================ TABS ============================
   * <div role="tablist"> with [role="tab"][aria-controls="panelId"]; each
   * panel is [role="tabpanel"][id]. Click + arrow/Home/End keys move selection
   * and toggle [hidden] on the panels. Roving tabindex for a11y. */
  function initTabs(list) {
    var tabs = qsa('[role="tab"]', list);
    if (!tabs.length) return;
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        var id = t.getAttribute('aria-controls');
        var panel = id && doc.getElementById(id);
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }
    list.addEventListener('click', function (e) {
      var t = e.target.closest('[role="tab"]');
      if (t) { e.preventDefault(); select(t); }
    });
    list.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(doc.activeElement);
      if (i < 0) return;
      var n = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = (i + 1) % tabs.length;
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === 'Home') n = 0;
      else if (e.key === 'End') n = tabs.length - 1;
      else return;
      e.preventDefault();
      select(tabs[n], true);
    });
    var initial = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0];
    select(initial);
  }

  /* ============================ MODAL ===========================
   * Trigger: [data-modal-open="id"]. Root: .modal#id (CSS toggles via .is-open).
   * Close: [data-modal-close], backdrop click, or Esc. Focus is trapped while
   * open and restored to the trigger on close. */
  var modalReturnFocus = null;
  function openModal(modal, trigger) {
    modalReturnFocus = trigger || doc.activeElement;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    var first = focusables(modal.querySelector('.modal-dialog') || modal)[0];
    (first || modal).focus();
    doc.addEventListener('keydown', modalKeydown, true);
  }
  function closeModal(modal) {
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    doc.removeEventListener('keydown', modalKeydown, true);
    if (modalReturnFocus && typeof modalReturnFocus.focus === 'function') modalReturnFocus.focus();
    modalReturnFocus = null;
  }
  function modalKeydown(e) {
    var modal = doc.querySelector('.modal.is-open');
    if (!modal) return;
    if (e.key === 'Escape') { e.preventDefault(); closeModal(modal); return; }
    if (e.key === 'Tab') {
      var f = focusables(modal);
      if (!f.length) { e.preventDefault(); return; }
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  }

  /* ============================ DRAWER ==========================
   * Trigger: [data-drawer-open="id"]. Panel: .mobile-nav#id (CSS .is-open).
   * Optional backdrop: [data-drawer-backdrop="id"]. Close: [data-drawer-close]
   * (closest panel), backdrop click, Esc. */
  function setDrawer(panel, open) {
    if (!panel) return;
    panel.classList.toggle('is-open', open);
    panel.setAttribute('aria-hidden', open ? 'false' : 'true');
    var bd = doc.querySelector('[data-drawer-backdrop="' + panel.id + '"]') ||
             doc.querySelector('.mobile-backdrop');
    if (bd) bd.classList.toggle('is-open', open);
  }
  function drawerKeydown(e) {
    if (e.key !== 'Escape') return;
    var open = doc.querySelector('.mobile-nav.is-open');
    if (open) setDrawer(open, false);
  }

  /* ============================ MENU ============================
   * Trigger: [data-menu-open="id"] (gets aria-expanded). Surface: .menu-content#id
   * (hidden via [hidden] until opened). Outside-click + Esc close; arrow keys
   * roam [role="menuitem"]. */
  function openMenu(trigger, menu) {
    closeMenus();
    menu.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    var items = qsa('[role="menuitem"]', menu);
    if (items[0]) items[0].focus();
  }
  function closeMenus() {
    qsa('[data-menu-open][aria-expanded="true"]').forEach(function (t) {
      t.setAttribute('aria-expanded', 'false');
      var m = doc.getElementById(t.getAttribute('data-menu-open'));
      if (m) m.hidden = true;
    });
  }
  function menuKeydown(e) {
    var menu = e.target.closest('.menu-content');
    if (!menu) return;
    var items = qsa('[role="menuitem"]', menu);
    var i = items.indexOf(doc.activeElement);
    if (e.key === 'ArrowDown') { e.preventDefault(); (items[(i + 1) % items.length] || items[0]).focus(); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); (items[(i - 1 + items.length) % items.length] || items[0]).focus(); }
    else if (e.key === 'Escape') {
      e.preventDefault();
      var trigger = doc.querySelector('[data-menu-open="' + menu.id + '"]');
      closeMenus();
      if (trigger) trigger.focus();
    }
  }

  /* ===================== ACCORDION (single-open) =================
   * Native <details> already works. Opt into exclusive mode with
   * <div class="accordion" data-accordion="single">: opening one closes peers. */
  function initAccordionSingle(acc) {
    var items = qsa('details.accordion-item', acc);
    items.forEach(function (d) {
      d.addEventListener('toggle', function () {
        if (!d.open) return;
        items.forEach(function (o) { if (o !== d) o.open = false; });
      });
    });
  }

  /* ===================== Global delegated clicks ================ */
  doc.addEventListener('click', function (e) {
    var t;
    if ((t = e.target.closest('[data-modal-open]'))) {
      var m = doc.getElementById(t.getAttribute('data-modal-open'));
      if (m) { e.preventDefault(); openModal(m, t); return; }
    }
    if ((t = e.target.closest('[data-modal-close]'))) {
      var mc = t.closest('.modal'); if (mc) { e.preventDefault(); closeModal(mc); return; }
    }
    if (e.target.classList && e.target.classList.contains('modal') && e.target.classList.contains('is-open')) {
      closeModal(e.target); return; // backdrop
    }
    if ((t = e.target.closest('[data-drawer-open]'))) {
      e.preventDefault(); setDrawer(doc.getElementById(t.getAttribute('data-drawer-open')), true); return;
    }
    if ((t = e.target.closest('[data-drawer-close]'))) {
      e.preventDefault(); setDrawer(t.closest('.mobile-nav'), false); return;
    }
    if ((t = e.target.closest('[data-drawer-backdrop]'))) {
      setDrawer(doc.getElementById(t.getAttribute('data-drawer-backdrop')), false); return;
    }
    if ((t = e.target.closest('[data-menu-open]'))) {
      e.preventDefault();
      var menu = doc.getElementById(t.getAttribute('data-menu-open'));
      if (!menu) return;
      if (t.getAttribute('aria-expanded') === 'true') closeMenus(); else openMenu(t, menu);
      return;
    }
    if (!e.target.closest('.menu-content')) closeMenus(); // outside click
  });

  doc.addEventListener('keydown', function (e) {
    drawerKeydown(e);
    menuKeydown(e);
  });

  /* ============================ INIT ============================ */
  function init() {
    qsa('[role="tablist"]').forEach(initTabs);
    qsa('.accordion[data-accordion="single"]').forEach(initAccordionSingle);
    qsa('[data-menu-open]').forEach(function (t) {
      t.setAttribute('aria-haspopup', 'menu');
      t.setAttribute('aria-expanded', 'false');
      var m = doc.getElementById(t.getAttribute('data-menu-open'));
      if (m) m.hidden = true;
    });
  }
  if (doc.readyState !== 'loading') init();
  else doc.addEventListener('DOMContentLoaded', init);
})();
