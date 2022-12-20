# Testausdokumentti

Ohjelman testaus on suoritettu automatisoiduin yksikkö- ja integraatiotestein unittestilla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

TestCourseService-testiluokalla testataan sovelluslogiikasta vastaavaa CourseService-luokkaa. CourseService-olio alustetaan ensin injektoimalla sille riippuvuksiksi repositorio-olio, joka tallentaa tietoa muistiin pysyväistallennuksen sijaan. Tätä varten testissä on käytössä luokka FakeCourseRepository. 

### Repositorio-luokka

CourseRepository-luokkaa testataan TestCourseRepository-testiluokalla.
