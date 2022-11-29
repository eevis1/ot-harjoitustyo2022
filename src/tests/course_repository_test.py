import unittest
from repositories.course_repository import CourseRepository
from entities.course import Course


class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        CourseRepository.delete_all_courses()
        self.course_1 = Course('test 1')
        self.course_2 = Course('test 2')

    def test_courserepository_exists(self):
        self.assertNotEqual(self.CourseRepository, None)

    def test_all_courses(self):
        CourseRepository.add_course(self.course_1)
        CourseRepository.add_course(self.course_1)
        courses = CourseRepository.all_courses()

        self.assertEqual(len(courses), 2)
        self.assertEqual(courses[0].content, self.course_1.content)
        self.assertEqual(courses[1].content, self.course_2.content)

    def test_add(self):
        CourseRepository.add_course(self.course_1)
        courses = CourseRepository.all_courses()

        self.assertEqual(len(courses), 1)
        self.assertEqual(courses[0].content, self.course_1.content)
