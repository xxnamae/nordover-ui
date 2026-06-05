# Motion System — Nordover

**Status:** Complete  
**Package:** `components-web.css` and `components-app.css`

## Overview

Nordover's motion system provides consistent animations and transitions. All motion respects `prefers-reduced-motion: reduce` for accessibility.

---

## Motion Tokens

### Duration

Web og app divergerer bevisst: app-pakken er raskere (SaaS-tetthet, mindre bevegelse), web er litt roligere (editorial). Begge har syv durations, men med ulike verdier.

**tokens-web:**
```css
--duration-instant: 50ms;     /* Imperceptible state flip */
--duration-fast: 150ms;       /* Quick feedback (button hover, focus) */
--duration-moderate: 200ms;   /* Small UI transitions */
--duration-base: 250ms;       /* Standard animations (fade, scale) */
--duration-slow-base: 700ms;  /* Modal/popover open */
--duration-slow: 800ms;       /* Editorial entrance (slide, reveal) */
--duration-slower: 1000ms;    /* Large drawer/sheet motion */
```

**tokens-app (raskere defaults — SaaS-tempo):**
```css
--duration-instant: 50ms;
--duration-fast: 100ms;       /* App: 100ms, ikke 150ms */
--duration-base: 150ms;       /* App: 150ms, ikke 250ms */
--duration-moderate: 200ms;
--duration-slow: 400ms;       /* App: 400ms entrance */
--duration-slow-base: 600ms;
--duration-slower: 800ms;
```

> Merk: `--duration-base` betyr 250ms i web, men 150ms i app. Bruk alltid token-navnet, ikke en antatt ms-verdi.

### Easing

Identisk i begge pakker, med ett tillegg i app:

```css
--ease-out: cubic-bezier(0.2, 0, 0, 1);        /* Deceleration (most common) */
--ease-spring: cubic-bezier(0.2, 0.8, 0.2, 1); /* Strong ease-out (NO overshoot) */
--ease-emphasized: cubic-bezier(0.3, 0, 0, 1); /* Material-style emphasized accel/decel */
```

App-pakken har i tillegg de klassiske inn/ut-kurvene:
```css
/* tokens-app only */
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
```

For ekte fjær-fysikk med faktisk overshoot (signatur-interaksjoner) finnes en `linear()`-easing i begge pakker:
```css
--ease-spring-physics: linear(0, 0.006, 0.025 2.8%, 0.101 6.1%, 0.539 18.9%, 0.721, 0.849, 0.937, 0.991, 1.02, 1.03, 1.017, 1.003, 0.998, 1);
```

**When to use:**
- `--ease-out`: state changes (button, focus, hover) — standardvalget
- `--ease-spring`: en **sterk ease-out** for entrance/scale. Den har IKKE overshoot — kontrollpunktene holder seg innenfor [0,1], så den «studser» ikke. Bruk den når du vil ha en tydelig, energisk decelerasjon, ikke en bounce.
- `--ease-emphasized`: fremhevede transisjoner som skal trekke blikket (Material 3-mønster)
- `--ease-spring-physics`: den ENESTE kurven med faktisk overshoot. Reservér for signatur-momenter der en liten studs er ønsket.

---

## Transition System

### Button State Changes

```css
.btn {
  transition: 
    background var(--duration-fast) var(--ease-out),
    color var(--duration-fast) var(--ease-out);
}

.btn-primary:hover {
  background: var(--color-accent-hover);  /* Smooth 150ms transition */
}
```

### Form Focus

```css
.form-input {
  transition: 
    border-color var(--duration-fast) var(--ease-out),
    box-shadow var(--duration-fast) var(--ease-out);
}

.form-input:focus-visible {
  border-color: var(--color-focus);
  box-shadow: 0 0 0 3px color-mix(in oklch, var(--color-focus) 15%, transparent);
}
```

### Card Hover

```css
.feature-card {
  transition: 
    border-color var(--duration-fast) var(--ease-out),
    background var(--duration-fast) var(--ease-out);
}

.feature-card:hover {
  border-color: var(--color-fg);
  background: var(--color-subtle);
}
```

**Pattern:** All state-based transitions use `--duration-fast` (web 150ms / app 100ms).

---

## Animation System

### Spin (Loading)

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.icon-spin {
  animation: spin var(--duration-base) linear infinite;
  /* One rotation per --duration-base (web 250ms / app 150ms), continuous */
}
```

**Use case:** Loading spinners, processing indicators

```html
<svg class="icon icon-spin" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2" />
</svg>
```

### Pulse (Attention)

```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.icon-pulse {
  animation: pulse var(--duration-slow) cubic-bezier(0.4, 0, 0.6, 1) infinite;
  /* Fade cycle over --duration-slow (web 800ms / app 400ms) */
}
```

**Use case:** Unread badges, live indicators, subtle attention

```html
<span class="badge icon-pulse">New</span>
```

### Bounce (Celebration)

```css
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

