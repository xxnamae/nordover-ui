# ADR: Nye komponenter, knappevarianter og web-flat-beslutning (2026-06-02)

**Status:** Vedtatt
**Signerare:** Design system owner
**Datering:** 2026-06-02
**Revidert:** —

---

## Kontekst

Komponent-auditen avdekket to ting:

1. **Spec↔leveranse-drift:** Wiki-en spesifiserte en verdensklasse komponentportefølje (Card-varianter, Tabs, Tooltip, Avatar, Menu/Dropdown, Toast, Kbd, Skeleton), men de **shippable** filene (`components-web.css` / `components-app.css`) inneholdt bare ~50 % av dem. Per CLAUDE.md sin egen regel gjelder dette begge veier: en komponent som finnes i spec men ikke i CSS, finnes ikke for brukere.

2. **Web↔app-divergens på interaktive komponenter:** App-laget var nær verdensklasse (taktile knapper, custom-stylede kontroller), mens web-laget brukte flate knapper og native browser-kontroller. Dette krevde en bevisst avklaring av hvor langt divergensen skal gå.

I tillegg manglet systemet en `destructive`-knapp (kritisk for SaaS/skjemaer: slett konto, slett rad) og en `tonal`-variant for hierarki mellom primary og secondary.

---

## Avgjørelse

### 1. Web forblir flat editorial — bevisst divergens

Web-laget skal **ikke** gjøres taktilt som app. Web-knapper forblir flate (skandinavisk editorial-estetikk), men:

- Web sine **skjemakontroller** (`.form-checkbox`, `.form-radio`, `.form-toggle`, `.form-switch`) custom-styles (ikke native), speilet fra app, for konsistent utseende på tvers av OS.
- Fokus-, hover- og disabled-tilstander fikses på begge plattformer.

Dette er en bevisst, dokumentert divergens — ikke en stille forskjell. App = taktil (gradient + inset-highlight + spring). Web = flat (rene flater, editorial luft). Begge deler samme arkitektur, tokens, a11y-garanti og komponentkontrakter.

### 2. Nye knappevarianter (kontraktsutvidelse)

| Variant | Web | App |
|---------|-----|-----|
| `.btn-destructive` | Flat, `--error`-bakgrunn | Taktil gradient med error-hue, `--error-strong` hover |
| `.btn-tonal` | `--accent-subtle` bakgrunn, `--on-accent-subtle` tekst | Samme (flat tinted) |

`.btn-destructive` dekker destruktive handlinger (Apple HIG «destructive» rolle, M3 error-knapp). `.btn-tonal` gir et hierarki-nivå mellom primary og secondary (M3 filled-tonal).

### 3. Nye komponenter (shippable CSS, speilet web↔app)

Bygget fra eksisterende wiki-spec inn i begge `components-*.css`:

- **Card-familie:** `.card` + `.card-bordered/-elevated/-subtle/-interactive` + `.card-header/-title/-meta/-footer`. Eksisterende `.feature-card`/`.card-featured` er urørt (egen kontekst).
- **Tabs:** `.tabs-list`, `.tabs-trigger` (støtter både `[aria-selected="true"]` og `.active`), `.tabs-content`.
- **Avatar:** `.avatar` + size-skala (`-xs/-sm/-lg/-xl`) + `.avatar-group` med overlapp.
- **Tooltip:** `.tooltip` + `.tooltip-content` (ren CSS, hover/focus-within).
- **Menu/Dropdown:** `.menu-content`, `.menu-item`, `.menu-separator`.
- **Toast:** `.toast-viewport`, `.toast` + semantiske varianter.
- **Kbd:** `.kbd`.
- **Skeleton:** `.skeleton`, `.skeleton-text`, `.skeleton-circle`.
- **Tag-varianter:** `.tag-solid`, `.tag-outline`, `.tag-success` (utvider eksisterende `.tag` uten rename).

### 4. Eksisterende komponenter løftet

- **Badges:** borderless tinted pills, speilet web↔app (var: web hadde tunge borders).
- **Tabeller:** sticky header, zebra (`.data-table-zebra`), tabulære tall (`.data-table-cell-numeric`), radvalg. Død duplikat-`.data-table` i web fjernet.
- **Modal:** backdrop-blur + scale-in (reduced-motion-beskyttet), `--surface-4` + `--shadow-modal`.
- **Dark elevation:** hevede komponenter bruker `--surface-2/3/4`.

---

## Konsekvenser

- **Kontraktsutvidelser:** nye klassenavn (`.btn-destructive`, `.btn-tonal`, `.card*`, `.tabs*`, `.avatar*`, `.tooltip*`, `.menu*`, `.toast*`, `.kbd`, `.skeleton*`) er nå offentlige kontrakter og immutable på vanlig vis.
- **Ingen renames** av eksisterende klasser; ingen breaking changes.
- **Styleguide-workflow:** alle nye komponenter dokumentert i `styleguide-web.html` og `styleguide-app.html` i samme leveranse (CLAUDE.md-krav).
- **Mirroring:** alt speilet web↔app; tiltenkt divergens (web flat / app taktil) er dokumentert her.
- **Versjon:** utløser minor-bump til v1.2.0 (nye, bakoverkompatible komponenter og varianter).

---

## Se også

- `docs/wiki/decisions/2026-06-02-verdensklasse-token-oppgradering.md`
- `docs/wiki/topics/nordover-buttons.md`
- `docs/wiki/topics/nordover-patterns-basis.md`
- `docs/wiki/topics/nordover-app-patterns.md`
