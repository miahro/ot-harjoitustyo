# Changelog

## Viikko 3
Toteutettu entities ja repositories luokkia, sekä moduleita konfigurointiin ja alustukseen. Varsinaista ajattevaa kokonaista ohjelmaa ei vielä tässä vaiheessa ole. Tarkemmin toteutetut:
- entities-luokat:
    - User luokka käyttäjän ominaisuuksille
    - Result luokka tuloken ominaisuuksille
    - Topic luokka aiheen ominaisuuksille
    - Task luokka tehtävän ominaisuuksille
- repositories luokat:
    - UserRepository luokka käyttäjään liittyville tietokantaoperaatioille
    - TopicRepository luokka aiheeseen liittyville tietokantaoperaatioille sekä aiheiden lukemiseen ulkoisesta .csv-tiedostosta 
    - TaskRepository luokka tehtäviin liittyville tietokantaoperaatioille sekä tehtävien lukemiseen ulkoisesta .csv-tiedostosta. Tämä luokka on vielä osittain kesken, ja vaatii laajennusta
    - ResultRepository luokka tuloksiin liittyville tietokantaoperaatioille. Tämä luokka on vielä osittain kesken, ja vaatii laajennusta
- konfigurointi ja alustusmoduulit:
    - dbcon.py tietokantayhteyttä varten
    - dbinit.py tietokannan alustusta varten
    - config.py ohjelman alustusta varten, määrittää polut tietokantaan sekä ulkoisiin .csv tiedostoihin

Lisäksi kirjoitettu yksikkötestejä, nämä tarkemmin erillisessä [testausdokumentissa](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/testaus.md)
 

 ## Viikko 4:
 Lisätty alustavia services luokkia. Laajennettu / korjattu entities ja repositories luokkia. Korjattu konfigurointi ja alustusmoduleita. Toteutettu QuestionGenerator-apuluokka. Tarkemmin:
 - services luokat:
    - user_services käyttäjän hallintaan
    - task services tehtävien hallintaan
- QuestionGenerator luokka:
    - apuluokka tehtävien automaattiseen generointiin. 
 - alustava käyttöliittymä
    - ei sisällä vielä läheskään kaikkea toiminnallisuutta, mutta uuden käyttäjän voi luoda, ja käyttäjä voi kirjautua sisään
    - lisäksi näkymien välillä (valinta, tee tehtäviä, tulokset) välillä voi liikkua. Näkymät eivät vielä toistaiseksi näytä mitään 
    