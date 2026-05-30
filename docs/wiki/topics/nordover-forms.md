# Forms

Skjema-primitiver: Input, Textarea, Select, Checkbox, Radio, Switch + komposisjons-wrappers Field og Form. Pluggbar validering (ingen intern logikk), top-labels med "(valgfritt)"-marking, native input + custom visuelt lag for checkbox/radio, custom Switch.

Se [decision 2026-05-27 — forms-arkitektur](../decisions/2026-05-27-forms-arkitektur.md).

## Komponentsett

| Komponent | Underliggende | Notater |
|---|---|---|
| `Input` | `<input>` | text, email, password, number, tel, url, search |
| `Textarea` | `<textarea>` | resize: vertical, min-height |
| `Select` | `<select>` | native, custom chevron via background-image |
| `Checkbox` | `<input type="checkbox">` + visuelt lag | `appearance: none` på native, custom checkmark |
| `Radio` | `<input type="radio">` + visuelt lag | samme mønster som checkbox |
| `Switch` | Custom (checkbox semantisk) | `role="switch"`, ingen native ekvivalent |
| `Field` | div-wrapper med slots | komposisjons-API for label/help/error |
| `Form` | `<form>`-wrapper | `noValidate`, optional density-prop |

**Bevisst utenfor:** Datepicker, Combobox, MultiSelect, FileUpload, Slider, RichTextEditor. Disse bygges på primitivene som **patterns** senere, eventuelt via Radix UI når behov dukker opp.

## Nye tokens (lagt til begge token-pakker)

```css
:root {
  --input-radius: var(--radius-md);
  --input-border-color: var(--color-border);
  --input-border-color-focus: var(--color-focus);
  --input-border-color-error: var(--color-error);
  --input-bg: var(--color-bg);
  --input-bg-disabled: var(--color-subtle);
}
```

## Field — composer-API

**Primær API (props-basert):**
```jsx
<Field label="E-post" help="Vi sender aldri spam" error={errors.email?.message}>
  <Input name="email" type="email" />
</Field>
```

Field genererer:
- `id` for input (eller bruker `id`-prop).
- `htmlFor` på label.
- `aria-describedby` knytter input til help + error.
- `aria-invalid="true"` på input når error er satt.
- "(valgfritt)"-suffiks på label hvis ikke `required`.
- `aria-required="true"` på input hvis `required`.

**Render-prop (spesialtilfeller):**
```jsx
<Field label="Telefon">
  {({ id, describedBy }) => (
    <Cluster gap="tight">
      <Input placeholder="+47" className="w-16" />
      <Input id={id} aria-describedby={describedBy} className="flex-1" />
    </Cluster>
  )}
</Field>
```

**Implementasjon via React-context:**
```jsx
import { createContext, useContext, useId } from "react";

const FieldContext = createContext(null);

function Field({
  label,
  help,
  error,
  success,
  required = false,
  optional = true,
  children,
  id: providedId,
  className,
  ...rest
}) {
  const generatedId = useId();
  const id = providedId ?? generatedId;
  const helpId = help ? `${id}-help` : undefined;
  const errorId = error ? `${id}-error` : undefined;
  const describedBy = [helpId, errorId].filter(Boolean).join(" ") || undefined;
  const invalid = Boolean(error);

  const optionalLabel = !required && optional
    ? <span className="field-label-optional"> (valgfritt)</span>
    : null;

  const renderedChild = typeof children === "function"
    ? children({ id, describedBy, invalid })
    : children;

  return (
    <FieldContext.Provider value={{ id, describedBy, invalid, required }}>
      <div className={`field ${className ?? ""}`.trim()} {...rest}>
        <label htmlFor={id} className="field-label">
          {label}{optionalLabel}
        </label>
        {renderedChild}
        {help && <p id={helpId} className="field-help">{help}</p>}
        {error && <p id={errorId} className="field-error" role="alert">{error}</p>}
      </div>
    </FieldContext.Provider>
  );
}

function useField() {
  return useContext(FieldContext) ?? {};
}
```

Input/Textarea/Select leser fra `useField()` for å automatisk få `id`, `aria-describedby`, `aria-invalid`, `aria-required`.

## Validation — pluggbar

Field har **ingen intern valideringslogikk**. Den viser `error` som blir gitt til den. Integrasjon med form-libraries:

**react-hook-form:**
```jsx
const { register, formState: { errors } } = useForm();

<Field label="E-post" error={errors.email?.message}>
  <Input {...register("email", { required: "Påkrevd" })} />
</Field>
```

**Conform / native FormData:**
```jsx
<Form action={action}>
  <Field label="E-post" error={state.errors?.email}>
    <Input name="email" type="email" />
  </Field>
</Form>
```

