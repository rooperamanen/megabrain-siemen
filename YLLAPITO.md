---
title: "Ylläpito"
modified: "{{PVM}}"
---

# Ylläpito

## Joka keskustelun lopussa (tekoäly tekee, omistaja ei)

- Projektin `TILANNE.md` ajan tasalle: tehty, kesken, seuraavaksi.
- Päätökset `paatokset.md`:hen, avoimet tehtävät `tehtavat.md`:hen, omistajan omat tehtävät erikseen.
- Opitut faktat (hinnat, mitat, yhteystiedot, polut, "missä X on") projektin tiedostoihin.
- Taidon tarve arvioitu (`CLAUDE.md` kohta 6).
- Commit, jos git on käytössä.

## Uusi aihe, uusi keskustelu

Kun aihe vaihtuu kokonaan tai keskustelu on venynyt pitkäksi, tekoäly ehdottaa uutta keskustelua. Tilanne on
tiedostoissa, joten uusi keskustelu jatkaa siitä, mihin jäätiin, ilman vanhan keskustelun painolastia.

## Viikoittain (omistaja pyytää: "viikkokatsaus")

- Käy `PROJEKTIT.md` läpi: mikä on aktiivinen, mikä voi mennä tauolle.
- Kaikkien aktiivisten projektien `tehtavat.md`: mitä erääntyy, mitä on jäänyt.
- Kooste juuren `TEHTAVAT.md`:n taulukkoon; erääntyneet ja omistajaa odottavat esiin.
- `_inbox/` tyhjäksi.
- Jos kalenteriliitin on käytössä: tuleva viikko vs. tehtävät.

## Kuukausittain

- `TYOKALUT.md`: toimivatko liittimet yhä, vaihtuiko työkalu.
- `TAIDOT.md`: `python3 _tyokalut/paivita_taidot.py`; vanhentuneet taidot päivitetään tai poistetaan.
- Varmuuskopio toimii (`SAILYTYS.md`): viimeisin commit tai synkkaus on tuore, Time Machine ajossa.
- `PROFIILI.md`: pitävätkö työtavat paikkansa.
- Valmiit projektit → status `arkistoitu`; kansio voi jäädä paikalleen.

## Kun otat toisen koneen tai toisen tekoälyn käyttöön

- Kansio mukaan (git clone, pilvikansio, kopio). Tekoälyn oma muisti ei kulje mukana: kaikki pysyvä on tiedostoissa.
- Ensimmäinen viesti uudessa ympäristössä: "Lue CLAUDE.md (tai AGENTS.md) ja PROFIILI.md, sitten jatketaan projektista X."
- Jos uusi tekoäly ei lue `CLAUDE.md`:tä automaattisesti, pidä `AGENTS.md` samana ja sano sen nimi ensimmäisessä viestissä.
