from entities.course import Course


from repositories.course_repository import (
    course_repository as default_course_repository
)

from repositories.student_repository import (
    student_repository as default_student_repository
)


class CourseService:

    def __init__(
        self,
        course_repository=default_course_repository,
        student_repository=default_student_repository
    ):

        self._student = None
        self._course_repository = course_repository
        self._student_repository = student_repository

    def add_course(self, content):

        course = Course(content=content, student=self._student)

        return self._course_repository.create(course)


    def set_course_done(self, course_id):

        self._course_repository.set_done(course_id)


course_service = CourseService()