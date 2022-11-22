

```mermaid
 classDiagram
    Pelaaja "1"--"1"Pelinappula
    Pelilauta "1"--"40"Ruutu
    Peli "1"--"1"Pelilauta
    Peli "1"--"2-8" Pelaaja
    Peli "1"--"2"Noppa
    Pelilauta "1"..>"1"Pelinappula
      class Peli{

      }
      class Pelaaja{

      }
      class Noppa{

      }
      class Pelilauta{

      }
      class Ruutu{

      }
      class Pelinappula{

      }
```