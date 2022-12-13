from entities.student import Student

def get_student_by_row(row):
    return Student(row["username"], row["password"]) if row else None


class StudentRepository:
    """Opiskelijoihin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, file_path):
        """Luokan konstruktori.
        Args:
            connection: Tietokantayhteyden Connection-olio
        """
        self._file_path = file_path
        """self._connection = connection"""

    def find_by_username(self, username):
        """Palauttaa opiskelijan käyttäjätunnuksen perusteella.
        Args:
            username: Käyttäjätunnus, jonka käyttäjä palautetaan.
        Returns:
            Palauttaa Student-olion, jos käyttäjätunnuksen omaava opiskelija on tietokannassa.
            Muussa tapauksessa None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            (username,)
        )

        row = cursor.fetchone()

        return get_student_by_row(row)
   
    def create(self, student):
        """Tallentaa opiskelijan tietokantaan.
        Args:
            course: Tallennettava opiskelija Student-oliona.
        Returns:
            Tallennettu opiskelija Student-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            (student.username, student.password)
        )

        self._connection.commit()

        return student

"""student_repository = StudentRepository(get_database_connection())"""