.icon-bounce {
  animation: bounce var(--duration-slow) ease-in-out infinite;
  /* Up-down cycle over --duration-slow (web 800ms / app 400ms) */
}
```

**Use case:** CTAs, promotional icons, celebratory moments

---

## Entrance Animations

### Fade In

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in {
  animation: fadeIn var(--duration-base) var(--ease-out) forwards;
  /* 300ms fade from invisible to visible */
}
```

**Use case:** Page load, modal open, content reveal

### Slide In (Directional)

```css
@keyframes slideInUp {
  from { transform: translateY(1rem); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes slideInDown {
  from { transform: translateY(-1rem); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes slideInLeft {
  from { transform: translateX(-1rem); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

@keyframes slideInRight {
  from { transform: translateX(1rem); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.slide-in-up {
  animation: slideInUp var(--duration-slow) var(--ease-out) forwards;
}
```

**Use case:** Modal open, drawer slide, list item appearance

### Scale In

```css
@keyframes scaleIn {
  from { transform: scale(0.95); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

.scale-in {
  animation: scaleIn var(--duration-base) var(--ease-spring) forwards;
  /* Grow from small → normal over --duration-base (web 250ms / app 150ms).
     --ease-spring is a strong ease-out — NO overshoot/bounce. */
}
```

**Use case:** Tooltip open, menu expansion, feature reveal

### Bounce In

```css
@keyframes bounceIn {
  0% { transform: scale(0.3); opacity: 0; }
  50% { opacity: 1; }
  70% { transform: scale(1.05); }
  100% { transform: scale(1); }
}

.bounce-in {
  animation: bounceIn var(--duration-base) var(--ease-spring) forwards;
  /* Entrance over --duration-base (web 250ms / app 150ms). The overshoot
     comes from the keyframes (scale 1.05), not from --ease-spring. */
}
```

**Use case:** Alert appear, success message, celebratory reveal

---

## Exit Animations

### Fade Out

```css
@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}

.fade-out {
  animation: fadeOut var(--duration-fast) var(--ease-out) forwards;
  /* 150ms quick disappear */
}
```

### Scale Out

```css
@keyframes scaleOut {
  from { transform: scale(1); opacity: 1; }
  to { transform: scale(0.95); opacity: 0; }
}

.scale-out {
  animation: scaleOut var(--duration-fast) var(--ease-out) forwards;
  /* 150ms shrink away */
}
```

---

## Complex Animations

### Modal Fade + Backdrop

```html
<dialog class="modal modal-fade-in" open>
  <div class="modal-backdrop modal-fade-in"></div>
  <div class="modal-content modal-scale-in"></div>
</dialog>
```

```css
.modal-fade-in {
  animation: fadeIn var(--duration-base) var(--ease-out) forwards;
}

.modal-content {
  animation: scaleIn var(--duration-base) var(--ease-spring) forwards;
  /* Parallel animations: backdrop fades, content scales */
}
```

**Result:** Backdrop fades while content grows over `--duration-base` (web 250ms / app 150ms).

### Drawer Slide + Backdrop

```html
<div class="drawer-backdrop drawer-fade-in"></div>
<nav class="drawer drawer-slide-in-left"></nav>
```

```css
.drawer-fade-in {
  animation: fadeIn var(--duration-slow) var(--ease-out) forwards;
  /* Backdrop fade over --duration-slow (web 800ms / app 400ms) */
}

.drawer {
  animation: slideInLeft var(--duration-slow) var(--ease-out) forwards;
  /* Drawer slide from left over --duration-slow (web 800ms / app 400ms) */
}
```

### List Item Stagger

```html
<ul class="list">
  <li class="list-item" style="animation-delay: 0ms;">Item 1</li>
  <li class="list-item" style="animation-delay: 100ms;">Item 2</li>
  <li class="list-item" style="animation-delay: 200ms;">Item 3</li>
</ul>
```

```css
.list-item {
  animation: slideInUp var(--duration-base) var(--ease-out) forwards;
  /* Each item slides up with 100ms delay */
}
```

**Result:** Items appear one after another (wave effect).

---

## Accessibility: Motion Respects Preferences

**All animations must respect `prefers-reduced-motion`:**

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-delay: -1ms !important;
    animation-duration: 1ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0s !important;
  }
}
```

**Result:** Users with vestibular disorders, epilepsy, or motion sensitivity get instant state changes (no animations).

### Testing Reduced Motion

1. **macOS:** System Preferences → Accessibility → Display → Reduce motion
2. **Windows:** Settings → Ease of Access → Display → Show animations
3. **DevTools:** Toggle in Chrome DevTools → Rendering → Emulate CSS media feature `prefers-reduced-motion`

---

## Performance Best Practices

### Transform-Based Animations Only

**Good (GPU-accelerated):**
```css
.slide {
  animation: slideIn var(--duration-base) var(--ease-out);
}

