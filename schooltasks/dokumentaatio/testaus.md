# Testausdokumentti

## Yksikkötestaus

Tehdyille luokille sekä moduleilla on toteutettu yksikkötestejä. Yksikkötestien yleinen periaate on ollut luoda yksittäisiä testitapauksia (testikäyttäjiä, testiaiheita, testitehtäviä) ja varmistaa, että näistä vastaavien luokkien funktiot palauttavat oikeat arvot. Osalle luokista ja moduleista yksikkötestit ovat vielä tekemättä tai testikattavuus on vajaa, tämä johtuu ajanpuutteesta, ja testikattavuutta parannetaan seuraaviin palautuksiin.

Testikattavuus alla:

![coverage](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_coverage.png)


## Järjestelmätestaus

Järjestelmätestausta on tehty manuaalisesti. 

### Asennus ja konfigurointi
Asennuksen ja konfiguroinnin toimivuus on testattu fuksi-läppärin Cubbli-linux ympäristössä, sekä laitoksen virtuaalikoneella. Asennus ja konfiguraatiotestauksessa on suoritettu [README](https://github.com/miahro/ot-harjoitustyo/blob/master/README.md) ohjeistamat asennustoimet, sekä käynnistäminen ja muut komentorivitoiminnot. 

### Toiminnalisuudet
Ohjelman toiminnallisuuksia on testattu manuaalisesti sekä käyttämällä ohjelmaa kuten tarkoitettu että tekemällä tarkoituksella virhetilanteita. Muunmuassa seuraavia virhetilanteita on tehty tarkoituksella:
- luodaan uusi käyttäjä epäkelvoilla syötteillä (tyhjiä kentti, salasana ja salasana uudestaan eroavat, yritetään luoda olemassaoleva käyttäjätunnus uudestaan)
- yritetään kirjautua väärällä salasanalla
- yritetään katsoa tuloksia, ennen kuin käyttäjä on tehnyt yhtään tehtävää
- klikkaillaan tehtävänäkymässä "vastaa" valitsematta mitään vaihtoehtoa

Manuaalisessa toiminnallisuustestauksessa ilmi tulleet virheet on korjattu. 

