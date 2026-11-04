Tila: aloittamatta

# Käyttöönotto

Tekoäly vie nämä askeleet läpi keskustellen. Säännöt tekoälylle:

- **Yksi kysymys kerrallaan.** Älä tulosta koko listaa kysymyksiä. Kerro aluksi yhdellä lauseella, mitä askel koskee ja miksi.
- **Kirjoita heti.** Jokainen vastaus menee mainittuun tiedostoon saman tien, ei keskustelun lopussa.
- **Merkitse tehdyksi:** vaihda `[ ]` → `[x] pvm` ja päivitä ylärivin `Tila:` (`kesken`, lopuksi `valmis`).
- **Saa keskeyttää.** Jos omistaja haluaa lopettaa, päivitä tila ja kerro, mistä jatketaan.
- Jos jokin askel ei koske omistajaa, merkitse `[–] ei tarpeen` ja syy.
- Älä lähetä, julkaise tai muuta mitään käyttöönoton aikana. Liittimien testit ovat pelkkää lukemista.
- Suosittele harkitusti: yksi suositus plussineen ja miinuksineen, ei kaikkia vaihtoehtoja. Helppo oletus
  ensin, ja kerro mitä sillä menettää.

## A. Ympäristö `[ ]`

Selvitä itse, älä kysy omistajalta turhaan: mikä tekoäly ja sovellus olet (Claude Code, Claude-sovellus,
ChatGPT, muu), näetkö tämän kansion tiedostot, voitko muokata niitä, voitko ajaa komentoja (`git --version`,
`python3 --version`), ja mitä liittimiä (connectors, MCP-palvelimia) sinulla on tällä hetkellä käytössä.
Kirjaa `TYOKALUT.md`:n kohtaan "Tekoäly ja liittimet". Jos et voi muokata tiedostoja, kerro se heti:
silloin tulokset annetaan omistajalle kopioitavaksi ja käyttöönottoa jatketaan ympäristössä, joka voi
kirjoittaa. Jos git tai python3 puuttuu, ohjaa `ASENNUS.md`:n kohtaan 2 ja jatka silti.

## B. Omistaja `[ ]`

Kysy vuorotellen: nimi ja miten haluaa, että häntä puhutellaan; mitä hän tekee (yksi kappale omin
sanoin: ammatti, mistä raha tulee, mitä tekee lisäksi); yritysmuoto, jos on (toiminimi, oy,
kevytyrittäjä, palkansaaja); kielet, joilla hän työskentelee; millä kielellä tekoälyn pitää vastata.
Kirjaa `PROFIILI.md`. Korvaa `{{OMISTAJA}}` ja `{{PVM}}` juuren tiedostoissa (`CLAUDE.md`, `AGENTS.md`,
`PROFIILI.md`, `TYOKALUT.md`, `PROJEKTIT.md`, `TEHTAVAT.md`, `YLLAPITO.md`, `SAILYTYS.md`, `ASENNUS.md`).

## C. Työkalukartta `[ ]`

Käy `TYOKALUT.md`:n kategoriat läpi yksi kerrallaan: mitä välinettä omistaja käyttää, mihin, ja missä
sen data on (pilvi, kone, puhelin). Ei tunnuksia eikä salasanoja. Älä kysy kategoriasta, joka on
selvästi turha. Kirjaa taulukkoon. Lopuksi kysy: "Mikä työkalu puuttuu listalta?"

## D. Liittimet `[ ]`

Käy `TYOKALUT.md`:n rivit läpi ja merkitse, mihin niistä sinulla voisi olla liitin. Yleensä:
sähköposti, kalenteri, pilvitiedostot, viestintä (Slack/Teams), muistiinpanot, suunnittelutyökalut
(Figma, Canva), verkkokauppa, laskutus, selain (Claude in Chrome). Jokaisesta tarvittavasta:

1. Onko liitin jo käytössä? Jos ei, kerro omistajalle, mistä se kytketään (`ASENNUS.md` kohta 4) ja odota.
2. Testaa **vain lukemalla**: sähköpostista kolmen viimeisimmän viestin otsikot, kalenterista
   seuraavat kolme tapahtumaa, tiedostoista viimeksi muokatut. Ei lähetyksiä, ei muutoksia.
3. Kirjaa tila taulukkoon: `toimii pvm`, `ei kytketty`, `ei tarjolla`.

Pankki, maksut ja tunnistautuminen eivät kuulu liittimiin. Kirjaa ne riveiksi "ei tekoälylle".

## E. Projektit `[ ]`

