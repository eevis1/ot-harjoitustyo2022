class CourseRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def all_courses(self):
        return self._read()