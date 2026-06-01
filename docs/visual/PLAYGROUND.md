# Component Playground

En interaktiv HTML/CSS editor for å eksperimentere med Nordover-komponenter i sanntid.

## Åpne Playground

- **Direkte**: Åpne [`playground.html`](./playground.html) i nettleseren
- **Fra styleguide**: Klikk på `→ [component-name]` linker i komponentseksjonene
- **Med deep-link**: `playground.html?component=btn-primary`

## Features

### 🎯 Component Picker
- **Søk**: Finn komponenter etter navn eller nøkkelord
- **Filtrer**: Gruppering efter kategori (Buttons, Forms, Status, Navigation, etc)
- **Metadata**: Se komponentsbelskrivelse og ARIA-egenskaper

### ✏️ Live Editor
- **HTML textarea**: Direkte HTML-redigering
- **Real-time preview**: Se endringer umiddelbar
- **Format HTML**: Automatisk formatering av kode
- **Class autocomplete**: Forslag på CSS-klasser mens du skriver
- **Clear**: Nullstill editor

### 👀 Live Preview
- **Responsive modes**: Desktop, Tablet, Mobile
- **Dark mode**: Toggle mellom lys/mørk tema
- **Real-time rendering**: Ser endringer med en gang

### ♿ Accessibility Panel
Automatisk validering av:
- ARIA-attributter (`aria-label`, `aria-expanded`, etc)
- Buttons uten labels
- Images uten alt-tekst
- Form inputs uten labels
- Heading-hierarki
- Tastatur-navigasjon

### 💾 Storage & Sharing
- **Local Storage**: Dine endringer lagres automatisk
- **Copy HTML**: Kopier koden til utklippstavle
- **Export**: Last ned komplett HTML-fil med Nordover CSS
- **Share**: Del deep-links med andre (`?component=button-name`)

### 🌙 Dark Mode
Toggle mørk modus ved siden av andre kontroller. Endringer lagres.

## Komponentliste

**40+ komponenter** inkludert:

#### Buttons (8)
- `btn-primary` - Primary action button
- `btn-secondary` - Secondary action button
- `btn-ghost` - Minimal ghost button
- `btn-link` - Link-styled button
- `btn-sm` - Small/compact button
- `btn-lg` - Large CTA button
- `btn-touch` - Touch-friendly button
- `btn-elevated` - Button with elevation

#### Forms (7)
- `input-text` - Text input
- `input-email` - Email input
- `input-password` - Password field
- `input-checkbox` - Checkbox
- `input-radio` - Radio button
- `input-select` - Select dropdown
- `input-textarea` - Multi-line input

#### Status & Badges (5)
- `badge-primary` - Default badge
- `badge-success` - Success badge
- `badge-error` - Error badge
- `badge-warning` - Warning badge
- `badge-info` - Info badge

#### Feedback & Alerts (4)
- `alert-success` - Success message
- `alert-error` - Error message
- `alert-warning` - Warning message
- `alert-info` - Info message

#### Navigation (2)
- `breadcrumbs` - Breadcrumb navigation
- `pagination` - Page pagination

#### Data (1)
- `data-table` - Data table with rows/cols

#### Modals (1)
- `modal-basic` - Dialog/modal box

#### Complex Components (3)
- `accordion` - Collapsible accordion
- `chip` - Single chip/tag
- `chips` - Chip group

## Bruk

### Velge en komponent
1. Søk eller filtrer i venste panel
2. Klikk på komponenten for å laste standardeksempel

### Redigere HTML
1. Endre koden i HTML-editoren
2. Se preview oppdateres i sanntid
3. Sjekk accessibility-panelet for problemer

### Teste responsivt
1. Klikk på Device-modus (Desktop/Tablet/Mobile)
2. Se hvordan komponenten reagerer

### Kopiere kode
1. Klikk **Copy** for å kopiere HTML
2. Eller klikk **Export** for komplett HTML-fil

### Deep-linking
Del URL med komponenten: `playground.html?component=btn-primary`

## Keyboard Shortcuts

- **Ctrl/Cmd + A**: Select all in editor
- **Ctrl/Cmd + X**: Cut
- **Ctrl/Cmd + C**: Copy
- **Ctrl/Cmd + V**: Paste
- **Tab**: Insert indent

## Tips & Tricks

- Bruk **Format HTML** knappen for å rydde opp i koden
- Slå på **Dark mode** for å teste kontrast
- Prøv alle **accessibility warnings** for å skrive bedre kode
- Test på **mobile view** for small screens
- Lagre ofte — data lagres lokalt

## Integrasjon i styleguides

Styleguides har automatiske linker til playground:

```html
<!-- I styleguide-web.html -->
<script src="./playground-injection.js"></script>
```

Dette legger til "Open in Playground" linker for hver komponentsektion.

## Lagring & Cookies

- Editor-innhold lagres i **localStorage**
- Ingen data sendes til server
- Data fjernes hvis du sletter browser-cache
- Hver komponent har sitt eget state

## Accessibility

Playground selv er fullt accessible:
- Keyboard navigation
- Screen reader friendly
- High contrast mode support
- ARIA labels på alle interaktive elementer

## For udvikler

### Legge til ny komponent

I `playground.html`, oppdater `COMPONENTS`:

```javascript
const COMPONENTS = {
  'my-component': {
    name: 'My Component',
    category: 'buttons',
    description: 'Description here',
    html: '<button class="my-component">Click</button>',
    ariaAttributes: ['aria-label'],
    keywords: ['my', 'component']
  }
};
```

Legg også til kategori i `playground-injection.js`:

```javascript
const COMPONENT_PLAYGROUND_COMPONENTS = {
  'my-section': {
    label: 'My Section',
    examples: ['my-component']
  }
};
```

### Styling

Playground bruker Nordover token-variabler:
- `--color-bg` - Background
- `--color-surface` - Surface
- `--color-accent` - Accent color
- `--color-border` - Border
- `--color-fg` - Foreground

## Lisensiering

MIT License — Som resten av Nordover.
