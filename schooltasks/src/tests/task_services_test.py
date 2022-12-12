"""yksikkötestit TaskServices luokalle"""
import unittest
from dbcon import connection
#from repositories.task_repository import taskrepository
from services.task_services import TaskServices, taskservices

class TestTaskServices(unittest.TestCase):
    def setUp(self):
        self.taskservices = TaskServices()
        self.taskservices.update_tasks_db()

    def test_get_tasks(self):
        tasks = self.taskservices.get_tasks(topic_id=3, difficulty=2, pcs=5)
        self.assertEqual(len(tasks),5)
        for task in tasks:
            self.assertEqual(task.topic_id, 3)
            self.assertEqual(task.difficulty, 2)

    def test_return_min_difficulty(self):
        self.assertEqual(self.taskservices.return_min_difficulty(), 1)
        

    def test_return_max_difficulty(self):
        self.assertEqual(self.taskservices.return_max_difficulty(), 10)


    def test_return_difficulty_range(self):
        self.assertEqual(self.taskservices.return_difficulty_range(), [1,2,3,4,5,6,7,8,9,10])

    def test_return_active_difficulty_str_not_selected(self):
        self.taskservices.active_difficulty = None
        self.assertEqual(self.taskservices.return_active_difficulty_str(),"vaikeustasoa ei valittu")


    def test_return_active_difficulty_str(self):
        self.taskservices.set_active_difficulty(difficulty=3)
        self.assertEqual(self.taskservices.return_active_difficulty_str(),"3")

    def test_set_active_difficulty(self):
        self.assertIsNone(self.taskservices.active_difficulty)
        self.taskservices.set_active_difficulty(difficulty=2)
        self.assertEqual(self.taskservices.active_difficulty, 2)





