# Kummituspeli

## Kuvaus

Kummituspelissä pelaaja hallitsee kummitusta, joka seikkailee pelitason läpi. Hän voi kerätä 2D-tasosta lusikoita, jotka kasvattavat kummituksen liikenopeutta: myös tarpeeksi kerättyään hän saa niistä lisäelämiä. Liikkuminen 
tapahtuu W- A- ja D-näppäimillä. Kun pääset tason uloskäynnille, voitat pelin!

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/smausquared/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/smausquared/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/smausquared/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/smausquared/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/smausquared/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

Kummitus-kuvaa käytetään tekijän Erkki Rytkönen luvalla, Twitter @finnytalks

## Asennus

**Huom!** Tietokoneellasi täytyy olla poetry asennettuna, jotta asennus onnistuu!

1. Lataa uusin release ja pura zip-tiedosto

2. Navigoi komentorivillä purkamaasi kansioon "ot-harjoitustyo"

3. Suorita seuraava komento: 
```bash
poetry install
```

4. Alusta tallennuksen tietokanta komennolla:
```bash
poetry run invoke build
```

5. Aja ohjelma seuraavalla komennolla:
```bash
poetry run invoke start
```

## Komennot

Tietokannan alustus:
```bash
poetry run invoke build
```


Ohjelman ajo:

```bash
poetry run invoke start
```

~~Testien ajo~~ rikki, coverage ajaa testit toimivasti:

```bash
poetry run invoke test
```

Testaaminen ja testikattavuusraportin luonti index.html-tiedostoon:

```bash
poetry run invoke coverage-report
```

Pylint-virheiden tarkistus:

```bash
poetry run invoke lint
```

## Huomioita

Tänään palautuspäivänä labtool on alhaalla. Näin en ole voinut muuttaa projektin nimeä labtoolissa!

Pylint antaa ainakin minun koneella false-positiveja trailing whitespacesta. Muut pylint-virheet tunnustan!
