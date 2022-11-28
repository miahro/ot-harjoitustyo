"""yksikkötestit User luokalle"""
import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_student = User(
            first_name='Tero', last_name='Testi', user_id='tt1', passwd='xx')
        self.test_teacher = User(
            first_name='Olli', last_name='Ope', user_id='maikka', passwd='yy', teacher=True)

    def test_student_values(self):
        self.assertEqual(self.test_student.first_name, "Tero")
        self.assertEqual(self.test_student.last_name, "Testi")
        self.assertEqual(self.test_student.user_id, "tt1")
        self.assertEqual(self.test_student.passwd, "xx")
        self.assertEqual(self.test_student.teacher, False)

    def test_teacher_values(self):
        self.assertEqual(self.test_teacher.first_name, "Olli")
        self.assertEqual(self.test_teacher.last_name, "Ope")
        self.assertEqual(self.test_teacher.user_id, "maikka")
        self.assertEqual(self.test_teacher.passwd, "yy")
        self.assertEqual(self.test_teacher.teacher, True)
