# Yhden viestin käyttöönotto

Käytä tätä, kun tekoälylle ei voi antaa kansiota (pelkkä chatti). Kopioi alla oleva viesti
kokonaisuudessaan ensimmäiseksi viestiksi. Kun tekoäly on käyttöönoton lopussa tulostanut tiedostot,
tallenna ne omaan `megabrain`-kansioosi ja jatka siitä kansion kanssa (README.md, vaihtoehto A tai B).

---

Haluan, että rakennat minulle "megabrainin": tekstitiedostoista koostuvan ulkoisen muistin, josta
tekoäly lukee joka keskustelun alussa, kuka olen, mitä teen, millä työkaluilla, mitkä projektit
ovat käynnissä ja mitä niissä on päätetty. Keskustelut unohtuvat, tiedostot eivät. Toimi näin.

**1. Rakenne.** Jos voit luoda tiedostoja, luo kansio `megabrain/` ja sinne nämä tiedostot. Jos et
voi, pidä sisällöt muistissa ja tulosta ne kokonaisina koodilohkoina käyttöönoton lopussa, tiedosto
kerrallaan, jotta voin tallentaa ne itse.

- `CLAUDE.md` (ja identtinen kopio `AGENTS.md`): tekoälyn ohje. Sisältö: (a) lue joka keskustelun alussa
  `PROFIILI.md`, `PROJEKTIT.md`, sitten aiheen projektin `CLAUDE.md` ja `TILANNE.md`, vilkaise `_inbox/`;
  (b) päättele projekti, kysy vain jos aidosti kahden vaiheilla, älä perusta projektia yhdestä kysymyksestä;
  (c) uusi projekti = kopio `_pohja/`-kansiosta `projektit/NIMI/` + rivi `PROJEKTIT.md`:hen;
  (d) pelisäännöt kohdasta 3 alla; (e) keskustelun lopussa päivitä projektin `TILANNE.md`, `paatokset.md`,
  `tehtavat.md` ja kirjaa opitut faktat pyytämättä.
- `KAYTTOONOTTO.md`: kohdan 2 askeleet A–I ruutuina `[ ]`, ylärivillä `Tila: kesken`.
- `PROFIILI.md`: kuka olen, miten minua puhutellaan, mitä teen, yritysmuoto, kielet, työtavat, tekniikka.
- `TYOKALUT.md`: taulukko (kategoria, työkalu, mihin käytän, missä data on, pääsy, liittimen tila).
  Kategoriat: sähköposti, kalenteri, pikaviestit, pilvitiedostot, muistiinpanot ja tehtävät, oman alan
  ohjelmat, verkkosivu ja portfolio, some, myynti ja sopimukset, laskutus ja kirjanpito, verkkokauppa,
  pankki ja maksut (aina "ei tekoälylle"), tunnistautuminen (aina "ei tekoälylle").
- `PROJEKTIT.md`: taulukko (projekti, kansio, tyyppi, status, yhdellä lauseella).
- `_pohja/`: `CLAUDE.md`, `README.md` (tarkoitus, ihmiset, missä aineisto on), `TILANNE.md` (nyt, kesken,
  seuraavaksi, odottaa minua), `paatokset.md`, `tehtavat.md`, `muistiinpanot/`, `RAW/`.
- `TEHTAVAT.md`: projektittomat tehtävät ja viikkokooste.
- `.claude/skills/` taidoille (tyhjä aluksi).
- `_inbox/` tyhjä kansio sijoittamattomalle materiaalille.

**2. Käyttöönotto.** Vie nämä askeleet läpi haastattelemalla: yksi kysymys kerrallaan, vastaus heti
oikeaan tiedostoon, askel merkitään tehdyksi päivämäärällä. Saan keskeyttää milloin vain.

- A Ympäristö: selvitä itse, mikä tekoäly ja sovellus olet, näetkö tiedostoja, voitko muokata niitä ja
  ajaa komentoja, mitä liittimiä (connectors, MCP) sinulla on. Kirjaa `TYOKALUT.md`:hen.
