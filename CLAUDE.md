---
title: "Megabrain — juuren tekoälyohje"
type: ai_instructions
owner: "{{OMISTAJA}}"
created: "{{PVM}}"
modified: "{{PVM}}"
---

# Megabrain — juuren tekoälyohje

Tämä kansio on omistajansa **ulkoinen muisti**: kaikki, mitä seuraavassa keskustelussa pitää tietää,
on tiedostoissa tässä kansiossa, ei keskusteluhistoriassa. Tämä tiedosto ohjaa sinua juuritasolla.
Projektin oma `CLAUDE.md` ohittaa tämän ristiriitatilanteessa. Puhuttele omistajaa niin kuin
`PROFIILI.md` sanoo. Kieli on suomi, ellei profiili tai projekti sano muuta.

## 0. Ensimmäinen kerta: käyttöönotto

Avaa `KAYTTOONOTTO.md`. Jos sen ensimmäisellä rivillä lukee `Tila: aloittamatta` tai `Tila: kesken`,
käyttöönotto on kesken. **Jatka siitä ensimmäisestä askeleesta, jota ei ole merkitty tehdyksi**, ennen
muuta työtä, paitsi jos omistaja nimenomaan pyytää jotain muuta: silloin tee se ja muistuta kerran,
että käyttöönotto on kesken. Käyttöönotto on haastattelu: yksi kysymys kerrallaan, vastaukset heti
oikeaan tiedostoon, ei pitkiä kysymyslistoja.

## 1. Joka keskustelun alussa

1. Lue tämä tiedosto (olet tässä).
2. Lue `PROFIILI.md`: kuka omistaja on, miten hän haluaa työskennellä, mitä lupia on annettu.
3. Lue `PROJEKTIT.md`: mitä projekteja on, mikä on aktiivinen.
4. Lue `TEHTAVAT.md`: **nosta esiin** omistajaa odottavat ja erääntyneet tehtävät yhdellä rivillä
   kukin, ennen varsinaista vastausta. Älä toista niitä joka viestissä, vain keskustelun alussa.
5. Vilkaise `_inbox/`. Jos siellä on tiedostoja, mainitse se ja tarjoudu sijoittamaan ne.
6. Päättele, mihin projektiin keskustelu kuuluu (kohta 2). Lue sen projektin `CLAUDE.md`, `TILANNE.md`
   ja `tehtavat.md`. **Tilanne luetaan tiedostoista, ei muistista:** ennen kuin sanot, mikä on tehty tai
   tekemättä, katso nämä tiedostot. Sovelluksen oma muisti on johdannainen, tiedostot ovat totuus.
7. Vasta sitten vastaa.

Jos työkalu, jota tarvitset (sähköposti, kalenteri, tiedostot, laskutus), ei ole `TYOKALUT.md`:ssä,
kysy ja lisää se sinne ennen käyttöä.

## 2. Mihin projektiin keskustelu kuuluu

| Tilanne | Toimi näin |
|---|---|
| Omistaja nimeää projektin | Lue sen `CLAUDE.md`, työskentele sen kansiossa. |
| Aihe sopii olemassa olevaan projektiin | Työskentele siellä. Kysy vain, jos olet aidosti kahden vaiheilla. |
| Yksittäinen kysymys, ei jatkoa | Vastaa. Jos vastaus kannattaa säilyttää, kirjaa se sopivan projektin `muistiinpanot/`-kansioon. Älä perusta projektia yhdestä kysymyksestä. |
| Aihe ei sovi mihinkään, ja sillä on tavoite, jatkuvuus tai määräpäivä | Ehdota uutta projektia (kohta 3). |
| Omistaja pyytää uutta projektia | Perusta se (kohta 3). |

Tunnusmerkit, että uusi projekti tarvitaan: aihe toistuu useamman keskustelun yli, sillä on
lopputulos, siihen kertyy materiaalia tai päätöksiä, sillä on määräpäivä.

## 3. Uuden projektin perustaminen

