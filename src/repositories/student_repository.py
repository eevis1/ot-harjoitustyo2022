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
        """
        return get_student_by_row()
   
    def create(self, student):
        """Tallentaa opiskelijan tietokantaan.
        """
        return student
