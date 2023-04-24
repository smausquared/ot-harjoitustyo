# Arkkitehtuurikuvaus

## Rakenne

Peliin pääsee sisälle hyvin yksinkertaisesta käyttöliittymästä, josta voi aloittaa pelin, sulkea pelin ja katsella tulostaulua. Tässä vaiheessa rakenne näyttää tältä:

![](https://github.com/smausquared/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio.png)

Gameloop-luokka toimii pelin koodin luurankona. Ghost-luokka mallintaa pelaajan hahmoa: pelaaja voi kerätä maailmasta Spoon-luokan mallintamia lusikoita.

## Sovelluslogiikka

Peli koostuu muutamasta tärkeästä rakennuspalasesta. Luokka Gameloop saa konstruktorin parametreiksi Ghost-olion, Level-olion ja pygamen screen- ja clock-alustukset. Gameloopin parametrit määritellään pääohjelmassa index.py-tiedostossa. Ghost-olio saa parametriksi sen x- ja y-koordinaatit ja alustavan nopeuden. Level-olio saa parametriksi pelin tason datan*. Level-olio sisältää myös keräiltäviä Spoon-olioita, jotka kasvattavat pelaajan nopeutta. Gameloopin start-metodi aloittaa pelin suorituksen, ja piirtää ruudulle vaaleansinisen taustan, tason* ja keräiltävät lusikat. Sitten kutsutaan Ghost-olion move-metodia, joka liikuttaa pelaajaa right- ja left-parametrien perusteella. Gameloop tarkistaa pelaajan ja lusikoiden törmäykset. Se myös tarkistaa pelaajan nopeuden perusteella, onko hän kerännyt lusikoita: jos on, niin nopeus alkaa pikkuhiljaa laskea, lähestyen alkunopeutta 1. Sitten päivitettyjen koordinaattien perusteella Gameloop piirtää kummituksen.

*Tulevaisuudessa kehitettävä, pvm nyt 24.4.

## Pysyväistalletus

Pelaaja voi pelin alussa antaa tietokantaan nimensä, jos hän haluaa, että hänen tason läpäisyaikaennätyksensä tallennetaan tulostauluun.