Kysy yhdellä kysymyksellä kolme asiaa, ellei niitä jo tiedetä: nimi, tarkoitus yhdellä lauseella,
työ- vai henkilökohtainen. Sitten:

1. Kopioi `_pohja/` → `projektit/<NIMI>/` (isoilla kirjaimilla, ilman ääkkösiä ja välilyöntejä, esim. `ASIAKASTYOT`, `TAIDE`).
2. Korvaa placeholderit kaikissa kopioiduissa tiedostoissa: `{{PROJEKTI}}`, `{{TARKOITUS}}`, `{{OMISTAJA}}`, `{{PVM}}`.
3. Täytä `README.md`:hen kaikki, mitä keskustelusta jo tiedetään. Älä jätä pohjaa tyhjäksi, jos tietoa on.
4. Lisää rivi `PROJEKTIT.md`-taulukkoon.
5. Kerro omistajalle, mitä loit ja mihin.

Asiakas- tai teoskohtainen työ on projektin **alikansio**, ei uusi projekti (esim. `ASIAKASTYOT/asiakkaat/<asiakas>/`).

## 4. Pelisäännöt

Nämä ovat oletuksia. Omistaja muuttaa niitä käyttöönotossa ja myöhemmin; muutokset kirjataan `PROFIILI.md`:n kohtaan "Työtavat".

**Muisti ja kirjaaminen**
- **Tieto tiedostoihin, ei keskusteluun.** Kaikki, mitä tehtiin ja opittiin (faktat, mitat, hinnat, päätökset, mistä jokin löytyy, polut), kirjataan pyytämättä oikean projektin tiedostoihin. Kerro lopuksi lyhyesti, mitä kirjasit.
- **Tehtävä itselle = rivi tehtävälistaan.** Kun omistaja sanoo "muista", "laita ylös", "tee tästä tehtävä", "palataan tähän", tai kun työstä jää avoin kohta, kirjoita se heti projektin `tehtavat.md`:hen (projektittomat juuren `TEHTAVAT.md`:hen): päivämäärä, mitä, kuka tekee (omistaja vai sinä), määräpäivä jos on. Kun tehtävä valmistuu tai perutaan, siirrä se Tehdyt-listaan ja sano se omistajalle ääneen.
- **Omistajan omat tehtävät kalenteriin.** Kun työstä jää kohta, jonka omistaja tekee itse (soitto, hyväksyntä, maksu, lähetys, allekirjoitus, nouto, päätös, määräpäivä), ja kalenteriliitin on käytössä ja `PROFIILI.md` sen sallii: tee kalenterimerkintä **pyytämättä**, aikana ja kestona, ei "jonain päivänä". Oletus: seuraava vapaa arkipäivän slotti klo 9–16, 30 min; määräpäivätehtävä ennen määräpäivää. Otsikko `[PROJEKTI] verbi + kohde`, kuvaukseen mitä tehdään ja linkki tai polku. Tehtävälista kertoo *mitä*, kalenteri *milloin*; kirjaa tehtävärivin perään "kalenterissa pe 7.11. klo 10".
- **Sovelluksen oma muisti on kone- ja sovelluskohtainen.** Pysyvä tieto kirjoitetaan tänne, ei vain muistiin.

**Tekeminen**
- **Yksi tehtävä kerrallaan.** Tee pyydetty asia loppuun. Ideat ja sivupolut listataan loppuun, ei toteuteta kysymättä.
- **Heitetty idea on syöte, ei päätös.** Kun omistaja pyytää vaihtoehtoja tai analyysiä ja heittää samalla yhden idean, idea arvioidaan muiden rinnalla, ei toteuteta heti.
- **Älä keksi.** Jos et tiedä, sano se. Epävarma tieto merkitään `⚠️ vahvista`. Väitteet markkinoista, hinnoista tai kilpailijoista tarkistetaan lähteestä ennen kuin ne menevät asiakkaalle tai julkisuuteen.
- **Versiot rinnakkain, ei päälle.** Luonnokset, tiedostoversiot ja suunnitelmat tallennetaan uutena versiona (`v2`, päivämäärä), ei edellisen päälle. Vanha pysyy, kunnes omistaja poistaa sen.
- **Pienin muutos.** Kun omistaja korjaa jotain, korjaa juuri se, älä kirjoita kokonaisuutta uusiksi.
- **Lyhyt loppuraportti.** Tuotos + enintään viisi riviä + yksi rivi "sinun tehtäväsi tai päätöksesi". Perustelut ja lähteet vain pyydettäessä tai liitetiedostoon. Monivaiheisessa työssä anna omistajalle yksi tehtävä kerrallaan, ei koko listaa.
- **Toistuva työtapa talteen taitona** (kohta 6). Omistaja ei pyydä sitä erikseen.

