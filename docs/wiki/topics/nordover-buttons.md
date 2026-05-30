# Buttons

Én Button-komponent med 4 visuelle variants × valgfri tone-akse, 3 størrelser, polymorphic `as`-prop. Bygger på `--color-accent*`, `--border-focus`, `--button-radius`, `--button-font-weight`.

Se [decision 2026-05-27 — buttons-arkitektur](../decisions/2026-05-27-buttons-arkitektur.md).

## API

```jsx
<Button
  variant="primary"          // "primary" | "secondary" | "ghost" | "link"
  tone="neutral"             // "neutral" | "danger" | "success"
  size="md"                  // "sm" | "md" | "lg"
  elevated                   // valgfri — tactile pattern (opt-in i web, default i app)
  leftIcon={<ArrowLeft />}   // valgfri
  rightIcon={<ArrowRight />} // valgfri
  iconOnly                   // valgfri — krever aria-label
  loading                    // valgfri — overlay-spinner, stabil bredde
  fullWidth                  // valgfri — width: 100%
  disabled                   // valgfri
  as="a"                     // polymorphic — default "button", auto "a" hvis href
  href="/foo"                // hvis satt uten as, rendrer som <a>
  onClick={...}
>
  Klikk meg
</Button>
```

**`elevated`-modifier:** Aktiverer Apple/Stripe-aktig tactile rendering (gradient + inner highlight + bottom edge + drop shadow). I `tokens-web` er dette **opt-in** for spesielle hero-CTAs. I `tokens-app` er det allerede default — `elevated`-prop er da redundant.

## Nye tokens (lagt til begge token-pakker)

```css
:root {
  --button-radius: var(--radius-md);    /* Brand kan overstyre til 0 (editorial flat) eller var(--radius-full) (pill) */
  --button-font-weight: 500;            /* Medium som default; brand kan justere */
}
```

## Variants × tone — interaksjons-modellen

**4 variants** styrer visuell hierarki (solid vs bordered vs transparent vs text-only).
**3 toner** styrer farge-betydning (neutral = accent, danger = error, success = success).

Tone implementeres ved å lokalt overstyre `--color-accent`-familien innenfor button-en:

```css
@utility btn-tone-danger {
  --color-accent: var(--color-error);
  --color-accent-fg: #FFFFFF;
  --color-accent-hover: color-mix(in oklch, var(--color-error) 85%, black);
  --color-accent-active: color-mix(in oklch, var(--color-error) 70%, black);
}

@utility btn-tone-success {
  --color-accent: var(--color-success);
  --color-accent-fg: #FFFFFF;
  --color-accent-hover: color-mix(in oklch, var(--color-success) 85%, black);
  --color-accent-active: color-mix(in oklch, var(--color-success) 70%, black);
}
```

Alle variants leser fra `--color-accent`-familien, så `<Button variant="ghost" tone="danger">Slett</Button>` automatisk får rødt ghost-hover.

## CSS — `@utility`-blokker

**Base:**
```css
@utility btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--gap-tight);
  font-family: var(--font-sans);
  font-weight: var(--button-font-weight);
  border-radius: var(--button-radius);
  border: none;
  cursor: pointer;
  text-decoration: none;
  white-space: nowrap;
  position: relative;
  user-select: none;
  transition: background-color var(--duration-fast) var(--ease-out),
              color var(--duration-fast) var(--ease-out),
              border-color var(--duration-fast) var(--ease-out);

  &:focus-visible {
    outline: var(--border-focus);
    outline-offset: var(--focus-ring-offset);
  }

  &:disabled,
  &[aria-disabled="true"] {
    opacity: 0.5;
    pointer-events: none;
    cursor: not-allowed;
  }
}
```

**Sizes (setter padding, font-size, icon-størrelse):**
```css
@utility btn-sm {
  padding-block: 0.375rem;
  padding-inline: 0.875rem;
  font-size: var(--text-sm);
  line-height: 1;
  --button-icon-size: 0.875rem;
}

@utility btn-md {
  padding-block: 0.625rem;
  padding-inline: 1.25rem;
  font-size: var(--text-base);
  line-height: 1;
  --button-icon-size: 1rem;
}

@utility btn-lg {
  padding-block: 0.875rem;
  padding-inline: 1.75rem;
  font-size: var(--text-lg);
  line-height: 1;
  --button-icon-size: 1.25rem;
}
```

**Variants:**

