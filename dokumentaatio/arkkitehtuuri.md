# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on rakennettu kolmeen tasoon ja seuraavassa kuvassa näkyy koodin pakkausrakenne:

![](/dokumentaatio/kuvat/Pakkauskaavio.png)

Pakkaukseen ui on sisällytetty käyttöliittymästä vastaava koodi, kun taas services vastaa sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta. Sovelluksen käyttämiä tietokohteita kuvastavat pakkauksen entities sisältämät luokat.

## Sovelluslogiikka

Luokat Student ja Course muodostavat sovelluksen loogisen tietomallin, nämä kuvaavat opiskelijoita ja heidän kurssejaan:

![](/dokumentaatio/kuvat/Sovelluslogiikka_1.png)

Luokka TodoService vastaa ohjelman toiminnallisista kokonaisuuksista ja tarjoaa erinäisiä metodeja. Se myös pääsee käsiksi opiskelijoihin ja kursseihin luokkien CourseRepository ja StudentRepository, jotka sijaitsevat pakkauksessa repositories.

CourseService-luokan ja ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![](/dokumentaatio/kuvat/Pakkaus_Sovelluskaavio.png)
