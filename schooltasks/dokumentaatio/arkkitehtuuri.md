# Arkkitehtuurikuvaus

## Rakenne

![PackageDiagram](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/PackageDiagram.jpg)



## Käyttöliittymä

## Sovelluslogiikka

## Tietojen pysyväistallennus
Tiedot tallennetaan sqlite3 tietokantaan. 

Luokkien:
- User
- Task
- Topics
- Result

data tallennetaan kaikki SQL tietokantaan. Tietokannan taulut ja kentät kuvattu alla. Tarkemmin [schema.sql](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/schema.sql) 

```mermaid
 classDiagram
      class User{
          id
          firstname
          lastname
          username
          password
          teacher
      }
      class Topics{
          id
          topic
      }
      class Tasks{
          id
          topic_id
          difficulty
          question
          correct
          wrong1
          wrong2
          wrong3
      }
    class Results{
          id
          person_id
          task_id
          result
      }
    Tasks --> Results
    Tasks <-- Topics
    Results <-- User
```


## Päätoiminnallisuudet

### Käyttäjän kirjautuminen


### Uuden käyttäjän luominen

### Tehvävien tekeminen

### Tulosten tarkastelu 

### Opettajan toiminnallisuudet 