**Egen state:**
```jsx
const [email, setEmail] = useState("");
const error = email && !isValidEmail(email) ? "Ugyldig adresse" : undefined;

<Field label="E-post" error={error}>
  <Input value={email} onChange={(e) => setEmail(e.target.value)} />
</Field>
```

## Sizing — sm/md/lg + Form-density

Default `md`. Form-wrapper kan sette `density` som internt setter alle nested inputs til `sm`:

```jsx
<Form density="compact">
  {/* Alle Field/Input/Select arver size="sm" via context */}
  <Field label="Navn"><Input /></Field>
  <Field label="E-post"><Input type="email" /></Field>
</Form>
```

Padding-skala:

| Size | Padding-block | Padding-inline | Type |
|---|---|---|---|
| sm | 0.375rem | 0.625rem | --text-sm |
| md | 0.625rem | 0.875rem | --text-base |
| lg | 0.875rem | 1.125rem | --text-lg |

## CSS — `@utility`-blokker

**Field-wrapper:**
```css
@utility field {
  display: flex;
  flex-direction: column;
  gap: var(--gap-tight);
}

@utility field-label {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);
  color: var(--color-fg);
}

@utility field-label-optional {
  color: var(--color-muted);
  font-weight: var(--font-weight-normal);
}

@utility field-help {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);   /* 500 — UI-hjelpetekst leser bedre i medium */
  color: var(--color-muted);
}

@utility field-error {
  font-size: var(--text-sm);
  font-weight: var(--font-weight-medium);   /* 500 */
  color: var(--color-error);
}
```

**Input (delte stiler for Input, Textarea, Select):**
```css
@utility form-input {
  width: 100%;
  font-family: var(--font-sans);
  font-size: var(--text-base);
  line-height: 1.5;
  color: var(--color-fg);
  background: var(--input-bg);
  border: var(--border-width-thin) solid var(--input-border-color);
  border-radius: var(--input-radius);
  padding-block: 0.625rem;
  padding-inline: 0.875rem;
  transition: border-color var(--duration-fast) var(--ease-out),
              background var(--duration-fast) var(--ease-out);

  &::placeholder { color: var(--color-muted); }

  &:hover:not(:disabled):not([aria-invalid="true"]) {
    border-color: var(--color-fg);
  }

  &:focus-visible {
    outline: var(--border-focus);
    outline-offset: 1px;
    border-color: var(--input-border-color-focus);
  }

  &[aria-invalid="true"] {
    border-color: var(--input-border-color-error);
  }

  &:disabled {
    background: var(--input-bg-disabled);
    color: var(--color-muted);
    cursor: not-allowed;
  }

  &:read-only:not(:disabled) {
    background: var(--color-subtle);
  }
}

@utility form-input-sm {
  font-size: var(--text-sm);
  padding-block: 0.375rem;
  padding-inline: 0.625rem;
}

@utility form-input-lg {
  font-size: var(--text-lg);
  padding-block: 0.875rem;
  padding-inline: 1.125rem;
}
```

**Textarea (legger til på form-input):**
```css
@utility form-textarea {
  resize: vertical;
  min-height: 6rem;
  line-height: 1.6;
}
```

**Select (legger til på form-input):**
```css
@utility form-select {
  appearance: none;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'><path d='M2 4l4 4 4-4' stroke='currentColor' stroke-width='1.5' fill='none' stroke-linecap='round' stroke-linejoin='round'/></svg>");
  background-repeat: no-repeat;
  background-position: right 0.875rem center;
  background-size: 0.75rem;
  padding-inline-end: 2.5rem;
}
```

**Checkbox + Radio (native + visuelt lag):**
```css
@utility form-checkbox {
  appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  border: var(--border-width-thin) solid var(--input-border-color);
  border-radius: var(--radius-sm);
  background: var(--input-bg);
  cursor: pointer;
  display: inline-grid;
  place-content: center;
  flex-shrink: 0;
  transition: background var(--duration-fast) var(--ease-out),
              border-color var(--duration-fast) var(--ease-out);

  &::before {
    content: "";
    width: 0.75rem;
    height: 0.75rem;
    background: var(--color-accent-fg);
    clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
    transform: scale(0);
    transition: transform var(--duration-fast) var(--ease-out);
  }

  &:checked {
    background: var(--color-accent);
    border-color: var(--color-accent);
  }

  &:checked::before { transform: scale(1); }

  &:focus-visible {
    outline: var(--border-focus);
    outline-offset: 2px;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}

@utility form-radio {
  appearance: none;
  width: 1.25rem;
  height: 1.25rem;
  border: var(--border-width-thin) solid var(--input-border-color);
  border-radius: var(--radius-full);
  background: var(--input-bg);
  cursor: pointer;
  display: inline-grid;
  place-content: center;
  flex-shrink: 0;
  transition: border-color var(--duration-fast) var(--ease-out);

  &::before {
    content: "";
    width: 0.625rem;
    height: 0.625rem;
    background: var(--color-accent);
    border-radius: var(--radius-full);
    transform: scale(0);
    transition: transform var(--duration-fast) var(--ease-out);
  }

  &:checked {
    border-color: var(--color-accent);
  }

  &:checked::before { transform: scale(1); }

  &:focus-visible {
    outline: var(--border-focus);
    outline-offset: 2px;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}
```

