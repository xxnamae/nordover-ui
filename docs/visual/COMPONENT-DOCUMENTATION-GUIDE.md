# Komponentdokumentasjonsmal — Nordover

**Målgruppe:** Designere, utviklere som implementerer komponenter i Nordover  
**Språk:** Norsk bokmål gjennomgående  
**Format:** Markdown i styleguide-HTML eller separate .md-filer

## Struktur per komponent

Hver komponent skal dokumenteres med disse delene:

### 1. Hva er det? (Formål + bruksscenario)

En setning som forklarer hva komponenten gjør og når man bruker den. Skriv som skulle du forklare en designer som ikke kjenner designsystemet.

**Mal:**
> `<komponent>` er brukt til [formål]. Velg denne når [spesifikt scenario]. Ikke bruk for [vanlig misforståing].

**Eksempel (Button):**
> Knappen er brukt til primære handlinger på siden. Velg denne når brukeren skal iverksette noe med øyeblikk-effekt (lagre skjema, slette element). Ikke bruk for navigasjon — bruk lenke i stedet.

### 2. Varianter (Typer + når)

Tabellformat: variant-navn, formål, bruksscenario.

| Variant | Formål | Når bruke |
|---------|--------|----------|
| `.btn-primary` | Primær handling | Main call-to-action på siden |
| `.btn-ghost` | Sekundær handling | Alternative handlinger, flere steg |
| `.btn-error` | Destruktiv handling | Sletting, uomgjørlig endring |

### 3. Do ✅ / Don't ❌

Minst 3 do, minst 3 don't. Skriv som instruksjoner til designere/utviklere.

**Do:**
- ✅ Bruk kortfattet, handlingsorientert tekst på knappen (f.eks. "Lagre" ikke "Lagre endringer du har gjort")
- ✅ Plasser primær knapp til venstre, sekundær til høyre (LTR-konvensjon)
- ✅ Gi skjemaknapper god avstand (minst 8px) slik at de ikke blir klikket ved uhell

**Don't:**
- ❌ Ikke bruk alle knappevariantene i samme handlingssekv — maksimalt 2-3 typer
- ❌ Ikke lag en knapp mindre enn 32px høyde (målbar overflate)
- ❌ Ikke bruk knapper for navigering — bruk `.nav-item` eller lenke

### 4. Tilgjengelighet (a11y-tabell)

Tabell med disse kolonnene:

| Aspekt | Krav | Implementering |
|--------|------|----------------|
| **ARIA-rolle** | Spesifiser rolle | `role="button"` på `<button>`, implisitt på `<button>`-element |
| **Fokus** | Tastaturbar | `Tab` når `focusable`, `:focus-visible` styling |
| **Aktivering** | Tastatur | `Enter` eller `Space` må fungere (native `<button>` gjør det) |
| **Navn (a11y-navn)** | Skjermleser kan lese | Synlig tekst eller `aria-label="Lagre"` om bare ikon |
| **State/aria-pressed** | Aktiv/inaktiv markering | `disabled="disabled"` gjør knappen uinteraktiv + visuelt deaktivert |
| **Kontrast** | WCAG AA | Tekst/farge minst 4.5:1 (sjekket per variant: primary, ghost, error) |

### 5. Kodetips (Implementering)

Kort JavaScript/CSS-tips hvis kompleks oppførsel.

```html
<!-- ✅ Rett: semantisk button + handling -->
<button class="btn btn-primary" onclick="saveForm()">Lagre</button>

<!-- ❌ Feil: div som knapp, krever ARIA + JS -->
<div class="btn" onclick="saveForm()">Lagre</div>
```

### 6. Relaterte komponenter

Lenker til beslektede komponenter (f.eks. Button → Textarea, Form, Modal).

---

## Tone-of-voice (norsk)

### Prinsippet

Skriv som en kollega som forklarer designsystemet. Direkte, faglig, men ikke stivt.

### Regler

| Regel | Eksempel ✅ | Unngå ❌ |
|-------|-----------|---------|
| **Aktivt språk, imperativ** | "Bruk kortfattet tekst" | "Kortfattet tekst bør brukes" |
| **Konkrete, målbare eksempler** | "Minst 32px høyde" | "passelig stor" |
| **Norsk fagbegrep** | "Tilgjengelighet", "fokus", "skjermleser" | "accessibility", "A11y", "screen reader" |
| **Unngå jargong uten kontekst** | "Knappen må være fokusbar (Tab)" | "implementer fokus-styling" |
| **Gendering: du/din når praksis** | "Du kan velge fra disse variantene" | "En utvikler kan velge..." |
| **Norsk interpunksjon** | «Anførselstegn», "Rett", … (ikke …) | "English style", '' '' |

