from entities.student import Student

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

"""student_repository = StudentRepository(get_database_connection())"""