**Switch:**
```css
@utility form-switch {
  appearance: none;
  width: 2.5rem;
  height: 1.5rem;
  background: var(--color-muted);
  border-radius: var(--radius-full);
  cursor: pointer;
  position: relative;
  flex-shrink: 0;
  transition: background var(--duration-fast) var(--ease-out);

  &::before {
    content: "";
    position: absolute;
    top: 2px;
    inset-inline-start: 2px;
    width: calc(1.5rem - 4px);
    height: calc(1.5rem - 4px);
    background: #FFFFFF;
    border-radius: var(--radius-full);
    transition: transform var(--duration-fast) var(--ease-out);
  }

  &:checked { background: var(--color-accent); }
  &:checked::before { transform: translateX(1rem); }

  &:focus-visible {
    outline: var(--border-focus);
    outline-offset: 2px;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}
```

## React-komponenter (stubs)

**Input/Textarea/Select** leser context fra Field:

```jsx
function Input({ size, className, ...rest }) {
  const { id, describedBy, invalid, required } = useField();
  const formCtx = useFormContext();
  const effectiveSize = size ?? formCtx?.density === "compact" ? "sm" : "md";
  const sizeClass = effectiveSize !== "md" ? `form-input-${effectiveSize}` : "";

  return (
    <input
      id={id}
      aria-describedby={describedBy}
      aria-invalid={invalid || undefined}
      aria-required={required || undefined}
      className={`form-input ${sizeClass} ${className ?? ""}`.trim()}
      {...rest}
    />
  );
}

function Textarea({ size, className, rows = 4, ...rest }) {
  // Same pattern as Input, adds form-textarea class
}

function Select({ size, className, children, ...rest }) {
  // Same pattern, adds form-select class
}
```

**Checkbox/Radio/Switch** brukes ofte uten Field-wrapper (siden de har label til høyre, ikke over):

```jsx
function Checkbox({ label, help, error, className, id: providedId, ...rest }) {
  const generatedId = useId();
  const id = providedId ?? generatedId;
  const helpId = help ? `${id}-help` : undefined;
  const errorId = error ? `${id}-error` : undefined;

  return (
    <div className={`field-toggle ${className ?? ""}`.trim()}>
      <Cluster gap="tight" align="start">
        <input
          id={id}
          type="checkbox"
          className="form-checkbox"
          aria-describedby={[helpId, errorId].filter(Boolean).join(" ") || undefined}
          aria-invalid={Boolean(error) || undefined}
          {...rest}
        />
        <label htmlFor={id} className="field-toggle-label">
          {label}
          {help && <span id={helpId} className="field-help">{help}</span>}
        </label>
      </Cluster>
      {error && <p id={errorId} className="field-error" role="alert">{error}</p>}
    </div>
  );
}

// Radio og Switch følger samme pattern, bare med .form-radio og .form-switch
// Switch får role="switch" på input
```

**Form:**
```jsx
const FormContext = createContext({});

function Form({
  density = "default",          // "default" | "compact"
  requiredMarking = "optional", // "optional" | "asterisk"
  className,
  children,
  ...rest
}) {
  return (
    <FormContext.Provider value={{ density, requiredMarking }}>
      <form noValidate className={`form ${className ?? ""}`.trim()} {...rest}>
        {children}
      </form>
    </FormContext.Provider>
  );
}

function useFormContext() {
  return useContext(FormContext);
}
```

## Bruksmønstre

**Standard kontakt-skjema:**
```jsx
<Form action={submitContact}>
  <Stack gap="component">
    <Field label="Navn" required>
      <Input name="name" />
    </Field>
    <Field label="E-post" required help="Vi sender bekreftelse hit">
      <Input name="email" type="email" />
    </Field>
    <Field label="Melding" required>
      <Textarea name="message" rows={6} />
    </Field>
    <Cluster justify="end">
      <Button type="submit">Send</Button>
    </Cluster>
  </Stack>
</Form>
```

