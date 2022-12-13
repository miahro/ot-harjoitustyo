# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne alla:

![PackageDiagram](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/PackageDiagram.jpg)

Pakkausten sisältö on seuraava:
- ui sisältää käyttöliittymästä vastaavan koodin
- services sisältää sovelluslogiikasta vastaavat luokat
- repositories sisältää luokat, jotka vastaavat tietojen pysyväistallennuksesta sekä tietokantakyselyistä
- entities sisältää sovelluksen käyttämät tieto-luokat

## Käyttöliittymä

Käyttöliittymä sisältää näkymät:
- aloitusnäkymä, jossa valitaan joko uuden käyttäjän luominen tai sisäänkirjautuminen
- uusi käyttäjä näkymä, jossa luodaan uusi käyttäjä
- kirjautumisnäkymä, jossa käyttäjä kirjautuu sisään
- valintanäkymä, jossa valitaan joko tulosten tarkastelu tai aihe sekä vaikeustaso ja jatketaan tehtävänäkymään
- tehtävänäkymässä tehdään tehtäviä
- tulosnäkymässä käyttäjä näkee yhteenvedon tuloksistaan

Jokainen näkymä on toteutettu oman luokkanaan. Käyttöliittymä on eriytetty muuten täysin sovelluslokiigasta, paitsi poikkeuksena tulosnäkymä pitää kirjaa kierroksen tehtävistä (tämä ei ole pysyväistalletettava tieto vaan vain tehtäväkierroksen väliaikainen tieto)

![UI](https://github.com/miahro/ot-harjoitustyo/blob/master/schooltasks/dokumentaatio/kuvat/UIdraft.jpg)

## Sovelluslogiikka

Sovelluksen tietomallin muodostavat luokat:
- User, joka kuvaa käyttäjän ominaisuuksia
- Topic, joka kuvaa tehtävän aiheen ominaisuuksia
- Task, joka kuvaa tehtävän ominaisuuksia
- Result, joka kuvaa tuloksen ominaisuuksia

Näistä tarkemmin alla, kohdassa "Tietokantamalli"

Toiminnallisista kokonaisuuksista vastaavat services-luokat:
- UserServices
- TopicServices
- TaskServices
- ResultServices

Services luokat pääsevät käsiksi tietokannan tietoihin repositories luokkien kautta. Repostitories luokkia on yksi kullekin tietoluokalla:
- UserRepository
- TopicRepository
- TaskRepository
- ResultRepository

Luokkien suhteet kuvattu alla:

```mermaid
 classDiagram
      class UI {

      }
      class User{
          firstname
          lastname
          username
          password
          teacher
      }
    class Result{
          person
          task
          result
      }
      class Task{
          topic_id
          difficulty
          question
          correct
          wrong1
          wrong2
          wrong3
      }
      class Topic{
          topic
      }

    class UserRepository{
          db connection
    }
    class ResultRepository{
          db connection
    }
    class TopicRepository{
          db connection
    }
    class TaskRepository{
          db connection
    }

    class UserServices{
          logged_in_user
          user
    }
    class ResultServices{
    }
    class TopicServices{
          active_topic
    }
    class TaskServices{
          active_difficulty
    }

    UI ..> UserServices
    UI ..> TopicServices
    UI ..> TaskServices
    UI ..> ResultServices
    User <.. UserRepository
    Task <.. TaskRepository
    Topic <.. TopicRepository
    Result <.. ResultRepository
    UserServices -- User
    UserServices ..> UserRepository
    TopicServices ..> TopicRepository
    TopicServices -- Topic
    TaskServices -- Task
    TaskServices ..> TaskRepository
    ResultServices -- Result
    ResultServices ..> ResultRepository
```


## Tietojen pysyväistallennus

### Tietokantamalli
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
### Tiedostot

## Päätoiminnallisuudet

### Käyttäjän kirjautuminen
- lisätään

### Uuden käyttäjän luominen
Uuden käyttäjän luontinäkymässä käyttäjä syöttää tiedot kenttiin:
- etunimi
- sukunimi
- käyttätunnus
- salasana
- salasana uudestaan

ja painaa "Luo uusi käyttäjä" painiketta. 

Kenttien syötteelle on seuraavat kriteerit:
- mikään kenttä ei saa olla tyhjä
- samaa käyttäjätunnusta ei ole olemassa
- salasana ja salasana uudelleen ovat samat

Alla on kuvattu sekvenssikaavio onnistuneelle uuden käyttäjän luonnille:

```mermaid
sequenceDiagram
  actor enduser
  participant ui.new_user_view
  participant UserServices
  participant UserRepository
  participant User
  enduser->>ui.new_user_view: fill fields and click "Luo uusi käyttäjä"
  ui.new_user_view->>UserServices: "create_new_user()
  UserServices->>UserServices: validate_inputs()
  UserServices->>UserServices: passwd1 == passwd2
  UserServices->>User: __init__()
  User-->>UserServices: User
  UserServices-->>UserRepository: user_details_by_user_id(User)
  UserRepository-->>UserServices: empty tuple
  UserServices->>UserRepository: add_user(User)
  UserRepository-->>UserServices: None
  UserServices-->>ui.new_user_view: (True, käyttäjätunnus luotu)
  ui.new_user_view-->>enduser: view message "käyttäjätunnus luotu"
```
Käyttäjän täytettyä tiedot ja klikattua "Luo uusi käyttäjä", ui.new_user_view kutsuu UserServices create_new_user metodia. Metodia tarkastaa ensin, ettei syötteessä ole tyhjiä kenttiä, ja sitten että salasanat ovat samoja. Jomman kumman tarkistuksen epäonnistuminen palauttausi ui.new_user_view:n virheviestin. Tämän jälkeen UserServices luo User-olion. Seuraavaksi UserServices kutsuu UserRepositoryn user_details_by_user_id metodia sen tarkistamiseksi, ettei käyttäjätunnusta ole jo olemassa. Jos on, palautetaan virheviesti ui.new_user_view:lle. Mikäli käyttätätunnusta ei ole olemassa, UserServices kutsuu UserRepositoryn metodia add_user, ja palauttaa "käyttäjätunnus luotu"-viestin ui.new_user_view-näkymälle. ui.new_user_view näyttää viestin käyttäjälle. 

### Tehtävien tekeminen
- lisätään

### Tulosten tarkastelu 
- lisätään
