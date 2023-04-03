# Monopolikaavio

Pelissä on pelilauta, pelaajia ja 2 noppaa.
Pelilaudalla on 40 ruutua, joilla kullakin on oma tyyppinsä. Ruutu tietää, mikä on sitä seuraava ruutu.
Pelaajalla on yksi pelinappula, jonka sijainti on aina jokin pelilaudan ruutu.

```mermaid
classDiagram
    Pelaaja "2..8" --> "1" Monopoli
    Pelilauta "1" --> "1" Monopoli
    Pelaaja "1" --> "1" Pelilauta
    Ruutu "40" --> "1" Pelilauta
    ruudunTyyppi "1" --> "1" Ruutu
    Vankila "1" --> "1" ruudunTyyppi
    Katu "1" --> "1" ruudunTyyppi
    Aloitusruutu "1" --> "1" ruudunTyyppi
    Sattuma "1" --> "1" ruudunTyyppi
    Yhteismaa "1" --> "1" ruudunTyyppi
    Laitos "1" --> "1" ruudunTyyppi
    Asema "1" --> "1" ruudunTyyppi
    
        class Monopoli{
            pelaajat
            noppa
            pelilauta
        }

        class Pelilauta{
            ruudut
            aloitusruutuSijainti
            vankilaSijainti
        }
        class Ruutu{
            ruudunTyyppi
            seuraava
        }
        class ruudunTyyppi{
            Vankila
            Katu
            Aloitusruutu
            Sattuma
            Yhteismaa
            Asema
            Laitos
        }
        class Vankila{
            vapaudu()
        }
        class Sattuma{
            nostaKortti()
        }
        class Yhteismaa{
            nostaKortti()
        }
        class Asema{
            nimi
            omistaja
            lunastaVuokra()
        }
        class Laitos{
            nimi
            omistaja
            lunastaVuokra()
        }
        class Aloitusruutu{
            maksaPalkka()
        }
        class Katu{
            nimi
            omistaja
            ostaTalo()
            ostaHotelli()
            lunastaVuokra()
        }
        
        
        class Pelaaja{
            rahat
            nimi
            pelinappula_sijainti
            heitaNoppaa()
        }
```