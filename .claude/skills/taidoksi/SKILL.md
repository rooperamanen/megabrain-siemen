---
name: taidoksi
description: 'Tee tehdystä työstä uudelleenkäytettävä taito (skill) tähän megabrainiin (.claude/skills/<nimi>/SKILL.md) tai päivitä olemassa olevaa, ja päivitä TAIDOT.md-hakemisto. Käytä AINA työn päätteeksi, kun syntyi toistettava menettely (raportti, tarjous- tai laskupohja, kuvankäsittely, julkaisu, haku, laskenta, tarkistuskierros, admin-rutiini), kun Stop-hook muistuttaa taidoista, tai kun omistaja sanoo "tee tästä taito", "muista jatkossa miten tää tehdään", "automatisoi tää". Käytä myös kesken työn, kun olemassa oleva taito osoittautui vanhentuneeksi. Ei vaadi omistajalta mitään: tekoäly päättää, nimeää ja kirjaa.'
---

# taidoksi: työstä taito

Taidot ovat tekoälyn muistia työtavoista. Omistaja ei käytä niitä itse eikä pyydä niitä; ne tehdään
pyytämättä, jotta sama työ sujuu seuraavalla kerralla ilman uutta selvittelyä. Faktat ja päätökset
menevät projektin tiedostoihin, taitoon menee *miten tehdään*.

## 1. Päätä: taito vai ei

Tee taito, kun vähintään yksi pätee:
- Sama pyyntö tulee todennäköisesti uudestaan (uusi asiakas, uusi versio, uusi kuukausi, uusi teos).
- Menettelyssä on yli kolme askelta tai tietoa, jota ei voi arvata: polkuja, asetusarvoja, mittoja, järjestyksen.
- Syntyi skripti, joka tuotti tuloksen (skripti kuuluu taitoon, `scripts/`-kansioon).
- Jotain meni ensin pieleen ja korjattiin: virhe toistuu ilman taitoa.

Älä tee taitoa pelkästä faktasta tai päätöksestä (→ projektin tiedostot), kertaluonteisesta
keskustelusta, tai kesken olevasta työstä (taito tehdään valmiista, toimivasta menettelystä).

## 2. Uusi vai päivitys

`ls .claude/skills/` ja `grep -ril "<avainsana>" .claude/skills/*/SKILL.md`. Jos aihetta vastaava taito
on olemassa, päivitä sitä pienimmällä muutoksella (uusi askel, korjattu polku, uusi Sudenkuopat-rivi
päivämäärällä). Yksi taito per toistuva tehtävä, ei yksi per keskustelu.

## 3. Nimeäminen

Kansion nimi = frontmatterin `name` = `<projekti>-<mitä-tekee>` pienillä kirjaimilla, väliviivoilla,
ilman ääkkösiä, enintään noin 30 merkkiä. Verbi tai tuotos nimeen: `asiakastyot-tarjous`,
`taide-teosluettelo`, `talous-kuukausikooste`, `markkinointi-julkaise`.

## 4. SKILL.md:n sisältö

Kirjoita tekoälylle, jolla ei ole tämän keskustelun muistia: polut kopioidaan, työkalut nimetään,
arvot kirjataan. Alle 300 riviä.

```markdown
---
name: [projekti]-[mitä-tekee]
description: '[Mitä taito tekee yhdellä virkkeellä, tuotos mukaan.] Käytä kun omistaja sanoo "[lause 1]", "[lause 2]" tai kun [tilanne, jossa tätä tarvitaan nimeämättä]. [Mitä taito EI tee, jos sekaannuksen vaara.]'
---

# [Otsikko]
[1–3 virkettä: miksi tämä taito on, kenen pyynnöstä ja milloin, mikä on lopputuote.]

## Lue ensin
- [projektin tiedosto, josta säännöt tai faktat katsotaan]

## Syöte
[Mitä omistaja antaa. Mitä kysytään, jos puuttuu. Oletusarvot.]

## Menettely
1. [askel: työkalu + tarkka komento tai klikkauspolku]
2. [askel: missä kohtaa luonnos näytetään omistajalle ennen lähetystä]

## Tarkistus
- [mistä näkee, että onnistui; mitä ei saa jäädä: tuplat, vanha hinta, väärä kieli]

## Kirjaa
- [minne tulos merkitään: TILANNE.md, tehtavat.md, loki]

## Sudenkuopat
- [pvm]: [mikä meni pieleen, miksi, miten vältetään]
```

- `description` on ainoa asia, jonka tekoäly näkee ennen taidon valintaa: kerro sekä mitä taito tekee
  että milloin, ja käytä omistajan omia sanoja. 2–4 virkettä, ei rivinvaihtoja.
- **Kuvaus aina yksinkertaisiin lainausmerkkeihin** `description: '…'` (heittomerkki tekstissä tuplataan `''`).
  Lainaamaton kaksoispiste tai kauttaviiva rikkoo jäsennyksen, ja taito ei laukea.
- Selitä miksi jokin kielto tai järjestys on, ei pelkkää "ei saa": silloin seuraava tekoäly osaa soveltaa.
- Pitkät taulukot ja mallitekstit `references/`-kansioon, ajettava koodi `scripts/`-kansioon
  (python3-vakiokirjasto, polut argumentteina, docstring alkuun).

## 5. Lopuksi

1. `python3 _tyokalut/paivita_taidot.py` → `TAIDOT.md` päivittyy.
2. Loppuviestiin yksi rivi: `Taito: <nimi> (uusi | päivitetty): <mitä kattaa>`.
3. Jos taito viittaa tiedostoihin, jotka ovat vain yhdellä koneella, sano se SKILL.md:ssä.
