"""yksikkötestit Topic luokalle"""
import unittest
from entities.topic import Topic

class TestTopic(unittest.TestCase):
    def setUp(self):
        self.test_topic=Topic(topic="yhteenlasku")

    def test_topic_values(self):
        self.assertEqual(self.test_topic.topic, "yhteenlasku")

