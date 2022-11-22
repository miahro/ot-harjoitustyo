"""yksikkötestit Task luokalle"""
import unittest
from entities.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.test_task=Task(topic_id=1, difficulty=1, question="kysymys", correct="oikea", wrong1="väärä1", wrong2="väärä2", wrong3="väärä3")

    def test_task_values(self):
        self.assertEqual(self.test_task.topic_id,1)
        self.assertEqual(self.test_task.difficulty,1)
        self.assertEqual(self.test_task.question,"kysymys")
        self.assertEqual(self.test_task.correct,"oikea")
        self.assertEqual(self.test_task.wrong1,"väärä1")
        self.assertEqual(self.test_task.wrong2,"väärä2")
        self.assertEqual(self.test_task.wrong3,"väärä3")


