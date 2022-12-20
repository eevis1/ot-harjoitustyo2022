# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on rakennettu kolmeen tasoon ja seuraavassa kuvassa näkyy koodin pakkausrakenne:

![](/dokumentaatio/kuvat/Pakkauskaavio.png)

Pakkaukseen ui on sisällytetty käyttöliittymästä vastaava koodi, kun taas services vastaa sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta. Sovelluksen käyttämiä tietokohteita kuvastavat pakkauksen entities sisältämät luokat.


## Käyttöliittymä

Käyttöliittymä sisältää näkymän kurssilistaukselle. Tämä on toteutettu omana luokkanaan ja sen näyttämisestä vastaa UI-luokka


## Sovelluslogiikka

Luokka Course muodostaa sovelluksen loogisen tietomallin, tämä kuvaa opiskelijan kursseja:

![](/dokumentaatio/kuvat/Sovelluslogiikka_2.png)

Luokka TodoService vastaa ohjelman toiminnallisista kokonaisuuksista ja tarjoaa erinäisiä metodeja. Näitä ovat esimerkiksi:
- get_undone_courses()
- add_course(name)
- set_course_done(course_id)

Se myös pääsee käsiksi kursseihin luokan CourseRepository välityksellä, joka sijaitsee pakkauksessa repositories.

CourseService-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![](/dokumentaatio/kuvat/Pakkaus_Sovelluskaavio_1.png)


## Tietojen pysyväistallennus

Pakkauksen repositories luokka CourseRepository huolehtii tietojen tallettamisesta. TodoRepository-luokka tallentee tietoa CSV-tiedostoon.

### Tiedostot

Sovelluksen juureen on sijoitettu konfiguraatiotiedosto .env, joka määrittelee tiedoston nimen.

Sovellus tallettaa kurssit CSV-tiedostoon seuraavassa formaatissa: kurssin id, kurssin nimi, tehtystatus (0 = ei tehty, 1 = tehty) ja kenttien arvot erotetaan puolipisteellä (;).


## Päätoiminnallisuudet

### Kurssin lisääminen

Uuden kurssin lisäävän "Add"-painikkeen painamisen jälkeen sovelluksen kontrolli etenee seuraavan kaavion mukaisesti:

![](/dokumentaatio/kuvat/Sekvenssikaavio.png)

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodia add_course ja antaa sille parametriksi lisättävän kurssin tiedot. Sovelluslogiikka luo uuden Course-olion ja tallettaa sen kutsumalla CourseRepositoryn metodia add. Tämän seurauksena käyttöliittymä päivittää näytettävät kurssit kutsumalla omaa metodiaan initialize_course_list.

