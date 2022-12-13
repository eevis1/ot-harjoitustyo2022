# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on rakennettu kolmeen tasoon ja seuraavassa kuvassa näkyy koodin pakkausrakenne:

![](/dokumentaatio/kuvat/Pakkauskaavio.png)

Pakkaukseen ui on sisällytetty käyttöliittymästä vastaava koodi, kun taas services vastaa sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta. Sovelluksen käyttämiä tietokohteita kuvastavat pakkauksen entities sisältämät luokat.


## Käyttöliittymä

Käyttöliittymä sisältää näkymät sisäänkirjautumiselle, uuden käyttäjän luomiselle ja kurssilistaukselle. Jokainen näistä on toteutettu omana luokkanaan ja niiden näyttämisestä vastaa UI-luokka


## Sovelluslogiikka

Luokat Student ja Course muodostavat sovelluksen loogisen tietomallin, nämä kuvaavat opiskelijoita ja heidän kurssejaan:

![](/dokumentaatio/kuvat/Sovelluslogiikka_1.png)

Luokka TodoService vastaa ohjelman toiminnallisista kokonaisuuksista ja tarjoaa erinäisiä metodeja. Se myös pääsee käsiksi opiskelijoihin ja kursseihin luokkien CourseRepository ja StudentRepository, jotka sijaitsevat pakkauksessa repositories.

CourseService-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![](/dokumentaatio/kuvat/Pakkaus_Sovelluskaavio.png)


## Päätoiminnallisuudet

### Kurssin lisääminen

Uuden kurssin lisäävän "Add"-painikkeen painamisen jälkeen sovelluksen kontrolli etenee seuraavan kaavion mukaisesti:

![](/dokumentaatio/kuvat/Sekvenssikaavio.png)

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodia add_course ja antaa sille parametriksi lisättävän kurssin tiedot. Sovelluslogiikka luo uuden Course-olion ja tallettaa sen kutsumalla CourseRepository:n metodia add. Tämän seurauksena käyttöliittymä päivittää näytettävät kurssit kutsumalla omaa metodiaan initialize_course_list.