**SaaS-skjema med density="compact" + validation:**
```jsx
<Form density="compact" onSubmit={handleSubmit}>
  <Stack gap="component">
    <Field label="Borettslag" required error={errors.org?.message}>
      <Select {...register("org")}>
        <option value="">Velg...</option>
        {orgs.map(o => <option key={o.id} value={o.id}>{o.name}</option>)}
      </Select>
    </Field>
    <Field label="Adresse">
      <Input {...register("address")} />
    </Field>
    <Checkbox label="Send rapport på e-post" {...register("emailReport")} />
    <Switch label="Aktiver påminnelser" {...register("reminders")} />
    <Cluster justify="end">
      <Button variant="ghost" type="button">Avbryt</Button>
      <Button type="submit" loading={isSubmitting}>Lagre</Button>
    </Cluster>
  </Stack>
</Form>
```

**Radio-gruppe:**
```jsx
<Fieldset legend="Frekvens">
  <Stack gap="tight">
    <Radio name="freq" value="daily" label="Daglig" />
    <Radio name="freq" value="weekly" label="Ukentlig" defaultChecked />
    <Radio name="freq" value="monthly" label="Månedlig" />
  </Stack>
</Fieldset>
```

(`<Fieldset>` er en tynn wrapper rundt native `<fieldset>` + `<legend>` for semantisk gruppering.)

## A11y-noter

- **Labels alltid synlige.** Floating labels skip pga lavere skannbarhet og a11y-issues.
- **`htmlFor` + `id`** auto-koblet av Field/Checkbox/Radio.
- **`aria-describedby`** kobler help og error til input.
- **`aria-invalid`** settes på input når error er satt.
- **`aria-required`** settes når `required={true}`.
- **`role="alert"`** på error-meldinger — skjermlesere annonserer feil umiddelbart.
- **`noValidate` på `<form>`** — vi bruker custom error-rendering. Browser-default-meldinger er stygge og engelske.
- **Native `<select>` med custom chevron** — full a11y bevart inklusive tastatur-navigasjon og IME.
- **Native checkbox/radio** med `appearance: none` — visuelt custom, men keyboard, screen reader, og form-submission fungerer som native.
- **Switch får `role="switch"`** — kommuniserer toggle-natur til skjermlesere.

## Required vs optional

Default-pattern: alt er required med mindre annet er sagt. Optional-felt får "(valgfritt)"-suffiks i label.

```jsx
<Field label="E-post" required>      {/* ingen suffiks, required */}
<Field label="Telefon">              {/* "(valgfritt)" suffiks */}
```

For complianse-kontekster (juridiske skjemaer der "required" er kontraktsbegrep) kan utvikleren bytte til asterisk-marking:
```jsx
<Form requiredMarking="asterisk">
  <Field label="E-post" required>     {/* viser "E-post *" */}
</Form>
```

## Brand-overstyringer — eksempler

```css
/* Sharp editorial inputs */
:root { --input-radius: 0; }

/* Subtilere borders (hairline) */
:root { --input-border-color: color-mix(in oklch, var(--color-border) 50%, transparent); }

/* Fylte inputs i stedet for bordered */
:root {
  --input-bg: var(--color-subtle);
  --input-border-color: transparent;
}
```

## Hva utelater vi bevisst

- **Datepicker** — native `input[type="date"]` for enkle cases; Radix UI for komplekse. Egen pattern senere.
- **Combobox / Autocomplete** — Radix Combobox eller egen pattern. Krever egen drodling.
- **MultiSelect** — komplekst. Egen pattern.
- **FileUpload** — krever drag/drop, progress, preview. Egen pattern.
- **Slider / Range** — Radix Slider eller native. Sjelden i Nordover-prosjekter.
- **RichTextEditor** — Payload sin egen, eller TipTap.

## Implementeringsrekkefølge

1. Legg til `--input-*`-tokens i `:root` i begge token-pakker.
2. Lag `forms.css` med alle `@utility`-blokker.
3. Lag `FieldContext` + `FormContext` i `@nordover/ui/forms/contexts.ts`.
4. Lag komponentene i denne rekkefølgen: `Form` → `Field` → `Input`/`Textarea`/`Select` → `Checkbox`/`Radio`/`Switch` → `Fieldset`.
5. TypeScript: diskriminerende unions for `iconOnly`-lignende constraints (eks. `Checkbox` krever enten `label` eller `aria-label`).
6. Import-rekkefølge per app: `tokens-*.css` → `base.css` → `typografi.css` → `layout.css` → `elevation.css` → `buttons.css` → `forms.css` → `prose.css` → `clients/<slug>.css`.

## Se også

- [Nordover-arkitektur — tokens](nordover-arkitektur.md)
- [Nordover-buttons](nordover-buttons.md) — variants, tone, sizes
- [Nordover-elevation](nordover-elevation.md) — focus-ring
- [Nordover-rammeverk — index](nordover-rammeverk.md)
- [Decision: forms-arkitektur](../decisions/2026-05-27-forms-arkitektur.md)
