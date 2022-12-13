"""yksikkötestit ResultRepository luokalle"""
import unittest
from dbcon import connection
from repositories.result_repository import resultrepository


class TestResultRepository(unittest.TestCase):
    def setUp(self):
        resultrepository.delete_all()
        resultrepository.add_result(1, 2, False)
        resultrepository.add_result(1, 3, True)
        resultrepository.add_result(1, 4, False)
        resultrepository.add_result(1, 5, True)
        resultrepository.add_result(1, 6, True)

    def test_table_exists(self):
        self.assertEqual(connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Results';").fetchone()[0], 1)

    def test_add_result(self):
        size0 = connection.execute(
            "SELECT COUNT(*) FROM Results;").fetchone()[0]
        resultrepository.add_result(1, 1, False)
        size1 = connection.execute(
            "SELECT COUNT(*) FROM Results;").fetchone()[0]
        self.assertEqual(size1-size0, 1)

    def test_get_user_total_correct(self):
        result = resultrepository.get_user_total_correct(1)
        self.assertEqual(result[0], 3)

    def test_get_user_total_false(self):
        result = resultrepository.get_user_total_fail(1)
        self.assertEqual(result[0], 2)

    def test_get_user_all_correct(self):
        result = resultrepository.get_user_all_correct(1)
        self.assertEqual(result[0], ('yhteenlasku',1,3))

    def test_get_user_all_false(self):
        result = resultrepository.get_user_all_false(1)
        self.assertEqual(result[0], ('yhteenlasku',1,2))
