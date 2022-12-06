"""yksikkötestit Result luokalle"""
import unittest
from entities.result import Result
from entities.user import User
from entities.task import Task


class TestResult(unittest.TestCase):
    def setUp(self):
        self.test_student = User(
            {"first_name": 'Tero', "last_name": 'Testi', "user_id": 'tt1', "passwd": 'xx'})
        self.test_task = Task({"topic_id": 1, "difficulty": 1, "question": "kysymys",
                              "correct": "oikea", "wrong1": "väärä1", "wrong2": "väärä2",
                               "wrong3": "väärä3", "task_id": 1})
        self.test_result = Result(
            person=self.test_student, task=self.test_task, result=True)
        unittest.TestCase.maxDiff = None

    def test_result_values(self):
        self.assertEqual(self.test_result.person, self.test_student)
        self.assertEqual(self.test_result.task, self.test_task)
        self.assertEqual(self.test_result.result, True)

    def test___repr__(self):
        self.assertEqual(self.test_result.__repr__(
        ), f"Result(User(Tero, Testi, tt1, xx, False), Task(1, 1, kysymys, oikea, väärä1, väärä2, väärä3, True)")

    def test___str__(self):
        self.assertEqual(self.test_result.__str__(), f"first_name: Tero, last_name: Testi, user_id: tt1, passwd: xx, teacher: False, "
                         f"topic_id: 1, difficulty: 1, question: kysymys, correct: oikea, "
                         f"wrong1: väärä1, wrong2: väärä2, wrong3: väärä3, True")
