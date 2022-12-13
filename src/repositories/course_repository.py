from pathlib import Path
from entities.course import Course


class CourseRepository:
    """Kursseihin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, file_path):
        """Luokan konstruktori.
        Args:
            file_path: Polku tiedostoon, johon kurssit tallennetaan.
        """
        self._file_path = file_path

    def all_courses(self):
        """Palauttaa kaikki kurssit.
        Returns:
            Palauttaa listan Course-olioita.
        """
        return self._read()

    def add_course(self, course):
        """Tallentaa kurssin tietokantaan.
        Args:
            course: Tallennettava tehtävä Course-oliona.
        Returns:
            Tallennettu tehtävä Course-oliona.
        """
        courses = self.all_courses()
        courses.append(course)
        self._write(courses)
        return course

    def set_done(self, course_id, done=True):
        """Asettaa kurssin suoritettu-statuksen.
        Args:
            course_id: Kurssin id, jonka suoritettu-status muutetaan.
            done:
                Vapaaehtoinen, oletusarvo True.
                Boolean-arvo, joka asetetaan kurssin suoritettu-statukseksi.
        """

        courses = self.all_courses()

        for course in courses:
            if course.id == course_id:
                course.done = done
                break

        self._write(courses)

    def delete_all_courses(self):
        """Poistaa kaikki kurssit.
        """
        self._write([])

    def _ensure_file_exists(self):
        Path(self._file_path).touch()


    def _read(self):
        courses = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                course_id = parts[0]
                content = parts[1]

                courses.append(
                    Course(content, course_id)
                )

        return courses

    def _write(self, courses):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for course in courses:

                row = f"{course.id};{course.content}"

                file.write(row+"\n")
