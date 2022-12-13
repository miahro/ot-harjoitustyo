# Käyttöohje

## Asennus ja konfigurointi 

1. asenna riippuvuudet 
```bash
poetry install
```

2. tehtävälista CSV-tiedoston luominen:
```bash
poetry run invoke generate-questions
``` 

3. alusta tietokanta. **Huomaa!** Tietokannan alustus tyhjentää kaiken jo mahdollisesti tallennetun tiedon tietokannasta
```bash
poetry run invoke build
``` 


## Ohjelman käynnistäminen 

```bash
poetry run invoke start
```

## Alkunäkymä

Ohjelman alkunmäkymässä valitaan:
- sisäänkirjautuminen: klikkaa "Kirjaudu sisään"
- uuden käyttäjän luominen: klikkaa "Luo uusi käyttäjä"

![StartView](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_start_view.png)


## Uuden käyttäjän luominen 

Uuden käyttäjän luontinäkymässä syötetään käyttäjän tiedot:
- Etunimi
- Sukunimi
- Käyttäjätunnus
- Salasana
- Salasana uudestaan

![NewUser](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_new_user.png)

Virheellisistä syötteistä syntyy virheilmoitus, eikä uutta käyttäjätunnusta luoda. Oikeiden syötteiden kriteerit:
- mikään kenttä ei saa olla tyhjä
- käyttäjätunnusta ei saa olla ennestään olemassa
- salasana ja salasanan varmitus tulee olla sama merkkijono

Onnistuneesta käyttäjän luonnista tulee ilmoitus "Käyttäjätunnus luotu", jonka jälkeen valitsemalla "Palaa" palataan takaisin alkunäkymään


## Kirjautuminen

Kirjautumisnäkymässä tulee syöttää 
- käyttäjätunnus
- salasana

![Login](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_login.png)

Mikäli käyttäjätunnus ja salasana täsmäävät ohjelman tallentamiin, kirjataan käyttäjä sisään, ja siirrytään automaattisesti valintanäkymään. 

Kirjautusmisnäkymä antaa virheilmoituksen mikäli käyttäjätunnusta ei ole olemassa tai käyttäjätunnus ja salasana eivät täsmää. 

## Valintanäkymä

Valintanäkymässä valitaan:
- tulosten näyttäminen: klikkaa "Näytä tulokset"
- tehtävien tekeminen

Tehtävien tekemistä varten pitää valita:
- aihe alasvetovalikosta valitse aihe
- vaikeustasto alasvetovalikosta valitse vaikeustaso

"Tee tehtäviä" valinta ilmestyy näkyviin vasta aiheen ja vaikeustason valinnan jälkeen.

![Choice](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_choice.png)




## Tehtävien tekeminen

Tehtävien tekonäkymä näyttää-
- kysymyksen
- neljä vastausvaihtoehtoa

Käyttäjä valitsee vastausvaihtoehdon ja klikkaa vastaa. Tämän jälkeen näkyviin ilmestyy uusi kysymys. Kysymyksiä on kierroksella yhteensä 10. 

Kun kaikkiin 10:n kysymykseen on vastattu, ohjelma näyttää kierroksen tuloksen (oikeiden ja väärien vastausten määrän). 

Valitsemalla loppunäkymässä "Palaa" palataan takaisin valintanäkymään. 

![Task](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_task.png)

## Tulosten tarkastelu

Tulosnäkymässä ohjelma näyttää oppilaan tulokset. Tulokset on jaoteltu:
- kaikki aiheet yhteensä
- aiheittan 

Kaikki aiheet yhteensä ja aiheittain näytetään:
- tehtävien yhteismäärä
- oikein vastattuja (kpl)
- väärin vastattuja (kpl)
- oikein vasttuja (%)

![Result](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/ohte_result.png)

TÄTÄ NÄKYMÄÄ PARANNETAAN VIELÄ