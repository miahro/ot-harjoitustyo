# Vaatimusmäärittely

## Sovelluksen tarkoitus
Kyseessä on alakoululaisten (7-12v) matematiikan koulutehtävien harjoitteluun tarkoitettu sovellus. Tehtävät ovat monivalintatehtäviä, joissa kysymykseen vastataan valitsemalla oikea vastausvaihtoehto. 

## Käyttäjät
Sovelluksen käyttäjät ovat oppilaite


## Käyttöliittymä
Käyttöliittymän periaatekuva alla.

![UI](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/UIdraft.jpg)


## Toiminnallisuus

### Käyttäjähallinta
- oppilaat voivat itse luoda käyttäjätunnuksia sekä niihin liittyviä salasanoja. 
- oppilaat voivat kirjautua sisään


### Tehtvävien ylläpito
Tehtävät syötetään ohjelman tietokannalle .csv-tiedostona. Tehtävätiedosto voidaan täyttää manuaalisesti tai käyttää "generate_questions" apuohjelmaa, joka generoi tehväviä (2200 kpl) automaattisesti. 

Tehtävillä on:
- aihe
    - toteutetut aiheet: yhteenlasku, vähennyslasku, kertolasku, jakolasku
    - aiheita voi laajentaa
- vaikeustaso 1-10
- oikea vastausvaihetoehto sekä kolme väärää vastaustavaihtoehtoa

### Tehtävien teko
Oppilaat tekevät tehtäviä. Oppilas voi valita:
- aiheen
- vaikeustason
 
Oppilas saa tehtäviä suoritettavaksi 10 kappaleen sarjoissa. Tehtävät ovat monivalintatyyppisiä (vaihtoehdot a-d, sis. yksi oikea ja kolme väärää vaihtoehtoa). 

### Tulosten seuranta
- oppilaan tekemistä tehtävisä pidetään kirjaa:
    - aiheittain
    - vaikeustasoittain
    - oikeat / väärät vastaukset
- oppilas voi tarkistaa omat tuloksensa:
    - yhteenvetona taulukkomuodossa (kaikki tehtävät yhteensä, oikeita, vääriä, oikein-%), taulukossa myös aiheittain tehtäviä yhteensä, oikeita, vääriä, oikein-%
    - graafisena esityksenä aiheittain yksityiskohtaisemmin (per aihe, per vaikeustaso, oikeita ja vääriä kullekin)


## Mahdollinen jatkokehitys
- tehtävien automaattinen generointi voisi olla parempi
- säädettävä aikaraja (lisävaikeustaso) tehtäville
- laajennetaan tulosten esittämistä
- mahdollisesti muiden aiheiden kuin matematiikan tehtävien lisäys
- opettajan toiminnallisuudet (kaikkien oppilaiden tulosten katsominen)

