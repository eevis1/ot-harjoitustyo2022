# Ohjelmistotekniikka, harjoitustyö

## Opintojen seurantajärjestelmä


Tämä on **Ohjelmistotekniikan** *harjoitustyö*. Opintojen seurantajärjestelmä antaa käyttäjälle mahdollisuuden pitää kirjaa jo suoritetuista ja vielä suorittamatta olevista kursseista.


### Dokumentaatio

- [Release](https://github.com/eevis1/ot-harjoitustyo2022/releases/tag/viikko6)

- [Arkkitehtuurikuvaus](https://github.com/eevis1/ot-harjoitustyo2022/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Vaatimusmäärittely](https://github.com/eevis1/ot-harjoitustyo2022/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Tuntikirjanpito](https://github.com/eevis1/ot-harjoitustyo2022/blob/master/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/eevis1/ot-harjoitustyo2022/blob/master/dokumentaatio/changelog.md)

- [Käyttöohje](https://github.com/eevis1/ot-harjoitustyo2022/blob/master/dokumentaatio/kayttoohje.md)


### Asennus

1. Riippuvuuksien asennus komennolla: *poetry install*
2. Pip täytyy olla asennettuna, jotta voidaan asentaa dotenv komennolla: *pip3 install python-dotenv*
3. Sovelluksen käynnistäminen komennolla: *poetry run invoke start*


### Komentorivitoiminnot

1. Ohjelman suorittaminen komennolla: *poetry run invoke start*
2. Testien suorittaminen komennolla: *poetry run invoke test*
3. Testikattavuusraportin generoiminen komennolla: *poetry run invoke coverage-report*
4. Tiedoston .pylintrc määrittelemien tarkistuksien suorittaminen komennolla: *poetry run invoke lint*