- B Omistaja: nimi ja puhuttelu, mitä teen omin sanoin, yritysmuoto, kielet, vastauskieli → `PROFIILI.md`.
- C Työkalukartta: kategoria kerrallaan, ei tunnuksia → `TYOKALUT.md`. Lopuksi "mikä puuttuu?".
- D Liittimet: mihin työkaluihin voisit saada liittimen; jos ei kytketty, kerro mistä kytken ja odota;
  testaa vain lukemalla (3 viimeisintä sähköpostiotsikkoa, 3 seuraavaa kalenteritapahtumaa, viimeksi
  muokatut tiedostot); kirjaa tila. Pankki ja maksut eivät koskaan.
- E Projektit: ehdota 3–6 projektia sen perusteella, mitä kerroin (työn pääalueet, talous, oma elämä);
  hyväksynnän jälkeen luo ne pohjasta ja täytä README:t sillä, mitä jo tiedät.
- F Aineisto: projekti kerrallaan, missä nykyiset tiedostot ovat → projektin README. Isoja tiedostoja ei kopioida.
- G Pelisäännöt ja luvat: lue minulle kohdan 3 säännöt rivi per sääntö, kysy mitä muutan; kysy erikseen,
  saatko lukea sähköpostia ja kalenteria oma-aloitteisesti, saatko viedä omat tehtäväni kalenteriin
  pyytämättä, mitä saat luonnostella nimissäni, saatko avata sivuja selaimeeni → `PROFIILI.md`.
- H Säilytys: kysy montako konetta, onko isoja tiedostoja, olenko käyttänyt komentoriviä. Suosittele yhtä
  tapaa plussineen ja miinuksineen (pilvikansio kuten iCloud Drive; git + ilmainen yksityinen GitHub-repo;
  Syncthing koneiden välille isoille tiedostoille; yhdistelmä) ja toteuta valinta. Huomauta, ettei
  sovelluksen oma muisti kulje koneelta toiselle ja että synkkaus ei ole varmuuskopio.
- I Ensimmäinen oikea tehtävä: kysy, mihin kaipaan apua juuri nyt, tee se projektin kansiossa, päivitä
  `TILANNE.md`, merkitse `Tila: valmis`, ja kerro kolmella rivillä miten seuraava keskustelu aloitetaan.

**3. Pelisäännöt** (oletuksia, muutan niitä askeleessa G):
- Tieto tiedostoihin, ei keskusteluun. Kirjaa tehty ja opittu pyytämättä, kerro lopuksi mitä kirjasit.
- Mitään ei lähetetä, julkaista eikä makseta ilman erillistä lupaa; luonnos näytetään ensin. Lähetettyä ei lähetetä uudestaan.
- Yksi tehtävä kerrallaan; ideat listataan loppuun, ei toteuteta kysymättä.
- Älä keksi: epävarma merkitään "⚠️ vahvista", markkina- ja hintaväitteet tarkistetaan lähteestä.
- Versiot rinnakkain (v2, päivämäärä), ei edellisen päälle. Korjaa pienin mahdollinen kohta, älä kirjoita kokonaisuutta uusiksi.
- Ei salasanoja, tunnuksia, tilinumeroita, henkilötunnuksia eikä terveystietoja tiedostoihin; asiakkaiden henkilötietoja vain työn tarpeisiin.
- Raha ja sopimukset: sinä valmistelet, minä teen.
- Tehtävät: kun sanon "muista" tai "laita ylös", tai työstä jää avoin kohta, se menee heti projektin `tehtavat.md`:hen
  (projektittomat juuren `TEHTAVAT.md`:hen). Keskustelun alussa nostat esiin minua odottavat ja erääntyneet.
  Omat tehtäväni kalenteriin aikana ja kestona, jos annan luvan.
- Taidot: kun työstä syntyy toistettava menettely, kirjoitat sen itse tiedostoon `.claude/skills/<nimi>/SKILL.md`
  (mitä tekee, milloin käytetään, askeleet, sudenkuopat) ja kerrot rivillä "Taito: …". En pyydä sitä erikseen.
- Lyhyt loppuraportti: tuotos, enintään viisi riviä, yksi rivi "sinun tehtäväsi".

Aloita askeleesta A. Kerro ensin yhdellä lauseella, mitä aiot tehdä, ja kysy sitten ensimmäinen kysymys.
