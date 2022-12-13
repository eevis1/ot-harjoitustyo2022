from entities.course import Course
from entities.student import Student


from repositories.course_repository import (
    CourseRepository as default_course_repository
)

from repositories.student_repository import (
    StudentRepository as default_student_repository
)

class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass

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

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.
        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä Student-olion muodossa.
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää.
        """

        student = self._student_repository.find_by_username(username)

        if not student or student.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._student = student

        return student

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.
        Args:
            username: Merkkijonoarvo, joka kuvastaa opiskelijan käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa opiskelijan salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.
        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.
        Returns:
            Luotu käyttäjä Student-olion muodossa.
        """

        existing_user = self._student_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        student = self._student_repository.create(Student(username, password))

        if login:
            self._student = student

        return student


course_service = CourseService()
