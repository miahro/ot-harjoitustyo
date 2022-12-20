# Testausdokumentti

## Yksikkö- ja integraatiotestaus

Tehdyille luokille sekä moduleilla on toteutettu automaattisia yksikkö- ja integraatiotestejä. Testien yleinen periaate on ollut luoda yksittäisiä testitapauksia (testikäyttäjiä, testiaiheita, testitehtäviä) ja varmistaa, että näistä vastaavien luokkien funktiot palauttavat oikeat arvot. Testit on toteutettu:
- kaikille entities-luokille
- kaikille repositories-luokille
- kaikille services luokille
- sekä apuluokalle/ohjelmalle QuestionGenerator

Testauksen ulkopuoelle on jätetty:
- käyttöliittymä (index.py sekä kaikki ui-hakemistossa oleva koodi)


## Testikattavuus

Lopullinen testikattavuus on 96%. Testien ulkopuolelle jäävät haarat ovat lähinnä koodirivejä, jotka liittyvät:
- ohjelman kutsumiseen komentoriviltä
- tiedostojen puuttumiseen liittyviin if-lauseisiin.

Testikattavuus alla:

![coverage](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_coverage.png)


## Järjestelmätestaus

Järjestelmätestausta on tehty manuaalisesti. 

### Asennus ja konfigurointi

Asennuksen ja konfiguroinnin toimivuus on testattu fuksi-läppärin Cubbli-linux ympäristössä, sekä laitoksen virtuaalikoneella. Asennus ja konfiguraatiotestauksessa on suoritettu [README](https://github.com/miahro/ot-harjoitustyo/blob/master/README.md) ohjeistamat asennustoimet, sekä käynnistäminen ja muut komentorivitoiminnot. 

### Toiminnallisuudet

Ohjelman toiminnallisuuksia on testattu manuaalisesti sekä käyttämällä ohjelmaa kuten tarkoitettu että tekemällä tarkoituksella virhetilanteita. Muunmuassa seuraavia virhetilanteita on tehty tarkoituksella:
- luodaan uusi käyttäjä epäkelvoilla syötteillä (tyhjiä kentti, salasana ja salasana uudestaan eroavat, yritetään luoda olemassaoleva käyttäjätunnus uudestaan)
- yritetään kirjautua väärällä salasanalla
- yritetään katsoa tuloksia, ennen kuin käyttäjä on tehnyt yhtään tehtävää
- klikkaillaan tehtävänäkymässä "vastaa" valitsematta mitään vaihtoehtoa

Manuaalisessa toiminnallisuustestauksessa ilmi tulleet virheet on korjattu. 

### Loppukäyttäjätestaus

Ohjelma on annettu loppukäyttäjäryhmään kuuluvalle käyttäjälle (12v) testattavksi ohjeella:
- käytä ohjelmaa ns. normaalisti
- yritä tehdä tahallaan kaikki väärin
- toimiiko kummallakaan tavalla ohjelma selvästi väärin, epäloogisesti tai saako ohjelman kaatumaan tai jumittumaan

Loppukäyttäjätestauksen perusteella löytyi yksi tietokannan alustukseen liittyvä virhe (sama kysymys toistui useita kertoja), joka korjattiin. Ohjelmaa ei saatu kaatumaan tai jumittumaan. 


