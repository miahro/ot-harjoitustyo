"""yksikkötestit TopicServicesluokalle"""
import unittest
from os.path import isfile
from config import DB_FILE, DB_FILE_PATH
from repositories.topic_repository import topicrepository
from services.topic_services import TopicServices, topicservices

class TestTopicServices(unittest.TestCase):
    def setUp(self):
        self.topicservices = TopicServices()
        self.topicservices.delete_all()
        self.topicservices.update_topics_db()

    def test_update_topics_db(self):
        self.topicservices.delete_all()
        result = self.topicservices.get_all_topics()
        self.assertEqual(result, [])
        self.topicservices.update_topics_db()
        result = self.topicservices.get_all_topics()
        self.assertTrue(len(result) > 0)

    def test_get_all_topics(self):
        result = self.topicservices.get_all_topics()
        self.assertEqual(
            result, ['yhteenlasku', 'vähennyslasku', 'kertolasku', 'jakolasku'])

    def test_set_active_topic(self):
        self.topicservices.set_active_topic("vähennyslasku")
        self.assertEqual(self.topicservices.active_topic,
                         self.topicservices.topicrepository.id_by_topic("vähennyslasku"))

    def test_return_active_topic(self):
        self.topicservices.active_topic = None
        self.assertEqual(
            self.topicservices.return_active_topic(), "aihetta ei valittu")
        self.topicservices.set_active_topic("yhteenlasku")
        self.assertEqual(
            self.topicservices.return_active_topic(), "yhteenlasku")

    def test_delete_all(self):
        self.assertTrue(len(self.topicservices.get_all_topics()) > 0)
        self.topicservices.delete_all()
        self.assertEqual(len(self.topicservices.get_all_topics()), 0)
