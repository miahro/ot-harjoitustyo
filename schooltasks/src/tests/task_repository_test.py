"""yksikkötestit TaskRepository luokalle"""
import unittest
from dbcon import connection
#from repositories.user_repository import userrepository
from repositories.task_repository import taskrepository

class TestTopicRepository(unittest.TestCase):
    def setUp(self):
        taskrepository.delete_all()


    def test_table_exists(self):
    #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Users';").fetchone()[0], 1)
    #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Topics';").fetchone()[0], 1)
        self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Tasks';").fetchone()[0], 1)
    #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Results';").fetchone()[0], 1)        

    def test_read_from_file(self):
        taskrepository.delete_all
        result = taskrepository.read_from_file()
        self.assertEqual(len(result)>0, True)


    def test_update_db(self):
        tasks = [[1,1,"kysymys", "oikea", "väärä1", "väärä2", "väärä3"]]
        size0 = connection.execute("SELECT COUNT(*) FROM Tasks;").fetchone()[0]
        taskrepository.update_db(tasks) 
        size1 = connection.execute("SELECT COUNT(*) FROM Tasks;").fetchone()[0]

