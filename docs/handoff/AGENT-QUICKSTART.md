# Nordover — Agent Quickstart

> **For Claude-agenter:** Dette er en kort, handlingsrettet oppskrift for å koble et nytt prosjekt på Nordover designsystem. Følg stegene som passer prosjekttypen. Hele guiden er public — hent den med `WebFetch` mot `https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/handoff/AGENT-QUICKSTART.md`.

---

## TL;DR

```bash
npm install @xxnamae/nordover-ui
```

Deretter importer riktig pakke i prosjektets CSS-entry:

- **App** (dashboard, SaaS, verktøy): `tokens-app` + `components-app`
- **Nettside** (marketing, editorial): `tokens-web` + `components-web`

---

## Steg 1 — Installer

I prosjektets rotmappe:

```bash
npm install @xxnamae/nordover-ui
```

Dette legger til `"@xxnamae/nordover-ui": "^1.2.0"` i `package.json`.

---

## Steg 2 — Importer CSS

Velg **én** av variantene basert på prosjekttype. Importer i prosjektets CSS-entry (f.eks. `src/styles.css` eller `src/main.css`).

### App-prosjekt (14px base, mørk default, kompakt)

```css
@import '@xxnamae/nordover-ui/tokens-app';
@import '@xxnamae/nordover-ui/components-app';
```

### Nettside-prosjekt (16px base, lys default, romslig)

```css
@import '@xxnamae/nordover-ui/tokens-web';
@import '@xxnamae/nordover-ui/components-web';
```

Hvis prosjektet ikke har en bundler (ren HTML), lenk i stedet via `<link>` i `<head>`:

```html
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/tokens/tokens-app.css">
<link rel="stylesheet" href="node_modules/@xxnamae/nordover-ui/docs/visual/components/components-app.css">
```

---

## Steg 3 — Brand-tilpasning (kun farger/logo/font)

ALT av struktur, komponenter, tilgjengelighet og responsivitet kommer fra Nordover. Per prosjekt endrer du **kun brand** i et `@layer brand`-blokk:

```css
@layer brand {
  :root {
    --color-accent: oklch(0.55 0.18 200);     /* prosjektets primærfarge */
    --color-accent-fg: oklch(0.99 0 0);        /* tekst på accent */
    --font-sans: 'Prosjekt Font', system-ui, sans-serif;
  }

  /* Valgfritt: overstyr mørk modus */
  :root:has(#dark:checked) {
    --color-accent: oklch(0.65 0.18 200);
  }
}
```

`@layer brand` har høyest prioritet, så dette overstyrer trygt uten å røre kjernen.

---

## Steg 4 — Bruk komponentene

Bruk klassenavnene direkte i markup. De er offentlige kontrakter:

```html
<button class="btn btn-primary">Lagre</button>

<div class="field">
  <label class="field-label" for="navn">Navn</label>
  <input id="navn" class="form-input" type="text">
</div>

<div class="card">
  <h3>Tittel</h3>
  <p>Innhold</p>
</div>
```

Full komponentliste: `docs/COMPONENT-INVENTORY.md`. Live examples: `docs/visual/styleguide.html` (unified).

---

## Regler (viktig)

1. **Skriv ALDRI egne komponent-CSS.** Bruk Nordovers klasser (`.btn`, `.card`, `.form-input`, `.alert`, `.badge`, `.stack`, `.cluster`, `.grid-auto` osv.).
2. **Kun brand lokalt.** Farger, logo, font i `@layer brand`. Aldri overstyr spacing-, radius- eller komponent-struktur.
3. **Token-navn er kontrakter.** `--color-accent`, `--space-4` osv. skal brukes, ikke erstattes med hardkodede verdier.
4. **Mørk modus er innebygd.** Bruk `:root:has(#dark:checked)`-mønsteret — ikke bygg eget tema-system.
5. **Oppgrader trygt:** `npm update @xxnamae/nordover-ui` henter nye minor/patch-versjoner.

---

## Oppgradering

```bash
npm update @xxnamae/nordover-ui      # minor/patch (bakoverkompatibelt)
npm install @xxnamae/nordover-ui@latest   # tving siste versjon
```

Sjekk `CHANGELOG.md` i nordover-ui for hva som endret seg mellom versjoner. Major-versjoner (f.eks. 2.0.0) kan ha breaking changes — les changelog før oppgradering.

---

## Velg riktig variant — beslutningstabell

| Prosjekt | Variant | Hvorfor |
|----------|---------|---------|
| SaaS-dashboard, internt verktøy, app | `*-app` | Kompakt, 14px base, mørk default, tett informasjon |
| Marketing, landingsside, blogg, editorial | `*-web` | Romslig, 16px base, lys default, fluid typografi |

Når du er i tvil: er det noe brukeren *jobber i* over tid → **app**. Er det noe brukeren *besøker* → **web**.

---

## CLAUDE.md-blokk til prosjektet

Lim dette inn i prosjektets `CLAUDE.md` så agenten husker reglene:

```markdown
## Designsystem (Nordover)

Dette prosjektet bruker `@xxnamae/nordover-ui` for all styling.
Oppsett-guide: https://raw.githubusercontent.com/xxnamae/nordover-ui/main/docs/handoff/AGENT-QUICKSTART.md

- App-prosjekt → importer `/tokens-app` + `/components-app`
- Nettside → importer `/tokens-web` + `/components-web`
- ALDRI skriv egne komponent-CSS — bruk nordover-ui sine klasser
- KUN brand-tilpasning (farger/logo/font) i `@layer brand`
- Oppgrader med `npm update @xxnamae/nordover-ui`
```