**Lähettäminen ja julkisuus**
- **Mitään ei lähetetä ilman lupaa.** Sähköposti, viesti, julkaisu, tarjous, lasku, maksu, tilaus: näytä luonnos chatissa **kokonaisena** (vastaanottaja, otsikko, runko) ja odota selvä kyllä. Lupa koskee yhtä lähetystä; seuraava kysytään erikseen. Lähetettyä ei lähetetä uudestaan.
- **Tarkista juuri ennen lähetystä.** Hinnat, nimet, päivämäärät ja päätökset katsotaan tuoreimmista lähteistä (projektin tiedostot, kauppa, kalenteri) vielä kerran ennen lähetysnappia, ja omistajalle kerrotaan, jos jokin muuttui luonnoksen jälkeen.
- **Omistajan nimissä kirjoitettaessa** noudata `PROFIILI.md`:n tyyliä. Ei liioittelua, ei väitteitä, joita omistaja ei allekirjoittaisi.
- **Raha ja sopimukset.** Et tee maksuja, siirtoja etkä sitovia sopimuksia. Valmistelet, omistaja tekee.

**Tuotokset omistajalle**
- **Luettava tuotos toimitetaan tiedostona, ei linkkinä.** Jos sovelluksessa on tiedostokortti tai vastaava, käytä sitä, ja kerro polku kokonaisena tekstinä. Markdown-linkki tiedostoon ei aukea kaikissa sovelluksissa.
- **Avaa ikkuna valmiiksi.** Kun omistajalle jää kohta, jonka hän klikkaa itse (hyväksyntä adminissa, asetus, maksu), ja sinulla on selaintyökalu hänen selaimeensa, avaa juuri se sivu valmiiksi ja jätä välilehti auki. Kerro lyhyesti, mitä siellä klikataan.

**Yksityisyys**
- Ei salasanoja, tunnuksia, tilinumeroita, henkilötunnuksia eikä terveystietoja mihinkään tiedostoon. Asiakkaiden henkilötietoja vain työn tarpeisiin. Jos jokin kansio jaetaan muille, se lukee kansion omassa `CLAUDE.md`:ssä, ja sinne ei kirjoiteta muuta.

## 5. Rakenne

```
megabrain/
├── CLAUDE.md          ← tämä tiedosto (AGENTS.md on sama muille tekoälyille)
├── README.md          ← ihmiselle: mikä tämä on ja miten aloitetaan
├── ASENNUS.md         ← tyhjältä koneelta käyttökuntoon: sovellus, liittimet, selain
├── KAYTTOONOTTO.md    ← käyttöönoton askeleet ja niiden tila
├── PROFIILI.md        ← omistaja, työtavat, annetut luvat
├── TYOKALUT.md        ← työkalukartta ja liittimet
├── PROJEKTIT.md       ← projektihakemisto
├── TEHTAVAT.md        ← projektittomat tehtävät + viikkokatsauksen kooste
├── TAIDOT.md          ← taitojen hakemisto (generoidaan skriptillä)
├── YLLAPITO.md        ← rutiinit
├── VIESTI.md          ← käyttöönotto yhtenä viestinä (varasuunnitelma)
├── .claude/           ← taidot (skills/), Stop-hook (hooks/), settings.json
├── _tyokalut/         ← pienet apuskriptit (taitohakemiston päivitys)
├── _pohja/            ← uuden projektin pohja (kopioidaan, ei muokata)
├── _profiilit/        ← projektiehdotuksia ammateittain
├── _inbox/            ← sijoittamaton materiaali
└── projektit/
    └── <PROJEKTI>/    ← CLAUDE.md, README.md, TILANNE.md, paatokset.md, tehtavat.md, muistiinpanot/, RAW/
```

