"""yksikkötestit Result luokalle"""
import unittest
from entities.result import Result
from entities.user import User
from entities.task import Task


class TestResult(unittest.TestCase):
    def setUp(self):
        self.test_student = User(
            first_name='Tero', last_name='Testi', user_id='tt1', passwd='xx')
        self.test_task = Task({"topic_id": 1, "difficulty": 1, "question": "kysymys",
                              "correct": "oikea", "wrong1": "väärä1", "wrong2": "väärä2", "wrong3": "väärä3"})
        self.test_result = Result(
            person=self.test_student, task=self.test_task, result=True)

    def test_result_values(self):
        self.assertEqual(self.test_result.person, self.test_student)
        self.assertEqual(self.test_result.task, self.test_task)
        self.assertEqual(self.test_result.result, True)
