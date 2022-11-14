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
- oppilaat voivat itse luoda käyttäjätunnuksia sekä niihin liittyviä salasanoja. 
- opettajan tunnus ja salasana luodaan ensimmäisen käynnistyksen yhteydessä


### Tehtvävien ylläpito
Opettaja-roolissa oleva käyttäjä voi ylläpitää tehtävälistoja. Alustavasassa versiossa tehtävälistat syötetään ulkoisena .csv-tiedostona. 

Tehtävillä on:
- aihe (esim. kertotaulut, yhteenlasku, vähennyslasku, jne)
- vaikeustaso 
- oikea vastausvaihetoehto sekä kolme väärää vastaustavaihtoehtoa

### Tehtävien teko
Oppilaat tekevät tehtäviä. Alustavasti oppilas valitsee aiheen ja vaikeustason, ja saa 10 tehtävää suoritettavaksi. Tehtävät ovat monivalintatyyppisiä (vaihtoehdot a-d). 

### Tulosten seuranta
- oppilaan tekemistä tehtävisä pidetään kirjaa:
    - aihe 
    - oikeat / väärät vastaukset
    - vaikeustaso
- oppilas voi tarkistaa omat tuloksensa
- opettaja voi tarkista kaikkien oppilaiden tulokset

## Mahdollinen jatkokehitys
- tehtävien automaattinen generointi
- säädettävä aikaraja (lisävaikeustaso) tehtäville
- laajennetaan tulosten tilastointinäkymiä
- mahdollisesti muiden aiheiden kuin matematiikan tehtävien lisäys

