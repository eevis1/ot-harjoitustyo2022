class CourseRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def all_courses(self):
        return self._read()

    def add_course(self, course):
        courses = self.all_courses()
        courses.append(course)
        self._write(courses)
        return course
