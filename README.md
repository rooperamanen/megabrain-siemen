# Megabrain — oma ulkoinen muisti tekoälylle

Tämä kansio on **sinun kontekstisi**: tekstitiedostoja, joista tekoäly (Claude, ChatGPT tai
mikä tahansa muu) lukee joka keskustelun alussa, kuka olet, mitä teet, millä työkaluilla, mitkä
projektit ovat käynnissä ja mitä niissä on päätetty. Keskustelut unohtuvat, tiedostot eivät.
Kansio on sinun, ei palvelun: sen voi avata millä tahansa tekoälyllä, varmuuskopioida ja viedä mukanaan.

Paketti on tarkoituksella **anonyymi ja jaettava**. Siinä ei ole kenenkään tietoja, vaan tyhjät
paikat ja käyttöönotto, jonka tekoäly vie läpi haastattelemalla sinua.

## Mitä tässä on

| Tiedosto / kansio | Mitä varten |
|---|---|
| `CLAUDE.md` | Tekoälyn ohje: mitä se lukee, miten toimii, mitä ei saa tehdä. Claude Code lukee tämän automaattisesti. |
| `AGENTS.md` | Sama ohje muille tekoälyille, jotka lukevat tämännimisen tiedoston (esim. Codex). Pidä samana kuin `CLAUDE.md`. |
| `KAYTTOONOTTO.md` | Käyttöönoton askeleet. Tekoäly vie ne läpi ensimmäisissä keskusteluissa ja merkitsee tehdyiksi. |
| `PROFIILI.md` | Kuka olet ja miten haluat työskennellä. Täytetään käyttöönotossa. |
| `TYOKALUT.md` | Työkalukartta: sähköposti, kalenteri, tiedostot, suunnitteluohjelmat, laskutus… ja mihin niistä tekoäly pääsee käsiksi. |
| `PROJEKTIT.md` | Projektihakemisto. Tekoäly lukee tämän joka kerta. |
| `TEHTAVAT.md` | Tehtävät, jotka eivät kuulu mihinkään projektiin, ja viikkokatsauksen kooste. Projektien omat tehtävät ovat niiden `tehtavat.md`:ssä. Tekoäly nostaa sinua odottavat esiin joka keskustelun alussa. |
| `SAILYTYS.md` | Miten kansio säilytetään ja synkataan: pilvikansio, git + GitHub (ilmainen), Syncthing, yhdistelmä; etäyhteys. Tekoäly suosittelee tämän pohjalta käyttöönotossa. |
| `ASENNUS.md` | Tyhjältä koneelta käyttökuntoon: sovellus, komentorivityökalut, liittimet, selainlaajennus. |
| `YLLAPITO.md` | Rutiinit: mitä tehdään keskustelun lopussa, viikoittain, kuukausittain. |
| `TAIDOT.md` + `.claude/skills/` | Taidot: tekoälyn omat muistiinpanot toistuvista työtavoista. Se tekee ne itse työn päätteeksi, sinun ei tarvitse pyytää. `.claude/hooks/` muistuttaa siitä Claude Codessa. |
| `VIESTI.md` | Käyttöönotto yhtenä viestinä, kun tekoälylle ei voi antaa kansiota. |
| `_pohja/` | Uuden projektin pohja. Kopioidaan, ei muokata. |
| `_profiilit/` | Valmiita projektiehdotuksia eri ammateille (esim. luova freelancer). Tekoäly käyttää näitä käyttöönotossa. |
| `_inbox/` | Pudota tänne tiedostot, joille ei vielä ole paikkaa. Tekoäly sijoittaa ne. |
| `projektit/` | Jokainen projekti omaan kansioonsa. Syntyy käyttöönotossa. |

## Miten aloitat

Varaa noin tunti. Käyttöönotto on keskustelu, ei lomake: tekoäly kysyy yhden asian kerrallaan
ja kirjoittaa vastaukset tiedostoihin. Sen voi keskeyttää ja jatkaa myöhemmin.

Jos koneella ei vielä ole tekoälysovellusta, komentorivityökaluja tai liittimiä, tee ensin `ASENNUS.md`.

**Helpoin: anna Claudelle tämä viesti.** Avaa Claude-sovellus, Code-välilehti, valitse kansioksi vaikka
kotikansiosi ja liitä:

