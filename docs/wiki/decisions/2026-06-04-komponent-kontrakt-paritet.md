# Komponent-kontrakt-paritet på tvers av web og app

**Dato:** 2026-06-04
**Status:** Aktiv
**Forgjenger:** [2026-06-03 Web vs. App Token Separation](2026-06-03-web-vs-app-token-separation.md) — bygger på, reverserer ikke.

**Kontekst:**

`components-web.css` og `components-app.css` hadde drevet fra hverandre i hvilke *klasser* de tilbød. Web hadde 20+ klasser app manglet (`.accordion*`, `.search-bar`, `.section-divider*`, `.tag-input*`, `.btn-link`, `.animate-*`, `.spinner`, m.fl.), mens app hadde noen web manglet (`.form-group*`, `.pagination-item`, `.bounce-in`).

Dette var **utilsiktet divergens** — ingen tidligere beslutning vedtok at klassesettene skulle være ulike. Det oppstod organisk fordi komponenter ble bygget i den ene pakken først. Konsekvensen: en utvikler kunne ikke stole på at en byggestein fantes i begge pakker, og den unifiserte styleguiden kunne ikke demonstrere ett felles komponentsett.

Dette må ikke forveksles med beslutningen i forgjengeren (2026-06-03), som handler om at **token-verdier og fil-struktur** forblir separate (web = luftig/editorial, app = tett/SaaS). Den beslutningen står ved lag.

**Alternativer:**

- **A) Aksepter divergensen som intensjonell.** Dokumenter at web og app har ulike komponentsett fordi de er ulike designmål. Styleguiden viser web-spesifikke og app-spesifikke klasser hver for seg.
- **B) Full kontrakt-paritet.** Begge pakker tilbyr identiske klasse*navn* (kontrakter), men beholder pakke-spesifikke *verdier* (spacing, button-stil, animasjonstempo). Filene forblir separate per 2026-06-03.
- **C) Slå sammen til én delt komponentfil** med betinget logikk. (Allerede avvist i 2026-06-03 for tokens — samme negative ROI gjelder komponenter.)

**Valgt: B) Full kontrakt-paritet.**

Klassenavn er offentlige kontrakter (jf. CLAUDE.md: "Component classes are contracts"). At en kontrakt finnes skal være forutsigbart på tvers av pakker; *hvordan* den ser ut er der pakkene får skille seg. Dette gir én mental modell for utviklere ("alle byggesteiner finnes i begge pakker") uten å ofre den platform-tilpassede estetikken 2026-06-03 verner om.

Alternativ A ble forkastet fordi den utilsiktede divergensen ikke sporet tilbake til noen designintensjon — den var et artefakt av byggerekkefølge, ikke et valg. Alternativ C ble forkastet av samme grunn som for tokens: betinget logikk gir uleselig, skjør CSS med negativ ROI.

**Konsekvenser:**

- `components-app.css` fikk tillagt: `.accordion*`, `.search-bar`/`.search-result*`, `.section-divider*`, `.tag-input*`/`.tag-list`, `.btn-link`, `.date-picker-weekday`, `.file-item-size`, `.table-sort`/`.table-filter`, `.spinner`, `.animate-fade-in/-scale-in/-slide-up`. Verdiene er kalibrert til app-tetthet (kompakt padding, raskere tempo der relevant).
- `components-web.css` fikk tillagt: `.form-group`/`.form-group-item`, `.pagination-item`.
- **Tillatt gjenstående divergens:** rene utility-klasser som reflekterer token-defaults — web beholder generøse spacing/width-utilities (`.gap-5`, `.p-4/5`, `.mb-4/5`, `.mt-4/5`, `.max-w-2xl…6xl`), app beholder kompakte (`.p-1`, `.max-w-sm/-xl`) + `.bounce-in`. Dette er konsistent med 2026-06-03 (verdi-divergens er tillatt; kontrakt-divergens er ikke).
- **Ny vedlikeholdsregel (additiv til mirroring-regelen):** Når en ny komponentklasse legges til i én pakke, må samme klassenavn finnes i den andre i samme commit — med pakke-tilpassede verdier. Dette utvider den eksisterende mirroring-regelen fra "shared component structure" til "shared component contracts".
- Den unifiserte styleguiden kan nå demonstrere ett komponentsett for begge pakker; pakkebytteren swapper kun token-stilark.
- Endringen er **additiv og ikke-brytende** — ingen klasser fjernet eller omdøpt. Ingen nedstrøms-kontrakt brytes.

**Reverseringskostnad:** Lav. Tilleggene er additive; å reversere ville bety å fjerne klasser fra én pakke, men det ville gjeninnført den utilsiktede divergensen uten gevinst.

**Revurder hvis:**

- Native iOS/Android-plattform legges til (kan tvinge frem en annen kontrakt-strategi)
- En komponent viser seg meningsløs i én kontekst (f.eks. en ren editorial-byggestein uten app-bruk) — da dokumenteres unntaket eksplisitt her fremfor å la divergensen være implisitt
