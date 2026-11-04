---
title: "Asennus tyhjältä koneelta"
modified: "{{PVM}}"
---

# Asennus tyhjältä koneelta

Ohje ihmiselle, joka ei ole koodari. Tehdään kerran per kone, ennen `KAYTTOONOTTO.md`:tä. Käyttöliittymät
muuttuvat; jos jokin kohta ei täsmää, kysy tekoälyltä ja korjaa tämä tiedosto.

## 1. Tekoälysovellus

- **Claude** (suositus tälle paketille): lataa Claude-työpöytäsovellus (claude.ai/download), kirjaudu.
  Sovelluksen **Code**-välilehti avaa kansion projektiksi ja lukee `CLAUDE.md`:n automaattisesti.
  Tarvitaan maksullinen tilaus (Pro tai Max), jotta Claude Code on käytössä. ⚠️ vahvista tilaustaso omasta tilistäsi.
- **Muu tekoäly** (ChatGPT, Cursor, Codex, paikallinen malli): tarvitaan tapa, jolla tekoäly näkee ja
  muokkaa kansion tiedostoja. Ensimmäisessä viestissä: "Lue AGENTS.md ja toimi sen mukaan."

## 2. Komentorivityökalut (Mac)

Tekoäly ajaa pieniä komentoja (git, python3) sinun puolestasi. Macissa ne tulevat Xcode-komentorivityökalujen
mukana. Avaa Pääte (Terminal) ja kirjoita:

```bash
xcode-select --install
```

Hyväksy asennus. Tämän jälkeen `git` ja `python3` toimivat, ja taitomuistutus (`.claude/hooks/`) toimii.
Windowsissa: asenna Git for Windows ja Python 3 (python.org, ruksi "Add to PATH").

## 3. Tämä kansio koneelle

Vaihtoehdot (`SAILYTYS.md` kertoo, mikä sopii):

- **Zip:** pura ja siirrä `megabrain`-kansio kotihakemistoosi, polku `~/megabrain`.
- **GitHubista:** "Code → Download ZIP" tai, jos git on asennettu, Päätteessä:

```bash
git clone https://github.com/rooperamanen/megabrain-siemen.git ~/megabrain
```

  Kloonissa on julkaisijan osoite remote-nimellä `origin`. Käyttöönoton askel H vaihtaa sen omaan
  yksityiseen repoosi tai poistaa sen (`git remote remove origin`), ettei omaa aineistoa yritetä työntää
  vieraaseen repoon.

- **iCloud Drive:** jos valitset pilvikansion, laita `megabrain` iCloud Driven alle ja valitse kansiolle
  Finderissä "Säilytä ladattuna", muuten tekoäly ei näe pilveen siirrettyjä tiedostoja.

## 4. Liittimet (connectors)

Liittimet antavat tekoälylle pääsyn sähköpostiin, kalenteriin ja tiedostoihin. Kytke ne **ennen**
käyttöönottoa, niin askel D voi testata ne heti.

| Liitin | Mistä kytketään (Claude) | Mitä tekoäly saa |
|---|---|---|
| Gmail, Google Calendar, Google Drive | claude.ai → Asetukset → Liittimet (Connectors) → Google → kirjaudu ja hyväksy | lukee postit ja kalenterin, luo luonnoksia ja tapahtumia; lähetys vain luvalla (`CLAUDE.md` kohta 4) |
| Microsoft 365 (Outlook, kalenteri, OneDrive, Teams) | sama paikka → Microsoft 365 | sama kuin yllä |
| Slack, Notion, Canva, Figma, Shopify, muut | sama paikka, jos tarjolla | työkalukohtainen |
| Claude Code -sovelluksessa | kirjoita keskusteluun `/mcp` → näet kytketyt ja kytkettävät | |

Hyväksy liittimelle vain ne oikeudet, joita käyttö tarvitsee. Pankkia, maksuja tai tunnistautumista ei kytketä koskaan.

## 5. Selain (valinnainen, mutta hyödyllinen)

**Claude in Chrome** -laajennus antaa tekoälyn käyttää sinun kirjautunutta Chromeasi: avata sivun valmiiksi
(`CLAUDE.md` kohta 4, "Avaa ikkuna valmiiksi"), lukea hallintapaneelin tai täyttää lomakkeen sinun
katsoessasi. Asenna Chrome Web Storesta, kirjaudu Claudeen laajennuksessa. Tekoäly ei kirjaudu palveluihin
puolestasi eikä syötä salasanoja; kirjaudu itse ja jätä välilehti auki.

## 6. Tarkistus

- Claude Code avaa `~/megabrain`-kansion ja näkee tiedostot.
- Päätteessä `git --version` ja `python3 --version` vastaavat.
- Liittimet näkyvät kytkettyinä.
- Sitten: ensimmäinen viesti "Hei, aloitetaan käyttöönotto."
