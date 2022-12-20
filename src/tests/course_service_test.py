import unittest
from entities.course import Course
from services.course_service import (
    CourseService
)


class FakeCourseRepository:
    def __init__(self, courses=None):
        self.courses = courses or []

    def all_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)

        return course

    def set_done(self, course_id, done=True):
        for course in self.courses:
            if course.id == course_id:
                course.done = done
                break

    def delete(self, course_id):
        courses_without_id = filter(lambda course: course.id != course_id, self.courses)

        self.courses = list(courses_without_id)

    def delete_all(self):
        self.courses = []


class TestCourseService(unittest.TestCase):
    def setUp(self):
        self.course_service = CourseService(
            FakeCourseRepository()
        )

        self.course_1 = Course('test 1')
        self.course_2 = Course('test 2')

    def test_add_course(self):

        self.course_service.add_course('testing')
        courses = self.course_service.get_undone_courses()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, 'testing')

    def test_get_undone_courses(self):

        self.course_service.add_course(self.course_1.name)

        added_course_2 = self.course_service.add_course(self.course_2.name)

        self.course_service.set_course_done(added_course_2.id)

        undone_courses = self.course_service.get_undone_courses()

        self.assertEqual(len(undone_courses), 1)
        self.assertEqual(undone_courses[0].name, self.course_1.name)

    def test_set_course_done(self):

        self.course_service.add_course('testing')

        undone_courses = self.course_service.get_undone_courses()

        self.assertEqual(len(undone_courses), 1)

        self.course_service.set_course_done(undone_courses[0].id)

        undone_courses = self.course_service.get_undone_courses()

        self.assertEqual(len(undone_courses), 0)