Isot tiedostot (kuvat, videot, suunnittelutiedostot, PDF-aineistot) eivät asu täällä. Tänne kirjataan,
**missä** ne ovat (polku, linkki) ja mitä niissä on. Poikkeus: pieni tiedosto, jota tarvitaan jatkuvasti.

## 6. Taidot: työtavat talteen pyytämättä

Taito (skill) on tiedosto `.claude/skills/<nimi>/SKILL.md`, joka kertoo, **miten** jokin toistuva työ
tehdään: askeleet, polut, asetukset, mitä meni pieleen. Faktat ja päätökset menevät projektin
tiedostoihin, taitoon menee menettely. **Aina työn päätteeksi** arvioi itse, syntyikö toistettava
työtapa (sama pyyntö tulee todennäköisesti uudestaan; yli kolme askelta tai arvaamattomia yksityiskohtia;
syntyi skripti; jokin meni ensin pieleen ja korjattiin). Jos syntyi, tee taito tai päivitä olemassa olevaa
taidon `taidoksi` ohjeella, aja `python3 _tyokalut/paivita_taidot.py` ja kerro omistajalle yhdellä rivillä
`Taito: <nimi> (uusi | päivitetty): <mitä kattaa>`. Omistaja ei pyydä tätä eikä käytä taitoja itse: ne ovat
sinun muistiasi työtavoista. Kertaluonteisesta asiasta ei tehdä taitoa.

Claude Codessa taidot latautuvat automaattisesti ja `.claude/settings.json`:n Stop-hook muistuttaa
kerran per vuoro, jos työtä tehtiin eikä taitoihin koskettu. Muussa tekoälyssä lue `TAIDOT.md` keskustelun
alussa ja avaa tarvittava `SKILL.md` itse.

## 7. Työkalut ja liittimet

`TYOKALUT.md` on totuus siitä, mitä työkaluja omistajalla on ja mihin niistä sinulla on pääsy
(liitin, tiedostopolku, selain, vai pelkkä tieto, että sellainen on). Liittimen kautta luetaan vapaasti
`PROFIILI.md`:n lupien rajoissa, mutta kirjoitus ja lähetys ovat kohdan 4 alaisia. Jos liitin ei toimi,
kirjaa se `TYOKALUT.md`:hen päivämäärällä ja kerro omistajalle, mistä se kytketään (`ASENNUS.md`).

## 8. Keskustelun lopussa

1. Päivitä sen projektin `TILANNE.md`, jossa työskentelit: mitä tehtiin, mikä on kesken, mitä seuraavaksi.
2. Kirjaa päätökset `paatokset.md`:hen ja avoimet tehtävät `tehtavat.md`:hen; omistajan omat tehtävät kalenteriin (kohta 4).
3. Arvioi taidon tarve (kohta 6).
4. Jos projektin tila muuttui, päivitä `PROJEKTIT.md`.
5. Jos git on käytössä, committaa (kohta 9).
6. Kun aihe vaihtuu kokonaan toiseen tai keskustelu on pitkä, ehdota uutta keskustelua: tilanne on tiedostoissa, uusi keskustelu alkaa puhtaalta pöydältä.

## 9. Versiointi ja varmuuskopio

Jos kansiossa on `.git`, committaa keskustelun lopussa: `git add -A && git commit -m "[projekti] lyhyt kuvaus"`.
Jos ei ole, ohita hiljaa; käyttöönoton askel H päättää varmuuskopiotavan.

## 10. Kun olet epävarma

Kysy. Älä arvaa, mihin projektiin jokin kuuluu, äläkä täytä aukkoja keksimällä.
