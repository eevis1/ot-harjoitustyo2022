import unittest
from repositories.course_repository import course_repository
from entities.course import Course


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        course_repository.delete_all_courses()

        self.course_1 = Course('test 1')
        self.course_2 = Course('test 2')

    def test_add_course(self):
        course_repository.add_course(self.course_1)
        courses = course_repository.all_courses()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].name, self.course_1.name)

    def test_all_courses(self):
        course_repository.add_course(self.course_1)
        course_repository.add_course(self.course_2)
        courses = course_repository.all_courses()

        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0].name, self.course_1.name)
        self.assertEqual(courses[1].name, self.course_2.name)

    def test_set_done(self):
        added_course = course_repository.add_course(self.course_1)
        courses = course_repository.all_courses()

        self.assertEqual(courses[0].done, False)

        course_repository.set_done(added_course.id)

        courses = course_repository.all_courses()

        self.assertEqual(courses[0].done, True)
     
    def test_delete(self):
        added_course = course_repository.add_course(self.course_1)
        courses = course_repository.all_courses()

        self.assertEqual(len(courses), 1)

        course_repository.delete(added_course.id)

        courses = course_repository.all_courses()

        self.assertEqual(len(courses), 0)
