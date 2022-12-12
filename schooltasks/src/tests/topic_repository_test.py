"""yksikkötestit TopicRepository luokalle"""
import unittest
from os.path import isfile
from config import DB_FILE, DB_FILE_PATH
from dbcon import connection
from entities.user import User
#from repositories.user_repository import userrepository
from repositories.topic_repository import topicrepository


class TestTopicRepository(unittest.TestCase):
    def setUp(self):
        topicrepository.delete_all()

    def test_DB_exists(self):
        print(DB_FILE_PATH)
        self.assertEqual(isfile(DB_FILE_PATH), True)

    def test_table_exists(self):
         self.assertEqual(connection.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='Topics';").fetchone()[0], 1)
 

    def test_read_from_file(self):
        result = topicrepository.read_from_file()
        self.assertEqual(len(result) > 0, True)
        self.assertEqual(len(result[0]), 1)

    def test_add_topics(self):
        size0 = connection.execute(
            "SELECT COUNT(*) FROM Topics;").fetchone()[0]
        topicrepository.update_db([("testiaihe1",), ("testiaihe2",)])
        size1 = connection.execute(
            "SELECT COUNT(*) FROM Topics;").fetchone()[0]
        self.assertEqual(size1-size0, 2)

    def test_all_topics(self):
        topicrepository.update_db([("testiaihe1",), ("testiaihe2",)])
        result = topicrepository.all_topics()
        self.assertEqual(result, ["testiaihe1", "testiaihe2"])

    def test_id_by_topic(self):
        topicrepository.update_db([("testiaihe1",), ("testiaihe2",)])
        result = topicrepository.id_by_topic("testiaihe1")
        reference = connection.execute(
            "SELECT id FROM Topics WHERE topic='testiaihe1'").fetchone()[0]
        self.assertEqual(result, reference)

    def test_topic_by_id(self):
        topicrepository.update_db([("testiaihe1",), ("testiaihe2",)])
        tid = topicrepository.id_by_topic("testiaihe1")
        result = topicrepository.topic_by_id(tid)
        self.assertEqual(result, "testiaihe1")

    def test_topic_by_id_fail(self):
        topicrepository.update_db([("testiaihe1",), ("testiaihe2",)])
        result = topicrepository.topic_by_id(0)
        self.assertEqual(result, "")
