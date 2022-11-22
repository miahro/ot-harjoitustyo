

```mermaid
 classDiagram
    Pelaaja "1"--"1"Pelinappula
    Pelilauta "1"--"40"Ruutu
    Peli "1"--"1"Pelilauta
    Peli "1"--"2-8" Pelaaja
    Peli "1"--"2"Noppa
    Pelilauta "1"..>"1"Pelinappula
    Katu "1"--"1-4" Talo
    Katu "1"--"1" Hotelli
    Ruutu "1"--"1" Toiminto
    Ruutu <|--Katu
    Ruutu <|--Sattuma_ja_yhteismaa
    Ruutu <|--Asema_ja_laitos
    Sattuma_ja_yhteismaa "1"--"1" Kortti
    Ruutu <|--Aloitusruutu
    Ruutu <|--Vankila
    Kortti "1"--"1"Toiminto
    Pelaaja "1"..>"1" Katu
    Peli "1"..>"1"Vankila
    Peli "1"..>"1"Aloitusruutu
      class Peli{

      }
      class Pelaaja{
        rahat
      }
      class Noppa{

      }
      class Pelilauta{

      }
      class Ruutu{
        sijainti
      }
      class Pelinappula{

      }

      class Toiminto{
        toiminnon tyyppi
      }
      class Katu{
        Nimi
      }

      class Vankila{

      }

      class Aloitusruutu{

      }

      class Sattuma_ja_yhteismaa{

      }

      class Asema_ja_laitos{

      }

      class Kortti {


      }

      class Talo {

      }

      class Hotelli{


      }

```