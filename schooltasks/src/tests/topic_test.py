"""yksikkötestit Topic luokalle"""
import unittest
from entities.topic import Topic


class TestTopic(unittest.TestCase):
    def setUp(self):
        self.test_topic = Topic(topic="yhteenlasku")

    def test_topic_values(self):
        self.assertEqual(self.test_topic.topic, "yhteenlasku")

    def test___repr__(self):
        self.assertEqual(self.test_topic.__repr__(), f"Topic(yhteenlasku)")

    def test___str__(self):
        self.assertEqual(self.test_topic.__str__(), "yhteenlasku")