### Eksempler

**God tone (praksis-nær):**
> Knappen er brukt til primære handlinger. Gi den kortfattet, handlingsorientert tekst — f.eks. "Lagre" ikke "Lagre endringer". Velg en av tre varianter: primær (blå), sekundær (grå), eller destruktiv (rød) for handlinger som sletting eller reset.

**Dårlig tone (abstrakt):**
> Knappen representerer en brukerinteraksjon. Teksten bør være optimert for lesbarhet og informativ verdi. Varianter er tilgjengelige avhengig av kontekst.

---

## Eksempel: Komplett komponentdokumentasjon

Se nedenfor for eksempel på `.button` dokumentert etter denne malen.

### Button (`<button>`)

**Hva?**  
Knappen er brukt til primære og sekundære handlinger. Bruk når brukeren skal iverksette noe med øyeblikk-effekt (lagre, sende, slette). For navigering mellom sider, bruk lenke.

**Varianter**

| Variant | Formål | Når |
|---------|--------|-----|
| `.btn` + `.btn-primary` | Primær handling | Main call-to-action |
| `.btn` + `.btn-ghost` | Sekundær handling | Avbryt, tilbake, alternativ |
| `.btn` + `.btn-error` | Destruktiv | Sletting, reset, uomgjørlig endring |
| `.btn-lg` / `.btn-sm` | Størrelse | Minimal `.btn-sm` for tett UI, `.btn-lg` for hero |

**Do ✅**
- ✅ Bruk kortfattet, handlingsorientert tekst: "Lagre", "Slett", "Åpne" — ikke "Lagre endringer du nettopp har gjort"
- ✅ Gi primær knapp god visuell vekt (høy kontrast)
- ✅ Plasser primær knapp først (venstre), sekundær andre eller høyre
- ✅ Minst 32px høyde for berørt overflate (touchable target)

**Don't ❌**
- ❌ Ikke bruk for navigering — bruk `.nav-item` eller `<a>` i stedet
- ❌ Ikke ha flere enn 2-3 knappevarianter i samme flow (overwhleming)
- ❌ Ikke bruk lang tekst (mer enn 3 ord) — omprioritert eller lag modal
- ❌ Ikke settklikkbare `<div>` med `.btn`-klasse — bruk semantisk `<button>`

**Tilgjengelighet**

| Aspekt | Krav | Implementering |
|--------|------|----------------|
| **ARIA-rolle** | `button` | Implisitt på `<button>`-element |
| **Fokus** | `Tab` navigering | Native `<button>` er fokusbar |
| **Tastatur-aktivering** | `Enter`, `Space` | Native `<button>` støtter begge |
| **Navn** | Skjermleser leser | Synlig tekst eller `aria-label` |
| **Deaktivert state** | `disabled`-attributt | Render `.is-disabled` visuelt |
| **Kontrast** | WCAG AA (4.5:1) | Primær 5.2:1 ✓, Ghost 4.5:1 ✓, Error 5.1:1 ✓ |

**Kodetips**

```html
<!-- ✅ Rett: semantisk button, enkel tekst -->
<button class="btn btn-primary">Lagre</button>

<!-- ✅ Rett: med aria-label for ikon -->
<button class="btn btn-ghost" aria-label="Åpne meny">
  <svg class="icon">...</svg>
</button>

<!-- ❌ Feil: div som knapp, mangler ARIA -->
<div class="btn btn-primary" onclick="save()">Lagre</div>

<!-- ❌ Feil: lang tekst, dårlig UX -->
<button class="btn btn-primary">Lagre alle dine endringer som du nettopp gjorde i skjemaet</button>
```

**Relatert**
- Form, Modal, Popover (bruker knapper internt)
- Lenke (for navigering, ikke handling)
- Tag, Badge (visuelle statuser, ikke interaktiv)

---

## Publisering

Hver komponentes dokumentasjon legges i:
1. **Styleguide HTML** (`docs/visual/styleguide.html`) som `.doc-section`
2. Eller som lenket `.md`-fil i `docs/components/`
3. Eller som kommentar i komponenten selv (`.css`-filen)

Vedlikehald: Oppdater dokumentasjonen når komponenten endrer API eller variant.
