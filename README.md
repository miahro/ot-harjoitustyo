# SchoolTasks

Sovellus on tarkoitettu alakoululaisten (7-12v) matematiikan tehtävien harjoitteleluun. Sovelluksessa:
- voidaan luoda käyttäjätunnuksia
- kirjautua sisään
- kirjautunut käyttäjä voi tehdä tehtäviä: 10 tehtävän sarjoja valitusta aiheesta ja valitulla vaikeustasolla
- tehtävät ovat monivalintatehtäviä: 1 oikea ja 3 väärää vastausta
- kirjautunut käyttäjä voi tarkastella tuloksiaan

Tehtäville on:
- 4 aihetta (yhteenlasku, vähennyslasku, kertolasku ja jakolasku)
- vaikeustaso välillä 1-10

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/changelog.md)
- [Testausdokumentti](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/testaus.md)
- [tuntikirjanpito](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/tuntikirjanpito.md)
- [arkkitehtuuri](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/arkkitehtuuri.md)
- viikko4 [release]()

## Asennus
1. kloonaa repositorio [SchoolTasks](https://github.com/miahro/ot-harjoitustyo)
2. asenna riippuvuudet 
```bash
poetry install
```

3. tehtävälista CSV-tiedoston luominen:
```bash
poetry run invoke generate-questions
``` 

4. alusta tietokanta. **Huomaa!** Tietokannan alustus tyhjentää kaiken jo mahdollisesti tallennetun tiedon tietokannasta
```bash
poetry run invoke build
``` 



## Komentorivitoiminnot


### Ohjelman käynnistäminen

```bash
poetry run invoke start
```

### Testaus
Yksikkötestit ajetaan komennolla:
```bash
poetry run invoke test
```

### Testikattavuus
Testiraportti generoidaan (ajaa myös yksikkötestit) komennolla:

```bash
poetry run invoke coverage-report
```


### Staattisen laadun tarkistus
Koodin staattisen laadun tarkastukseen käytetään *pylint* työkalua. Laadun tarkastus ajetaan komennolla:
```bash
poetry run invoke lint
```