@keyframes slideIn {
  from { transform: translateX(-1rem); }
  to { transform: translateX(0); }
}
```

**Bad (causes reflow):**
```css
.slide {
  animation: slideIn var(--duration-base) var(--ease-out);
}

@keyframes slideIn {
  from { left: -1rem; }  /* Changes layout, slow */
  to { left: 0; }
}
```

### Opacity + Transform Only

Animatable properties without layout cost:
- `transform`: translate, rotate, scale
- `opacity`: transparency
- `color`: text color changes

### Avoid These

- `width`, `height` (causes reflow)
- `padding`, `margin` (causes reflow)
- `box-shadow` (can be expensive)
- `filter` (expensive, use sparingly)

---

## Motion Tokens in Components

### Button Hover (--duration-fast)

```css
.btn {
  transition: background var(--duration-fast) var(--ease-out);
}
```

### Modal Open (--duration-base)

```css
.modal-content {
  animation: scaleIn var(--duration-base) var(--ease-spring) forwards;
}
```

### Loading Spinner (infinite)

```css
.icon-spin {
  animation: spin var(--duration-base) linear infinite;
}
```

### Drawer Open (--duration-slow)

```css
.drawer {
  animation: slideInLeft var(--duration-slow) var(--ease-out) forwards;
}
```

---

## Real-World Examples

### Alert Toast

```html
<div class="alert alert-success animate-slide-in-up">
  ✓ Changes saved
</div>

<style>
  .animate-slide-in-up {
    animation: slideInUp var(--duration-base) var(--ease-out) forwards;
  }
  
  .animate-fade-out {
    animation: fadeOut var(--duration-fast) var(--ease-out) forwards;
  }
</style>

<script>
  const toast = document.querySelector('.alert');
  setTimeout(() => {
    toast.classList.remove('animate-slide-in-up');
    toast.classList.add('animate-fade-out');
    setTimeout(() => toast.remove(), 150);
  }, 3000); // Show for 3s, fade out in 150ms
</script>
```

### Loading State

```html
<button class="btn" id="submit">Submit</button>

<script>
  const btn = document.getElementById('submit');
  
  btn.addEventListener('click', async () => {
    btn.disabled = true;
    btn.innerHTML = '<svg class="icon icon-spin"></svg> Processing...';
    
    await fetch('/api/submit');
    
    btn.disabled = false;
    btn.innerHTML = '✓ Submitted';
    btn.classList.add('btn-success');
    
    setTimeout(() => {
      btn.classList.remove('btn-success');
      btn.innerHTML = 'Submit';
    }, 2000);
  });
</script>
```

### Modal Dialog

```html
<button class="btn" data-modal="confirm">Delete</button>

<dialog id="confirm" class="modal">
  <div class="modal-backdrop"></div>
  <div class="modal-content">
    <h2>Confirm Delete?</h2>
    <p>This action cannot be undone.</p>
    <div class="modal-footer">
      <button class="btn btn-ghost" onclick="this.closest('dialog').close()">Cancel</button>
      <button class="btn btn-error">Delete</button>
    </div>
  </div>
</dialog>

<style>
  .modal {
    animation: none;
  }
  
  .modal[open] {
    animation: fadeIn var(--duration-base) var(--ease-out) forwards;
  }
  
  .modal-content {
    animation: scaleIn var(--duration-base) var(--ease-spring) forwards;
  }
</style>

<script>
  document.querySelector('[data-modal="confirm"]').addEventListener('click', (e) => {
    document.getElementById('confirm').showModal();
  });
</script>
```

---

## Animation Checklist

- [ ] Motion uses `--duration-*` tokens
- [ ] Motion uses `--ease-*` easing
- [ ] All animations respect `prefers-reduced-motion`
- [ ] Transform-based (no layout cost)
- [ ] Duration ≤ 500ms (faster = better)
- [ ] No jank (60fps, GPU-accelerated)
- [ ] Focus/keyboard navigation unaffected
- [ ] Tested on real devices (not DevTools only)

---

## References

- `components-web.css` line 450+: animation keyframes
- `components-app.css` line 400+: app-optimized motion
- `tokens-web.css` line 274+: motion variables (durations + easings)
- `tokens-app.css` line 275+: app motion variables (faster defaults)
- [MDN: CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations)
- [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
- [High Performance Animations](https://www.html5rocks.com/en/tutorials/speed/high-performance-animations/)