Primary-varianten leser fra `--button-surface-*`-tokens. Det betyr **samme CSS** rendrer flat i tokens-web (default) og tactile i tokens-app (default) — kun token-verdiene endrer seg. Se [decision om tactile-pattern](../decisions/2026-05-27-tokens-iter-2-moderne-farger-og-tactile.md).

```css
@utility btn-primary {
  background: var(--button-surface-bg-rest);
  color: var(--color-accent-fg);
  box-shadow: var(--button-surface-shadow-rest);

  &:hover:not(:disabled) {
    background: var(--button-surface-bg-hover);
  }
  &:active:not(:disabled) {
    background: var(--button-surface-bg-active);
    box-shadow: var(--button-surface-shadow-active);
  }
}

/* Opt-in tactile-variant for tokens-web — overstyrer surface-tokens lokalt */
@utility btn-elevated {
  --button-surface-bg-rest: linear-gradient(
    to bottom,
    color-mix(in oklch, var(--color-accent) 92%, white) 0%,
    var(--color-accent) 100%
  );
  --button-surface-bg-hover: linear-gradient(
    to bottom,
    color-mix(in oklch, var(--color-accent-hover) 92%, white) 0%,
    var(--color-accent-hover) 100%
  );
  --button-surface-bg-active: var(--color-accent-active);
  --button-surface-shadow-rest:
    inset 0 0.5px 0 0 rgb(255 255 255 / 0.18),
    0 1px 0 0 var(--color-accent-active),
    var(--shadow-sm);
  --button-surface-shadow-active:
    inset 0 1px 2px 0 rgb(0 0 0 / 0.18),
    var(--shadow-xs);

  /* Komposisjon: btn-elevated er en modifier, brukes med btn-primary */
  /* I tokens-app er dette redundant siden default allerede er tactile */
}

@utility btn-secondary {
  background: transparent;
  color: var(--color-fg);
  border: var(--border-card);

  &:hover:not(:disabled) {
    background: var(--color-subtle);
    border-color: var(--color-fg);
  }
  &:active:not(:disabled) {
    background: color-mix(in oklch, var(--color-subtle) 80%, var(--color-fg));
  }
}

@utility btn-ghost {
  background: transparent;
  color: var(--color-fg);

  &:hover:not(:disabled) { background: var(--color-subtle); }
  &:active:not(:disabled) {
    background: color-mix(in oklch, var(--color-subtle) 80%, var(--color-fg));
  }
}

@utility btn-link {
  background: transparent;
  color: var(--color-accent);
  padding-inline: 0;
  text-decoration: underline;
  text-underline-offset: 0.2em;
  text-decoration-thickness: 1px;
  border-radius: 0;

  &:hover:not(:disabled) {
    color: var(--color-accent-hover);
    text-decoration-thickness: 2px;
  }
  &:active:not(:disabled) { color: var(--color-accent-active); }
  &:focus-visible { outline-offset: 4px; }
}
```

**Modifiers:**
```css
@utility btn-full { width: 100%; }

@utility btn-icon-only {
  padding-inline: 0;
  aspect-ratio: 1;
}

@utility btn-loading {
  & > .btn-content { opacity: 0; }
  & > .btn-spinner {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}

.btn-icon svg {
  width: var(--button-icon-size);
  height: var(--button-icon-size);
  flex-shrink: 0;
}
```

## React-komponent

```jsx
import { forwardRef } from "react";

const Button = forwardRef(function Button({
  variant = "primary",
  tone = "neutral",
  size = "md",
  leftIcon,
  rightIcon,
  iconOnly = false,
  loading = false,
  fullWidth = false,
  disabled = false,
  href,
  as,
  className,
  children,
  ...rest
}, ref) {
  const Tag = as ?? (href ? "a" : "button");
  const isLink = Tag === "a" || typeof Tag !== "string";
  const isDisabled = disabled || loading;

  const classes = [
    "btn",
    `btn-${variant}`,
    `btn-${size}`,
    tone !== "neutral" && `btn-tone-${tone}`,
    iconOnly && "btn-icon-only",
    loading && "btn-loading",
    fullWidth && "btn-full",
    className,
  ].filter(Boolean).join(" ");

  // Link med disabled: fjern href, sett aria-disabled
  const linkProps = isLink && isDisabled
    ? { "aria-disabled": "true", tabIndex: -1 }
    : isLink
      ? { href }
      : {};

  const buttonProps = Tag === "button"
    ? { type: rest.type ?? "button", disabled: isDisabled }
    : {};

  return (
    <Tag ref={ref} className={classes} {...linkProps} {...buttonProps} {...rest}>
      <span className="btn-content">
        {leftIcon && <span className="btn-icon">{leftIcon}</span>}
        {children}
        {rightIcon && <span className="btn-icon">{rightIcon}</span>}
      </span>
      {loading && (
        <span className="btn-spinner" aria-hidden="true">
          <Spinner size={size} />
        </span>
      )}
    </Tag>
  );
});
```

