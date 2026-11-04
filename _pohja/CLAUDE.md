---
title: "{{PROJEKTI}} — tekoälyohje"
type: ai_instructions
owner: "{{OMISTAJA}}"
created: "{{PVM}}"
modified: "{{PVM}}"
---

# {{PROJEKTI}} — tekoälyohje

**Tarkoitus:** {{TARKOITUS}}

Juuren `CLAUDE.md` pätee. Tämä tiedosto kertoo vain, mikä on tässä projektissa toisin tai tarkemmin.

## Lue ensin

1. `TILANNE.md` — missä mennään.
2. `tehtavat.md` — mikä on auki.
3. `README.md` — mitä projekti on, keitä siinä on, missä aineisto on.

## Tämän projektin säännöt

- (lisätään, kun niitä syntyy; päivämäärä mukaan)

## Rakenne

```
{{PROJEKTI}}/
├── CLAUDE.md        ← tämä
├── README.md        ← mikä, miksi, ketkä, missä aineisto
├── TILANNE.md       ← elävä tilanne (päivitetään joka keskustelun lopussa)
├── paatokset.md     ← päätösloki
├── tehtavat.md      ← avoimet ja tehdyt tehtävät
├── muistiinpanot/   ← wiki-sivut aiheittain
└── RAW/             ← käsittelemätön materiaali; käsitelty siirretään RAW/_kasitelty/
```

Alikansiot (asiakas, teos, hanke) luodaan tarpeen mukaan tämän rinnalle, esim. `asiakkaat/<asiakas>/`.
