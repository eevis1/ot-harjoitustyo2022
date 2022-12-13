from entities.course import Course


from repositories.course_repository import (
    CourseRepository as default_course_repository
)

from repositories.student_repository import (
    StudentRepository as default_student_repository
)


class CourseService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(
        self,
        course_repository=default_course_repository,
        student_repository=default_student_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.
        Args:
            course_repository:
                Vapaaehtoinen, oletusarvoltaan CourseRepository-olio.
                Olio, jolla on CourseRepository-luokkaa vastaavat metodit.
            student_repository:
                Vapaaehtoinen, oletusarvoltaan StudentRepository-olio.
                Olio, jolla on StudentRepository-luokkaa vastaavat metodit.
        """
        self._student = None
        self._course_repository = course_repository
        self._student_repository = student_repository

    def add_course(self, content):
        """Lisää kurssin.
        Args:
            content: Merkkijonoarvo, joka kuvaa kurssin sisältöä.
        Returns:
            Lisätty kurssi Course-olion muodossa.
        """

        course = Course(content=content, student=self._student)

        return self._course_repository.create(course)


    def set_course_done(self, course_id):
        """Merkitsee kurssin suoritetuksi.
        Args:
            course_id: Merkkijonoarvo, joka kuvaa kurssin id:tä.
        """

        self._course_repository.set_done(course_id)


course_service = CourseService()
