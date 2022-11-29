# SchoolTasks

Sovellus on tarkoitettu alakoululaisten (7-12v) matematiikan tehtävien harjoitteleluun. 

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/changelog.md)
- [Testausdokumentti](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/testaus.md)
- [tuntikirjanpito](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/tuntikirjanpito.md)
- [arkkitehtuuri](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/arkkitehtuuri.md)


## Asennus
1. kloonaa repositorio [ShoolTasks](https://github.com/miahro/ot-harjoitustyo)
2. asenna riippuvuudet 
```bash
poetry install
```
3. alusta tietokanta. **Huomaa!** Tietokannan alustus tyhjentää kaiken jo mahdollisesti tallennetun tiedon tietokannasta
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
