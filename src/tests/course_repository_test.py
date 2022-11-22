import unittest
from course_repository import CourseRepository

class TestCourseRepository(unittest.TestCase):
    def setUp(self):
        self.courserepository = CourseRepository()

    def test_courserepository_exists(self):
        self.assertNotEqual(self.courserepository, None)