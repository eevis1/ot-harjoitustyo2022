from entities.course import Course

from repositories.course_repository import (
    CourseRepository as default_course_repository
)

class CourseService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(
        self,
        course_repository=default_course_repository,
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        Args:
            course_repository:
                Vapaaehtoinen, oletusarvoltaan CourseRepository-olio.
                Olio, jolla on CourseRepository-luokkaa vastaavat metodit.
        """
        self._course_repository = course_repository

    def add_course(self, name):
        """Lisää kurssin.
        Args:
            content: Merkkijonoarvo, joka kertoo kurssin nimen.
        Returns:
            Lisätty kurssi Course-olion muodossa.
        """

        course = Course(name=name)

        return self._course_repository.add_course(course)

    def get_undone_courses(self):
        """Palauttaa suorittamattomat kurssit.
        Returns:
            Palauttaa suorittamattomat kurssit Course-olioden listana.
        """

        courses = self._course_repository.all_courses(self)
        undone_courses = filter(lambda course: not course.done, courses)

        return list(undone_courses)

    def set_course_done(self, course_id):
        """Merkitsee kurssin suoritetuksi.
        Args:
            course_id: Merkkijonoarvo, joka kuvaa kurssin id:tä.
        """

        self._course_repository.set_done(course_id)

course_service = CourseService()
