"""yksikkötestit ResultRepository luokalle"""
import unittest
from dbcon import connection
#from repositories.user_repository import userrepository
from repositories.result_repository import resultrepository


class TestTopicRepository(unittest.TestCase):
    def setUp(self):
        resultrepository.delete_all()

    def test_table_exists(self):
        #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Users';").fetchone()[0], 1)
        #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Topics';").fetchone()[0], 1)
        #    self.assertEqual(connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Tasks';").fetchone()[0], 1)
        self.assertEqual(connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Results';").fetchone()[0], 1)

    def test_add_result(self):
        size0 = connection.execute(
            "SELECT COUNT(*) FROM Results;").fetchone()[0]
        resultrepository.add_result(1, 1, False)
        size1 = connection.execute(
            "SELECT COUNT(*) FROM Results;").fetchone()[0]
        self.assertEqual(size1-size0, 1)
