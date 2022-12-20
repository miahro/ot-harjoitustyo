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

Ohjelma lukee tehtävien aiheet CSV tiedostosta "topic.csv" (nimi määritelty .env-tiedostossa), joka löytyy kansiosta "data" . Aihe-CSV tiedosto on osana asennuspakettia, ja tulee olla asennettuna kun tietokantaa alustetaan. Oletuksena aiheet ovat: yhteenlasku, vähennyslasku, kertolasku ja jakolasku. Ohjelma on periaatteessa laajennettavissa lisäämällä aiheita (sekä näihin liittyviä kysymyksiä), mutta tätä laajennettavuutta ei ole laajemmin testattu. Aihe CSV tiedoston formaatti on seuraava:

|topic| 
|:---:| 
|yhteenlasku|
|vähennyslasku|
|kertolasku|
|jakolasku|

Tehtävät syötetään tietokantaan tiedostosta "task.csv" (nimi määritelty .env-tiedostossa), joka sijaitsee kansiossa "data". Tehtävä CSV-tiedoston voisi täyttää manuaalisesti, mutta sen generoimiseksi on apuohjelma "generate_questions.py". Tehtävä-csv tiedoston formaatti on seuraava:

|topic| difficulty|question| correct|wrong1|wrong2|wrong3|
| :---:| :----:|:-----| :-----|:-----|:-----|:-----|
|aihe| vaikeustaso|kysymys|oikea vastaus|väärä vastaus 1|väärä vastaus 2|väärä vastaus 3|
|int 1-4| int 1-10|str|str|str|str|str|

Tietokanta on tallennettu tiedostoon "db.sqlite3" (nimi määritely .env-tiedostossa), kansiossa "data". 

Lisäksi testejä varten on vastaavat tiedostot:
- test_topic.csv (asennetaan paketin mukana)
- test_task.csv (generoidaan testien aikana)
- test_db.sqlite3 (generoidaan testien aikana)

## Päätoiminnallisuudet

### Käyttäjän kirjautuminen

Käyttäjän kirjautumisnäkymässä käyttäjä syöttää tiedot kenttiin:
- käyttäjätunnus
- salasana

ja painaa "Kirjaudu sisään" painiketta. Käyttöliittymä kutsuu userservices.login metodia syötetyillä tiedoilla, ja joko:
- näyttää userservices.login palauttaman virheviestin mikäli kirjatuminen ei onnistunut
- kirjaa käyttäjän sisään, ja siirtyy valintanäkymään, jos kirjautuminen onnistui

Alla kuvattuna sekvenssikaavio onnistuneella sisäänkirjautumiselle:

```mermaid
sequenceDiagram
  actor enduser
  participant ui.choice_view
  participant ui.login_view
  participant UserServices
  participant UserRepository
  participant User
  enduser->>ui.login_view: fill fields and click "Kirjaudu sisään"
  ui.login_view->>UserServices: "login"
  UserServices->>UserRepository: get_pwd_by_user_id()
  UserRepository-->>UserServices: pwd
  UserServices-->>UserServices: pwd==input_pwd
  UserServices->>UserRepository: user_by_user_id
  UserRepository->>User: __init__()
  UserRepository-->>UserServices: user
  UserServices->>UserServices: logged_in_user=user
  UserServices-->>ui.login_view: (True, sisäänkirjauminen onnistui)
  ui.login_view-->>ui.choice_view: view message "käyttäjätunnus luotu"
  ui.choice_view->>enduser: view
```

Epäonnistuneen sisäänkirjautumisen tapauksessa ui.login -view näyttäisi virheviestin, ja sisäänkirjatumisnäkymä jäisi näkyviin. 

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

### Valintanäkymä 

Valintanäkymässä käyttäjää:
- voi kirjautua ulos (palaa takaisin aloitusnäkymään)
- valita aiheen alasvetovalikosta
- valita vaikeustason alasvetovalikosta
- aloittaa tehtävien tekemisen (valittavissa vain, jos aihe ja vaikeustaso on valittu)
- näyttää tulokset

Uloskirjautuminen sekvenssikaaviona:
```mermaid
sequenceDiagram
  actor enduser
  participant ui.start_view
  participant ui.choice_view
  participant UserServices
  enduser->>ui.choice_view: click "Kirjaudu ulos"
  ui.choice_view->>UserServices: logout()
  UserServices->>UserServices: logged_in_user=None
  UserServices-->>ui.choice_view: None
  ui.choice_view-->>ui.start_view: None
  ui.start_view->>enduser: view
```



Aiheen valinta sekvenssikaaviona:
```mermaid
sequenceDiagram
  actor enduser
  participant ui.choice_view
  participant TopicServices
  enduser->>ui.choice_view: select topic (pull-down menu)
  ui.choice_view->>TopicServices: set_active_topic(topic)
  TopicServices->>TopicServices: active_topic=topic
  TopicServices-->>ui.choice_view: None
  ui.choice_view->>enduser: view
```

Vaikeustason valinta sekvenssikaaviona:
```mermaid
sequenceDiagram
  actor enduser
  participant ui.choice_view
  participant TaskServices
  enduser->>ui.choice_view: select difficulty (pull-down menu)
  ui.choice_view->>TaskServices: set_active_difficulty(difficulty)
  TaskServices->>TaskServices: active_difficulty=difficulty
  TaskServices-->>ui.choice_view: None
  ui.choice_view->>enduser: view
```



### Tehtävien tekeminen

Tehtävien tekonäkymässä käyttäjä saa 10:n tehtävän sarjan valitusta aiheesta valitulla vaikeustasolla vastattavaksi. Ui.task_view käyttää sovelluslogiikasta luokkia:
- UserServices: käyttäjän tietojen näyttämiseen, ja kirjautuneen käyttäjän tunnistamiseen
- TopicServices: valitun aiheen tunnistamiseen, ja aiheen näyttämiseen
- TaskServices: valitun aiheenn tunnistamiseen, satunnaisen tehtäväjoukon palauttamiseen, ja tulosten kirjaamiseen


Tehtävien tekeminen sekvenssikaaviona:

```mermaid
sequenceDiagram
  actor enduser
  participant ui.task_view
  participant TaskServices
  participant TaskRepository
  participant ResultServices
  participant ResultRepository
  ui.task_view ->> TaskServices: get_tasks(topic, difficulty, 10)
  TaskServices ->> TaskRepository: get_random_task_list(topic, difficulty, 10)
  TaskRepository-->>TaskServices: [10 x Task]
  TaskServices-->>ui.task_view:[10 x Task]
  loop Tasklist_not_empty
    ui.task_view->>ui.task_view: show question and answer options (randomized order)
    ui.task_view->>enduser: view task
    enduser->>ui.task_view: select answer_option
    ui.task_view->>ui.task_view: answer_option==correct
    ui.task_view->>ResultServices: add_result(active_user, task_id, True/False)
    ResultServices->>ResultRepository: add_result(active_user, task_id, True/False)
    ResultRepository-->>ResultServices: None
    ResultServices-->>ui.task_view: None
  end
  ui.task_view->>enduser: "kaikkiin tehtäviin vastattu"  

```
Piirrosteknisistä syistä luokkia UserServices ja TopicServices ei ole esitetty ylläolevassa diagrammissa. Käytännössä näistä vain käytetään tietoa kirjautuneesta käyttäjästä ja valitusta aiheesta. 


### Tulosten tarkastelu 
- lisätään