> Hae minulle megabrain-aloituspaketti ja asenna se. 1) Lataa
> https://github.com/rooperamanen/megabrain-siemen/archive/refs/heads/main.zip ja pura se niin, että kansion
> sisältö päätyy polkuun ~/megabrain (tai kloonaa repo sinne ja poista sitten remote origin, koska se on
> julkaisijan repo). Jos ~/megabrain on jo olemassa, älä kirjoita päälle vaan kysy. 2) Tarkista, että
> ~/megabrain/CLAUDE.md ja KAYTTOONOTTO.md ovat paikallaan. 3) Lue CLAUDE.md ja ASENNUS.md ja kerro, mitä
> koneelta vielä puuttuu. 4) Pyydä minua avaamaan ~/megabrain projektiksi ja kirjoittamaan "Hei, aloitetaan
> käyttöönotto", tai jatka käyttöönottoa heti KAYTTOONOTTO.md:n mukaan, jos pystyt.

**Vaihtoehto A, Claude Code -sovellus, käsin.** Siirrä tämä `megabrain`-kansio kotihakemistoosi
(`~/megabrain`); GitHubista joko "Download ZIP" tai `git clone … ~/megabrain` (`ASENNUS.md` kohta 3). Avaa Claude Code, valitse kansio projektiksi ja kirjoita ensimmäiseksi viestiksi:

> Hei, aloitetaan käyttöönotto.

Claude lukee `CLAUDE.md`:n, huomaa että käyttöönotto on kesken, ja alkaa kysyä.

**Vaihtoehto B, muu tekoäly, joka näkee tiedostoja** (ChatGPT:n projektit, Cursor, Codex, paikallinen
malli…). Anna sille tämä kansio ja sano samalla: "Lue ensin AGENTS.md ja toimi sen mukaan. Aloitetaan käyttöönotto."

**Vaihtoehto C, pelkkä chatti ilman tiedostoja.** Kansiossa on `VIESTI.md`: yksi pitkä viesti,
joka pyytää tekoälyä luomaan rakenteen itse ja vetämään käyttöönoton. Tämä toimii, mutta tiedostot
jäävät silloin tekoälyn puolelle: siirrä ne mahdollisimman pian omaan kansioosi (vaihtoehto A tai B).

## Ennen kuin aloitat, kokoa käsille

- Lista työkaluistasi: sähköposti(t), kalenteri, pilvitiedostot, suunnitteluohjelmat, laskutus,
  some-kanavat, verkkokauppa tai galleriat, muistiinpanot. Ei tunnuksia, pelkät nimet.
- Tieto siitä, mitä **liittimiä** (connectors, MCP) tekoälysovelluksessasi on käytössä tai saatavilla:
  Claudessa Asetukset → Liittimet (Connectors), Claude Codessa `/mcp`. Sähköposti ja kalenteri kannattaa
  kytkeä ennen käyttöönottoa, niin tekoäly voi testata ne saman tien.
- Kolme asiaa, joihin kaipaat eniten apua juuri nyt. Käyttöönotto päättyy ensimmäiseen oikeaan tehtävään.
- Vastaus kolmeen kysymykseen: montako konetta käytät, onko isoja tiedostoja (kuvat, videot), oletko
  käyttänyt komentoriviä. Niiden perusteella tekoäly suosittelee säilytystavan (`SAILYTYS.md`).

## Mitä tekoäly tekee pyytämättä

- Kirjaa tehdyn ja opitun tiedostoihin ja kertoo lopuksi, mitä kirjasi.
- Pitää tehtävälistaa: "muista", "laita ylös" → rivi `tehtavat.md`:hen; sinua odottavat nostetaan esiin keskustelun alussa.
- Vie sinun omat tehtäväsi kalenteriin aikana ja kestona, jos annat luvan (askel G).
- Tekee toistuvista työtavoista taitoja (`.claude/skills/`), jotta sama työ sujuu seuraavalla kerralla.
- Ei lähetä, julkaise eikä maksa mitään ilman erillistä lupaa. Luonnos näytetään aina kokonaan.

## Yksityisyys

Kansioon ei kirjoiteta salasanoja, tunnuksia, tilinumeroita, henkilötunnuksia eikä terveystietoja.
Asiakkaiden tietoja vain sen verran kuin työ vaatii. Jos jaat kansion tai sen osan jollekulle
(tiimi, kirjanpitäjä), tee jaettavasta osasta oma kansio. Säännöt ovat `CLAUDE.md`:n kohdassa 4;
muuta niitä, kun olet eri mieltä, ne ovat sinun.

## Jaa vapaasti

Tämän paketin saa kopioida, muokata ja jakaa ilman rajoituksia (CC0). Jos parannat sitä, jaa parannuksesi eteenpäin.

Versio 2, 4.11.2026. Lähde ja uusin versio: https://github.com/rooperamanen/megabrain-siemen
