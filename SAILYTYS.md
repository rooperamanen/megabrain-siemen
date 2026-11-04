---
title: "Säilytys, synkkaus ja varmuuskopio"
modified: "{{PVM}}"
---

# Säilytys, synkkaus ja varmuuskopio

Tekoäly käyttää tätä käyttöönoton askeleessa H: se kysyy kolme asiaa ja suosittelee **yhtä** tapaa
plussineen ja miinuksineen, ei listaa kaikkea. Omistaja päättää. Valinta kirjataan `PROFIILI.md`:n kohtaan "Tekniikka".

## Kolme kysymystä

1. **Montako konetta** käyttää megabrainia (ja puhelin)?
2. **Isot tiedostot:** onko työssä kuvia, videoita, suunnittelutiedostoja, jotka pitäisi olla samoina joka koneella?
3. **Terminaali:** onko omistaja koskaan käyttänyt komentoriviä tai gitiä, vai haluaako hän, että tekoäly hoitaa kaiken tekniikan?

## Vaihtoehdot

| | A. Pilvikansio (iCloud Drive, Google Drive, Dropbox, OneDrive) | B. Git + GitHub | C. Syncthing | D. Yhdistelmä |
|---|---|---|---|---|
| **Mitä** | `megabrain/` pilvipalvelun synkkaamassa kansiossa | kansio on git-repo, etäkopio GitHubissa yksityisenä repona | koneet synkkaavat suoraan keskenään, ei pilveä | tekstit gitillä (B), isot tiedostot Syncthingillä (C) |
| **Hinta** | kuuluu usein jo tilaukseen; tila maksaa, kun loppuu | ilmainen (yksityiset repot ilmaisia) | ilmainen, avoin lähdekoodi | ilmainen |
| **Useampi kone** | kyllä, automaattisesti | kyllä, mutta vaatii "tallenna ja hae" (tekoäly tekee: commit, push, pull) | kyllä, automaattisesti kun vähintään kaksi konetta on päällä yhtä aikaa | kyllä |
| **Versiohistoria** | heikko (palvelun oma tiedostohistoria, 30 pv tms.) | täysi: joka muutos, kuka, milloin, miksi; vanha versio palautettavissa | ei oletuksena; "file versioning" -asetus pitää vanhat kopiot | täysi teksteille |
| **Isot tiedostot** | ok, kunnes tila loppuu | **ei**: kuvat ja videot eivät kuulu gitiin | **hyvä**, tämä on Syncthingin vahvuus | hyvä |
| **Vaatii** | ei mitään | gitin asennuksen (Macissa mukana Xcode-komentorivityökaluissa), GitHub-tunnuksen | asennuksen joka koneelle ja laitteiden hyväksynnän; yhden koneen on hyvä olla usein päällä | molemmat |
| **Sudenkuopat** | iCloudin "Optimoi Macin tallennustila" siirtää tiedostoja pilveen, jolloin tekoäly ei näe niitä → pidä kansio "Säilytä ladattuna". Ristiriitakopiot, jos sama tiedosto muokataan kahdella koneella. Git ja pilvikansio samassa kansiossa menevät helposti rikki. | tekoälyn muisti ei kulje mukana (se on tiedostoissa, joten ei haittaa). Jos kansio kloonattiin jonkun muun julkisesta reposta, remote on vaihdettava omaan. | ei "pilvikopiota": jos kaikki koneet hajoavat, data on mennyt → Time Machine tai yksi kone, joka ei ole koskaan pois | enemmän osia |
| **Sopii** | yksi kone, tai kaksi ja ei-tekninen käyttäjä | kaikki, jotka haluavat historian; tekoäly hoitaa komennot | 2+ konetta ja isot tiedostot; ei halua maksaa pilvestä | sama kuin paketin tekijällä: tekstit git, media Syncthing |

## Suositus kysymysten perusteella

- **1 kone, ei isoja tiedostoja, ei terminaalia:** A. Lisäksi Time Machine tai vastaava koko koneen varmuuskopio. Git voi tulla myöhemmin.
- **1 kone, haluaa historian tai tekoäly saa hoitaa tekniikan:** B. Tekoäly tekee `git init`, commitit ja GitHub-remote-ohjeen.
- **2+ konetta, pelkkä teksti:** B (pilvikansio toimii myös, mutta ristiriitakopiot ja muisti sekoittavat).
- **2+ konetta ja isot tiedostot:** D: `megabrain/` gitillä, media omaan Syncthing-kansioon (esim. `~/media-sync/`), ja megabrainiin vain polut. Jos git tuntuu liialta: C kaikelle + versiointi päälle + Time Machine.
- **Tiimi tai kumppani tarvitsee osan aineistosta:** jaettava osa omaksi kansioksi (oma repo tai oma Syncthing-jako), ei koko megabrain.

## Etäyhteys toiselta koneelta

Kun megabrainia halutaan käyttää vieraalta koneelta tai kotikoneelta toimistokoneeseen: **Tailscale**
(ilmainen henkilökohtaiseen käyttöön) yhdistää omat koneet yksityisverkoksi, ja macOS:n Etäkirjautuminen
(SSH) + Näytön jakaminen avataan Jakaminen-asetuksista. Ei portinavauksia reitittimeen. Tämä on
lisävaihe, ei käyttöönoton osa: kirjaa `PROFIILI.md`:hen "myöhemmin", jos kiinnostaa.

## Riippumatta valinnasta

- Tekoälyn sovelluskohtainen muisti ei kulje koneelta toiselle. Kaikki pysyvä on tiedostoissa; siksi säännöt vaativat kirjaamista.
- Koko koneen varmuuskopio (Time Machine, tai Windowsissa Tiedostohistoria) aina. Synkkaus ei ole varmuuskopio: poisto synkkaa myös.
- Salasanat ja tunnukset eivät kuulu mihinkään näistä. Salasanahallinta erikseen.