Katso `_profiilit/`: jos siellä on omistajan ammattia vastaava profiili, ehdota sen projektijakoa
ja kysy, mitä muutetaan. Muuten ehdota omistajan kuvauksen perusteella 3–6 projektia (työn
pääalueet, talous, oma elämä). Hyväksytyn jaon mukaan: kopioi `_pohja/` jokaiselle, täytä
placeholderit ja `README.md` sillä, mitä jo tiedät (profiilin kuvaukset mukaan), lisää rivit
`PROJEKTIT.md`:hen. Kerro, mitä loit.

## F. Nykyinen aineisto `[ ]`

Kysy projekti kerrallaan, missä sen nykyiset tiedostot ovat (asiakaskansiot, teoskuvat, laskut,
sopimukset, brändiohjeet, portfolio). Kirjaa polut ja linkit projektin `README.md`:hen kohtaan
"Aineisto". Älä kopioi isoja tiedostoja megabrainiin. Jos omistaja haluaa jonkin tiedoston sisällön
heti käyttöön (hinnasto, brändiohje, teosluettelo), lue se ja kirjaa olennainen projektin tiedostoihin.
Jos omistajalla on avoimia asioita mielessä ("pitäisi soittaa", "lasku lähettämättä"), kirjaa ne
saman tien projektin `tehtavat.md`:hen: tehtävälista on käytössä ensimmäisestä päivästä.

## G. Pelisäännöt ja luvat `[ ]`

Lue omistajalle `CLAUDE.md`:n kohta 4 tiivistettynä (yksi rivi per sääntö) ja kysy, mitä hän
muuttaa tai lisää. Kirjaa muutokset `PROFIILI.md`:n kohtaan "Työtavat". Kysy sitten erikseen, yksi kerrallaan,
ja kirjaa `PROFIILI.md`:n kohtaan "Luvat":

1. Saako tekoäly lukea sähköpostia ja kalenteria oma-aloitteisesti keskustelun alussa?
2. Saako tekoäly viedä omistajan omat tehtävät kalenteriin pyytämättä (aika + kesto)? Mihin kalenteriin, mihin kellonaikoihin?
3. Millaisia viestejä tekoäly saa luonnostella omistajan nimissä (asiakasviestit, tarjoukset, some, ei mitään)?
4. Saako tekoäly avata sivuja omistajan selaimeen (Claude in Chrome), kun hänelle jää klikattava kohta?

Kerro lopuksi yhdellä kappaleella, mitä **taidot** ovat (`CLAUDE.md` kohta 6): tekoäly kirjaa toistuvat
työtavat talteen itse, omistajan ei tarvitse pyytää, ja loppuviestissä näkyy rivi "Taito: …", kun niin kävi.

## H. Säilytys, synkkaus ja varmuuskopio `[ ]`

Avaa `SAILYTYS.md`. Kysy sen kolme kysymystä (montako konetta, isot tiedostot, terminaalitottumus) yksi
kerrallaan. Anna **yksi suositus** ja sen plussat ja miinukset kolmella–viidellä rivillä, ja mainitse
lähin vaihtoehto yhdellä rivillä. Omistaja päättää. Toteuta valinta:

- **Git:** `git init` (jos `.git` puuttuu), ensimmäinen commit, ja jos omistaja haluaa etäkopion, ohjaa
  luomaan yksityinen GitHub-repo (ilmainen) ja kytke se remoteksi. Jos kansio kloonattiin paketin
  julkaisijan reposta, **vaihda tai poista `origin` ensin** (`git remote remove origin`).
- **Pilvikansio:** varmista, että `megabrain` on synkatun kansion alla ja iCloudissa "Säilytä ladattuna".
- **Syncthing:** anna asennusohje koneille ja sovi, mikä kone on "aina päällä"; versiointi päälle.
- Kaikissa: muistuta koko koneen varmuuskopiosta (Time Machine).

Kirjaa tapa, polku ja muut koneet `PROFIILI.md`:n kohtaan "Tekniikka". Huomauta, ettei tekoälyn oma
muisti kulje koneelta toiselle. Jos omistaja haluaa etäyhteyden koneiden välille, kirjaa se
`TEHTAVAT.md`:hen myöhemmäksi (`SAILYTYS.md`, Etäyhteys), ei nyt.

## I. Ensimmäinen oikea tehtävä `[ ]`

Kysy: "Mikä on se asia, johon kaipaat eniten apua juuri nyt?" Tee se, projektin kansiossa ja sen
sääntöjen mukaan. Lopuksi päivitä projektin `TILANNE.md`, arvioi taidon tarve, merkitse tämä askel tehdyksi,
vaihda ylärivi `Tila: valmis` ja kerro omistajalle kolmella rivillä, miten seuraava keskustelu kannattaa
aloittaa (nimeä projekti, pudota aineisto `_inbox/`-kansioon, pyydä yhtä asiaa kerrallaan).