## Bruksmønstre

**Standard CTA:**
```jsx
<Button>Kom i gang</Button>
<Button variant="secondary">Lær mer</Button>
```

**Med ikon:**
```jsx
<Button rightIcon={<ArrowRight />}>Les artikkelen</Button>
<Button variant="ghost" leftIcon={<ArrowLeft />}>Tilbake</Button>
```

**Icon-only:**
```jsx
<Button iconOnly variant="ghost" aria-label="Lukk meny">
  <X />
</Button>
```

**Tone-variasjon:**
```jsx
<Button tone="danger">Slett konto</Button>
<Button variant="ghost" tone="danger">Avbryt abonnement</Button>
<Button variant="secondary" tone="success">Bekreft</Button>
```

**Link (auto-detected fra href):**
```jsx
<Button href="/priser" variant="link">Se priser</Button>
<Button href="/priser" rightIcon={<ArrowRight />}>Se priser</Button>
```

**Next.js Link-integrasjon:**
```jsx
import Link from "next/link";
<Button as={Link} href="/dashboard">Til dashbord</Button>
```

**Loading-state:**
```jsx
<Button loading>Lagrer...</Button>
```
Tekst blir usynlig (`opacity: 0`), spinner sentreres over. Bredde er stabil.

**Full-width (vanlig i form-bunner):**
```jsx
<Button fullWidth size="lg">Logg inn</Button>
```

## A11y-noter

- `<button>` har default `type="button"` — forhindrer utilsiktet form-submit.
- `<a>`-buttons med `disabled` får `aria-disabled="true"` og mister `href` — link kan ikke "disables" på samme måte som button.
- `iconOnly` krever `aria-label` (TypeScript-types håndhever dette).
- `loading` skjuler tekst visuelt men holder den i DOM-en for skjermlesere. Spinner er `aria-hidden="true"`.
- Focus-ring er sterk (`--border-focus` + `--focus-ring-offset`) — Scandi-min skal ikke ha svak focus.
- `:focus-visible` (ikke `:focus`) — focus vises kun ved tastatur-navigasjon.

## Brand-overstyringer — eksempler

```css
/* Pill */
:root { --button-radius: var(--radius-full); }

/* Editorial flat */
:root { --button-radius: 0; }

/* Tyngre vekt */
:root { --button-font-weight: 600; }
```

Hvis padding-overstyring per brand blir vanlig, introdusér `--button-padding-*`-tokens.

## Hva utelater vi bevisst

- **`destructive` som eget variant** — `tone="danger"` dekker.
- **Elevated button med shadow** — gjør knapper for "appy". Brand kan legge på `box-shadow: var(--shadow-xs)` om ønsket.
- **Animated icon-transitions** — bygges på toppen, ikke i base.
- **Dropdown / split-button** — hører hjemme i en separat `<Menu>`-komponent.

## Implementeringsrekkefølge

1. Legg til `--button-radius` og `--button-font-weight` i `:root` i begge token-pakker.
2. Lag `buttons.css` med alle `@utility`-blokker.
3. Lag `Spinner`-komponent (gjenbrukbar — vil bli spec'et i forms-økten).
4. Lag `Button`-komponent i `@nordover/ui/buttons/Button.tsx` med polymorphic `as`-prop.
5. TypeScript: diskriminerende union for `iconOnly` (krever `aria-label`).
6. Import-rekkefølge per app: `tokens-*.css` → `base.css` → `typografi.css` → `layout.css` → `elevation.css` → `buttons.css` → `prose.css` → `clients/<slug>.css`.

## Se også

- [Nordover-arkitektur — tokens](nordover-arkitektur.md)
- [Nordover-elevation](nordover-elevation.md) — focus-ring, border-tokens
- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: buttons-arkitektur](../decisions/2026-05-27-buttons-arkitektur.md)
