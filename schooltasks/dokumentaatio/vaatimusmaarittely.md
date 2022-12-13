# Vaatimusmäärittely

## Sovelluksen tarkoitus
Kyseessä on alakoululaisten (8-12v) matematiikan koulutehtävien harjoitteluun tarkoitettu sovellus. Tehtävät ovat monivalintatehtäviä, joissa kysymykseen vastataan valitsemalla oikea vastausvaihtoehto. 

## Käyttäjät
Sovelluksessa on kahdenlaisia käyttäjiä:
- oppilaita
- opettaja

## Käyttöliittymä
Alusva luonnos käyttäliittymäksi alla. Tämä kuvaa oppilas käyttäjän perustoimintoja:

![UI](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/UIdraft.jpg)


## Toiminnallisuus

### Käyttäjähallinta
- oppilaat voivat itse luoda käyttäjätunnuksia sekä niihin liittyviä salasanoja. "tehty"
- opettajan tunnus ja salasana luodaan ensimmäisen käynnistyksen yhteydessä


### Tehtvävien ylläpito
Opettaja-roolissa oleva käyttäjä voi ylläpitää tehtävälistoja. Alustavasassa versiossa tehtävälistat syötetään ulkoisena .csv-tiedostona. 

Tehtävillä on:
- aihe (esim. kertotaulut, yhteenlasku, vähennyslasku, jne) "tehty"
- vaikeustaso  "tehty"
- oikea vastausvaihetoehto sekä kolme väärää vastaustavaihtoehtoa "tehty"

### Tehtävien teko
Oppilaat tekevät tehtäviä. Alustavasti oppilas valitsee aiheen ja vaikeustason, ja saa 10 tehtävää suoritettavaksi. Tehtävät ovat monivalintatyyppisiä (vaihtoehdot a-d). "tehty"

### Tulosten seuranta
- oppilaan tekemistä tehtävisä pidetään kirjaa:
    - aihe "tehty"
    - oikeat / väärät vastaukset "tehty"
    - vaikeustaso "tehty"
- oppilas voi tarkistaa omat tuloksensa "tehty"
- opettaja voi tarkista kaikkien oppilaiden tulokset

## Mahdollinen jatkokehitys
- tehtävien automaattinen generointi "tehty"
- säädettävä aikaraja (lisävaikeustaso) tehtäville
- laajennetaan tulosten tilastointinäkymiä
- mahdollisesti muiden aiheiden kuin matematiikan tehtävien lisäys

