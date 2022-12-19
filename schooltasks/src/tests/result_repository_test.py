"""yksikkötestit ResultRepository luokalle"""
import unittest
import os
from dbcon import connection
from question_generator import QuestionGenerator
from config import TASKS_INPUT_PATH
from repositories.result_repository import ResultRepository
from repositories.user_repository import  UserRepository
from repositories.topic_repository import TopicRepository
from entities.user import User

class TestResultRepository(unittest.TestCase):
    def setUp(self):
        if os.path.isfile(TASKS_INPUT_PATH):
            os.remove(TASKS_INPUT_PATH)
        self.test_question_generator = QuestionGenerator()
        self.test_question_generator.populate_csv()

        testuser = User({"first_name": "Tero",
                        "last_name": "Testi",
                        "user_id": "tt1",
                        "passwd": "sala",
                        "teacher": False})
        self.userrepository = UserRepository()
        self.userrepository.add_user(testuser)
        self.person_id = self.userrepository.get_pk_id("tt1")[0]

        self.topicrepository = TopicRepository()
        topics = [("yhteenlasku",), ("vähennyslasku",), ("kertolasku", ), ("jakolasku",)]
        self.topicrepository.update_db(topics)


        self.resultrepository = ResultRepository()
        self.resultrepository.delete_all()
        self.resultrepository.add_result(self.person_id, 2, False)
        self.resultrepository.add_result(self.person_id, 3, True)
        self.resultrepository.add_result(self.person_id, 4, False)
        self.resultrepository.add_result(self.person_id, 5, True)
        self.resultrepository.add_result(self.person_id, 6, True)

    def test_table_exists(self):
        self.assertEqual(connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Results';").fetchone()[0], 1)

    def test_add_result(self):
        size0 = connection.execute(
            "SELECT COUNT(*) FROM Results;").fetchone()[0]
        self.resultrepository.add_result(1, 1, False)
        size1 = connection.execute(
            "SELECT COUNT(*) FROM Results;").fetchone()[0]
        self.assertEqual(size1-size0, 1)

    def test_get_user_total_correct(self):
        result = self.resultrepository.get_user_total_correct(self.person_id)
        self.assertEqual(result[0], 3)

    def test_dummy(self):
        self.assertEqual(self.person_id, 1)

    def test_get_user_total_false(self):
        result = self.resultrepository.get_user_total_fail(self.person_id)
        self.assertEqual(result[0], 2)

    def test_get_user_all_correct(self):
        result = self.resultrepository.get_user_all_correct(self.person_id)
        if result:
            self.assertEqual(result[0], ('yhteenlasku', 1, 3))

    def test_get_user_all_false(self):
        result = self.resultrepository.get_user_all_false(self.person_id)
        if result:
            self.assertEqual(result[0], ('yhteenlasku', 1, 2))
