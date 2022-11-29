# Vaatimusmäärittely

## Sovelluksen tarkoitus

Opintojen seurantajärjestelmä antaa käyttäjälle mahdollisuuden pitää kirjaa jo suoritetuista ja vielä suorittamatta olevista kursseista. Sovellusta voi käyttää useampi käyttäjä omien profiiliensa kautta, jolloin myös kurssilistat ovat yksilöllisiä.


## Käyttäjät

Sovelluksella on kaksi käyttäjäroolia, toinen on normaali käyttäjä eli opiskelija ja toinen on suuremmilla oikeuksilla varustettu opettaja, joka voi lisätä opiskelijoiden arvosanoja järjestelmään.


## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjän täytyy luoda järjestelmään käyttäjätunnus
  - Käyttäjätunnusten täytyy olla uniikkeja ja pituudeltaan vähintään 3 merkkiä
- Käyttäjä käyttää käyttäjätunnusta kirjaututuakseen järjestelmään
  - Kirjautuminen tapahtuu syötettämällä käyttäjätunnuksen ja salasanan kirjautumislomakkeelle
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, järjestelmä ilmoittaa tästä


### Kirjautumisen jälkeen

- Käyttäjä näkee omat käydyt ja käymättömät kurssinsa, sekä niiden arvosanat
- Käyttäjä voi lisätä kursseja "tehty"
  - Lisätyt kurssit näkyvät vain ne lisänneelle käyttäjälle
- Käyttäjä voi merkitä kurssin suoritetuksi, jolloin kurssi siirtyy suoritettujen kurssien joukkoon
- Käyttäjä voi kirjautua ulos sovelluksesta


## Jatkokehitysideoita

Perusversion jälkeen sovellusta voidaan jatkaa, jos aikaa riittää muun muassa seuraavilla toiminnallisuuksilla:

- Jo suoritettujen kurssien lähempi tarkastelu
- Tehdyksi merkittyjen kurssien merkitseminen takaisin tekemättömäksi
- Jo lisättyjen kurssien editoiminen
- Kurssien ajoittaminen
- Lisätään kurssiin kenttä, johon on mahdollista merkitä kurssiin liittyviä tarkempia tietoja
- Käyttäjätunnuksen ja siihen liittyvien kurssien poisto

