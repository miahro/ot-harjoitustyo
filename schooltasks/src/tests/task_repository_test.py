"""yksikkötestit TaskRepository luokalle"""
import unittest
from dbcon import connection
from repositories.task_repository import taskrepository


class TestTaskRepository(unittest.TestCase):
    def setUp(self):
        taskrepository.delete_all()

    def test_table_exists(self):
        self.assertEqual(connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Tasks';").fetchone()[0], 1)

    def test_read_from_file(self):
        taskrepository.delete_all
        result = taskrepository.read_from_file()
        self.assertEqual(len(result) > 0, True)

    def test_update_db(self):
        tasks = [[1, 1, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
        size0 = connection.execute("SELECT COUNT(*) FROM Tasks;").fetchone()[0]
        taskrepository.update_db(tasks)
        size1 = connection.execute("SELECT COUNT(*) FROM Tasks;").fetchone()[0]
        self.assertEqual(size1-size0, 1)
        taskrepository.delete_all()

    def test_max_difficulty(self):
        task = [[1, 1, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
        task2 = [[1, 10, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
        taskrepository.update_db(task)
        taskrepository.update_db(task2)
        self.assertEqual(taskrepository.max_difficulty(), 10)
        taskrepository.delete_all()

    def test_min_difficulty(self):
        task = [[1, 1, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
        task2 = [[1, 9, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
        taskrepository.update_db(task)
        taskrepository.update_db(task2)
        self.assertEqual(taskrepository.min_difficulty(), 1)
        taskrepository.delete_all()

    def test_get_random_task_list(self):
        for i in range(10):
            task = [[1, 1, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
            task2 = [[1, 2, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
            task3 = [[1, 1, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
            task4 = [[2, 2, "kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
            taskrepository.update_db(task)
            taskrepository.update_db(task2)
            taskrepository.update_db(task3)
            taskrepository.update_db(task4)
       
        result = taskrepository.get_random_task_list(1, 1, 5)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].topic_id, 1)
        self.assertEqual(result[0].difficulty, 1)

        result = taskrepository.get_random_task_list(2, 2, 5)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].topic_id, 2)
        self.assertEqual(result[0].difficulty, 2)
        taskrepository.delete_all()
