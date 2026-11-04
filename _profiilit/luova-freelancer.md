# Profiili: luova freelancer (brändi- ja graafinen suunnittelu + oma taide)

Sopii, kun omistaja tekee asiakastöitä suunnittelijana (brändit, graafinen suunnittelu, kuvitus)
ja lisäksi omaa taidetta (maalaukset, näyttelyt, teosmyynti), ja hoitaa itse myynnin, markkinoinnin
ja laskutuksen. Tekoäly ehdottaa näitä projekteja ja kysyy, mitä muutetaan.

## Ehdotetut projektit

| Projekti | Tyyppi | Mitä kuuluu |
|---|---|---|
| `ASIAKASTYOT` | työ | Asiakkaiden suunnittelutyöt liidistä laskuun. Alikansio per asiakas `asiakkaat/<asiakas>/`. |
| `TAIDE` | työ/oma | Omat teokset, näyttelyt, galleriat, teosmyynti, apurahat. |
| `MARKKINOINTI` | työ | Oma näkyvyys: portfolio, verkkosivu, some, uutiskirje, referenssit, hinnasto julkisena. |
| `TALOUS` | työ | Laskutus, kulut, alv, ennakkovero, YEL, tilitoimisto, kassavirta. |
| `OMA` | henkilökohtainen | Omat selvitykset, hankinnat, terveys ja arki (vain se, minkä omistaja haluaa kirjata). |

Yhdistä `MARKKINOINTI` ja `ASIAKASTYOT`, jos omistaja kokee ne samaksi; erota `NAYTTELYT` omaksi,
jos näyttelytoiminta on iso osa työtä.

## Mitä perustetaan heti

**ASIAKASTYOT**
- `asiakkaat.md`: taulukko asiakkaista (nimi, yhteyshenkilö, mitä tehty, tila, seuraava askel). Ei henkilötietoja yli tarpeen.
- `muistiinpanot/prosessi.md`: työn vaiheet liidi → tarjous → brief → luonnokset → kommentit → toimitus → lasku → jälkihoito, ja mitä kussakin vaiheessa toimitetaan.
- `muistiinpanot/hinnasto.md`: tuntihinta, pakettihinnat, mitä sisältyy, käyttöoikeudet ja lisenssit.
- `muistiinpanot/sopimuspohja.md`: tarjouksen ja sopimuksen vakiolauseet (oikeudet, kierrokset, maksuehdot, peruutus).
- Asiakaskansion pohja `asiakkaat/_pohja/`: `README.md` (brief, yhteys, aikataulu), `versiot.md` (mitä lähetetty milloin), `laskutus.md`.

**TAIDE**
- `teokset.md`: teosluettelo (nimi, vuosi, tekniikka, koko, hinta, tila: työn alla / vapaa / varattu / myyty / näyttelyssä / lainassa, missä kuva on).
- `muistiinpanot/nayttelyt.md`: pidetyt ja tulevat, hakuajat, galleriat ja yhteyshenkilöt.
- `muistiinpanot/myyntikanavat.md`: missä teoksia myydään (oma sivu, galleria, verkkoalusta), provisiot, toimitus.
- `muistiinpanot/apurahat.md`: haettavat apurahat, hakuajat, mitä hakemukseen tarvitaan.

**MARKKINOINTI**
- `muistiinpanot/kanavat.md`: kanavat, mihin kukin on, julkaisurytmi, mikä on toiminut.
- `muistiinpanot/aani.md`: miten omistaja puhuu julkisesti (sanat, joita käyttää ja ei käytä, sävy, kielet).
- `muistiinpanot/referenssit.md`: työt, jotka saa näyttää julkisesti, ja ne, joita ei saa.

**TALOUS**
- `muistiinpanot/rytmi.md`: alv-kaudet, ennakkoveron erät, YEL, tilitoimiston aikataulu, laskutuspäivät.
- `muistiinpanot/kulut.md`: toistuvat kulut (ohjelmistot, tila, materiaalit, vakuutukset).
- Sääntö: tekoäly ei tee maksuja eikä lähetä laskuja; se valmistelee ja omistaja lähettää.

## Erityissäännöt (lisätään projektien CLAUDE.md:hin)

- Suunnittelutiedostot (ai, psd, fig, procreate) ja teoskuvat eivät asu megabrainissa. Projektiin kirjataan polku ja versiohistoria.
- Asiakkaan materiaalia (logot, kuvat, tekstit) ei käytetä toisen asiakkaan työssä eikä omassa markkinoinnissa ilman lupaa; lupa kirjataan asiakkaan `README.md`:hen.
- Teoksen hintaa ei muuteta `teokset.md`:hen ilman omistajan päätöstä; päätös `paatokset.md`:hen.
- Some-julkaisut ja asiakasviestit: luonnos aina chattiin, omistaja julkaisee tai antaa luvan.

## Hyviä ensimmäisiä tehtäviä (askel I)

- Kirjata nykyiset asiakkaat ja niiden tila `asiakkaat.md`:hen sähköpostin perusteella (lukemalla).
- Koota teosluettelo olemassa olevista kuvista ja muistiinpanoista.
- Tehdä hinnasto ja tarjouspohja, joita omistaja on tähän asti kirjoittanut joka kerta uusiksi.
- Käydä läpi tulevan kuukauden kalenteri ja laskutettavat.
